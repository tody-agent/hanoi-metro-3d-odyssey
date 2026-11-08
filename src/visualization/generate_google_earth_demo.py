#!/usr/bin/env python3
"""
B1 Research Project — Google Earth Web KML/KMZ/GeoJSON Generator (Demo & Pipeline Prototype)
Chủ đề: Định lượng mối liên hệ giữa khả năng tiếp cận giao thông công cộng và giá chào bán căn hộ
tại Hà Nội bằng mô hình Hedonic Pricing và hệ thống thông tin địa lý GIS.

Khu vực mẫu: Hành lang Tuyến Metro số 3 (Nhổn - Cầu Giấy) & Khu vực Cầu Giấy - Mỹ Đình (Nam/Bắc Từ Liêm).
Lưu ý liêm chính khoa học (Mục VI & VIII research_b1.md):
- Tọa độ các nhà ga Metro Tuyến số 3 và các tòa chung cư là tọa độ thực tế đã xác minh (WGS84).
- Dữ liệu tin đăng căn hộ chi tiết bên trong từng tòa là dữ liệu mô phỏng có cấu trúc (Synthetic Benchmark)
  để kiểm thử pipeline kinh tế lượng (OLS Hedonic với Clustered SE) và giao diện trực quan Google Earth.
"""

from __future__ import annotations

import csv
import html
import json
import math
import zipfile
from pathlib import Path
from typing import Any

import numpy as np


# ==============================================================================
# 1. DỮ LIỆU HẠ TẦNG GIAO THÔNG CÔNG CỘNG (TỌA ĐỘ THỰC TẾ WGS84)
# ==============================================================================
METRO_STATIONS = [
    {
        "code": "T3-S01",
        "name": "Ga Nhổn (Depot)",
        "lat": 21.05250,
        "lon": 105.73528,
        "status": "operational",
        "status_label": "Đang vận hành thương mại (08/08/2024)",
        "structure": "Trên cao (Elevated)",
        "feeder_bus": "05, 13, 20A, 29, 32, 70A, 70B, 92",
        "line": "Tuyến số 3 (Nhổn – Ga Hà Nội)",
    },
    {
        "code": "T3-S02",
        "name": "Ga Minh Khai",
        "lat": 21.04806,
        "lon": 105.74472,
        "status": "operational",
        "status_label": "Đang vận hành thương mại (08/08/2024)",
        "structure": "Trên cao (Elevated)",
        "feeder_bus": "20A, 29, 32, 57, 70A, 70B",
        "line": "Tuyến số 3 (Nhổn – Ga Hà Nội)",
    },
    {
        "code": "T3-S03",
        "name": "Ga Phú Diễn",
        "lat": 21.04389,
        "lon": 105.75528,
        "status": "operational",
        "status_label": "Đang vận hành thương mại (08/08/2024)",
        "structure": "Trên cao (Elevated)",
        "feeder_bus": "20A, 29, 32, 70A, 70B",
        "line": "Tuyến số 3 (Nhổn – Ga Hà Nội)",
    },
    {
        "code": "T3-S04",
        "name": "Ga Cầu Diễn",
        "lat": 21.04111,
        "lon": 105.76278,
        "status": "operational",
        "status_label": "Đang vận hành thương mại (08/08/2024)",
        "structure": "Trên cao (Elevated)",
        "feeder_bus": "05, 13, 20A, 29, 32, 70A, 70B",
        "line": "Tuyến số 3 (Nhổn – Ga Hà Nội)",
    },
    {
        "code": "T3-S05",
        "name": "Ga Lê Đức Thọ",
        "lat": 21.03806,
        "lon": 105.77306,
        "status": "operational",
        "status_label": "Đang vận hành thương mại (08/08/2024)",
        "structure": "Trên cao (Elevated)",
        "feeder_bus": "20A, 29, 32, 56A, 70A, 70B",
        "line": "Tuyến số 3 (Nhổn – Ga Hà Nội)",
    },
    {
        "code": "T3-S06",
        "name": "Ga Đại học Quốc gia",
        "lat": 21.03667,
        "lon": 105.78278,
        "status": "operational",
        "status_label": "Đang vận hành thương mại (08/08/2024)",
        "structure": "Trên cao (Elevated)",
        "feeder_bus": "07, 16, 20A, 26, 27, 32, 34, 49",
        "line": "Tuyến số 3 (Nhổn – Ga Hà Nội)",
    },
    {
        "code": "T3-S07",
        "name": "Ga Chùa Hà",
        "lat": 21.03497,
        "lon": 105.79431,
        "status": "operational",
        "status_label": "Đang vận hành thương mại (08/08/2024)",
        "structure": "Trên cao (Elevated)",
        "feeder_bus": "07, 16, 20A, 26, 27, 28, 32, 34, 49",
        "line": "Tuyến số 3 (Nhổn – Ga Hà Nội)",
    },
    {
        "code": "T3-S08",
        "name": "Ga Cầu Giấy (Điểm trung chuyển)",
        "lat": 21.02944,
        "lon": 105.80333,
        "status": "operational",
        "status_label": "Đang vận hành thương mại (08/08/2024)",
        "structure": "Trên cao (Elevated)",
        "feeder_bus": "07, 09A, 16, 24, 26, 27, 28, 32, 34, 38, 49, 55, 90",
        "line": "Tuyến số 3 (Nhổn – Ga Hà Nội)",
    },
    {
        "code": "T3-S09",
        "name": "Ga Ngầm Kim Mã (Đang thi công)",
        "lat": 21.03056,
        "lon": 105.81417,
        "status": "under_construction",
        "status_label": "Đang thi công ngầm (Chưa vận hành thương mại)",
        "structure": "Đi ngầm (Underground)",
        "feeder_bus": "09A, 22A, 32, 34, 38, 50, BRT01",
        "line": "Tuyến số 3 (Đoạn ngầm Cầu Giấy – Ga Hà Nội)",
    },
    {
        "code": "T3-S10",
        "name": "Ga Cát Linh (Trung chuyển Tuyến 2A/3)",
        "lat": 21.02806,
        "lon": 105.82722,
        "status": "under_construction",
        "status_label": "Ga T2A đang vận hành / Ga ngầm T3 đang thi công",
        "structure": "Trung chuyển Trên cao T2A & Ngầm T3",
        "feeder_bus": "18, 22A, 23, 25, 38, 49, 50, 99, BRT01",
        "line": "Tuyến số 3 & Tuyến 2A (Cát Linh – Hà Đông)",
    },
]

# Một số điểm dừng xe buýt tiếp vận chính quanh khu vực Cầu Giấy - Mỹ Đình
BUS_STOPS = [
    {"id": "BUS-01", "name": "Điểm trung chuyển Cầu Giấy", "lat": 21.02890, "lon": 105.80380, "routes": "07, 16, 24, 26, 27, 28, 32, 34, 49"},
    {"id": "BUS-02", "name": "Trạm 302 Cầu Giấy (Discovery)", "lat": 21.03550, "lon": 105.79310, "routes": "07, 16, 20A, 26, 27, 32, 34"},
    {"id": "BUS-03", "name": "Trạm ĐH Quốc gia / IPH Xuân Thủy", "lat": 21.03635, "lon": 105.78280, "routes": "07, 16, 20A, 26, 27, 32, 34, 49"},
    {"id": "BUS-04", "name": "Trạm Bến xe Mỹ Đình (Phạm Hùng)", "lat": 21.02860, "lon": 105.77850, "routes": "16, 20B, 22B, 29, 30, 33, 34, 44, 46, 53B, 60B"},
    {"id": "BUS-05", "name": "Trạm 136 Hồ Tùng Mậu (Goldmark)", "lat": 21.03915, "lon": 105.76750, "routes": "05, 13, 20A, 29, 32, 70A, 70B"},
    {"id": "BUS-06", "name": "Trạm Ngã tư Lê Đức Thọ - Hàm Nghi", "lat": 21.03280, "lon": 105.76810, "routes": "26, 50, 56A, 104, E05"},
    {"id": "BUS-07", "name": "Trạm Quảng trường SVĐ Quốc gia Mỹ Đình", "lat": 21.02090, "lon": 105.76540, "routes": "26, 50, 56A, 104"},
    {"id": "BUS-08", "name": "Trạm Keangnam / Phạm Hùng", "lat": 21.01720, "lon": 105.78210, "routes": "05, 22B, 29, 30, 33, 50, 60A, 60B"},
]


# ==============================================================================
# 2. DỮ LIỆU TỔ HỢP DỰ ÁN CHUNG CƯ & ĐƯỜNG ĐI BỘ THỰC TẾ (G1, G2, G3)
# ==============================================================================
# Mỗi dự án có:
# - Tọa độ thực tế (lat, lon)
# - Geocoding tier: Exact Building (Tier 1) hoặc Approximate Street-level (Tier 2)
# - Tuyến đi bộ thực tế (walking_waypoints) dọc theo vỉa hè/cầu vượt bộ hành tới ga Metro gần nhất
# - Các đặc trưng dự án và danh sách các căn hộ đang chào bán bên trong
PROJECTS_RAW = [
    {
        "project_id": "PRJ-01",
        "name": "Discovery Complex (302 Cầu Giấy)",
        "district": "Cầu Giấy",
        "ward": "Dịch Vọng",
        "segment": "Cao cấp (High-end)",
        "handover_year": 2018,
        "total_floors": 54,
        "lat": 21.03585,
        "lon": 105.79295,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 5,
        "nearest_station_code": "T3-S07",
        "bus_stops_500m": 6,
        "nearest_bus_m": 65,
        "dist_cbd_km": 5.8,
        # Đi bộ dọc thẳng vỉa hè đường Cầu Giấy tới cầu thang lên Ga Chùa Hà (kết nối cầu cạn trực tiếp)
        "walking_waypoints": [
            (21.03585, 105.79295),
            (21.03545, 105.79305),
            (21.03515, 105.79385),
            (21.03497, 105.79431),
        ],
        "barrier_note": "Tiếp cận trực tiếp dọc vỉa hè đường Cầu Giấy và lối cầu bộ hành nối thẳng tầng trung chuyển Ga Chùa Hà.",
        "apartments": [
            {"apt_id": "DC-2204", "tower": "Tháp A", "floor": 22, "area_m2": 96.5, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 82.5, "listing_date": "2026-09"},
            {"apt_id": "DC-3510", "tower": "Tháp A", "floor": 35, "area_m2": 112.0, "bedrooms": 3, "direction": "Đông Bắc", "asking_price_m2": 84.0, "listing_date": "2026-10"},
            {"apt_id": "DC-1508", "tower": "Tháp A", "floor": 15, "area_m2": 87.0, "bedrooms": 2, "direction": "Tây Bắc", "asking_price_m2": 79.5, "listing_date": "2026-10"},
            {"apt_id": "DC-4102", "tower": "Tháp A", "floor": 41, "area_m2": 143.5, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 85.5, "listing_date": "2026-10"},
            {"apt_id": "DC-2806", "tower": "Tháp A", "floor": 28, "area_m2": 99.0, "bedrooms": 2, "direction": "Nam", "asking_price_m2": 81.8, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-02",
        "name": "Indochina Plaza Hanoi - IPH (241 Xuân Thủy)",
        "district": "Cầu Giấy",
        "ward": "Dịch Vọng Hậu",
        "segment": "Cao cấp (High-end)",
        "handover_year": 2012,
        "total_floors": 36,
        "lat": 21.03569,
        "lon": 105.78276,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 5,
        "nearest_station_code": "T3-S06",
        "bus_stops_500m": 7,
        "nearest_bus_m": 75,
        "dist_cbd_km": 6.8,
        "walking_waypoints": [
            (21.03569, 105.78276),
            (21.03625, 105.78277),
            (21.03667, 105.78278),
        ],
        "barrier_note": "Đối diện trực tiếp Ga Đại học Quốc gia qua đường Xuân Thủy (có cầu bộ hành lên thẳng ke ga).",
        "apartments": [
            {"apt_id": "IPH-E1802", "tower": "East Tower", "floor": 18, "area_m2": 93.0, "bedrooms": 2, "direction": "Bắc", "asking_price_m2": 88.0, "listing_date": "2026-09"},
            {"apt_id": "IPH-W2405", "tower": "West Tower", "floor": 24, "area_m2": 110.5, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 91.5, "listing_date": "2026-10"},
            {"apt_id": "IPH-E1104", "tower": "East Tower", "floor": 11, "area_m2": 93.0, "bedrooms": 2, "direction": "Nam", "asking_price_m2": 86.2, "listing_date": "2026-10"},
            {"apt_id": "IPH-W3001", "tower": "West Tower", "floor": 30, "area_m2": 128.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 93.0, "listing_date": "2026-10"},
            {"apt_id": "IPH-E2107", "tower": "East Tower", "floor": 21, "area_m2": 116.0, "bedrooms": 3, "direction": "Đông", "asking_price_m2": 89.4, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-03",
        "name": "The West / FLC Twin Towers (265 Cầu Giấy)",
        "district": "Cầu Giấy",
        "ward": "Dịch Vọng",
        "segment": "Trung - Cao cấp",
        "handover_year": 2019,
        "total_floors": 50,
        "lat": 21.03445,
        "lon": 105.79385,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 6,
        "nearest_station_code": "T3-S07",
        "bus_stops_500m": 6,
        "nearest_bus_m": 80,
        "dist_cbd_km": 5.9,
        "walking_waypoints": [
            (21.03445, 105.79385),
            (21.03495, 105.79395),
            (21.03497, 105.79431),
        ],
        "barrier_note": "Nằm sát cổng lên xuống phía Nam của Ga Chùa Hà trên mặt đường Cầu Giấy.",
        "apartments": [
            {"apt_id": "FLC-1903", "tower": "Res Tower", "floor": 19, "area_m2": 92.0, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 76.5, "listing_date": "2026-09"},
            {"apt_id": "FLC-2708", "tower": "Res Tower", "floor": 27, "area_m2": 110.0, "bedrooms": 3, "direction": "Bắc", "asking_price_m2": 78.2, "listing_date": "2026-10"},
            {"apt_id": "FLC-1405", "tower": "Res Tower", "floor": 14, "area_m2": 97.0, "bedrooms": 2, "direction": "Tây Nam", "asking_price_m2": 74.8, "listing_date": "2026-10"},
            {"apt_id": "FLC-3310", "tower": "Res Tower", "floor": 33, "area_m2": 125.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 79.5, "listing_date": "2026-11"},
            {"apt_id": "FLC-2201", "tower": "Res Tower", "floor": 22, "area_m2": 92.0, "bedrooms": 2, "direction": "Đông", "asking_price_m2": 77.0, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-04",
        "name": "TNR Goldmark City (136 Hồ Tùng Mậu)",
        "district": "Bắc Từ Liêm",
        "ward": "Phú Diễn",
        "segment": "Trung - Cao cấp",
        "handover_year": 2017,
        "total_floors": 40,
        "lat": 21.03820,
        "lon": 105.76620,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 8,
        "nearest_station_code": "T3-S04",
        "bus_stops_500m": 4,
        "nearest_bus_m": 210,
        "dist_cbd_km": 8.4,
        # Minh họa điển hình Gap G1: Đường chim bay sang Ga Cầu Diễn/Lê Đức Thọ rất gần,
        # nhưng thực tế đi bộ phải ra cổng 136 Hồ Tùng Mậu rồi đi dọc theo vỉa hè Hồ Tùng Mậu!
        "walking_waypoints": [
            (21.03820, 105.76620),
            (21.03965, 105.76695),
            (21.04020, 105.76520),
            (21.04111, 105.76278),
        ],
        "barrier_note": "Khu đô thị khép kín và bị chắn bởi khuôn viên phía Đông; người đi bộ phải đi ra cổng chính 136 Hồ Tùng Mậu rồi rẽ dọc trục Hồ Tùng Mậu tới Ga Cầu Diễn.",
        "apartments": [
            {"apt_id": "GM-R2-1608", "tower": "Ruby 2", "floor": 16, "area_m2": 78.5, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 68.5, "listing_date": "2026-09"},
            {"apt_id": "GM-R4-2512", "tower": "Ruby 4", "floor": 25, "area_m2": 104.0, "bedrooms": 3, "direction": "Bắc", "asking_price_m2": 70.2, "listing_date": "2026-10"},
            {"apt_id": "GM-S1-1204", "tower": "Sapphire 1", "floor": 12, "area_m2": 83.0, "bedrooms": 2, "direction": "Nam", "asking_price_m2": 69.0, "listing_date": "2026-10"},
            {"apt_id": "GM-S3-3109", "tower": "Sapphire 3", "floor": 31, "area_m2": 114.5, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 72.0, "listing_date": "2026-10"},
            {"apt_id": "GM-R1-0905", "tower": "Ruby 1", "floor": 9, "area_m2": 74.5, "bedrooms": 2, "direction": "Tây Bắc", "asking_price_m2": 66.8, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-05",
        "name": "The Zei Mỹ Đình (Số 8 Lê Đức Thọ)",
        "district": "Nam Từ Liêm",
        "ward": "Mỹ Đình 2",
        "segment": "Cao cấp (High-end)",
        "handover_year": 2021,
        "total_floors": 42,
        "lat": 21.03320,
        "lon": 105.76860,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 5,
        "nearest_station_code": "T3-S05",
        "bus_stops_500m": 5,
        "nearest_bus_m": 90,
        "dist_cbd_km": 8.1,
        # Đi bộ dọc Lê Đức Thọ lên nút giao Hồ Tùng Mậu rồi rẽ phải tới Ga Lê Đức Thọ
        "walking_waypoints": [
            (21.03320, 105.76860),
            (21.03520, 105.76955),
            (21.03735, 105.77050),
            (21.03806, 105.77306),
        ],
        "barrier_note": "Đường chim bay cắt chéo qua khu dân cư Mai Dịch và hồ điều hòa; đi bộ thực tế phải theo trục Lê Đức Thọ – Hồ Tùng Mậu.",
        "apartments": [
            {"apt_id": "ZEI-1810", "tower": "Tòa đơn", "floor": 18, "area_m2": 89.0, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 84.5, "listing_date": "2026-09"},
            {"apt_id": "ZEI-2904", "tower": "Tòa đơn", "floor": 29, "area_m2": 105.0, "bedrooms": 3, "direction": "Đông Bắc", "asking_price_m2": 87.0, "listing_date": "2026-10"},
            {"apt_id": "ZEI-1208", "tower": "Tòa đơn", "floor": 12, "area_m2": 84.0, "bedrooms": 2, "direction": "Tây Nam", "asking_price_m2": 82.0, "listing_date": "2026-10"},
            {"apt_id": "ZEI-3602", "tower": "Tòa đơn", "floor": 36, "area_m2": 108.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 88.5, "listing_date": "2026-11"},
            {"apt_id": "ZEI-2411", "tower": "Tòa đơn", "floor": 24, "area_m2": 94.0, "bedrooms": 2, "direction": "Nam", "asking_price_m2": 85.2, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-06",
        "name": "Sun Square (21 Lê Đức Thọ)",
        "district": "Nam Từ Liêm",
        "ward": "Mỹ Đình 2",
        "segment": "Trung cấp (Mid-end)",
        "handover_year": 2017,
        "total_floors": 34,
        "lat": 21.03240,
        "lon": 105.76750,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 6,
        "nearest_station_code": "T3-S05",
        "bus_stops_500m": 5,
        "nearest_bus_m": 70,
        "dist_cbd_km": 8.2,
        "walking_waypoints": [
            (21.03240, 105.76750),
            (21.03320, 105.76860),
            (21.03735, 105.77050),
            (21.03806, 105.77306),
        ],
        "barrier_note": "Đi bộ dọc trục Lê Đức Thọ lên ngã ba Hồ Tùng Mậu rồi rẽ phải tới Ga Lê Đức Thọ.",
        "apartments": [
            {"apt_id": "SSQ-A1502", "tower": "Tháp A", "floor": 15, "area_m2": 85.0, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 67.5, "listing_date": "2026-09"},
            {"apt_id": "SSQ-B2206", "tower": "Tháp B", "floor": 22, "area_m2": 107.0, "bedrooms": 3, "direction": "Đông Bắc", "asking_price_m2": 69.0, "listing_date": "2026-10"},
            {"apt_id": "SSQ-A1008", "tower": "Tháp A", "floor": 10, "area_m2": 93.0, "bedrooms": 3, "direction": "Nam", "asking_price_m2": 66.2, "listing_date": "2026-10"},
            {"apt_id": "SSQ-B2801", "tower": "Tháp B", "floor": 28, "area_m2": 115.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 70.4, "listing_date": "2026-11"},
            {"apt_id": "SSQ-A1904", "tower": "Tháp A", "floor": 19, "area_m2": 85.0, "bedrooms": 2, "direction": "Đông", "asking_price_m2": 68.0, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-07",
        "name": "Dolphin Plaza (6 Nguyễn Hoàng / 28 Trần Bình)",
        "district": "Nam Từ Liêm",
        "ward": "Mỹ Đình 2",
        "segment": "Cao cấp (High-end)",
        "handover_year": 2012,
        "total_floors": 28,
        "lat": 21.03110,
        "lon": 105.77660,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 6,
        "nearest_station_code": "T3-S06",
        "bus_stops_500m": 7,
        "nearest_bus_m": 150,
        "dist_cbd_km": 7.3,
        # Minh họa cực rõ Gap G1: Đường chim bay tới Ga ĐHQG hoặc Ga Lê Đức Thọ chỉ ~850m,
        # nhưng bị chắn bởi nút giao cầu vượt Mai Dịch & Vành đai 3 trên cao, đi bộ phải qua phố Trần Bình -> Hồ Tùng Mậu!
        "walking_waypoints": [
            (21.03110, 105.77660),
            (21.03380, 105.77690),
            (21.03650, 105.77985),
            (21.03667, 105.78278),
        ],
        "barrier_note": "Bị ngăn cách bởi nút giao cầu vượt Mai Dịch và đường Vành đai 3 trên cao (Phạm Hùng). Người đi bộ phải vòng qua phố Trần Bình và cầu vượt bộ hành Mai Dịch.",
        "apartments": [
            {"apt_id": "DP-T1-1402", "tower": "Tháp 1", "floor": 14, "area_m2": 132.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 69.5, "listing_date": "2026-09"},
            {"apt_id": "DP-T2-2005", "tower": "Tháp 2", "floor": 20, "area_m2": 144.0, "bedrooms": 3, "direction": "Nam", "asking_price_m2": 71.0, "listing_date": "2026-10"},
            {"apt_id": "DP-T3-1108", "tower": "Tháp 3", "floor": 11, "area_m2": 138.0, "bedrooms": 3, "direction": "Đông Bắc", "asking_price_m2": 68.0, "listing_date": "2026-10"},
            {"apt_id": "DP-T4-2301", "tower": "Tháp 4", "floor": 23, "area_m2": 156.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 72.2, "listing_date": "2026-11"},
            {"apt_id": "DP-T2-1604", "tower": "Tháp 2", "floor": 16, "area_m2": 132.0, "bedrooms": 3, "direction": "Đông", "asking_price_m2": 70.1, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-08",
        "name": "Vinhomes Gardenia - The Arcadia (Hàm Nghi)",
        "district": "Nam Từ Liêm",
        "ward": "Cầu Diễn",
        "segment": "Cao cấp (High-end)",
        "handover_year": 2017,
        "total_floors": 39,
        "lat": 21.03510,
        "lon": 105.75950,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 8,
        "nearest_station_code": "T3-S04",
        "bus_stops_500m": 4,
        "nearest_bus_m": 180,
        "dist_cbd_km": 8.9,
        "walking_waypoints": [
            (21.03510, 105.75950),
            (21.03780, 105.76050),
            (21.04050, 105.76180),
            (21.04111, 105.76278),
        ],
        "barrier_note": "Đi bộ từ phân khu cao tầng The Arcadia qua đường nội khu Hoàng Hoa Thám / Nguyễn Văn Giáp nối ra đường Cầu Diễn tới Ga Cầu Diễn.",
        "apartments": [
            {"apt_id": "VG-A1-1709", "tower": "Arcadia A1", "floor": 17, "area_m2": 84.0, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 76.0, "listing_date": "2026-09"},
            {"apt_id": "VG-A2-2612", "tower": "Arcadia A2", "floor": 26, "area_m2": 102.5, "bedrooms": 3, "direction": "Đông Bắc", "asking_price_m2": 78.5, "listing_date": "2026-10"},
            {"apt_id": "VG-A3-1205", "tower": "Arcadia A3", "floor": 12, "area_m2": 78.0, "bedrooms": 2, "direction": "Tây Nam", "asking_price_m2": 74.2, "listing_date": "2026-10"},
            {"apt_id": "VG-A3-3210", "tower": "Arcadia A3", "floor": 32, "area_m2": 116.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 80.0, "listing_date": "2026-11"},
            {"apt_id": "VG-A1-2103", "tower": "Arcadia A1", "floor": 21, "area_m2": 86.5, "bedrooms": 2, "direction": "Nam", "asking_price_m2": 77.2, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-09",
        "name": "Iris Garden (30 Trần Hữu Dực)",
        "district": "Nam Từ Liêm",
        "ward": "Cầu Diễn",
        "segment": "Trung cấp (Mid-end)",
        "handover_year": 2020,
        "total_floors": 29,
        "lat": 21.03150,
        "lon": 105.76180,
        "geocoding_tier": "Tier 2: Approximate Street-level (Cần xác minh tòa)",
        "geocoding_error_m": 45,
        "nearest_station_code": "T3-S04",
        "bus_stops_500m": 4,
        "nearest_bus_m": 120,
        "dist_cbd_km": 8.8,
        "walking_waypoints": [
            (21.03150, 105.76180),
            (21.03240, 105.76750),
            (21.03735, 105.77050),
            (21.04111, 105.76278),
        ],
        "barrier_note": "Minh họa quan sát có Geocoding Tier 2 (chỉ có địa chỉ đường Trần Hữu Dực trên tin đăng) và hệ số đi vòng cao do phải vòng qua trục Lê Đức Thọ / KĐT Mỹ Đình.",
        "apartments": [
            {"apt_id": "IG-CT2-1104", "tower": "CT2", "floor": 11, "area_m2": 61.0, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 63.0, "listing_date": "2026-09"},
            {"apt_id": "IG-CT3-1809", "tower": "CT3", "floor": 18, "area_m2": 103.0, "bedrooms": 3, "direction": "Đông Bắc", "asking_price_m2": 64.5, "listing_date": "2026-10"},
            {"apt_id": "IG-CT1-0802", "tower": "CT1", "floor": 8, "area_m2": 61.0, "bedrooms": 2, "direction": "Tây Nam", "asking_price_m2": 61.8, "listing_date": "2026-10"},
            {"apt_id": "IG-CT4-2306", "tower": "CT4", "floor": 23, "area_m2": 115.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 65.5, "listing_date": "2026-11"},
            {"apt_id": "IG-CT2-1510", "tower": "CT2", "floor": 15, "area_m2": 66.0, "bedrooms": 2, "direction": "Nam", "asking_price_m2": 63.8, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-10",
        "name": "Sky Park Residence (Số 3 Tôn Thất Thuyết)",
        "district": "Cầu Giấy",
        "ward": "Dịch Vọng Hậu",
        "segment": "Cao cấp (High-end)",
        "handover_year": 2018,
        "total_floors": 37,
        "lat": 21.02680,
        "lon": 105.78520,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 6,
        "nearest_station_code": "T3-S06",
        "bus_stops_500m": 6,
        "nearest_bus_m": 95,
        "dist_cbd_km": 6.4,
        "walking_waypoints": [
            (21.02680, 105.78520),
            (21.02980, 105.78560),
            (21.03350, 105.78320),
            (21.03667, 105.78278),
        ],
        "barrier_note": "Đi bộ qua trục Trần Thái Tông – Xuân Thủy lên Ga Đại học Quốc gia (ngoài vùng đi bộ 10 phút, phụ thuộc nhiều hơn vào xe buýt và trục Vành đai 3).",
        "apartments": [
            {"apt_id": "SKP-A1604", "tower": "Tháp A", "floor": 16, "area_m2": 71.5, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 78.0, "listing_date": "2026-09"},
            {"apt_id": "SKP-B2408", "tower": "Tháp B", "floor": 24, "area_m2": 86.0, "bedrooms": 2, "direction": "Bắc", "asking_price_m2": 80.5, "listing_date": "2026-10"},
            {"apt_id": "SKP-A1210", "tower": "Tháp A", "floor": 12, "area_m2": 79.0, "bedrooms": 2, "direction": "Nam", "asking_price_m2": 77.2, "listing_date": "2026-10"},
            {"apt_id": "SKP-B3102", "tower": "Tháp B", "floor": 31, "area_m2": 128.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 82.0, "listing_date": "2026-11"},
            {"apt_id": "SKP-A2006", "tower": "Tháp A", "floor": 20, "area_m2": 86.0, "bedrooms": 2, "direction": "Đông", "asking_price_m2": 79.4, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-11",
        "name": "Vinhomes Skylake (Phạm Hùng - Hồ Cầu Giấy)",
        "district": "Nam Từ Liêm",
        "ward": "Mỹ Đình 1",
        "segment": "Cao cấp - Hạng sang",
        "handover_year": 2019,
        "total_floors": 42,
        "lat": 21.02250,
        "lon": 105.78180,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 6,
        "nearest_station_code": "T3-S06",
        "bus_stops_500m": 6,
        "nearest_bus_m": 110,
        "dist_cbd_km": 6.9,
        "walking_waypoints": [
            (21.02250, 105.78180),
            (21.02850, 105.77950),
            (21.03650, 105.77985),
            (21.03667, 105.78278),
        ],
        "barrier_note": "Minh họa hiệu ứng biến bị bỏ sót (Omitted Variable Bias / Amenity Effect): cách xa Ga Metro (>1.8km đi bộ) nhưng giá rất cao nhờ sát Công viên Hồ điều hòa Cầu Giấy 32ha -> Phần dư mô hình thuần tiếp cận giao thông sẽ dương cao nếu không kiểm soát biến Công viên.",
        "apartments": [
            {"apt_id": "VSL-S1-1805", "tower": "Tòa S1", "floor": 18, "area_m2": 75.0, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 92.0, "listing_date": "2026-09"},
            {"apt_id": "VSL-S2-2910", "tower": "Tòa S2", "floor": 29, "area_m2": 101.0, "bedrooms": 3, "direction": "Đông Bắc (View Hồ)", "asking_price_m2": 98.5, "listing_date": "2026-10"},
            {"apt_id": "VSL-S3-1408", "tower": "Tòa S3", "floor": 14, "area_m2": 68.0, "bedrooms": 2, "direction": "Tây Nam", "asking_price_m2": 89.0, "listing_date": "2026-10"},
            {"apt_id": "VSL-S2-3602", "tower": "Tòa S2", "floor": 36, "area_m2": 133.0, "bedrooms": 3, "direction": "Đông Nam (View Hồ)", "asking_price_m2": 102.0, "listing_date": "2026-11"},
            {"apt_id": "VSL-S3-2211", "tower": "Tòa S3", "floor": 22, "area_m2": 95.0, "bedrooms": 3, "direction": "Đông", "asking_price_m2": 94.5, "listing_date": "2026-11"},
        ],
    },
    {
        "project_id": "PRJ-12",
        "name": "The Matrix One (Ngã tư Lê Quang Đạo - Mễ Trì)",
        "district": "Nam Từ Liêm",
        "ward": "Mễ Trì",
        "segment": "Cao cấp - Hạng sang",
        "handover_year": 2021,
        "total_floors": 44,
        "lat": 21.01520,
        "lon": 105.76950,
        "geocoding_tier": "Tier 1: Exact Building Rooftop",
        "geocoding_error_m": 5,
        "nearest_station_code": "T3-S05",
        "bus_stops_500m": 5,
        "nearest_bus_m": 85,
        "dist_cbd_km": 8.5,
        "walking_waypoints": [
            (21.01520, 105.76950),
            (21.02056, 105.76550),
            (21.03240, 105.76750),
            (21.03735, 105.77050),
            (21.03806, 105.77306),
        ],
        "barrier_note": "Nằm tại khu vực Sân vận động Quốc gia Mỹ Đình (ngoài vùng phục vụ đi bộ của Tuyến Metro số 3, cách >2,7km); đóng vai trò nhóm đối chứng không gian (Control zone) trong phân tích Hedonic.",
        "apartments": [
            {"apt_id": "TMO-A2106", "tower": "Tháp A", "floor": 21, "area_m2": 87.5, "bedrooms": 2, "direction": "Đông Nam", "asking_price_m2": 95.0, "listing_date": "2026-09"},
            {"apt_id": "TMO-B3208", "tower": "Tháp B", "floor": 32, "area_m2": 112.0, "bedrooms": 3, "direction": "Tây Bắc (View Công viên)", "asking_price_m2": 99.0, "listing_date": "2026-10"},
            {"apt_id": "TMO-A1504", "tower": "Tháp A", "floor": 15, "area_m2": 86.0, "bedrooms": 2, "direction": "Đông Bắc", "asking_price_m2": 92.5, "listing_date": "2026-10"},
            {"apt_id": "TMO-B3801", "tower": "Tháp B", "floor": 38, "area_m2": 114.0, "bedrooms": 3, "direction": "Đông Nam", "asking_price_m2": 101.5, "listing_date": "2026-11"},
            {"apt_id": "TMO-A2510", "tower": "Tháp A", "floor": 25, "area_m2": 88.0, "bedrooms": 2, "direction": "Nam", "asking_price_m2": 96.2, "listing_date": "2026-11"},
        ],
    },
]


# Bảng ánh xạ Định danh Không gian 3 Tầng (3-Tier Spatial Identification Strategy)
# xử lý cải cách hành chính bỏ cấp quận/huyện sang mô hình chính quyền địa phương 2 cấp (Thành phố -> Phường/Xã mới)
THREE_TIER_SPATIAL_MAP = {
    "PRJ-01": {
        "urban_ring_sector": "UZ2: Vành đai 2–3 (Nội đô phát triển)",
        "new_ward_2level": "Phường Cầu Giấy, TP. Hà Nội (HN_W07)",
        "historical_submarket": "Tiểu thị trường Cầu Giấy (Dịch Vọng cũ)",
    },
    "PRJ-02": {
        "urban_ring_sector": "UZ2: Vành đai 2–3 (Nội đô phát triển)",
        "new_ward_2level": "Phường Cầu Giấy, TP. Hà Nội (HN_W07)",
        "historical_submarket": "Tiểu thị trường Cầu Giấy (Dịch Vọng Hậu cũ)",
    },
    "PRJ-03": {
        "urban_ring_sector": "UZ2: Vành đai 2–3 (Nội đô phát triển)",
        "new_ward_2level": "Phường Cầu Giấy, TP. Hà Nội (HN_W07)",
        "historical_submarket": "Tiểu thị trường Cầu Giấy (Dịch Vọng cũ)",
    },
    "PRJ-04": {
        "urban_ring_sector": "UZ3: Vành đai 3–3.5 (Hành lang phía Tây)",
        "new_ward_2level": "Phường Phú Diễn, TP. Hà Nội (HN_W13)",
        "historical_submarket": "Tiểu thị trường Bắc Từ Liêm (Phú Diễn cũ)",
    },
    "PRJ-05": {
        "urban_ring_sector": "UZ3: Vành đai 3–3.5 (Hành lang phía Tây)",
        "new_ward_2level": "Phường Từ Liêm, TP. Hà Nội (HN_W16)",
        "historical_submarket": "Tiểu thị trường Nam Từ Liêm (Mỹ Đình 2 cũ)",
    },
    "PRJ-06": {
        "urban_ring_sector": "UZ3: Vành đai 3–3.5 (Hành lang phía Tây)",
        "new_ward_2level": "Phường Từ Liêm, TP. Hà Nội (HN_W16)",
        "historical_submarket": "Tiểu thị trường Nam Từ Liêm (Mỹ Đình 2 cũ)",
    },
    "PRJ-07": {
        "urban_ring_sector": "UZ3: Vành đai 3–3.5 (Hành lang phía Tây)",
        "new_ward_2level": "Phường Từ Liêm, TP. Hà Nội (HN_W16)",
        "historical_submarket": "Tiểu thị trường Nam Từ Liêm (Mỹ Đình 2 cũ)",
    },
    "PRJ-08": {
        "urban_ring_sector": "UZ3: Vành đai 3–3.5 (Hành lang phía Tây)",
        "new_ward_2level": "Phường Từ Liêm, TP. Hà Nội (HN_W16)",
        "historical_submarket": "Tiểu thị trường Nam Từ Liêm (Cầu Diễn cũ)",
    },
    "PRJ-09": {
        "urban_ring_sector": "UZ3: Vành đai 3–3.5 (Hành lang phía Tây)",
        "new_ward_2level": "Phường Từ Liêm, TP. Hà Nội (HN_W16)",
        "historical_submarket": "Tiểu thị trường Nam Từ Liêm (Cầu Diễn cũ)",
    },
    "PRJ-10": {
        "urban_ring_sector": "UZ2: Vành đai 2–3 (Nội đô phát triển)",
        "new_ward_2level": "Phường Cầu Giấy, TP. Hà Nội (HN_W07)",
        "historical_submarket": "Tiểu thị trường Cầu Giấy (Dịch Vọng Hậu cũ)",
    },
    "PRJ-11": {
        "urban_ring_sector": "UZ3: Vành đai 3–3.5 (Hành lang phía Tây)",
        "new_ward_2level": "Phường Từ Liêm, TP. Hà Nội (HN_W16)",
        "historical_submarket": "Tiểu thị trường Nam Từ Liêm (Mỹ Đình 1 cũ)",
    },
    "PRJ-12": {
        "urban_ring_sector": "UZ3: Vành đai 3–3.5 (Hành lang phía Tây)",
        "new_ward_2level": "Phường Mễ Trì, TP. Hà Nội (HN_W18)",
        "historical_submarket": "Tiểu thị trường Nam Từ Liêm (Mễ Trì cũ)",
    },
}


# ==============================================================================
# 3. HÀM TÍNH KHOẢNG CÁCH ĐỊA LÝ & HỒI QUY KINH TẾ LƯỢNG HEDONIC (OLS + CLUSTER SE)
# ==============================================================================
def haversine_m(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Tính khoảng cách đường chim bay (Euclidean trên mặt cầu WGS84) theo đơn vị mét."""
    r = 6371000.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0) ** 2
    return 2.0 * r * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))


def polyline_length_m(waypoints: list[tuple[float, float]]) -> float:
    """Tính tổng chiều dài tuyến đường đi bộ theo danh sách tọa độ (mét)."""
    total = 0.0
    for i in range(len(waypoints) - 1):
        total += haversine_m(waypoints[i][0], waypoints[i][1], waypoints[i + 1][0], waypoints[i + 1][1])
    return total


def run_hedonic_models(projects: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Chạy 2 mô hình Hedonic Pricing thực tế trên toàn bộ 60 quan sát căn hộ:
    - Model E0 (Euclidean Distance): ln(TotalPrice) ~ ln(d_Euclidean) + ln(Area) + Floor + Bus500m + DistCBD + HighEndDummy
    - Model E1 (Network Walking Distance - Chính): ln(TotalPrice) ~ ln(d_Network) + ln(Area) + Floor + Bus500m + DistCBD + HighEndDummy
    Tính cả sai số chuẩn phân cụm theo dự án (Clustered Standard Errors by Project)
    và gắn đầy đủ 3 tầng định danh không gian (3-Tier Spatial Identification).
    """
    stations_by_code = {s["code"]: s for s in METRO_STATIONS}

    rows = []
    for prj in projects:
        tier_info = THREE_TIER_SPATIAL_MAP[prj["project_id"]]
        prj["urban_ring_sector"] = tier_info["urban_ring_sector"]
        prj["new_ward_2level"] = tier_info["new_ward_2level"]
        prj["historical_submarket"] = tier_info["historical_submarket"]

        st = stations_by_code[prj["nearest_station_code"]]
        d_euc = haversine_m(prj["lat"], prj["lon"], st["lat"], st["lon"])
        # Nhân hệ số vi mô vỉa hè/cầu thang lên ga (1.08) để phản ánh đúng chiều dài đi bộ thực tế
        d_net = polyline_length_m(prj["walking_waypoints"]) * 1.08
        if d_net < d_euc * 1.05:
            d_net = d_euc * 1.12
        detour_ratio = d_net / max(d_euc, 1.0)
        walk_time_min = d_net / 80.0  # Tốc độ đi bộ chuẩn đô thị: 80m/phút (4.8 km/h)

        prj["d_euclidean_m"] = round(d_euc, 1)
        prj["d_network_m"] = round(d_net, 1)
        prj["detour_ratio"] = round(detour_ratio, 2)
        prj["walk_time_min"] = round(walk_time_min, 1)
        prj["nearest_station_name"] = st["name"]
        prj["nearest_station_lat"] = st["lat"]
        prj["nearest_station_lon"] = st["lon"]
        prj["nearest_station_status"] = st["status_label"]

        is_high_end = 1.0 if ("Cao cấp" in prj["segment"]) else 0.0
        is_ultra_luxury = 1.0 if ("Hạng sang" in prj["segment"]) else 0.0

        for apt in prj["apartments"]:
            total_price_billion = (apt["asking_price_m2"] * apt["area_m2"]) / 1000.0
            apt["total_price_billion"] = round(total_price_billion, 2)
            rows.append(
                {
                    "project_id": prj["project_id"],
                    "apt_ref": apt,
                    "prj_ref": prj,
                    "ln_total_price": math.log(total_price_billion),
                    "ln_price_m2": math.log(apt["asking_price_m2"]),
                    "ln_d_euc": math.log(d_euc),
                    "ln_d_net": math.log(d_net),
                    "ln_area": math.log(apt["area_m2"]),
                    "floor": float(apt["floor"]),
                    "bus_stops": float(prj["bus_stops_500m"]),
                    "dist_cbd": float(prj["dist_cbd_km"]),
                    "is_high_end": is_high_end,
                    "is_ultra_luxury": is_ultra_luxury,
                }
            )

    n = len(rows)
    y = np.array([r["ln_total_price"] for r in rows])

    # Ma trận thiết kế X cho Model E1 (Network Distance) và Model E0 (Euclidean Distance)
    X_net = np.column_stack(
        [
            np.ones(n),
            np.array([r["ln_d_net"] for r in rows]),
            np.array([r["ln_area"] for r in rows]),
            np.array([r["floor"] for r in rows]),
            np.array([r["bus_stops"] for r in rows]),
            np.array([r["dist_cbd"] for r in rows]),
            np.array([r["is_high_end"] for r in rows]),
            np.array([r["is_ultra_luxury"] for r in rows]),
        ]
    )
    X_euc = np.column_stack(
        [
            np.ones(n),
            np.array([r["ln_d_euc"] for r in rows]),
            np.array([r["ln_area"] for r in rows]),
            np.array([r["floor"] for r in rows]),
            np.array([r["bus_stops"] for r in rows]),
            np.array([r["dist_cbd"] for r in rows]),
            np.array([r["is_high_end"] for r in rows]),
            np.array([r["is_ultra_luxury"] for r in rows]),
        ]
    )

    def fit_ols_clustered(X: np.ndarray, y_vec: np.ndarray, cluster_ids: list[str]) -> dict[str, Any]:
        k = X.shape[1]
        xtx_inv = np.linalg.inv(X.T @ X)
        beta = xtx_inv @ (X.T @ y_vec)
        y_hat = X @ beta
        resid = y_vec - y_hat
        tss = float(np.sum((y_vec - np.mean(y_vec)) ** 2))
        rss = float(np.sum(resid**2))
        r2 = 1.0 - rss / tss
        adj_r2 = 1.0 - (1.0 - r2) * (n - 1) / (n - k)

        # Clustered sandwich variance estimator (Cameron & Miller, 2015)
        unique_clusters = sorted(set(cluster_ids))
        g = len(unique_clusters)
        meat = np.zeros((k, k))
        for cid in unique_clusters:
            idx = [i for i, c in enumerate(cluster_ids) if c == cid]
            Xg = X[idx, :]
            eg = resid[idx]
            score_g = Xg.T @ eg
            meat += np.outer(score_g, score_g)
        # Small-sample correction factor: (G / (G - 1)) * ((N - 1) / (N - K))
        dfc = (g / (g - 1.0)) * ((n - 1.0) / (n - k))
        vcov_cl = dfc * (xtx_inv @ meat @ xtx_inv)
        se_cl = np.sqrt(np.diag(vcov_cl))
        return {
            "beta": beta,
            "se_cl": se_cl,
            "y_hat": y_hat,
            "resid": resid,
            "r2": r2,
            "adj_r2": adj_r2,
            "n": n,
            "g": g,
        }

    cluster_ids = [r["project_id"] for r in rows]
    res_net = fit_ols_clustered(X_net, y, cluster_ids)
    res_euc = fit_ols_clustered(X_euc, y, cluster_ids)

    # Gán giá trị dự báo và phần dư về từng căn hộ & tổng hợp theo từng dự án
    mean_ln_d_net = float(np.mean([r["ln_d_net"] for r in rows]))
    beta_net_transit = float(res_net["beta"][1])

    for i, r in enumerate(rows):
        apt = r["apt_ref"]
        pred_total_billion = math.exp(float(res_net["y_hat"][i]))
        pred_price_m2 = (pred_total_billion * 1000.0) / apt["area_m2"]
        resid_pct = (math.exp(float(res_net["resid"][i])) - 1.0) * 100.0
        # Đóng góp biên của tiếp cận Metro so với mức trung bình mẫu (%)
        transit_premium_pct = (math.exp(beta_net_transit * (r["ln_d_net"] - mean_ln_d_net)) - 1.0) * 100.0

        apt["pred_price_m2"] = round(pred_price_m2, 1)
        apt["pred_total_billion"] = round(pred_total_billion, 2)
        apt["residual_pct"] = round(resid_pct, 2)
        apt["transit_premium_pct"] = round(transit_premium_pct, 2)

    for prj in projects:
        apts = prj["apartments"]
        prices = [a["asking_price_m2"] for a in apts]
        preds = [a["pred_price_m2"] for a in apts]
        resids = [a["residual_pct"] for a in apts]
        areas = [a["area_m2"] for a in apts]

        prj["n_listings"] = len(apts)
        prj["mean_price_m2"] = round(float(np.mean(prices)), 1)
        prj["median_price_m2"] = round(float(np.median(prices)), 1)
        prj["min_price_m2"] = round(float(np.min(prices)), 1)
        prj["max_price_m2"] = round(float(np.max(prices)), 1)
        prj["mean_pred_price_m2"] = round(float(np.mean(preds)), 1)
        prj["mean_residual_pct"] = round(float(np.mean(resids)), 2)
        prj["mean_area_m2"] = round(float(np.mean(areas)), 1)
        prj["transit_premium_pct"] = apts[0]["transit_premium_pct"]

    return {
        "model_e1_network": res_net,
        "model_e0_euclidean": res_euc,
        "rows": rows,
    }


# ==============================================================================
# 4. HÀM DỰNG HÌNH HỌC ĐA GIÁC 3D & VÙNG ĐỆM ISOCHRONE TRONG KML
# ==============================================================================
def create_polygon_circle_coords(
    lat: float, lon: float, radius_m: float, num_points: int = 36, altitude_m: float = 0.0
) -> str:
    """Tạo chuỗi tọa độ KML 'lon,lat,alt' cho một đa giác tròn/đa giác đều bán kính radius_m."""
    coords = []
    lat_rad = math.radians(lat)
    m_per_deg_lat = 111132.92
    m_per_deg_lon = 111412.84 * math.cos(lat_rad)

    for i in range(num_points + 1):
        angle = 2.0 * math.pi * (i % num_points) / num_points
        dlat = (radius_m * math.sin(angle)) / m_per_deg_lat
        dlon = (radius_m * math.cos(angle)) / m_per_deg_lon
        coords.append(f"{lon + dlon:.6f},{lat + dlat:.6f},{altitude_m:.1f}")
    return " ".join(coords)


def create_dashed_line_segments(
    lat1: float, lon1: float, lat2: float, lon2: float, dash_len_m: float = 35.0, gap_len_m: float = 25.0
) -> list[tuple[tuple[float, float], tuple[float, float]]]:
    """
    Chia một đoạn thẳng nối (lat1, lon1) -> (lat2, lon2) thành các đoạn nét đứt (dashed segments)
    để hiển thị rõ nét đứt trên Google Earth Web (do KML chuẩn không hỗ trợ thuộc tính line-dash native).
    """
    total_m = haversine_m(lat1, lon1, lat2, lon2)
    if total_m <= dash_len_m:
        return [((lat1, lon1), (lat2, lon2))]

    segments = []
    step_m = dash_len_m + gap_len_m
    cur_m = 0.0
    while cur_m < total_m:
        end_m = min(cur_m + dash_len_m, total_m)
        t1 = cur_m / total_m
        t2 = end_m / total_m
        p1 = (lat1 + t1 * (lat2 - lat1), lon1 + t1 * (lon2 - lon1))
        p2 = (lat1 + t2 * (lat2 - lat1), lon1 + t2 * (lon2 - lon1))
        segments.append((p1, p2))
        cur_m += step_m
    return segments


# ==============================================================================
# 5. THIẾT KẾ THẺ POPUP HTML KHOA HỌC (RESEARCH SCORECARD) KHI ẤN VÀO DỰ ÁN / GA
# ==============================================================================
def build_project_popup_html(prj: dict[str, Any], model_summary: dict[str, Any]) -> str:
    """Tạo giao diện thẻ kết quả nghiên cứu (HTML) hiển thị trong Google Earth khi click vào tòa chung cư."""
    res_net = model_summary["model_e1_network"]
    res_euc = model_summary["model_e0_euclidean"]

    beta_net = float(res_net["beta"][1])
    se_net = float(res_net["se_cl"][1])
    r2_net = float(res_net["r2"])
    r2_euc = float(res_euc["r2"])

    resid_val = prj["mean_residual_pct"]
    if resid_val > 1.5:
        resid_badge_bg = "#fef2f2"
        resid_badge_fg = "#b91c1c"
        resid_label = f"+{resid_val:.1f}% (Cao hơn dự báo Hedonic)"
    elif resid_val < -1.5:
        resid_badge_bg = "#eff6ff"
        resid_badge_fg = "#1d4ed8"
        resid_label = f"{resid_val:.1f}% (Thấp hơn dự báo Hedonic)"
    else:
        resid_badge_bg = "#f0fdf4"
        resid_badge_fg = "#15803d"
        resid_label = f"{resid_val:+.1f}% (Khớp sát dự báo Hedonic)"

    tp_val = prj["transit_premium_pct"]
    tp_color = "#15803d" if tp_val >= 0 else "#b45309"

    tier_is_exact = "Tier 1" in prj["geocoding_tier"]
    tier_bg = "#dcfce7" if tier_is_exact else "#fef3c7"
    tier_fg = "#166534" if tier_is_exact else "#92400e"

    # Tạo danh sách từng căn hộ bên trong tòa nhà bằng thẻ <div>/<p> (Google Earth Web Map Project
    # ẩn thẻ <table> thành "TABLE SECTION" và xóa background tối, nên dùng layout dòng trực quan trên nền sáng)
    apt_rows_html = []
    for idx, apt in enumerate(prj["apartments"], start=1):
        r_pct = apt["residual_pct"]
        if r_pct > 1.5:
            r_color = "#dc2626"
            r_tag = "Cao hơn dự báo"
        elif r_pct < -1.5:
            r_color = "#2563eb"
            r_tag = "Thấp hơn dự báo"
        else:
            r_color = "#15803d"
            r_tag = "Sát dự báo"

        apt_rows_html.append(
            f"""
            <div style="padding:6px 0;border-bottom:1px solid #cbd5e1;font-size:12px;color:#0f172a;">
              <div>
                <strong>{idx}. Mã căn {html.escape(apt["apt_id"])}</strong> ({html.escape(apt["tower"])} • Tầng {apt["floor"]} • {apt["bedrooms"]}PN • {apt["area_m2"]:.1f} m² • Hướng {html.escape(apt["direction"])})
              </div>
              <div style="margin-top:2px;color:#334155;">
                • Giá chào: <strong style="color:#dc2626;">{apt["asking_price_m2"]:.1f} tr/m²</strong> ({apt["total_price_billion"]:.2f} tỷ)
                | Dự báo Hedonic: <strong style="color:#0284c7;">{apt["pred_price_m2"]:.1f} tr/m²</strong>
                | Phần dư ε̂: <strong style="color:{r_color};">{r_pct:+.1f}% ({r_tag})</strong>
              </div>
            </div>
            """
        )

    return f"""
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0f172a;line-height:1.5;font-size:12.5px;">
      <div style="border-left:4px solid #d97706;padding-left:8px;margin-bottom:10px;font-size:11.5px;color:#92400e;">
        <strong>[B1 Research Demo — Synthetic Benchmark]:</strong> Tọa độ GIS của tòa nhà &amp; ga Metro là tọa độ thực (WGS84). Số liệu tin đăng bên dưới là bộ mẫu kiểm thử pipeline Hedonic (Mục VI.353 research_b1.md).
      </div>

      <div style="margin-bottom:10px;padding-bottom:8px;border-bottom:2px solid #cbd5e1;">
        <div style="font-size:11px;color:#475569;text-transform:uppercase;font-weight:700;">
          Mã cụm dự án: {html.escape(prj["project_id"])} • Chính quyền 2 cấp: {html.escape(prj["new_ward_2level"])} (Submarket lịch sử: {html.escape(prj["historical_submarket"])})
        </div>
        <div style="font-size:11px;color:#0284c7;font-weight:700;margin-top:2px;">
          🌐 Định danh Không gian 3 Tầng (Tầng 1): {html.escape(prj["urban_ring_sector"])}
        </div>
        <div style="font-size:16px;font-weight:800;margin:3px 0 6px 0;color:#0f172a;">
          🏢 {html.escape(prj["name"])}
        </div>
        <div style="font-size:12px;color:{tier_fg};font-weight:700;">
          📍 {html.escape(prj["geocoding_tier"])} (±{prj["geocoding_error_m"]}m) • Phân khúc: {html.escape(prj["segment"])} • Bàn giao: {prj["handover_year"]} ({prj["total_floors"]} tầng)
        </div>
      </div>

      <div style="margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid #cbd5e1;">
        <div style="font-size:13px;font-weight:700;color:#0f172a;margin-bottom:6px;">
          📊 1. Thống kê Giá chào bán &amp; Kết quả Mô hình Hedonic (N = {prj["n_listings"]} căn)
        </div>
        <div>• <strong>Giá chào bán trung bình (Observed):</strong> <span style="color:#dc2626;font-weight:700;">{prj["mean_price_m2"]:.1f} triệu/m²</span></div>
        <div>• <strong>Trung vị (Min – Max trong tòa):</strong> {prj["median_price_m2"]:.1f} triệu/m² ({prj["min_price_m2"]:.1f} – {prj["max_price_m2"]:.1f} tr/m²)</div>
        <div>• <strong>Giá dự báo Hedonic E1 (Predicted):</strong> <span style="color:#0284c7;font-weight:700;">{prj["mean_pred_price_m2"]:.1f} triệu/m²</span></div>
        <div>• <strong>Phần dư mô hình trung bình (Residual ε̂):</strong> <span style="color:{resid_badge_fg};font-weight:700;">{resid_label}</span></div>
        <div>• <strong>Đóng góp biên tiếp cận Metro (so với TB mẫu):</strong> <span style="color:{tp_color};font-weight:700;">{tp_val:+.2f}%</span></div>
      </div>

      <div style="margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid #cbd5e1;">
        <div style="font-size:13px;font-weight:700;color:#0369a1;margin-bottom:6px;">
          🚇 2. Chỉ tiêu Tiếp cận Giao thông Công cộng (GIS Accessibility — Gap G1 &amp; G2)
        </div>
        <div>• <strong>Ga Metro gần nhất:</strong> <span style="color:#0f172a;font-weight:700;">{html.escape(prj["nearest_station_name"])} ({html.escape(prj["nearest_station_code"])})</span></div>
        <div>• <strong>Trạng thái vận hành:</strong> <span style="color:#15803d;font-weight:700;">{html.escape(prj["nearest_station_status"])}</span></div>
        <div>• <strong>Khoảng cách chim bay (d_Euclidean):</strong> <strong>{prj["d_euclidean_m"]:.0f} m</strong> (Đường nét đứt)</div>
        <div>• <strong>Khoảng cách đi bộ thực tế (d_Network):</strong> <span style="color:#0284c7;font-weight:700;">{prj["d_network_m"]:.0f} m</span> (~{prj["walk_time_min"]:.1f} phút đi bộ)</div>
        <div>• <strong>Hệ số đi vòng (Detour Ratio = d_Net / d_Euc):</strong> <span style="color:#7c3aed;font-weight:700;">{prj["detour_ratio"]:.2f}x</span></div>
        <div>• <strong>Tiếp cận Xe buýt (Đa phương thức - Gap G2):</strong> Cách trạm gần nhất <strong>{prj["nearest_bus_m"]} m</strong> ({prj["bus_stops_500m"]} trạm trong bán kính 500m)</div>
        <div style="margin-top:5px;font-size:11.5px;color:#0c4a6e;">
          <em>💡 Giải thích không gian (GIS Note): {html.escape(prj["barrier_note"])}</em>
        </div>
      </div>

      <div style="margin-bottom:12px;padding-bottom:8px;border-bottom:1px solid #cbd5e1;">
        <div style="font-size:13px;font-weight:700;color:#0f172a;margin-bottom:4px;">
          🏠 3. Chi tiết từng Căn hộ chào bán trong tòa ({prj["n_listings"]} quan sát)
        </div>
        {"".join(apt_rows_html)}
      </div>

      <div style="font-size:11.5px;color:#334155;">
        <div style="font-weight:700;color:#0f172a;margin-bottom:3px;">
          📐 4. Tóm tắt Kiểm định Kinh tế lượng Đa Tầng (3-Tier Spatial Strategy — Thích ứng Bỏ Cấp Quận/Huyện):
        </div>
        <div>• <strong>Benchmark 3D (N = 60, G = 12):</strong> Model E1 (Network) β̂₁ = <strong>{beta_net:+.4f}</strong> (SE = {se_net:.4f}, R² = {r2_net:.4f}) vs. Model E0 (Euclidean) R² = {r2_euc:.4f}</div>
        <div>• <strong>Toàn mẫu Thực nghiệm (N = 16,471, Dải 500m–1,000m):</strong> M3 (Vành đai-Tọa độ) <strong>+3.61%***</strong> | M4 (Submarket lịch sử) <strong>+3.91%***</strong> | M5 (21 Phường/Xã 2 cấp) <strong>+3.73%***</strong> | M6 (Exact Rooftop) <strong>+3.90%***</strong></div>
        <div style="margin-top:4px;color:#475569;font-style:italic;">
          *Lưu ý phương pháp luận (Mục VIII.6 research_b1.md): Hệ số phản ánh mối liên hệ thống kê có điều kiện (conditional association) đối với giá chào bán, bất biến trước cải cách địa giới hành chính 2 cấp (kiểm định MAUP).*
        </div>
      </div>
    </div>
    """


def build_station_popup_html(st: dict[str, Any]) -> str:
    """Tạo thẻ HTML thông tin cho từng Nhà ga Metro (tương thích 100% Google Earth Web)."""
    is_op = st["status"] == "operational"
    fg_badge = "#15803d" if is_op else "#b45309"
    return f"""
    <div style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0f172a;line-height:1.5;font-size:12.5px;">
      <div style="margin-bottom:8px;padding-bottom:6px;border-bottom:2px solid #cbd5e1;">
        <div style="font-size:11px;color:#0369a1;text-transform:uppercase;font-weight:700;">{html.escape(st["line"])} • Mã ga: {html.escape(st["code"])}</div>
        <div style="font-size:16px;font-weight:800;margin:3px 0;color:#0f172a;">🚇 {html.escape(st["name"])}</div>
        <div style="font-size:12px;color:{fg_badge};font-weight:700;">
          ● Trạng thái: {html.escape(st["status_label"])}
        </div>
      </div>
      <div style="margin-bottom:8px;">
        <div>• <strong>Kết cấu nhà ga:</strong> {html.escape(st["structure"])}</div>
        <div>• <strong>Tọa độ WGS84:</strong> {st["lat"]:.5f}, {st["lon"]:.5f}</div>
        <div>• <strong>Tuyến xe buýt kết nối (Feeder Bus):</strong> <span style="color:#0369a1;font-weight:700;">{html.escape(st["feeder_bus"])}</span></div>
      </div>
      <div style="font-size:11.5px;color:#475569;border-left:3px solid #0284c7;padding-left:8px;">
        <strong>Quy tắc kiểm soát biến thời gian (Mục VII.4 research_b1.md):</strong> Phân biệt rõ nhà ga đang vận hành thương mại (từ 08/08/2024) và nhà ga ngầm đang thi công khi ước lượng hiệu ứng vốn hóa vào giá căn hộ.
      </div>
    </div>
    """


# ==============================================================================
# 6. HÀM XUẤT FILE KML ĐA LỚP CHUẨN GOOGLE EARTH WEB
# ==============================================================================
def generate_kml(projects: list[dict[str, Any]], model_summary: dict[str, Any]) -> str:
    """Tạo nội dung XML cho file KML với 5 Folders (Layers) bật/tắt độc lập."""

    # Bảng màu KML dùng hệ AABBGGRR (Alpha - Blue - Green - Red)
    styles_xml = """
    <!-- STYLE CHO DỰ ÁN THEO PHÂN KHÚC GIÁ / PHẦN DƯ -->
    <Style id="prj_high_price">
      <IconStyle>
        <color>ff2626dc</color>
        <scale>1.25</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/paddle/red-circle.png</href></Icon>
      </IconStyle>
      <LabelStyle><scale>0.95</scale><color>ffffffff</color></LabelStyle>
      <PolyStyle><color>b32626dc</color><fill>1</fill><outline>1</outline></PolyStyle>
      <LineStyle><color>ff1d1db9</color><width>2</width></LineStyle>
    </Style>

    <Style id="prj_mid_price">
      <IconStyle>
        <color>ff0088f5</color>
        <scale>1.2</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/paddle/ylw-circle.png</href></Icon>
      </IconStyle>
      <LabelStyle><scale>0.95</scale><color>ffffffff</color></LabelStyle>
      <PolyStyle><color>b30088f5</color><fill>1</fill><outline>1</outline></PolyStyle>
      <LineStyle><color>ff0066cc</color><width>2</width></LineStyle>
    </Style>

    <Style id="prj_affordable_price">
      <IconStyle>
        <color>ff4ade22</color>
        <scale>1.15</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/paddle/grn-circle.png</href></Icon>
      </IconStyle>
      <LabelStyle><scale>0.95</scale><color>ffffffff</color></LabelStyle>
      <PolyStyle><color>b34ade22</color><fill>1</fill><outline>1</outline></PolyStyle>
      <LineStyle><color>ff16a34a</color><width>2</width></LineStyle>
    </Style>

    <Style id="prj_tier2_approx">
      <IconStyle>
        <color>ff00b4f5</color>
        <scale>1.15</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/paddle/orange-blank.png</href></Icon>
      </IconStyle>
      <LabelStyle><scale>0.95</scale><color>ff80e5ff</color></LabelStyle>
      <PolyStyle><color>4000b4f5</color><fill>1</fill><outline>1</outline></PolyStyle>
      <LineStyle><color>ff00b4f5</color><width>2</width></LineStyle>
    </Style>

    <!-- STYLE CHO ĐƯỜNG ĐI BỘ THỰC TẾ VS ĐƯỜNG CHIM BAY (GAP G1) -->
    <Style id="route_walking_network">
      <LineStyle>
        <color>ffffd400</color>
        <width>4.5</width>
      </LineStyle>
    </Style>

    <Style id="route_euclidean_dashed">
      <LineStyle>
        <color>ff44e0ff</color>
        <width>2.5</width>
      </LineStyle>
    </Style>

    <!-- STYLE CHO TUYẾN & GA METRO / XE BUÝT (GAP G2) -->
    <Style id="metro_station_operational">
      <IconStyle>
        <color>ffff5500</color>
        <scale>1.3</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/shapes/rail.png</href></Icon>
      </IconStyle>
      <LabelStyle><scale>1.0</scale><color>ffffd580</color></LabelStyle>
    </Style>

    <Style id="metro_station_construction">
      <IconStyle>
        <color>ff94a3b8</color>
        <scale>1.1</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/shapes/rail.png</href></Icon>
      </IconStyle>
      <LabelStyle><scale>0.9</scale><color>ffcbd5e1</color></LabelStyle>
    </Style>

    <Style id="metro_line_operational">
      <LineStyle>
        <color>ff2626ef</color>
        <width>6</width>
      </LineStyle>
    </Style>

    <Style id="metro_line_underground">
      <LineStyle>
        <color>ff94a3b8</color>
        <width>4</width>
      </LineStyle>
    </Style>

    <Style id="bus_stop_style">
      <IconStyle>
        <color>ff38bdf8</color>
        <scale>0.85</scale>
        <Icon><href>http://maps.google.com/mapfiles/kml/shapes/bus.png</href></Icon>
      </IconStyle>
      <LabelStyle><scale>0.75</scale><color>ffbae6fd</color></LabelStyle>
    </Style>

    <!-- STYLE CHO VÙNG ĐỆM ĐI BỘ ISOCHRONE 5 - 10 PHÚT -->
    <Style id="iso_400m_5min">
      <LineStyle><color>cc4ade22</color><width>2</width></LineStyle>
      <PolyStyle><color>264ade22</color><fill>1</fill><outline>1</outline></PolyStyle>
    </Style>

    <Style id="iso_800m_10min">
      <LineStyle><color>ccffd400</color><width>1.5</width></LineStyle>
      <PolyStyle><color>18ffd400</color><fill>1</fill><outline>1</outline></PolyStyle>
    </Style>
    """

    # --------------------------------------------------------------------------
    # LAYER 1: TỔ HỢP DỰ ÁN CĂN HỘ & CỘT GIÁ 3D EXTRUSION
    # --------------------------------------------------------------------------
    layer1_items = []
    for prj in projects:
        mean_p = prj["mean_price_m2"]
        if "Tier 2" in prj["geocoding_tier"]:
            style_id = "#prj_tier2_approx"
        elif mean_p >= 85.0:
            style_id = "#prj_high_price"
        elif mean_p >= 70.0:
            style_id = "#prj_mid_price"
        else:
            style_id = "#prj_affordable_price"

        popup_html = build_project_popup_html(prj, model_summary)
        # Chiều cao cột 3D tỷ lệ với giá chào bán trung bình (1 triệu/m2 = 2.2m chiều cao cột 3D)
        col_height_m = round(mean_p * 2.2, 1)
        poly_coords = create_polygon_circle_coords(
            prj["lat"], prj["lon"], radius_m=24.0, num_points=16, altitude_m=col_height_m
        )

        # Nếu là Tier 2 (Approximate), vẽ thêm vòng tròn bán kính sai số 45m trên mặt đất
        uncertainty_xml = ""
        if "Tier 2" in prj["geocoding_tier"]:
            err_coords = create_polygon_circle_coords(
                prj["lat"], prj["lon"], radius_m=float(prj["geocoding_error_m"]), num_points=36, altitude_m=2.0
            )
            uncertainty_xml = f"""
            <Polygon>
              <extrude>0</extrude>
              <altitudeMode>relativeToGround</altitudeMode>
              <outerBoundaryIs><LinearRing><coordinates>{err_coords}</coordinates></LinearRing></outerBoundaryIs>
            </Polygon>
            """

        apt_ext_data = []
        for idx, apt in enumerate(prj["apartments"], start=1):
            apt_summary = (
                f"{apt['tower']} - Tầng {apt['floor']} ({apt['bedrooms']}PN, {apt['area_m2']:.1f}m², {apt['direction']}) | "
                f"Giá chào: {apt['asking_price_m2']:.1f} tr/m² ({apt['total_price_billion']:.2f} tỷ) | "
                f"Dự báo Hedonic: {apt['pred_price_m2']:.1f} tr/m² | Phần dư ε̂: {apt['residual_pct']:+.1f}%"
            )
            apt_ext_data.append(
                f'<Data name="can_ho_{idx}_{html.escape(apt["apt_id"])}"><value>{html.escape(apt_summary)}</value></Data>'
            )
        apt_ext_xml = "\n                ".join(apt_ext_data)

        layer1_items.append(
            f"""
            <Placemark id="{prj["project_id"]}">
              <name>{html.escape(prj["name"])} [{mean_p:.1f} tr/m² | ε̂={prj["mean_residual_pct"]:+.1f}%]</name>
              <visibility>1</visibility>
              <styleUrl>{style_id}</styleUrl>
              <LookAt>
                <longitude>{prj["lon"]:.6f}</longitude>
                <latitude>{prj["lat"]:.6f}</latitude>
                <altitude>0</altitude>
                <heading>-25</heading>
                <tilt>60</tilt>
                <range>850</range>
                <altitudeMode>relativeToGround</altitudeMode>
              </LookAt>
              <description><![CDATA[{popup_html}]]></description>
              <ExtendedData>
                <Data name="project_id"><value>{html.escape(prj["project_id"])} ({html.escape(prj["new_ward_2level"])})</value></Data>
                <Data name="urban_ring_sector"><value>{html.escape(prj["urban_ring_sector"])}</value></Data>
                <Data name="new_ward_2level"><value>{html.escape(prj["new_ward_2level"])}</value></Data>
                <Data name="historical_submarket"><value>{html.escape(prj["historical_submarket"])}</value></Data>
                <Data name="geocoding_tier"><value>{html.escape(prj["geocoding_tier"])} (±{prj["geocoding_error_m"]}m)</value></Data>
                <Data name="mean_asking_price_m2"><value>{prj["mean_price_m2"]:.1f} triệu/m² (Min-Max: {prj["min_price_m2"]:.1f}–{prj["max_price_m2"]:.1f})</value></Data>
                <Data name="hedonic_predicted_price_m2"><value>{prj["mean_pred_price_m2"]:.1f} triệu/m² (Model E1 Network)</value></Data>
                <Data name="hedonic_residual_pct"><value>{prj["mean_residual_pct"]:+.2f}% | Đóng góp biên Metro: {prj["transit_premium_pct"]:+.2f}%</value></Data>
                <Data name="nearest_station"><value>{html.escape(prj["nearest_station_name"])} ({html.escape(prj["nearest_station_code"])}) - {html.escape(prj["nearest_station_status"])}</value></Data>
                <Data name="d_euclidean_vs_network"><value>Chim bay: {prj["d_euclidean_m"]:.0f}m | Đi bộ thực tế: {prj["d_network_m"]:.0f}m (~{prj["walk_time_min"]:.1f} phút) | Detour: {prj["detour_ratio"]:.2f}x</value></Data>
                <Data name="bus_accessibility_500m"><value>Cách trạm buýt {prj["nearest_bus_m"]}m ({prj["bus_stops_500m"]} trạm trong bán kính 500m)</value></Data>
                {apt_ext_xml}
              </ExtendedData>
              <MultiGeometry>
                <Point>
                  <altitudeMode>relativeToGround</altitudeMode>
                  <coordinates>{prj["lon"]:.6f},{prj["lat"]:.6f},{col_height_m + 5:.1f}</coordinates>
                </Point>
                <Polygon>
                  <extrude>1</extrude>
                  <altitudeMode>relativeToGround</altitudeMode>
                  <outerBoundaryIs>
                    <LinearRing>
                      <coordinates>{poly_coords}</coordinates>
                    </LinearRing>
                  </outerBoundaryIs>
                </Polygon>
                {uncertainty_xml}
              </MultiGeometry>
            </Placemark>
            """
        )

    # --------------------------------------------------------------------------
    # LAYER 2: SO SÁNH ĐƯỜNG ĐI BỘ THỰC TẾ VS ĐƯỜNG CHIM BAY (GAP G1)
    # --------------------------------------------------------------------------
    layer2_items = []
    for prj in projects:
        walk_coords = " ".join(f"{lon:.6f},{lat:.6f},3.0" for lat, lon in prj["walking_waypoints"])
        route_desc = f"""
        <div style="font-family:Arial,sans-serif;font-size:12px;max-width:360px;">
          <h4 style="margin:0 0 6px 0;color:#0369a1;">🚶 So sánh Tuyến đi bộ vs. Đường chim bay (Gap G1)</h4>
          <div><strong>Từ dự án:</strong> {html.escape(prj["name"])}</div>
          <div><strong>Tới ga Metro:</strong> {html.escape(prj["nearest_station_name"])}</div>
          <hr style="border:0;border-top:1px solid #cbd5e1;margin:6px 0;"/>
          <div>• <strong>Khoảng cách đường chim bay (d_Euclidean):</strong> {prj["d_euclidean_m"]:.0f} m</div>
          <div>• <strong>Khoảng cách mạng lưới đi bộ (d_Network):</strong> <span style="color:#0284c7;font-weight:700;">{prj["d_network_m"]:.0f} m</span> (~{prj["walk_time_min"]:.1f} phút)</div>
          <div>• <strong>Hệ số đi vòng (Detour Ratio):</strong> <span style="color:#7c3aed;font-weight:700;">{prj["detour_ratio"]:.2f}x</span></div>
          <div style="margin-top:6px;color:#475569;"><em>{html.escape(prj["barrier_note"])}</em></div>
        </div>
        """
        layer2_items.append(
            f"""
            <Placemark>
              <name>[Đường đi bộ {prj["d_network_m"]:.0f}m] {html.escape(prj["name"])} → {html.escape(prj["nearest_station_code"])}</name>
              <styleUrl>#route_walking_network</styleUrl>
              <description><![CDATA[{route_desc}]]></description>
              <LineString>
                <tessellate>1</tessellate>
                <altitudeMode>relativeToGround</altitudeMode>
                <coordinates>{walk_coords}</coordinates>
              </LineString>
            </Placemark>
            """
        )

        # Tạo các đoạn nét đứt (dashed segments) cho đường chim bay Euclidean
        dashed_segs = create_dashed_line_segments(
            prj["lat"], prj["lon"], prj["nearest_station_lat"], prj["nearest_station_lon"]
        )
        seg_lines_xml = []
        for p1, p2 in dashed_segs:
            seg_lines_xml.append(
                f"""
                <LineString>
                  <tessellate>1</tessellate>
                  <altitudeMode>relativeToGround</altitudeMode>
                  <coordinates>{p1[1]:.6f},{p1[0]:.6f},2.0 {p2[1]:.6f},{p2[0]:.6f},2.0</coordinates>
                </LineString>
                """
            )
        layer2_items.append(
            f"""
            <Placemark>
              <name>[Đường chim bay {prj["d_euclidean_m"]:.0f}m - Nét đứt] {html.escape(prj["name"])} → {html.escape(prj["nearest_station_code"])}</name>
              <styleUrl>#route_euclidean_dashed</styleUrl>
              <description><![CDATA[{route_desc}]]></description>
              <MultiGeometry>
                {"".join(seg_lines_xml)}
              </MultiGeometry>
            </Placemark>
            """
        )

    # --------------------------------------------------------------------------
    # LAYER 3: TUYẾN METRO SỐ 3 (PHÂN BIỆT ĐANG VẬN HÀNH VS ĐANG THI CÔNG) & XE BUÝT
    # --------------------------------------------------------------------------
    layer3_items = []
    op_stations = [s for s in METRO_STATIONS if s["status"] == "operational"]
    uc_stations = [METRO_STATIONS[7], METRO_STATIONS[8], METRO_STATIONS[9]]  # Cầu Giấy -> Kim Mã -> Cát Linh

    op_line_coords = " ".join(f"{s['lon']:.6f},{s['lat']:.6f},12.0" for s in op_stations)
    uc_line_coords = " ".join(f"{s['lon']:.6f},{s['lat']:.6f},2.0" for s in uc_stations)

    layer3_items.append(
        f"""
        <Placemark>
          <name>Tuyến Metro số 3: Đoạn trên cao Nhổn – Cầu Giấy (Đang vận hành)</name>
          <styleUrl>#metro_line_operational</styleUrl>
          <description><![CDATA[Đoạn trên cao dài 8,5km từ Ga Nhổn (T3-S01) đến Ga Cầu Giấy (T3-S08), vận hành thương mại chính thức từ ngày 08/08/2024.]]></description>
          <LineString>
            <extrude>0</extrude>
            <tessellate>1</tessellate>
            <altitudeMode>relativeToGround</altitudeMode>
            <coordinates>{op_line_coords}</coordinates>
          </LineString>
        </Placemark>
        <Placemark>
          <name>Tuyến Metro số 3: Đoạn ngầm Cầu Giấy – Kim Mã – Cát Linh (Đang thi công)</name>
          <styleUrl>#metro_line_underground</styleUrl>
          <description><![CDATA[Đoạn đi ngầm của Tuyến số 3 đang trong quá trình thi công hoàn thiện nhà ga ngầm; được tách biệt trong mô hình Hedonic để tránh nhầm lẫn hiệu ứng kỳ vọng với hiệu ứng vận hành thực tế (Mục VII.4 research_b1.md).]]></description>
          <LineString>
            <tessellate>1</tessellate>
            <altitudeMode>clampToGround</altitudeMode>
            <coordinates>{uc_line_coords}</coordinates>
          </LineString>
        </Placemark>
        """
    )

    for st in METRO_STATIONS:
        st_style = "#metro_station_operational" if st["status"] == "operational" else "#metro_station_construction"
        st_html = build_station_popup_html(st)
        layer3_items.append(
            f"""
            <Placemark id="{st["code"]}">
              <name>{html.escape(st["code"])}: {html.escape(st["name"])}</name>
              <styleUrl>{st_style}</styleUrl>
              <description><![CDATA[{st_html}]]></description>
              <Point>
                <altitudeMode>relativeToGround</altitudeMode>
                <coordinates>{st["lon"]:.6f},{st["lat"]:.6f},15.0</coordinates>
              </Point>
            </Placemark>
            """
        )

    for bus in BUS_STOPS:
        layer3_items.append(
            f"""
            <Placemark id="{bus["id"]}">
              <name>🚌 {html.escape(bus["name"])}</name>
              <styleUrl>#bus_stop_style</styleUrl>
              <description><![CDATA[
                <div style="font-family:Arial,sans-serif;font-size:12px;">
                  <strong>Điểm dừng xe buýt tiếp vận ({html.escape(bus["id"])}):</strong> {html.escape(bus["name"])}<br/>
                  <strong>Các tuyến đi qua:</strong> {html.escape(bus["routes"])}
                </div>
              ]]></description>
              <Point>
                <clampToGround>1</clampToGround>
                <coordinates>{bus["lon"]:.6f},{bus["lat"]:.6f},0</coordinates>
              </Point>
            </Placemark>
            """
        )

    # --------------------------------------------------------------------------
    # LAYER 4: VÙNG ĐỆM TIẾP CẬN ĐI BỘ (400m ~ 5 PHÚT & 800m ~ 10 PHÚT)
    # --------------------------------------------------------------------------
    layer4_items = []
    # Hiển thị mặc định vùng 400m & 800m cho 4 ga trung tâm khu vực nghiên cứu (Cầu Diễn, Lê Đức Thọ, ĐHQG, Chùa Hà, Cầu Giấy)
    focus_stations = [s for s in op_stations if s["code"] in {"T3-S04", "T3-S05", "T3-S06", "T3-S07", "T3-S08"}]
    for st in focus_stations:
        c400 = create_polygon_circle_coords(st["lat"], st["lon"], radius_m=400.0, num_points=48, altitude_m=1.5)
        c800 = create_polygon_circle_coords(st["lat"], st["lon"], radius_m=800.0, num_points=48, altitude_m=1.0)
        layer4_items.append(
            f"""
            <Placemark>
              <name>Vùng TOD 400m (~5 phút đi bộ) - {html.escape(st["name"])}</name>
              <visibility>1</visibility>
              <styleUrl>#iso_400m_5min</styleUrl>
              <Polygon>
                <altitudeMode>relativeToGround</altitudeMode>
                <outerBoundaryIs><LinearRing><coordinates>{c400}</coordinates></LinearRing></outerBoundaryIs>
              </Polygon>
            </Placemark>
            <Placemark>
              <name>Vùng đệm 800m (~10 phút đi bộ) - {html.escape(st["name"])}</name>
              <visibility>0</visibility>
              <styleUrl>#iso_800m_10min</styleUrl>
              <Polygon>
                <altitudeMode>relativeToGround</altitudeMode>
                <outerBoundaryIs><LinearRing><coordinates>{c800}</coordinates></LinearRing></outerBoundaryIs>
              </Polygon>
            </Placemark>
            """
        )

    # --------------------------------------------------------------------------
    # LAYER 5: GÓC NHÌN THUYẾT TRÌNH KỂ CHUYỆN (SAVED CAMERA VIEWS)
    # --------------------------------------------------------------------------
    layer5_items = """
    <Placemark>
      <name>🎥 Góc nhìn 1: Toàn cảnh Hành lang Metro Nhổn – Cầu Giấy &amp; Mỹ Đình</name>
      <LookAt>
        <longitude>105.776500</longitude>
        <latitude>21.031500</latitude>
        <altitude>0</altitude>
        <heading>-15</heading>
        <tilt>52</tilt>
        <range>4200</range>
        <altitudeMode>relativeToGround</altitudeMode>
      </LookAt>
      <description><![CDATA[Góc nhìn tổng quan bao quát các ga trên cao Tuyến số 3 và 12 cụm chung cư nghiên cứu theo Chiến lược Định danh Không gian 3 Tầng (Chính quyền địa phương 2 cấp).]]></description>
      <Point><coordinates>105.776500,21.031500,0</coordinates></Point>
    </Placemark>
    <Placemark>
      <name>🎥 Góc nhìn 2: Cụm TOD Xuân Thủy – Cầu Giấy (IPH &amp; Discovery Complex)</name>
      <LookAt>
        <longitude>105.788500</longitude>
        <latitude>21.035500</latitude>
        <altitude>0</altitude>
        <heading>75</heading>
        <tilt>62</tilt>
        <range>1350</range>
        <altitudeMode>relativeToGround</altitudeMode>
      </LookAt>
      <description><![CDATA[Cận cảnh các tòa chung cư kết nối trực tiếp với Ga Đại học Quốc gia (T3-S06) và Ga Chùa Hà (T3-S07).]]></description>
      <Point><coordinates>105.788500,21.035500,0</coordinates></Point>
    </Placemark>
    <Placemark>
      <name>🎥 Góc nhìn 3: Minh họa Gap G1 tại Nút giao Mai Dịch – Lê Đức Thọ – Hồ Tùng Mậu</name>
      <LookAt>
        <longitude>105.768500</longitude>
        <latitude>21.036500</latitude>
        <altitude>0</altitude>
        <heading>-35</heading>
        <tilt>60</tilt>
        <range>1650</range>
        <altitudeMode>relativeToGround</altitudeMode>
      </LookAt>
      <description><![CDATA[So sánh trực quan sự khác biệt giữa khoảng cách đường chim bay (nét đứt) và tuyến đi bộ thực tế (nét liền) tại Goldmark City, The Zei và Dolphin Plaza.]]></description>
      <Point><coordinates>105.768500,21.036500,0</coordinates></Point>
    </Placemark>
    """

    kml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2">
  <Document>
    <name>B1 Research: Hedonic Pricing &amp; Tiếp cận Metro Hà Nội (3-Tier Spatial Strategy)</name>
    <open>1</open>
    <description><![CDATA[
      <div style="font-family:Arial,sans-serif;font-size:12.5px;line-height:1.5;">
        <strong>Đề tài B1:</strong> Định lượng mối liên hệ giữa khả năng tiếp cận giao thông công cộng và giá chào bán căn hộ tại Hà Nội bằng mô hình Hedonic Pricing và GIS (Tích hợp Chiến lược Định danh Không gian 3 Tầng thích ứng Cải cách Hành chính 2 cấp).<br/>
        <strong>Hướng dẫn sử dụng trên Google Earth Web:</strong>
        <ul>
          <li>Bật/tắt từng <strong>Folder (Layer 1 → Layer 5)</strong> ở thanh bên trái.</li>
          <li>Ấn vào từng <strong>Tòa chung cư (cột 3D)</strong> để xem Thẻ kết quả nghiên cứu (Định danh không gian 3 tầng, Giá chào bán, Giá dự báo Hedonic, Phần dư ε̂, Khoảng cách đi bộ vs. Chim bay, và Bảng danh sách từng căn hộ bên trong).</li>
        </ul>
      </div>
    ]]></description>
    <LookAt>
      <longitude>105.776500</longitude>
      <latitude>21.031500</latitude>
      <altitude>0</altitude>
      <heading>-15</heading>
      <tilt>52</tilt>
      <range>4200</range>
      <altitudeMode>relativeToGround</altitudeMode>
    </LookAt>
    {styles_xml}

    <Folder>
      <name>1. Tổ hợp Dự án Chung cư &amp; Kết quả Hedonic (12 cụm / 60 căn hộ)</name>
      <open>1</open>
      {"".join(layer1_items)}
    </Folder>

    <Folder>
      <name>2. So sánh Đường đi bộ thực tế vs. Đường chim bay (Research Gap G1)</name>
      <open>1</open>
      {"".join(layer2_items)}
    </Folder>

    <Folder>
      <name>3. Hạ tầng Tuyến Metro số 3 &amp; Trạm Xe buýt tiếp vận (Gap G2)</name>
      <open>1</open>
      {"".join(layer3_items)}
    </Folder>

    <Folder>
      <name>4. Vùng đệm Đi bộ quanh Ga Metro (400m ~ 5 phút &amp; 800m ~ 10 phút)</name>
      <open>0</open>
      {"".join(layer4_items)}
    </Folder>

    <Folder>
      <name>5. Góc nhìn Thuyết trình cài sẵn (Camera Views)</name>
      <open>0</open>
      {layer5_items}
    </Folder>
  </Document>
</kml>
"""
    return kml_content


def export_all_files(output_dir: Path) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    model_summary = run_hedonic_models(PROJECTS_RAW)
    kml_text = generate_kml(PROJECTS_RAW, model_summary)

    # 1. Xuất file KML
    kml_path = output_dir / "b1_hanoi_metro_hedonic_demo.kml"
    kml_path.write_text(kml_text, encoding="utf-8")

    # 2. Xuất file KMZ (nén chuẩn cho Google Earth)
    kmz_path = output_dir / "b1_hanoi_metro_hedonic_demo.kmz"
    with zipfile.ZipFile(kmz_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("doc.kml", kml_text.encode("utf-8"))

    # 3. Xuất file GeoJSON (cho QGIS / GeoPandas / Google Earth)
    geojson_features = []
    for prj in PROJECTS_RAW:
        geojson_features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [prj["lon"], prj["lat"]]},
                "properties": {
                    "project_id": prj["project_id"],
                    "name": prj["name"],
                    "urban_ring_sector": prj["urban_ring_sector"],
                    "new_ward_2level": prj["new_ward_2level"],
                    "historical_submarket": prj["historical_submarket"],
                    "district_legacy": prj["district"],
                    "ward_legacy": prj["ward"],
                    "segment": prj["segment"],
                    "geocoding_tier": prj["geocoding_tier"],
                    "geocoding_error_m": prj["geocoding_error_m"],
                    "n_listings": prj["n_listings"],
                    "mean_asking_price_m2": prj["mean_price_m2"],
                    "median_asking_price_m2": prj["median_price_m2"],
                    "hedonic_predicted_price_m2": prj["mean_pred_price_m2"],
                    "hedonic_residual_pct": prj["mean_residual_pct"],
                    "transit_premium_pct": prj["transit_premium_pct"],
                    "nearest_station_code": prj["nearest_station_code"],
                    "nearest_station_name": prj["nearest_station_name"],
                    "d_euclidean_m": prj["d_euclidean_m"],
                    "d_network_m": prj["d_network_m"],
                    "detour_ratio": prj["detour_ratio"],
                    "walk_time_min": prj["walk_time_min"],
                    "bus_stops_500m": prj["bus_stops_500m"],
                },
            }
        )
    geojson_path = output_dir / "b1_hanoi_metro_hedonic_projects.geojson"
    geojson_path.write_text(
        json.dumps({"type": "FeatureCollection", "features": geojson_features}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # 4. Xuất file CSV chi tiết từng căn hộ (60 căn)
    csv_path = output_dir / "b1_hanoi_metro_hedonic_apartments.csv"
    fieldnames = [
        "apt_id",
        "project_id",
        "project_name",
        "urban_ring_sector",
        "new_ward_2level",
        "historical_submarket",
        "district_legacy",
        "ward_legacy",
        "lat",
        "lon",
        "geocoding_tier",
        "tower",
        "floor",
        "area_m2",
        "bedrooms",
        "direction",
        "asking_price_m2",
        "total_price_billion",
        "hedonic_pred_price_m2",
        "hedonic_residual_pct",
        "transit_premium_pct",
        "nearest_station_code",
        "nearest_station_name",
        "d_euclidean_m",
        "d_network_m",
        "detour_ratio",
        "walk_time_min",
        "bus_stops_500m",
        "listing_date",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for prj in PROJECTS_RAW:
            for apt in prj["apartments"]:
                writer.writerow(
                    {
                        "apt_id": apt["apt_id"],
                        "project_id": prj["project_id"],
                        "project_name": prj["name"],
                        "urban_ring_sector": prj["urban_ring_sector"],
                        "new_ward_2level": prj["new_ward_2level"],
                        "historical_submarket": prj["historical_submarket"],
                        "district_legacy": prj["district"],
                        "ward_legacy": prj["ward"],
                        "lat": prj["lat"],
                        "lon": prj["lon"],
                        "geocoding_tier": prj["geocoding_tier"],
                        "tower": apt["tower"],
                        "floor": apt["floor"],
                        "area_m2": apt["area_m2"],
                        "bedrooms": apt["bedrooms"],
                        "direction": apt["direction"],
                        "asking_price_m2": apt["asking_price_m2"],
                        "total_price_billion": apt["total_price_billion"],
                        "hedonic_pred_price_m2": apt["pred_price_m2"],
                        "hedonic_residual_pct": apt["residual_pct"],
                        "transit_premium_pct": apt["transit_premium_pct"],
                        "nearest_station_code": prj["nearest_station_code"],
                        "nearest_station_name": prj["nearest_station_name"],
                        "d_euclidean_m": prj["d_euclidean_m"],
                        "d_network_m": prj["d_network_m"],
                        "detour_ratio": prj["detour_ratio"],
                        "walk_time_min": prj["walk_time_min"],
                        "bus_stops_500m": prj["bus_stops_500m"],
                        "listing_date": apt["listing_date"],
                    }
                )

    # 5. Xuất file tổng hợp 12 dự án GIS (b1_tong_hop_12_du_an_gis.csv) tích hợp 3 tầng không gian
    projects_csv_path = output_dir / "b1_tong_hop_12_du_an_gis.csv"
    prj_fields = [
        "Mã Dự án",
        "Tên Tổ hợp Chung cư",
        "Vành đai - Khu vực Đô thị (Tầng 1)",
        "Phường/Xã Mới 2 Cấp (Tầng 2)",
        "Submarket Lịch sử (Tầng 3)",
        "Phân khúc",
        "Cấp độ Geocoding",
        "Ga Metro gần nhất",
        "d_Euclidean (m)",
        "d_Network (m)",
        "Detour Ratio (d_Net/d_Euc)",
        "Thời gian đi bộ (phút)",
        "Số trạm buýt 500m",
        "Giá chào bán TB (tr/m²)",
        "Giá dự báo Hedonic E1 (tr/m²)",
        "Phần dư TB ε̂ (%)",
        "Đóng góp biên Metro (%)",
    ]
    with projects_csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=prj_fields)
        writer.writeheader()
        for prj in PROJECTS_RAW:
            writer.writerow(
                {
                    "Mã Dự án": prj["project_id"],
                    "Tên Tổ hợp Chung cư": prj["name"],
                    "Vành đai - Khu vực Đô thị (Tầng 1)": prj["urban_ring_sector"],
                    "Phường/Xã Mới 2 Cấp (Tầng 2)": prj["new_ward_2level"],
                    "Submarket Lịch sử (Tầng 3)": prj["historical_submarket"],
                    "Phân khúc": prj["segment"],
                    "Cấp độ Geocoding": prj["geocoding_tier"],
                    "Ga Metro gần nhất": f"{prj['nearest_station_name']} ({prj['nearest_station_code']})",
                    "d_Euclidean (m)": prj["d_euclidean_m"],
                    "d_Network (m)": prj["d_network_m"],
                    "Detour Ratio (d_Net/d_Euc)": prj["detour_ratio"],
                    "Thời gian đi bộ (phút)": prj["walk_time_min"],
                    "Số trạm buýt 500m": prj["bus_stops_500m"],
                    "Giá chào bán TB (tr/m²)": prj["mean_price_m2"],
                    "Giá dự báo Hedonic E1 (tr/m²)": prj["mean_pred_price_m2"],
                    "Phần dư TB ε̂ (%)": f"{prj['mean_residual_pct']:+.2f}%",
                    "Đóng góp biên Metro (%)": f"{prj['transit_premium_pct']:+.2f}%",
                }
            )

    res_net = model_summary["model_e1_network"]
    res_euc = model_summary["model_e0_euclidean"]
    print("=== KẾT QUẢ CHẠY MÔ HÌNH HEDONIC TRÊN BỘ MẪU KIỂM THỬ (N=60, G=12 DỰ ÁN) ===")
    print(f"Model E1 (Network Walking Distance): beta_1 = {res_net['beta'][1]:+.4f} (Clustered SE = {res_net['se_cl'][1]:.4f}), R2 = {res_net['r2']:.4f}")
    print(f"Model E0 (Euclidean Straight Line) : beta_1 = {res_euc['beta'][1]:+.4f} (Clustered SE = {res_euc['se_cl'][1]:.4f}), R2 = {res_euc['r2']:.4f}")
    print("Đã xuất thành công các file:")
    for k, p in [
        ("KML", kml_path),
        ("KMZ", kmz_path),
        ("GeoJSON", geojson_path),
        ("CSV (60 căn)", csv_path),
        ("CSV (12 dự án)", projects_csv_path),
    ]:
        print(f" - {k}: {p} ({p.stat().st_size:,} bytes)")

    return {
        "kml": kml_path,
        "kmz": kmz_path,
        "geojson": geojson_path,
        "csv": csv_path,
        "projects_csv": projects_csv_path,
    }


if __name__ == "__main__":
    export_all_files(Path("/tmp/gdrive_b1"))

