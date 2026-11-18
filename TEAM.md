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
|   4 |           |      |     |             |

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
