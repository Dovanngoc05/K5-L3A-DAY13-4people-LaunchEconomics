# Phân công nhóm 4 người — Lab 13: Launch & Economics

## 1. Mục tiêu và phạm vi

Hoàn thiện bộ hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN từ dữ liệu giả lập gồm 1.200 yêu cầu và 1.624 lần chạy agent. Hồ sơ cần trả lời: chi phí có hợp lý không, nhân viên có dùng không, xử lý lỗi thế nào và pilot có đủ cơ sở để ra quyết định không.

Thực hiện đủ nhiệm vụ A–E, trình hồ sơ trước hội đồng Gate 2a và chấm chéo một nhóm khác. Các mốc giờ dưới đây theo lịch mẫu buổi chiều; nếu lớp học giờ khác thì giữ thứ tự và thời lượng, điều chỉnh theo coach.

## 2. Danh sách và vai trò

Điền tên, MSSV trước khi bắt đầu; cập nhật thông tin tương ứng trong [TEAM.md](TEAM.md).

| Thành viên | Họ tên | MSSV | Vai trò |
| --- | --- | --- | --- |
| Người 1 | Chưa điền | Chưa điền | Người viết code đầu buổi; hỗ trợ tính chỉ số và kiểm tra kỹ thuật |
| Người 2 | Chưa điền | Chưa điền | Người kiểm số; tiếp quản viết code sau giải lao |
| Người 3 | Chưa điền | Chưa điền | Người gắn nhãn 1; phụ trách bảng lỗi, chỉ số và event |
| Người 4 | Chưa điền | Chưa điền | Người gắn nhãn 2 kiêm giữ hồ sơ; điều phối pilot và tổng hợp bài nộp |

## 3. Công việc chi tiết

### Người 1 — Code A–B và hỗ trợ kiểm tra kỹ thuật

- Cài môi trường theo [src/README.md](src/README.md), chạy lệnh trong `src/`.
- Viết ba hàm A1; chỉ làm tiếp khi cả ba phép thử đạt 1,20 · 1,25 · 1,25.
- Hoàn thiện `mo_hinh(runs, reqs, ...)`: tính token, tool, xem lại, làm lại và chi phí mỗi việc thành công.
- Viết phần A3 phân tích bốn loại yêu cầu, A4 chi phí cố định theo hai mức khối lượng.
- Viết phần B: chín kịch bản riêng lẻ, một kịch bản kết hợp, giới hạn 1–2–3 lần chạy và xem lại 100%.
- Chuyển output và cách tính cho người 2 để kiểm tra, điền bảng chi phí.
- Sau giải lao, bàn giao quyền sửa `src/lab13.py` cho người 2; rà soát công thức và hỗ trợ hoàn thiện B.
- Phối hợp với người 2 bổ sung phép tính ba chỉ số E vào code; chuyển kết quả cho người 3. Nếu cần sửa cùng file, thống nhất lượt sửa trước.
- Phối hợp chạy lại chương trình trên máy khác trong nhóm trước khi nộp.

**Đầu ra:** phần A–B trong [src/lab13.py](src/lab13.py), output các bảng và kết quả ba chỉ số E.

**Hoàn thành khi:** A1 đạt cả ba phép thử; A–B có đủ kết quả để lập báo cáo; các số đã được người 2 đối chiếu.

### Người 2 — Kiểm số, bảng chi phí và code D1

- Đọc [docs/du_lieu_va_cong_thuc.md](docs/du_lieu_va_cong_thuc.md); tính tay ít nhất một kết quả, ghi rõ cách tính để đối chiếu với code.
- Kiểm tra tử số tính mọi lần chạy, kể cả lỗi; mẫu số chỉ đếm yêu cầu có `ket_qua == 'thanh_cong'`.
- Điền A1–A4 và B1–B4 vào `report/team/bang_chi_phi.md`; kiểm tra nhãn `simulated` và nguồn số.
- Với B3, cộng cả chi phí nhân viên xử lý yêu cầu không thành công; với A4, ghi rõ khối lượng và chi phí cố định.
- Sau giải lao, tiếp quản code, tự chạy lại mô hình chi phí, hoàn tất B nếu còn thiếu.
- Viết code tính đủ năm câu D1: chia theo yêu cầu, theo nhân viên, giới hạn 20 nhân viên mỗi nhóm, theo depot và mức chênh 6 điểm.
- Chuyển kết quả D1 và các đánh đổi về cỡ mẫu cho người 4; kiểm tra phần chú thích D1 trong kế hoạch pilot.
- Phối hợp bổ sung phép tính chỉ số E và tỉ lệ mở lại hiện tại vào code.
- Kiểm tra code chạy từ đầu đến cuối; đối chiếu số giữa bảng chi phí, chỉ số, pilot và hồ sơ launch.

**Đầu ra:** [report/team/bang_chi_phi.md](report/team/bang_chi_phi.md), phần D1 trong `src/lab13.py` và kết quả đối chiếu.

**Hoàn thành khi:** bảng A2 đủ 9 dòng, A3 đủ 4 loại, A4 đủ 2 mức khối lượng; B1 đủ 9 kịch bản; B2–B4 có kết quả; D1 đủ 5 câu. Số đối chiếu nằm trong sai số 2% theo đề.

### Người 3 — Gắn nhãn 1, bảng lỗi, chỉ số và event

- Đọc đề, theo dõi điều kiện hoàn thành của từng nhiệm vụ để nhắc nhóm phần còn thiếu.
- Chuẩn bị khung chỉ số, event và bảng lỗi trước CP3.
- Tại CP3, tự gắn nhãn đủ 20 ca trong 8 phút, không trao đổi và không xem nhãn của người 4 hoặc nhãn tham khảo trước khi hoàn tất.
- Sau khi cả hai hoàn tất, so nhãn, tính tỉ lệ đồng thuận, giữ nguyên hai bộ nhãn ban đầu; ghi nhãn thống nhất và quy tắc phân biệt cho các ca bất đồng.
- Cùng người 4 chọn 5 ca thuộc đủ 5 loại lỗi; ghi cách phát hiện đo được, cách khắc phục và vai trò phụ trách.
- Tổng hợp `bang_loi.md`; nếu đồng thuận dưới 80%, ghi lại định nghĩa đã sửa theo hướng dẫn.
- Hoàn thiện `chi_so.md`: ba chỉ số có kết quả tính từ code hoặc tính tay có cách tính; thêm một chỉ số dùng và một chỉ số an toàn.
- Liệt kê ít nhất sáu event, mỗi event có tên, bên tạo, thuộc tính, thời điểm và `trace_id`; chỉ rõ event dùng để tính từng chỉ số.
- Viết ít nhất hai dòng rủi ro kinh tế, lấy số từ bảng độ nhạy đã được người 2 kiểm tra.
- Ghi `phieu_cham.md` khi nhóm làm hội đồng, dựa trên hồ sơ và trao đổi thực tế với nhóm được chấm.

**Đầu ra:** [report/team/bang_loi.md](report/team/bang_loi.md), [report/team/chi_so.md](report/team/chi_so.md), [report/team/phieu_cham.md](report/team/phieu_cham.md).

**Hoàn thành khi:** có hai bộ nhãn độc lập và tỉ lệ đồng thuận; bảng khắc phục đủ năm loại; bảng chỉ số đủ năm dòng, ba dòng đầu có kết quả; đủ event và rủi ro. Phiếu chấm được ghi sau duyệt chéo thực tế.

### Người 4 — Gắn nhãn 2, kế hoạch pilot và hồ sơ tổng hợp

- Điều phối điền thông tin nhóm trong `TEAM.md`; chuẩn bị hồ sơ launch từ đầu buổi và cập nhật dần bằng kết quả đã kiểm tra.
- Tại CP3, tự gắn nhãn đủ 20 ca trong 8 phút, độc lập với người 3; giữ nguyên bộ nhãn ban đầu sau khi so sánh.
- Cùng người 3 thống nhất các ca bất đồng và xây bảng khắc phục năm loại lỗi.
- Chủ trì `pilot_plan.yaml`, nhận kết quả A3, B và D1 từ người 1–2 trước khi chốt phạm vi, cách chia và luật dừng.
- Ghi đủ năm câu D2 về khả năng tách tác động; ghi rõ đánh đổi nếu thiết kế chưa đáp ứng đầy đủ mục tiêu.
- Điền owner, scope, assignment, rollout, cỡ mẫu, identifiability, interim_looks, rollback, decision_date và simulated_inputs.
- Viết ít nhất ba luật dừng về an toàn, chi phí và mức độ sử dụng; mỗi luật đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có vai trò thực hiện rõ ràng.
- Dùng tỉ lệ mở lại hiện tại đã tính từ dữ liệu để kiểm tra ngưỡng an toàn trước khi chốt kế hoạch.
- Hoàn thiện hồ sơ launch một trang, đủ bảy mục: con số chính, trạng thái và vai trò phụ trách. Chốt đề xuất Go / Go có điều kiện / No-go theo bằng chứng; điều kiện phải có người phụ trách và ngày kiểm tra.
- Tổng hợp báo cáo nhóm tối đa hai trang; cập nhật đóng góp, tập hợp báo cáo cá nhân và điều phối commit, push.

**Đầu ra:** [report/team/pilot_plan.yaml](report/team/pilot_plan.yaml), [report/team/ho_so_launch_v0.md](report/team/ho_so_launch_v0.md), [report/team/group_report.md](report/team/group_report.md), [TEAM.md](TEAM.md).

**Hoàn thành khi:** YAML đọc được bằng `yaml.safe_load`, không còn chỗ cần điền; hồ sơ đủ bảy mục, có đề xuất nhất quán với số; thông tin và đóng góp từng thành viên được ghi rõ.

## 4. Tiến độ và bàn giao

| Thời gian mẫu | Người 1 | Người 2 | Người 3 | Người 4 | Mốc chung |
| --- | --- | --- | --- | --- | --- |
| 14:00–14:10 | Cài môi trường, mở code | Chuẩn bị kiểm số, mở bảng chi phí | Đọc yêu cầu và tiêu chí | Điền thông tin nhóm, dựng hồ sơ | Chốt vai trò |
| 14:10–14:53 — A | Viết A1–A4 | Kiểm số, điền A1–A4 | Soát yêu cầu, chuẩn bị khung E | Cập nhật hồ sơ, chuẩn bị pilot | A1 đạt; bảng A đủ |
| 14:53–15:20 — B | Viết code B | Kiểm và điền B1–B4 | Chuẩn bị event, bảng lỗi | Cập nhật hồ sơ từ A–B | Có bảng độ nhạy |
| 15:20–15:35 | Giải lao | Giải lao | Giải lao | Giải lao | Đổi người viết code sau giải lao |
| 15:35–16:08 — C | Rà soát, hỗ trợ hoàn thiện B | Tiếp quản code, hoàn tất B | Gắn nhãn độc lập, sau đó tổng hợp C | Gắn nhãn độc lập, sau đó cùng hoàn thiện C | Hai bộ nhãn, đồng thuận, 5 cách khắc phục |
| 16:08–16:36 — D | Hỗ trợ tính chỉ số E | Viết D1, tính chỉ số và tỉ lệ mở lại | Hoàn thiện event, rủi ro | Chốt D2 và kế hoạch pilot | Pilot đủ trường và luật dừng |
| 16:36–17:00 — E | Kiểm kết quả tính | Đối chiếu số toàn bộ hồ sơ | Chốt chỉ số, event và rủi ro | Chốt hồ sơ và đề xuất | Hồ sơ sẵn sàng lúc 17:00 |
| 17:00–17:45 | Giải thích mô hình chi phí | Bảo vệ số liệu và cỡ mẫu | Ghi phiếu chấm nhóm khác | Trình hồ sơ, ghi phản hồi nhận được | Hoàn thành duyệt chéo thực tế |
| 17:45–18:00 | Kiểm tra chạy trên máy khác | Soát số và nhãn simulated | Soát danh sách file | Tổng hợp, điều phối commit và push | Có bản bài làm tại lớp |

## 5. Nguyên tắc phối hợp

- Trước giải lao, người 1 giữ lượt sửa `src/lab13.py`; sau giải lao người 2 tiếp quản. Khi cần hỗ trợ sửa, thống nhất trước để tránh ghi đè.
- Người 1–2 bàn giao output kèm phạm vi dữ liệu, giả định và cách tính; người 3–4 dùng cùng bộ số đã kiểm tra.
- Phần A là đầu vào của B; A3 và D1 là đầu vào của pilot; A–D là đầu vào của hồ sơ launch. Không chốt đề xuất trước khi kiểm tra các phần này.
- Hai người gắn nhãn không trao đổi, không xem nhãn của nhau hoặc nhãn tham khảo cho đến khi cả hai hoàn thành 20 ca. Không sửa hai bộ nhãn gốc sau khi so.
- Bốn thành viên cùng duyệt và chịu trách nhiệm giải thích bài. Người giữ file tổng hợp không thay thế trách nhiệm kiểm tra của người cung cấp số liệu.
- Người phụ trách trong hồ sơ pilot phải là vai trò có quyền thực hiện hoặc quyết định, ví dụ PM, trưởng nhóm CSKH, giám đốc vận hành; không ghi chung là “cả đội”.

## 6. Việc mỗi thành viên tự làm

- Copy [report/team/MSSV_HoTen.md](report/team/MSSV_HoTen.md) thành file riêng theo tên `MSSV_HoTen.md`, giữ nguyên file mẫu.
- Ghi phần phụ trách, đóng góp thực tế, bằng chứng từ file/commit/kết quả và công cụ AI đã dùng cùng cách tự kiểm tra.
- Cung cấp thông tin đóng góp để cập nhật `TEAM.md`.
- Tự nộp cùng link repo nhóm trên LMS bằng tài khoản cá nhân. Nhóm push bài không thay cho bước nộp cá nhân.

## 7. Checklist trước khi nộp

- [ ] Repo đúng mẫu `K5-L3A-DAY13-TenNhom-LaunchEconomics` hoặc mẫu L3B; public hoặc đã cấp quyền cho giảng viên.
- [ ] `TEAM.md` đủ thông tin, vai và đóng góp của bốn người.
- [ ] `src/lab13.py` chạy hết trong `src/` trên một máy khác; ba phép thử A1 đạt.
- [ ] Đủ sáu file hồ sơ: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md` trong `report/team/`.
- [ ] Có `report/team/group_report.md` và bốn báo cáo cá nhân đúng tên.
- [ ] Mọi con số tính từ cột `_simulated`, kể cả tổng và tỉ lệ dẫn xuất, có nhãn `simulated`.
- [ ] Số liệu do code nhóm tính hoặc tính tay có ghi cách tính; không bịa nhãn độc lập hay kết quả duyệt chéo.
- [ ] YAML đọc được, không còn dấu hỏi trong các trường; ít nhất ba luật dừng đủ bốn vế.
- [ ] Hồ sơ launch một trang, đủ bảy mục, đúng trạng thái và vai trò phụ trách; dòng cuối là đề xuất của nhóm.
- [ ] Không dùng từ bị cấm ở quy tắc 5 trong `README.md` trong các file hồ sơ.
- [ ] Không sửa hai CSV hoặc bản gốc `src/lab13_starter.py`; không commit secret, `.env` hoặc môi trường ảo.
- [ ] Đã push bài, kiểm tra người chấm mở được repo; cả bốn người đã nộp link lên LMS.

## 8. Mốc nộp và tiêu chí chấm

- **17:00:** hồ sơ sẵn sàng để duyệt chéo theo lịch mẫu.
- **17:45–18:00:** đóng gói, commit và push bản làm tại lớp.
- **Deadline chính thức:** trước **23:59 GMT+7 ngày lab**, theo [SUBMISSION.md](SUBMISSION.md); gia hạn chỉ theo thông báo của coach. Mốc nộp 18:00 trong tài liệu gốc đã được quy định nộp tại root repo thay thế.
- **Điểm:** A 20, B 15, C 10, D 15, E 10; hội đồng 30. Chi tiết tại [RUBRIC.md](RUBRIC.md).

Nguồn phân công: [README.md](README.md), [TEAM.md](TEAM.md), [CHECKPOINTS.md](CHECKPOINTS.md), [RULES.md](RULES.md), [SUBMISSION.md](SUBMISSION.md), [hướng dẫn chi tiết](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) và đề bài gốc trong `docs/`.
