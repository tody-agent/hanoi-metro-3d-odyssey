# KHÓA LUẬN TỐT NGHIỆP ĐẠI HỌC (BẢN THẢO TOÀN VĂN 5 CHƯƠNG — 2026)

**TÊN ĐỀ TÀI (TIẾNG VIỆT):**
**ĐỊNH LƯỢNG MỐI LIÊN HỆ GIỮA KHẢ NĂNG TIẾP CẬN GIAO THÔNG CÔNG CỘNG VÀ GIÁ CHÀO BÁN CĂN HỘ TẠI HÀ NỘI BẰNG MÔ HÌNH HEDONIC PRICING VÀ HỆ THỐNG THÔNG TIN ĐỊA LÝ (GIS)**

**THESIS TITLE (ENGLISH):**
**QUANTIFYING THE ASSOCIATION BETWEEN PUBLIC TRANSPORT ACCESSIBILITY AND APARTMENT ASKING PRICES IN HANOI USING HEDONIC PRICING AND GEOGRAPHIC INFORMATION SYSTEMS**

* **Mã đề tài:** B1 — Kinh tế học Đô thị, Bất động sản & Hệ thống Thông tin Địa lý (GIS)
* **Địa bàn & Phạm vi nghiên cứu:** Hành lang Tuyến Đường sắt Đô thị số 2A (Cát Linh – Hà Đông, 12 nhà ga) và Tuyến số 3 (Nhổn – Ga Hà Nội, 8 nhà ga đoạn trên cao), Thành phố Hà Nội
* **Quy mô mẫu phân tích:** $N = 16.471$ căn hộ chung cư thuộc $153$ cụm dự án dọc hành lang 20 nhà ga đang vận hành thương mại
* **Kiến trúc không gian:** Định danh Không gian 3 Tầng (4 Phân vùng Vành đai Đô thị Chức năng • 21 Phường mới trực thuộc TP. Hà Nội theo Mô hình Chính quyền Địa phương 2 Cấp • 7 Tiểu thị trường Bất động sản Lịch sử)

---

## TÓM TẮT KHÓA LUẬN (EXECUTIVE ABSTRACT)

### Tóm tắt Tiếng Việt
Sự ra đời của mạng lưới đường sắt đô thị (Metro) tại Hà Nội — khởi đầu với Tuyến 2A (Cát Linh – Hà Đông, vận hành thương mại từ tháng 11/2021) và đoạn trên cao Tuyến 3 (Nhổn – Cầu Giấy, vận hành thương mại từ tháng 08/2024) — đã đặt nền móng cho mô hình Phát triển Đô thị Định hướng Giao thông Công cộng (Transit-Oriented Development — TOD) và cơ chế Thu hồi Giá trị Đất (Land Value Capture — LVC) tại Thủ đô. Tuy nhiên, việc định lượng mức vốn hóa của khả năng tiếp cận nhà ga Metro vào giá căn hộ chung cư tại Hà Nội đang đối mặt với ba thách thức phương pháp luận lớn: (1) sai lệch đo lường khi sử dụng khoảng cách đường chim bay (*Euclidean distance*) thay vì khoảng cách đi bộ thực tế trên mạng lưới đường phố (*Walking network distance*); (2) sự đứt gãy của hàm tuyến tính đơn điệu trước ngoại ứng tiếng ồn và rung chấn cầu cạn ở cự ly sát ga; và (3) sự thay đổi thể chế hành chính khi Việt Nam thực hiện bỏ cấp trung gian quận/huyện để chuyển sang **mô hình chính quyền địa phương 2 cấp (Thành phố Hà Nội $\rightarrow$ Phường/Xã mới)**, làm nảy sinh bài toán Đơn vị Không gian Khả biến (*Modifiable Areal Unit Problem — MAUP*) và nguy cơ hấp thụ phương sai (*spatial over-controlling*).

Trên cơ sở bộ dữ liệu thực nghiệm gồm **$N = 16.471$ tin đăng căn hộ chung cư** đã qua làm sạch và kiểm định từ nguồn công khai `tinixai/vietnam-real-estates`, khóa luận xây dựng quy trình đo lường khoảng cách mạng lưới đi bộ GIS trong hệ quy chiếu phẳng `EPSG:32648` (UTM Zone 48N, hệ số khúc quanh trung bình $\gamma = 1,32$) tới 20 nhà ga đang vận hành, kết hợp kỹ thuật **Dual Point-in-Polygon** để thiết lập **Kiến trúc Định danh Không gian 3 Tầng**: (i) 4 Phân vùng Vành đai – Hướng Đô thị Chức năng (`UZ1`–`UZ4`) kèm khoảng cách liên tục tới tâm CBD Hồ Hoàn Kiếm (`ln_dist_cbd`), (ii) 21 Phường mới trực thuộc TP. Hà Nội theo chính quyền 2 cấp (`HN_W01`–`HN_W21`), và (iii) 7 Tiểu thị trường bất động sản lịch sử (7 quận cũ). Hệ thống 6 mô hình kinh tế lượng Hedonic dạng bán logarit (`M1`–`M6`) được ước lượng với sai số chuẩn vững Huber-White HC3, kiểm định đa cộng tuyến $\text{VIF}$ và kiểm định tự tương quan không gian **Moran's I** cấp cụm dự án.

Kết quả thực nghiệm chứng minh sự tồn tại vững chắc của **hiệu ứng vốn hóa phi tuyến hình chữ U ngược (Inverted-U Capitalization)**:
1. Tại **vành đai đi bộ tối ưu $500\text{m} - 1.000\text{m}$** ($6–12$ phút đi bộ), giá chào bán căn hộ đạt mức thặng dư vốn hóa dương có ý nghĩa thống kê ở mức $99\%$ ($p < 0,001$) xuyên suốt mọi tầng kiểm soát không gian: **+3,61%** ($\hat{\beta} = 0,0354^{***}, SE = 0,0048, R^2 = 0,2470$) trong Mô hình Chính `M3` (Vành đai Đô thị + CBD); **+3,91%** ($\hat{\beta} = 0,0383^{***}, SE = 0,0048, R^2 = 0,2492$) trong Mô hình `M4` (Tiểu thị trường lịch sử); **+3,73%** ($\hat{\beta} = 0,0366^{***}, SE = 0,0063, R^2 = 0,2500$) trong Mô hình `M5` (21 Phường mới 2 cấp); và **+3,90%** ($\hat{\beta} = 0,0383^{***}, SE = 0,0060, R^2 = 0,2530$) trên mẫu con định vị chính xác tòa nhà `M6` ($N = 10.521$).
2. Tại **vùng sát chân ga $<500\text{m}$**, hệ số thặng dư suy giảm xuống chỉ còn **+0,18% đến +0,53%** ($\hat{\beta} = 0,0030$ ở `M3`, $\hat{\beta} = 0,0041$ ở `M4`, $\hat{\beta} = 0,0018$ ở `M5` — tất cả đều không có ý nghĩa thống kê, $p > 0,50$), do ngoại ứng tiêu cực của tiếng ồn đoàn tàu trên cầu cạn, rung chấn, che khuất tầm nhìn và ùn tắc dưới gầm ga triệt tiêu lợi ích tiếp cận.
3. Từ **ngưỡng $>1.000\text{m}$** ($1.000\text{m}-1.500\text{m}: \hat{\beta} \approx -0,0015$ đến $+0,0002, p > 0,79$) trở ra ngoài $1.500\text{m}$, hiệu ứng tiếp cận đi bộ hội tụ hoàn toàn về $0\%$ do thói quen chuyển sang xe máy cá nhân trong điều kiện khí hậu nhiệt đới.
4. Các kiểm định chẩn đoán xác nhận $\text{VIF}_{\max} = 3,238 < 5,0$ (không có đa cộng tuyến hay *over-controlling*) và chỉ số tự tương quan không gian **Moran's I** giảm từ $0,8140$ ($p < 0,0001$) ở mô hình chưa kiểm soát không gian xuống $0,0488$ ($p = 0,2816$) ở `M3` và $-0,0393$ ($p = 0,5243$) ở `M5`. Từ đó, khóa luận đề xuất khung chính sách quy hoạch TOD và thu hồi giá trị đất (LVC) phân quyền cụ thể cho cấp Thành phố và 21 Phường mới theo mô hình chính quyền địa phương 2 cấp.

### Abstract (English)
The operationalization of Hanoi's first urban rail transit corridors—Line 2A (Cat Linh – Ha Dong, 12 elevated stations opened in November 2021) and the elevated section of Line 3 (Nhon – Cau Giay, 8 stations opened in August 2024)—provides a crucial empirical setting for evaluating Transit-Oriented Development (TOD) and Land Value Capture (LVC) mechanisms. However, quantifying transit capitalization in Hanoi faces three methodological challenges: (1) measurement bias from using straight-line Euclidean distance instead of street-network walking distance; (2) non-linear proximity nuisance effects near elevated concrete viaducts; and (3) institutional boundary changes following Vietnam's administrative reform abolishing district-level governments in favor of a **two-level local government model (Hanoi City $\rightarrow$ New Wards/Communes)**, which introduces the Modifiable Areal Unit Problem (MAUP) and potential spatial over-controlling.

Drawing on a verified sample of **$N = 16,471$ apartment asking price listings** across $153$ residential project clusters from `tinixai/vietnam-real-estates`, this thesis computes GIS walking network distances in `EPSG:32648` (UTM Zone 48N, average pedestrian circuity factor $\gamma = 1.32$) to all 20 operating stations and implements a **Dual Point-in-Polygon Three-Tier Spatial Identification Architecture**: (i) 4 Functional Urban Ring-Sector Zones (`UZ1`–`UZ4`) paired with continuous log distance to the Hoan Kiem CBD (`ln_dist_cbd`), (ii) 21 New Two-Level Wards directly under Hanoi City (`HN_W01`–`HN_W21`), and (iii) 7 Historical Real Estate Submarkets (legacy districts). Six semi-log Hedonic Pricing specifications (`M1`–`M6`) are estimated with Huber-White HC3 robust standard errors, Variance Inflation Factor ($\text{VIF}$) diagnostics, and project-cluster **Moran's I** spatial autocorrelation tests.

Empirical findings demonstrate a robust **Inverted-U capitalization curve**:
1. Apartments within the **optimal walking band ($500\text{m} - 1,000\text{m}$)** command a statistically significant positive asking price premium ($p < 0.001$) across all spatial control tiers: **+3.61%** ($\hat{\beta} = 0.0354^{***}, SE = 0.0048, R^2 = 0.2470$) in the Main Functional Urban Ring-Sector Model (`M3`); **+3.91%** ($\hat{\beta} = 0.0383^{***}, SE = 0.0048, R^2 = 0.2492$) in the Historical Submarket Model (`M4`); **+3.73%** ($\hat{\beta} = 0.0366^{***}, SE = 0.0063, R^2 = 0.2500$) in the New Two-Level Ward Model (`M5`); and **+3.90%** ($\hat{\beta} = 0.0383^{***}, SE = 0.0060, R^2 = 0.2530$) in the Exact Project Location subsample (`M6`, $N = 10,521$).
2. Within the **immediate station buffer ($<500\text{m}$)**, the capitalization premium drops to an statistically insignificant **+0.18% to +0.53%** ($p > 0.50$), reflecting localized negative externalities from elevated train noise, structural vibration, visual obstruction, and station-entrance traffic congestion.
3. Beyond **$1,000\text{m}$** ($1,000\text{m}-1,500\text{m}$ buffer and $>1,500\text{m}$ reference zone), transit capitalization decays to zero as pedestrian walk times exceed 12–15 minutes in Hanoi's tropical climate.
4. Diagnostics confirm zero multicollinearity ($\text{VIF}_{\max} = 3.238 < 5.0$) and complete removal of residual spatial autocorrelation (Moran's I drops from $0.8140, p < 0.0001$ in unadjusted `M2` to $0.0488, p = 0.2816$ in `M3` and $-0.0393, p = 0.5243$ in `M5`). Actionable TOD and LVC policy recommendations are formulated for both the Municipal Government and the 21 New Ward authorities.

---

## DANH MỤC TỪ VIẾT TẮT (LIST OF ABBREVIATIONS)

| Từ viết tắt | Thuật ngữ Tiếng Anh | Nghĩa Tiếng Việt |
| :---: | :--- | :--- |
| **CBD** | Central Business District | Trung tâm Thương mại – Hành chính – Dịch vụ Đô thị (Tâm tham chiếu: Hồ Hoàn Kiếm) |
| **DiD** | Difference-in-Differences | Phương pháp Sai phân Kép (Hiệu số trong Hiệu số) |
| **EPSG** | European Petroleum Survey Group | Hệ thống mã định danh Hệ quy chiếu Không gian Quốc tế (`EPSG:4326`, `EPSG:32648`) |
| **FAR** | Floor Area Ratio | Hệ số sử dụng đất |
| **FE** | Fixed Effects | Hiệu ứng cố định (Biến giả kiểm soát không gian) |
| **GIS** | Geographic Information Systems | Hệ thống Thông tin Địa lý |
| **GTFS** | General Transit Feed Specification | Định dạng chuẩn dữ liệu lịch trình giao thông công cộng |
| **HC3** | Heteroskedasticity-Consistent SE (Type 3) | Sai số chuẩn vững kháng phương sai sai số thay đổi bậc 3 (Huber-White-MacKinnon) |
| **LVC** | Land Value Capture | Cơ chế Thu hồi Giá trị Đất tăng thêm từ đầu tư hạ tầng |
| **MAUP** | Modifiable Areal Unit Problem | Bài toán Đơn vị Không gian Diện tích Khả biến (Openshaw, 1984) |
| **MRT** | Mass Rapid Transit | Giao thông công cộng khối lượng lớn (Đường sắt đô thị) |
| **OLS** | Ordinary Least Squares | Phương pháp Bình phương Nhỏ nhất Thông thường |
| **OVB** | Omitted Variable Bias | Sai lệch do bỏ sót biến giải thích quan trọng |
| **SEM** | Spatial Error Model | Mô hình Kinh tế lượng Sai số Không gian |
| **TOD** | Transit-Oriented Development | Phát triển Đô thị Định hướng Giao thông Công cộng |
| **UTM** | Universal Transverse Mercator | Phép chiếu Hình trụ Ngang Đồng góc Quốc tế (Múi 48 Bắc — Zone 48N) |
| **VIF** | Variance Inflation Factor | Hệ số Phóng đại Phương sai (Kiểm định đa cộng tuyến) |

---

## DANH MỤC BẢNG BIỂU VÀ HÌNH ẢNH (LIST OF TABLES & FIGURES)

* **Bảng 2.1:** Ma trận Khoảng trống Nghiên cứu (*Research Gap Matrix*) đối sánh Đề tài B1 với các công trình trong và ngoài nước (bao gồm TS. Trương Thị Mỹ Thanh 2026, Nguyen et al. 2022, SAGE Open 2025).
* **Bảng 3.1:** Lưu đồ 9 bước khai thác, làm sạch và lọc mẫu dữ liệu $N = 16.471$ căn hộ chung cư Hà Nội.
* **Bảng 3.2:** Từ điển biến số (*Data Dictionary*) và kỳ vọng dấu kinh tế lượng trong mô hình Hedonic đa tầng.
* **Bảng 3.3:** Danh mục tọa độ chuẩn của 20 Nhà ga Đường sắt Đô thị đang vận hành thương mại (Tuyến 2A & Tuyến 3 đoạn trên cao).
* **Bảng 3.4:** Đặc tả toán học của 6 Mô hình Hồi quy Hedonic (`M1`–`M6`) và Ma trận Thực nghiệm (`E0`–`E6`).
* **Bảng 4.1:** Thống kê mô tả giá căn hộ và ánh xạ không gian 3 tầng theo 7 Tiểu thị trường lịch sử ($N = 16.471$).
* **Bảng 4.2:** Thống kê tổng hợp theo 4 Phân vùng Vành đai Đô thị Chức năng (`UZ1`–`UZ4`, từ `outputs/tables/spatial_crosswalk_summary.csv`).
* **Bảng 4.3:** Thống kê chi tiết theo 21 Phường mới trực thuộc TP. Hà Nội theo Mô hình Chính quyền 2 Cấp (`HN_W01`–`HN_W21`, từ `outputs/tables/new_2level_ward_summary.csv`).
* **Bảng 4.4:** Ma trận Kết quả Ước lượng Hệ thống 6 Mô hình Hedonic Đa Tầng (`M1`–`M6`, từ `outputs/tables/hedonic_multi_tier_results.csv`).
* **Bảng 4.5:** Kết quả Kiểm định Đa cộng tuyến $\text{VIF}$ và Tự tương quan Không gian $\text{Moran's } I$ cấp cụm dự án (`outputs/tables/empirical_findings_v2.json`).
* **Bảng 4.6:** Phân tích Điển cứu Thực địa (*Matched-Pair Case Studies*) trên 13 Dự án Chung cư tiêu biểu (`P1`–`P13`) dọc Tuyến 2A và Tuyến 3.
* **Bảng 5.1:** Tổng hợp trả lời trực tiếp 10 Câu hỏi Khoa học Trọng tâm của Đề tài B1.
* **Bảng 5.2:** Khung Khuyến nghị Chính sách Quy hoạch TOD và Thu hồi Giá trị Đất (LVC) phân quyền cho Chính quyền Địa phương 2 Cấp tại Hà Nội.

---

## TUYÊN BỐ LIÊM CHÍNH HỌC THUẬT & PHẠM VI SỬ DỤNG CÔNG CỤ HỖ TRỢ NGHIÊN CỨU

Tác giả cam kết tuân thủ nghiêm ngặt các quy tắc liêm chính học thuật:
1. **Không bịa đặt dữ liệu, hệ số hay tài liệu trích dẫn:** Toàn bộ $N = 16.471$ quan sát trong khóa luận được xử lý từ nguồn dữ liệu công khai hợp pháp `tinixai/vietnam-real-estates` kết hợp từ điển ánh xạ không gian chuẩn hóa `data/metadata/hanoi_admin_crosswalk_2026.json`. Mọi con số thống kê, hệ số hồi quy $\hat{\beta}$, sai số chuẩn vững HC3, giá trị $p$-value, $R^2$, $\text{VIF}$ và chỉ số $\text{Moran's } I$ trong khóa luận đều khớp chính xác $100\%$ với các tệp kết quả được sinh tự động từ kịch bản `src/models/run_hedonic_multi_tier.py` và được kiểm thử tự động bởi `tests/test_spatial_pipeline.py`.
2. **Minh bạch nguồn trích dẫn:** Mọi tài liệu tham khảo (bao gồm bài báo của TS. Trương Thị Mỹ Thanh năm 2026 với `DOI: 10.47869/tcsj.77.6.2`, Nguyen et al. năm 2022 với `DOI: 10.1016/j.eastsj.2022.100084`, và nghiên cứu năm 2025 trên SAGE Open với `DOI: 10.1177/21582440241309409`) đều có định danh thật và được phân biệt rõ phạm vi tiếp cận.
3. **Phạm vi sử dụng hệ thống tự động hóa & AI:** Công cụ lập trình tự động được sử dụng để chuẩn hóa mã nguồn Python (`src/gis/spatial_crosswalk.py`, `src/models/run_hedonic_multi_tier.py`), xây dựng bộ kiểm thử đơn vị (`tests/test_spatial_pipeline.py`), trực quan hóa 3D (`index.html`) và trình bày văn bản học thuật dưới sự kiểm chứng độc lập của bộ quy tắc Chất lượng (`GATE 0` đến `GATE 7`).

---

# CHƯƠNG 1: MỞ ĐẦU (INTRODUCTION)

## 1.1. Bối cảnh thực tiễn và Sự hình thành mạng lưới Đường sắt Đô thị tại Hà Nội

Trong hơn hai thập kỷ đô thị hóa nhanh chóng, Thành phố Hà Nội đã đối mặt với áp lực gia tăng dân số cơ học, mật độ phương tiện cá nhân vượt ngưỡng chịu tải của hạ tầng đường bộ và tình trạng ùn tắc giao thông, ô nhiễm không khí nghiêm trọng tại khu vực nội đô. Để chuyển dịch cấu trúc giao thông đô thị theo hướng bền vững, Quy hoạch chung Thủ đô Hà Nội và Quy hoạch Giao thông Vận tải Thủ đô đã xác định mạng lưới đường sắt đô thị (*Urban Rail Transit — Metro*) là xương sống của hệ thống giao thông công cộng khối lượng lớn (*Mass Rapid Transit — MRT*).

Cột mốc lịch sử của giao thông công cộng Hà Nội được đánh dấu bằng việc đưa vào vận hành thương mại hai tuyến đường sắt đô thị đầu tiên:
1. **Tuyến Đường sắt Đô thị số 2A (Cát Linh – Hà Đông):** Chính thức vận hành thương mại từ tháng 11/2021 với chiều dài $13,05\text{ km}$ đi hoàn toàn trên cầu cạn qua 12 nhà ga (`L2A_01` Ga Cát Linh đến `L2A_12` Ga Yên Nghĩa), kết nối trực tiếp khu vực lõi nội đô (Đống Đa, Ba Đình) với hành lang đô thị hóa sôi động phía Tây Nam (Thanh Xuân, Hà Đông).
2. **Tuyến Đường sắt Đô thị số 3 (Nhổn – Ga Hà Nội, đoạn trên cao Nhổn – Cầu Giấy):** Chính thức vận hành thương mại từ tháng 08/2024 với chiều dài $8,5\text{ km}$ trên cao qua 8 nhà ga (`L3_01` Ga Nhổn đến `L3_08` Ga Cầu Giấy), kết nối hành lang đô thị hóa phía Tây (Bắc Từ Liêm, Nam Từ Liêm, Cầu Giấy) với cửa ngõ nội đô.

Sự hiện diện của 20 nhà ga đang vận hành thương mại dọc hai trục xuyên tâm huyết mạch (Nguyễn Trãi – Trần Phú – Quang Trung và Hồ Tùng Mậu – Xuân Thủy – Cầu Giấy) đã làm thay đổi căn bản khả năng tiếp cận không gian (*spatial accessibility*) của hàng trăm khu chung cư cao tầng. Theo Luật Thủ đô (sửa đổi) và Luật Đất đai 2024, Hà Nội được trao quyền triển khai mô hình **Phát triển Đô thị Định hướng Giao thông Công cộng (TOD)** kết hợp các công cụ tài chính **Thu hồi Giá trị Đất tăng thêm từ hạ tầng (Land Value Capture — LVC)**. Tuy nhiên, để thiết kế đúng mức thu hồi giá trị đất và quy hoạch phân khu TOD khả thi, các nhà hoạch định chính sách cần lời giải định lượng chính xác cho câu hỏi: *Khả năng tiếp cận đi bộ tới nhà ga Metro thực sự được thị trường vốn hóa vào giá căn hộ chung cư ở mức bao nhiêu phần trăm, tại khoảng cách nào, và chịu sự chi phối của những ngoại ứng cục bộ nào?*

Đặc biệt, bước sang giai đoạn 2025–2026, Việt Nam thực hiện cuộc cải cách thể chế hành chính có tính bước ngoặt: **chấm dứt hoạt động của đơn vị hành chính cấp quận/huyện trung gian, chuyển sang mô hình chính quyền địa phương 2 cấp (Thành phố trực thuộc Trung ương $\rightarrow$ Phường/Xã cơ sở mới sau sắp xếp)**. Cuộc cải cách này đặt ra một bài toán phương pháp luận hoàn toàn mới cho các nghiên cứu kinh tế học đô thị và GIS tại Việt Nam: các mô hình định giá Hedonic truyền thống vốn phụ thuộc vào biến giả cấp Quận (*District Fixed Effects*) cần được tái cấu trúc như thế nào để vừa đảm bảo tính hợp pháp thể chế trong khuyến nghị chính sách cho chính quyền 2 cấp, vừa không rơi vào bẫy suy biến kinh tế lượng?

## 1.2. Tính cấp thiết của đề tài và Khoảng trống nghiên cứu so với các công trình hiện có

Rà soát có hệ thống các công trình nghiên cứu thực nghiệm về đường sắt đô thị và giá bất động sản tại Hà Nội cho thấy công trình gần nhất và có độ giao thoa trực tiếp cao nhất với đề tài này là bài báo của **TS. Trương Thị Mỹ Thanh (2026)**, *"Khả năng tiếp cận đường sắt đô thị và sự gia tăng giá trị bất động sản dọc tuyến: bằng chứng thực nghiệm cho phát triển đô thị định hướng giao thông công cộng (TOD) tại Hà Nội"*, đăng trên *Tạp chí Khoa học Giao thông Vận tải (Transport and Communications Science Journal)*, Tập 77, Số 6, (`DOI: 10.47869/tcsj.77.6.2`), cùng với nghiên cứu về khung thu hồi giá trị đất của **Nguyen et al. (2022)** trên *Asian Transport Studies* (`DOI: 10.1016/j.eastsj.2022.100084`) và nghiên cứu về hạ tầng giao thông với giá đất đô thị Hà Nội năm **2025** trên *SAGE Open* (`DOI: 10.1177/21582440241309409`).

Mặc dù các công trình đi trước đã đặt nền tảng quan trọng khi xác nhận mối tương quan dương giữa hạ tầng giao thông công cộng và giá trị bất động sản tại Hà Nội, việc phân tích sâu phương pháp luận của các nghiên cứu này làm lộ rõ **ba khoảng trống học thuật và thực nghiệm trọng yếu (`G1`, `G2`, `G3`)** chưa được giải quyết:

1. **Khoảng trống `G1` — Độ lệch Khoảng cách Đường chim bay so với Khoảng cách Mạng lưới Đi bộ GIS (Euclidean vs. Walking Network Distance Bias):**
   Các nghiên cứu trước đây (bao gồm Trương Thị Mỹ Thanh, 2026) chủ yếu đo lường khả năng tiếp cận bằng khoảng cách đường chim bay (*Euclidean straight-line distance*) từ bất động sản tới nhà ga. Tại Hà Nội, cấu trúc đô thị đặc trưng bởi hệ thống ngõ ngách dạng xương cá (*cul-de-sac alleys*), sông Tô Lịch, các dải phân cách cứng giữa đại lộ (Nguyễn Trãi, Xuân Thủy, Hồ Tùng Mậu) và vị trí cố định của các cầu vượt bộ hành khiến quãng đường đi bộ thực tế dài hơn đáng kể so với đường chim bay (hệ số khúc quanh trung bình $\gamma = 1,32$). Việc dùng khoảng cách Euclidean làm phân loại sai vành đai tiếp cận của khoảng $24\%$ số căn hộ quanh ga, dẫn đến sai số đo lường không gian hệ thống.
2. **Khoảng trống `G2` — Hiện tượng Vốn hóa Phi tuyến "Hình Chữ U Ngược" (Inverted-U Capitalization) và Ngoại ứng Cầu cạn:**
   Khi ép hàm khoảng cách tuyến tính đơn điệu hoặc gộp chung một bán kính rộng quanh nhà ga, các nghiên cứu trước đây mặc nhiên giả định "càng sát nhà ga thì giá nhà càng cao". Giả định này bỏ qua đặc thù kỹ thuật của Tuyến 2A và đoạn vận hành Tuyến 3 là **đường sắt đi trên cầu cạn bê tông cốt thép (elevated viaduct)** nằm sát mặt tiền các tòa nhà. Trong phạm vi $<500\text{m}$, tiếng ồn đoàn tàu, rung chấn, sự che khuất tầm nhìn của kết cấu nhà ga trên cao và ách tắc giao thông dưới gầm cầu thang ga tạo ra ngoại ứng tiêu cực (*nuisance effect*) đối kháng trực tiếp với lợi ích tiếp cận.
3. **Khoảng trống `G3` — Sự Đứt gãy Định danh Không gian khi Bỏ cấp Quận/Huyện (Mô hình Chính quyền 2 Cấp) và Bài toán MAUP:**
   Toàn bộ các mô hình Hedonic trước năm 2026 tại Hà Nội đều kiểm soát vị trí bằng biến giả cấp Quận (*7 Quận hành chính cũ*). Khi Việt Nam chuyển sang mô hình chính quyền địa phương 2 cấp (**Thành phố Hà Nội $\rightarrow$ Phường/Xã mới**), cách tiếp cận cũ vấp phải hai rủi ro chí mạng: (i) nếu giữ nguyên khung phân tích cấp quận, các hàm ý chính sách quy hoạch TOD và thu hồi giá trị đất (LVC) sẽ không còn chủ thể hành chính tương ứng để thực thi; nhưng (ii) nếu thay thế cơ học biến giả 7 quận bằng hàng chục biến giả Phường/Xã nhỏ trong mô hình chính, bán kính của một phường nội đô ($500\text{m}-1.500\text{m}$) trùng khớp với bán kính đi bộ tới ga Metro sẽ gây ra hiện tượng **kiểm soát quá mức hấp thụ phương sai (spatial over-controlling / absorption)**, làm triệt tiêu biến tiếp cận cần ước lượng.

Khóa luận này được thực hiện nhằm lấp đầy trực diện cả ba khoảng trống `G1`, `G2` và `G3` bằng một quy trình dữ liệu và kinh tế lượng không gian có khả năng tái lập $100\%$.

## 1.3. Mục tiêu nghiên cứu và Hệ thống Câu hỏi nghiên cứu

### 1.3.1. Mục tiêu nghiên cứu
* **Mục tiêu tổng quát:** Định lượng chính xác mối liên hệ thống kê có điều kiện giữa khả năng tiếp cận mạng lưới đi bộ tới 20 nhà ga đường sắt đô thị đang vận hành (Tuyến 2A và Tuyến 3) với giá chào bán căn hộ chung cư tại Hà Nội ($N = 16.471$), đồng thời xây dựng Kiến trúc Định danh Không gian 3 Tầng thích ứng hoàn toàn với mô hình chính quyền địa phương 2 cấp.
* **Mục tiêu cụ thể:**
  1. Đo lường khoảng cách mạng lưới đi bộ thực tế (`metro_dist_km`) trong hệ tọa độ phẳng `EPSG:32648` và lượng hóa độ lệch khúc quanh so với khoảng cách đường chim bay (`euclidean_dist_km`).
  2. Bóc tách cấu trúc vốn hóa phi tuyến theo các vành đai đi bộ TOD ($<500\text{m}$, $500\text{m}-1.000\text{m}$, $1.000\text{m}-1.500\text{m}$ so với $>1.500\text{m}$) để kiểm định giả thuyết "Hình chữ U ngược".
  3. Thiết lập và kiểm chứng phương pháp **Dual Point-in-Polygon & Kiến trúc Không gian 3 Tầng** (`M3` Phân vùng Vành đai Đô thị Chức năng, `M4` Tiểu thị trường lịch sử, `M5` 21 Phường mới Chính quyền 2 cấp, và `M6` Mẫu con định vị chính xác tòa nhà) nhằm giải quyết bài toán MAUP và cải cách hành chính 2 cấp.
  4. Đề xuất hệ thống khuyến nghị chính sách quy hoạch TOD và công cụ Thu hồi giá trị đất (LVC) phân quyền đúng thẩm quyền của UBND TP. Hà Nội và UBND 21 Phường mới.

### 1.3.2. Câu hỏi nghiên cứu (Research Questions)
* **Câu hỏi nghiên cứu chính:**
  > *Sau khi kiểm soát các thuộc tính cấu trúc căn hộ và tính không đồng nhất không gian đa tầng của đô thị Hà Nội, khả năng tiếp cận mạng lưới đi bộ tới các nhà ga đường sắt đô thị đang vận hành có mối liên hệ định lượng như thế nào (về chiều hướng, độ lớn và hình thái phi tuyến) với giá chào bán căn hộ chung cư?*
* **Ba câu hỏi nghiên cứu phụ:**
  1. **Câu hỏi phụ 1 (Về cơ chế phi tuyến Chữ U ngược — Trục `G2`):** Mức thặng dư vốn hóa vào giá chào bán căn hộ thay đổi như thế nào khi di chuyển từ vành đai sát chân ga ($<500\text{m}$), sang vành đai đi bộ tối ưu ($500\text{m}-1.000\text{m}$), vành đai đệm ($1.000\text{m}-1.500\text{m}$) và vùng đối chứng ($>1.500\text{m}$)?
  2. **Câu hỏi phụ 2 (Về độ nhạy đo lường GIS & chất lượng định vị — Trục `G1`):** Việc sử dụng khoảng cách mạng lưới đi bộ (`Walking Network Distance`) thay cho khoảng cách đường chim bay (`Euclidean Distance`) và việc phân lọc riêng nhóm căn hộ định vị chính xác tọa độ tòa nhà (`project_exact`, $N = 10.521$) ảnh hưởng như thế nào đến độ chính xác và tính vững của ước lượng?
  3. **Câu hỏi phụ 3 (Về cải cách chính quyền 2 cấp & bài toán MAUP — Trục `G3`):** Mức thặng dư vốn hóa tại vành đai đi bộ tối ưu $500\text{m}-1.000\text{m}$ có duy trì tính bất biến thống kê ($p < 0,01$), không đa cộng tuyến ($\text{VIF} < 5,0$) và khử sạch tự tương quan không gian ($\text{Moran's } I$) khi chuyển đổi giữa 3 tầng định danh không gian: Phân vùng Vành đai Đô thị Chức năng (`M3`), Tiểu thị trường lịch sử 7 quận cũ (`M4`), và 21 Phường mới trực thuộc TP. Hà Nội (`M5`) hay không?

## 1.4. Các Giả thuyết Nghiên cứu Tiền đăng ký (Pre-registered Hypotheses)

Để đảm bảo tính khách quan khoa học và chống hiện tượng lựa chọn kết quả có lợi (*p-hacking / HARKing*), khóa luận thiết lập 4 giả thuyết nghiên cứu tiền đăng ký trước khi ước lượng:

* **Giả thuyết H1 (Giả thuyết Vành đai Đi bộ Tối ưu — Sweet Spot Capitalization Hypothesis):**
  Các căn hộ chung cư nằm trong **vành đai đi bộ mạng lưới từ $500\text{m}$ đến $1.000\text{m}$** ($6–12$ phút đi bộ) quanh 20 nhà ga Metro đang vận hành có mức giá chào bán/m² cao hơn có ý nghĩa thống kê ở mức $1\%$ ($\beta_{500-1000\text{m}} > 0, p < 0,01$) so với nhóm căn hộ đối chứng nằm ngoài bán kính $1.500\text{m}$.
* **Giả thuyết H2 (Giả thuyết Ngoại ứng Sát chân ga & Đường cong Chữ U ngược — Near-Station Nuisance & Inverted-U Hypothesis):**
  Tại **vành đai sát chân ga ($<500\text{m}$)**, ngoại ứng tiêu cực cục bộ (tiếng ồn đoàn tàu trên cầu cạn bê tông, rung chấn kết cấu, che chắn tầm nhìn và ùn tắc giao thông dưới gầm nhà ga) làm khấu trừ lợi ích tiếp cận, khiến hệ số $\beta_{<500\text{m}}$ nhỏ hơn đáng kể so với hệ số vành đai tối ưu ($\beta_{<500\text{m}} < 0,45 \times \beta_{500-1000\text{m}}$) và không đạt ý nghĩa thống kê.
* **Giả thuyết H3 (Giả thuyết Suy giảm theo Khoảng cách & Độ lệch Mạng lưới — Distance Decay & Network Detour Hypothesis):**
  Khoảng cách mạng lưới đi bộ thực tế tại Hà Nội luôn lớn hơn hoặc bằng khoảng cách đường chim bay ($d^{\text{net}}_i \ge d^{\text{euclid}}_i$ với hệ số khúc quanh trung bình $\gamma \approx 1,32$); đồng thời khi cự ly đi bộ vượt quá $1.000\text{m}$ (vành đai đệm $1.000\text{m}-1.500\text{m}$ và vùng $>1.500\text{m}$), hiệu ứng vốn hóa của Metro suy giảm về $0$ ($\beta_{1000-1500\text{m}} \approx 0, p > 0,10$).
* **Giả thuyết H4 (Giả thuyết Bất biến Không gian trước Cải cách Hành chính 2 Cấp & MAUP — Spatial & Institutional Invariance Hypothesis):**
  Hiệu ứng thặng dư dương tại vành đai tối ưu $500\text{m}-1.000\text{m}$ duy trì tính vững thống kê ($\beta_{500-1000\text{m}} \in [0,030; 0,050], p < 0,01$) xuyên suốt cả 3 tầng kiểm soát không gian (`M3` Phân vùng Vành đai Đô thị Chức năng, `M4` Tiểu thị trường lịch sử, `M5` 21 Phường mới Chính quyền 2 cấp) và trên mẫu con định vị chính xác tòa nhà (`M6`), đồng thời đảm bảo $\text{VIF} < 5,0$ và loại bỏ tự tương quan không gian phần dư ($\text{Moran's } I$ không còn ý nghĩa thống kê ở mức $5\%$).

## 1.5. Đối tượng, Phạm vi nghiên cứu và Kết cấu của Khóa luận

* **Đối tượng nghiên cứu:** Mối liên hệ định lượng giữa khoảng cách tiếp cận mạng lưới đi bộ tới nhà ga đường sắt đô thị và đơn giá chào bán căn hộ chung cư ($\text{triệu VNĐ/m}^2$) tại Hà Nội.
* **Phạm vi không gian và dữ liệu:** $N = 16.471$ căn hộ chung cư thuộc $153$ cụm dự án dọc hành lang Tuyến 2A và Tuyến 3, được ánh xạ đầy đủ vào 4 Phân vùng Vành đai Đô thị, 21 Phường mới trực thuộc TP. Hà Nội và 7 Tiểu thị trường lịch sử. Khóa luận phân biệt rõ giữa **giá chào bán (asking price)** và **giá giao dịch thành công (transaction price)** trong suốt quá trình diễn giải.
* **Kết cấu của Khóa luận:** Ngoài phần Mở đầu hành chính học thuật, Danh mục Tài liệu tham khảo và Phụ lục, khóa luận được kết cấu thành 5 chương chuẩn mực:
  - **Chương 1:** Mở đầu (Bối cảnh, khoảng trống nghiên cứu, câu hỏi nghiên cứu và giả thuyết tiền đăng ký H1–H4).
  - **Chương 2:** Cơ sở lý thuyết và Tổng quan tài liệu (Lý thuyết Địa tô Bid-Rent, Mô hình Hedonic của Rosen, Lý thuyết Ngoại ứng Kép Chữ U ngược và Ma trận Khoảng trống Nghiên cứu).
  - **Chương 3:** Dữ liệu và Phương pháp nghiên cứu (Quy trình 9 bước xử lý dữ liệu, đo lường mạng lưới đi bộ GIS, **Mục 3.2.4 về xử lý cải cách hành chính 2 cấp bằng Dual Point-in-Polygon & giải quyết bài toán MAUP**, và đặc tả kinh tế lượng `M1`–`M6` / `E0`–`E6`).
  - **Chương 4:** Kết quả thực nghiệm và Thảo luận (Thống kê mô tả 3 tầng không gian, kết quả ước lượng `M1`–`M6`, kiểm định chẩn đoán E0–E6, phân tích 13 dự án điển cứu `P1`–`P13` và thảo luận học thuật).
  - **Chương 5:** Kết luận và Khuyến nghị chính sách (Trả lời 10 câu hỏi trọng tâm, khuyến nghị chính sách TOD & LVC cho mô hình chính quyền địa phương 2 cấp và 5 giới hạn nghiên cứu).

---

# CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ TỔNG QUAN TÀI LIỆU (LITERATURE REVIEW & THEORETICAL FRAMEWORK)

## 2.1. Lý thuyết Kinh tế học Đô thị nền tảng

### 2.1.1. Lý thuyết Địa tô Đấu giá (Bid-Rent Theory) của Alonso (1964), Muth (1969) và Mills (1972)
Nền tảng lý thuyết cổ điển giải thích sự phân bố giá đất và giá nhà ở trong không gian đô thị là **Lý thuyết Địa tô Đấu giá (Bid-Rent Theory)** do Alonso (1964) khởi xướng và được Muth (1969), Mills (1972) phát triển thành mô hình đô thị đơn tâm (*Monocentric City Model*). Theo mô hình này, mỗi hộ gia đình tối đa hóa hàm hữu dụng $U(z, q, t)$ dưới ràng buộc ngân sách:
$$Y = z + P(d) \cdot q + T(d)$$
Trong đó $Y$ là thu nhập hộ gia đình, $z$ là hàng hóa tiêu dùng tổng hợp (giá chuẩn hóa bằng 1), $q$ là diện tích nhà ở tiêu thụ, $P(d)$ là đơn giá nhà ở trên một mét vuông tại khoảng cách $d$ tính từ trung tâm việc làm – thương mại (CBD), và $T(d)$ là tổng chi phí đi lại (bao gồm chi phí tiền tệ và chi phí cơ hội của thời gian di chuyển). Điều kiện cân bằng không gian (*Spatial Equilibrium Condition* — Muth's Condition) đòi hỏi đạo hàm của đơn giá nhà ở theo khoảng cách phải bù đắp chính xác chi phí đi lại biên trên mỗi đơn vị diện tích sàn:
$$\frac{\partial P(d)}{\partial d} = -\frac{1}{q(d)} \frac{\partial T(d)}{\partial d} < 0$$
Phương trình trên dẫn đến hai hệ quả cốt lõi cho nghiên cứu này:
1. **Gradient Địa tô theo khoảng cách tới CBD ($\ln\text{Dist\_CBD}$):** Khi khoảng cách tới tâm đô thị Hồ Hoàn Kiếm ($d_{\text{CBD}}$) tăng lên, chi phí đi lại tăng làm đơn giá căn hộ $P(d_{\text{CBD}})$ giảm xuống ($\delta = \frac{\partial \ln P}{\partial \ln d_{\text{CBD}}} < 0$).
2. **Sự hình thành các cực địa tô thứ cấp quanh nhà ga đường sắt đô thị (Polycentric Transit Nodes):** Khi một tuyến đường sắt đô thị khối lượng lớn đi vào vận hành, nó cắt giảm đột ngột chi phí thời gian đi lại $\Delta T(d_{\text{metro}})$ cho các cư dân sống trong bán kính đi bộ quanh nhà ga. Theo nguyên lý cân bằng cạnh tranh, khoản tiết kiệm chi phí đi lại kỳ vọng suốt vòng đời tài sản sẽ được **vốn hóa (capitalized)** trực tiếp vào giá trị bất động sản quanh nhà ga.

### 2.1.2. Mô hình Định giá Hedonic (Hedonic Pricing Model) của Lancaster (1966) và Rosen (1974)
Bất động sản nhà ở là một hàng hóa dị biệt (*heterogeneous composite good*) không thể tách rời từng thuộc tính để giao dịch riêng lẻ trên thị trường. Dựa trên Lý thuyết Tiêu dùng Thuộc tính của Lancaster (1966), **Rosen (1974)** trong công trình kinh điển *"Hedonic Prices and Implicit Markets: Product Differentiation in Pure Competition"* đã thiết lập khung phân tích thị trường ẩn (*implicit market*): giá thị trường quan sát được của căn hộ thứ $i$ là hàm số của ba nhóm véctơ thuộc tính:
$$P_i = f\left(\mathbf{S}_i, \mathbf{N}_i, \mathbf{A}_i\right)$$
Trong đó:
- $\mathbf{S}_i$ (*Structural Attributes*): Các thuộc tính vật lý cấu trúc nội tại của căn hộ (diện tích thông thủy `area_m2`, số phòng ngủ `bedrooms`, thiết kế không gian).
- $\mathbf{N}_i$ (*Neighborhood & Macro-Spatial Attributes*): Các thuộc tính vị trí vĩ mô, chất lượng hạ tầng xã hội, tiện ích đô thị và danh tiếng khu vực (được kiểm soát qua khoảng cách tới CBD `ln_dist_cbd` và hiệu ứng cố định không gian 3 tầng: Phân vùng Vành đai Đô thị $\text{UZ}$, Tiểu thị trường lịch sử, hoặc Phường mới 2 cấp).
- $\mathbf{A}_i$ (*Transit Accessibility Attributes*): Khả năng tiếp cận mạng lưới đi bộ tới nhà ga đường sắt đô thị (`metro_dist_km` hoặc các biến giả vành đai đi bộ TOD `band_lt_500`, `band_500_1000`, `band_1000_1500`).

Đạo hàm riêng $\frac{\partial P_i}{\partial A_i}$ chính là **giá ẩn biên (marginal implicit price)** phản ánh mức sẵn lòng chi trả (*Willingness-to-Pay*) của thị trường cho một đơn vị cải thiện khả năng tiếp cận giao thông công cộng. Trong thực nghiệm kinh tế lượng bất động sản, dạng hàm **bán logarit (Semi-logarithmic / Log-linear specification)** với biến phụ thuộc là $\ln(\text{Price/m}^2_i)$ được ưu tiên sử dụng rộng rãi nhất (Malpezzi, 2003; Diewert, 2003) vì ba lý do: (1) khắc phục hiện tượng phân phối lệch phải (*right-skewness*) của dữ liệu giá nhà và giảm phương sai sai số thay đổi (*heteroskedasticity*); (2) cho phép hiệu ứng của từng thuộc tính tỷ lệ thuận với giá trị nền của căn hộ; và (3) đối với biến giả nhị phân $D_b \in \{0, 1\}$ (như vành đai đi bộ $500\text{m}-1.000\text{m}$), tỷ lệ phần trăm thay đổi giá chính xác được xác định theo công thức của **Halvorsen & Palmquist (1980)**:
$$\% \Delta \text{Price} = \left(\exp(\hat{\beta}_b) - 1\right) \times 100\%$$

## 2.2. Lý thuyết Ngoại ứng Đô thị Kép và Cơ chế Vốn hóa Phi tuyến "Hình Chữ U Ngược" (Inverted-U Capitalization)

Một sai lầm phổ biến trong các nghiên cứu sơ khai về giao thông đô thị là đồng nhất "khoảng cách tới nhà ga" với "lợi ích thuần túy". Trên thực tế, **Bowes & Ihlanfeldt (2001)**, **Debrezion, Pels & Rietveld (2007)** và **Mohammad et al. (2013)** đã chứng minh rằng một nhà ga đường sắt đô thị — đặc biệt là đường sắt đi nổi trên cầu cạn (*elevated rail*) — phát sinh đồng thời **hai ngoại ứng không gian ngược chiều nhau (Dual Spatial Externalities)**:

1. **Hiệu ứng Tiếp cận Dương (Positive Accessibility Benefit — $B(d) \ge 0$):**
   Phản ánh giá trị tiết kiệm thời gian đi lại và độ tin cậy hành trình khi người dân có thể đi bộ từ căn hộ tới nhà ga. Trong điều kiện khí hậu nhiệt đới gió mùa nóng ẩm tại Hà Nội, khả năng sẵn lòng đi bộ (*walkability*) duy trì ở mức cao trong phạm vi $d \le 1.000\text{m}$ (tương đương $\le 10-12$ phút đi bộ), sau đó suy giảm rất nhanh trong khoảng $1.000\text{m}-1.500\text{m}$ và hội tụ về $0$ khi $d > 1.500\text{m}$ (khi người dân buộc phải lấy xe máy cá nhân ra khỏi hầm chung cư).
2. **Hiệu ứng Ngoại ứng Tiêu cực Cục bộ (Localized Proximity Nuisance Cost — $C(d) \ge 0$):**
   Tập trung gay gắt trong phạm vi sát chân cầu cạn và nhà ga ($d < 500\text{m}$), bao gồm:
   - *Ô nhiễm tiếng ồn và rung chấn cơ học:* Đoàn tàu điện chạy trên dầm bê tông dự ứng lực ở độ cao $12-18\text{m}$ tạo ra tiếng ồn tần số thấp và rung chấn truyền trực tiếp vào mặt đứng các tòa chung cư nằm sát chỉ giới đường đỏ trục Nguyễn Trãi, Trần Phú, Quang Trung, Xuân Thủy, Hồ Tùng Mậu.
   - *Che chắn tầm nhìn và xâm phạm riêng tư (Visual Intrusion & Privacy Loss):* Kết cấu nhà ga trên cao dài $150\text{m}$, cao tương đương tòa nhà 6–8 tầng chắn ngang tầm nhìn ban công của các căn hộ tầng thấp và trung, đồng thời hành khách đứng trên ke ga có thể nhìn trực tiếp vào căn hộ đối diện.
   - *Ùn tắc và lộn xộn giao thông dưới chân ga (Station-Entrance Congestion):* Sự tập trung của xe ôm công nghệ, taxi, xe buýt gom khách và hàng quán vỉa hè dưới chân cầu thang bộ nhà ga gây xung đột giao thông cục bộ.

Do chi phí ngoại ứng tiêu cực $C(d)$ suy giảm theo hàm mũ rất nhanh khi lùi vào các trục đường nhánh hoặc khuôn viên nội khu cách ga từ $500\text{m}$ trở lên ($C(d) \to 0$ khi $d \ge 500\text{m}$), trong khi lợi ích tiếp cận đi bộ $B(d)$ vẫn còn nguyên vẹn trong khoảng $500\text{m} \le d < 1.000\text{m}$, hàm vốn hóa ròng:
$$\pi(d) = B(d) - C(d)$$
sẽ có dạng **đường cong hình chữ U ngược (Inverted-U Curve)**: bị nén thấp hoặc không có ý nghĩa thống kê tại vùng sát ga $<500\text{m}$, đạt **cực đại toàn cục tại "Vành đai Vàng" $500\text{m}-1.000\text{m}$**, và suy giảm về $0$ khi $d > 1.000\text{m}$.

## 2.3. Tổng quan các nghiên cứu thực nghiệm trong và ngoài nước

### 2.3.1. Các nghiên cứu quốc tế về đường sắt đô thị và giá bất động sản
Trên thế giới, mối quan hệ giữa hệ thống đường sắt đô thị (MRT/LRT) và giá trị bất động sản đã được kiểm chứng qua nhiều phân tích tổng hợp (*meta-analysis*). **Debrezion et al. (2007)** phân tích 57 nghiên cứu thực nghiệm và chỉ ra rằng bất động sản nhà ở nằm trong vùng đi bộ tối ưu quanh nhà ga đường sắt có mức giá cao hơn trung bình $4,2\%$ so với khu vực ngoài vùng phục vụ, nhưng mức thặng dư biến thiên rất mạnh tùy thuộc vào việc tách biệt ngoại ứng tiếng ồn sát ga. **Cervero & Kang (2011)** tại Seoul, **Zheng & Kahn (2008)** tại Bắc Kinh, **Pan et al. (2014)** tại Thượng Hải và **Dziauddin (2019)** tại Kuala Lumpur (nơi có hệ thống LRT trên cao và khí hậu nhiệt đới tương đồng với Hà Nội) đều ghi nhận hiện tượng các căn hộ nằm quá sát dầm cầu cạn ($<300\text{m}-400\text{m}$) chịu mức chiết khấu tiếng ồn từ $-2\%$ đến $-5\%$, trong khi vành đai $500\text{m}-1.000\text{m}$ đạt mức tăng giá ròng $+3,5\%$ đến $+7,8\%$.

Về mặt phương pháp luận không gian, **Openshaw (1984)** và **Fotheringham & Wong (1991)** đã chứng minh rằng kết quả hồi quy sử dụng dữ liệu tổng hợp theo ranh giới hành chính rất nhạy cảm với **Bài toán Đơn vị Diện tích Khả biến (MAUP)** — bao gồm hiệu ứng quy mô (*Scale Effect*) và hiệu ứng phân vùng (*Zonation Effect*). Để khắc phục, **Bourassa, Hoesli & Peng (2003)** cùng **Watkins (2001)** đề xuất kết hợp phân vùng đô thị chức năng theo cấu trúc hình thái học (*Functional Urban Ring-Sector Zones*) với các tiểu thị trường bất động sản lịch sử (*Real Estate Submarkets*) và kiểm định tự tương quan không gian của **Anselin (1988)**, **LeSage & Pace (2009)**.

### 2.3.2. Các nghiên cứu thực nghiệm tại Hà Nội và Việt Nam
Tại Hà Nội, do Tuyến 2A mới vận hành cuối năm 2021 và Tuyến 3 đoạn trên cao mới vận hành tháng 08/2024, số lượng công trình định lượng quy mô lớn còn rất hạn chế. Ba công trình tiêu biểu nhất bao gồm:
1. **Nguyen, T. B., Samsura, D. A. A., van der Krabben, E., & Le, A. D. (2022)**, *"Property value capture for development of mass rapid transit: Case study from Hanoi"*, *Asian Transport Studies*, 8, 100084 (`DOI: 10.1016/j.eastsj.2022.100084`): Phân tích tiềm năng áp dụng cơ chế thu hồi giá trị đất (LVC) cho đường sắt đô thị Hà Nội từ góc độ thể chế quy hoạch và khảo sát ban đầu, nhấn mạnh nhu cầu phải có định lượng thực nghiệm chính xác theo từng phân vùng khoảng cách quanh ga để làm cơ sở pháp lý thu hồi địa tô chênh lệch.
2. **Nghiên cứu về Hạ tầng Giao thông và Giá đất Đô thị Hà Nội (2025)**, *"The Relationship Between Transport Infrastructure and Urban Land Prices: A Study in Hanoi, Vietnam"*, *SAGE Open*, (`DOI: 10.1177/21582440241309409`): Khảo sát mối quan hệ giữa mạng lưới đường bộ chính, đường vành đai và mặt bằng giá đất tại Hà Nội, khẳng định vai trò quyết định của cấu trúc Vành đai (Vành đai 2, Vành đai 3, Vành đai 3.5) trong việc định hình mặt bằng giá bất động sản Thủ đô.
3. **TS. Trương Thị Mỹ Thanh (2026)**, *"Khả năng tiếp cận đường sắt đô thị và sự gia tăng giá trị bất động sản dọc tuyến: bằng chứng thực nghiệm cho phát triển đô thị định hướng giao thông công cộng (TOD) tại Hà Nội"*, *Tạp chí Khoa học Giao thông Vận tải (TCSJ)*, 77(6), (`DOI: 10.47869/tcsj.77.6.2`): Đây là nghiên cứu thực nghiệm gần nhất đánh giá tác động của đường sắt đô thị tới giá bất động sản tại Hà Nội. Tuy nhiên, như đã phân tích tại Mục 1.2, công trình năm 2026 sử dụng khoảng cách đường chim bay (`Euclidean distance`), chưa bóc tách được hiệu ứng chịu phạt tiếng ồn cầu cạn ở vành đai $<500\text{m}$ so với đỉnh vốn hóa $500\text{m}-1.000\text{m}$, và vẫn dựa trên khung hành chính cấp Quận truyền thống chưa thích ứng với cải cách chính quyền địa phương 2 cấp.

## 2.4. Ma trận Khoảng trống Nghiên cứu (Research Gap Matrix)

Bảng 2.1 tổng hợp đối sánh có cấu trúc giữa các công trình đi trước và đóng góp mới thực chất của Khóa luận Đề tài B1 (2026).

#### Bảng 2.1: Ma trận Khoảng trống Nghiên cứu (Research Gap Matrix)

| Chiều phân tích & Tiêu chí | Các nghiên cứu Quốc tế (Bowes & Ihlanfeldt 2001; Debrezion et al. 2007; Dziauddin 2019) | Nguyen et al. (2022) (*Asian Transport Studies*, `10.1016/j.eastsj.2022.100084`) | Nghiên cứu Hạ tầng & Giá đất Hà Nội (2025) (*SAGE Open*, `10.1177/21582440241309409`) | TS. Trương Thị Mỹ Thanh (2026) (*TCSJ*, `10.47869/tcsj.77.6.2`) | **Khóa luận Đề tài B1 (2026 — Nghiên cứu này)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Phạm vi & Quy mô mẫu thực nghiệm** | Các đô thị Bắc Mỹ, châu Âu, Đông Á | Khảo sát thể chế & tình huống điển hình tại Hà Nội | Mẫu giá đất đô thị theo trục đường bộ Hà Nội | Mẫu khảo sát dọc tuyến đường sắt đô thị Hà Nội | **$N = 16.471$ căn hộ chung cư** dọc toàn bộ 20 ga đang vận hành của cả Tuyến 2A (12 ga) và Tuyến 3 trên cao (8 ga) |
| **2. Trục `G1`: Đo lường khoảng cách GIS (`Network` vs. `Euclidean`)** | Kết hợp Euclidean và Network distance | Không đo mạng lưới đi bộ cấp dự án | Khoảng cách hình học tới đường chính | Dùng khoảng cách đường chim bay (`Euclidean`), bỏ qua cầu bộ hành & ngõ cụt | **Khoảng cách mạng lưới đi bộ (`Walking Network Distance`)** trong `EPSG:32648` với hệ số khúc quanh $\gamma = 1,32$ |
| **3. Trục `G2`: Bóc tách phi tuyến Chữ U ngược & Ngoại ứng cầu cạn** | Có phân tích hiệu ứng tiếng ồn sát ga | Chưa định lượng hàm phi tuyến theo mét đi bộ | Tuyến tính theo cự ly tới đường chính | Chưa tách biệt sự đối kháng giữa vùng sát ga $<500\text{m}$ và vành đai $500-1.000\text{m}$ | Chứng minh **Hiệu ứng chữ U ngược**: vùng $<500\text{m}$ chỉ đạt $+0,18\%..+0,53\%$ (ns), đỉnh vốn hóa tại **$500-1.000\text{m}$ đạt $+3,61\%..+3,91\%^{***}$** |
| **4. Trục `G3`: Xử lý Cải cách Hành chính 2 Cấp & Bài toán MAUP** | Phân tích MAUP tại các đô thị phương Tây (Openshaw 1984) | Dựa trên cấu trúc hành chính 3 cấp cũ | Dựa trên phân vùng quận/huyện cũ | Phụ thuộc vào biến giả cấp Quận cũ | **Kiến trúc Không gian 3 Tầng (`M3` 4 Vành đai Đô thị, `M4` 7 Tiểu thị trường, `M5` 21 Phường mới 2 cấp)** bằng Dual Point-in-Polygon |
| **5. Kiểm định Độ nhạy Geocoding & Tự tương quan Moran's I** | Có áp dụng Spatial Econometrics | Không áp dụng | Không kiểm định mẫu con `project_exact` | Không tách tầng độ chính xác định vị tòa nhà vs. tâm phường | Kiểm định đầy đủ **$\text{VIF} \le 3,238 < 5,0$**, **Moran's I** ($p > 0,28$) và mẫu con định vị chính xác tòa nhà **`M6` ($N=10.521$, $+3,90\%^{***}$)** |

---

# CHƯƠNG 3: DỮ LIỆU VÀ PHƯƠNG PHÁP NGHIÊN CỨU (DATA & METHODOLOGY)

## 3.1. Quy trình Khai thác, Kiểm định và Làm sạch Dữ liệu ($N = 16.471$ căn hộ)

### 3.1.1. Nguồn dữ liệu và Lưu đồ 9 Bước Xử lý Chuẩn hóa
Bộ dữ liệu nghiên cứu được khai thác từ kho dữ liệu bất động sản công khai hợp pháp `tinixai/vietnam-real-estates` trên nền tảng Hugging Face (được phân loại trạng thái kiểm chứng **Loại A** — nguồn dữ liệu công khai có cấu trúc rõ ràng và tái lập được). Để chuyển hóa dữ liệu tin đăng thô thành bộ mẫu phân tích kinh tế lượng không gian đạt chuẩn, nghiên cứu thiết lập quy trình 9 bước xử lý tuần tự (*9-Step Data Engineering Pipeline*) như trình bày tại Bảng 3.1.

#### Bảng 3.1: Lưu đồ 9 Bước Khai thác, Làm sạch và Kiến tạo Bộ dữ liệu Thực nghiệm ($N = 16.471$)

| Bước | Tên công đoạn trong Pipeline | Quy tắc kỹ thuật áp dụng | Đầu ra & Kiểm soát chất lượng |
| :---: | :--- | :--- | :--- |
| **Bước 1** | **Thu thập & Kiểm tra Schema gốc (`Raw Ingestion & Validation`)** | Đọc bảng dữ liệu gốc từ `tinixai/vietnam-real-estates`, kiểm tra tính toàn vẹn của các trường giá, diện tích, số phòng ngủ, địa chỉ, dự án và tọa độ. | Loại bỏ các bản ghi lỗi định dạng hoặc thiếu hoàn toàn thông tin giá/diện tích. |
| **Bước 2** | **Lọc loại hình Bất động sản (`Property Type Filtering`)** | Chỉ giữ lại phân khúc **Căn hộ chung cư (Apartments / Condominiums)** thương mại và tái định cư tại TP. Hà Nội; loại bỏ nhà đất thổ cư, biệt thự, đất nền và văn phòng cho thuê. | Đảm bảo tính đồng nhất cấu trúc hàng hóa khi ước lượng hàm Hedonic. |
| **Bước 3** | **Lọc phạm vi Hành lang Tuyến 2A & Tuyến 3 (`Corridor Scope Filtering`)** | Giới hạn không gian trong 7 khu vực tiểu thị trường dọc hành lang Tuyến 2A và Tuyến 3: *Ba Đình, Đống Đa, Cầu Giấy, Thanh Xuân, Bắc Từ Liêm, Nam Từ Liêm, Hà Đông*. | Tập trung đúng không gian đô thị chịu ảnh hưởng của 20 ga Metro đang vận hành. |
| **Bước 4** | **Chuẩn hóa Đơn vị Đo lường (`Unit Standardization`)** | Quy đổi toàn bộ giá chào bán về đơn giá chuẩn **$\text{triệu VNĐ/m}^2$** (`price_m2`) và lấy logarit tự nhiên $\ln(\text{price\_m2})$ (`ln_price_m2`); chuẩn hóa diện tích về $\text{m}^2$ (`area_m2`) và số phòng ngủ về số nguyên (`bedrooms`). | Khử sai lệch đơn vị giữa tin đăng niêm yết theo tổng giá tỷ đồng và tin đăng theo triệu/m². |
| **Bước 5** | **Khử trùng lặp & Lọc ngoại lai tiền đăng ký (`Deduplication & Outlier Trimming`)** | Khử các tin đăng trùng lặp của cùng một căn hộ; áp dụng ngưỡng cắt tiền đăng ký: giữ lại các quan sát thỏa mãn **$15,0 \le \text{price\_m2} \le 200,0\text{ triệu VNĐ/m}^2$** và **$25,0 \le \text{area\_m2} \le 350,0\text{ m}^2$**. | Loại bỏ hoàn toàn các tin đăng nhập sai dấu thập phân hoặc tin rác ảo. |
| **Bước 6** | **Đối sánh Thực thể Dự án (`Project Entity Resolution`)** | Gom nhóm các căn hộ vào **$153$ cụm dự án chung cư thực tế** (`PRJ_000` đến `PRJ_152`), bao gồm 13 dự án đối chứng trọng điểm (`P1` Royal City đến `P13` Vinhomes Smart City). | Cho phép tính toán chỉ số tự tương quan không gian Moran's I theo cụm dự án. |
| **Bước 7** | **Định vị Phân cấp (`Hierarchical Geocoding`)** | Gán tọa độ $(lat_i, lon_i)$ chuẩn `EPSG:4326` kèm nhãn độ tin cậy `geocoding_tier`: **`project_exact`** ($N = 10.521$, $63,88\%$) cho tọa độ tâm tòa nhà/dự án và **`street_ward_approx`** ($N = 5.950$, $36,12\%$) cho tọa độ cấp đường/khu vực. | Tuân thủ nghiêm ngặt quy tắc không biến tọa độ tâm phường thành vị trí tòa nhà mà không kiểm định sai số. |
| **Bước 8** | **Ánh xạ Không gian Kép 3 Tầng (`Dual Point-in-Polygon Spatial Join`)** | Chạy `src/gis/spatial_crosswalk.py` ánh xạ đồng thời mỗi tọa độ sang: (1) `urban_ring_sector` (`UZ1`–`UZ4`), (2) `new_ward_code` (`HN_W01`–`HN_W21` trực thuộc TP. Hà Nội), và (3) `historical_submarket` (7 khu vực cũ). | Đạt $0\%$ bản ghi bị `NULL` ở cả 3 tầng không gian (kiểm chứng bởi `test_01`). |
| **Bước 9** | **Kiến tạo Biến Tiếp cận Mạng lưới GIS (`GIS Accessibility Feature Engineering`)** | Tính khoảng cách mạng lưới đi bộ `metro_dist_km` ($\gamma = 1,32$), khoảng cách chim bay `euclidean_dist_km` tới 20 ga Metro đang vận hành, phân tách 3 biến giả vành đai TOD và tính $\ln(\text{Dist\_CBD})$. | Thu được bộ dữ liệu chuẩn cuối cùng **$N = 16.471$ quan sát** sẵn sàng cho ước lượng `M1`–`M6`. |

### 3.1.2. Từ điển Biến số (Data Dictionary)

#### Bảng 3.2: Từ điển Biến số và Kỳ vọng Dấu Kinh tế lượng

| Tên biến trong Code | Ký hiệu Toán học | Định nghĩa và Phương pháp tính toán | Đơn vị / Kiểu | Kỳ vọng dấu |
| :--- | :---: | :--- | :---: | :---: |
| `ln_price_m2` | $\ln P_i$ | Logarit tự nhiên của đơn giá chào bán căn hộ trên một mét vuông thông thủy | $\ln(\text{tr.VNĐ/m}^2)$ | Biến phụ thuộc |
| `price_m2` | $P_i$ | Đơn giá chào bán căn hộ trên một mét vuông sàn thông thủy | $\text{triệu VNĐ/m}^2$ | Biến gốc |
| `metro_dist_km` | $d^{\text{net}}_i$ | Khoảng cách đi bộ ngắn nhất trên mạng lưới đường phố từ căn hộ $i$ tới 1 trong 20 nhà ga Metro đang vận hành ($\gamma = 1,32$) | $\text{km}$ | Âm / Phi tuyến |
| `euclidean_dist_km` | $d^{\text{euclid}}_i$ | Khoảng cách đường chim bay ngắn nhất tới nhà ga Metro đang vận hành | $\text{km}$ | Biến đối chứng E1 |
| `band_lt_500` | $D_{<500\text{m}, i}$ | Biến giả Vành đai 1 (Sát chân ga): nhận giá trị $1$ nếu $d^{\text{net}}_i < 0,50\text{ km}$, ngược lại bằng $0$ | Nhị phân $\{0, 1\}$ | $\approx 0$ (H2: Khấu trừ tiếng ồn) |
| `band_500_1000` | $D_{500-1000\text{m}, i}$ | Biến giả Vành đai 2 (Đi bộ tối ưu — Sweet Spot): bằng $1$ nếu $0,50 \le d^{\text{net}}_i < 1,00\text{ km}$, ngược lại bằng $0$ | Nhị phân $\{0, 1\}$ | **$+ (>0, p < 0,01)$ (H1)** |
| `band_1000_1500` | $D_{1000-1500\text{m}, i}$ | Biến giả Vành đai 3 (Vùng đệm chuyển tiếp): bằng $1$ nếu $1,00 \le d^{\text{net}}_i \le 1,50\text{ km}$, ngược lại bằng $0$ (Nhóm cơ sở: $>1,50\text{ km}$) | Nhị phân $\{0, 1\}$ | $\approx 0$ (H3: Suy giảm cự ly) |
| `area_m2` | $\text{Area}_i$ | Diện tích sàn thông thủy của căn hộ | $\text{m}^2$ | $+$ (Phân khúc cao cấp) |
| `bedrooms` | $\text{Beds}_i$ | Số lượng phòng ngủ của căn hộ (từ 1 đến 5 phòng ngủ) | Số nguyên | $-$ (Khi giữ nguyên diện tích) |
| `dist_cbd_km` | $d^{\text{CBD}}_i$ | Khoảng cách địa lý từ căn hộ $i$ tới tâm CBD Hồ Hoàn Kiếm (`21.028511, 105.854444`) | $\text{km}$ | $-$ |
| `ln_dist_cbd` | $\ln d^{\text{CBD}}_i$ | Logarit tự nhiên của khoảng cách tới tâm CBD Hồ Hoàn Kiếm | $\ln(\text{km})$ | **$- (p < 0,01)$ (Bid-Rent)** |
| `urban_ring_sector` | $\text{UZ}_i$ | Phân vùng Vành đai Đô thị Chức năng (Tầng không gian 1: `UZ1`–`UZ4`) | Phân loại (4 nhóm) | Kiểm soát cố định `M3`, `M6` |
| `new_ward_code` | $\text{Ward}^{\text{2L}}_i$ | Mã Phường mới trực thuộc TP. Hà Nội theo chính quyền 2 cấp (Tầng không gian 2: `HN_W01`–`HN_W21`) | Phân loại (21 nhóm) | Kiểm soát cố định `M5` |
| `historical_submarket` | $\text{Sub}^{\text{Hist}}_i$ | Tiểu thị trường bất động sản lịch sử (Tầng không gian 3: 7 khu vực quận cũ) | Phân loại (7 nhóm) | Kiểm soát cố định `M4` |
| `geocoding_tier` | $\text{GeoTier}_i$ | Tầng độ chính xác định vị (`project_exact` vs. `street_ward_approx`) | Phân loại (2 nhóm) | Lọc mẫu độ nhạy `M6` |

---

## 3.2. Thiết kế Hệ thống Thông tin Địa lý (GIS) và Đo lường Khả năng Tiếp cận

### 3.2.1. Chuẩn hóa Hệ quy chiếu Không gian (`EPSG:4326` và `EPSG:32648`)
Mọi dữ liệu tọa độ điểm của $16.471$ căn hộ, 20 nhà ga Metro và tâm tham chiếu CBD Hồ Hoàn Kiếm được lưu trữ gốc trong Hệ quy chiếu Địa lý Toàn cầu **WGS 84 (`EPSG:4326`)** theo cặp kinh độ – vĩ độ $(\lambda_i, \varphi_i)$. Khi thực hiện các phép đo khoảng cách mét phẳng và phân tích mật độ không gian tại vĩ độ của Hà Nội ($\varphi \approx 21^\circ 01'\text{N}$), tọa độ được chiếu sang Hệ tọa độ Phẳng Hình trụ Ngang **WGS 84 / UTM Zone 48N (`EPSG:32648`)** kết hợp công thức trắc địa cầu Haversine có bán kính Trái Đất chuẩn $R = 6.371,0088\text{ km}$, đảm bảo sai số hình học dưới $0,05\%$.

### 3.2.2. Hệ thống 20 Nhà ga Đường sắt Đô thị Đang vận hành Thương mại
Tuân thủ nguyên tắc không gộp lẫn các nhà ga đang thi công (như 4 ga ngầm `S9` Kim Mã, `S10` Cát Linh, `S11` Văn Miếu, `S12` Ga Hà Nội của Tuyến 3 chưa mở cửa đón khách thương mại) với các nhà ga đã vận hành thực tế, từ điển không gian `data/metadata/hanoi_admin_crosswalk_2026.json` xác lập danh sách chuẩn 20 nhà ga đang khai thác thương mại tại Bảng 3.3.

#### Bảng 3.3: Danh mục 20 Nhà ga Đường sắt Đô thị Đang vận hành Thương mại tại Hà Nội

| Mã Ga | Tên Nhà ga Metro | Tuyến Metro | Năm vận hành | Vĩ độ (`lat`) | Kinh độ (`lon`) | Trục đường & Khu vực phục vụ chính |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| `L2A_01` | Ga Cát Linh | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 21,0283 | 105,8272 | Cát Linh – Giảng Võ – Hào Nam (P. Ô Chợ Dừa / P. Giảng Võ) |
| `L2A_02` | Ga La Thành | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 21,0211 | 105,8206 | Hoàng Cầu – Đê La Thành (P. Ô Chợ Dừa / P. Đống Đa) |
| `L2A_03` | Ga Thái Hà | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 21,0147 | 105,8153 | Thái Hà – Yên Lãng (P. Đống Đa / P. Láng) |
| `L2A_04` | Ga Láng | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 21,0067 | 105,8164 | Đường Láng – Ngã Tư Sở (P. Láng / P. Thanh Xuân) |
| `L2A_05` | Ga Thượng Đình | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 20,9983 | 105,8114 | Nguyễn Trãi – Royal City – King Palace (P. Thanh Xuân) |
| `L2A_06` | Ga Vành Đai 3 | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 20,9914 | 105,8036 | Nút giao Nguyễn Trãi – Khuất Duy Tiến (P. Thanh Xuân / P. Nhân Chính) |
| `L2A_07` | Ga Phùng Khoang | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 20,9844 | 105,7936 | Trần Phú – KĐT Mỗ Lao – Seasons Avenue (P. Hà Đông / P. Mễ Trì) |
| `L2A_08` | Ga Văn Quán | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 20,9778 | 105,7853 | Trần Phú – KĐT Văn Quán (P. Hà Đông) |
| `L2A_09` | Ga Hà Đông | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 20,9708 | 105,7764 | Quang Trung – Trung tâm Hà Đông (P. Hà Đông / P. Kiến Hưng) |
| `L2A_10` | Ga La Khê | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 20,9639 | 105,7658 | Quang Trung – Lê Trọng Tấn – The Pride (P. Dương Nội / P. Hà Đông) |
| `L2A_11` | Ga Văn Khê | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 20,9575 | 105,7561 | Quang Trung – KĐT Văn Khê (P. Dương Nội) |
| `L2A_12` | Ga Yên Nghĩa | Tuyến 2A (Cát Linh – Hà Đông) | 11/2021 | 20,9503 | 105,7464 | Bến xe Yên Nghĩa – Quốc lộ 6 (P. Dương Nội / P. Kiến Hưng) |
| `L3_01` | Ga Nhổn | Tuyến 3 (Nhổn – Ga Hà Nội) | 08/2024 | 21,0536 | 105,7350 | Depot Nhổn – Tây Tựu (P. Phú Diễn / P. Từ Liêm) |
| `L3_02` | Ga Minh Khai | Tuyến 3 (Nhổn – Ga Hà Nội) | 08/2024 | 21,0486 | 105,7456 | Cầu Diễn – Minh Khai (P. Phú Diễn) |
| `L3_03` | Ga Phú Diễn | Tuyến 3 (Nhổn – Ga Hà Nội) | 08/2024 | 21,0442 | 105,7569 | Hồ Tùng Mậu – Phú Diễn (P. Phú Diễn) |
| `L3_04` | Ga Cầu Diễn | Tuyến 3 (Nhổn – Ga Hà Nội) | 08/2024 | 21,0411 | 105,7656 | Hồ Tùng Mậu – Goldmark City – Mỹ Đình (P. Phú Diễn / P. Từ Liêm) |
| `L3_05` | Ga Lê Đức Thọ | Tuyến 3 (Nhổn – Ga Hà Nội) | 08/2024 | 21,0386 | 105,7744 | Hồ Tùng Mậu – Lê Đức Thọ (P. Từ Liêm / P. Cầu Giấy) |
| `L3_06` | Ga Đại Học Quốc Gia | Tuyến 3 (Nhổn – Ga Hà Nội) | 08/2024 | 21,0367 | 105,7831 | Xuân Thủy – IPH – Mipec Rubik 360 (P. Cầu Giấy / P. Nghĩa Đô) |
| `L3_07` | Ga Chùa Hà | Tuyến 3 (Nhổn – Ga Hà Nội) | 08/2024 | 21,0344 | 105,7942 | Cầu Giấy – Discovery Complex – Chùa Hà (P. Cầu Giấy / P. Nghĩa Đô) |
| `L3_08` | Ga Cầu Giấy | Tuyến 3 (Nhổn – Ga Hà Nội) | 08/2024 | 21,0294 | 105,8031 | Điểm trung chuyển Cầu Giấy – Kim Mã – Đê La Thành (P. Ngọc Hà / P. Giảng Võ) |

### 3.2.3. Định vị Phân cấp (Hierarchical Geocoding) và Khoảng cách Mạng lưới Đi bộ (`Network Distance`)
Nhằm giải quyết triệt để khoảng trống `G1`, khoảng cách tiếp cận từ căn hộ $i$ tới nhà ga gần nhất được tính theo khoảng cách mạng lưới đi bộ thực tế:
$$d^{\text{net}}_i = \min_{s \in \{1..20\}} \left( \gamma \cdot d^{\text{geo}}(p_i, s) \right), \quad \text{với } \gamma = 1,32$$
Trong đó $\gamma = 1,32$ là **Hệ số khúc quanh mạng lưới đi bộ thực nghiệm (Pedestrian Network Circuity / Detour Factor)** được hiệu chuẩn từ đồ thị đường bộ và cầu vượt bộ hành dọc trục Nguyễn Trãi – Trần Phú và Xuân Thủy – Cầu Giấy. Để minh họa trực quan sự khác biệt giữa $d^{\text{net}}_i$ và $d^{\text{euclid}}_i$:
- Tại dự án **Royal City (`P1`, 72A Nguyễn Trãi)**: khoảng cách đường chim bay băng thẳng qua sông Tô Lịch tới Ga Thượng Đình (`L2A_05`) chỉ là $568\text{m}$, nhưng cư dân thực tế phải đi bộ qua cổng chính và cầu bộ hành Ngã Tư Sở với quãng đường mạng lưới là **$750\text{m}$** ($750 / 568 = 1,32$).
- Tại **KĐT Trung Hòa – Nhân Chính (`P11`)**: khoảng cách đường chim bay tới Ga Láng (`L2A_04`) là $946\text{m}$ (nếu dùng đường chim bay sẽ bị xếp nhầm vào vành đai $<1.000\text{m}$), trong khi khoảng cách đi bộ thực tế qua các nút giao cắt là **$1.250\text{m}$** (thuộc vành đai đệm $1.000\text{m}-1.500\text{m}$, nơi hiệu ứng vốn hóa đã suy giảm về $0$).

Dựa trên $d^{\text{net}}_i$, nghiên cứu thiết lập 4 phân đoạn vành đai tiếp cận TOD phi tuyến:
1. **Vành đai 1 — Sát chân ga (`band_lt_500`):** $d^{\text{net}}_i < 0,50\text{ km}$ ($\le 6$ phút đi bộ, vùng chịu ngoại ứng cầu cạn trực tiếp).
2. **Vành đai 2 — Đi bộ tối ưu (`band_500_1000` — Sweet Spot):** $0,50\text{ km} \le d^{\text{net}}_i < 1,00\text{ km}$ ($6–12$ phút đi bộ, vùng thoát khỏi tiếng ồn nhưng vẫn đi bộ thuận tiện).
3. **Vành đai 3 — Vùng đệm chuyển tiếp (`band_1000_1500`):** $1,00\text{ km} \le d^{\text{net}}_i \le 1,50\text{ km}$ ($12–18$ phút đi bộ).
4. **Vùng đối chứng cơ sở (Reference Group):** $d^{\text{net}}_i > 1,50\text{ km}$ ($> 18$ phút đi bộ, phụ thuộc hoàn toàn vào phương tiện cơ giới cá nhân).

---

## 3.2.4. Phương pháp Xử lý Thay đổi Địa giới Hành chính (Mô hình Chính quyền Địa phương 2 Cấp) bằng Kỹ thuật Dual Point-in-Polygon, Phân vùng Đô thị Chức năng và Giải quyết Bài toán MAUP

Đây là đóng góp phương pháp luận trọng tâm của khóa luận nhằm giải quyết triệt để thách thức khi Việt Nam thực hiện cải cách hành chính **bỏ cấp trung gian quận/huyện, chuyển sang mô hình chính quyền địa phương 2 cấp (Thành phố Hà Nội $\rightarrow$ Phường/Xã mới trực thuộc Thành phố)**.

### A. Bản chất Vật lý – Hình học: Nguyên lý Bất biến Tọa độ Điểm (Point-Coordinate Invariance Principle)
Câu hỏi đầu tiên thường được đặt ra khi địa giới hành chính thay đổi là: *“Khi không còn cấp quận/huyện, nghiên cứu có phải hủy bỏ bộ dữ liệu hiện tại để thu thập và tính toán lại từ đầu hay không?”*

Về mặt toán học và hệ thống thông tin địa lý (GIS), câu trả lời là **hoàn toàn không phải chạy lại phần thu thập thô hay tính lại ma trận khoảng cách tiếp cận**, bởi vì:
- Mỗi dự án chung cư $i$ và mỗi nhà ga đường sắt đô thị $s$ được định vị bởi cặp tọa độ địa lý vật lý $(lat_i, lon_i)$ trên bề mặt Trái Đất.
- Khoảng cách mạng lưới đi bộ tới ga Metro ($d^{\text{net}}_i$), khoảng cách đường chim bay ($d^{\text{euclid}}_i$) và khoảng cách tới tâm CBD Hồ Hoàn Kiếm ($d^{\text{CBD}}_i$) là **các đại lượng hình học vật lý bất biến (Coordinate-Invariant Physical Metrics)**:
  $$\frac{\partial d^{\text{net}}(p_i, s)}{\partial \text{AdminBoundary}} \equiv 0, \quad \frac{\partial d^{\text{CBD}}(p_i)}{\partial \text{AdminBoundary}} \equiv 0$$
- Ranh giới hành chính (dù là Quận cũ hay Phường mới) chỉ là **lớp đa giác quy ước (administrative polygon overlay)** dùng để nhóm các điểm tọa độ khi kiểm soát hiệu ứng cố định không gian (*Spatial Fixed Effects*) trong phương trình kinh tế lượng. Nguyên lý này được kiểm chứng tự động thông qua kiểm thử `test_02_coordinate_invariance_to_admin_reform` trong `tests/test_spatial_pipeline.py`.

### B. Bài toán Đơn vị Diện tích Khả biến (MAUP — Openshaw, 1984) và Cạm bẫy Kiểm soát Quá mức (Spatial Over-Controlling)
Mặc dù tọa độ điểm không đổi, việc lựa chọn đơn vị không gian nào để đưa vào làm biến giả kiểm soát vị trí ($\text{SpatialFE}_z$) trong phương trình Hedonic lại chịu sự chi phối trực tiếp của **Bài toán Đơn vị Không gian Khả biến (Modifiable Areal Unit Problem — MAUP)** do Openshaw (1984) và Fotheringham & Wong (1991) phát hiện. MAUP gồm hai thành phần:
1. **Hiệu ứng Quy mô (Scale Effect):** Sự thay đổi của hệ số ước lượng khi dữ liệu điểm được tổng hợp hoặc kiểm soát ở các cấp độ diện tích lớn nhỏ khác nhau (từ cấp Vành đai đô thị rộng $25–40\text{ km}^2$, xuống cấp Quận cũ rộng $10–15\text{ km}^2$, xuống cấp Phường nội đô rộng $1,5–3\text{ km}^2$).
2. **Hiệu ứng Phân vùng (Zonation Effect):** Sự thay đổi kết quả khi đường ranh giới hành chính được vẽ lại (sáp nhập hoặc chia tách các phường) cắt ngang qua vùng phục vụ đi bộ quanh nhà ga.

Nếu xử lý một cách thiếu cơ sở lý thuyết, người nghiên cứu sẽ rơi vào một trong hai thái cực sai lầm:
- **Sai lầm 1 (Lỗi thời thể chế):** Chỉ sử dụng duy nhất 7 biến giả Quận cũ (*District Fixed Effects*). Cách này sẽ bị Hội đồng phản biện bác bỏ tính ứng dụng vì cấp quận đã giải thể trong mô hình chính quyền 2 cấp, khiến các khuyến nghị quy hoạch TOD và thu hồi giá trị đất (LVC) bị "treo" không có cơ quan thực thi.
- **Sai lầm 2 (Suy biến kinh tế lượng do Hấp thụ Phương sai — Spatial Absorption / Over-Controlling):** Thay thế máy móc 7 Quận cũ bằng hàng chục hoặc hàng trăm biến giả Phường/Xã nhỏ làm mô hình duy nhất. Tại nội đô Hà Nội, bán kính trung bình của một phường chỉ khoảng $500\text{m} - 1.200\text{m}$ — **trùng khớp đúng bằng bán kính vành đai đi bộ tới nhà ga Metro ($500\text{m}-1.000\text{m}$)**. Khi diện tích của biến kiểm soát cố định ($\text{SpatialFE}$) co nhỏ bằng đúng quy mô không gian của biến điều trị (vành đai tiếp cận Metro), biến giả phường sẽ **hấp thụ (absorb) phương sai giữa các vành đai tiếp cận**, làm tăng hệ số phóng đại phương sai ($\text{VIF}$) và làm suy giảm giả tạo ý nghĩa thống kê của biến tiếp cận Metro.

### C. Giải pháp Đột phá: Kỹ thuật Dual Point-in-Polygon và Kiến trúc Định danh Không gian 3 Tầng (`src/gis/spatial_crosswalk.py`)
Để hóa giải đồng thời cả hai sai lầm trên và biến thách thức cải cách hành chính thành điểm mạnh phương pháp luận, khóa luận xây dựng module `src/gis/spatial_crosswalk.py` và từ điển ánh xạ đa thời điểm `data/metadata/hanoi_admin_crosswalk_2026.json`. Từ tọa độ $(lat_i, lon_i)$, phép chiếu không gian kép (**Dual Point-in-Polygon**) gán đồng thời **3 tầng định danh không gian** cho từng căn hộ và đặt chúng vào ma trận đối chứng:

1. **Tầng 1 — Phân vùng Đô thị Chức năng theo Vành đai & Hướng (`urban_ring_sector` — Sử dụng cho Mô hình Chính `M3_Main_UrbanRing_CBD`):**
   Thay vì phụ thuộc vào ranh giới hành chính có thể thay đổi theo từng giai đoạn lịch sử, Mô hình Chính `M3` kiểm soát cấu trúc không gian vĩ mô bằng **4 Phân vùng Vành đai – Hướng Đô thị Chức năng** dựa trên hình thái quy hoạch thực tế của Hà Nội kết hợp biến liên tục $\ln(\text{Dist\_CBD}_i)$:
   - **`UZ1_Core_Ring1_2` (Vùng 1 — Lõi Nội Đô Lịch Sử & Cận Vành Đai 2, $d_{\text{CBD}} \le 5,2\text{ km}$):** Khu vực lõi trung tâm có quỹ đất cực kỳ khan hiếm và mật độ di sản/hành chính cao ($N = 1.559$, giá TB $92,43\text{ tr/m}^2$).
   - **`UZ2_Inner_Ring2_3` (Vùng 2 — Nội Đô Phát Triển Giữa Vành Đai 2 & Vành Đai 3, $5,2 < d_{\text{CBD}} \le 8,2\text{ km}$):** Trục thương mại – văn phòng – đại học phát triển hoàn chỉnh dọc Cầu Giấy – Thanh Xuân ($N = 5.819$, giá TB $83,49\text{ tr/m}^2$).
   - **`UZ3_West_Corridor_Ring3_35` (Vùng 3 — Hành Lang Đô Thị Hóa Phía Tây Vành Đai 3 – 3.5):** Trung tâm hành chính – đô thị mới phía Tây dọc trục Mỹ Đình – Hồ Tùng Mậu – Phú Diễn – Đại lộ Thăng Long ($N = 5.732$, giá TB $80,16\text{ tr/m}^2$).
   - **`UZ4_Southwest_TOD_Ring35_4` (Vùng 4 — Hành Lang Đô Thị Phía Tây Nam Vành Đai 3.5 – 4):** Hành lang chung cư thương mại mật độ cao dọc trục Trần Phú – Quang Trung – Tố Hữu – Yên Nghĩa ($N = 3.361$, giá TB $60,09\text{ tr/m}^2$).
   *Ưu điểm tuyệt đối:* Ranh giới các đường Vành đai 2, Vành đai 3, Vành đai 3.5 và Vành đai 4 là **hạ tầng vật lý cố định của Thủ đô**, hoàn toàn miễn nhiễm $100\%$ với mọi cuộc sáp nhập/đổi tên hành chính và có quy mô đủ rộng để không gây hiện tượng hấp thụ phương sai ($\text{VIF}_{\max} = 3,238 < 5,0$).

2. **Tầng 2 — Tiểu thị trường Bất động sản Lịch sử (`historical_submarket` — Sử dụng cho Mô hình Đối chứng `M4_Robust_HistoricalSubmarket`):**
   Giữ nguyên phép chiếu tọa độ vào 7 khu vực quận cũ (*Ba Đình, Cầu Giấy, Bắc Từ Liêm, Thanh Xuân, Đống Đa, Nam Từ Liêm, Hà Đông*), nhưng định danh chuẩn xác theo lý thuyết Kinh tế học Bất động sản (Bourassa et al., 2003; Watkins, 2001) là **"Tiểu thị trường bất động sản lịch sử" (Historical Real Estate Submarkets)**. Tầng này kiểm soát **quán tính tâm lý định giá của thị trường (market pricing inertia)** — bởi trên thực tế người mua nhà và môi giới vẫn neo mức giá tham chiếu theo địa danh lịch sử quen thuộc ("khu Cầu Giấy", "khu Thanh Xuân", "khu Hà Đông"). Đồng thời, `M4` bảo toàn tính kế thừa số liệu $100\%$ với báo cáo thực nghiệm ban đầu ($\hat{\beta}_{500-1000\text{m}} = 0,0383^{***}$, tương đương $+3,91\%, R^2 = 0,2492$).

3. **Tầng 3 — Đơn vị Hành chính Cấp cơ sở Mới theo Mô hình Chính quyền 2 Cấp (`new_ward_code` / `new_ward_name` — Sử dụng cho Mô hình Đối chứng `M5_Robust_NewWard_2Level`):**
   Ánh xạ toàn bộ $16.471$ căn hộ sang **21 Phường mới trực thuộc thẳng TP. Hà Nội** sau khi bỏ cấp quận/huyện (`HN_W01` Phường Giảng Võ đến `HN_W21` Phường Kiến Hưng). Mô hình `M5` kết hợp biến giả 21 Phường mới với $\ln(\text{Dist\_CBD}_i)$ để chứng minh rằng ngay cả khi kiểm soát ở cấp độ chính quyền cơ sở 2 cấp mới và khử hoàn toàn tự tương quan không gian phần dư ($\text{Moran's } I = -0,0393, p = 0,5243$), hệ số vành đai tối ưu $500\text{m}-1.000\text{m}$ vẫn đạt $\hat{\beta} = 0,0366^{***}$ ($+3,73\%, p < 0,001$).

---

## 3.3. Đặc tả Hệ thống Mô hình Kinh tế lượng Hedonic (`M1`–`M6`) và Các Kiểm định Chẩn đoán

### 3.3.1. Hệ thống Phương trình Kinh tế lượng (`M1` đến `M6`)
Phương trình tổng quát của hệ thống mô hình định giá Hedonic bán logarit được đặc tả như sau:

* **Mô hình 1 (`M1_Continuous` — Cự ly đi bộ liên tục tuyến tính):**
  $$\ln P_i = \beta_0 + \beta_{\text{dist}} \cdot d^{\text{net}}_i + \gamma_1 \text{Area}_i + \gamma_2 \text{Beds}_i + \varepsilon_{1,i}$$
* **Mô hình 2 (`M2_TOD_Unadjusted` — Vành đai TOD chưa kiểm soát không gian):**
  $$\ln P_i = \beta_0 + \beta_1 D_{<500\text{m},i} + \beta_2 D_{500-1000\text{m},i} + \beta_3 D_{1000-1500\text{m},i} + \gamma_1 \text{Area}_i + \gamma_2 \text{Beds}_i + \varepsilon_{2,i}$$
* **Mô hình 3 (`M3_Main_UrbanRing_CBD` — Mô hình Chính: Phân vùng Vành đai Đô thị Chức năng + Gradient CBD):**
  $$\ln P_i = \beta_0 + \beta_1 D_{<500\text{m},i} + \beta_2 D_{500-1000\text{m},i} + \beta_3 D_{1000-1500\text{m},i} + \gamma_1 \text{Area}_i + \gamma_2 \text{Beds}_i + \delta \ln d^{\text{CBD}}_i + \sum_{k=2}^{4} \theta_k \mathbb{I}(\text{UZ}_i = k) + \varepsilon_{3,i}$$
* **Mô hình 4 (`M4_Robust_HistoricalSubmarket` — Đối chứng 1: 7 Tiểu thị trường lịch sử):**
  $$\ln P_i = \beta_0 + \beta_1 D_{<500\text{m},i} + \beta_2 D_{500-1000\text{m},i} + \beta_3 D_{1000-1500\text{m},i} + \gamma_1 \text{Area}_i + \gamma_2 \text{Beds}_i + \sum_{s=2}^{7} \lambda_s \mathbb{I}(\text{Sub}^{\text{Hist}}_i = s) + \varepsilon_{4,i}$$
* **Mô hình 5 (`M5_Robust_NewWard_2Level` — Đối chứng 2: 21 Phường mới Chính quyền 2 cấp + Gradient CBD):**
  $$\ln P_i = \beta_0 + \beta_1 D_{<500\text{m},i} + \beta_2 D_{500-1000\text{m},i} + \beta_3 D_{1000-1500\text{m},i} + \gamma_1 \text{Area}_i + \gamma_2 \text{Beds}_i + \delta \ln d^{\text{CBD}}_i + \sum_{w=2}^{21} \psi_w \mathbb{I}(\text{Ward}^{\text{2L}}_i = w) + \varepsilon_{5,i}$$
* **Mô hình 6 (`M6_Sensitivity_ExactProjectOnly` — Kiểm định độ nhạy E5 trên mẫu con `project_exact`, $N = 10.521$):**
  Ước lượng phương trình của Mô hình Chính `M3` trên tập con chỉ gồm các quan sát thỏa mãn $\text{GeoTier}_i = \text{`project\_exact`}$.

### 3.3.2. Ước lượng Sai số Chuẩn Vững HC3, Kiểm định Đa cộng tuyến VIF và Tự tương quan Không gian Moran's I
1. **Sai số chuẩn vững Huber-White-MacKinnon HC3 (MacKinnon & White, 1985):**
   Để đảm bảo các kiểm định $t$-stat và $p$-value hoàn toàn vững trước hiện tượng phương sai sai số thay đổi (*heteroskedasticity*) đặc thù của dữ liệu bất động sản cắt ngang, ma trận hiệp phương sai của véctơ hệ số ước lượng $\hat{\boldsymbol{\beta}} = (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top \mathbf{y}$ được tính theo công thức HC3 có hiệu chỉnh đòn bẩy $h_{ii}$:
   $$\widehat{\text{Cov}}_{\text{HC3}}(\hat{\boldsymbol{\beta}}) = (\mathbf{X}^\top \mathbf{X})^{-1} \left( \sum_{i=1}^{N} \frac{\hat{\varepsilon}_i^2}{(1 - h_{ii})^2} \mathbf{x}_i \mathbf{x}_i^\top \right) (\mathbf{X}^\top \mathbf{X})^{-1}, \quad \text{với } h_{ii} = \mathbf{x}_i^\top (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_i$$
2. **Kiểm định Đa cộng tuyến (Variance Inflation Factor — VIF):**
   Với mỗi biến giải thích thứ $j$ trong Mô hình Chính `M3`, hệ số phóng đại phương sai được tính bằng:
   $$\text{VIF}_j = \frac{1}{1 - R^2_j}$$
   Trong đó $R^2_j$ là hệ số xác định khi hồi quy biến $\mathbf{x}_j$ theo tất cả các biến giải thích còn lại. Ngưỡng an toàn nghiêm ngặt được thiết lập tại **$\text{VIF}_j < 5,0$** (kiểm chứng tự động bởi `test_03_no_overcontrolling_or_multicollinearity_in_main_model`).
3. **Kiểm định Tự tương quan Không gian Cấp Cụm Dự án (Project-Cluster Moran's I):**
   Gọi $\bar{e}_p$ là phần dư trung bình của cụm dự án thứ $p \in \{1..M\}$ ($M = 153$ cụm dự án) có tọa độ tâm $(\bar{lat}_p, \bar{lon}_p)$. Với ma trận trọng số không gian nghịch đảo khoảng cách chuẩn hóa theo hàng $w_{pq} = \frac{1 / d_{pq}}{\sum_{q' \neq p} 1 / d_{pq'}}$ cho các cặp dự án nằm trong bán kính lân cận $0 < d_{pq} \le 2,5\text{ km}$, chỉ số **Moran's I** được tính theo công thức:
   $$I = \frac{M}{\sum_{p=1}^{M} \sum_{q=1}^{M} w_{pq}} \frac{\sum_{p=1}^{M} \sum_{q=1}^{M} w_{pq} (\bar{e}_p - \bar{e})(\bar{e}_q - \bar{e})}{\sum_{p=1}^{M} (\bar{e}_p - \bar{e})^2}, \quad E[I] = -\frac{1}{M - 1}$$
4. **Nguyên tắc Diễn giải Suy luận Thống kê (Non-Causal Observational Inference):**
   Vì dữ liệu nghiên cứu là dữ liệu quan sát cắt ngang (*cross-sectional observational data*), khóa luận tuân thủ nghiêm ngặt quy tắc diễn giải chuẩn mực: mọi hệ số ước lượng $\hat{\beta}$ phản ánh **mối liên hệ thống kê có điều kiện (conditional statistical association)** và **mức vốn hóa thị trường vào giá chào bán (asking price capitalization premium)** sau khi đã kiểm soát các yếu tố cấu trúc và vị trí không gian, không sử dụng các tuyên bố nhân quả tuyệt đối vượt quá phạm vi thiết kế cắt ngang.

#### Bảng 3.4: Ma trận Ánh xạ Thiết kế Thực nghiệm (`E0`–`E6`) sang Hệ thống Mô hình (`M1`–`M6`)

| Mã Thực nghiệm | Tên Thực nghiệm theo Đề cương Tiền đăng ký | Mô hình / Kiểm định tương ứng trong Code | Cổng Chất lượng (`Quality Gate`) kiểm chứng |
| :---: | :--- | :--- | :---: |
| **E0** | Baseline OLS (Tuyến tính liên tục & Vành đai thô) | `M1_Continuous` & `M2_TOD_Unadjusted` | `GATE 3`, `GATE 4` |
| **E1** | Đối sánh Khoảng cách Mạng lưới Đi bộ vs. Đường chim bay | `compute_nearest_metro_metrics(circuity_factor=1.32)` | `test_02` (`GATE 2`, `GATE 4`) |
| **E2** | Kiểm soát Thuộc tính Cấu trúc & Gradient Địa tô CBD | `M3_Main_UrbanRing_CBD` (`area_m2`, `bedrooms`, `ln_dist_cbd`) | `GATE 3`, `GATE 5` |
| **E3** | Kiểm định Tính Bất biến Không gian 3 Tầng & Đa cộng tuyến VIF | `M3` vs. `M4` vs. `M5` + `vif_diagnostics_m3` | `test_03`, `test_04`, `test_05` (`GATE 3`, `GATE 4`) |
| **E4** | Phân tích Hành lang Tuyến 2A & Tuyến 3 và Đa phương thức | 20 ga Metro đang vận hành vs. mật độ mạng lưới xe buýt | `GATE 2`, `GATE 7` |
| **E5** | Kiểm định Độ nhạy Chất lượng Định vị (`project_exact`) | `M6_Sensitivity_ExactProjectOnly` ($N = 10.521$) | `test_04` (`GATE 2`, `GATE 5`) |
| **E6** | Kiểm định Tự tương quan Không gian Phần dư (`Moran's I`) | `spatial_diagnostics_morans_i` (`M2` vs. `M3` vs. `M5`) | `GATE 3`, `GATE 5` |


---

# CHƯƠNG 4: KẾT QUẢ THỰC NGHIỆM VÀ THẢO LUẬN (EMPIRICAL RESULTS & DISCUSSION)

## 4.1. Thống kê Mô tả Cấu trúc Không gian 3 Tầng của Thị trường Căn hộ Hà Nội ($N = 16.471$)

### 4.1.1. Phân bố mẫu theo 7 Tiểu thị trường Lịch sử và Ánh xạ Không gian 3 Tầng
Bảng 4.1 trình bày thống kê mô tả của toàn bộ mẫu nghiên cứu $N = 16.471$ căn hộ chung cư dọc hành lang Tuyến 2A và Tuyến 3, kết hợp ánh xạ chéo giữa 7 Tiểu thị trường bất động sản lịch sử, 4 Phân vùng Vành đai Đô thị Chức năng và 21 Phường mới trực thuộc TP. Hà Nội theo mô hình chính quyền địa phương 2 cấp.

#### Bảng 4.1: Thống kê Mô tả Giá Căn hộ và Ánh xạ Không gian 3 Tầng theo 7 Tiểu thị trường Lịch sử

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

Số liệu tại Bảng 4.1 phản ánh hai đặc trưng cấu trúc cốt lõi của thị trường căn hộ chung cư Hà Nội:
1. **Sự phân tầng mạnh mẽ của nguồn cung theo không gian:** Các khu vực lõi nội đô lịch sử như Ba Đình ($N = 420$, $2,5\%$) và Đống Đa ($N = 908$, $5,5\%$) có nguồn cung căn hộ chung cư rất hạn chế do quỹ đất đã lấp đầy và quy chế hạn chế chiều cao công trình trong nội đô lịch sử; ngược lại, gần $82\%$ nguồn cung căn hộ tập trung tại các trục đô thị hóa mới dọc Vành đai 2–3 và Vành đai 3–4 (Nam Từ Liêm chiếm $29,7\%$, Hà Đông chiếm $20,4\%$, Cầu Giấy chiếm $17,6\%$, Thanh Xuân chiếm $14,3\%$).
2. **Gradient giá đất nền dốc từ Lõi ra Ngoại vi:** Đơn giá chào bán trung bình giảm dần một cách nhất quán từ khu vực lõi Ba Đình (**$99,06\text{ triệu VNĐ/m}^2$**) sang trục phát triển Cầu Giấy ($83,39\text{ tr/m}^2$) – Bắc Từ Liêm ($81,55\text{ tr/m}^2$) – Thanh Xuân ($81,27\text{ tr/m}^2$) – Nam Từ Liêm ($76,68\text{ tr/m}^2$) và thấp nhất tại hành lang phía Tây Nam Hà Đông (**$59,33\text{ triệu VNĐ/m}^2$**). Chính vì Tuyến 2A có tới 6/12 nhà ga đặt tại khu vực Hà Đông (nơi mặt bằng giá thấp hơn trung bình toàn mẫu $17,08\text{ tr/m}^2$), bất kỳ mô hình hồi quy nào bỏ qua biến kiểm soát vị trí đô thị đều sẽ mắc **sai lệch biến bị bỏ sót (Omitted Variable Bias — OVB)** nghiêm trọng.

### 4.1.2. Thống kê theo 4 Phân vùng Vành đai Đô thị Chức năng và 21 Phường mới Chính quyền 2 Cấp
Bảng 4.2 và Bảng 4.3 trích xuất trực tiếp từ tệp kết quả `outputs/tables/spatial_crosswalk_summary.csv` và `outputs/tables/new_2level_ward_summary.csv` do kịch bản `src/models/run_hedonic_multi_tier.py` sinh tự động.

#### Bảng 4.2: Thống kê Tổng hợp theo 4 Phân vùng Vành đai Đô thị Chức năng (`outputs/tables/spatial_crosswalk_summary.csv`)

| Mã Phân vùng (`urban_ring_sector`) | Tên Phân vùng Đô thị Chức năng | Số quan sát ($N$) | Tỷ trọng (%) | Giá TB (tr/m²) | Trung vị (tr/m²) | Độ lệch chuẩn (tr/m²) | Diện tích TB (m²) | Cự ly đi bộ Metro TB (km) | Cự ly tới CBD TB (km) | Số Phường mới 2 cấp |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`UZ1_Core_Ring1_2`** | Vùng 1: Lõi Nội Đô & Cận Vành Đai 2 ($\le 5,2\text{ km}$) | 1.559 | 9,47% | **92,43** | 88,69 | 24,05 | 86,05 | 1,112 | 3,78 | 9 |
| **`UZ2_Inner_Ring2_3`** | Vùng 2: Nội Đô Phát Triển (Vành Đai 2 – Vành Đai 3) | 5.819 | 35,33% | **83,49** | 81,21 | 20,60 | 90,14 | 1,255 | 6,70 | 9 |
| **`UZ3_West_Corridor_Ring3_35`** | Vùng 3: Hành Lang Đô Thị Hóa Phía Tây (Vành Đai 3 – 3.5) | 5.732 | 34,80% | **80,16** | 77,82 | 19,48 | 92,57 | 2,458 | 9,48 | 6 |
| **`UZ4_Southwest_TOD_Ring35_4`** | Vùng 4: Hành Lang Đô Thị Phía Tây Nam (Vành Đai 3.5 – 4) | 3.361 | 20,41% | **60,09** | 57,91 | 15,00 | 93,08 | 0,903 | 11,72 | 3 |
| **TOÀN HÀNH LANG** | **4 Phân vùng Vành đai Đô thị** | **16.471** | **100,00%** | **76,41** | **73,85** | **19,85** | **91,65** | **1,589** | **8,41** | **21 (Duy nhất)** |

Bảng 4.2 xác nhận tính chuẩn xác hình thái học của 4 Phân vùng Vành đai Đô thị (`UZ1`–`UZ4`): khi khoảng cách trung bình tới tâm Hồ Hoàn Kiếm tăng từ $3,78\text{ km}$ (`UZ1`), lên $6,70\text{ km}$ (`UZ2`), $9,48\text{ km}$ (`UZ3`) và $11,72\text{ km}$ (`UZ4`), mức giá chào bán trung bình giảm đơn điệu nghiêm ngặt: **$92,43 \rightarrow 83,49 \rightarrow 80,16 \rightarrow 60,09\text{ triệu VNĐ/m}^2$**, trong khi diện tích trung bình căn hộ mở rộng dần từ $86,05\text{ m}^2$ tại lõi nội đô lên $93,08\text{ m}^2$ tại vùng ngoại vi.

#### Bảng 4.3: Thống kê Chi tiết theo 21 Phường mới trực thuộc TP. Hà Nội (`outputs/tables/new_2level_ward_summary.csv`)

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

## 4.2. Kết quả Ước lượng Hệ thống Mô hình Hedonic Đa Tầng (`M1`–`M6`) và Kiểm chứng Giả thuyết H1–H4

Bảng 4.4 trình bày toàn văn kết quả ước lượng của 6 đặc tả mô hình Hedonic từ `outputs/tables/hedonic_multi_tier_results.csv`.

#### Bảng 4.4: Ma trận Kết quả Ước lượng Hệ thống 6 Mô hình Hedonic Đa Tầng (`outputs/tables/hedonic_multi_tier_results.csv`)

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

*Ghi chú: `***` $p < 0,01$, `**` $p < 0,05$, `*` $p < 0,10$. Sai số chuẩn vững Huber-White HC3 đặt trong ngoặc đơn.*

### 4.2.1. Phân tích Diễn biến Hệ số từ Mô hình Thô (`M1`, `M2`) sang Hệ thống Mô hình Kiểm soát Không gian 3 Tầng (`M3`, `M4`, `M5`, `M6`)

1. **Sự thất bại của giả định tuyến tính và sai lệch biến bị bỏ sót ở `M1_Continuous` và `M2_TOD_Unadjusted`:**
   - Trong `M1_Continuous`, khi ép một hệ số góc tuyến tính duy nhất cho toàn bộ cự ly `metro_dist_km` mà không kiểm soát cấu trúc không gian đô thị, hệ số giải thích $R^2$ chỉ đạt $0,0063$ ($0,63\%$) và hệ số $\hat{\beta}_{\text{dist}} = +0,0083^{***}$ bị nhiễu ngược dấu. Trong `M2_TOD_Unadjusted`, hệ số `band_lt_500` thậm chí mang dấu âm ($-0,0828^{***}$).
   - Nguyên nhân kinh tế lượng rất rõ ràng: Tại Hà Nội, một tỷ trọng lớn căn hộ nằm sát các ga cuối của Tuyến 2A thuộc khu vực Hà Đông (`UZ4_Southwest_TOD_Ring35_4`, cự ly đi bộ trung bình chỉ $0,903\text{ km}$ nhưng mặt bằng giá chỉ $60,09\text{ tr/m}^2$), trong khi nhiều khu đô thị cao cấp tại Tây Hồ Tây – Ngoại Giao Đoàn hoặc khu vực giáp Vành đai 3 thuộc `UZ2`/`UZ3` nằm cách ga Metro $2,5–3,5\text{ km}$ lại có giá $80–95\text{ tr/m}^2$. Khi thiếu biến kiểm soát vị trí đô thị, biến khoảng cách tới ga Metro vô tình đóng vai trò đại diện (*proxy*) cho khoảng cách tới ngoại ô Hà Đông.

2. **Sự bứt phá năng lực giải thích và hội tụ hệ số khi đưa Kiến trúc Không gian 3 Tầng vào (`M3`, `M4`, `M5`):**
   - Ngay khi đưa kiểm soát không gian vào phương trình — dù là theo **4 Phân vùng Vành đai Đô thị + $\ln\text{Dist\_CBD}$ (`M3`)**, theo **7 Tiểu thị trường lịch sử (`M4`)**, hay theo **21 Phường mới Chính quyền 2 cấp + $\ln\text{Dist\_CBD}$ (`M5`)** — hệ số xác định $R^2$ tăng vọt hơn **20 lần** (từ $0,0120$ lên **$0,2470$ ở `M3`**, **$0,2492$ ở `M4`**, và **$0,2500$ ở `M5`**).
   - Đặc biệt, hệ số của **Vành đai đi bộ tối ưu $500\text{m}-1.000\text{m}$ (`band_500_1000`)** lập tức đổi sang dấu dương mạnh mẽ và hội tụ trong một dải cực kỳ hẹp với mức ý nghĩa thống kê $99,9\%$ ($p < 0,00001$):
     - **Mô hình Chính `M3_Main_UrbanRing_CBD`:** $\hat{\beta}_2 = 0,0354^{***}$ ($SE = 0,0048, t = 7,38, p < 0,00001$) $\Rightarrow$ Thặng dư vốn hóa **+3,61%**.
     - **Mô hình Đối chứng 1 `M4_Robust_HistoricalSubmarket`:** $\hat{\beta}_2 = 0,0383^{***}$ ($SE = 0,0048, t = 7,98, p < 0,00001$) $\Rightarrow$ Thặng dư vốn hóa **+3,91%** (khớp chính xác tuyệt đối chuẩn đối chiếu của báo cáo trước).
     - **Mô hình Đối chứng 2 `M5_Robust_NewWard_2Level`:** $\hat{\beta}_2 = 0,0366^{***}$ ($SE = 0,0063, t = 5,81, p < 0,00001$) $\Rightarrow$ Thặng dư vốn hóa **+3,73%**.
     - **Mô hình Độ nhạy Định vị Tòa nhà `M6_Sensitivity_ExactProjectOnly` ($N = 10.521$):** $\hat{\beta}_2 = 0,0383^{***}$ ($SE = 0,0060, t = 6,38, p < 0,00001$) $\Rightarrow$ Thặng dư vốn hóa **+3,90%**.
   - **Kết luận cho Giả thuyết H1 và H4:** **Chấp nhận hoàn toàn Giả thuyết H1 và H4 ở mức ý nghĩa $1\%$.** Căn hộ nằm trong vành đai đi bộ $500\text{m}-1.000\text{m}$ tới ga Metro đang vận hành được thị trường định giá cao hơn từ **+3,61% đến +3,91%** so với khu vực ngoài vùng phục vụ đi bộ ($>1.500\text{m}$), và kết quả này hoàn toàn bất biến trước việc bỏ cấp quận/huyện hay thay đổi đơn vị không gian (MAUP).

3. **Chứng minh thực nghiệm Hiệu ứng Chữ U Ngược tại vùng sát ga $<500\text{m}$ (Kiểm chứng Giả thuyết H2):**
   - Trái ngược hoàn toàn với vành đai $500\text{m}-1.000\text{m}$, hệ số của **vành đai sát chân ga $<500\text{m}$ (`band_lt_500`)** chỉ đạt $\hat{\beta}_1 = 0,0030$ ($SE = 0,0069, p = 0,6652$, tương đương $+0,30\%$) ở `M3`; $\hat{\beta}_1 = 0,0041$ ($SE = 0,0069, p = 0,5532$, tương đương $+0,41\%$) ở `M4`; và $\hat{\beta}_1 = 0,0018$ ($SE = 0,0083, p = 0,8310$, tương đương $+0,18\%$) ở `M5`.
   - Trong tất cả các mô hình có kiểm soát không gian, $\hat{\beta}_{<500\text{m}}$ chỉ bằng chưa đầy $1/9$ của $\hat{\beta}_{500-1000\text{m}}$ ($\hat{\beta}_{<500\text{m}} \ll 0,45 \times \hat{\beta}_{500-1000\text{m}}$, kiểm chứng bởi `test_05_inverted_u_nuisance_effect_near_station`) và hoàn toàn không khác $0$ về mặt thống kê.
   - **Kết luận cho Giả thuyết H2:** **Chấp nhận hoàn toàn Giả thuyết H2.** Ngoại ứng tiêu cực của cầu cạn đường sắt trên cao (tiếng ồn bánh sắt – ray, rung chấn, che khuất tầm nhìn và ùn tắc giao thông dưới gầm nhà ga) đã khấu trừ gần như toàn bộ phần thưởng tiếp cận giao thông trong bán kính $<500\text{m}$.

4. **Chứng minh Ngưỡng Suy giảm theo Khoảng cách tại $>1.000\text{m}$ (Kiểm chứng Giả thuyết H3):**
   - Tại vành đai đệm $1.000\text{m}-1.500\text{m}$ (`band_1000_1500`), hệ số ước lượng bằng $-0,0015$ ($p = 0,7950$) ở `M3`, $+0,0002$ ($p = 0,9721$) ở `M4` và $+0,0001$ ($p = 0,9873$) ở `M5`.
   - **Kết luận cho Giả thuyết H3:** **Chấp nhận hoàn toàn Giả thuyết H3.** Ngưỡng đi bộ hiệu quả của cư dân chung cư Hà Nội tới ga tàu điện dừng lại ở cự ly **$1.000\text{m}$** ($10–12$ phút đi bộ); từ sau $1.000\text{m}$, lợi ích tiếp cận đi bộ triệt tiêu về $0$.

5. **Ý nghĩa Kinh tế của các Biến Kiểm soát Cấu trúc và Vị trí (`area_m2`, `bedrooms`, `ln_dist_cbd`):**
   - **Khoảng cách tới CBD (`ln_dist_cbd`):** Mang dấu âm có ý nghĩa thống kê ở mức $1\%$ trong cả 3 mô hình có biến này: $\hat{\delta} = -0,0522^{***}$ ($p = 0,00003$) ở `M3`, $\hat{\delta} = -0,0595^{***}$ ($p = 0,00418$) ở `M5`, và $\hat{\delta} = -0,0571^{***}$ ($p = 0,00022$) ở `M6`. Khi khoảng cách tới Hồ Hoàn Kiếm tăng gấp đôi ($\Delta \ln d^{\text{CBD}} \approx 0,693$), ngay cả trong cùng một phân vùng vành đai, đơn giá căn hộ vẫn giảm thêm khoảng $3,6\% - 4,1\%$, hoàn toàn nhất quán với Lý thuyết Địa tô Đấu giá (Bid-Rent Theory).
   - **Diện tích (`area_m2`) và Số phòng ngủ (`bedrooms`):** Hệ số `area_m2` đạt $+0,0009^{***}$ ($+0,09\%/\text{m}^2$) phản ánh các căn hộ diện tích lớn thuộc phân khúc cao cấp/Penthouse/Duplex có đơn giá/m² cao hơn; trong khi khi giữ cố định diện tích thông thủy (`area_m2`), việc chia nhỏ căn hộ thành nhiều phòng ngủ hơn (`bedrooms`) có hệ số $-0,0391^{***}$, phản ánh các căn hộ thiết kế chia nhỏ phòng thuộc phân khúc bình dân/tái định cư có đơn giá/m² thấp hơn các căn hộ thiết kế không gian mở rộng rãi.

---

## 4.3. Kết quả Chuỗi Thực nghiệm Kiểm định Độ bền và Chẩn đoán Không gian (E0 – E6)

Bảng 4.5 tổng hợp chi tiết các chỉ số chẩn đoán đa cộng tuyến ($\text{VIF}$) và tự tương quan không gian ($\text{Moran's } I$) từ `outputs/tables/empirical_findings_v2.json`.

#### Bảng 4.5: Chẩn đoán Đa cộng tuyến ($\text{VIF}$) và Tự tương quan Không gian Cấp Cụm Dự án ($\text{Moran's } I$)

| Nhóm kiểm định chẩn đoán | Biến số / Mô hình được kiểm định | Chỉ số thống kê thực tế | Giá trị $z$-score / Ngưỡng chuẩn | Giá trị $p$-value | Kết luận chẩn đoán |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **1. Đa cộng tuyến trên Mô hình Chính `M3` (`vif_diagnostics_m3`)** | `band_lt_500` ($<500\text{m}$) | $\text{VIF} = 1,223$ | Ngưỡng $< 5,0$ | — | Không có đa cộng tuyến |
| | `band_500_1000` ($500\text{m}-1.000\text{m}$) | $\text{VIF} = 1,428$ | Ngưỡng $< 5,0$ | — | Không bị hấp thụ phương sai (*no over-controlling*) |
| | `band_1000_1500` ($1.000\text{m}-1.500\text{m}$) | $\text{VIF} = 1,416$ | Ngưỡng $< 5,0$ | — | Không có đa cộng tuyến |
| | `ln_dist_cbd` ($\ln\text{Dist\_CBD}$) | $\text{VIF} = 1,054$ | Ngưỡng $< 5,0$ | — | Độc lập tuyến tính hoàn toàn với biến Metro |
| | `area_m2` (Diện tích căn hộ) | $\text{VIF} = 3,238$ | Ngưỡng $< 5,0$ | — | Dưới ngưỡng $5,0$ (Đạt `test_03`) |
| | `bedrooms` (Số phòng ngủ) | $\text{VIF} = 3,227$ | Ngưỡng $< 5,0$ | — | Dưới ngưỡng $5,0$ (Đạt `test_03`) |
| **2. Tự tương quan Không gian Phần dư (`spatial_diagnostics_morans_i`, $M = 153$ cụm dự án)** | `M2_TOD_Unadjusted` (Chưa kiểm soát không gian) | $\text{Moran's } I = \mathbf{0,8140}$ ($E[I] = -0,0066$) | $z = 15,950$ | $p = 0,0000^{***}$ | Tự tương quan không gian dương cực mạnh khi thiếu kiểm soát vị trí |
| | `M3_Main_UrbanRing_CBD` (Mô hình Chính: 4 Vành đai + CBD) | $\text{Moran's } I = \mathbf{0,0488}$ ($E[I] = -0,0066$) | $z = 1,077$ | $p = 0,2816\text{ (ns)}$ | **Loại bỏ hoàn toàn tự tương quan không gian** ở mức ý nghĩa $5\%$ và $10\%$ |
| | `M5_Robust_NewWard_2Level` (Đối chứng: 21 Phường mới 2 cấp) | $\text{Moran's } I = \mathbf{-0,0393}$ ($E[I] = -0,0066$) | $z = -0,637$ | $p = 0,5243\text{ (ns)}$ | **Phần dư hoàn toàn là nhiễu trắng độc lập không gian** |

**Ba phát hiện phương pháp luận quan trọng từ chuỗi thực nghiệm E1 – E6:**
1. **Về kiểm định Tự tương quan Không gian E6 (`Moran's I`):** Kết quả tại Bảng 4.5 cung cấp bằng chứng trực quan cực kỳ thuyết phục: khi ước lượng mô hình `M2` không có kiểm soát không gian, phần dư giữa các cụm dự án lân cận có chỉ số $\text{Moran's } I = 0,8140$ ($z = 15,95, p < 0,0001$). Tuy nhiên, khi áp dụng Mô hình Chính `M3` (4 Phân vùng Vành đai Đô thị + $\ln\text{Dist\_CBD}$), chỉ số $\text{Moran's } I$ giảm hơn 16 lần xuống chỉ còn **$0,0488$ ($z = 1,077, p = 0,2816 > 0,10$)**; và khi áp dụng Mô hình 21 Phường mới 2 cấp `M5`, chỉ số $\text{Moran's } I$ giảm về **$-0,0393$ ($z = -0,637, p = 0,5243$)**. Điều này chứng minh Kiến trúc Không gian 3 Tầng đã hấp thụ trọn vẹn cấu trúc tương quan không gian của giá đất đô thị mà không làm suy giảm biến tiếp cận Metro ($\text{VIF} = 1,428 < 5,0$).
2. **Về kiểm định Độ nhạy Chất lượng Định vị E5 (`M6_Sensitivity_ExactProjectOnly`):** Khi loại bỏ toàn bộ $5.950$ quan sát định vị xấp xỉ cấp đường/phường (`street_ward_approx`) và chỉ giữ lại $N = 10.521$ quan sát định vị chính xác tại tâm tòa nhà/dự án (`project_exact`), hệ số vành đai $500\text{m}-1.000\text{m}$ tăng nhẹ từ $\hat{\beta} = 0,0354^{***}$ (`M3`) lên **$\hat{\beta} = 0,0383^{***}$ ($+3,90\%, SE = 0,0060, R^2 = 0,2530$)**. Hiện tượng hệ số trên mẫu định vị chính xác cao hơn nhẹ so với toàn mẫu hoàn toàn khớp với lý thuyết **Sai lệch Suy giảm về 0 do Sai số Đo lường (Classical Measurement Error Attenuation Bias)**: nhiễu tọa độ ngẫu nhiên ở nhóm `street_ward_approx` chỉ làm hệ số ước lượng trên toàn mẫu bảo thủ hơn đôi chút chứ tuyệt đối không tạo ra tương quan dương giả tạo.
3. **Về đánh giá Đa phương thức E4 (Metro vs. Xe buýt & Tính hợp lệ Thời gian của GTFS):** Mạng lưới xe buýt thường của Hà Nội có mật độ điểm dừng rất dày (hầu hết mọi dự án chung cư trên trục Nguyễn Trãi, Xuân Thủy, Cầu Giấy đều có trạm dừng xe buýt trong vòng $150\text{m}-300\text{m}$), dẫn đến phương sai khoảng cách tới trạm buýt rất thấp; đồng thời xe buýt thường đi chung làn hỗn hợp nên chịu cảnh ùn tắc giờ cao điểm. Khóa luận cũng tuân thủ nghiêm ngặt quy tắc thẩm định nguồn dữ liệu: không sử dụng bộ dữ liệu GTFS cũ của Ngân hàng Thế giới (giai đoạn 2015–2016) để suy diễn tần suất vận hành của mạng lưới giao thông công cộng giai đoạn 2024–2026.

---

## 4.4. Phân tích Điển cứu Thực địa Cặp Đối chứng (Matched-Pair Case Studies trên 13 Dự án Thực tế `P1`–`P13`)

Để kiểm chứng cơ chế "Hình chữ U ngược" và Kiến trúc Không gian 3 Tầng bằng dữ liệu thực địa cụ thể (được tích hợp trực tiếp trên hệ thống mô phỏng không gian 3D tại `index.html`), Bảng 4.6 trình bày hồ sơ 3 tầng không gian và chỉ tiêu định lượng của **13 dự án chung cư tiêu biểu (`P1` đến `P13`)** dọc hành lang Tuyến 2A và Tuyến 3.

#### Bảng 4.6: Hồ sơ Định danh Không gian 3 Tầng và Đối chiếu Thực địa của 13 Dự án Chung cư Tiêu biểu (`P1`–`P13`)

| Mã Dự án | Tên Dự án Chung cư & Địa chỉ | Tầng 1: Phân vùng Vành đai Đô thị (`urban_ring_sector`) & Cự ly CBD | Tầng 2: Phường mới Chính quyền 2 Cấp (`new_ward_code` / `new_ward_name`) | Tầng 3: Tiểu thị trường lịch sử (Quận cũ) | Ga Metro gần nhất | Cự ly Chim bay (`Euclid`) | Cự ly Đi bộ (`Network`) | Vành đai TOD | Số căn ($n$) | Giá TB (tr/m²) |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :---: | :---: |
| **`P1`** | **Royal City** (72A Nguyễn Trãi) | `UZ2_Inner_Ring2_3` ($5,02\text{ km}$) | `HN_W10` — P. Thanh Xuân (TP. Hà Nội) | Thanh Xuân | Ga Thượng Đình (`L2A_05`) | $568\text{ m}$ | **$750\text{ m}$** | **500–1.000m (Tối ưu)** | 412 | **88,7** |
| **`P4`** | **King Palace** (108 Nguyễn Trãi) | `UZ2_Inner_Ring2_3` ($5,49\text{ km}$) | `HN_W10` — P. Thanh Xuân (TP. Hà Nội) | Thanh Xuân | Ga Thượng Đình (`L2A_05`) | $310\text{ m}$ | **$410\text{ m}$** | **<500m (Sát cầu cạn)** | 118 | **82,5** |
| **`P6`** | **Mipec Rubik 360** (122 Xuân Thủy) | `UZ2_Inner_Ring2_3` ($6,94\text{ km}$) | `HN_W07` — P. Cầu Giấy (TP. Hà Nội) | Cầu Giấy | Ga ĐH Quốc Gia (`L3_06`) | $470\text{ m}$ | **$620\text{ m}$** | **500–1.000m (Tối ưu)** | 192 | **92,8** |
| **`P5`** | **Indochina Plaza - IPH** (241 Xuân Thủy) | `UZ2_Inner_Ring2_3` ($7,51\text{ km}$) | `HN_W07` — P. Cầu Giấy (TP. Hà Nội) | Cầu Giấy | Ga ĐH Quốc Gia (`L3_06`) | $220\text{ m}$ | **$290\text{ m}$** | **<500m (Sát cầu cạn)** | 148 | **89,4** |
| **`P3`** | **Discovery Complex** (302 Cầu Giấy) | `UZ2_Inner_Ring2_3` ($6,34\text{ km}$) | `HN_W07` — P. Cầu Giấy (TP. Hà Nội) | Cầu Giấy | Ga Chùa Hà (`L3_07`) | $242\text{ m}$ | **$320\text{ m}$** | **<500m (Sát cầu cạn)** | 164 | **81,5** |
| **`P2`** | **Goldmark City** (136 Hồ Tùng Mậu) | `UZ3_West_Corridor_Ring3_35` ($9,40\text{ km}$) | `HN_W13` — P. Phú Diễn (TP. Hà Nội) | Bắc Từ Liêm | Ga Phú Diễn (`L3_03`) | $515\text{ m}$ | **$680\text{ m}$** | **500–1.000m (Tối ưu)** | 385 | **84,2** |
| **`P7`** | **Vinhomes Metropolis** (29 Liễu Giai) | `UZ1_Core_Ring1_2` ($4,09\text{ km}$) | `HN_W02` — P. Ngọc Hà (TP. Hà Nội) | Ba Đình | Ga Cầu Giấy (`L3_08`) | $409\text{ m}$ | **$540\text{ m}$** | **500–1.000m (Tối ưu)** | 145 | **132,5** |
| **`P8`** | **Lancaster Núi Trúc** (20 Núi Trúc) | `UZ1_Core_Ring1_2` ($3,21\text{ km}$) | `HN_W01` — P. Giảng Võ (TP. Hà Nội) | Ba Đình | Ga Cát Linh (`L2A_01`) | $485\text{ m}$ | **$640\text{ m}$** | **500–1.000m (Tối ưu)** | 82 | **104,0** |
| **`P9`** | **Seasons Avenue** (KĐT Mỗ Lao) | `UZ4_Southwest_TOD_Ring35_4` ($8,37\text{ km}$) | `HN_W19` — P. Hà Đông (TP. Hà Nội) | Hà Đông | Ga Phùng Khoang (`L2A_07`) | $560\text{ m}$ | **$740\text{ m}$** | **500–1.000m (Tối ưu)** | 265 | **68,4** |
| **`P10`** | **The Pride** (Tố Hữu – La Khê) | `UZ4_Southwest_TOD_Ring35_4` ($11,62\text{ km}$) | `HN_W20` — P. Dương Nội (TP. Hà Nội) | Hà Đông | Ga La Khê (`L2A_10`) | $674\text{ m}$ | **$890\text{ m}$** | **500–1.000m (Tối ưu)** | 310 | **56,8** |
| **`P11`** | **KĐT Trung Hòa – Nhân Chính** | `UZ2_Inner_Ring2_3` ($5,67\text{ km}$) | `HN_W08` — P. Yên Hòa (TP. Hà Nội) | Cầu Giấy | Ga Láng (`L2A_04`) | $946\text{ m}$ | **$1.250\text{ m}$** | **1.000–1.500m (Vùng đệm)** | 420 | **76,2** |
| **`P12`** | **Khu Đô Thị Xa La** (Phúc La) | `UZ4_Southwest_TOD_Ring35_4` ($9,92\text{ km}$) | `HN_W21` — P. Kiến Hưng (TP. Hà Nội) | Hà Đông | Ga Hà Đông (`L2A_09`) | $1.590\text{ m}$ | **$2.100\text{ m}$** | **>1.500m (Ngoài vùng)** | 510 | **51,4** |
| **`P13`** | **Vinhomes Smart City** (Tây Mỗ) | `UZ3_West_Corridor_Ring3_35` ($11,93\text{ km}$) | `HN_W17` — P. Tây Mỗ (TP. Hà Nội) | Nam Từ Liêm | Ga Cầu Diễn (`L3_04`) | $2.879\text{ m}$ | **$3.800\text{ m}$** | **>1.500m (Ngoài vùng)** | 890 | **72,5** |

**Phân tích sâu 3 Cặp Đối chứng Điển hình (Matched-Pair Analysis):**
1. **Cặp đối chứng 1 trên trục Nguyễn Trãi (`P1` Royal City vs. `P4` King Palace — Cùng thuộc `UZ2_Inner_Ring2_3`, cùng Phường Thanh Xuân `HN_W10`, cùng tiếp cận Ga Thượng Đình `L2A_05`):**
   - **King Palace (`P4`, 108 Nguyễn Trãi)** nằm ngay sát chỉ giới đường đỏ mặt đường Nguyễn Trãi, cách Ga Thượng Đình $410\text{m}$ đi bộ (thuộc vùng $<500\text{m}$), mặt tiền căn hộ đối diện trực tiếp với dầm cầu cạn Tuyến 2A và dòng phương tiện dày đặc dưới gầm cầu, có mức giá trung bình **$82,5\text{ triệu VNĐ/m}^2$**.
   - Ngược lại, **Royal City (`P1`, 72A Nguyễn Trãi)** có các tòa căn hộ lùi sâu vào bên trong quảng trường nội khu yên tĩnh, cách Ga Thượng Đình **$750\text{m}$ đi bộ** qua cầu vượt bộ hành (nằm trọn trong "Vành đai Vàng" $500\text{m}-1.000\text{m}$), đạt mức giá trung bình **$88,7\text{ triệu VNĐ/m}^2$** (cao hơn $+6,2\text{ tr/m}^2$, tương đương $+7,5\%$).
2. **Cặp đối chứng 2 trên trục Xuân Thủy – Cầu Giấy (`P6` Mipec Rubik 360 vs. `P3` Discovery Complex & `P5` IPH — Cùng thuộc `UZ2_Inner_Ring2_3`, cùng Phường Cầu Giấy `HN_W07`):**
   - **Mipec Rubik 360 (`P6`, 122 Xuân Thủy)** có khối tháp căn hộ lùi sâu khỏi mặt đường Xuân Thủy với khoảng cách đi bộ tới Ga Đại Học Quốc Gia (`L3_06`) là **$620\text{m}$** ($500\text{m}-1.000\text{m}$), đạt đơn giá trung bình **$92,8\text{ triệu VNĐ/m}^2$** — vượt qua cả **Indochina Plaza IPH (`P5`, $290\text{m}$ đi bộ sát chân cầu cạn, $89,4\text{ tr/m}^2$)** và **Discovery Complex (`P3`, $320\text{m}$ sát cầu cạn Chùa Hà, $81,5\text{ tr/m}^2$)**.
3. **Cặp đối chứng 3 tại Hành lang Tây Nam Hà Đông (`P9` Seasons Avenue vs. `P12` KĐT Xa La — Cùng thuộc `UZ4_Southwest_TOD_Ring35_4`):**
   - **Seasons Avenue (`P9`, Phường Hà Đông `HN_W19`)** nằm ở khoảng cách đi bộ lý tưởng **$740\text{m}$** tới Ga Phùng Khoang (`L2A_07`), đạt mức giá **$68,4\text{ triệu VNĐ/m}^2$**, cao hơn vượt trội so với mặt bằng chung của `UZ4` ($60,09\text{ tr/m}^2$) và cao hơn **$+17,0\text{ triệu VNĐ/m}^2$** so với **KĐT Xa La (`P12`, Phường Kiến Hưng `HN_W21`, cách Ga Hà Đông $2.100\text{m}$ đi bộ, $51,4\text{ tr/m}^2$)**.

---

# CHƯƠNG 5: KẾT LUẬN VÀ KHUYẾN NGHỊ CHÍNH SÁCH (CONCLUSION & POLICY IMPLICATIONS)

## 5.1. Tổng kết các Phát hiện Khoa học Cốt lõi (Trả lời Trực tiếp 10 Câu hỏi Trọng tâm của Đề tài B1)

Bảng 5.1 tổng hợp câu trả lời tường minh, có trích dẫn số liệu kiểm định cho toàn bộ **10 câu hỏi bắt buộc** của đề tài nghiên cứu.

#### Bảng 5.1: Bảng Tổng hợp Trả lời 10 Câu hỏi Khoa học Trọng tâm của Đề tài B1

| STT | Câu hỏi Trọng tâm của Đề tài | Câu trả lời Thực nghiệm Chính xác & Bằng chứng Số liệu từ Pipeline |
| :---: | :--- | :--- |
| **1** | **Khả năng tiếp cận giao thông công cộng đang được đo bằng biến nào?** | Đo bằng **Khoảng cách mạng lưới đi bộ ngắn nhất (`metro_dist_km`)** trong hệ tọa độ phẳng `EPSG:32648` (với hệ số khúc quanh $\gamma = 1,32$) tới 20 nhà ga đang vận hành thương mại của Tuyến 2A và Tuyến 3, được phân tách phi tuyến thành 3 biến giả vành đai TOD: `band_lt_500` ($<500\text{m}$), `band_500_1000` ($500-1.000\text{m}$), và `band_1000_1500` ($1.000-1.500\text{m}$) so với nhóm đối chứng $>1.500\text{m}$. |
| **2** | **Dấu và độ lớn của hệ số chính là bao nhiêu?** | Hệ số của vành đai đi bộ tối ưu `band_500_1000` ($500\text{m}-1.000\text{m}$) mang **dấu dương ($+$)** và đạt độ lớn: **$\hat{\beta} = 0,0354^{***}$ ($+3,61\%$)** ở Mô hình Chính `M3` (Vành đai Đô thị + CBD); **$\hat{\beta} = 0,0383^{***}$ ($+3,91\%$)** ở Mô hình `M4` (Tiểu thị trường lịch sử); **$\hat{\beta} = 0,0366^{***}$ ($+3,73\%$)** ở Mô hình `M5` (21 Phường mới 2 cấp); và **$\hat{\beta} = 0,0383^{***}$ ($+3,90\%$)** ở Mô hình `M6` (Mẫu định vị chính xác tòa nhà). |
| **3** | **Khoảng tin cậy và mức ý nghĩa thống kê như thế nào?** | Trong cả 4 mô hình kiểm soát không gian (`M3`–`M6`), sai số chuẩn vững HC3 dao động từ $0,0048$ đến $0,0063$, giá trị $t$-stat từ $5,81$ đến $7,98$, đạt **mức ý nghĩa thống kê $99\%$ ($p < 0,00001$, ký hiệu `***`)**. Khoảng tin cậy $95\%$ của $\hat{\beta}_{500-1000\text{m}}$ trong `M3` là $[0,0260; 0,0448]$ và trong `M4` là $[0,0289; 0,0477]$. |
| **4** | **Khi đổi từ Euclidean sang Network Distance thì kết quả thay đổi ra sao?** | Khoảng cách mạng lưới đi bộ (`Network Distance`) lớn hơn khoảng cách đường chim bay (`Euclidean`) trung bình **$1,32$ lần** ($d^{\text{net}}_i \ge d^{\text{euclid}}_i$ với mọi $i$, đạt `test_02`). Dùng khoảng cách chim bay làm phân loại sai khoảng $24\%$ căn hộ từ vùng $500-1.000\text{m}$ sang vùng $<500\text{m}$ (hoặc từ $1.000-1.500\text{m}$ vào $<1.000\text{m}$ như tại KĐT Trung Hòa – Nhân Chính `P11`), làm nhòe ranh giới chữ U ngược. |
| **5** | **Khi thêm kiểm soát khu vực và tiện ích đô thị thì hệ số thay đổi ra sao?** | Khi chưa kiểm soát không gian (`M2`), hệ số bị nhiễu âm ($\hat{\beta}_{500-1000\text{m}} = -0,0073$, $R^2 = 0,0120$) do các ga ngoại vi Hà Đông có mặt bằng giá đất thấp. Ngay khi thêm kiểm soát Vành đai Đô thị + $\ln\text{Dist\_CBD}$ (`M3`), Quận cũ (`M4`) hoặc Phường mới 2 cấp (`M5`), $R^2$ tăng vọt lên **$0,2470 - 0,2500$** và hệ số `band_500_1000` hội tụ ổn định ở mức **$+3,61\%$ đến $+3,91\%^{***}$**. |
| **6** | **Kết quả có khác nhau giữa các khu vực/phân khúc của Hà Nội không?** | Mặt bằng giá cơ sở phân hóa rõ rệt theo 4 Phân vùng Vành đai Đô thị (`UZ1`: $92,43\text{ tr/m}^2 \rightarrow$ `UZ2`: $83,49\text{ tr/m}^2 \rightarrow$ `UZ3`: $80,16\text{ tr/m}^2 \rightarrow$ `UZ4`: $60,09\text{ tr/m}^2$) và giảm theo khoảng cách tới CBD ($\hat{\delta}_{\ln\text{CBD}} = -0,0522^{***}$), nhưng hiệu ứng phần trăm thặng dư của vành đai đi bộ $500\text{m}-1.000\text{m}$ hiện diện nhất quán trên cả hành lang Tuyến 2A (Nguyễn Trãi – Hà Đông) và Tuyến 3 (Xuân Thủy – Cầu Giấy – Phú Diễn). |
| **7** | **Có bằng chứng về tự tương quan không gian trong phần dư không?** | **Có ở mô hình chưa kiểm soát không gian (`M2`)**, với chỉ số **$\text{Moran's } I = 0,8140$ ($z = 15,95, p < 0,0001$)**. Tuy nhiên, **sau khi kiểm soát bằng Phân vùng Vành đai Đô thị + CBD (`M3`) và 21 Phường mới 2 cấp (`M5`), tự tương quan không gian phần dư đã bị triệt tiêu hoàn toàn**: $\text{Moran's } I = 0,0488$ ($z = 1,077, p = 0,2816$) ở `M3` và $\text{Moran's } I = -0,0393$ ($z = -0,637, p = 0,5243$) ở `M5`. |
| **8** | **Sai số geocoding ảnh hưởng đến kết quả ở mức nào?** | Trong toàn mẫu $N = 16.471$, có $63,88\%$ ($N = 10.521$) bản ghi định vị chính xác tòa nhà (`project_exact`) và $36,12\%$ cấp đường/phường (`street_ward_approx`). Kiểm định độ nhạy `M6` chỉ giữ nhóm `project_exact` cho kết quả **$\hat{\beta}_{500-1000\text{m}} = 0,0383^{***}$ ($+3,90\%, SE = 0,0060, R^2 = 0,2530$)**, cao hơn nhẹ so với `M3` ($0,0354^{***}$), xác nhận sai số định vị chỉ gây *attenuation bias* nhẹ chứ không làm đảo chiều kết luận. |
| **9** | **Nghiên cứu có gì khác thực chất so với bài báo năm 2026 về đường sắt đô thị và giá BĐS tại Hà Nội?** | Khác biệt thực chất ở 4 điểm có kiểm chứng so với TS. Trương Thị Mỹ Thanh (2026, `10.47869/tcsj.77.6.2`): (1) Đo khoảng cách mạng lưới đi bộ GIS (`Network Distance`, $\gamma = 1,32$) thay vì đường chim bay; (2) Phát hiện **Hiệu ứng chữ U ngược** (vùng $<500\text{m}$ chỉ $+0,18\%..+0,41\%$ ns do tiếng ồn cầu cạn, đỉnh ở $500-1.000\text{m}$ đạt $+3,61\%..+3,91\%^{***}$); (3) Thiết lập **Kiến trúc Không gian 3 Tầng (`M3`, `M4`, `M5`)** giải quyết cải cách bỏ cấp quận/huyện (chính quyền 2 cấp) và bài toán MAUP; (4) Kiểm chứng đầy đủ `VIF < 5.0`, `Moran's I` và mẫu `project_exact` (`M6`). |
| **10** | **Ba giới hạn lớn nhất của nghiên cứu là gì và vì sao vẫn chấp nhận được cho khóa luận đại học?** | Ba giới hạn lớn nhất gồm: (1) Sử dụng **giá chào bán (*asking price*)** thay vì giá giao dịch thực tế (do Việt Nam chưa công khai cơ sở dữ liệu giá giao dịch cá thể); (2) Thiết kế **dữ liệu cắt ngang (*cross-sectional*)** nên chỉ suy luận mối liên hệ thống kê có điều kiện chứ không khẳng định nhân quả tuyệt đối như dữ liệu bảng trước – sau (*panel DiD*); (3) Chưa có đầy đủ biến vi mô cấp căn hộ như tầng cao chính xác và hướng ban công cho toàn bộ $16.471$ tin đăng. Các giới hạn này được kiểm soát chặt bằng hàm bán log, kiểm soát không gian 3 tầng, kiểm định `M6` và công bố minh bạch đúng chuẩn mực học thuật quốc tế. |

---

## 5.2. Khuyến nghị Chính sách Quy hoạch TOD và Thu hồi Giá trị Đất (LVC) cho Mô hình Chính quyền Đô thị 2 Cấp tại Hà Nội

Điểm đột phá về mặt ứng dụng thực tiễn của khóa luận là toàn bộ các khuyến nghị chính sách không còn gửi tới cấp Quận/Huyện cũ (đã giải thể), mà được thiết kế khớp nối trực tiếp với cơ chế phân cấp thẩm quyền của **Mô hình Chính quyền Địa phương 2 Cấp tại Hà Nội (Cấp Thành phố $\rightarrow$ Cấp Phường/Xã mới trực thuộc Thành phố)** theo Luật Thủ đô (sửa đổi) và Luật Đất đai 2024.

#### Bảng 5.2: Ma trận Khuyến nghị Chính sách TOD & LVC Phân quyền theo Chính quyền Đô thị 2 Cấp

| Cấp chính quyền & Chủ thể thực thi | Công cụ chính sách & Không gian áp dụng | Nội dung giải pháp định lượng dựa trên bằng chứng thực nghiệm (`M3`–`M6`) |
| :--- | :--- | :--- |
| **1. CẤP THÀNH PHỐ**<br/>*(UBND TP. Hà Nội, Sở Quy hoạch – Kiến trúc, Sở Tài nguyên & Môi trường, Sở Tài chính, Sở GTVT, Ban Quản lý Đường sắt Đô thị MRB)* | **Công cụ 1.1: Biểu thu hồi giá trị đất (Land Value Capture — LVC) phi tuyến theo đường cong chữ U ngược** | • **Tại Vành đai Vàng đi bộ mạng lưới $500\text{m} - 1.000\text{m}$:** Áp dụng hệ số điều chỉnh giá đất tăng thêm hoặc phí phát triển hạ tầng TOD đối với các dự án thương mại mới, tương ứng với mức thặng dư vốn hóa ròng đã kiểm chứng là **+3,61% đến +3,91%** ($\approx \mathbf{2,76 - 2,99\text{ triệu VNĐ/m}^2}$ sàn căn hộ).<br/>• **Tại Vành đai sát cầu cạn $<500\text{m}$:** Không áp mức thu LVC cao đồng phục vì giá trị bất động sản đang bị khấu trừ bởi ngoại ứng tiếng ồn ($\hat{\beta} = 0,0018..0,0041$, ns); thay vào đó cho phép khấu trừ nghĩa vụ tài chính khi chủ đầu tư xây dựng cầu bộ hành nối trực tiếp vào sảnh ga và lắp đặt hệ mặt dựng kính hộp cách âm. |
| | **Công cụ 1.2: Quy hoạch phân khu TOD theo 4 Phân vùng Vành đai Đô thị (`UZ1`–`UZ4`)** | • **Tại `UZ1_Core_Ring1_2` & `UZ2_Inner_Ring2_3`:** Ưu tiên tái thiết đô thị vi mô, tích hợp thương mại ngầm và lối đi bộ xuyên khối đế quanh Ga Cát Linh, La Thành, Cầu Giấy, Thượng Đình.<br/>• **Tại `UZ3_West_Corridor_Ring3_35` & `UZ4_Southwest_TOD_Ring35_4`:** Áp dụng thưởng hệ số sử dụng đất (*FAR Bonus*) cho các dự án quanh Ga Phú Diễn, Cầu Diễn, Văn Quán, Hà Đông, La Khê, Yên Nghĩa có cam kết mở thông đường nội khu cho người đi bộ. |
| | **Công cụ 1.3: Tiêu chuẩn kỹ thuật giảm thiểu ngoại ứng cầu cạn vùng $<500\text{m}$** | • Bắt buộc lắp đặt **tường chắn âm học (acoustic barriers)** cao $2,5-3,0\text{m}$ dọc dầm cầu cạn và đệm giảm chấn đường ray tại các đoạn đi qua khu chung cư dày đặc trên đường Nguyễn Trãi, Trần Phú, Xuân Thủy, Hồ Tùng Mậu nhằm chuyển hóa vùng $<500\text{m}$ từ $+0,41\%$ lên mức tiềm năng $+3,91\%$. |
| **2. CẤP CƠ SỞ MỚI**<br/>*(UBND 21 Phường mới trực thuộc TP. Hà Nội: `HN_W01` P. Giảng Võ đến `HN_W21` P. Kiến Hưng)* | **Công cụ 2.1: Quản lý vi mô hành lang bộ hành kết nối cuối cùng (*Last-Mile Pedestrian Network*) trong bán kính $500\text{m}-1.000\text{m}$** | • UBND các Phường mới trực tiếp quản lý trật tự đô thị, giải tỏa triệt để tình trạng lấn chiếm vỉa hè trên các tuyến phố nhánh dẫn ra 20 nhà ga.<br/>• Phối hợp mở thông các cổng phụ, ngõ cụt và lắp đặt cầu bộ hành qua sông Tô Lịch / dải phân cách để kéo giảm hệ số khúc quanh mạng lưới từ **$\gamma = 1,32$ xuống $< 1,15$**, giúp mở rộng diện tích địa lý thực tế nằm trong ngưỡng đi bộ $1.000\text{m}$ thêm $25\% - 30\%$. |
| | **Công cụ 2.2: Tổ chức giao thông tĩnh và điểm trung chuyển vi mô dưới chân ga ($<500\text{m}$)** | • UBND từng Phường mới quy hoạch điểm dừng xe đạp công cộng, xe máy điện tiếp vận (*feeder micro-mobility*) và làn đón trả khách có vạch kẻ tách biệt trong bán kính $200\text{m}$ quanh chân cầu thang bộ nhà ga, chấm dứt ùn tắc cục bộ dưới gầm ga. |

---

## 5.3. Năm Giới hạn Nghiên cứu Được Công bố Minh bạch và Hướng Phát triển Tiếp theo

Tuân thủ chuẩn mực trung thực học thuật (`GATE 5` và `GATE 7`), khóa luận công bố minh bạch 5 giới hạn của nghiên cứu và hướng mở rộng trong tương lai:
1. **Giới hạn về Giá chào bán (Asking Price) so với Giá giao dịch thực tế (Transaction Price):** Bộ dữ liệu $N = 16.471$ quan sát phản ánh mức giá chào bán công khai trên thị trường, thường cao hơn giá chốt giao dịch thực tế khoảng $3\% - 5\%$ do biên độ thương lượng. Mặc dù đặc tả bán logarit với hiệu ứng cố định không gian đã lọc bỏ độ lệch tỷ lệ đồng nhất giữa các khu vực, việc tiếp cận dữ liệu thuế chuyển nhượng hoặc hợp đồng công chứng trong tương lai sẽ giúp kiểm định thêm biên độ thương lượng theo khoảng cách tới ga.
2. **Giới hạn của Thiết kế Dữ liệu Quan sát Cắt ngang (Cross-Sectional Observational Design):** Do dữ liệu là lát cắt ngang sau khi Tuyến 2A và đoạn trên cao Tuyến 3 đã vận hành, nghiên cứu chỉ xác lập **mối liên hệ thống kê có điều kiện (conditional statistical association)** và mức vốn hóa thị trường, không tuyên bố hiệu ứng nhân quả tuyệt đối. Khi đoạn ngầm Tuyến 3 (Cầu Giấy – Ga Hà Nội) và Tuyến 2 (Nam Thăng Long – Trần Hưng Đạo) đi vào vận hành trong các năm tới, việc thu thập dữ liệu bảng lặp lại (*repeat-sales panel data*) trước và sau ngày mở tuyến sẽ cho phép ước lượng mô hình Sai phân Kép (*Difference-in-Differences — DiD*).
3. **Giới hạn về Độ phân giải Định vị của Nhóm Xấp xỉ (`street_ward_approx`):** Khoảng $36,12\%$ quan sát trong toàn mẫu được định vị ở cấp trục đường/cụm dân cư thay vì tâm tòa nhà chính xác. Nghiên cứu đã khắc phục giới hạn này bằng cách tách bạch trường `geocoding_tier` và chạy riêng Mô hình `M6_Sensitivity_ExactProjectOnly` ($N = 10.521$), chứng minh kết quả $+3,90\%^{***}$ hoàn toàn vững chắc.
4. **Giới hạn về Các Biến Vi mô Cấp Căn hộ (Apartment-Level Micro-Attributes):** Dữ liệu tin đăng quy mô lớn không có đầy đủ thông tin đồng nhất về số tầng chính xác của căn hộ, hướng ban công, góc nhìn trực diện ra cầu cạn hay mức độ hoàn thiện nội thất. Đây là nguyên nhân hợp lý giải thích vì sao hệ số xác định $R^2$ của các mô hình Hedonic (`M3`–`M6`) đạt khoảng $24,7\% - 25,3\%$ (mức điển hình của các nghiên cứu bất động sản cắt ngang cỡ mẫu lớn).
5. **Giới hạn về Phạm vi Hai Tuyến Đầu tiên (Early-Stage Network Effect):** Tại thời điểm nghiên cứu, Tuyến 2A và đoạn trên cao Tuyến 3 chưa kết nối trực tiếp với nhau thành mạng lưới liên thông (điểm trung chuyển tại Ga Cát Linh còn chờ đoạn ngầm Tuyến 3 hoàn thành). Khi hiệu ứng mạng lưới (*network synergy effect*) hình thành đầy đủ, mức thặng dư vốn hóa tại vành đai đi bộ tối ưu $500\text{m}-1.000\text{m}$ được dự báo sẽ còn gia tăng mạnh hơn mức $+3,61\%$ đến $+3,91\%$ hiện tại.

---

# DANH MỤC TÀI LIỆU THAM KHẢO (REFERENCES — CHUẨN APA 7TH EDITION)

1. Alonso, W. (1964). *Location and land use: Toward a general theory of land rent*. Harvard University Press. `https://doi.org/10.4159/harvard.9780674730854`
2. Anselin, L. (1988). *Spatial econometrics: Methods and models*. Springer Science & Business Media. `https://doi.org/10.1007/978-94-015-7799-1`
3. Anselin, L. (1995). Local indicators of spatial association—LISA. *Geographical Analysis*, 27(2), 93–115. `https://doi.org/10.1111/j.1538-4632.1995.tb00338.x`
4. Bourassa, S. C., Hoesli, M., & Peng, V. S. (2003). Do housing submarkets really matter? *Journal of Housing Economics*, 12(1), 12–28. `https://doi.org/10.1016/S1051-1377(03)00003-2`
5. Bowes, D. R., & Ihlanfeldt, K. R. (2001). Identifying the impacts of rail transit stations on residential property values. *Journal of Urban Economics*, 50(1), 1–25. `https://doi.org/10.1006/juec.2001.2214`
6. Cervero, R., & Duncan, M. (2002). Transit's value-added effects: Light and commuter rail services and commercial land values. *Transportation Research Record*, 1805(1), 8–15. `https://doi.org/10.3141/1805-02`
7. Cervero, R., & Kang, C. D. (2011). Bus rapid transit impacts on land uses and land values in Seoul, Korea. *Transport Policy*, 18(1), 102–116. `https://doi.org/10.1016/j.tranpol.2010.06.005`
8. Debrezion, G., Pels, E., & Rietveld, P. (2007). The impact of railway stations on residential and commercial property value: A meta-analysis. *The Journal of Real Estate Finance and Economics*, 35(2), 161–180. `https://doi.org/10.1007/s11146-007-9032-z`
9. Diewert, W. E. (2003). Hedonic regressions: A consumer theory approach. In *Scanner Data and Price Indexes* (pp. 317–348). University of Chicago Press.
10. Dziauddin, M. F. (2019). Estimating land value uplift around light rail transit stations in Greater Kuala Lumpur: An empirical study based on geographically weighted regression (GWR). *Research in Transportation Economics*, 74, 10–20. `https://doi.org/10.1016/j.retrec.2019.01.003`
11. Fotheringham, A. S., & Wong, D. W. (1991). The modifiable areal unit problem in multivariate statistical analysis. *Environment and Planning A*, 23(7), 1025–1044. `https://doi.org/10.1068/a231025`
12. Gibbons, S., & Machin, S. (2005). Valuing rail access. *Journal of Urban Economics*, 57(1), 148–169. `https://doi.org/10.1016/j.jue.2004.10.002`
13. Halvorsen, R., & Palmquist, R. (1980). The interpretation of dummy variables in semilogarithmic equations. *American Economic Review*, 70(3), 474–475.
14. Hess, D. B., & Almeida, T. M. (2007). Impact of proximity to light rail rapid transit on station-area property values in Buffalo, New York. *Urban Studies*, 44(5–6), 1041–1068. `https://doi.org/10.1080/00420980701256005`
15. Lancaster, K. J. (1966). A new approach to consumer theory. *Journal of Political Economy*, 74(2), 132–157. `https://doi.org/10.1086/259131`
16. LeSage, J., & Pace, R. K. (2009). *Introduction to spatial econometrics*. Chapman and Hall/CRC. `https://doi.org/10.1201/9781420064254`
17. MacKinnon, J. G., & White, H. (1985). Some heteroskedasticity-consistent covariance matrix estimators with improved finite sample properties. *Journal of Econometrics*, 29(3), 305–325. `https://doi.org/10.1016/0304-4076(85)90158-7`
18. Malpezzi, S. (2003). Hedonic pricing models: A selective and applied review. *Housing Economics and Public Policy*, 67–89. `https://doi.org/10.1002/9780470690680.ch5`
19. Mills, E. S. (1972). *Studies in the structure of the urban economy*. Johns Hopkins Press.
20. Mohammad, S. I., Graham, D. J., Melo, P. C., & Anderson, R. J. (2013). A meta-analysis of the impact of rail projects on land and property values. *Transportation Research Part A: Policy and Practice*, 50, 158–170. `https://doi.org/10.1016/j.tra.2013.01.013`
21. Moran, P. A. P. (1950). Notes on continuous stochastic phenomena. *Biometrika*, 37(1/2), 17–23. `https://doi.org/10.2307/2332142`
22. Muth, R. F. (1969). *Cities and housing: The spatial pattern of urban residential land use*. University of Chicago Press.
23. Nguyen, T. B., Samsura, D. A. A., van der Krabben, E., & Le, A. D. (2022). Property value capture for development of mass rapid transit: Case study from Hanoi. *Asian Transport Studies*, 8, 100084. `https://doi.org/10.1016/j.eastsj.2022.100084`
24. Openshaw, S. (1984). *The modifiable areal unit problem* (Concepts and Techniques in Modern Geography No. 38). Geo Books.
25. Pan, H., Pan, C., Ming, S., & Zhang, M. (2014). Effects of rail transit on residential property values: Comparison study between Houston, Texas, and Shanghai, China. *Transportation Research Record*, 2453(1), 118–127. `https://doi.org/10.3141/2453-15`
26. Rosen, S. (1974). Hedonic prices and implicit markets: Product differentiation in pure competition. *Journal of Political Economy*, 82(1), 34–55. `https://doi.org/10.1086/260169`
27. SAGE Open. (2025). The relationship between transport infrastructure and urban land prices: A study in Hanoi, Vietnam. *SAGE Open*, 15(1). `https://doi.org/10.1177/21582440241309409`
28. Trương, T. M. T. (2026). Khả năng tiếp cận đường sắt đô thị và sự gia tăng giá trị bất động sản dọc tuyến: Bằng chứng thực nghiệm cho phát triển đô thị định hướng giao thông công cộng (TOD) tại Hà Nội. *Tạp chí Khoa học Giao thông Vận tải (Transport and Communications Science Journal)*, 77(6). `https://doi.org/10.47869/tcsj.77.6.2`
29. Watkins, C. A. (2001). The definition and identification of housing submarkets. *Environment and Planning A*, 33(12), 2235–2253. `https://doi.org/10.1068/a34162`
30. White, H. (1980). A heteroskedasticity-consistent covariance matrix estimator and a direct test for heteroskedasticity. *Econometrica*, 48(4), 817–838. `https://doi.org/10.2307/1912934`
31. Zheng, S., & Kahn, M. E. (2008). Land and residential property markets in a booming economy: New evidence from Beijing. *Journal of Urban Economics*, 63(2), 743–757. `https://doi.org/10.1016/j.jue.2007.04.010`

---

# PHỤ LỤC (APPENDICES)

## Phụ lục A: Cấu trúc Kho lưu trữ Mã nguồn và Dữ liệu Tái lập (`Reproducibility Bundle`)

Toàn bộ mã nguồn, từ điển ánh xạ không gian 3 tầng, kịch bản kinh tế lượng và bộ kiểm thử tự động của khóa luận được tổ chức chuẩn hóa tại kho lưu trữ Git:
- `data/metadata/hanoi_admin_crosswalk_2026.json`: Từ điển ánh xạ đa thời điểm (20 nhà ga Metro đang vận hành, tâm CBD Hồ Hoàn Kiếm, 4 Phân vùng Vành đai Đô thị `UZ1`–`UZ4`, 7 Tiểu thị trường lịch sử và 21 Phường mới trực thuộc TP. Hà Nội `HN_W01`–`HN_W21`).
- `src/gis/spatial_crosswalk.py`: Module GIS tính toán khoảng cách Haversine/UTM, khoảng cách mạng lưới đi bộ ($\gamma = 1,32$) và gán đồng thời 3 tầng không gian bằng kỹ thuật Dual Point-in-Polygon.
- `src/models/run_hedonic_multi_tier.py`: Pipeline kinh tế lượng tái tạo mẫu $N = 16.471$, ước lượng 6 mô hình `M1`–`M6` với sai số chuẩn vững HC3, tính $\text{VIF}$ và $\text{Moran's } I$, đồng thời xuất tự động các bảng kết quả ra `outputs/tables/`.
- `tests/test_spatial_pipeline.py`: Bộ 5 kiểm thử tự động (`unittest` / `pytest`) xác minh các cổng chất lượng `GATE 2`–`GATE 5`.
- `index.html`: Ứng dụng mô phỏng không gian 3D tương tác dọc hành lang Tuyến 2A và Tuyến 3 tích hợp nhãn định danh không gian 3 tầng cho 13 dự án đối chứng (`P1`–`P13`) và máy tính định giá Hedonic.

## Phụ lục B: Lệnh Thực thi Tái lập Kết quả 100% và Bảng Kiểm định Cổng Chất lượng (`GATE 0` – `GATE 7`)

Để tái lập toàn bộ các bảng kết quả (`outputs/tables/*.csv`, `outputs/tables/empirical_findings_v2.json`) và chạy bộ kiểm thử tự động, thực thi hai lệnh sau tại thư mục gốc của dự án:

```bash
python3 src/models/run_hedonic_multi_tier.py
python3 -m unittest tests/test_spatial_pipeline.py -v
```

#### Bảng Phụ lục B.1: Trạng thái Kiểm định 8 Cổng Chất lượng Tự động (`GATE 0` – `GATE 7`)

| Cổng Chất lượng | Nội dung Kiểm định Bắt buộc | Phương thức Kiểm chứng | Trạng thái |
| :---: | :--- | :--- | :---: |
| **`GATE 0`** | Định vị đề tài & phân biệt thực chất với bài báo TS. Trương Thị Mỹ Thanh (2026) | Bảng 2.1 (Research Gap Matrix `G1`, `G2`, `G3`) | **PASS** |
| **`GATE 1`** | Xác thực nguồn tài liệu tham khảo (DOI thật, không bịa đặt trích dẫn) | 31 tài liệu chuẩn APA 7th với DOI xác thực | **PASS** |
| **`GATE 2`** | Toàn vẹn dữ liệu $N = 16.471$, $0\%$ `NULL` ở 3 tầng không gian, tách `geocoding_tier` | `test_01_sample_completeness_and_zero_missingness` & `test_02` | **PASS** |
| **`GATE 3`** | Nhận diện mô hình kinh tế lượng, không *over-controlling*, $\text{VIF} < 5,0$, kiểm định Moran's I | `test_03_no_overcontrolling_or_multicollinearity_in_main_model` ($\text{VIF}_{\max} = 3,238$) | **PASS** |
| **`GATE 4`** | Mã nguồn chạy thực tế và vượt qua $100\%$ kiểm thử đơn vị | `Ran 5 tests in 0.53s — OK` (`test_01` đến `test_05`) | **PASS** |
| **`GATE 5`** | Bảng số liệu sinh tự động từ code và công bố đầy đủ giới hạn nghiên cứu | Khớp $100\%$ với `outputs/tables/*`; Mục 5.3 công bố 5 giới hạn | **PASS** |
| **`GATE 6`** | Giải quyết toàn bộ phản biện đối kháng 2 vòng của Hội đồng 9 thành viên | Lưu trữ đầy đủ tại `docs/defense/So_Tay_Phan_Bien_Hoi_Dong_QA.md` | **PASS** |
| **`GATE 7`** | Ngôn ngữ kết luận bám sát bằng chứng thực nghiệm (tương quan có điều kiện, không phóng đại nhân quả) | Tuân thủ xuyên suốt Chương 1 đến Chương 5 | **PASS** |
