# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` đồng thời `mo_lai_trong_7_ngay == 0`, chia tổng yêu cầu | 994 / 1.200 × 100 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Trong các yêu cầu `duoc_xem_lai == 1`, đếm quyết định `sua` hoặc `bo`, chia số được xem lại | (41 + 7) / 177 × 100 = **27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày, dùng làm chỉ báo thay thế cho lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng yêu cầu | 51 / 1.200 × 100 = **4,25%** |
| Dùng (tự đề xuất) | Tỉ lệ yêu cầu được mở trợ lý trong nhóm can thiệp | Số yêu cầu hợp lệ thuộc nhóm can thiệp có ít nhất một lượt mở trợ lý được cấp quyền, chia tổng yêu cầu hợp lệ được phân vào nhóm can thiệp | Không tính: CSV chưa có event mở trợ lý và phân nhóm |
| An toàn (tự đề xuất) | Tỉ lệ yêu cầu hoàn sai tiền trong mẫu kiểm tra tuần | Số yêu cầu kiểm tra có tổng tiền thực trả khác số tiền đúng, chia tổng yêu cầu đã hoàn tất đối soát trong mẫu tuần | Không tính: CSV chưa có số tiền đúng và kết quả kiểm tra mẫu |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

### Cách tính và bằng chứng

Người 3 chuẩn bị với hỗ trợ AI; ba chỉ số đã đếm trực tiếp từ CSV và đối chiếu với code người 1–2 cùng phần E trong [ket_qua_kiem_tra.md](ket_qua_kiem_tra.md). Toàn bộ dữ liệu lab là giả lập; ba tỉ lệ trên không dùng hai cột số phút `_simulated`.

- Có 177 yêu cầu được xem lại: 129 `giu`, 41 `sua`, 7 `bo`; tổng 177. Có 1.023 yêu cầu không được xem lại, không đưa vào mẫu số của tỉ lệ bỏ qua.
- Có 994 yêu cầu thỏa đồng thời hai điều kiện của chỉ số chính; 51 yêu cầu mở lại. Không thay chỉ số chính bằng `ket_qua == 'thanh_cong'`, vì đó là định nghĩa khác.
- Trong phạm vi `noi_dia` + `hang_nang`: mở lại 39/982 = **3,97%**, làm lại 48/982 = **4,89%**. Đây là số mô tả, chưa phải ngưỡng pilot được duyệt.
- Chỉ số trong đợt chạy thử là 82,83%; chưa thể kết luận tác động so với baseline 0,70, vì baseline là giả định đề cho, không phải nhóm đối chứng trong mẫu này.
- Mở lại không đồng nghĩa mọi ca đều có lỗi; không mở lại cũng không chứng minh không có lỗi. Chỉ số kiểm tra sai tiền bổ sung khả năng phát hiện lỗi ngầm.

Các tử số, mẫu số và phép chia ở trên cho phép đối chiếu tay. Đã kiểm tra bằng cách đếm lại trực tiếp với Python và PowerShell: 1.200 yêu cầu; 994 đạt chỉ số chính; 177 được xem lại, trong đó 48 sửa hoặc bỏ; 51 mở lại.

Đoạn Python dưới đây chỉ đọc CSV và in kết quả, không tạo file. Thực hiện trong phiên Python có thư mục làm việc là thư mục gốc repo, chỉ cần thư viện chuẩn:

```python
import csv

with open('src/logix_requests.csv', encoding='utf-8-sig', newline='') as f:
    requests = list(csv.DictReader(f))
reviewed = [r for r in requests if r['duoc_xem_lai'] == '1']
primary = sum(r['dong_trong_24h'] == '1' and r['mo_lai_trong_7_ngay'] == '0'
              for r in requests)
ignored = sum(r['quyet_dinh_xem_lai'] in ('sua', 'bo') for r in reviewed)
reopened = sum(r['mo_lai_trong_7_ngay'] == '1' for r in requests)
for name, numerator, denominator in (
    ('Chi so chinh', primary, len(requests)),
    ('Bo qua goi y', ignored, len(reviewed)),
    ('Mo lai', reopened, len(requests)),
):
    print(f'{name}: {numerator}/{denominator} = {100*numerator/denominator:.2f}%')
```

`src/lab13.py` đã in cùng ba chỉ số trong phần E; nhánh `--nguoi-2` cũng trả về các tử số, mẫu số tương ứng. Đã chạy cả hai lệnh thành công và xác nhận các số khớp. Nếu dùng pandas, đọc yêu cầu bằng `keep_default_na=False`.

Dấu vân tay SHA-256 của dữ liệu đã dùng:

| File | SHA-256 |
| --- | --- |
| `src/logix_requests.csv` | `7fcb7a23afbabe4d1b8f60980f147f87061050d4d43aa3a2cd11db1fcb71d06e` |
| `src/logix_runs.csv` | `521145e65c645e7ecbdd48e3a4d91a015ddd14beaf163f2bfe439107b735231d` |

## Danh sách event

Đây là thiết kế đề xuất, chưa phải bằng chứng event đã được triển khai. Mọi event có `event_id`, `event_version`, `occurred_at` có múi giờ, `request_id`, `trace_id`, `depot`, `arm`, `assignment_version` và `staff_id` khi có.

Trong luồng mới, `trace_id` nối chuỗi xử lý một yêu cầu, kể cả luồng thủ công. CSV có trace theo từng lần chạy; event lần chạy lưu thêm `agent_run_trace_id` trỏ về trace gốc và `run_id`, không giả định một yêu cầu chỉ có một run.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | Dịch vụ tiếp nhận | `created_at`, `loai`, `requested_amount_vnd`, `eligible`, `exclusion_reason`, `trace_id` | Khi tiếp nhận và xác định yêu cầu hợp lệ |
| pilot_assignment_recorded | Dịch vụ phân nhóm | `assignment_unit`, `unit_id`, `assigned_arm`, `seed_version`, `trace_id` | Trước khi tiếp cận trợ lý |
| agent_opened | Giao diện nhân viên | `session_id`, `access_allowed`, `trace_id` | Khi mở trợ lý cho yêu cầu |
| agent_run_completed | Agent runtime | `run_id`, `agent_run_trace_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `pricing_version`, `policy_version`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| agent_suggestion_shown | Giao diện nhân viên | `suggestion_id`, `suggested_amount_vnd`, `trace_id` | Khi hiển thị gợi ý |
| staff_review_decision | Giao diện nhân viên | `suggestion_id`, `decision` (`giu/sua/bo`), `is_final`, `review_seconds`, `trace_id` | Khi lưu quyết định xem lại |
| staff_rework_completed | Luồng CSKH | `rework_seconds`, `reason_code`, `is_final`, `trace_id` | Khi hoàn tất làm lại |
| refund_ledger_write | Dịch vụ hoàn tiền | `transaction_id`, `idempotency_key`, `order_id`, `paid_amount_vnd`, `ledger_status`, `trace_id` | Sau mỗi lần ghi sổ, kể cả thất bại |
| refund_confirmation_sent | Dịch vụ thông báo | `transaction_id`, `message_status`, `claim_status`, `channel`, `trace_id` | Khi gửi thông báo về trạng thái hoàn tiền |
| handoff_to_staff | Agent runtime | `reason_code`, `summary_id`, `limit_explained`, `retention_months`, `trace_id` | Khi chuyển nhân viên |
| ticket_closed | Hệ thống ticket | `closed_at`, `closure_id`, `trace_id` | Khi đóng yêu cầu |
| ticket_reopened | Hệ thống ticket | `reopened_at`, `previous_closure_id`, `reason_code`, `trace_id` | Khi mở lại |
| audit_sample_checked | Công cụ đối soát kế toán | `audit_id`, `audit_week`, `sampling_method`, `paid_amount_vnd`, `expected_amount_vnd`, `pricing_version`, `audit_complete`, `trace_id` | Khi hoàn tất kiểm tra mẫu |
| input_validation_failed | Dịch vụ kiểm tra đầu vào | `field_name`, `reason_code`, `trace_id` | Khi đầu vào không hợp lệ; không lưu số tài khoản nguyên văn |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

| Chỉ số | Event dùng để tính | Quy tắc |
| --- | --- | --- |
| Đóng 24 giờ, không mở lại 7 ngày | `refund_request_created`, `pilot_assignment_recorded`, `ticket_closed`, `ticket_reopened` | Kiểm tra lần đóng đầu trong 24 giờ và không mở lại trong 7 ngày sau đóng; đếm một lần mỗi yêu cầu |
| Bỏ qua gợi ý | `staff_review_decision`, `agent_suggestion_shown` | Lấy quyết định cuối `is_final == true` cho mỗi yêu cầu được xem lại; số `sua/bo` chia số yêu cầu có quyết định cuối |
| Mở lại 7 ngày | `refund_request_created`, `ticket_closed`, `ticket_reopened` | Đếm một lần mỗi yêu cầu có mở lại trong 7 ngày sau đóng, trên cohort đủ theo dõi |
| Mở trợ lý ở nhóm can thiệp | `refund_request_created`, `pilot_assignment_recorded`, `agent_opened` | Tử số và mẫu số cùng thuộc nhóm can thiệp và phạm vi hợp lệ; không cộng lượt mở lặp hoặc bị từ chối quyền |
| Hoàn sai tiền qua kiểm tra mẫu | `audit_sample_checked`, `refund_ledger_write` | Đối soát tổng tiền thực trả với số tiền đúng, chỉ lấy kiểm tra hoàn tất; một yêu cầu một lần trong mẫu tuần |

Quy ước cửa sổ thời gian là đề xuất cần chốt cùng người 4 trước pilot. CSV không có timestamp để tự kiểm tra cửa sổ; kết quả tính thử dùng cờ có sẵn theo đề. Khi vận hành, khử trùng event theo `event_id`, báo cáo theo nhóm phân ban đầu và chỉ chốt cohort đã đủ theo dõi. Dữ liệu thiếu hoặc chưa đủ 7 ngày không được mặc định là không có lỗi. Báo cáo riêng số chưa đủ theo dõi, thiếu event và tỉ lệ hoàn tất kiểm tra mẫu; không suy rộng mẫu kiểm tra có chủ đích thành tỉ lệ toàn bộ yêu cầu.

## E2 · Rủi ro kinh tế

**Đã đối chiếu số liệu với bảng B1 trong [bang_chi_phi.md](bang_chi_phi.md) và kết quả chạy code người 1–2.** Hai tác động chi phí dưới đây khớp đến hai chữ số thập phân; phần phụ thuộc số liệu người 1–2 đã hoàn tất. Ngưỡng theo dõi và hành động vẫn là đề xuất để người 4 chốt cùng kế hoạch pilot, chưa phải luật dừng đã được duyệt.

| Nội dung bàn giao từ người 1–2 | Kết quả đối chiếu |
| --- | --- |
| Ba chỉ số E | Khớp: 994/1.200 = 82,83%; 48/177 = 27,12%; 51/1.200 = 4,25% |
| A2 · Chi phí gốc | Khớp: 4.373.585,132 / 978 = 4.471,97 đ/việc — **simulated** |
| B1 · Làm lại gấp đôi | Khớp: 6.786,90 đ/việc, tăng 51,77% — **simulated** |
| B1 · Xem lại gấp đôi | Khớp: 6.292,01 đ/việc, tăng 40,70% — **simulated** |
| Phạm vi `noi_dia` + `hang_nang` | Khớp số mở lại: 39/982 = 3,97%; dùng để người 4 cân nhắc ngưỡng an toàn |

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Chi phí làm lại gấp đôi | Từ 4.471,97 đ lên **6.786,90 đ/việc**, tăng **51,77%** — **simulated**, toàn mẫu, chưa gồm cố định | Tỉ lệ làm lại trong phạm vi vượt 7% trong một tuần; theo dõi thêm phút làm lại thực đo trên số việc thành công. Mức mô tả hiện tại trong phạm vi: 48/982 = 4,89% | Rà ít nhất 20 trace làm lại, sửa nguyên nhân lặp; cân nhắc thu hẹp về `noi_dia` trước mở rộng | PM trợ lý hoàn phí |
| Chi phí xem lại gấp đôi | Từ 4.471,97 đ lên **6.292,01 đ/việc**, tăng **40,70%** — **simulated**, toàn mẫu, chưa gồm cố định | Phút xem lại thực đo trên mỗi việc thành công vượt 2 lần mức kế hoạch trong một tuần; báo cáo kèm tỉ lệ được xem lại | Phân tích nhóm phải xem lại nhiều, cải thiện gợi ý; chỉ giảm mức xem lại khi chỉ số an toàn và kiểm tra mẫu cho phép | Trưởng nhóm CSKH |

### Cách tính và bằng chứng đối chiếu

- Cộng trên mọi lần chạy: 5.771.712 token vào, 734.774 token ra, 5.600 lần tool. Tiền token = (5.771.712 × 26 + 734.774 × 130) / 1.000 = 245.585,132 đ; tool = 5.600 × 15 = 84.000 đ.
- Phút xem lại = 890; làm lại = 1.132 — **simulated**. Tiền xem lại = 890 × 2.000 = 1.780.000 đ; làm lại = 1.132 × 2.000 = 2.264.000 đ — **simulated**.
- Tổng gốc = 245.585,132 + 84.000 + 1.780.000 + 2.264.000 = 4.373.585,132 đ — **simulated**. Số việc thành công = 978.
- Gốc = 4.373.585,132 / 978 = 4.471,97 đ/việc — **simulated**.
- Làm lại gấp đôi = (4.373.585,132 + 2.264.000) / 978 = 6.786,90 đ/việc; thay đổi = 51,77% — **simulated**.
- Xem lại gấp đôi = (4.373.585,132 + 1.780.000) / 978 = 6.292,01 đ/việc; thay đổi = 40,70% — **simulated**.

Thay đổi (%) = (chi phí kịch bản / chi phí gốc − 1) × 100. Giữ độ chính xác đầy đủ khi tính, chỉ làm tròn khi trình bày. Kịch bản giữ nguyên số việc thành công và các khoản khác; tác động toàn mẫu không thay cho dự báo riêng của phạm vi pilot.

Nguồn: hai CSV của lab và [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md). Phép đếm, công thức và hash dữ liệu được ghi trực tiếp trong file này.
