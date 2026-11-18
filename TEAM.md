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
|   3 |           |      |     |             |
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

- Đã đối chiếu offline metric A2 với nội dung ở commit `1d9c999`. Chờ P4 xác nhận một telemetry production dùng chung ở câu 1.4. B6 kỹ thuật và B7.2 đã điền trên Phiếu B. Commit/PR P2: `PENDING`.
- B2: đã tái chạy trace `T-002@55` ở `base` và `after`. Baseline P1 ghi ở B0 là `R-base-before-20261118-120241-e347b3`, chờ bản report và trace của run đó để đối chiếu toàn bộ.
- B7.3: đã chạy BT-01 và BT-02 ở `after`, seed `55`. Cổng chặn khoản hoàn oan ở BT-01. BT-02 vẫn từ chối sai quyền lợi khi khách khai ít hơn tracking DB.
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
