# Báo cáo nhóm · Lab 13 Launch & Economics

> Bản nháp tổng hợp từ các file hiện có. Cần cập nhật phần C, quyết định cuối và kết quả duyệt chéo sau khi nhóm xác nhận.

## 1. Thông tin nhóm

- Tên nhóm: 4people
- Lớp: L3A
- Thành viên và đóng góp: xem `TEAM.md` (cần điền vai lab và đóng góp cụ thể).

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá tính kinh tế của trợ lý hoàn phí LogiX-VN trên 1.200 yêu cầu và 1.624 lần chạy giả lập. Nhóm tính cả token/tool, thời gian nhân viên xem lại và làm lại; phân tích độ nhạy; phân loại lỗi; rồi thiết kế pilot có đối chứng, chỉ số và luật dừng. Tất cả kết quả từ bộ dữ liệu lab được coi là giả lập; không suy ra tác động nhân quả từ đợt chạy thử không có đối chứng.

## 3. Giải pháp

- **A–B:** `src/lab13.py` tính CPS, tách theo loại yêu cầu, chi phí cố định và các kịch bản độ nhạy. `report/team/bang_chi_phi.md` ghi bảng và phép tính đối chiếu. Ba phép thử A1 đạt; bộ kiểm số độc lập ghi kết quả khớp.
- **C:** `report/team/bang_loi.md` có tiêu chí phân loại và đề xuất khắc phục năm loại lỗi. Bộ nhãn người 1 được ghi là có hỗ trợ AI; bộ nhãn người 2 và tỷ lệ đồng thuận còn chờ, nên chưa kết luận CP3 hoàn tất.
- **D:** `report/team/pilot_plan.yaml` chọn phạm vi `noi_dia` + `hang_nang`, phân nhóm theo nhân viên, nêu cỡ mẫu, nguy cơ ảnh hưởng chéo, luật dừng và rollback. YAML đã được người dùng xác nhận đọc thành công.
- **E:** `report/team/chi_so.md` định nghĩa chỉ số, event cần thu và rủi ro kinh tế; `report/team/ho_so_launch_v0.md` tổng hợp bằng chứng và đề xuất có điều kiện. Cần nhóm xác nhận các điều kiện và ngày quyết định.

## 4. Kết quả

Mô hình A–B cho CPS **4.471,97 đ/việc thành công** với 978/1.200 yêu cầu thành công (simulated). Chỉ số quan sát trong dữ liệu là 82,83% đóng trong 24 giờ và không mở lại, 27,12% bỏ qua gợi ý, 4,25% mở lại toàn mẫu (simulated). Pilot mẫu chấp nhận MDE 6 điểm; power xấp xỉ 0,64 nếu tác động thật chỉ 5 điểm. Hồ sơ hiện đề xuất dự thảo **Go có điều kiện**; nhóm cần chốt sau khi hoàn tất CP3 và rà soát điều kiện pilot. Kết quả hội đồng chấm nhóm khác: chờ buổi duyệt chéo.

## 5. Khó khăn và cách xử lý

Với 40 nhân viên, chia cụm không đủ mẫu để phát hiện chênh 5 điểm theo mục tiêu power 0,8. Nhóm dùng phương án mẫu 20 nhân viên mỗi nhánh và MDE 6 điểm, đồng thời công khai power thấp hơn nếu tác động thật chỉ 5 điểm. Chi phí bị chi phối nhiều bởi làm lại và xem lại, nên kế hoạch theo dõi hai khoản này và giới hạn mở rộng bằng luật dừng.

## 6. Tổng hợp đóng góp

- **Đỗ Văn Ngọc (trưởng nhóm, Người 4):** chạy lại A–B và bộ kiểm số; hoàn thiện bản nháp D2/pilot plan; phối hợp tổng hợp hồ sơ launch. Báo cáo cá nhân: `2A202603391_DoVanNgoc.md`. CP3 chưa có bộ nhãn người 2 hợp lệ.
- Đóng góp của ba thành viên còn lại cần được từng người xác nhận trong `TEAM.md` và báo cáo cá nhân. Không ghi nhận lượt gắn nhãn độc lập hoặc kết quả duyệt chéo khi chưa thực hiện.

## 7. Hạn chế và hướng cải thiện

Dữ liệu là giả lập; thử nghiệm ban đầu không có đối chứng; phương án pilot có thể chỉ phát hiện được tác động lớn hơn 6 điểm. Phần C chưa có bộ nhãn thứ hai hợp lệ. Trước quyết định, cần xác nhận phân công, hoàn tất đối chiếu nhãn, thay thời lượng giả lập bằng số đo pilot và xác nhận ngày quyết định.

## 8. Tài liệu tham khảo

- `docs/du_lieu_va_cong_thuc.md`
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`
- `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`
- Google PAIR, *People + AI Guidebook*, mục “Errors + Graceful Failure”.
