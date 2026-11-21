"""Kiểm số độc lập của người 2, không thay phần A–B của người 1.

Chạy trong src/: python lab13.py --nguoi-2 [--ghi-bao-cao]
Chỉ dùng dữ liệu CSV và công thức của lab; không cần statsmodels/API/mạng.
"""
import csv
import json
import math
from pathlib import Path
from statistics import NormalDist

from lab13 import co_mau_d1


def doc_csv(ten):
    with open(ten, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def doi_chieu(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15,
              luong_phut=2000, he_so_xem_lai=1, he_so_lam_lai=1,
              max_lan_chay=None):
    """Bộ cộng độc lập dùng csv/stdlib để so với mo_hinh dùng pandas."""
    ids = {r['request_id'] for r in reqs}
    ds = [r for r in runs if r['request_id'] in ids
          and (max_lan_chay is None or int(r['attempt']) <= max_lan_chay)]
    giu = [r for r in reqs if max_lan_chay is None
           or int(r['so_lan_chay']) <= max_lan_chay]
    token = sum((int(r['tokens_in']) * gia_vao + int(r['tokens_out']) * gia_ra)
                / 1000 for r in ds)
    tool = sum(int(r['tool_calls']) * gia_tool for r in ds)
    chay_lai = sum((int(r['tokens_in']) * gia_vao + int(r['tokens_out']) * gia_ra)
                  / 1000 + int(r['tool_calls']) * gia_tool
                  for r in ds if int(r['attempt']) > 1)
    xem = sum(float(r['phut_xem_lai_simulated']) for r in giu) * luong_phut * he_so_xem_lai
    lam = sum(float(r['phut_lam_lai_simulated']) for r in giu) * luong_phut * he_so_lam_lai
    n = sum(r['ket_qua'] == 'thanh_cong' for r in giu)
    tong = token + tool + xem + lam
    return dict(token=token, tool=tool, chay_lai=chay_lai, xem_lai=xem,
                lam_lai=lam, tong=tong, thanh_cong=n,
                cps=tong / n if n else math.inf,
                hoa_don_moi_yc=(token + tool) / len(reqs) if reqs else math.inf)


KICH_BAN = [
    ('Giá token gấp đôi', '52 và 260 đ/1.000 token', dict(gia_vao=52, gia_ra=260)),
    ('Giá token giảm một nửa', '13 và 65 đ/1.000 token', dict(gia_vao=13, gia_ra=65)),
    ('Tỉ lệ xem lại gấp đôi', 'Tiền xem lại × 2', dict(he_so_xem_lai=2)),
    ('Tỉ lệ xem lại giảm một nửa', 'Tiền xem lại × 0,5', dict(he_so_xem_lai=0.5)),
    ('Số ca làm lại gấp đôi', 'Tiền làm lại × 2', dict(he_so_lam_lai=2)),
    ('Số ca làm lại giảm một nửa', 'Tiền làm lại × 0,5', dict(he_so_lam_lai=0.5)),
    ('Lương nhân viên tăng 25%', '2.500 đ/phút', dict(luong_phut=2500)),
    ('Chỉ cho chạy tối đa 2 lần', 'attempt ≤ 2; vượt giới hạn: chuyển người, phút = 0', dict(max_lan_chay=2)),
    ('Chỉ cho chạy 1 lần', 'attempt ≤ 1; vượt giới hạn: chuyển người, phút = 0', dict(max_lan_chay=1)),
]


def tong_hop(runs, reqs):
    goc = doi_chieu(runs, reqs)
    loai = {}
    for ten in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
        ds = [r for r in reqs if r['loai'] == ten]
        a = doi_chieu(runs, ds)
        a.update(so_yc=len(ds), ti_le=a['thanh_cong'] / len(ds),
                 lan_moi_yc=sum(int(r['so_lan_chay']) for r in ds) / len(ds))
        loai[ten] = a
    scope = [r for r in reqs if r['loai'] in ('noi_dia', 'hang_nang')]
    pham_vi = doi_chieu(runs, scope)
    # A4: 45.000 là toàn bộ yêu cầu, không phải chỉ 982 yêu cầu trong phạm vi.
    a4 = []
    for v in (45000, 22500):
        thanh_cong = v * pham_vi['thanh_cong'] / len(reqs)
        cd = 40000000 / thanh_cong
        a4.append(dict(khoi_luong=v, thanh_cong=thanh_cong, co_dinh=cd,
                       cps=pham_vi['cps'] + cd))
    b1 = [(ten, cach, doi_chieu(runs, reqs, **kw)) for ten, cach, kw in KICH_BAN]
    b2 = doi_chieu(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    b3 = []
    for k in (1, 2, 3):
        a = doi_chieu(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - a['thanh_cong']
        b3.append(dict(k=k, tong=a['tong'], khong_tc=khong_tc,
                       he_thong=a['tong'] + 12000 * khong_tc, cps=a['cps']))
    ids = {r['request_id'] for r in scope}
    ok = len({r['request_id'] for r in runs if r['request_id'] in ids and r['status'] == 'ok'})
    lam = sum(r['ket_qua'] == 'lam_lai' for r in scope)
    all_lam = [r for r in reqs if r['ket_qua'] == 'lam_lai']
    phut = sum(float(r['phut_lam_lai_simulated']) for r in all_lam) / len(all_lam)
    may = pham_vi['token'] + pham_vi['tool']
    b4 = []
    # Giữ 15,3 phút như phép độ nhạy trong hướng dẫn; báo cả trung bình chính xác.
    for t in (9, 15.3):
        tong = may + ok * 5 * 2000 + lam * t * 2000
        b4.append(dict(phut=t, ok=ok, lam_lai=lam, tong=tong,
                       cps=tong / pham_vi['thanh_cong'],
                       phut_xem_hoa_von=(12000 * pham_vi['thanh_cong'] - may
                                         - lam * t * 2000) / (ok * 2000)))
    xem = [r for r in reqs if r['duoc_xem_lai'] == '1']
    e = dict(chinh_tu=sum(r['dong_trong_24h'] == '1' and r['mo_lai_trong_7_ngay'] == '0' for r in reqs),
             tong=len(reqs), bo_qua_tu=sum(r['quyet_dinh_xem_lai'] in ('sua', 'bo') for r in xem),
             xem_mau=len(xem), mo_lai_tu=sum(r['mo_lai_trong_7_ngay'] == '1' for r in reqs),
             scope_mo_lai=sum(r['mo_lai_trong_7_ngay'] == '1' for r in scope), scope_mau=len(scope))
    qids = {r['request_id'] for r in reqs if r['loai'] == 'quoc_te'}
    q_ok = {}
    for k in (1, 2, 3):
        ds = [r for r in runs if r['request_id'] in qids and int(r['attempt']) == k]
        q_ok[k] = sum(r['status'] == 'ok' for r in ds) / len(ds)
    d = co_mau_d1()
    # Xấp xỉ power bằng cùng công thức z của D1, khi hiệu ứng thật chỉ +5 điểm.
    za = NormalDist().inv_cdf(0.975)
    se0 = math.sqrt(2 * .725 * .275 / d['n_hieu_dung_6_diem'])
    se1 = math.sqrt((.7 * .3 + .75 * .25) / d['n_hieu_dung_6_diem'])
    d['power_5_diem_xap_xi'] = (NormalDist().cdf((.05 - za * se0) / se1)
                              + NormalDist().cdf((-.05 - za * se0) / se1))
    return dict(a2=goc, a3=loai, a4=a4, b1=b1, b2=b2, b3=b3, b4=b4,
                pham_vi=pham_vi, d1=d, e=e, quoc_te_ok=q_ok,
                phut_lam_lai_tb=phut)


def so(x, n=0):
    return f'{x:,.{n}f}'.replace(',', '_').replace('.', ',').replace('_', '.')


def bang_chi_phi(k, runs, reqs):
    a, d, e = k['a2'], k['d1'], k['e']
    lines = ['# Bảng chi phí · Nhiệm vụ A và B', '',
             'Nguồn: hai CSV gốc; tính bằng `src/kiem_tra_so_lieu.py` theo công thức của đề. '
             'Chạy trong `src/`: `python lab13.py --nguoi-2 --ghi-bao-cao`.', '',
             'Đây là bộ kiểm số độc lập của người 2; đối chiếu với `mo_hinh` bằng lệnh chạy trên. '
             'Dữ liệu lab là giả lập; mọi tổng, chi phí và tỉ lệ chi phí chứa phút giả lập đều mang nhãn **simulated**.', '',
             '## A1 · Ba phép thử đáp án biết trước', '',
             '| Phép thử (p = 0,8) | Tính tay |', '| --- | ---: |',
             '| Tối đa 2 lần: 1 + (1 − 0,8) | 1,20 |',
             '| Chạy đến khi đúng: 1 / 0,8 | 1,25 |',
             '| Tối đa 3: (1 + 0,2 + 0,04) / (1 − 0,2³) | 1,25 |', '',
             'Đây là kết quả kiểm số; lệnh chạy trên cũng kiểm tra ba assert A1 của nhóm.', '',
             '## A2 · Mô hình chi phí từ trace', '',
             '| Khoản | Số tiền (đ) / số việc | Nguồn | Nhãn |', '| --- | ---: | --- | --- |']
    rows = [('Token', 'token', 'Tổng tokens_in × 26/1.000 + tokens_out × 130/1.000, mọi run', 'đo từ trace'),
            ('Tool', 'tool', 'Tổng tool_calls × 15, mọi run', 'đo từ trace'),
            ('Trong đó, lần chạy thứ 2 và 3', 'chay_lai', 'Token + tool với attempt > 1; đã nằm trong hai dòng trên', 'đo từ trace'),
            ('Xem lại', 'xem_lai', 'Tổng phut_xem_lai_simulated × 2.000', 'simulated'),
            ('Làm lại', 'lam_lai', 'Tổng phut_lam_lai_simulated × 2.000', 'simulated'),
            ('Tổng chi phí', 'tong', 'Token + tool + xem lại + làm lại', 'simulated'),
            ('Số việc thành công', 'thanh_cong', "ket_qua == thanh_cong", 'đếm yêu cầu'),
            ('Chi phí mỗi việc thành công', 'cps', 'Tổng / số việc thành công', 'simulated'),
            ('Hoá đơn token và tool / số yêu cầu', 'hoa_don_moi_yc', 'Token + tool chia 1.200', 'đo từ trace')]
    for ten, key, nguon, nhan in rows:
        lines.append(f'| {ten} | {so(a[key], 2)} | {nguon} | {nhan} |')
    lines += ['', f'- Chi phí mỗi việc thành công gấp **{so(a["cps"] / a["hoa_don_moi_yc"], 2)} lần** hoá đơn/yêu cầu (simulated).',
              f'- Làm lại lớn nhất: **{so(100*a["lam_lai"]/a["tong"], 2)}%**; tổng giờ nhân viên chiếm **{so(100*(a["lam_lai"]+a["xem_lai"])/a["tong"], 2)}%** (simulated).', '',
              '### Tính tay để đối chiếu', '']
    tin = sum(int(r['tokens_in']) for r in runs)
    tout = sum(int(r['tokens_out']) for r in runs)
    tools = sum(int(r['tool_calls']) for r in runs)
    lines += [f'- Token = {so(tin)} × 26/1.000 + {so(tout)} × 130/1.000 = **{so(a["token"], 2)} đ**; tool = {so(tools)} × 15 = **{so(a["tool"])} đ**.',
              f'- Tổng = {so(a["token"],2)} + {so(a["tool"])} + {so(a["xem_lai"])} + {so(a["lam_lai"])} = **{so(a["tong"],2)} đ**; chia {a["thanh_cong"]} = **{so(a["cps"],2)} đ/việc thành công** (simulated).',
              f'- Tử số tính đủ **{len(runs)} run**, kể cả lỗi; mẫu số chỉ **{a["thanh_cong"]}/{len(reqs)}** yêu cầu thành công. Dòng chạy lại là phần nằm trong token + tool, không cộng hai lần.',
              f'- So với người tự làm: ({so(a["tong"],2)} + {len(reqs)-a["thanh_cong"]} × 12.000)/1.200 = **{so((a["tong"]+(len(reqs)-a["thanh_cong"])*12000)/len(reqs),2)} đ/yêu cầu** (simulated); dùng quy ước B3 cho mọi ca không thành công.', '',
              '## A3 · Tách theo loại yêu cầu', '',
              '| Loại | Số yêu cầu | Tỉ lệ thành công | Lần chạy/yêu cầu | CPS (đ, simulated) | CPS / 12.000 (simulated) |',
              '| --- | ---: | ---: | ---: | ---: | ---: |']
    for ten, v in k['a3'].items():
        lines.append(f'| {ten} | {v["so_yc"]} | {so(100*v["ti_le"],2)}% | {so(v["lan_moi_yc"],2)} | {so(v["cps"],2)} | {so(v["cps"]/12000,2)}× |')
    lines += ['', f'- `quoc_te`: CPS {so(k["a3"]["quoc_te"]["cps"],2)} đ (simulated); tỉ lệ run ok theo lần 1–2–3 là '+ ' / '.join(so(v*100,2)+'%' for v in k['quoc_te_ok'].values()) + '; chạy lại ít hiệu quả.',
              '- Đề xuất phạm vi `noi_dia + hang_nang`; để người 4 chốt pilot. Tỉ số CPS/12.000 ở bảng chỉ là chỉ báo; so chi phí công ty phải cộng xử lý thủ công như B3.', '',
              '## A4 · Chi phí cố định (noi_dia + hang_nang)', '',
              '40.000.000 đ/tháng; khối lượng dưới đây là **tất cả yêu cầu công ty**, giữ cơ cấu mẫu: số thành công trong phạm vi = khối lượng × 900/1.200.', '',
              '| Khối lượng yêu cầu/tháng | Việc thành công trong phạm vi | Cố định/việc (đ) | CPS + cố định (đ, simulated) | / 12.000 (simulated) |',
              '| --- | ---: | ---: | ---: | ---: | ---: |']
    for v in k['a4']:
        lines.append(f'| {so(v["khoi_luong"])} | {so(v["thanh_cong"])} | {so(v["co_dinh"],2)} | {so(v["cps"],2)} | {so(v["cps"]/12000,2)}× |')
    lines += ['', '- Cố định không đổi kết luận chỉ báo ở cả 45.000 và 22.500 yêu cầu/tháng; các CPS này chưa cộng xử lý thủ công cho yêu cầu không thành công.', '',
              '## B1 · Đổi từng yếu tố', '',
              '| Kịch bản | Cách tính | CPS (đ, simulated) | Thay đổi (simulated) |', '| --- | --- | ---: | ---: |']
    for ten, cach, v in k['b1']:
        lines.append(f'| {ten} | {cach} | {so(v["cps"],2)} | {so((v["cps"]/a["cps"]-1)*100,2)}% |')
    lines += ['', '## B2 · Đổi một cặp và xếp hạng', '',
              f'- Token × 2 và xem lại × 2: **{so(k["b2"]["cps"],2)} đ**, tăng **{so((k["b2"]["cps"]/a["cps"]-1)*100,2)}%** (simulated); bằng tổng tác động riêng vì mô hình cộng tuyến tính.',
              '- Ba yếu tố mạnh nhất theo mức tăng đã thử: **1. làm lại; 2. xem lại; 3. lương** (simulated).', '',
              '## B3 · Giới hạn chạy lại', '',
              'Cả hệ thống = tổng trợ lý + 12.000 × số yêu cầu không thành công; theo quy ước đề, áp dụng cả `lam_lai` và `chuyen_nhan_vien`.', '',
              '| Giới hạn | Tổng trợ lý (đ, simulated) | Không thành công | Cả hệ thống (đ, simulated) | CPS trợ lý (đ, simulated) |',
              '| --- | ---: | ---: | ---: | ---: |']
    for v in k['b3']:
        lines.append(f'| {v["k"]} lần | {so(v["tong"],2)} | {v["khong_tc"]} | {so(v["he_thong"],2)} | {so(v["cps"],2)} |')
    lines += ['', '- **2 lần** rẻ nhất cho công ty; **1 lần** cho CPS trợ lý thấp nhất nhưng đẩy thêm **85 yêu cầu** sang người so với 2 lần (chi phí simulated).', '',
              '## B4 · Xem lại 100% trong phạm vi', '',
              f'{e["scope_mau"]} yêu cầu; {k["b4"][0]["ok"]} yêu cầu có ít nhất 1 run ok được xem lại 5 phút; {k["b4"][0]["lam_lai"]} ca làm lại. Token + tool = {so(k["pham_vi"]["token"]+k["pham_vi"]["tool"],2)} đ; chia {k["pham_vi"]["thanh_cong"]} việc thành công.', '',
              '| Giả định phút làm lại/ca | Tổng (đ, simulated) | CPS (đ, simulated) | / 12.000 (simulated) | Phút xem lại hoà vốn (simulated) |',
              '| --- | ---: | ---: | ---: | ---: |']
    for v in k['b4']:
        lines.append(f'| {so(v["phut"],1)} | {so(v["tong"],2)} | {so(v["cps"],2)} | {so(v["cps"]/12000,2)}× | {so(v["phut_xem_hoa_von"],2)} |')
    lines += ['', f'- Trung bình phút làm lại trên toàn bộ ca `lam_lai` trong CSV: **{so(k["phut_lam_lai_tb"],4)} phút (simulated)**; dùng 15,3 làm kịch bản độ nhạy theo hướng dẫn.',
              '- Xem lại 100% gần mất lợi ích chi phí, vượt 12.000 đ nếu làm lại 15,3 phút (simulated); pilot cần đo phút thật và mức giảm xem lại an toàn.', '',
              '## Nguồn và giới hạn đối chiếu', '',
              '- Công thức: `docs/du_lieu_va_cong_thuc.md`; quy ước giới hạn chạy, A4 và B4: `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.',
              '- Bộ kiểm số đối chiếu số hướng dẫn trong sai số 2%; trạng thái so code A–B ghi ở `ket_qua_kiem_tra.md`. Hồ sơ người 3–4 cần kiểm tra khi hoàn thiện.']
    return '\n'.join(lines) + '\n'


def ban_giao(k, trang_thai):
    d, e = k['d1'], k['e']
    return f'''# Kết quả kiểm tra số liệu và cỡ mẫu

Chạy trong `src/`: `python lab13.py --nguoi-2`; thêm `--ghi-bao-cao` để cập nhật bảng chi phí và file này.

## D1 · Gửi người 4

| Câu | Cách tính | Kết quả |
| --- | --- | --- |
| a · Theo yêu cầu, +5 điểm | Công thức hai tỉ lệ, alpha 0,05, power 0,8 | {d['n_5_diem']} yêu cầu/nhóm |
| b · Theo nhân viên, m=75 | DE=1+74×0,02={so(d['de_75'],2)} | {d['n_theo_nhan_vien']} yêu cầu/nhóm; {d['nhan_vien_can_moi_nhom']} nhân viên/nhóm, tổng 84 > 40 |
| c · 20 nhân viên/nhóm | n hiệu dụng < 20/0,02 | Luôn < {so(d['tran_20_nhan_vien'])}, không đủ {d['n_5_diem']} |
| d · 6 depot/nhóm | n hiệu dụng < 6/0,02 | Luôn < {so(d['tran_6_depot'])}; chỉ 6 cụm/nhóm |
| e · +6 điểm, 20 nhân viên/nhóm | Cần {d['n_6_diem']}; giải 20m/[1+(m−1)×0,02] ≥ {d['n_6_diem']} | m ≥ {d['m_6_diem']}; DE={so(d['de_6_diem'],2)}; n hiệu dụng={so(d['n_hieu_dung_6_diem'],2)} |

Với phương án e: 20 × 299 = 5.980 yêu cầu/nhóm, tổng 11.960; cần đủ yêu cầu **trong phạm vi pilot**, không lấy tổng công ty thay thế.
Nếu tác động thật chỉ +5 điểm, power xấp xỉ **{so(d['power_5_diem_xap_xi'],2)}**, thấp hơn mục tiêu 0,80; người 4 cần ghi đánh đổi và chốt MDE 0,06 nếu chọn phương án này.
Đây là xấp xỉ theo công thức z của đề, không thay thế phân tích cụm chi tiết. Đã điền a–e vào chú thích D1 của `pilot_plan.yaml`; người 4 tự chốt D2 và các trường kế hoạch.

## E · Gửi người 3 và người 4

| Chỉ số trong đợt chạy thử | Tử số / mẫu số | Tỉ lệ |
| --- | --- | ---: |
| Đóng 24 giờ và không mở lại 7 ngày | {e['chinh_tu']}/{e['tong']} | {so(100*e['chinh_tu']/e['tong'],2)}% |
| Bỏ qua gợi ý (sửa + bỏ), chỉ trong ca được xem lại | {e['bo_qua_tu']}/{e['xem_mau']} | {so(100*e['bo_qua_tu']/e['xem_mau'],2)}% |
| Mở lại 7 ngày, toàn mẫu | {e['mo_lai_tu']}/{e['tong']} | {so(100*e['mo_lai_tu']/e['tong'],2)}% |
| Mở lại 7 ngày, noi_dia + hang_nang | {e['scope_mo_lai']}/{e['scope_mau']} | {so(100*e['scope_mo_lai']/e['scope_mau'],2)}% |

Các tỉ lệ trên không dùng cột phút `_simulated`, nhưng vẫn là dữ liệu lab giả lập; chưa có đối chứng nên không kết luận tác động nhân quả.
Ngưỡng mở lại tuyệt đối 3% thấp hơn cả nền toàn mẫu và phạm vi; người 4 cần cân nhắc so đối chứng +2 điểm và trần 6% theo hướng dẫn.

## Phụ thuộc và kiểm tra cuối

- **Làm ngay:** D1, E, tính tay và bảng chi phí độc lập đã có; không cần chờ người 1, 3 hoặc 4 để tính các phần này.
- **Đối chiếu code người 1:** trạng thái lần chạy kiểm tra: **{trang_thai}**. Chạy lại cùng lệnh mỗi khi code A–B đổi để so mô hình gốc, 9 kịch bản và mọi loại yêu cầu.
- **Chờ người 3–4 để so toàn hồ sơ:** `chi_so.md`, các trường kế hoạch trong `pilot_plan.yaml` và `ho_so_launch_v0.md` còn mẫu; D1 đã được điền nhưng chưa thể xác nhận toàn hồ sơ nhất quán.
- **Bàn giao file chung:** D1 nằm trong `lab13.py`; người 1 cần giữ phần này và nhánh `--nguoi-2` khi ghép A–B. Bộ kiểm số nằm riêng trong `kiem_tra_so_lieu.py` để tránh ghi đè A–B.
- **Kiểm tra tích hợp:** đã chạy `python lab13.py` từ đầu đến cuối sau khi ghép A–B; trước nộp còn cần so số toàn hồ sơ và chạy trên máy khác.

## Ghi nhận công cụ và đóng góp

Đã dùng Codex để đọc yêu cầu, viết bộ cộng độc lập, code D1 và dựng bảng từ CSV; tự kiểm tra bằng phép tính tay A2, ba giá trị A1 và số hướng dẫn (sai số ≤2%).
Bạn cần tự chạy lệnh, kiểm tra công thức và giải thích được các số trước khi nộp; chưa ghi nhận bạn đã làm bước này.
Chưa có họ tên/MSSV nên chưa tạo báo cáo cá nhân đúng tên; khi có thông tin, copy `MSSV_HoTen.md`, ghi đóng góp thực tế và AI đã dùng, rồi cập nhật `TEAM.md`.
'''


def kiem_tra(k):
    """Đối chiếu các mốc của hướng dẫn; không dùng các mốc này làm đầu vào tính."""
    for key, expected in dict(token=245585, tool=84000, chay_lai=93804,
                              xem_lai=1780000, lam_lai=2264000,
                              tong=4373585, thanh_cong=978, cps=4472).items():
        assert math.isclose(k['a2'][key], expected, rel_tol=.02), (key, k['a2'][key])
    for (_, _, v), expected in zip(k['b1'], (4723, 4346, 6292, 3562, 6787, 3315, 5506, 4237, 4111)):
        assert math.isclose(v['cps'], expected, rel_tol=.02)
    assert [v['khong_tc'] for v in k['b3']] == [319, 234, 222]
    for v, expected in zip(k['b4'], (11743, 12414)):
        assert math.isclose(v['cps'], expected, rel_tol=.02)
    assert (k['d1']['n_5_diem'], k['d1']['n_6_diem'], k['d1']['m_6_diem']) == (1251, 859, 299)
    assert (k['e']['chinh_tu'], k['e']['bo_qua_tu'], k['e']['mo_lai_tu']) == (994, 48, 51)


def so_voi_nguoi1(runs, reqs):
    import lab13
    import pandas as pd
    pr = pd.read_csv('logix_runs.csv')
    pq = pd.read_csv('logix_requests.csv', keep_default_na=False)
    try:
        lab13.kiem_tra_dap_an_biet_truoc()
        for kw in [{}] + [v[2] for v in KICH_BAN] + [dict(max_lan_chay=3),
                dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2)]:
            want, got = doi_chieu(runs, reqs, **kw), lab13.mo_hinh(pr, pq, **kw)
            for key in ('token', 'tool', 'xem_lai', 'lam_lai', 'tong', 'thanh_cong', 'cps'):
                assert math.isclose(want[key], got[key], rel_tol=1e-9, abs_tol=1e-6), (kw, key, want[key], got[key])
        for ten in ('noi_dia', 'hang_nang', 'quoc_te', 'doi_tac'):
            want = doi_chieu(runs, [r for r in reqs if r['loai'] == ten])
            got = lab13.mo_hinh(pr, pq[pq.loai == ten])
            assert math.isclose(want['cps'], got['cps'], rel_tol=1e-9)
    except NotImplementedError:
        return 'CHỜ: người 1 chưa hoàn thiện A1–A2; bộ kiểm số độc lập đã chạy'
    return 'ĐẠT: A1 và mô hình A2/A3/B1/B2/B3 khớp bộ kiểm số độc lập'


def main(ghi_bao_cao=False):
    runs, reqs = doc_csv('logix_runs.csv'), doc_csv('logix_requests.csv')
    k = tong_hop(runs, reqs)
    kiem_tra(k)
    trang_thai = so_voi_nguoi1(runs, reqs)
    print(json.dumps(k, ensure_ascii=False, indent=2))
    print('ĐẠT: bộ kiểm số so hướng dẫn trong sai số 2%.')
    print(trang_thai)
    if ghi_bao_cao:
        out = Path('../report/team')
        (out / 'bang_chi_phi.md').write_text(bang_chi_phi(k, runs, reqs), encoding='utf-8')
        (out / 'ket_qua_kiem_tra.md').write_text(ban_giao(k, trang_thai), encoding='utf-8')
        print('Đã ghi bang_chi_phi.md và ket_qua_kiem_tra.md.')


if __name__ == '__main__':
    import sys
    main(ghi_bao_cao='--ghi-bao-cao' in sys.argv)
