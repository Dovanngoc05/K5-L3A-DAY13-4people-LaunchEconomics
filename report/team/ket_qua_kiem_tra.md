# Kết quả kiểm tra số liệu và cỡ mẫu

Chạy trong `src/`: `python lab13.py --nguoi-2`; thêm `--ghi-bao-cao` để cập nhật bảng chi phí và file này.

## D1 · Gửi người 4

| Câu | Cách tính | Kết quả |
| --- | --- | --- |
| a · Theo yêu cầu, +5 điểm | Công thức hai tỉ lệ, alpha 0,05, power 0,8 | 1251 yêu cầu/nhóm |
| b · Theo nhân viên, m=75 | DE=1+74×0,02=2,48 | 3103 yêu cầu/nhóm; 42 nhân viên/nhóm, tổng 84 > 40 |
| c · 20 nhân viên/nhóm | n hiệu dụng < 20/0,02 | Luôn < 1.000, không đủ 1251 |
| d · 6 depot/nhóm | n hiệu dụng < 6/0,02 | Luôn < 300; chỉ 6 cụm/nhóm |
| e · +6 điểm, 20 nhân viên/nhóm | Cần 859; giải 20m/[1+(m−1)×0,02] ≥ 859 | m ≥ 299; DE=6,96; n hiệu dụng=859,20 |

Với phương án e: 20 × 299 = 5.980 yêu cầu/nhóm, tổng 11.960; cần đủ yêu cầu **trong phạm vi pilot**, không lấy tổng công ty thay thế.
Nếu tác động thật chỉ +5 điểm, power xấp xỉ **0,64**, thấp hơn mục tiêu 0,80; người 4 cần ghi đánh đổi và chốt MDE 0,06 nếu chọn phương án này.
Đây là xấp xỉ theo công thức z của đề, không thay thế phân tích cụm chi tiết. Đã điền a–e vào chú thích D1 của `pilot_plan.yaml`; người 4 tự chốt D2 và các trường kế hoạch.

## E · Gửi người 3 và người 4

| Chỉ số trong đợt chạy thử | Tử số / mẫu số | Tỉ lệ |
| --- | --- | ---: |
| Đóng 24 giờ và không mở lại 7 ngày | 994/1200 | 82,83% |
| Bỏ qua gợi ý (sửa + bỏ), chỉ trong ca được xem lại | 48/177 | 27,12% |
| Mở lại 7 ngày, toàn mẫu | 51/1200 | 4,25% |
| Mở lại 7 ngày, noi_dia + hang_nang | 39/982 | 3,97% |

Các tỉ lệ trên không dùng cột phút `_simulated`, nhưng vẫn là dữ liệu lab giả lập; chưa có đối chứng nên không kết luận tác động nhân quả.
Ngưỡng mở lại tuyệt đối 3% thấp hơn cả nền toàn mẫu và phạm vi; người 4 cần cân nhắc so đối chứng +2 điểm và trần 6% theo hướng dẫn.

## Phụ thuộc và kiểm tra cuối

- **Làm ngay:** D1, E, tính tay và bảng chi phí độc lập đã có; không cần chờ người 1, 3 hoặc 4 để tính các phần này.
- **Chờ người 1 để chốt kiểm số:** A1–A2 hiện còn khung; trạng thái lần chạy kiểm tra: **CHỜ: người 1 chưa hoàn thiện A1–A2; bộ kiểm số độc lập đã chạy**. Khi có code, chạy lại cùng lệnh để so mô hình gốc, 9 kịch bản và mọi loại yêu cầu.
- **Chờ người 3–4 để so toàn hồ sơ:** `chi_so.md`, các trường kế hoạch trong `pilot_plan.yaml` và `ho_so_launch_v0.md` còn mẫu; D1 đã được điền nhưng chưa thể xác nhận toàn hồ sơ nhất quán.
- **Bàn giao file chung:** D1 nằm trong `lab13.py`; người 1 cần giữ phần này và nhánh `--nguoi-2` khi ghép A–B. Bộ kiểm số nằm riêng trong `kiem_tra_so_lieu.py` để tránh ghi đè A–B.
- **Trước nộp:** chạy `python lab13.py` từ đầu đến cuối, so số toàn hồ sơ, chạy trên máy khác; đây vẫn là việc cần làm sau tích hợp.

## Ghi nhận công cụ và đóng góp

Đã dùng Codex để đọc yêu cầu, viết bộ cộng độc lập, code D1 và dựng bảng từ CSV; tự kiểm tra bằng phép tính tay A2, ba giá trị A1 và số hướng dẫn (sai số ≤2%).
Bạn cần tự chạy lệnh, kiểm tra công thức và giải thích được các số trước khi nộp; chưa ghi nhận bạn đã làm bước này.
Chưa có họ tên/MSSV nên chưa tạo báo cáo cá nhân đúng tên; khi có thông tin, copy `MSSV_HoTen.md`, ghi đóng góp thực tế và AI đã dùng, rồi cập nhật `TEAM.md`.
