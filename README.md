# 🚝 Hanoi Metro 3D Odyssey — Định Lượng Mối Liên Hệ Giữa Tiếp Cận Giao Thông Công Cộng & Giá Chào Bán Căn Hộ Tại Hà Nội ($N = 16.471$)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](#5-hướng-dẫn-tái-lập-kết-quả-100-reproducibility)
[![Automated Tests](https://img.shields.io/badge/Unit%20Tests-6%2F6%20PASSED-10b981)](#5-hướng-dẫn-tái-lập-kết-quả-100-reproducibility)
[![Sample Size](https://img.shields.io/badge/Sample%20Size-N%20%3D%2016%2C471%20Apartments-3b82f6)](#2-kiến-trúc-định-danh-không-gian-3-tầng-giải-quyết-bài-toán-bỏ-cấp-quậnhuyện--maup)
[![Spatial Tiers](https://img.shields.io/badge/Spatial%20Architecture-3--Tier%20%282--Level%20Gov%20Ready%29-f59e0b)](#2-kiến-trúc-định-danh-không-gian-3-tầng-giải-quyết-bài-toán-bỏ-cấp-quậnhuyện--maup)
[![Autonomous 3D Presentation](https://img.shields.io/badge/3D%20Presentation-Vietnamese%20TTS%20%2B%20360%C2%B0%20Orbit-ec4899)](#3-chế-độ-trình-bày-khoa-học-tự-động-3d-autonomous-3d-scientific-presentation)

> **Đề tài Khóa luận Tốt nghiệp Đại học (Mã B1):**
> *“Định lượng mối liên hệ giữa khả năng tiếp cận giao thông công cộng và giá chào bán căn hộ tại Hà Nội bằng mô hình Hedonic Pricing và hệ thống thông tin địa lý (GIS)”*
> *(Quantifying the Association Between Public Transport Accessibility and Apartment Asking Prices in Hanoi Using Hedonic Pricing and Geographic Information Systems)*

---

## 1. Tổng quan Dự án & Ba Phát hiện Thực nghiệm Cốt lõi

Kho lưu trữ này chứa **toàn bộ mã nguồn thực nghiệm GIS – Kinh tế lượng, bộ dữ liệu đối chiếu không gian 3 tầng, hệ thống kiểm thử tự động, ứng dụng trình bày khoa học 3D tự động tích hợp thuyết minh giọng đọc tiếng Việt (`index.html`) và bộ hồ sơ Khóa luận Tốt nghiệp 5 Chương kèm Sổ tay Phản biện Hội đồng** phân tích **$N = 16.471$ tin đăng căn hộ chung cư** dọc hành lang **Tuyến Metro 2A (Cát Linh – Hà Đông, 12 nhà ga)** và **Tuyến Metro 3 (Nhổn – Ga Hà Nội, 8 nhà ga đoạn trên cao)**.

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

## 3. Chế độ Trình bày Khoa học Tự động 3D (Autonomous 3D Scientific Presentation)

Ứng dụng [`index.html`](file:///home/antigravity/tody-agent/hanoi-metro-3d-odyssey/index.html) được trang bị **Bộ Đạo diễn Trình bày Khoa học Tự động (`Autonomous Tour Director`)** kết hợp **Thuyết minh Giọng đọc Tiếng Việt (`Hybrid TTS Narration`: 13 file `.mp3` dựng sẵn + Web Speech API fallback)**:

- **Kích hoạt nhanh:** Nhấn nút **`🎙️ Trình Bày Tự Động`** trên thanh công cụ trên cùng, nút **`🎙️ Thuyết Trình 3D`** ở thanh bước dưới cùng, hoặc truy cập trực tiếp với tham số URL `?present=1` (hoặc `?stage=2`).
- **Kịch bản 8 Chặng (13 Phân cảnh đồng bộ Đoàn tàu – Điểm dừng – Xoay 3D 360° – Bảng số liệu):**
  1. **Chặng 1 (`scene_01` — `ORBIT_OVERVIEW`):** Toàn cảnh 3D Hà Nội ($N=16.471$ căn hộ, 20 ga Metro) & Kiến trúc Không gian 3 Tầng.
  2. **Chặng 2 (`scene_02` + `scene_03` — Tuyến 2A: Cát Linh $\rightarrow$ Thượng Đình):** Tàu lướt trên cầu cạn (`TRAIN_TRANSIT`), giảm tốc dừng tại **Ga Thượng Đình (`2A-05`)**, phát chuông báo vào ga và **tự động xoay 3D 360° (`STATION_STOP_ORBIT`)** phân tích cặp dự án đối chứng: **King Palace** ($410\text{m}, 82,5\text{ tr/m}^2$ — vùng ồn $<500\text{m}$) và **Royal City** ($750\text{m}, 88,7\text{ tr/m}^2$ — vành đai vàng $500–1.000\text{m}$).
  3. **Chặng 3 (`scene_04` + `scene_05` — Tuyến 2A: Thượng Đình $\rightarrow$ Hà Đông):** Tàu di chuyển qua Vành đai 3 vào Phân vùng 4 Tây Nam (`UZ4`), dừng tại **Ga Hà Đông (`2A-09`)** và xoay 3D 360° đối chứng **Seasons Avenue** ($740\text{m}$) với **KĐT Xa La** ($2.100\text{m}$, suy giảm về $0\%$).
  4. **Chặng 4 (`scene_06` + `scene_07` — Tuyến 3: Nhổn $\rightarrow$ Cầu Diễn):** Chuyển sang đoàn tàu Tuyến 3 trên cao, dừng tại **Ga Cầu Diễn (`3-04`)** và xoay 3D 360° phân tích **Goldmark City** ($680\text{m}, 84,2\text{ tr/m}^2$).
  5. **Chặng 5 (`scene_08` + `scene_09` — Tuyến 3: Cầu Diễn $\rightarrow$ ĐH Quốc Gia):** Tàu vượt cầu cạn Mai Dịch vào trục Xuân Thủy – Cầu Giấy, dừng tại **Ga ĐH Quốc Gia (`3-06`)** và xoay 3D 360° đối chứng **Indochina Plaza** ($290\text{m}$) & **Discovery Complex** ($320\text{m}$) với **Mipec Rubik 360** ($620\text{m}$).
  6. **Chặng 6 (`scene_10` — `SIMULATION_ORBIT`):** Tự động trượt tòa nhà kiểm thử 3D từ $150\text{m} \rightarrow 1.750\text{m}$ đồng thời xoay 360° minh họa sự vọt tăng chiều cao thặng dư tại $500–1.000\text{m}$.
  7. **Chặng 7 (`scene_11` + `scene_12` — `ECONOMETRIC_ORBIT`):** Dựng vòm Parabol chữ U ngược 3D + 4 cột trụ hệ số và tự động mở bảng hồi quy đa tầng `M1–M6` (`HC3`, $\text{VIF}_{\max} = 3,238 < 5,0$, $\text{Moran's } I = 0,0488$).
  8. **Chặng 8 (`scene_13` — `VALUATION_FINALE`):** Tự động vận hành máy tính định giá Hedonic ($\approx +286\text{ triệu VNĐ}$ cho căn hộ $90\text{m}^2$ tại vành đai vàng) và tổng kết khuyến nghị chính sách LVC/TOD.

---

## 4. Cấu trúc Kho lưu trữ (Repository Layout)

```text
hanoi-metro-3d-odyssey/
├── index.html                                         # Ứng dụng WebGL 3D tương tác + Đạo diễn Trình bày Khoa học Tự động 8 Chặng
├── README.md                                          # Tài liệu tổng quan và hướng dẫn tái lập dự án
├── assets/
│   └── audio/
│       ├── narration_manifest.json                    # Manifest kịch bản thuyết minh, thời lượng và siêu dữ liệu 13 phân cảnh
│       └── scene_01.mp3 .. scene_13.mp3               # 13 file âm thanh thuyết minh tiếng Việt dựng sẵn (24kHz mono MP3)
├── data/
│   └── metadata/
│       └── hanoi_admin_crosswalk_2026.json            # Từ điển ánh xạ 3 tầng không gian (4 Vành đai, 21 Phường mới 2 cấp, 7 Tiểu thị trường, 20 Ga Metro)
├── src/
│   ├── audio/
│   │   └── generate_narration_tts.py                  # Script tổng hợp giọng đọc thuyết minh tiếng Việt (Edge-TTS / Google TTS + ffmpeg)
│   ├── gis/
│   │   └── spatial_crosswalk.py                       # Module GIS tính khoảng cách mạng lưới đi bộ (γ=1.32) & Dual Point-in-Polygon 3 tầng
│   └── models/
│       └── run_hedonic_multi_tier.py                  # Pipeline kinh tế lượng ước lượng 6 mô hình Hedonic (M1–M6, HC3 SE, VIF, Moran's I)
├── tests/
│   └── test_spatial_pipeline.py                       # Bộ 6 kiểm thử tự động (Automated Quality Gates G2–G6)
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

## 5. Hướng dẫn Tái lập Kết quả 100% (Reproducibility)

### Bước 1: Chạy Pipeline Kinh tế lượng Không gian Đa tầng (`M1`–`M6`)
```bash
python3 src/models/run_hedonic_multi_tier.py
```

### Bước 2: Tái tạo Giọng đọc Thuyết minh Khoa học Tiếng Việt (`scene_01.mp3` – `scene_13.mp3`)
```bash
python3 src/audio/generate_narration_tts.py
```

### Bước 3: Chạy Bộ Kiểm thử Tự động (`Automated Quality Gates`)
```bash
python3 -m unittest tests/test_spatial_pipeline.py -v
```
Tất cả 6 bài kiểm thử (`test_01` đến `test_06`) kiểm chứng cỡ mẫu $N = 16.471$, tính bất biến tọa độ vật lý, $\text{VIF} < 5,0$, tính vững xuyên suốt 3 tầng không gian, hiệu ứng chữ U ngược và tính toàn vẹn của 13 phân cảnh thuyết minh 3D đều báo **`OK`**.

### Bước 4: Khởi chạy Ứng dụng Trình bày Khoa học 3D Tự động (`index.html`)
Mở trực tiếp tệp `index.html` trên trình duyệt hoặc chạy máy chủ tĩnh:
```bash
python3 -m http.server 8080
```
Truy cập `http://localhost:8080/?present=1` để khởi chạy ngay chế độ Trình bày Khoa học Tự động 3D kèm thuyết minh tiếng Việt.

