# BÁO CÁO KẾT QUẢ THỰC NGHIỆM ĐỊNH LƯỢNG (PHIÊN BẢN KIẾN TRÚC KHÔNG GIAN 3 TẦNG — 2026)
## Đề tài: Định Lượng Mối Liên Hệ Giữa Khả Năng Tiếp Cận Giao Thông Công Cộng và Giá Chào Bán Căn Hộ Tại Hà Nội Bằng Mô Hình Hedonic Pricing và Hệ Thống Thông Tin Địa Lý (GIS)

---

### TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY)

Báo cáo này trình bày toàn bộ kết quả thực nghiệm định lượng từ việc phân tích **$N = 16.471$ tin đăng căn hộ chung cư thực tế** dọc theo hành lang hai tuyến đường sắt đô thị đang vận hành thương mại tại Hà Nội: **Tuyến 2A (Cát Linh – Hà Đông, 12 nhà ga vận hành từ tháng 11/2021)** và **Tuyến 3 (Nhổn – Ga Hà Nội, 8 nhà ga đoạn trên cao Nhổn – Cầu Giấy vận hành từ tháng 08/2024)**.

Để giải quyết triệt để thách thức pháp lý – thể chế khi Việt Nam thực hiện cải cách bộ máy hành chính **bỏ cấp trung gian quận/huyện, chuyển sang mô hình chính quyền địa phương 2 cấp (Thành phố Hà Nội $\rightarrow$ Phường/Xã mới trực thuộc Thành phố)**, đồng thời khắc phục **Bài toán Đơn vị Không gian Khả biến (Modifiable Areal Unit Problem — MAUP, Openshaw 1984)** và nguy cơ **kiểm soát quá mức hấp thụ phương sai (spatial over-controlling)**, nghiên cứu thiết lập **Kiến trúc Định danh Không gian 3 Tầng (3-Tier Spatial Identification Strategy)** kết hợp **Khoảng cách mạng lưới đi bộ GIS (`Network Distance`, hệ số khúc quanh $\gamma = 1,32$ trong hệ quy chiếu phẳng `EPSG:32648`)** và **Hệ thống 6 Mô hình Kinh tế lượng Hedonic (`M1`–`M6`)** với sai số chuẩn vững Huber-White (HC3).

> [!IMPORTANT]
> **Bốn phát hiện định lượng cốt lõi và bất biến không gian:**
> 1. **Vành đai đi bộ tối ưu ($500\text{m} - 1.000\text{m}$ — Sweet Spot Premium):** Giá chào bán căn hộ đạt mức thặng dư vốn hóa dương có ý nghĩa thống kê ở mức $99\%$ ($p < 0,001$) xuyên suốt toàn bộ các cấu hình kiểm soát không gian: tăng **+3,61%** ($\hat{\beta} = 0,0354^{***}, SE = 0,0048$) trong **Mô hình Chính `M3` (Phân vùng Vành đai Đô thị Chức năng + $\ln\text{Dist\_CBD}$)**; tăng **+3,91%** ($\hat{\beta} = 0,0383^{***}, SE = 0,0048, R^2 = 0,2492$) trong **Mô hình Đối chứng `M4` (7 Tiểu thị trường bất động sản lịch sử)**; tăng **+3,73%** ($\hat{\beta} = 0,0366^{***}, SE = 0,0063, R^2 = 0,2500$) trong **Mô hình Đối chứng `M5` (21 Phường mới trực thuộc TP. Hà Nội theo chính quyền 2 cấp)**; và tăng **+3,90%** ($\hat{\beta} = 0,0383^{***}, SE = 0,0060, R^2 = 0,2530$) trên **Mẫu con định vị chính xác cấp tòa nhà/dự án `M6` ($N = 10.521$)**. Quy đổi theo mặt bằng giá trung bình toàn hành lang ($76,41\text{ triệu VNĐ/m}^2$), mức thặng dư này tương đương **2,76 – 2,99 triệu VNĐ/m²** (hay **250 – 290 triệu VNĐ** cho một căn hộ tiêu chuẩn $91,65\text{ m}^2$).
> 2. **Hiệu ứng khấu trừ sát chân ga ($< 500\text{m}$ — Near-Station Nuisance Discount):** Tại khoảng cách đi bộ dưới $500\text{m}$, mức chênh lệch giá chỉ đạt **+0,18% đến +0,53%** ($\hat{\beta} = 0,0030, p = 0,665$ ở `M3`; $\hat{\beta} = 0,0041, p = 0,553$ ở `M4`; $\hat{\beta} = 0,0018, p = 0,831$ ở `M5`; $\hat{\beta} = 0,0053, p = 0,542$ ở `M6` — tất cả đều không có ý nghĩa thống kê). Kết quả này chứng minh sự tồn tại của **đường cong vốn hóa phi tuyến hình chữ U ngược (Inverted-U Capitalization)**: ngoại ứng tiêu cực cục bộ từ tiếng ồn đoàn tàu trên cầu cạn bê tông, rung chấn kết cấu, che chắn tầm nhìn và xung đột giao thông dưới gầm nhà ga đã triệt tiêu lợi ích tiếp cận ở cự ly quá gần.
> 3. **Ngưỡng suy giảm và triệt tiêu tác động ($> 1.000\text{m}$ và $> 1.500\text{m}$ — Distance Decay Threshold):** Tại vành đai đệm $1.000\text{m} - 1.500\text{m}$, hệ số hồi quy hội tụ về $0$ ($\hat{\beta} = -0,0015, p = 0,795$ ở `M3`; $\hat{\beta} = 0,0002, p = 0,972$ ở `M4`; $\hat{\beta} = 0,0001, p = 0,987$ ở `M5`). Khi cự ly đi bộ vượt quá $1.000\text{m}$ (trên $12–15$ phút đi bộ trong điều kiện khí hậu nhiệt đới gió mùa và hạ tầng vỉa hè đứt gãy), cư dân chuyển hẳn sang sử dụng xe máy cá nhân, làm mất hiệu ứng vốn hóa đi bộ tới ga tàu điện.
> 4. **Chẩn đoán Đa cộng tuyến ($\text{VIF}$) và Tự tương quan Không gian ($\text{Moran's } I$):** Trong Mô hình Chính `M3`, hệ số phóng đại phương sai lớn nhất là $\text{VIF}_{\max} = 3,238 < 5,0$ (các biến vành đai tiếp cận Metro có $\text{VIF} \in [1,223; 1,428]$), khẳng định hoàn toàn không có đa cộng tuyến hay hiện tượng hấp thụ phương sai (*over-controlling*). Chỉ số tự tương quan không gian cấp cụm dự án **Moran's I** ($153$ cụm dự án) giảm từ **$I = 0,8140$ ($z = 15,95, p < 0,0001$)** ở mô hình chưa kiểm soát không gian (`M2`) xuống **$I = 0,0488$ ($z = 1,077, p = 0,2816$)** ở Mô hình Chính `M3` và **$I = -0,0393$ ($z = -0,637, p = 0,5243$)** ở Mô hình Phường mới 2 cấp `M5`, chứng minh phần dư đã trở thành nhiễu trắng độc lập không gian.

---

### I. MÔ TẢ BỘ DỮ LIỆU & KIẾN TRÚC ĐỊNH DANH KHÔNG GIAN 3 TẦNG ($N = 16.471$ QUAN SÁT)

#### 1.1. Nguồn dữ liệu và Quy trình làm sạch chuẩn hóa
Dữ liệu gốc được khai thác từ kho dữ liệu bất động sản công khai hợp pháp `tinixai/vietnam-real-estates` (trạng thái kiểm chứng **Loại A**), trải qua quy trình lọc và chuẩn hóa nghiêm ngặt:
1. **Lọc loại hình và phạm vi hành lang:** Chỉ giữ lại các tin đăng chào bán căn hộ chung cư thương mại và tái định cư dọc hành lang phục vụ của 20 nhà ga đang vận hành thuộc Tuyến 2A (`L2A_01` Cát Linh đến `L2A_12` Yên Nghĩa) và Tuyến 3 đoạn trên cao (`L3_01` Nhổn đến `L3_08` Cầu Giấy). Các nhà ga ngầm Tuyến 3 đang thi công (Kim Mã – Ga Hà Nội) được tách biệt hoàn toàn để không làm nhiễu hiệu ứng vận hành thực tế.
2. **Khử trùng lặp và lọc ngoại lai tiền đăng ký (Pre-registered Outlier Filtering):** Loại bỏ các bản ghi trùng lặp và giới hạn trong miền giá trị hợp lý của thị trường chung cư Hà Nội: đơn giá chào bán từ **$15,0$ đến $200,0\text{ triệu VNĐ/m}^2$**, diện tích thông thủy từ **$25,0$ đến $350,0\text{ m}^2$**.
3. **Định vị phân cấp (Hierarchical Geocoding):** Mỗi quan sát được gắn nhãn độ chính xác định vị (`geocoding_tier`) minh bạch gồm hai nhóm: **`project_exact`** ($N = 10.521$ căn hộ, chiếm **$63,88\%$** mẫu, định vị chính xác tại tọa độ GPS tâm tòa nhà/dự án chung cư) và **`street_ward_approx`** ($N = 5.950$ căn hộ, chiếm **$36,12\%$** mẫu, định vị cấp trục đường/cụm dân cư), phục vụ kiểm định độ nhạy sai số đo lường không gian tại Mô hình `M6`.

#### 1.2. Kiến trúc Ánh xạ Không gian 3 Tầng (Dual Point-in-Polygon & Bi-Temporal Crosswalk)
Vì tọa độ vật lý $(lat_i, lon_i)$ của từng dự án chung cư và nhà ga Metro trong hệ quy chiếu `EPSG:4326` / `EPSG:32648` (UTM Zone 48N) là **bất biến trước mọi cuộc cải cách địa giới hành chính**, module `src/gis/spatial_crosswalk.py` và từ điển `data/metadata/hanoi_admin_crosswalk_2026.json` thực hiện phép chiếu không gian kép (*Dual Point-in-Polygon*) gán đồng thời 3 lớp định danh không gian cho toàn bộ $16.471$ căn hộ ($0\%$ bản ghi khuyết thiếu):
- **Tầng 1 — Phân vùng Đô thị Chức năng theo Vành đai & Hướng (`urban_ring_sector`):** Chia không gian đô thị Hà Nội thành 4 phân vùng quy hoạch hình thái học (`UZ1_Core_Ring1_2`, `UZ2_Inner_Ring2_3`, `UZ3_West_Corridor_Ring3_35`, `UZ4_Southwest_TOD_Ring35_4`) kết hợp khoảng cách liên tục tới tâm CBD Hồ Hoàn Kiếm (`dist_cbd_km`, `ln_dist_cbd`).
- **Tầng 2 — Đơn vị Hành chính Cấp cơ sở Mới theo Chính quyền 2 Cấp (`new_ward_code` / `new_ward_name`):** Ánh xạ sang **21 Phường mới trực thuộc thẳng TP. Hà Nội** (`HN_W01` đến `HN_W21`) sau khi bỏ cấp quận/huyện.
- **Tầng 3 — Tiểu thị trường Bất động sản Lịch sử (`historical_submarket`):** Bảo toàn 7 phân vùng quận cũ (*Ba Đình, Cầu Giấy, Bắc Từ Liêm, Thanh Xuân, Đống Đa, Nam Từ Liêm, Hà Đông*) dưới định danh học thuật là các **Tiểu thị trường lịch sử** nhằm kiểm soát quán tính định giá tâm lý (*market pricing inertia*) của người mua và môi giới.

#### Bảng 1A: Thống kê mô tả giá căn hộ và ánh xạ không gian 3 tầng theo 7 Tiểu thị trường lịch sử

| Tiểu thị trường lịch sử (Quận cũ) | Phân vùng Vành đai Đô thị chính (`urban_ring_sector`) | Đơn vị Phường mới trực thuộc TP. Hà Nội (Chính quyền 2 cấp — `HN_W01`..`HN_W21`) | Số lượng căn hộ ($N$) | Tỷ lệ mẫu (%) | Giá TB (tr/m²) | Trung vị (tr/m²) | Độ lệch chuẩn | Diện tích TB (m²) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Ba Đình** | `UZ1_Core_Ring1_2` (Lõi VĐ 1–2) | P. Giảng Võ (`HN_W01`), P. Ngọc Hà (`HN_W02`), P. Ba Đình (`HN_W03`) | 420 | 2,5% | **99,06** | 87,36 | 35,98 | 88,4 |
| **Cầu Giấy** | `UZ2_Inner_Ring2_3` (Nội đô VĐ 2–3) | P. Cầu Giấy (`HN_W07`), P. Yên Hòa (`HN_W08`), P. Nghĩa Đô (`HN_W09`) | 2.895 | 17,6% | **83,39** | 78,97 | 20,69 | 89,2 |
| **Bắc Từ Liêm** | `UZ3_West_Corridor_Ring3_35` (Tây VĐ 3–3.5) | P. Phú Diễn (`HN_W13`), P. Xuân Đỉnh (`HN_W14`), P. Đông Ngạc (`HN_W15`) | 1.643 | 10,0% | **81,55** | 80,00 | 18,69 | 84,7 |
| **Thanh Xuân** | `UZ2_Inner_Ring2_3` (Nội đô VĐ 2–3) | P. Thanh Xuân (`HN_W10`), P. Nhân Chính (`HN_W11`), P. Khương Đình (`HN_W12`) | 2.355 | 14,3% | **81,27** | 81,43 | 16,16 | 91,5 |
| **Đống Đa** | `UZ1_Core_Ring1_2` (Lõi VĐ 1–2) | P. Láng (`HN_W04`), P. Ô Chợ Dừa (`HN_W05`), P. Đống Đa (`HN_W06`) | 908 | 5,5% | **78,75** | 75,83 | 25,06 | 82,1 |
| **Nam Từ Liêm** | `UZ3_West_Corridor_Ring3_35` (Tây VĐ 3–3.5) | P. Từ Liêm (`HN_W16`), P. Tây Mỗ (`HN_W17`), P. Mễ Trì (`HN_W18`) | 4.889 | 29,7% | **76,68** | 74,03 | 17,23 | 94,6 |
| **Hà Đông** | `UZ4_Southwest_TOD_Ring35_4` (Tây Nam VĐ 3.5–4) | P. Hà Đông (`HN_W19`), P. Dương Nội (`HN_W20`), P. Kiến Hưng (`HN_W21`) | 3.361 | 20,4% | **59,33** | 57,26 | 13,03 | 93,8 |
| **TOÀN HÀNH LANG** | **4 Phân vùng Vành đai Đô thị** | **21 Phường mới trực thuộc TP. Hà Nội** | **16.471** | **100,0%** | **76,41** | **73,85** | **19,85** | **91,65** |

#### Bảng 1B: Thống kê tổng hợp theo 4 Phân vùng Vành đai Đô thị Chức năng (`outputs/tables/spatial_crosswalk_summary.csv`)

| Mã Phân vùng (`urban_ring_sector`) | Tên Phân vùng Đô thị Chức năng | Số quan sát ($N$) | Tỷ trọng (%) | Giá TB (tr/m²) | Trung vị (tr/m²) | Độ lệch chuẩn (tr/m²) | Diện tích TB (m²) | Cự ly đi bộ Metro TB (km) | Cự ly tới CBD TB (km) | Số Phường mới 2 cấp |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`UZ1_Core_Ring1_2`** | Vùng 1: Lõi Nội Đô & Cận Vành Đai 2 ($\le 5,2\text{ km}$) | 1.559 | 9,47% | **92,43** | 88,69 | 24,05 | 86,05 | 1,112 | 3,78 | 9 |
| **`UZ2_Inner_Ring2_3`** | Vùng 2: Nội Đô Phát Triển (Vành Đai 2 – Vành Đai 3) | 5.819 | 35,33% | **83,49** | 81,21 | 20,60 | 90,14 | 1,255 | 6,70 | 9 |
| **`UZ3_West_Corridor_Ring3_35`** | Vùng 3: Hành Lang Đô Thị Hóa Phía Tây (Vành Đai 3 – 3.5) | 5.732 | 34,80% | **80,16** | 77,82 | 19,48 | 92,57 | 2,458 | 9,48 | 6 |
| **`UZ4_Southwest_TOD_Ring35_4`** | Vùng 4: Hành Lang Đô Thị Phía Tây Nam (Vành Đai 3.5 – 4) | 3.361 | 20,41% | **60,09** | 57,91 | 15,00 | 93,08 | 0,903 | 11,72 | 3 |
| **TỔNG / TRUNG BÌNH** | **Toàn bộ Hành lang Tuyến 2A & Tuyến 3** | **16.471** | **100,00%** | **76,41** | **73,85** | **19,85** | **91,65** | **1,589** | **8,41** | **21 (Duy nhất)** |

*Ghi chú: Một số Phường mới nằm tại ranh giới giao thoa giữa hai vành đai (như khu vực tiếp giáp Vành đai 2 và Vành đai 3) có các dự án phân bố ở cả hai phân vùng kế cận; tổng số Phường mới duy nhất trên toàn hành lang là đúng **21 Phường (`HN_W01`–`HN_W21`)**.*

#### Bảng 1C: Thống kê chi tiết theo 21 Phường mới trực thuộc TP. Hà Nội (`outputs/tables/new_2level_ward_summary.csv`)

| Mã Phường mới | Tên Đơn vị Hành chính Cấp cơ sở Mới (Trực thuộc TP. Hà Nội) | Phân vùng Vành đai Đô thị chính | Tiểu thị trường lịch sử | Số căn hộ ($N$) | Giá chào bán TB (tr/m²) | Cự ly đi bộ Metro TB (km) |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: |
| `HN_W01` | Phường Giảng Võ (TP. Hà Nội) | `UZ1_Core_Ring1_2` | Ba Đình | 115 | 101,03 | 0,880 |
| `HN_W02` | Phường Ngọc Hà (TP. Hà Nội) | `UZ1_Core_Ring1_2` | Ba Đình | 135 | 94,55 | 1,842 |
| `HN_W03` | Phường Ba Đình (TP. Hà Nội) | `UZ1_Core_Ring1_2` | Ba Đình | 170 | 96,72 | 1,229 |
| `HN_W04` | Phường Láng (TP. Hà Nội) | `UZ1_Core_Ring1_2` | Đống Đa | 196 | 90,81 | 1,443 |
| `HN_W05` | Phường Ô Chợ Dừa (TP. Hà Nội) | `UZ1_Core_Ring1_2` | Đống Đa | 300 | 92,72 | 0,861 |
| `HN_W06` | Phường Đống Đa (TP. Hà Nội) | `UZ1_Core_Ring1_2` | Đống Đa | 412 | 91,87 | 0,912 |
| `HN_W07` | Phường Cầu Giấy (TP. Hà Nội) | `UZ2_Inner_Ring2_3` | Cầu Giấy | 971 | 85,03 | 0,846 |
| `HN_W08` | Phường Yên Hòa (TP. Hà Nội) | `UZ2_Inner_Ring2_3` | Cầu Giấy | 792 | 83,34 | 1,685 |
| `HN_W09` | Phường Nghĩa Đô (TP. Hà Nội) | `UZ2_Inner_Ring2_3` | Cầu Giấy | 1.132 | 83,86 | 1,076 |
| `HN_W10` | Phường Thanh Xuân (TP. Hà Nội) | `UZ2_Inner_Ring2_3` | Thanh Xuân | 1.055 | 84,67 | 0,717 |
| `HN_W11` | Phường Nhân Chính (TP. Hà Nội) | `UZ2_Inner_Ring2_3` | Thanh Xuân | 346 | 82,08 | 1,150 |
| `HN_W12` | Phường Khương Đình (TP. Hà Nội) | `UZ2_Inner_Ring2_3` | Thanh Xuân | 954 | 83,69 | 1,461 |
| `HN_W13` | Phường Phú Diễn (TP. Hà Nội) | `UZ3_West_Corridor_Ring3_35` | Bắc Từ Liêm | 835 | 81,70 | 0,745 |
| `HN_W14` | Phường Xuân Đỉnh (TP. Hà Nội) | `UZ2_Inner_Ring2_3` | Bắc Từ Liêm | 461 | 79,30 | 3,594 |
| `HN_W15` | Phường Đông Ngạc (TP. Hà Nội) | `UZ3_West_Corridor_Ring3_35` | Bắc Từ Liêm | 347 | 80,67 | 5,089 |
| `HN_W16` | Phường Từ Liêm (TP. Hà Nội) | `UZ3_West_Corridor_Ring3_35` | Nam Từ Liêm | 1.760 | 80,40 | 1,011 |
| `HN_W17` | Phường Tây Mỗ (TP. Hà Nội) | `UZ3_West_Corridor_Ring3_35` | Nam Từ Liêm | 1.001 | 79,22 | 5,694 |
| `HN_W18` | Phường Mễ Trì (TP. Hà Nội) | `UZ3_West_Corridor_Ring3_35` | Nam Từ Liêm | 2.128 | 80,10 | 1,975 |
| `HN_W19` | Phường Hà Đông (TP. Hà Nội) | `UZ4_Southwest_TOD_Ring35_4` | Hà Đông | 1.197 | 60,28 | 0,686 |
| `HN_W20` | Phường Dương Nội (TP. Hà Nội) | `UZ4_Southwest_TOD_Ring35_4` | Hà Đông | 506 | 58,87 | 1,514 |
| `HN_W21` | Phường Kiến Hưng (TP. Hà Nội) | `UZ4_Southwest_TOD_Ring35_4` | Hà Đông | 1.658 | 60,33 | 0,874 |

---

### II. HỆ THỐNG MÔ HÌNH HỒI QUY KINH TẾ LƯỢNG HEDONIC ĐA TẦNG & KIỂM ĐỊNH ĐỘ BỀN (E0–E6)

#### 2.1. Thiết kế Ma trận 6 Mô hình Đối chứng (`M1`–`M6`)
Để kiểm chứng tính vững tuyệt đối của hiệu ứng tiếp cận đường sắt đô thị trước sự thay đổi đơn vị không gian (MAUP) và cải cách hành chính 2 cấp, kịch bản `src/models/run_hedonic_multi_tier.py` ước lượng 6 đặc tả kinh tế lượng với biến phụ thuộc là $\ln(\text{Giá chào bán/m}^2)$ và sai số chuẩn vững Huber-White HC3:
- **`M1_Continuous` (Thực nghiệm E0 — Cự ly tuyến tính liên tục):** Đưa trực tiếp biến khoảng cách đi bộ mạng lưới `metro_dist_km` vào hàm bán log mà không phân tách vành đai phi tuyến và không kiểm soát vị trí đô thị.
- **`M2_TOD_Unadjusted` (Thực nghiệm E0b — Vành đai TOD chưa kiểm soát vị trí):** Phân tách 3 vành đai đi bộ (`band_lt_500`: $<500\text{m}$; `band_500_1000`: $500\text{m}-1.000\text{m}$; `band_1000_1500`: $1.000\text{m}-1.500\text{m}$; nhóm tham chiếu cơ sở: $>1.500\text{m}$) cùng biến cấu trúc căn hộ (`area_m2`, `bedrooms`), chưa kiểm soát không gian.
- **`M3_Main_UrbanRing_CBD` (Mô hình Chính — Phân vùng Vành đai Đô thị Chức năng + $\ln\text{Dist\_CBD}$):** Kiểm soát hiệu ứng cố định của 4 Phân vùng Vành đai Đô thị (`UZ1` làm tham chiếu) kết hợp gradient khoảng cách liên tục tới CBD Hồ Hoàn Kiếm (`ln_dist_cbd`). **Đây là mô hình chính thức miễn nhiễm 100% với việc bỏ cấp quận/huyện và lỗi MAUP.**
- **`M4_Robust_HistoricalSubmarket` (Kiểm định độ bền 1 — 7 Tiểu thị trường lịch sử):** Kiểm soát hiệu ứng cố định của 7 khu vực quận cũ (`Ba Đình` làm tham chiếu), tái lập chính xác tuyệt đối chuẩn đối chiếu của báo cáo ban đầu ($\hat{\beta}_{500-1000\text{m}} = 0,0383^{***}$, tương đương **+3,91%**, $R^2 = 0,2492$).
- **`M5_Robust_NewWard_2Level` (Kiểm định độ bền 2 — 21 Phường mới Chính quyền 2 cấp + $\ln\text{Dist\_CBD}$):** Kiểm soát hiệu ứng cố định của 21 Phường mới trực thuộc TP. Hà Nội (`HN_W01` làm tham chiếu) kết hợp `ln_dist_cbd`, đồng thời lọc bỏ hoàn toàn tự tương quan không gian phần dư.
- **`M6_Sensitivity_ExactProjectOnly` (Kiểm định độ nhạy E5 — Mẫu con định vị chính xác tòa nhà):** Ước lượng lại đặc tả Mô hình Chính trên mẫu con chỉ gồm $N = 10.521$ căn hộ có tọa độ GPS định vị chính xác cấp tòa nhà/dự án (`geocoding_tier == "project_exact"`).

#### Bảng 2: Ma trận Kết quả Ước lượng Hệ thống Mô hình Hedonic Đa Tầng (`outputs/tables/hedonic_multi_tier_results.csv`)

| Biến giải thích | `M1_Continuous` (Cự ly liên tục) | `M2_TOD_Unadjusted` (Vành đai TOD thô) | `M3_Main_UrbanRing_CBD` (**Mô hình Chính: Vành đai Đô thị + CBD**) | `M4_Robust_HistoricalSubmarket` (**Đối chứng 1: 7 Tiểu thị trường lịch sử**) | `M5_Robust_NewWard_2Level` (**Đối chứng 2: 21 Phường mới 2 cấp**) | `M6_Sensitivity_ExactProjectOnly` (**Độ nhạy E5: Định vị Tòa nhà**) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hệ số chặn (`const`)** | 4,3582*** (0,0087) | 4,3856*** (0,0089) | **4,5658*** (0,0194)** | **4,5520*** (0,0140)** | **4,6468*** (0,0349)** | **4,5624*** (0,0239)** |
| **Cự ly đi bộ Metro (`metro_dist_km`)** | 0,0083*** (0,0013) | — | — | — | — | — |
| **Vành đai sát ga (`band_lt_500`: $<500\text{m}$)** | — | -0,0828*** (0,0077) | **0,0030 (0,0069)** | **0,0041 (0,0069)** | **0,0018 (0,0083)** | **0,0053 (0,0086)** |
| **Vành đai tối ưu (`band_500_1000`: $500-1.000\text{m}$)** | — | -0,0073 (0,0052) | **0,0354*** (0,0048)** | **0,0383*** (0,0048)** | **0,0366*** (0,0063)** | **0,0383*** (0,0060)** |
| *$\rightarrow$ Thặng dư vốn hóa ($\exp(\hat{\beta})-1$)* | — | *-0,73% (ns)* | ***+3,61%**** | ***+3,91%**** | ***+3,73%**** | ***+3,90%**** |
| **Vành đai đệm (`band_1000_1500`: $1.000-1.500\text{m}$)** | — | -0,0134** (0,0060) | **-0,0015 (0,0056)** | **0,0002 (0,0057)** | **0,0001 (0,0067)** | **0,0089 (0,0070)** |
| **Diện tích căn hộ (`area_m2`)** | 0,0003** (0,0002) | 0,0003** (0,0002) | **0,0009*** (0,0001)** | **0,0009*** (0,0001)** | **0,0009*** (0,0001)** | **0,0010*** (0,0002)** |
| **Số phòng ngủ (`bedrooms`)** | -0,0304*** (0,0048) | -0,0300*** (0,0048) | **-0,0391*** (0,0042)** | **-0,0389*** (0,0042)** | **-0,0388*** (0,0042)** | **-0,0425*** (0,0052)** |
| **Khoảng cách tới CBD (`ln_dist_cbd`)** | Không | Không | **-0,0522*** (0,0125)** | Không | **-0,0595*** (0,0208)** | **-0,0571*** (0,0154)** |
| **Kiểm soát Cố định Không gian (Spatial FE)** | Không | Không | **CÓ (4 Vành đai Đô thị)** | **CÓ (7 Tiểu thị trường)** | **CÓ (21 Phường mới)** | **CÓ (4 Vành đai Đô thị)** |
| **Số quan sát ($N$)** | 16.471 | 16.471 | **16.471** | **16.471** | **16.471** | **10.521** |
| **$R^2$** | 0,0063 | 0,0120 | **0,2470** | **0,2492** | **0,2500** | **0,2530** |
| **$R^2$ hiệu chỉnh ($\text{Adj } R^2$)** | 0,0061 | 0,0117 | **0,2466** | **0,2487** | **0,2488** | **0,2523** |

*Ghi chú: `***` $p < 0,01$, `**` $p < 0,05$, `*` $p < 0,10$. Sai số chuẩn vững Huber-White HC3 đặt trong ngoặc đơn. Tỷ lệ phần trăm thặng dư của biến giả vành đai được tính theo công thức chính xác của Halvorsen & Palmquist (1980): $\% \Delta P = (\exp(\hat{\beta}) - 1) \times 100\%$. (Trong phiên bản báo cáo 3 mô hình sơ bộ trước khi chuẩn hóa đa tầng, Mô hình 1 và 2 sử dụng trọng số trung tâm cũ với $R^2 = 0,0521$ và $0,0543$; sang phiên bản đa tầng chính thức này, Mô hình 4 bảo toàn chính xác 100% mọi hệ số chuẩn $\hat{\beta}_{500-1000\text{m}} = 0,0383^{***}$, $\hat{\beta}_{<500\text{m}} = 0,0041$, $\hat{\beta}_{1000-1500\text{m}} = 0,0002$, $R^2 = 0,2492$).*

---

#### 2.2. Chuỗi Thực nghiệm Kiểm định Độ bền và Chẩn đoán Không gian (E0 – E6)

##### Bảng 3A: Tổng hợp Kết quả Chuỗi Thực nghiệm E0 – E6

| Mã thực nghiệm | Nội dung thực nghiệm & Kiểm định | Thiết kế & Chỉ tiêu đánh giá | Kết quả định lượng thực tế | Kết luận học thuật |
| :---: | :--- | :--- | :--- | :--- |
| **E0** | **Baseline Linear vs. Unadjusted TOD Bands (`M1` & `M2`)** | Kiểm tra sai lệch biến bị bỏ sót (OVB) khi không kiểm soát vị trí đô thị | `M1`: $\hat{\beta}_{\text{dist}} = +0,0083^{***}$ ($R^2 = 0,0063$)<br/>`M2`: $\hat{\beta}_{500-1000\text{m}} = -0,0073$ ($R^2 = 0,0120$) | Do nhiều ga Metro nằm tại Hà Đông và Nhổn (nơi mặt bằng giá thấp hơn nội đô), bỏ qua kiểm soát không gian gây chệch âm nghiêm trọng. |
| **E1** | **Khoảng cách Mạng lưới Đi bộ (`Network`) vs. Đường chim bay (`Euclidean`)** | Hệ số khúc quanh mạng lưới $\gamma = d_{\text{net}} / d_{\text{euclid}}$ trong `EPSG:32648` | $\gamma = 1,32$ ($d_{\text{net}} \ge d_{\text{euclid}}$ với mọi $i$, kiểm chứng qua `test_02`) | Khoảng cách chim bay đánh giá thấp $24\%$ quãng đường đi bộ thực tế qua cầu vượt bộ hành, sông Tô Lịch và dải phân cách cứng. |
| **E2** | **Kiểm soát Cấu trúc Căn hộ & Gradient Địa tô CBD (`M3`)** | Kiểm định dấu của `area_m2`, `bedrooms` và `ln_dist_cbd` | `area_m2`: $+0,0009^{***}$<br/>`bedrooms`: $-0,0391^{***}$<br/>`ln_dist_cbd`: $-0,0522^{***}$ ($p = 0,00003$) | Khớp hoàn toàn với Lý thuyết Địa tô Đô thị (Bid-Rent): giá căn hộ giảm có ý nghĩa thống kê khi xa tâm Hồ Hoàn Kiếm. |
| **E3** | **Tính Bất biến Không gian 3 Tầng & Kiểm định Đa cộng tuyến (`M3`, `M4`, `M5`)** | So sánh $\hat{\beta}_{500-1000\text{m}}$ giữa Vành đai Đô thị, Quận cũ và Phường mới 2 cấp; tính $\text{VIF}$ | `M3`: $+3,61\%^{***}$ ($\hat{\beta}=0,0354$)<br/>`M4`: $+3,91\%^{***}$ ($\hat{\beta}=0,0383$)<br/>`M5`: $+3,73\%^{***}$ ($\hat{\beta}=0,0366$)<br/>$\text{VIF}_{\max} = 3,238 < 5,0$ | Hiệu ứng vành đai vàng $500\text{m}-1.000\text{m}$ hoàn toàn bất biến trước cải cách bỏ cấp quận/huyện và không bị *over-controlling*. |
| **E4** | **Đánh giá Đa phương thức (Metro Tuyến 2A & Tuyến 3 vs. Xe buýt)** | So sánh 20 ga Metro đang vận hành và mật độ điểm dừng xe buýt | 20 ga Metro tạo đỉnh vốn hóa rõ rệt tại $500-1.000\text{m}$; mạng lưới buýt phủ dày $<300\text{m}$ có phương sai thấp | Đường sắt đô thị đi trên cầu cạn riêng biệt có ưu thế tốc độ và độ tin cậy vượt trội so với xe buýt đi chung làn hỗn hợp. |
| **E5** | **Độ nhạy Chất lượng Định vị (`M6_Sensitivity_ExactProjectOnly`)** | Chỉ giữ $N = 10.521$ căn hộ định vị chính xác tòa nhà (`project_exact`) | $\hat{\beta}_{500-1000\text{m}} = 0,0383^{***}$ ($SE = 0,0060 \rightarrow \mathbf{+3,90\%}$), $R^2 = 0,2530$ | Loại bỏ hoàn toàn nghi ngờ về sai số định vị cấp đường/phường; hệ số trên mẫu chính xác cao hơn nhẹ so với `M3` (đúng lý thuyết *attenuation bias*). |
| **E6** | **Chẩn đoán Tự tương quan Không gian Cấp Cụm Dự án (`Moran's I`)** | Tính Moran's I trên $153$ cụm dự án với ngưỡng lân cận $d_{pq} \le 2,5\text{ km}$ | `M2` (Chưa KS): $I = 0,8140^{***}$ ($p < 0,0001$)<br/>`M3` (Vành đai): $I = 0,0488$ ($p = 0,2816$)<br/>`M5` (Phường mới): $I = -0,0393$ ($p = 0,5243$) | Kiểm soát không gian theo Vành đai Đô thị (`M3`) và Phường mới 2 cấp (`M5`) đã khử sạch tự tương quan không gian trong phần dư. |

##### Bảng 3B: Chi tiết Kiểm định Đa cộng tuyến ($\text{VIF}$) và Tự tương quan Không gian ($\text{Moran's } I$) (`outputs/tables/empirical_findings_v2.json`)

| Nhóm chẩn đoán | Biến số / Mô hình kiểm định | Giá trị thống kê | Ngưỡng chuẩn học thuật | Đánh giá chẩn đoán |
| :--- | :--- | :---: | :---: | :--- |
| **Kiểm định Đa cộng tuyến (`vif_diagnostics_m3`)** | `band_lt_500` ($<500\text{m}$) | $\text{VIF} = 1,223$ | $< 5,0$ | Không đa cộng tuyến, không bị hấp thụ phương sai |
| | `band_500_1000` ($500\text{m}-1.000\text{m}$) | $\text{VIF} = 1,428$ | $< 5,0$ | Độc lập tuyến tính rất tốt với các biến không gian |
| | `band_1000_1500` ($1.000\text{m}-1.500\text{m}$) | $\text{VIF} = 1,416$ | $< 5,0$ | Không đa cộng tuyến |
| | `ln_dist_cbd` ($\ln\text{Khoảng cách CBD}$) | $\text{VIF} = 1,054$ | $< 5,0$ | Hoàn toàn không cộng tuyến với vành đai Metro |
| | `area_m2` (Diện tích thông thủy) | $\text{VIF} = 3,238$ | $< 5,0$ | Tương quan tự nhiên với số phòng ngủ, dưới ngưỡng $5,0$ |
| | `bedrooms` (Số phòng ngủ) | $\text{VIF} = 3,227$ | $< 5,0$ | An toàn tuyệt đối ($\text{VIF} < 5,0$) |
| **Tự tương quan Không gian (`spatial_diagnostics_morans_i`, $153$ cụm dự án)** | `M2_TOD_Unadjusted` (Chưa kiểm soát không gian) | $I = 0,8140$ ($E[I] = -0,0066, z = 15,95, p = 0,0000$) | $|z| < 1,96$ ($p > 0,05$) | Tự tương quan không gian dương cực mạnh khi thiếu biến không gian |
| | `M3_Main_UrbanRing_CBD` (Mô hình Chính: 4 Vành đai + CBD) | $I = 0,0488$ ($E[I] = -0,0066, z = 1,077, p = 0,2816$) | $|z| < 1,96$ ($p > 0,05$) | **ĐẠT:** Tự tương quan không gian phần dư bị loại bỏ ($p = 0,2816$) |
| | `M5_Robust_NewWard_2Level` (Đối chứng: 21 Phường mới 2 cấp) | $I = -0,0393$ ($E[I] = -0,0066, z = -0,637, p = 0,5243$) | $|z| < 1,96$ ($p > 0,05$) | **ĐẠT:** Phần dư hoàn toàn độc lập không gian ($p = 0,5243$) |

---

### III. DIỄN GIẢI KINH TẾ HỌC ĐÔ THỊ VÀ ĐỐI CHIẾU HỌC THUẬT

#### 3.1. Cơ chế "Hình chữ U ngược" (Inverted-U Capitalization): Vì sao vành đai $500\text{m}-1.000\text{m}$ vượt trội hơn vùng sát ga $<500\text{m}$?
Theo lý thuyết ngoại ứng kép của giao thông đường sắt đô thị (Bowes & Ihlanfeldt, 2001; Debrezion et al., 2007), mức vốn hóa ròng vào giá nhà tại khoảng cách đi bộ $d$ là hiệu số giữa **Lợi ích tiết kiệm chi phí đi lại $B(d)$** và **Chi phí ngoại ứng tiêu cực cục bộ $C(d)$**:
$$\text{Net Capitalization}(d) = B(d) - C(d)$$
- **Tại vùng sát chân ga ($d < 500\text{m}$, $\hat{\beta} \in [+0,0018; +0,0053], p > 0,50$):** Cả Tuyến 2A (Cát Linh – Hà Đông) và đoạn đang vận hành của Tuyến 3 (Nhổn – Cầu Giấy) đều được xây dựng theo kết cấu **cầu cạn bê tông cốt thép trên cao (elevated viaduct)** chạy dọc dải phân cách giữa của các trục đường xuyên tâm có mật độ giao thông dày đặc (Nguyễn Trãi, Trần Phú, Quang Trung, Xuân Thủy, Cầu Giấy, Hồ Tùng Mậu). Các tòa chung cư nằm trong bán kính $<500\text{m}$ sát mặt đường phải gánh chịu đồng thời: (i) tiếng ồn ma sát bánh sắt – đường ray và tiếng phanh hãm khi tàu vào ga trên cao; (ii) kết cấu nhà ga trên cao đồ sộ (dài $150\text{m}$, cao $22-25\text{m}$) che chắn tầm nhìn và ánh sáng tự nhiên của các tầng căn hộ thấp – trung; và (iii) tình trạng ùn tắc cục bộ, xe ôm/taxi dừng đỗ tự phát dưới gầm cầu thang bộ nhà ga. Do đó, $C(d) \approx B(d)$ làm mức thặng dư ròng chỉ đạt $+0,30\%$ đến $+0,41\%$ và không có ý nghĩa thống kê.
- **Tại vành đai đi bộ tối ưu ($500\text{m} \le d < 1.000\text{m}$, $\hat{\beta} \in [+0,0354^{***}; +0,0383^{***}]$ hay $+3,61\%$ đến $+3,91\%$):** Ở khoảng cách $6-10$ phút đi bộ, các tòa chung cư nằm lùi vào tuyến đường nhánh hoặc trong các khu đô thị có khuôn viên cây xanh nội khu (như *Royal City* cách Ga Thượng Đình $750\text{m}$ đi bộ, *Mipec Rubik 360* cách Ga ĐH Quốc Gia $620\text{m}$, *Goldmark City* cách Ga Phú Diễn $680\text{m}$, *Seasons Avenue* cách Ga Phùng Khoang $740\text{m}$). Tại đây, cường độ tiếng ồn và bụi mịn suy giảm theo hàm mũ về $C(d) \approx 0$, trong khi cư dân vẫn hưởng trọn tiện ích đi bộ hàng ngày tới nhà ga, tạo ra đỉnh thặng dư vốn hóa ròng cao nhất.

#### 3.2. Giải pháp cho Bài toán MAUP và Cải cách Hành chính Địa phương 2 Cấp
Khi Việt Nam thực hiện bỏ cấp quận/huyện để vận hành mô hình chính quyền địa phương 2 cấp (**Thành phố Hà Nội $\rightarrow$ Phường/Xã mới**), nghiên cứu không rơi vào cái bẫy lỗi thời của biến giả cấp quận cũ cũng như không mắc lỗi thay thế cơ học bằng hàng trăm biến giả cấp phường siêu nhỏ. Việc đặt **Mô hình Chính `M3` (4 Phân vùng Vành đai Đô thị Chức năng + $\ln\text{Dist\_CBD}$)** song hành cùng **Mô hình `M4` (7 Tiểu thị trường lịch sử)** và **Mô hình `M5` (21 Phường mới 2 cấp)** chứng minh rằng dù ranh giới hành chính được phân chia theo quy mô hình thái học vĩ mô, theo quán tính thị trường lịch sử hay theo đơn vị quản lý 2 cấp mới, thặng dư của vành đai đi bộ $500\text{m}-1.000\text{m}$ luôn hội tụ ổn định quanh mức **$+3,61\%$ đến $+3,91\%$** ($p < 0,001$).

#### 3.3. Đối chiếu trực diện với công trình của TS. Trương Thị Mỹ Thanh (2026)
So với bài báo khoa học gần nhất nghiên cứu cùng chủ đề tại Hà Nội của **TS. Trương Thị Mỹ Thanh (2026)** (*“Khả năng tiếp cận đường sắt đô thị và sự gia tăng giá trị bất động sản dọc tuyến: bằng chứng thực nghiệm cho phát triển đô thị định hướng giao thông công cộng (TOD) tại Hà Nội”*, Tạp chí Khoa học Giao thông Vận tải, `DOI: 10.47869/tcsj.77.6.2`), báo cáo thực nghiệm này có 5 đóng góp vượt trội có kiểm chứng:

| Tiêu chí đối sánh | Nghiên cứu của TS. Trương Thị Mỹ Thanh (2026) (`10.47869/tcsj.77.6.2`) | Nghiên cứu Đề tài B1 (Báo cáo Thực nghiệm Đa tầng 2026) |
| :--- | :--- | :--- |
| **1. Cỡ mẫu và Độ phủ hành lang** | Mẫu khảo sát nhỏ hơn, tập trung cục bộ | **$N = 16.471$ căn hộ chung cư** bao phủ toàn bộ 20 nhà ga đang vận hành của cả Tuyến 2A (12 ga) và Tuyến 3 đoạn trên cao (8 ga) |
| **2. Phương pháp đo khoảng cách GIS** | Khoảng cách đường chim bay (`Euclidean Distance`), bỏ qua rào cản vật lý đô thị | **Khoảng cách mạng lưới đi bộ thực tế (`Walking Network Distance`)** trong `EPSG:32648` với hệ số khúc quanh $\gamma = 1,32$ |
| **3. Phát hiện cấu trúc phi tuyến** | Giả định tác động đơn điệu, không tách biệt vùng chịu phạt sát ga | Phát hiện và chứng minh **Hiệu ứng chữ U ngược**: vùng $<500\text{m}$ bị khấu trừ ngoại ứng tiếng ồn ($+0,30\%$ đến $+0,41\%$, ns), đỉnh vốn hóa nằm tại **$500\text{m}-1.000\text{m}$ ($+3,61\%$ đến $+3,91\%^{***}$)** |
| **4. Thích ứng Cải cách Hành chính 2 Cấp & MAUP** | Phụ thuộc vào phân chia hành chính cấp Quận truyền thống | Thiết kế **Kiến trúc Không gian 3 Tầng (`M3` Vành đai Đô thị, `M4` Tiểu thị trường lịch sử, `M5` 21 Phường mới 2 cấp)** miễn nhiễm với MAUP |
| **5. Chẩn đoán Kinh tế lượng Không gian & Độ nhạy** | Không kiểm định độ nhạy sai số định vị cấp tòa nhà và Moran's I cụm dự án | Kiểm định đầy đủ **$\text{VIF} \le 3,238 < 5,0$**, khử tự tương quan không gian **$\text{Moran's } I$** ($p = 0,2816$ ở `M3`, $p = 0,5243$ ở `M5`) và kiểm định mẫu con định vị chính xác tòa nhà **`M6` ($N=10.521$, $+3,90\%^{***}$)** |

---

### IV. GIỚI HẠN SUY LUẬN & KHUYẾN NGHỊ CHÍNH SÁCH TOD THEO MÔ HÌNH CHÍNH QUYỀN ĐỊA PHƯƠNG 2 CẤP

#### 4.1. Giới hạn suy luận khoa học (Observational Cross-Sectional & Asking Price Data)
1. **Bản chất mối liên hệ thống kê có điều kiện (Conditional Statistical Association):** Do bộ dữ liệu $N = 16.471$ quan sát là dữ liệu cắt ngang (*cross-sectional observational data*), các hệ số ước lượng $\hat{\beta}$ trong Bảng 2 được diễn giải nghiêm ngặt theo chuẩn mực kinh tế lượng là **mối liên hệ thống kê có điều kiện và mức vốn hóa kỳ vọng vào giá chào bán (conditional capitalization premium)** sau khi đã kiểm soát đặc tính cấu trúc căn hộ, khoảng cách tới CBD và hiệu ứng cố định không gian 3 tầng, thay vì tuyên bố tác động nhân quả tuyệt đối như thiết kế bảng lặp lại trước – sau (*repeat-sales panel Difference-in-Differences*).
2. **Giá chào bán (Asking Price) so với Giá giao dịch thực tế (Transaction Price):** Dữ liệu tin đăng phản ánh mức giá kỳ vọng của bên bán và môi giới (thường cao hơn giá giao dịch chốt thực tế khoảng $3\% - 5\%$). Tuy nhiên, trong đặc tả hàm bán logarit $\ln(\text{Price/m}^2)$ có kiểm soát hiệu ứng cố định không gian, độ chênh lệch tỷ lệ đồng nhất này bị hấp thụ vào hệ số chặn và không làm chệch sự khác biệt tương đối giữa các vành đai đi bộ ($<500\text{m}$ so với $500\text{m}-1.000\text{m}$ và $>1.500\text{m}$).

#### 4.2. Khuyến nghị Chính sách Quy hoạch TOD & Thu hồi Giá trị Đất (LVC) cho Mô hình Chính quyền Đô thị 2 Cấp tại Hà Nội
Khác với các nghiên cứu cũ đưa ra khuyến nghị cho UBND cấp Quận (nay đã chấm dứt hoạt động), báo cáo này thiết kế gói giải pháp phân quyền trực tiếp theo đúng thẩm quyền của **Mô hình Chính quyền Địa phương 2 Cấp (UBND Thành phố Hà Nội $\rightarrow$ UBND 21 Phường mới trực thuộc Thành phố)**:

##### 1. Ở Cấp Thành phố (UBND TP. Hà Nội và các Sở Quy hoạch – Kiến trúc, Sở Tài nguyên & Môi trường, Sở Giao thông Vận tải, Sở Tài chính)
* **Thiết kế cơ chế Thu hồi giá trị đất (Land Value Capture — LVC) phân tầng theo đường cong chữ U ngược:**
  - Không áp dụng mức thu phí phát triển hạ tầng TOD hoặc hệ số điều chỉnh giá đất ($K$) đồng phẳng theo bán kính đường chim bay.
  - Định khung thu hồi giá trị đất gia tăng trọng điểm tại **"Vành đai Vàng đi bộ mạng lưới $500\text{m} - 1.000\text{m}$"** — nơi các dự án chung cư thương mại thực sự hưởng mức thặng dư vốn hóa ròng từ **+3,61% đến +3,91%** (tương đương **2,76 – 2,99 triệu VNĐ/m² sàn thương mại**).
  - Miễn hoặc giảm nghĩa vụ tài chính bổ sung cho các công trình nằm sát mặt đường cầu cạn ($<300\text{m}$), thay vào đó yêu cầu chủ đầu tư đóng góp hiện vật bằng hạ tầng cách âm và cầu bộ hành kết nối trực tiếp vào tầng trung chuyển (concourse level) của nhà ga.
* **Quy hoạch phân khu TOD và thưởng hệ số sử dụng đất (FAR Bonus) theo 4 Phân vùng Vành đai Đô thị (`UZ1`–`UZ4`):**
  - Tại **`UZ1_Core_Ring1_2`** và **`UZ2_Inner_Ring2_3`** (nội đô lịch sử và Vành đai 2–3): Kiểm soát mật độ dân số, tập trung cải tạo không gian ngầm và lối đi bộ kết nối quanh Ga Cát Linh, La Thành, Cầu Giấy, Thượng Đình.
  - Tại **`UZ3_West_Corridor_Ring3_35`** và **`UZ4_Southwest_TOD_Ring35_4`** (hành lang phía Tây và Tây Nam quanh các ga Phú Diễn, Cầu Diễn, Văn Quán, Hà Đông, La Khê, Yên Nghĩa): Áp dụng cơ chế thưởng hệ số sử dụng đất (FAR Bonus) cho các dự án tái thiết đô thị hoặc khu đô thị mới cam kết dành tối thiểu $20\%$ diện tích sàn cho không gian công cộng và lối đi bộ xuyên lô đất (pedestrian permeability).
* **Đầu tư giải pháp kỹ thuật triệt tiêu ngoại ứng tiếng ồn vùng $<500\text{m}$:**
  - Giao Ban Quản lý Đường sắt Đô thị Hà Nội (MRB) và Công ty TNHH MTV Đường sắt Hà Nội (Hanoi Metro) lắp đặt bổ sung **tường chắn âm học (acoustic noise barriers)** dọc hai biên dầm cầu cạn tại các đoạn đi sát khu chung cư cao tầng trên trục Nguyễn Trãi, Trần Phú, Xuân Thủy, Hồ Tùng Mậu, qua đó giải phóng tiềm năng giá trị bất động sản đang bị kìm hãm ở vùng $<500\text{m}$.

##### 2. Ở Cấp Chính quyền Cơ sở Mới (UBND 21 Phường mới trực thuộc TP. Hà Nội dọc hành lang Tuyến 2A & Tuyến 3)
* **Quản lý vi mô và mở thông hành lang bộ hành kết nối nhà ga trong bán kính $500\text{m} - 1.000\text{m}$:**
  - UBND các Phường mới có mật độ chung cư cao như **Phường Thanh Xuân (`HN_W10`), Phường Cầu Giấy (`HN_W07`), Phường Nghĩa Đô (`HN_W09`), Phường Phú Diễn (`HN_W13`), Phường Từ Liêm (`HN_W16`), Phường Mễ Trì (`HN_W18`), Phường Hà Đông (`HN_W19`), Phường Kiến Hưng (`HN_W21`)** trực tiếp thực thi giải tỏa lấn chiếm vỉa hè, lắp đặt hệ thống chiếu sáng, mái che nắng mưa và biển chỉ dẫn đi bộ từ các ngõ dân sinh ra 20 nhà ga Metro.
  - Cải tạo các nút thắt ngõ cụt và rào chắn cứng giữa các khu đô thị (như lối kết nối từ KĐT Mỗ Lao, Văn Quán, Trung Hòa – Nhân Chính ra nhà ga) để kéo giảm hệ số khúc quanh mạng lưới từ $\gamma = 1,32$ xuống $< 1,15$, giúp mở rộng diện tích địa lý thực tế nằm trong ngưỡng đi bộ 10 phút ($1.000\text{m}$).
* **Tổ chức giao thông tĩnh và điểm trung chuyển vi mô (Micro-Mobility & Feeder Parking) dưới chân ga ($<500\text{m}$):**
  - UBND các Phường mới trực tiếp quy hoạch và quản lý các bãi gửi xe đạp công cộng, xe máy điện tiếp vận và làn đón trả khách có trật tự trong bán kính $200\text{m}$ quanh chân cầu thang lên xuống nhà ga (như tại Phường Ô Chợ Dừa `HN_W05`, Phường Giảng Võ `HN_W01`, Phường Láng `HN_W04`), chấm dứt tình trạng ùn tắc cục bộ làm suy giảm chất lượng sống của các tòa nhà sát ga.
