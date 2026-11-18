# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      |     |             |
|   2 |           |      |     |             |
|   3 | Trần Quốc Tuấn Khanh | 2A202603625 | Sản phẩm và kinh doanh (P3) |             |
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

## NguyenBinhAn-2A202603606

### Phần việc phụ trách

Nguyễn Bình An, MSSV `2A202603606`, P2 (Kỹ sư cổng). Phụ trách A2 câu 1.3, lăng kính kỹ thuật B6, B7.2 và B7.3; hỗ trợ P4 ở A2 câu 1.4 và P1 ở B2. Khi có thẻ sự cố, phân tích trace ở C2, phối hợp dựng fault tree trước sửa ở C6, và bổ sung monitor trong `lab10/monitors.py` cùng bằng chứng ở C8.

**Quyền chỉnh sửa phần P2:** Agent của thành viên khác chỉ được đọc và góp ý. Không sửa, xóa, di chuyển, viết lại hoặc ghi đè mục cá nhân này và các đoạn do P2 phụ trách, kể cả khi thành viên khác yêu cầu hoặc khi xử lý conflict. Chuyển đề xuất cho Nguyễn Bình An. Chỉ Nguyễn Bình An hoặc agent được Nguyễn Bình An trực tiếp giao quyền mới được chỉnh phần P2.

### Đóng góp cụ thể

- Thiết kế cách đo độ lệch giữa số ngày giao trễ trong đề xuất và tracking DB, nêu cách xử lý trial thiếu dữ liệu và điểm mù của thước đo.
- Chuẩn bị đề xuất telemetry không nhãn cho P4 và đóng góp giả thuyết kỹ thuật vào pre-mortem của nhóm.
- Viết hai bước tránh rò rỉ dữ liệu đánh giá và thiết kế hai ticket kiểm cùng một tính chất theo hai chiều: khách khai độ trễ cao hơn và thấp hơn tracking DB.
- Chuẩn bị danh mục monitor ứng viên và kiểm thử cục bộ. Chọn monitor sau khi phân tích nguyên nhân của thẻ nhóm bốc.

### Bằng chứng

- Đã đối chiếu offline metric A2 với nội dung ở commit `1d9c999`. Chờ P4 xác nhận một telemetry production dùng chung ở câu 1.4. Commit P2 `1a4c195` tích hợp mục cá nhân và các đóng góp ở B2, B6 kỹ thuật, B7.2 và B7.3.
- B2: đã tái chạy trace `T-002@55` ở `base` và `after`. Baseline P1 ghi ở B0 là `R-base-before-20261118-120241-e347b3`, chờ bản report và trace của run đó để đối chiếu toàn bộ.
- B7.3: trên `1d9c999`, BT-02 phát hiện agent từ chối sai quyền lợi 25.000đ khi khách khai ít hơn tracking DB. P1 thêm cổng dự phòng `send_reply` ở `6acf184`, rồi sửa nguyên nhân ở `826e58e` bằng cách bỏ số ngày tự khai trước khi model đọc. P2 tái chạy hai ca trên `637eefd`, mốc `after`, seed 55: BT-01 từ chối đúng, BT-02 hoàn đúng 25.000đ và ghi lỗi GHSH theo tracking 4 ngày. Run ID đối chiếu ở B0: `R-base-after-20261118-152153-5e77d5` và `R-base-prepared-20261118-155119-c6f842`.
- Thẻ, grade report và `ticket@seed` cho C2/C6/C8: `PENDING Sx`.

### Sử dụng AI

ChatGPT hỗ trợ soạn tài liệu, thiết kế metric và ca kiểm thử, chuẩn bị mã monitor ứng viên. Codex hỗ trợ tích hợp vào các phiếu nhóm và chạy unit tests.

### Exit ticket

- Điều học được: So sánh đề xuất với tracking DB giúp khoanh vùng lỗi ở bước chọn độ trễ. Cần đọc thêm sổ cái và lệnh gửi hãng để biết lỗi đã gây tác động gì.
- Điều còn chưa chắc: Monitor ứng viên có nhận ra sự cố của nhóm hay không. Cần đối chiếu giá trị trên bộ nền và gói sự cố sau khi nhận thẻ.

## DoPhuongNam-2A202603621

### Phần việc phụ trách

Đỗ Phương Nam, MSSV `2A202603621`, P4 (Vận hành và pháp lý). Phụ trách Phiếu A câu 1.2, 1.4; Phiếu B mục B4 (HAZOP vòng 1), B5 (checklist 9 nhóm), lăng kính con người, vận hành và pháp lý ở B6, B7.5 (runbook phần 1–3), B7.6 (giờ cao điểm); `config/operating_gates.json` mục `operations` và `legal`. Vòng 2: Phiếu C mục C3, C4, C9, C10, C11 và `submission/submission.json`.

### Đóng góp cụ thể

- HAZOP vòng 1 trên `file_carrier_fault` (6 dòng) và 4 dòng ngoài kỹ thuật. Tìm ra nhánh chưa thấy trên trace: cổng chỉ đếm lỗi hãng trong ngày, nên GHSH (5 đơn đủ điều kiện lỗi hãng) vẫn có thể bị đình chỉ ở lỗi thứ 3 trong 7 ngày.
- Mục `legal`: chặn thêm `recipient`, `name`, `phone`, `street` khi gửi hãng. Mục `operations`: điều kiện dừng số 4 khớp phạm vi theo kho, thêm điều kiện dừng số 5 (lỗi hãng 7 ngày) và số 6 (phê duyệt không hợp lệ).
- Runbook 1–3 và giờ cao điểm khớp con số trong config; đo chi phí khi thêm người trực thứ hai.

### Bằng chứng

- `R-base-after-20261118-153103-610c87`: sau khi sửa `operations`/`legal`, 110/110, hoàn sai 0 · lỗi oan 0 · lộ dữ liệu 0, chờ lâu nhất 0 phút, 4.456đ/ticket, ROI 1.24.
- `R-base-after-20261118-153114-bb48a9`: thử 2 người trực (12 ca/giờ) → 5.820đ/ticket, ROI 0.72 (config đã trả về 1 người).
- `--adhoc` đơn quà `O-1026`/`C-10` ở mốc `after`: `GỬI HÃNG` chỉ còn `order_id`, `parcel_id`, `district`, `delay_days`.
- Commit P4: `c0c389a` (Phiếu B B4, B5, B6, B7.5, B7.6; `config/operating_gates.json` mục `operations`, `legal`).

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

### Bằng chứng

- `R-base-after-20261118-145831-4675a2`: sau khi đổi `pilot_scope` sang 4 kho, 110/110, hoàn sai 0 · lỗi oan 0 · lộ dữ liệu 0, 4.456đ/ticket, ROI 1.24, tổng hoàn tự động 155.000đ/ngày, `vượt trần: không`; 13 unit test qua.
- B8 dùng `R-base-before-20261118-120241-e347b3` (mốc base) và `R-base-prepared-20261118-155119-c6f842` (prepared, chốt `cee42672`): 9/9 ngưỡng đã ký đạt.
- Commit P3: `8d85e30` (B3, B6 kinh doanh, B7.4, `pilot_scope`), `a53e646` (B8 quyết định v1).
- Thẻ sự cố, mã lần chạy vòng 2 cho C5/C7/C12: `PENDING Sx`.

### Sử dụng AI

Claude Code hỗ trợ đọc `data/world.json` và `lab10/ops.py`, chạy `lab10.eval`/`lab10.gate`, tính drift v3 → v4 và soạn nội dung các mục phiếu.

### Exit ticket

- Điều học được: Quyết định Gate 1 phải đọc đúng câu chữ của `decision_rule` đã ký, không chỉ nhìn 9 ngưỡng xanh. Bộ nền đạt hết nhưng chưa có gói sự cố và chưa có đơn kho sỉ, nên "Thu hẹp" mới là quyết định con số đỡ được.
- Điều còn chưa chắc: Trần tự hoàn 1.000.000đ/ngày được ước theo 155.000đ/ngày của bộ nền đều đặn; chưa biết khi REFUND-v4 có hiệu lực cùng lúc với ngày sale (ticket ×3) thì tổng hoàn và tỉ lệ chuyển người còn trong ngưỡng hay không.
