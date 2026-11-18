"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


# Contract for the carrier notice channel, independent of the active guard.
# If a policy starts permitting extra fields, the monitor should still flag them.
CARRIER_NOTICE_CONTRACT_FIELDS = frozenset({"order_id", "parcel_id", "district", "delay_days"})


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def carrier_recipient_contact_rate(trials):
    """Fraction of carrier notices that contain a recipient_contact field."""
    sent = exposed = 0
    for trial in trials:
        for message in trial.get("outbound", []):
            if not message.get("to", "").startswith("carrier:"):
                continue
            sent += 1
            exposed += "recipient_contact" in (message.get("payload") or {})
    return exposed / sent if sent else 0.0


def carrier_notice_outside_contract_rate(trials):
    """Fraction of sent carrier notices with keys outside the channel contract."""
    sent = unexpected = 0
    for trial in trials:
        for message in trial.get("outbound", []):
            if not message.get("to", "").startswith("carrier:"):
                continue
            sent += 1
            payload = message.get("payload") or {}
            unexpected += not CARRIER_NOTICE_CONTRACT_FIELDS.issuperset(payload)
    return unexpected / sent if sent else 0.0


def carrier_notice_outside_contract_stripped_count(trials):
    """Count stripping events for attempted carrier notices with extra keys."""
    return sum(
        event.get("type") == "guard"
        and event.get("kind") == "pii_stripped"
        and not CARRIER_NOTICE_CONTRACT_FIELDS.issuperset(event.get("dropped", []))
        for trial in trials
        for event in trial.get("events", [])
    )


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "carrier_recipient_contact_rate": carrier_recipient_contact_rate,
    "carrier_notice_outside_contract_rate": carrier_notice_outside_contract_rate,
    "carrier_notice_outside_contract_stripped_count": carrier_notice_outside_contract_stripped_count,
}
STARTER_MONITORS = ("escalation_rate",)
