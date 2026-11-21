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

## Hai bộ nhãn — đánh giá tham khảo CP3

Người gắn nhãn 1: Nguyễn Hữu Đức — 2A202603429 (có hỗ trợ AI) · Người gắn nhãn 2: Đỗ Văn Ngọc — 2A202603391 

| Ca | Nhãn người 1 | Nhãn người 2 (tham khảo) | So với người 1 | Lý do ngắn |
| -: | --------------- | ------------------------- | --------------- | ------------ |
| 1 | Do người dùng | Do người dùng | Trùng | Khách nhập thiếu chữ số; ngân hàng từ chối lệnh. |
| 2 | Hệ thống | Hệ thống | Trùng | Agent chọn sai tham số bảng giá và hoàn thiếu tiền. |
| 3 | Ngữ cảnh | Ngữ cảnh | Trùng | Hoàn về ví đúng thiết kế, nhưng khác kỳ vọng khách về tài khoản ngân hàng. |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Không có dữ liệu chặng của hãng nước ngoài. |
| 5 | Ngầm | Ngầm | Trùng | Hoàn sai giá nhưng khách và hệ thống không phát hiện; kiểm tra mẫu mới tìm ra. |
| 6 | Do người dùng | Do người dùng | Trùng | Khách chọn sai luồng so với mô tả hàng bị vỡ. |
| 7 | Hệ thống | Hệ thống | Trùng | Báo hoàn thành dù API ghi sổ thất bại sau các lần thử lại. |
| 8 | Hệ thống | Hệ thống | Trùng | Agent viện dẫn điều khoản không tồn tại trong chính sách hiện hành. |
| 9 | Do người dùng | Do người dùng | Trùng | Khách nhập mã sàn thay vì mã vận đơn; thiếu gợi ý là điểm cần sửa của sản phẩm. |
| 10 | Ngữ cảnh | Ngữ cảnh | Trùng | Từ chối đúng điều khoản, nhưng xung đột với cam kết 24 giờ hiển thị trên ứng dụng. |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Đầu vào thoại không được hệ thống hỗ trợ. |
| 12 | Ngầm | Ngầm | Trùng | Dữ liệu thiếu làm phát sinh chi phí lặp; không ai phát hiện trong ba tuần. |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Yêu cầu ngoài phạm vi; trợ lý không nêu giới hạn và trả lời lạc đề. |
| 14 | Do người dùng | Do người dùng | Trùng | Khách bấm xác nhận nhầm khiến yêu cầu đóng. |
| 15 | Hệ thống | Hệ thống | Trùng | Tính 100% thay vì 50%; nhân viên phát hiện trước khi gửi. |
| 16 | Ngữ cảnh | Ngữ cảnh | Trùng | Gửi đúng quy tắc “ngay khi xong” nhưng thời điểm 2:14 sáng không phù hợp hoàn cảnh. |
| 17 | Ngầm | Ngầm | Trùng | Cache bảng giá cũ gây lệch tiền; lỗi chỉ được nêu là không ai phát hiện trong mô tả. |
| 18 | Ngữ cảnh | Ngữ cảnh | Trùng | Số tiền đúng nhưng thiếu phép tính nên khách hiểu là hoàn thiếu. |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Trùng | Dữ liệu chỉ truy cập được 12 tháng; trợ lý đã báo giới hạn và chuyển người. |
| 20 | Hệ thống | Hệ thống | Trùng | Thiếu khóa chống trùng khiến hệ thống hoàn tiền hai lần. |

**Đánh giá:** theo tiêu chí đã ghi trong file, cả 20 nhãn người 1 đều hợp lý; các nhãn người 2 tham khảo cũng trùng cả 20. Tuy nhiên, vì người 2 đã xem nhãn người 1 và phần giải thích trước khi quyết định, **20/20 (100%) chỉ là mức trùng khi rà soát, không phải tỉ lệ đồng thuận độc lập của bài CP3**. Không dùng kết quả này để tuyên bố đã đạt yêu cầu gắn nhãn độc lập ≥80%.

### Các ca cần lưu ý khi chấm

- **Ca 1, 6, 9, 14:** nhãn Do người dùng dựa vào đầu vào/lựa chọn sai được mô tả trực tiếp. Việc hệ thống nên xác thực, gợi ý hoặc xác nhận lại là biện pháp giảm lỗi, không làm đổi nguyên nhân của ca theo cách phân loại hiện tại.
- **Ca 4, 11, 13, 19:** Giới hạn hệ thống áp dụng khi thiếu dữ liệu, không hỗ trợ loại đầu vào hoặc yêu cầu ngoài phạm vi. Ở ca 13, câu trả lời lạc đề là biểu hiện cần khắc phục; nguyên nhân phân loại vẫn là giới hạn phạm vi.
- **Ca 5, 12, 17:** Ngầm chỉ dùng khi lỗi chưa bị khách hoặc hệ thống nhận ra vào thời điểm xảy ra và chỉ lộ qua kiểm tra/đối soát sau đó.
- **Ca 10, 16, 18:** Ngữ cảnh là khi hành vi đúng theo thiết kế/chính sách nhưng kỳ vọng, thời điểm hoặc cách diễn đạt không phù hợp hoàn cảnh khách.
- **Ca 2, 7, 8, 15, 20:** Hệ thống vì xử lý, viện dẫn chính sách hoặc thực thi sai; ca 15 vẫn là lỗi hệ thống dù nhân viên chặn được trước khi gửi.

**Đồng thuận độc lập CP3:** chưa đo được. Muốn có số hợp lệ, cần một thành viên chưa xem bộ nhãn 1 và lý do ở trên tự gắn đủ 20 ca trước khi đối chiếu. Khi đó tính số ca trùng / 20; nếu chưa thể tổ chức lượt độc lập, báo đây là rà soát tham khảo và không ghi 100% là kết quả đồng thuận.
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

**Việc còn thiếu:** một lượt gắn nhãn độc lập mù để đo đồng thuận theo yêu cầu CP3. Phần rà soát tham khảo ở trên chưa thay thế lượt này. Nếu có lượt độc lập, ghi kết quả so nhãn và quy tắc cho các ca bất đồng; ngưỡng yêu cầu là ít nhất 16/20 = 80%.
