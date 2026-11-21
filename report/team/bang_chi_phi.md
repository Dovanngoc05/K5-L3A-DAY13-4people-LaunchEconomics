# Bảng chi phí · Nhiệm vụ A và B

Nguồn: hai CSV gốc; tính bằng `src/kiem_tra_so_lieu.py` theo công thức của đề. Chạy trong `src/`: `python lab13.py --nguoi-2 --ghi-bao-cao`.

Đây là bộ kiểm số độc lập của người 2; đối chiếu với `mo_hinh` bằng lệnh chạy trên. Dữ liệu lab là giả lập; mọi tổng, chi phí và tỉ lệ chi phí chứa phút giả lập đều mang nhãn **simulated**.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Tính tay |
| --- | ---: |
| Tối đa 2 lần: 1 + (1 − 0,8) | 1,20 |
| Chạy đến khi đúng: 1 / 0,8 | 1,25 |
| Tối đa 3: (1 + 0,2 + 0,04) / (1 − 0,2³) | 1,25 |

Đây là kết quả kiểm số; lệnh chạy trên cũng kiểm tra ba assert A1 của nhóm.

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) / số việc | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,13 | Tổng tokens_in × 26/1.000 + tokens_out × 130/1.000, mọi run | đo từ trace |
| Tool | 84.000,00 | Tổng tool_calls × 15, mọi run | đo từ trace |
| Trong đó, lần chạy thứ 2 và 3 | 93.804,49 | Token + tool với attempt > 1; đã nằm trong hai dòng trên | đo từ trace |
| Xem lại | 1.780.000,00 | Tổng phut_xem_lai_simulated × 2.000 | simulated |
| Làm lại | 2.264.000,00 | Tổng phut_lam_lai_simulated × 2.000 | simulated |
| Tổng chi phí | 4.373.585,13 | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978,00 | ket_qua == thanh_cong | đếm yêu cầu |
| Chi phí mỗi việc thành công | 4.471,97 | Tổng / số việc thành công | simulated |
| Hoá đơn token và tool / số yêu cầu | 274,65 | Token + tool chia 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,28 lần** hoá đơn/yêu cầu (simulated).
- Làm lại lớn nhất: **51,77%**; tổng giờ nhân viên chiếm **92,46%** (simulated).

### Tính tay để đối chiếu

- Token = 5.771.712 × 26/1.000 + 734.774 × 130/1.000 = **245.585,13 đ**; tool = 5.600 × 15 = **84.000 đ**.
- Tổng = 245.585,13 + 84.000 + 1.780.000 + 2.264.000 = **4.373.585,13 đ**; chia 978 = **4.471,97 đ/việc thành công** (simulated).
- Tử số tính đủ **1624 run**, kể cả lỗi; mẫu số chỉ **978/1200** yêu cầu thành công. Dòng chạy lại là phần nằm trong token + tool, không cộng hai lần.
- So với người tự làm: (4.373.585,13 + 222 × 12.000)/1.200 = **5.864,65 đ/yêu cầu** (simulated); dùng quy ước B3 cho mọi ca không thành công.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | CPS (đ, simulated) | CPS / 12.000 (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.695,64 | 0,22× |
| hang_nang | 158 | 74,05% | 1,47 | 8.220,73 | 0,69× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515,17 | 1,88× |
| doi_tac | 68 | 54,41% | 1,88 | 10.214,87 | 0,85× |

- `quoc_te`: CPS 22.515,17 đ (simulated); tỉ lệ run ok theo lần 1–2–3 là 30,00% / 11,43% / 2,15%; chạy lại ít hiệu quả.
- Đề xuất phạm vi `noi_dia + hang_nang`; để người 4 chốt pilot. Tỉ số CPS/12.000 ở bảng chỉ là chỉ báo; so chi phí công ty phải cộng xử lý thủ công như B3.

## A4 · Chi phí cố định (noi_dia + hang_nang)

40.000.000 đ/tháng; khối lượng dưới đây là **tất cả yêu cầu công ty**, giữ cơ cấu mẫu: số thành công trong phạm vi = khối lượng × 900/1.200.

| Khối lượng yêu cầu/tháng | Việc thành công trong phạm vi | Cố định/việc (đ) | CPS + cố định (đ, simulated) | / 12.000 (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 45.000 | 33.750 | 1.185,19 | 4.599,09 | 0,38× |
| 22.500 | 16.875 | 2.370,37 | 5.784,27 | 0,48× |

- Cố định không đổi kết luận chỉ báo ở cả 45.000 và 22.500 yêu cầu/tháng; các CPS này chưa cộng xử lý thủ công cho yêu cầu không thành công.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | CPS (đ, simulated) | Thay đổi (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 và 260 đ/1.000 token | 4.723,08 | 5,62% |
| Giá token giảm một nửa | 13 và 65 đ/1.000 token | 4.346,41 | -2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292,01 | 40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại × 0,5 | 3.561,95 | -20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.786,90 | 51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại × 0,5 | 3.314,50 | -25,88% |
| Lương nhân viên tăng 25% | 2.500 đ/phút | 5.505,71 | 23,12% |
| Chỉ cho chạy tối đa 2 lần | attempt ≤ 2; vượt giới hạn: chuyển người, phút = 0 | 4.237,29 | -5,25% |
| Chỉ cho chạy 1 lần | attempt ≤ 1; vượt giới hạn: chuyển người, phút = 0 | 4.110,99 | -8,07% |

## B2 · Đổi một cặp và xếp hạng

- Token × 2 và xem lại × 2: **6.543,12 đ**, tăng **46,31%** (simulated); bằng tổng tác động riêng vì mô hình cộng tuyến tính.
- Ba yếu tố mạnh nhất theo mức tăng đã thử: **1. làm lại; 2. xem lại; 3. lương** (simulated).

## B3 · Giới hạn chạy lại

Cả hệ thống = tổng trợ lý + 12.000 × số yêu cầu không thành công; theo quy ước đề, áp dụng cả `lam_lai` và `chuyen_nhan_vien`.

| Giới hạn | Tổng trợ lý (đ, simulated) | Không thành công | Cả hệ thống (đ, simulated) | CPS trợ lý (đ, simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.780,64 | 319 | 7.449.780,64 | 4.110,99 |
| 2 lần | 4.093.220,23 | 234 | 6.901.220,23 | 4.237,29 |
| 3 lần | 4.373.585,13 | 222 | 7.037.585,13 | 4.471,97 |

- **2 lần** rẻ nhất cho công ty; **1 lần** cho CPS trợ lý thấp nhất nhưng đẩy thêm **85 yêu cầu** sang người so với 2 lần (chi phí simulated).

## B4 · Xem lại 100% trong phạm vi

982 yêu cầu; 948 yêu cầu có ít nhất 1 run ok được xem lại 5 phút; 48 ca làm lại. Token + tool = 224.513,27 đ; chia 900 việc thành công.

| Giả định phút làm lại/ca | Tổng (đ, simulated) | CPS (đ, simulated) | / 12.000 (simulated) | Phút xem lại hoà vốn (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 9,0 | 10.568.513,27 | 11.742,79 | 0,98× | 5,12 |
| 15,3 | 11.173.313,27 | 12.414,79 | 1,03× | 4,80 |

- Trung bình phút làm lại trên toàn bộ ca `lam_lai` trong CSV: **15,2973 phút (simulated)**; dùng 15,3 làm kịch bản độ nhạy theo hướng dẫn.
- Xem lại 100% gần mất lợi ích chi phí, vượt 12.000 đ nếu làm lại 15,3 phút (simulated); pilot cần đo phút thật và mức giảm xem lại an toàn.

## Nguồn và giới hạn đối chiếu

- Công thức: `docs/du_lieu_va_cong_thuc.md`; quy ước giới hạn chạy, A4 và B4: `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Bộ kiểm số đối chiếu số hướng dẫn trong sai số 2%; trạng thái so code A–B ghi ở `ket_qua_kiem_tra.md`. Hồ sơ người 3–4 cần kiểm tra khi hoàn thiện.
