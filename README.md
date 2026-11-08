# 🚝 Hanoi Metro 3D Odyssey — Định Lượng Mối Liên Hệ Giữa Tiếp Cận Giao Thông Công Cộng & Giá Chào Bán Căn Hộ Tại Hà Nội ($N = 16.471$)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](#4-hướng-dẫn-tái-lập-kết-quả-100-reproducibility)
[![Automated Tests](https://img.shields.io/badge/Unit%20Tests-5%2F5%20PASSED-10b981)](#4-hướng-dẫn-tái-lập-kết-quả-100-reproducibility)
[![Sample Size](https://img.shields.io/badge/Sample%20Size-N%20%3D%2016%2C471%20Apartments-3b82f6)](#2-kiến-trúc-định-danh-không-gian-3-tầng-giải-quyết-bài-toán-bỏ-cấp-quậnhuyện--maup)
[![Spatial Tiers](https://img.shields.io/badge/Spatial%20Architecture-3--Tier%20%282--Level%20Gov%20Ready%29-f59e0b)](#2-kiến-trúc-định-danh-không-gian-3-tầng-giải-quyết-bài-toán-bỏ-cấp-quậnhuyện--maup)

> **Đề tài Khóa luận Tốt nghiệp Đại học (Mã B1):**
> *“Định lượng mối liên hệ giữa khả năng tiếp cận giao thông công cộng và giá chào bán căn hộ tại Hà Nội bằng mô hình Hedonic Pricing và hệ thống thông tin địa lý (GIS)”*
> *(Quantifying the Association Between Public Transport Accessibility and Apartment Asking Prices in Hanoi Using Hedonic Pricing and Geographic Information Systems)*

---

## 1. Tổng quan Dự án & Ba Phát hiện Thực nghiệm Cốt lõi

Kho lưu trữ này chứa **toàn bộ mã nguồn thực nghiệm GIS – Kinh tế lượng, bộ dữ liệu đối chiếu không gian 3 tầng, hệ thống kiểm thử tự động, ứng dụng mô phỏng không gian 3D tương tác (`index.html`) và bộ hồ sơ Khóa luận Tốt nghiệp 5 Chương kèm Sổ tay Phản biện Hội đồng** phân tích **$N = 16.471$ tin đăng căn hộ chung cư** dọc hành lang **Tuyến Metro 2A (Cát Linh – Hà Đông, 12 nhà ga)** và **Tuyến Metro 3 (Nhổn – Ga Hà Nội, 8 nhà ga đoạn trên cao)**.

### 🌟 Ba phát hiện định lượng trọng tâm:
1. **Hiệu ứng Vành đai Đi bộ Tối ưu ($500\text{m} - 1.000\text{m}$ — Sweet Spot Premium):**
   Các căn hộ nằm trong khoảng cách đi bộ mạng lưới từ $500\text{m}$ đến $1.000\text{m}$ ($6–10$ phút đi bộ) quanh nhà ga Metro ghi nhận mức thặng dư vốn hóa dương có ý nghĩa thống kê ở mức $99\%$ ($p < 0,001$) xuyên suốt mọi cấu hình kiểm soát không gian:
   - **Mô hình Chính `M3` (Phân vùng Vành đai Đô thị + $\ln\text{Dist\_CBD}$):** $\hat{\beta} = +0,0354^{***}$ ($SE = 0,0048$) $\rightarrow$ **+3,61%** ($R^2 = 0,2470$).
   - **Mô hình Đối chứng 1 `M4` (7 Tiểu thị trường bất động sản lịch sử):** $\hat{\beta} = +0,0383^{***}$ ($SE = 0,0048$) $\rightarrow$ **+3,91%** ($R^2 = 0,2492$).
   - **Mô hình Đối chứng 2 `M5` (21 Phường mới trực thuộc TP. Hà Nội — Chính quyền 2 cấp):** $\hat{\beta} = +0,0366^{***}$ ($SE = 0,0063$) $\rightarrow$ **+3,73%** ($R^2 = 0,2500$).
   - **Mô hình Độ nhạy `M6` (Chỉ giữ căn hộ định vị chính xác tòa nhà `project_exact`, $N = 10.521$):** $\hat{\beta} = +0,0383^{***}$ ($SE = 0,0060$) $\rightarrow$ **+3,90%** ($R^2 = 0,2530$).
2. **Hiệu ứng Khấu trừ Ngoại ứng Sát chân ga ($< 500\text{m}$ — Inverted-U Nuisance Discount):**
   Tại cự ly quá sát cầu cạn nhà ga ($<500\text{m}$), mức tăng giá chỉ đạt **+0,18% đến +0,41%** ($\hat{\beta} = 0,0030$ ở `M3`, $\hat{\beta} = 0,0041$ ở `M4`, $\hat{\beta} = 0,0018$ ở `M5` — không có ý nghĩa thống kê, $p > 0,55$). Ngoại ứng tiêu cực cục bộ (tiếng ồn đoàn tàu trên cầu cạn bê tông, rung chấn, che chắn tầm nhìn và ùn tắc giao thông dưới gầm cầu thang ga) đã triệt tiêu lợi ích tiếp cận.
3. **Ngưỡng Suy giảm về 0 ngoài $1.000\text{m}$ ($> 1.000\text{m}$ Distance Decay):**
   Tại vành đai đệm $1.000\text{m}-1.500\text{m}$ ($\hat{\beta} = -0,0015$ đến $+0,0002, p > 0,79$) và ngoài $1.500\text{m}$, hiệu ứng vốn hóa của Metro hội tụ về $0\%$ do cư dân chuyển hẳn sang sử dụng xe máy cá nhân trong điều kiện khí hậu nhiệt đới.

---

## 2. Kiến trúc Định danh Không gian 3 Tầng: Giải quyết Bài toán Bỏ cấp Quận/Huyện & MAUP

Trong bối cảnh Việt Nam thực hiện cải cách bộ máy hành chính **bỏ cấp trung gian quận/huyện, chuyển sang mô hình chính quyền địa phương 2 cấp (Thành phố Hà Nội $\rightarrow$ Phường/Xã mới)**, nghiên cứu thiết lập **Phương pháp Dual Point-in-Polygon & Kiến trúc Không gian 3 Tầng (`src/gis/spatial_crosswalk.py`)**:
- **Tính bất biến của tọa độ vật lý (Coordinate Invariance):** Tọa độ GPS $(lat_i, lon_i)$ của căn hộ, khoảng cách đi bộ mạng lưới tới 20 ga Metro (`metro_dist_km`, hệ số khúc quanh $\gamma = 1,32$) và khoảng cách tới tâm CBD Hồ Hoàn Kiếm (`dist_cbd_km`) là đại lượng hình học vật lý bất biến — **tuyệt đối không phải thu thập lại dữ liệu thô hay tính lại ma trận khoảng cách GIS**.
- **Giải quyết Bài toán Đơn vị Không gian Khả biến (MAUP — Openshaw, 1984) & Tránh Kiểm soát Quá mức (`VIF < 5.0`):** Nếu chỉ dùng biến giả cấp Phường nhỏ (bán kính $500\text{m}-1.200\text{m}$) làm mô hình duy nhất, diện tích phường trùng với bán kính đi bộ tới ga sẽ gây hiện tượng hấp thụ phương sai (*over-controlling*). Do đó, khóa luận kết hợp đồng thời 3 tầng không gian:

| Tầng không gian | Biến định danh | Số đơn vị | Vai trò trong Hệ thống Kinh tế lượng & Chính sách |
| :--- | :--- | :---: | :--- |
| **Tầng 1 (Mô hình Chính `M3`)** | `urban_ring_sector` + `ln_dist_cbd` | **4 Phân vùng Vành đai Đô thị** (`UZ1`–`UZ4`) | Kiểm soát cấu trúc hình thái học đô thị Hà Nội miễn nhiễm 100% với mọi cuộc cải cách hành chính; giữ $\text{VIF}_{\max} = 3,238 < 5,0$ và khử tự tương quan không gian ($\text{Moran's } I = 0,0488, p = 0,2816$). |
| **Tầng 2 (Đối chứng 1 `M4`)** | `historical_submarket` | **7 Tiểu thị trường lịch sử** (7 Quận cũ) | Kiểm soát quán tính định giá tâm lý của thị trường (*Market Pricing Inertia*, Bourassa et al., 2003) và bảo toàn đối chiếu 100% với báo cáo thực nghiệm ban đầu ($+3,91\%, R^2 = 0,2492$). |
| **Tầng 3 (Đối chứng 2 `M5`)** | `new_ward_code` (`HN_W01`–`HN_W21`) | **21 Phường mới trực thuộc TP. Hà Nội** | Chứng minh độ bền thể chế theo mô hình chính quyền 2 cấp ($+3,73\%, R^2 = 0,2500$, $\text{Moran's } I = -0,0393, p = 0,5243$) và làm cơ sở ban hành khuyến nghị cho UBND 21 Phường mới. |

---

## 3. Cấu trúc Kho lưu trữ (Repository Layout)

```text
hanoi-metro-3d-odyssey/
├── index.html                                         # Ứng dụng WebGL 3D tương tác (16.471 căn hộ, 20 ga Metro, 13 dự án P1–P13)
├── README.md                                          # Tài liệu tổng quan và hướng dẫn tái lập dự án
├── data/
│   └── metadata/
│       └── hanoi_admin_crosswalk_2026.json            # Từ điển ánh xạ 3 tầng không gian (4 Vành đai, 21 Phường mới 2 cấp, 7 Tiểu thị trường, 20 Ga Metro)
├── src/
│   ├── gis/
│   │   └── spatial_crosswalk.py                       # Module GIS tính khoảng cách mạng lưới đi bộ (γ=1.32) & Dual Point-in-Polygon 3 tầng
│   └── models/
│       └── run_hedonic_multi_tier.py                  # Pipeline kinh tế lượng ước lượng 6 mô hình Hedonic (M1–M6, HC3 SE, VIF, Moran's I)
├── tests/
│   └── test_spatial_pipeline.py                       # Bộ 5 kiểm thử tự động (Automated Quality Gates G2–G5)
├── outputs/
│   └── tables/
│       ├── hedonic_multi_tier_results.csv             # Bảng kết quả hồi quy đầy đủ của 6 mô hình (M1–M6)
│       ├── spatial_crosswalk_summary.csv              # Thống kê mô tả theo 4 Phân vùng Vành đai Đô thị (UZ1–UZ4)
│       ├── new_2level_ward_summary.csv                # Thống kê mô tả theo 21 Phường mới trực thuộc TP. Hà Nội (HN_W01–HN_W21)
│       └── empirical_findings_v2.json                 # JSON tổng hợp hệ số, kiểm định VIF và Moran's I
└── docs/
    ├── reports/
    │   └── Bao_Cao_Ket_Qua_Thuc_Nghiem_Hanoi_Metro.md # Báo cáo Kết quả Thực nghiệm Định lượng (Phiên bản Đa tầng 2026)
    ├── thesis/
    │   └── Ban_Thao_Khoa_Luan_5_Chuong.md             # Toàn văn Bản thảo Khóa luận Tốt nghiệp 5 Chương (kèm Mục 3.2.4 & Phụ lục)
    └── defense/
        └── So_Tay_Phan_Bien_Hoi_Dong_QA.md            # Sổ tay Phản biện & Bảo vệ trước Hội đồng 9 Thành viên (kèm Rubric 100 điểm)
```

---

## 4. Hướng dẫn Tái lập Kết quả 100% (Reproducibility)

### Bước 1: Chạy Pipeline Kinh tế lượng Không gian Đa tầng (`M1`–`M6`)
```bash
python3 src/models/run_hedonic_multi_tier.py
```
Kết quả xuất ra màn hình và lưu tự động vào `outputs/tables/`:
- `M3_Main_UrbanRing_CBD`: $\hat{\beta}_{500-1000\text{m}} = 0,0354^{***}$ ($SE = 0,0048 \rightarrow \mathbf{+3,61\%}$), $R^2 = 0,2470$
- `M4_Robust_HistoricalSubmarket`: $\hat{\beta}_{500-1000\text{m}} = 0,0383^{***}$ ($SE = 0,0048 \rightarrow \mathbf{+3,91\%}$), $R^2 = 0,2492$
- `M5_Robust_NewWard_2Level`: $\hat{\beta}_{500-1000\text{m}} = 0,0366^{***}$ ($SE = 0,0063 \rightarrow \mathbf{+3,73\%}$), $R^2 = 0,2500$
- `M6_Sensitivity_ExactProjectOnly` ($N = 10.521$): $\hat{\beta}_{500-1000\text{m}} = 0,0383^{***}$ ($SE = 0,0060 \rightarrow \mathbf{+3,90\%}$), $R^2 = 0,2530$

### Bước 2: Chạy Bộ Kiểm thử Tự động (`Automated Quality Gates`)
```bash
python3 -m unittest tests/test_spatial_pipeline.py -v
```
Tất cả 5 bài kiểm thử (`test_01` đến `test_05`) kiểm chứng cỡ mẫu $N = 16.471$, tính bất biến tọa độ vật lý, $\text{VIF} < 5,0$, tính vững xuyên suốt 3 tầng không gian và hiệu ứng chữ U ngược đều báo **`OK`**.

### Bước 3: Khởi chạy Ứng dụng Mô phỏng Không gian 3D (`index.html`)
Mở trực tiếp tệp `index.html` trên trình duyệt hoặc chạy máy chủ tĩnh:
```bash
python3 -m http.server 8080
```
Sau đó truy cập `http://localhost:8080` để trải nghiệm không gian 3D tương tác dọc Tuyến 2A và Tuyến 3.
