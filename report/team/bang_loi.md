# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Phần chuẩn bị của người 3

Bộ nhãn ở cột **Nhãn người 1** được điền theo yêu cầu với hỗ trợ AI đã đọc tài liệu tham khảo. Việc này chưa chứng minh một lượt gắn nhãn độc lập trong 8 phút. Người gắn nhãn 2 cần hoàn tất bộ nhãn riêng trước khi so; giữ nguyên nhãn ban đầu sau khi đối chiếu.

| Loại | Tiêu chí nhận biết |
| --- | --- |
| Do người dùng | Nguyên nhân gốc là đầu vào hoặc lựa chọn sai của người dùng |
| Hệ thống | Xử lý sai thiết kế/chính sách và lỗi đã lộ ra |
| Ngữ cảnh | Xử lý đúng thiết kế/chính sách nhưng giả định không phù hợp hoàn cảnh |
| Giới hạn hệ thống | Thiếu dữ liệu, ngoài phạm vi hoặc không xử lý được đầu vào |
| Ngầm | Sai tồn tại nhưng chỉ được phát hiện qua kiểm tra, chưa có khách hoặc hệ thống nhận ra |

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Hữu Đức — 2A202603429 (có hỗ trợ AI) · Người gắn nhãn 2: chờ bổ sung bộ nhãn riêng.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| -: | --------------- | --------------- | ------- | ------------------ |
| 1 | Do người dùng | ... | ... | ... |
| 2 | Hệ thống | ... | ... | ... |
| 3 | Ngữ cảnh | ... | ... | ... |
| 4 | Giới hạn hệ thống | ... | ... | ... |
| 5 | Ngầm | ... | ... | ... |
| 6 | Do người dùng | ... | ... | ... |
| 7 | Hệ thống | ... | ... | ... |
| 8 | Hệ thống | ... | ... | ... |
| 9 | Do người dùng | ... | ... | ... |
| 10 | Ngữ cảnh | ... | ... | ... |
| 11 | Giới hạn hệ thống | ... | ... | ... |
| 12 | Ngầm | ... | ... | ... |
| 13 | Giới hạn hệ thống | ... | ... | ... |
| 14 | Do người dùng | ... | ... | ... |
| 15 | Hệ thống | ... | ... | ... |
| 16 | Ngữ cảnh | ... | ... | ... |
| 17 | Ngầm | ... | ... | ... |
| 18 | Ngữ cảnh | ... | ... | ... |
| 19 | Giới hạn hệ thống | ... | ... | ... |
| 20 | Hệ thống | ... | ... | ... |

**Tỉ lệ đồng thuận:** chưa tính, chờ bộ nhãn người 2; không suy ra đồng thuận từ bộ nhãn người 1.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Chưa xác định các ca bất đồng vì chưa có bộ nhãn người 2. Sau khi so, ghi một câu phân biệt cho mỗi ca bất đồng.

### Giải thích các ca dễ nhầm trong bộ nhãn người 1

- Ca 6 và 9: nguyên nhân gốc là khách chọn sai mục hoặc nhập sai loại mã; hướng dẫn và phát hiện mâu thuẫn thuộc biện pháp cải thiện.
- Ca 8 và 15: lỗi đã hiện trong câu trả lời hoặc được nhân viên bắt được, nên xếp Hệ thống.
- Ca 12: kết quả đúng nhưng chi phí tăng kéo dài không ai nhận ra, nên xếp Ngầm; lỗi có thể nằm ở chi phí.
- Ca 13: yêu cầu nằm ngoài phạm vi trợ lý, nên xếp Giới hạn hệ thống; cách giải thích giới hạn cần cải thiện.
- Ca 18: số tiền đúng chính sách nhưng thiếu cách tính làm khách hiểu nhầm, nên xếp Ngữ cảnh.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

|  Ca | Loại lỗi            | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --------------------- | --------------------- | --------------------- | -------------- |
| 9 | Do người dùng | Hằng ngày: yêu cầu có `input_validation_failed.reason_code = wrong_id_type` / tổng yêu cầu; cảnh báo khi >2% | Nhận diện loại mã; hướng dẫn lấy mã vận đơn hoặc tra ánh xạ mã sàn nếu có; cho khách sửa đầu vào | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: `refund_confirmation_sent.claim_status = completed` không có giao dịch sổ cái thành công cùng `transaction_id`; ≥1 ca thì cảnh báo | Chỉ xác nhận khi sổ cái báo thành công; lỗi kéo dài thì báo đang xử lý và chuyển nhân viên; kiểm tra khóa chống trùng khi thử lại | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Hằng tuần: yêu cầu mở lại vì thắc mắc tiền nhưng kiểm tra thấy tiền đúng / tổng yêu cầu đóng đủ theo dõi; cảnh báo khi >1% | Tin nhắn ghi phí gốc, tỉ lệ và phép tính: 30.000 đ × 50% = 15.000 đ; thêm cách yêu cầu giải thích | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Hằng ngày: kiểm tra ca `handoff_to_staff.reason_code = beyond_retention` có thông báo giới hạn và tóm tắt; ≥1 ca thiếu thì cảnh báo | Nói rõ chỉ tra được 12 tháng; giữ luồng chuyển nhân viên kèm tóm tắt và tuyến tra lịch sử | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra ngẫu nhiên 100 yêu cầu/tuần theo bảng giá đúng thời điểm; ≥1 ca lệch tiền hoặc sai phiên bản thì cảnh báo | Xóa cache khi đổi bảng giá; ghi phiên bản trong trace; rà yêu cầu chịu ảnh hưởng và điều chỉnh qua kế toán | Kế toán trưởng |

**Trạng thái bảng khắc phục:** đề xuất chuẩn bị trước, chưa thống nhất với người 4. Ngưỡng phát hiện là đề xuất, chưa phải số quan sát hoặc luật dừng đã duyệt. Đối chiếu event với [chi_so.md](chi_so.md) trước triển khai.

**Phần chờ:** bộ nhãn người 2, số ca trùng, quy tắc cho bất đồng và nhãn thống nhất. Công thức đồng thuận = số ca trùng / 20 × 100%; mục tiêu ít nhất 16/20 = 80%. Chưa có đủ dữ liệu để tính.
