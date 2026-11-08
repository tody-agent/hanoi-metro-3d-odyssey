# 🚝 Hanoi Metro 3D Odyssey

**Bản đồ 3D tương tác (OpenStreetMap & Google Earth)** chia sẻ kết quả nghiên cứu thực nghiệm về tác động của khả năng tiếp cận đường sắt đô thị (**Tuyến Metro 2A Cát Linh – Hà Đông** & **Tuyến 3 Nhổn – Ga Hà Nội**) đến giá chào bán căn hộ chung cư tại Hà Nội ($N = 16.471$ căn hộ trên 7 quận).

---

## ✨ Tính năng nổi bật

1. **Địa hình & Hạ tầng 3D theo tọa độ GPS thực tế (WGS84)**:
   - Tái hiện mặt nước **Sông Hồng**, **Hồ Tây**, sông Tô Lịch, sông Nhuệ và hệ thống hồ nội đô (Hoàng Cầu, Thủ Lệ, Giảng Võ, Văn Quán, Linh Đàm).
   - Các trục giao thông huyết mạch: **Vành Đai 3**, **Đại lộ Thăng Long**, **Nguyễn Trãi – Trần Phú – Quang Trung**, **Xuân Thủy – Cầu Giấy – Kim Mã**, **Giải Phóng – Lê Duẩn**.
   - Chuyển đổi tức thì giữa **Nền 3D Google Earth** (Dark Geospatial) và **Nền Bản Đồ OpenStreetMap (OSM Standard)**.
2. **Kiến trúc Tòa nhà Chung cư & Đoàn tàu Metro 3D**:
   - **Tổ hợp căn hộ 3D**: Khối đế thương mại (Podium), cụm tháp đôi (Twin-Tower), hệ thống lưới cửa sổ phát sáng (Window Mullions) và tầng mái Penthouse.
   - **Đoàn tàu Metro 4 toa khớp nối (4-Car Articulated Trains)**: Chuyển động mượt theo đường cong Catmull-Rom, xoay theo góc tiếp tuyến của cầu cạn, có dải màu nhận diện trên nóc và thân tàu, cụm điều hòa nóc toa (HVAC pod) và chùm đèn pha chiếu sáng đường ray.
   - **23 Nhà ga 3D**: Thiết kế mái vòm kính tối màu viền phát sáng tách biệt rõ ràng trên cầu cạn và đoạn đi ngầm (Kim Mã – Cát Linh – Văn Miếu – Ga Hà Nội).
3. **Kết quả nghiên cứu thực nghiệm (Quy luật Chữ U Ngược — Inverted-U)**:
   - Mô hình hồi quy **Hedonic OLS (sai số chuẩn vững HC3)** có kiểm soát **Hiệu ứng cố định theo Quận (District Fixed Effects)** ($R^2 = 0.2492$):
     - **Sát chân ga (`< 500m`)**: `+0.41%` (*p = 0.415*, không có ý nghĩa thống kê) — Lợi ích đi lại bị khấu trừ bởi ngoại ứng tiếng ồn cầu cạn, rung chấn và ùn tắc giao thông dưới gầm ga.
     - **Vùng đi bộ tối ưu (`500m – 1.000m` — Sweet Spot)**: **`+3.91% ***`** (*p < 0.001, t = 7.82*) — Khoảng cách đi bộ 6–12 phút tách khỏi mặt đường ồn ào nhưng hưởng trọn tiện ích giao thông công cộng (tương đương **+260 đến +350 triệu VNĐ** cho căn hộ 75–100 m²).
     - **Vùng đệm (`1.000m – 1.500m`)**: `+0.02%` (*p = 0.968*).
     - **Ngoài vùng đi bộ (`> 1.500m`)**: `0.00%` (Nhóm đối chiếu).

---

## 🚀 Chạy trực tiếp

Trang web được đóng gói hoàn toàn độc lập (**Zero-build Single-file HTML5 + 3D Canvas Engine**) trong file `index.html`, tối ưu cho cả **Desktop** và **Mobile**.
