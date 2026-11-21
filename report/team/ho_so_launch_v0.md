# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm: 4people · Lớp: L3A · Đây là đề xuất kế hoạch pilot; số từ dữ liệu lab và cột `_simulated` được đánh dấu **simulated**.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.471,97 đ/việc thành công; 978/1.200 yêu cầu thành công (simulated) | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: CPS +51,77%; xem lại ×2: +40,70%; lương +25%: +23,12% (simulated) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | 12.000 đ/yêu cầu; cả hệ thống theo B3 là 5.864,65 đ/yêu cầu (simulated), chưa tính chi phí cố định ở dòng này | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng, an toàn | 82,83%; 27,12%; mở lại 4,25% toàn mẫu và 3,97% trong phạm vi (simulated); chưa có đối chứng | Giả lập | Người phụ trách chỉ số |
| 5 · Bảng lỗi và cách khắc phục | Có tiêu chí và 5 biện pháp dự thảo; chưa có bộ nhãn thứ hai hợp lệ, đồng thuận chưa tính | Chưa | Hai người gắn nhãn |
| 6 · Pilot plan | `noi_dia` + `hang_nang`; 20 staff/nhánh; MDE 6 điểm; 859 hiệu dụng/nhánh; power ≈0,64 nếu tác động thật là 5 điểm | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 làm CPS lên 6.786,90 đ; xem lại 100% ở 15,3 phút làm CPS lên 12.414,79 đ (simulated) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất dự thảo: Go có điều kiện** cho pilot giới hạn `noi_dia` và `hang_nang`; đây chưa phải quyết định cuối của nhóm.

- Trước khởi động: hoàn tất đối soát idempotency và sổ cái; người phụ trách: Kỹ sư trưởng agent; hạn: trước ngày bắt đầu pilot.
- Trước khởi động: Giám đốc vận hành chấp thuận MDE 6 điểm và power khoảng 0,64 nếu tác động thật chỉ 5 điểm; hạn: trước ngày bắt đầu pilot.
- Trong tuần đầu: bật đủ event có `trace_id`, đo phút xem lại/làm lại thực tế và rà mẫu an toàn; người phụ trách: PM trợ lý hoàn phí; rà soát trước khi mở rollout tiếp.
- Ngày quyết định theo kế hoạch hiện tại: 2027-01-05; nhóm cần xác nhận ngày này khớp lịch pilot.

**Giới hạn:** lượt chạy thử không có nhóm đối chứng nên các tỷ lệ hiện tại không chứng minh trợ lý gây ra cải thiện. Phần phân loại lỗi còn chờ bộ nhãn thứ hai và tỷ lệ đồng thuận; nhóm cần cập nhật hồ sơ sau khi xác nhận kết quả CP3.
