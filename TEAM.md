# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `SaoCungDuoc`
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-SaoCungDuoc-PoCtoPilotGate1` (https://github.com/VictorUIT/K5-L3A-DAY10-SaoCungDuoc-PoCtoPilotGate1)
- Thẻ sự cố đã bốc (S1–S8): `S7`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Văn Ngọc Sơn | 2A202603600 | Kỹ sư cổng (P1) |     |
|   2 | Nguyễn Bình An | 2A202603606 | Kỹ sư cổng (P2) |             |
|   3 | Trần Quốc Tuấn Khanh | 2A202603625 | Sản phẩm và kinh doanh (P3) |      ✔      |
|   4 | Đỗ Phương Nam | 2A202603621 | Vận hành và pháp lý (P4) |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## NguyenVanNgocSon-2A202603600

### Phần việc phụ trách

Nguyễn Văn Ngọc Sơn, MSSV `2A202603600`, P1 (Kỹ sư cổng 1, giữ máy chạy lệnh và danh tính git của bàn). Phụ trách: ký Bản tiêu chí (`config/acceptance_criteria.json`, Phiếu A mục A5); Phiếu B mục B0, B1 (câu 2.1), B2 (câu 2.2), B7.1 (câu 2.6); `lab10/guards.py` (cổng vòng 1 và vòng 2); chốt cổng vòng 1 (`lab10.checkpoint`) và chạy mốc prepared. Vòng 2 (thẻ S7): nhận thẻ và chạy grade trước khi sửa (câu 3.0, Phiếu C mục C0, C1), sửa `lab10/guards.py` (câu 3.5), chạy lại S7 và bộ nền; chạy lệnh 6 và lệnh 7 lần cuối.

### Đóng góp cụ thể

- Ký tiêu chí trước mọi lần đánh giá: ký lúc 12:02:19, commit `Sign acceptance criteria` lúc 12:02:36, lần `eval` đầu tiên lúc 12:02:41.
- Câu 2.1–2.2: chạy mốc base (trượt 2 ngưỡng an toàn: hoàn sai 20.000đ, 1 lỗi oan, đều từ `T-002@55`); soát lỗi `T-002@55` thành 2 lỗi chìm (model tin số ngày khách khai thay tracking; chữ khách gõ bị chép sang hãng).
- Câu 2.6, `lab10/guards.py` gồm 3 cổng: (1) tiền chỉ đi khi khớp tracking DB và chính sách hiệu lực (sửa số tiền và người trả về đúng thay vì chuyển người; chặn hoàn lặp, phê duyệt sai ticket hoặc hết hạn, vượt hạn mức tự động, vượt 300.000đ/khách/ngày, quá 2 lỗi/hãng/ngày); (2) chỉ ghi lỗi hãng đúng kiện, đúng hãng, có nguyên nhân trong tracking, và bỏ dữ liệu cá nhân khỏi thông báo gửi hãng; (3) `pre_guard` ghim chính sách theo ngày hiệu lực và bỏ số ngày khách tự khai trước khi model đọc.
- Vá lỗ hổng do ticket hiểm BT-02 của P2 tìm ra (khách khai trễ ít hơn tracking, trợ lý từ chối sai 25.000đ): thêm cổng dự phòng ở `send_reply`, rồi sửa gốc ở `pre_guard`.
- Dựng 13 tình huống sự cố giả lập (LLM 429, câu lệnh cài trong ticket và ghi chú đặt hàng, chỉ mục chính sách lệch, REFUND-v4, đơn nhiều kiện, phê duyệt sai, quà tặng…) để thử cổng trước khi chốt: không cổng 12/13 tình huống có thiệt hại, có cổng 13/13 sạch.
- Chốt cổng vòng 1 (`cee42672`); mốc prepared đạt cả 9 ngưỡng đã ký.
- Thẻ S7: kiểm 4 file thẻ khớp hash MANIFEST; grade trước khi sửa cho thấy cổng vòng 1 đã đỡ trọn phần nhìn thấy (pass 0.25 → 1.0, lộ dữ liệu 30 → 0). Câu 3.5: đổi `notify_carrier` từ danh sách cấm (GIẢM) sang danh sách cho phép `carrier_notice_fields` của chính sách hiệu lực (BẢO ĐẢM).

### Bằng chứng

- Commit P1: `be86664` (ký tiêu chí), `ea9c219` (cổng vòng 1, A5, B0, B1, B2, B7.1), `2c3660e` (bản nháp `operating_gates.json` để P3/P4 sửa), `6acf184` (cổng dự phòng `send_reply`), `826e58e` (`pre_guard` bỏ số ngày tự khai), `637eefd` (bản cuối cổng vòng 1, chốt `cee42672`, B0), `fc228bd` (S7: C0, C1, danh sách cho phép).
- Vòng 1: base `R-base-before-20261118-120241-e347b3` → after `R-base-after-20261118-154910-39f687` → prepared `R-base-prepared-20261118-155119-c6f842` (110/110, 9/9 ngưỡng đã ký đạt).
- Vòng 2 (S7): grade trước khi sửa `R-S7-grade-20261118-164613-c6f842` (base `R-S7-before-20261118-164613-c6f842`, prepared `R-S7-prepared-20261118-164613-c6f842`); sau khi sửa `R-S7-after-20261118-164712-b3ebf5`, bộ nền `R-base-after-20261118-164713-b3ebf5`, grade `R-S7-grade-20261118-164814-b3ebf5`.
- Phiếu: A5; B0, B1, B2, B7.1; C0, C1, dòng `Thẻ đã bốc: S7`.

### Sử dụng AI

Claude Code (Claude) được dùng xuyên suốt phần P1: đọc code trợ lý (`agent.py`, `mock_llm.py`, `tools.py`, `eval.py`) để tìm chỗ yếu; viết và kiểm thử `lab10/guards.py`; chạy `lab10.eval`, `lab10.trace`, `lab10.gate`, `lab10.checkpoint`, `lab10.grade`; dựng 13 tình huống giả lập; soạn nội dung A5, B0, B1, B2, B7.1, C0, C1. Claude cũng soạn **bản nháp ban đầu** của Phiếu A (A1–A4, ngưỡng tiêu chí trước khi ký) và của `config/operating_gates.json`; P2, P3, P4 đã rà lại và sửa phần của mình. Exit ticket do Claude soạn nháp, P1 đã đọc và chốt. Mọi ngưỡng, con số và quyết định do cả bàn chốt và phải giải thích được lúc demo.

### Exit ticket

- Điều học được: Chặn dữ liệu cá nhân bằng danh sách cấm chỉ GIẢM rủi ro, vì nó bỏ sót trường mới như `recipient_contact` ở S7; chỉ danh sách cho phép mới BẢO ĐẢM.
- Điều còn chưa chắc: `pre_guard` chỉ bỏ số ngày viết bằng số ("9 ngày"), nên chưa chắc cổng còn đứng vững khi khách viết bằng chữ ("hơn một tuần") hoặc khi thay MockLLM bằng model thật.

## NguyenBinhAn-2A202603606

### Phần việc phụ trách

Nguyễn Bình An, MSSV `2A202603606`, P2 (Kỹ sư cổng). Vòng 1 phụ trách đề xuất cách đo offline ở A2 câu 1.3, lăng kính kỹ thuật ở B6, B7.2 và B7.3. Hỗ trợ P4 ở A2 câu 1.4 và P1 ở B2. Vòng 2 phụ trách phân tích trace S7 ở C2, dựng fault tree trước sửa ở C6 và triển khai monitor trong `lab10/monitors.py` cho C8.

### Đóng góp cụ thể

- Đề xuất thước đo offline cho bước chọn độ trễ, nêu cách xử lý trial thiếu dữ liệu và điểm mù. Đối chiếu với thước đo ghi lỗi hãng trong Phiếu A và chuẩn bị đề xuất telemetry không nhãn cho P4.
- Đối chiếu B2 bằng trace `T-002@55`, đóng góp giả thuyết kỹ thuật vào B6 và viết hai bước tránh rò rỉ dữ liệu đánh giá ở B7.2.
- Thiết kế BT-01/BT-02 để kiểm hai hướng khai sai độ trễ. BT-02 làm lộ lỗi từ chối sai khoản hoàn 25.000đ. Sau khi P1 sửa, chạy lại cả hai ca và ghi kết quả trước/sau ở B7.3.
- Nhận thẻ S7. Dùng trace để tách hai nguồn lộ thông tin liên hệ qua `customer_note` và `recipient_contact`, với ca mã vận đơn làm đối chứng. Ghi bảng soát lỗi ở C2, dựng fault tree ở C6 và thêm `carrier_recipient_contact_rate` ở C8. Theo rủi ro C10, bổ sung đo khóa ngoài hợp đồng ở đầu ra thực gửi và đếm riêng các trường bị cổng loại.

### Bằng chứng

- **Vòng 1:** `1a4c195` tích hợp mục cá nhân và B2/B6/B7.2/B7.3. B2 đối chiếu `T-002@55` ở base và after. Run ID baseline của nhóm ở B0 là `R-base-before-20261118-120241-e347b3`.
- **Xác minh bản sửa:** P1 thêm cổng dự phòng `send_reply` ở `6acf184`, rồi bỏ số ngày tự khai trước khi model đọc ở `826e58e`. Trên `637eefd`, seed 55, BT-01 từ chối đúng và BT-02 hoàn đúng 25.000đ, ghi lỗi GHSH theo tracking 4 ngày. Kết quả tái chạy ở B7.3, commit `904b5a5`. Run ID đánh giá bộ nền của P1 ở B0 là `R-base-after-20261118-152153-5e77d5` và `R-base-prepared-20261118-155119-c6f842`.
- **S7:** `cb6c615` nhận thẻ, `fcf709c` tích hợp C2/C6/C8 và monitor. Trace `S7-01@11`, `S7-20@11` xác nhận hai nguồn lộ thông tin, còn `S7-05@11` là ca đối chứng. Đối chiếu lượt grade trước sửa mà P1 ghi ở C0/C1: `R-S7-grade-20261118-164613-c6f842`.
- **Monitor S7:** Ở before, bộ nền có 0/56 thông báo chứa `recipient_contact`, S7 có 10/35 (28,57%). S7 về 0/35 ở cả prepared và after. Lượt `R-S7-grade-20261118-173953-414377` được P4 ghi ở C11 với `6 monitor ✅` cho monitor ban đầu. Sau khi bổ sung hai tín hiệu, kiểm tra local tại `ef67cf5` cho thấy S7 after gửi 0/35 thông báo có khóa ngoài hợp đồng và cổng đã loại khóa thừa 35 lần; `monitor_check.ok=true`, `errors=[]`. Grade cho hai tín hiệu bổ sung chưa có.

### Sử dụng AI

ChatGPT hỗ trợ soạn tài liệu và thiết kế metric, ca kiểm thử, monitor ứng viên. Codex hỗ trợ chạy và đối chiếu trace, tích hợp monitor, kiểm thử cục bộ và cập nhật các mục P2 trong phiếu nhóm.

### Exit ticket

- Điều học được: BT-02 cho thấy cổng kiểm lệnh hoàn không bảo vệ được quyền lợi nếu agent trả lời từ chối trước khi tạo lệnh ghi. Với S7, cần đọc payload thực gửi vì thông tin người nhận có thể đến từ cả ticket lẫn dữ liệu đơn hàng.
- Điều còn chưa chắc: Các monitor C8 kiểm tên trường và tín hiệu cổng. Cần kiểm riêng dữ liệu liên hệ nằm trong giá trị của trường được phép và độ phủ telemetry khi thử pilot.

## DoPhuongNam-2A202603621

### Phần việc phụ trách

Đỗ Phương Nam, MSSV `2A202603621`, P4 (Vận hành và pháp lý). Phụ trách Phiếu A câu 1.2, 1.4; Phiếu B mục B4 (HAZOP vòng 1), B5 (checklist 9 nhóm), lăng kính con người, vận hành và pháp lý ở B6, B7.5 (runbook phần 1–3), B7.6 (giờ cao điểm); `config/operating_gates.json` mục `operations` và `legal`. Vòng 2: Phiếu C mục C3, C4, C9, C10, C11 và `submission/submission.json`.

### Đóng góp cụ thể

- HAZOP vòng 1 trên `file_carrier_fault` (6 dòng) và 4 dòng ngoài kỹ thuật. Tìm ra nhánh chưa thấy trên trace: cổng chỉ đếm lỗi hãng trong ngày, nên GHSH (5 đơn đủ điều kiện lỗi hãng) vẫn có thể bị đình chỉ ở lỗi thứ 3 trong 7 ngày.
- Mục `legal`: chặn thêm `recipient`, `name`, `phone`, `street` khi gửi hãng. Mục `operations`: điều kiện dừng số 4 khớp phạm vi theo kho, thêm điều kiện dừng số 5 (lỗi hãng 7 ngày) và số 6 (phê duyệt không hợp lệ).
- Runbook 1–3 và giờ cao điểm khớp con số trong config; đo chi phí khi thêm người trực thứ hai.
- Vòng 2 (thẻ S7): C5 câu 3.3, giả định môi trường "cờ `is_gift` phản ánh đúng đơn quà" (sai ngay trong data: `O-2701`…`O-2704`, `O-2706`), và chỉ ra monitor `carrier_recipient_contact_rate` mù với 4/6 ticket bị lộ ở base.
- C3.3 hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng); C4 HAZOP của thẻ trên `notify_carrier` (5 dòng, nhánh chưa thấy trên trace: chính danh sách cho phép `carrier_notice_fields` có thể bị chính sách sau thêm trường liên hệ); C9 fault tree sau khi sửa; C10 risk register 3 dòng; C11 checklist và runbook phần 4–5.
- Điền `submission/submission.json` (team, members, incident, decision_v1); sửa lỗi CRLF trên Windows làm grade báo nhầm file khoá bị đổi.

### Bằng chứng

- `R-base-after-20261118-153103-610c87`: sau khi sửa `operations`/`legal`, 110/110, hoàn sai 0 · lỗi oan 0 · lộ dữ liệu 0, chờ lâu nhất 0 phút, 4.456đ/ticket, ROI 1.24.
- `R-base-after-20261118-153114-bb48a9`: thử 2 người trực (12 ca/giờ) → 5.820đ/ticket, ROI 0.72 (config đã trả về 1 người).
- `--adhoc` đơn quà `O-1026`/`C-10` ở mốc `after`: `GỬI HÃNG` chỉ còn `order_id`, `parcel_id`, `district`, `delay_days`.
- Vòng 2: `R-S7-grade-20261118-173953-414377` (after S7 `R-S7-after-20261118-173952-414377`, bộ nền `R-base-after-20261118-173952-414377`): `pii_leaks` 30 → 0, `5 regression ✅`, `6 monitor ✅`; base `R-S7-before-20261118-173955-414377` dùng cho C3.3, C4, câu 3.3.
- Commit P4: `c0c389a` (Phiếu B B4, B5, B6, B7.5, B7.6; `config/operating_gates.json` mục `operations`, `legal`).
- Commit P4 vòng 2: `d5fb912` (Phiếu C C3.3, C4, C5 câu 3.3, C9, C10, C11; `submission/submission.json`).

### Exit ticket

- Điều học được: Một cổng phòng ngừa chỉ đáng tin khi nó đếm đúng khung thời gian của người chịu hại. Trần "2 lỗi/hãng/ngày" trông an toàn, nhưng hãng nhỏ như GHSH bị đình chỉ theo 7 ngày, nên con số vận hành (người trực, điều kiện dừng, runbook) phải đặt theo hậu quả cho bên thứ ba chứ không chỉ theo chỉ số của bộ thử.
- Điều còn chưa chắc: Ngưỡng gọi người thứ hai (4 ca hoặc 40 phút) mới được ước tính theo Phụ lục D, chưa đo được trên bộ nền chỉ có một ngày đều đặn; chưa biết khi ticket dồn ×3 trong một giờ (thẻ S4) thì 1 người trực có làm `queue_stuck` > 0 hay không, và thêm người có giữ ROI trên 0,25 hay không.

## TranQuocTuanKhanh-2A202603625

### Phần việc phụ trách

Trần Quốc Tuấn Khanh, MSSV `2A202603625`, P3 (Sản phẩm và kinh doanh). Phụ trách Phiếu B mục B3 (bản đồ dữ liệu và ví dụ drift), lăng kính kinh doanh ở B6, B7.4 (cổng kinh doanh), B8 (quyết định Gate 1 v1); `config/operating_gates.json` mục `business`. Vòng 2: Phiếu C mục C5 (câu 3.2 specification), phần business của C7, C12 (quyết định Gate 1 v2) và sửa mục `business` nếu thẻ sự cố đòi hỏi.

### Đóng góp cụ thể

- B3: bản đồ dữ liệu của trợ lý, tách nguồn sự thật với bản sao (cờ `index_active` chỉ là bản sao của ngày hiệu lực chính sách). Lượng hoá drift REFUND-v3 → v4 (01/12/2026) trên 25 đơn trong data: số đơn được hoàn 16 → 18, tổng tiền hoàn 977.000đ → 1.237.000đ (+27%), số đơn vượt hạn mức tự động 2 → 3; đơn trễ do bão O-1006 không còn bị ghi lỗi hãng.
- Mục `business`: giữ trần tự hoàn 1.000.000đ/ngày (một nửa ngân sách Finance), ngân sách 1.500đ/ticket (bằng trần LLM trong `ops_limits`), `roi_min` 0.25 (khớp tiêu chí đã ký). Đổi `pilot_scope` từ `all` sang 4 kho đơn lẻ HN, HCM, DN, CT, bỏ kho sỉ HCM-B2B: kho này có 0 đơn trong bộ nền, đơn sỉ từ 2 triệu nên mức hoàn luôn vượt hạn mức tự động, ca nào cũng chuyển người và đắt hơn làm tay.
- B6 lăng kính kinh doanh: 3 lý do thất bại (vượt ngân sách hoàn trong ngày sale, chi phí mỗi ticket vượt làm tay, ticket dài làm tiền LLM tăng vọt), mỗi lý do gắn với một số trong report và một cổng trong config.
- B8: quyết định v1 là **Thu hẹp** (4 kho đơn lẻ, 100% ticket, 1 người trực), khớp dòng "Thu hẹp" của `decision_rule`. Chưa chọn "Tiếp tục" vì gói sự cố chưa đo. Phát hiện cảnh báo "file tiêu chí ĐÃ BỊ SỬA" của `lab10.gate` trên máy Windows là do checkout CRLF (`core.autocrlf=true`), hash bản LF vẫn khớp lock `8a985c95`.
- C5 câu 3.2 (thẻ S7): viết spec của kênh gửi hãng. Thông báo `notify_carrier` chỉ được chứa đúng các khoá trong `carrier_notice_fields` của chính sách hiệu lực (`order_id`, `parcel_id`, `district`, `delay_days`), không giá trị nào chứa SĐT, tên hay đường của người nhận, bất kể `is_gift`; kèm vế không chặn quá tay (ca hợp lệ vẫn báo hãng đủ 4 trường). Chỉ ra `pii_leaks` chỉ dò giá trị, không kiểm tập khoá, nên vế khoá phải kiểm bằng dòng `GỬI HÃNG` trong trace.
- C7 phần kinh doanh: giữ `pilot_scope` 4 kho và `notify_carrier: on`, vì lộ dữ liệu ở base trải 3/4 kho (HN 10, HCM 15, DN 5 lượt) và 3/4 hãng nên cắt kho không chặn được nhánh [3]. Kiểm cái giá của bản sửa danh sách cho phép: prepared → after 5.005đ → 5.005đ/ticket, ROI 1.0 → 1.0, tức tốn 0đ; phần tăng base → prepared đến từ kiểm mẫu 10% và ghi chú giải thích của vòng 1.
- C12: quyết định v2 **giữ Thu hẹp**. Số đã đủ cho "Tiếp tục" (8 ngưỡng đạt trên bộ nền và gói S7, lộ dữ liệu 30 → 0 → 0), nhưng chỉ trong 4 kho đã đo: HCM-B2B vẫn 0 đơn, và 30 lượt dữ liệu gửi trước khi sửa còn ở GHSH, VNX, DNB. Thêm điều kiện không mở rộng khi chưa có xác nhận xoá của 3 hãng; quyết định lại 2026-11-30 (trước REFUND-v4). Viết ba dòng bắt buộc và chép sang `submission/submission.json` (`decision_v2`, `three_lines`), cập nhật theo hai monitor hợp đồng kênh gửi hãng của P2.

### Bằng chứng

- `R-base-after-20261118-145831-4675a2`: sau khi đổi `pilot_scope` sang 4 kho, 110/110, hoàn sai 0 · lỗi oan 0 · lộ dữ liệu 0, 4.456đ/ticket, ROI 1.24, tổng hoàn tự động 155.000đ/ngày, `vượt trần: không`; 13 unit test qua.
- B8 dùng `R-base-before-20261118-120241-e347b3` (mốc base) và `R-base-prepared-20261118-155119-c6f842` (prepared, chốt `cee42672`): 9/9 ngưỡng đã ký đạt.
- Commit P3: `8d85e30` (B3, B6 kinh doanh, B7.4, `pilot_scope`), `a53e646` (B8 quyết định v1).
- Thẻ sự cố **S7**. C7 và C12 dùng gói S7: base `R-S7-before-20261118-164613-c6f842`, prepared `R-S7-prepared-20261118-164613-c6f842`, after `R-S7-after-20261118-164814-b3ebf5`, bộ nền after `R-base-after-20261118-164713-b3ebf5` (C0), self-check `R-S7-grade-20261118-173953-414377` (C9). Số kinh doanh ba mốc của C7 đối chiếu lại bằng `R-S7-grade-20261118-173925-dcc726`.
- Commit P3 vòng 2: `5452130` (C5 câu 3.2), `fc9bcec` (C7 phần kinh doanh), `5c17779` (C12 và `submission.json`), `605292b` (C12 cập nhật theo monitor của P2).

### Sử dụng AI

Claude Code hỗ trợ đọc `data/world.json` và `lab10/ops.py`, chạy `lab10.eval`/`lab10.gate`, tính drift v3 → v4 và soạn nội dung các mục phiếu.

### Exit ticket

- Điều học được: Quyết định Gate 1 phải đọc đúng câu chữ của `decision_rule` đã ký, không chỉ nhìn 9 ngưỡng xanh. Bộ nền đạt hết nhưng chưa có gói sự cố và chưa có đơn kho sỉ, nên "Thu hẹp" mới là quyết định con số đỡ được.
- Điều còn chưa chắc: Trần tự hoàn 1.000.000đ/ngày được ước theo 155.000đ/ngày của bộ nền đều đặn; chưa biết khi REFUND-v4 có hiệu lực cùng lúc với ngày sale (ticket ×3) thì tổng hoàn và tỉ lệ chuyển người còn trong ngưỡng hay không. Với S7, gói thử chỉ 8 ticket/ngày nên phí giữ chỗ người trực chiếm khoảng 3.750đ/ticket; chưa biết ROI 1.0 còn giữ được với lượng ticket thật.
