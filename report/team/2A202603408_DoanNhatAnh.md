# Báo cáo cá nhân — Đoàn Nhật Anh — 2A202603408

## 1. Thông tin thành viên

- Họ tên: Đoàn Nhật Anh.
- MSSV: 2A202603408.
- Email: nhatanhdoan1@gmail.com.
- Vai trong nhóm: Người 2 — kiểm số, bảng chi phí và code D1; tiếp nhận phần code theo phân công sau giải lao.
- Repo nhóm: https://github.com/Dovanngoc05/K5-L3A-DAY13-4people-LaunchEconomics

## 2. Phần việc phụ trách

- Đọc công thức và kiểm tra nguyên tắc tính chi phí: tử số gồm mọi lần chạy, kể cả lỗi; mẫu số chỉ gồm yêu cầu có `ket_qua == 'thanh_cong'`.
- Hoàn thiện bảng chi phí A1–A4, B1–B4, có cách tính để đối chiếu và nhãn `simulated` cho số dùng phút giả lập.
- Viết D1 đủ năm câu về cỡ mẫu; bổ sung code tính ba chỉ số E và tỷ lệ mở lại để bàn giao cho người 3–4.
- Đối chiếu code A–B của người 1 sau tích hợp; kiểm tra chương trình chạy từ đầu đến cuối và chuẩn bị kết quả cho hồ sơ pilot.

## 3. Đóng góp cụ thể

- Xây dựng `src/kiem_tra_so_lieu.py` với sự hỗ trợ của Codex, dùng bộ cộng độc lập dựa trên `csv` để đối chiếu `mo_hinh` dùng pandas của nhóm.
- Điền A2 đủ 9 dòng, A3 đủ 4 loại, A4 đủ 2 mức khối lượng, B1 đủ 9 kịch bản và B2–B4 trong `bang_chi_phi.md`.
- Ghi phép tính đối chiếu A2: (245.585,13 + 84.000 + 1.780.000 + 2.264.000) / 978 = **4.471,97 đ/việc thành công (simulated)**; tử số tính đủ 1.624 run.
- Kiểm tra B3 có cộng chi phí xử lý thủ công cho mọi yêu cầu không thành công: giới hạn 2 lần có tổng **6.901.220,23 đ (simulated)**, thấp hơn giới hạn 1 hoặc 3 lần.
- Bổ sung `co_mau` và `co_mau_d1` trong `src/lab13.py`: +5 điểm cần **1.251 yêu cầu/nhóm**; theo nhân viên với m = 75 cần **42 người/nhóm**, vượt nguồn lực 40 người tổng cộng.
- Ghi kết quả D1 vào chú thích `pilot_plan.yaml`: với 20 nhân viên/nhóm, +6 điểm cần **299 yêu cầu/người**, DE = **6,96**; power xấp xỉ **0,64** nếu tác động thật chỉ +5 điểm.
- Tính chỉ số trong đợt chạy thử: đóng trong 24 giờ và không mở lại 7 ngày **994/1.200 = 82,83%**; bỏ qua gợi ý **48/177 = 27,12%**; mở lại **51/1.200 = 4,25%**.
- Bổ sung tỷ lệ mở lại trong phạm vi `noi_dia + hang_nang`: **39/982 = 3,97%**, để người 4 kiểm tra ngưỡng an toàn; ghi kết quả và đánh đổi trong `ket_qua_kiem_tra.md`.
- Trong phiên làm việc có Codex hỗ trợ, đã ghép cập nhật A–B từ `origin/main`, xử lý xung đột, chạy kiểm số và push bản tích hợp lên `main`.

## 4. Bằng chứng

| Bằng chứng | Nội dung |
| --- | --- |
| [bang_chi_phi.md](bang_chi_phi.md) | A1–A4, B1–B4; phép tính đối chiếu, nguồn số và nhãn `simulated` |
| [kiem_tra_so_lieu.py](../../src/kiem_tra_so_lieu.py) | Bộ cộng độc lập, kịch bản độ nhạy, chỉ số E và đối chiếu tự động với `mo_hinh` |
| [lab13.py](../../src/lab13.py) | Các hàm D1 và nhánh chạy `--nguoi-2`; giữ phần A–B do người 1 cung cấp |
| [pilot_plan.yaml](pilot_plan.yaml) | Chú thích năm câu D1, đánh đổi cỡ mẫu và tỷ lệ mở lại hiện tại |
| [ket_qua_kiem_tra.md](ket_qua_kiem_tra.md) | Kết quả bàn giao D1, E, trạng thái đối chiếu và việc còn phụ thuộc nhóm |
| [Commit 0620b63](https://github.com/Dovanngoc05/K5-L3A-DAY13-4people-LaunchEconomics/commit/0620b63) | Thêm bộ kiểm số, bảng chi phí và phép tính cỡ mẫu |
| [Commit 7e39d07](https://github.com/Dovanngoc05/K5-L3A-DAY13-4people-LaunchEconomics/commit/7e39d07) | Ghép cập nhật từ nhóm, xử lý xung đột và kiểm tra mô hình tích hợp |

Các lệnh đã chạy thành công trong phiên làm việc, từ thư mục `src/`:

```powershell
python lab13.py
python lab13.py --nguoi-2 --ghi-bao-cao
```

Kết quả: ba phép thử A1 đạt; A2/A3/B1/B2/B3 khớp bộ kiểm số độc lập; các mốc đối chiếu của hướng dẫn nằm trong sai số 2%; YAML đọc được và `git diff --check` không báo lỗi.

## 5. Công cụ AI đã dùng

- Công cụ: Codex trong ứng dụng ChatGPT.
- Mục đích: hỗ trợ đọc đề và phân công, viết code kiểm số và D1, tính số từ CSV, dựng bảng báo cáo, xử lý xung đột Git và chạy các lệnh kiểm tra.
- Cách kiểm chứng đã thực hiện với Codex: ghi phép tính A2 bằng tổng token, tool và phút giả lập; dùng bộ cộng `csv` độc lập so với mô hình pandas; kiểm tra các mốc theo hướng dẫn và ba phép thử A1.
- Toàn bộ kết quả được tính từ CSV và giả định của lab; không tạo nhãn lỗi độc lập hoặc kết quả duyệt chéo. Không nhận phần A–B của người 1 là code do mình viết.
- Các lệnh kiểm tra nêu trên được Codex thực thi trong phiên làm việc. Trước khi nộp, tôi cần tự đọc, chạy lại và giải thích được công thức; báo cáo này chưa xác nhận bước tự kiểm tra ngoài phiên hỗ trợ.

## 6. Tự đánh giá

Phần kiểm số, bảng chi phí, D1 và số liệu E đã có kết quả kiểm tra bằng code. Điểm cần giải thích rõ là giới hạn chạy cho CPS thấp nhất (**1 lần**) khác giới hạn rẻ nhất cho công ty (**2 lần**, chi phí simulated).

Đã chạy chương trình tích hợp từ đầu đến cuối; còn cần đối chiếu với chỉ số, pilot và hồ sơ launch khi người 3–4 hoàn thiện, đồng thời kiểm tra chạy trên máy khác trước khi nộp.

Chưa ghi nhận việc trình bày hội đồng, duyệt chéo hoặc tự nộp LMS.
