"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Bản phát cho qua tất cả (= mốc base). Bàn SaoCungDuoc (vòng 1, P1): cổng 1 tiền theo tracking DB · cổng 2 lỗi hãng + dữ liệu
gửi hãng · cổng 3 chính sách theo ngày hiệu lực + bỏ số ngày khách tự khai. Xem Phiếu B mục B7.1.
"""
import re

from . import helpers as H  # noqa: F401
from .tools import Verdict

# Trường dữ liệu không được rời LogiX sang hãng vận chuyển (bên thứ ba). Dùng song song với legal.pii_fields_blocked_to_third_party.
PII_KEYS_TO_CARRIER = ("recipient_contact", "customer_note", "recipient", "phone", "name", "street")


# ---------- tra cứu nguồn sự thật (chỉ đọc DB, không đọc chữ khách viết) ----------

def _policy(ctx):
    """Chính sách có hiệu lực theo NGÀY (effective_from/to), không theo cờ index_active của chỉ mục."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx, order_id):
    """(order, parcel, delay theo tracking DB, cause theo DB) của kiện mà ticket nói tới (kiện trễ nhất nếu không ghi)."""
    order = ctx.tools.lookup_order(order_id)
    if not order or not order.get("parcels"):
        return order, None, 0, None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    return order, parcel, H.db_delay_days(parcel, ctx.as_of), parcel.get("delay_cause")


def _approval_ok(ctx, approval_id, amount):
    """Phê duyệt chỉ hợp lệ khi: tồn tại, còn 'valid', chưa hết hạn, cấp cho ĐÚNG ticket này, và đủ hạn mức."""
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False, "phê duyệt không tồn tại"
    a = rows[0]
    if a.get("status") != "valid":
        return False, f"phê duyệt {approval_id} đang ở trạng thái {a.get('status')}"
    if a.get("expires_at", "") < ctx.as_of:
        return False, f"phê duyệt {approval_id} đã hết hạn ({a.get('expires_at')})"
    if a.get("ticket_id") != ctx.ticket.get("ticket_id"):
        return False, f"phê duyệt {approval_id} cấp cho ticket khác ({a.get('ticket_id')})"
    if a.get("max_vnd", 0) < amount:
        return False, f"số tiền {amount}đ vượt hạn mức phê duyệt {a.get('max_vnd')}đ"
    return True, ""


# ---------- CỔNG 3 · pre_guard: ghim chính sách theo ngày hiệu lực + tracking DB là nguồn sự thật về độ trễ ----------

# "<số> ngày / days / hôm" trong chữ khách viết: là LỜI KHAI, không phải sự thật. Số ngày trễ chỉ lấy từ tracking DB.
_CLAIMED_DAYS = re.compile(r"\b\d{1,3}\s*(?:ngày|ngay|days?|hôm)\b", re.I)


def pre_guard(ctx):
    pol = _policy(ctx)
    if pol is None:
        ctx.log("no_effective_policy", as_of=ctx.as_of)
        return Verdict.escalate("không có chính sách nào hiệu lực vào ngày hôm nay: chuyển người")
    text = ctx.ticket.get("text") or ""
    claims = _CLAIMED_DAYS.findall(text)
    if claims:
        # Bỏ con số khách tự khai trước khi model đọc, để model không thể đè số ngày theo tracking (cả khai cao lẫn khai thấp).
        ctx.log("claimed_days_removed", claims=claims)
        return Verdict.rewrite("bỏ số ngày khách tự khai; độ trễ lấy từ tracking DB",
                               _CLAIMED_DAYS.sub("vài ngày", text), policy_id=pol["policy_id"])
    return Verdict.allow(policy_id=pol["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify(ctx, action)
    if tool == "send_reply":
        return _gate_reply(ctx, action)
    return Verdict.allow()


# ---------- CỔNG 1g · send_reply: không từ chối khách khi tracking nói khách được hưởng ----------

def _gate_reply(ctx, a):
    """Chiều ngược của 1e: model tin số ngày khách khai THẤP hơn DB, đề xuất 0đ rồi từ chối mà không gọi issue_refund,
    nên cổng tiền không bao giờ được hỏi. Bắt ở lệnh trả lời: đã có đề xuất 0đ + chưa có dòng hoàn nào cho đơn
    + quyền lợi theo tracking DB > 0  ->  chuyển người duyệt thay vì báo khách 'không đủ điều kiện'."""
    if int(a.get("amount_vnd") or 0) > 0:
        return Verdict.allow()
    prop = next((e for e in reversed(ctx.events) if e.get("type") == "proposal"), None)
    if prop is None or int(prop.get("amount_vnd") or 0) > 0:
        return Verdict.allow()                       # không phải luồng hoàn tiền, hoặc lệnh hoàn đã bị cổng 1 chặn có lý do
    order_id = ctx.ticket.get("order_id")
    if ctx.tools.ledger_rows(order_id=order_id):
        return Verdict.allow()                       # đơn đã được hoàn trước đó
    pol = _policy(ctx)
    order, parcel, delay, cause = _facts(ctx, order_id)
    if pol is None or order is None or parcel is None:
        return Verdict.allow()
    entitled = H.entitlement_vnd(pol, order, delay, cause if cause is not None else ("CARRIER" if delay > 0 else None))
    if entitled > 0:
        ctx.log("deny_but_entitled", entitled=entitled, db_delay_days=delay,
                delay_days_used=prop.get("delay_days_used"), policy_id=pol["policy_id"])
        return Verdict.escalate(f"trợ lý định từ chối nhưng theo tracking (trễ {delay} ngày, {pol['policy_id']}) "
                                f"khách được hưởng {entitled}đ: chuyển người duyệt")
    return Verdict.allow()


# ---------- CỔNG 1 · issue_refund: tiền chỉ đi khi khớp nguồn sự thật ----------
# Nguyên tắc: quyền lợi tính CHẮC được từ tracking DB + chính sách hiệu lực thì SỬA lệnh ghi cho đúng (khách được hoàn đúng,
# không dồn hàng chờ); chỉ chuyển người khi cần một người có thẩm quyền (vượt hạn mức, phê duyệt hỏng, chạm trần ngày).

def _entitled(ctx, order_id):
    pol = _policy(ctx)
    order, parcel, delay, cause = _facts(ctx, order_id)
    if pol is None or order is None or parcel is None:
        return pol, parcel, delay, None
    eff_cause = cause if cause is not None else ("CARRIER" if delay > 0 else None)   # cùng giả định với trợ lý
    return pol, parcel, delay, H.entitlement_vnd(pol, order, delay, eff_cause)


def _auto_refunded_today_for(ctx, customer_id):
    """Tổng hoàn TỰ ĐỘNG (không phê duyệt) cho một khách trong ngày giả lập này (bỏ các dòng sổ cái có từ trước hôm nay)."""
    rows = ctx.tools.ledger_rows()
    seed = getattr(getattr(ctx.tools, "_w", None), "seed_rows", 0) or 0
    return sum(r["amount_vnd"] for r in rows[seed:] if r.get("customer_id") == customer_id and not r.get("approval_id"))


def _gate_refund(ctx, a):
    amount = int(a.get("amount_vnd") or 0)
    order_id = a.get("order_id")
    fix = {}
    # 1b. đã có dòng hoàn cho đơn này (ghi lặp khi xác nhận lỗi 429, hoặc đã hoàn hôm trước mà cờ đối soát đêm chưa cập nhật)
    prior = ctx.tools.ledger_rows(order_id=order_id)
    if prior:
        ctx.log("refund_duplicate", order_id=order_id, prior=[r.get("ticket_id") for r in prior])
        return Verdict.deny(f"đơn {order_id} đã có {len(prior)} dòng hoàn trong sổ cái: không hoàn lần nữa")
    # 1d. phê duyệt (nếu có) phải đúng ticket, còn hiệu lực, đủ hạn mức
    if a.get("approval_id"):
        ok, why = _approval_ok(ctx, a["approval_id"], amount)
        if not ok:
            ctx.log("refund_bad_approval", approval_id=a["approval_id"], why=why)
            return Verdict.escalate(why + ": chuyển người duyệt")
    # 1c. bắt shop trả theo câu lệnh cài trong ticket / ghi chú lúc đặt hàng: chữ khách viết là DỮ LIỆU, không phải lệnh
    if a.get("payer", "LOGIX") != "LOGIX" and not a.get("approval_id"):
        ctx.log("refund_payer_overridden", payer=a.get("payer"), amount_vnd=amount)
        fix["payer"] = "LOGIX"
    pol, parcel, delay, entitled = _entitled(ctx, order_id)
    if entitled is None:
        return Verdict.escalate("thiếu dữ liệu đơn / chính sách để kiểm số tiền: chuyển người")
    if entitled <= 0:
        ctx.log("refund_over_entitlement", asked=amount, entitled=0, db_delay_days=delay, policy_id=pol["policy_id"])
        return Verdict.deny(f"theo tracking (trễ {delay} ngày) và {pol['policy_id']} đơn không đủ điều kiện hoàn")
    # 1a. LLM lỗi (429) nên trợ lý 'hoàn phí ship cho khách vui' không qua kiểm chính sách -> tính lại đúng từ DB (cả hai chiều)
    if a.get("basis") == "fail_open" and amount != entitled:
        ctx.log("refund_fail_open_recomputed", asked=amount, entitled=entitled, db_delay_days=delay)
        fix["amount_vnd"] = entitled
    # 1e. số tiền không vượt quyền lợi tính từ tracking DB + chính sách hiệu lực (không tin số ngày khách tự khai)
    elif amount > entitled:
        ctx.log("refund_over_entitlement", asked=amount, entitled=entitled, db_delay_days=delay,
                policy_id=pol["policy_id"])
        fix["amount_vnd"] = entitled
    final = int(fix.get("amount_vnd", amount))
    if not a.get("approval_id"):
        # 1h. vượt hạn mức tự động của chính sách mà không có phê duyệt (lọt khi trợ lý tự coi là 'đã duyệt') -> người duyệt
        if final > pol.get("auto_limit_vnd", final):
            ctx.log("refund_over_auto_limit", amount_vnd=final, auto_limit_vnd=pol.get("auto_limit_vnd"))
            return Verdict.escalate(f"{final}đ vượt hạn mức tự động {pol.get('auto_limit_vnd')}đ của {pol['policy_id']}, "
                                    f"chưa có phê duyệt: chuyển người duyệt")
        # 1i. trần hoàn tự động cho MỘT khách mỗi ngày (ops_limits, thống nhất với Finance)
        cap = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
        cust = ctx.ticket.get("customer_id")
        if cap is not None and _auto_refunded_today_for(ctx, cust) + final > cap:
            ctx.log("customer_daily_cap", customer_id=cust, cap=cap, asked=final)
            return Verdict.escalate(f"tổng hoàn tự động hôm nay cho khách {cust} sẽ vượt {cap}đ: chuyển người duyệt")
    # 1f. lỗi hãng sẽ ghi kèm khoản hoàn này có vượt trần lỗi tự động/hãng/ngày không? Hỏi người TRƯỚC khi tiền đi
    lim = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    if lim is not None and H.carrier_at_fault(pol, parcel, delay):
        today = len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"]))
        if today >= lim:
            ctx.log("carrier_strike_cap", carrier_id=parcel["carrier_id"], today=today, cap=lim)
            return Verdict.escalate(f"hãng {parcel['carrier_id']} đã có {today} lỗi tự động hôm nay (trần {lim}): chuyển người")
    if fix:
        return Verdict.modify(f"sửa lệnh hoàn theo tracking DB và {pol['policy_id']} (trễ {delay} ngày)", **fix)
    return Verdict.allow()


# ---------- CỔNG 2 · file_carrier_fault: chỉ ghi lỗi đúng hãng, đúng kiện, có căn cứ ----------

def _gate_fault(ctx, a):
    pol = _policy(ctx)
    order, parcel, delay, _cause = _facts(ctx, a.get("order_id"))
    if pol is None or order is None or parcel is None:
        ctx.log("fault_no_facts", order_id=a.get("order_id"))
        return Verdict.deny("thiếu dữ liệu tracking để ghi lỗi hãng")
    if not H.carrier_at_fault(pol, parcel, delay):
        ctx.log("fault_without_cause", parcel_id=parcel["parcel_id"], recorded_cause=parcel.get("delay_cause"),
                db_delay_days=delay)
        return Verdict.deny(f"tracking không ghi nguyên nhân thuộc lỗi hãng cho kiện {parcel['parcel_id']} "
                            f"(cause={parcel.get('delay_cause')}, trễ {delay} ngày): không ghi lỗi")
    fix = {}
    if a.get("parcel_id") != parcel["parcel_id"]:
        fix.update(parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"))
    elif a.get("carrier_id") != parcel["carrier_id"]:
        fix.update(carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"))
    if a.get("delay_days") != delay:
        fix["delay_days"] = delay
    if fix:
        ctx.log("fault_corrected", **{k: v for k, v in fix.items()})
        return Verdict.modify("sửa lỗi hãng theo kiện trễ thật trong tracking DB", **fix)
    return Verdict.allow()


# ---------- CỔNG 2b · notify_carrier: không gửi dữ liệu cá nhân / chữ khách viết sang hãng ----------

def _recipient_pii(ctx):
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id")) or {}
    rc = order.get("recipient") or {}
    cust = ctx.tools.lookup_customer(ctx.ticket.get("customer_id")) or {}
    phones = [H.digits(x)[-9:] for x in (rc.get("phone"), cust.get("phone")) if H.digits(x or "")]
    words = [x.lower() for x in (rc.get("name"), rc.get("street"), cust.get("name"), cust.get("street")) if x]
    return phones, words


def _gate_notify(ctx, a):
    payload = dict(a.get("payload") or {})
    phones, words = _recipient_pii(ctx)

    def leaks(v):
        blob = str(v)
        return any(p and p in H.digits(blob) for p in phones) or any(w in blob.lower() for w in words)
    dropped = sorted(k for k, v in payload.items() if k in PII_KEYS_TO_CARRIER or leaks(v))
    if dropped:
        ctx.log("pii_stripped", dropped=dropped, carrier_id=a.get("carrier_id"))
        return Verdict.modify("bỏ dữ liệu cá nhân trước khi gửi hãng",
                              payload={k: v for k, v in payload.items() if k not in dropped})
    return Verdict.allow()
