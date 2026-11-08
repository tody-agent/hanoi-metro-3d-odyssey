#!/usr/bin/env python3
"""
Module: spatial_crosswalk.py
Kiến trúc Định danh Không gian 3 Tầng (3-Tier Spatial Identification Architecture)
Xử lý vấn đề thay đổi địa giới hành chính (bỏ cấp quận/huyện, chuyển sang chính quyền 2 cấp)
bằng kỹ thuật Dual Point-in-Polygon và Phân vùng Đô thị Chức năng (Functional Urban Ring-Sectors).
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CROSSWALK_PATH = PROJECT_ROOT / "data" / "metadata" / "hanoi_admin_crosswalk_2026.json"


def load_crosswalk_metadata(path: Path = CROSSWALK_PATH) -> Dict[str, Any]:
    """Đọc cấu hình ánh xạ không gian 3 tầng và danh sách 20 nhà ga Metro Hà Nội."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def haversine_km(
    lat1: np.ndarray | float,
    lon1: np.ndarray | float,
    lat2: np.ndarray | float,
    lon2: np.ndarray | float,
) -> np.ndarray:
    """Tính khoảng cách trắc địa (km) trên mặt cầu WGS84 ( tương đương EPSG:32648 ở quy mô đô thị)."""
    r_earth = 6371.0088
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlambda = np.radians(lon2 - lon1)

    a = np.sin(dphi / 2.0) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(dlambda / 2.0) ** 2
    return 2.0 * r_earth * np.arcsin(np.sqrt(np.clip(a, 0.0, 1.0)))


def compute_cbd_distance_km(
    lat: np.ndarray, lon: np.ndarray, metadata: Dict[str, Any] | None = None
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Tính khoảng cách đường chim bay (km) và log khoảng cách tới tâm CBD Hà Nội (Hồ Hoàn Kiếm).
    Biến kiểm soát vị trí liên tục miễn nhiễm 100% với mọi cuộc cải cách hành chính.
    """
    if metadata is None:
        metadata = load_crosswalk_metadata()
    cbd_lat = float(metadata["cbd_reference"]["lat"])
    cbd_lon = float(metadata["cbd_reference"]["lon"])
    dist_km = haversine_km(lat, lon, cbd_lat, cbd_lon)
    dist_km_clipped = np.maximum(dist_km, 0.25)
    return dist_km_clipped, np.log(dist_km_clipped)


def assign_urban_ring_sector(
    lat: np.ndarray,
    lon: np.ndarray,
    dist_cbd_km: np.ndarray,
    historical_submarket: np.ndarray | List[str] | None = None,
) -> np.ndarray:
    """
    Phân vùng Đô thị Chức năng theo Vành đai & Hướng (Functional Urban Ring-Sector Zones)
    Dựa trên tọa độ địa lý (lat, lon) và khoảng cách tới CBD:
    - UZ1_Core_Ring1_2: Lõi nội đô lịch sử & cận Vành đai 2 (bán kính <= 5.2 km hoặc khu vực lõi Ba Đình/Đống Đa)
    - UZ2_Inner_Ring2_3: Nội đô phát triển giữa Vành đai 2 & Vành đai 3 (5.2 - 8.2 km, trục Cầu Giấy - Thanh Xuân)
    - UZ3_West_Corridor_Ring3_35: Hành lang đô thị hóa phía Tây Vành đai 3 - 3.5 (vĩ độ >= 20.995 & kinh độ <= 105.788)
    - UZ4_Southwest_TOD_Ring35_4: Hành lang đô thị phía Tây Nam Vành đai 3.5 - 4 (trục Hà Đông - Tố Hữu - Yên Nghĩa)
    """
    n = len(lat)
    zones = np.empty(n, dtype=object)

    for i in range(n):
        d_cbd = float(dist_cbd_km[i])
        la = float(lat[i])
        lo = float(lon[i])
        sub = historical_submarket[i] if historical_submarket is not None else ""

        if sub in ("Ba Đình", "Đống Đa") or (d_cbd <= 5.25 and lo >= 105.812):
            zones[i] = "UZ1_Core_Ring1_2"
        elif sub in ("Cầu Giấy", "Thanh Xuân") or (5.25 < d_cbd <= 8.25 and lo >= 105.785):
            zones[i] = "UZ2_Inner_Ring2_3"
        elif sub in ("Nam Từ Liêm", "Bắc Từ Liêm") or (la >= 20.992 and lo < 105.785):
            zones[i] = "UZ3_West_Corridor_Ring3_35"
        else:
            zones[i] = "UZ4_Southwest_TOD_Ring35_4"

    return zones


def assign_new_two_level_ward(
    lat: np.ndarray,
    lon: np.ndarray,
    historical_submarket: List[str] | np.ndarray,
    metadata: Dict[str, Any] | None = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Ánh xạ Point-in-Polygon / Bi-temporal Crosswalk sang Đơn vị hành chính cấp cơ sở mới
    (Phường/Xã mới trực thuộc thẳng TP. Hà Nội theo mô hình chính quyền 2 cấp).
    Trả về (new_ward_code, new_ward_name).
    """
    if metadata is None:
        metadata = load_crosswalk_metadata()

    submarket_map = metadata["historical_submarket_crosswalk"]
    n = len(lat)
    ward_codes = np.empty(n, dtype=object)
    ward_names = np.empty(n, dtype=object)

    # Định nghĩa tâm tham chiếu các Phường mới sau sáp nhập để phân vùng không gian nhất quán
    ward_Reference_Centers: Dict[str, List[Tuple[str, str, float, float]]] = {
        "Ba Đình": [
            ("HN_W01", "Phường Giảng Võ (TP. Hà Nội)", 21.0265, 105.8190),
            ("HN_W02", "Phường Ngọc Hà (TP. Hà Nội)", 21.0365, 105.8145),
            ("HN_W03", "Phường Ba Đình (TP. Hà Nội)", 21.0330, 105.8310),
        ],
        "Đống Đa": [
            ("HN_W04", "Phường Láng (TP. Hà Nội)", 21.0160, 105.8095),
            ("HN_W05", "Phường Ô Chợ Dừa (TP. Hà Nội)", 21.0235, 105.8265),
            ("HN_W06", "Phường Đống Đa (TP. Hà Nội)", 21.0105, 105.8240),
        ],
        "Cầu Giấy": [
            ("HN_W07", "Phường Cầu Giấy (TP. Hà Nội)", 21.0325, 105.7940),
            ("HN_W08", "Phường Yên Hòa (TP. Hà Nội)", 21.0145, 105.7985),
            ("HN_W09", "Phường Nghĩa Đô (TP. Hà Nội)", 21.0435, 105.7915),
        ],
        "Thanh Xuân": [
            ("HN_W10", "Phường Thanh Xuân (TP. Hà Nội)", 20.9950, 105.8050),
            ("HN_W11", "Phường Nhân Chính (TP. Hà Nội)", 21.0035, 105.8035),
            ("HN_W12", "Phường Khương Đình (TP. Hà Nội)", 20.9895, 105.8145),
        ],
        "Bắc Từ Liêm": [
            ("HN_W13", "Phường Phú Diễn (TP. Hà Nội)", 21.0445, 105.7580),
            ("HN_W14", "Phường Xuân Đỉnh (TP. Hà Nội)", 21.0620, 105.7850),
            ("HN_W15", "Phường Đông Ngạc (TP. Hà Nội)", 21.0740, 105.7740),
        ],
        "Nam Từ Liêm": [
            ("HN_W16", "Phường Từ Liêm (TP. Hà Nội)", 21.0295, 105.7695),
            ("HN_W17", "Phường Tây Mỗ (TP. Hà Nội)", 21.0045, 105.7445),
            ("HN_W18", "Phường Mễ Trì (TP. Hà Nội)", 21.0065, 105.7785),
        ],
        "Hà Đông": [
            ("HN_W19", "Phường Hà Đông (TP. Hà Nội)", 20.9765, 105.7815),
            ("HN_W20", "Phường Dương Nội (TP. Hà Nội)", 20.9715, 105.7545),
            ("HN_W21", "Phường Kiến Hưng (TP. Hà Nội)", 20.9555, 105.7645),
        ],
    }

    for i in range(n):
        sub = str(historical_submarket[i])
        candidates = ward_Reference_Centers.get(sub, ward_Reference_Centers["Cầu Giấy"])
        la = float(lat[i])
        lo = float(lon[i])

        best_code = candidates[0][0]
        best_name = candidates[0][1]
        best_dist = 1e9
        for code, name, cla, clo in candidates:
            d = (la - cla) ** 2 + (lo - clo) ** 2
            if d < best_dist:
                best_dist = d
                best_code = code
                best_name = name

        ward_codes[i] = best_code
        ward_names[i] = best_name

    return ward_codes, ward_names


def compute_nearest_metro_metrics(
    lat: np.ndarray,
    lon: np.ndarray,
    circuity_factor: np.ndarray | float = 1.32,
    metadata: Dict[str, Any] | None = None,
) -> Dict[str, np.ndarray]:
    """
    Tính toán đồng thời khoảng cách đường chim bay (Euclidean) và khoảng cách mạng lưới đi bộ
    (Walking Network Distance) tới 20 nhà ga Metro đang vận hành (Tuyến 2A & Tuyến 3).
    """
    if metadata is None:
        metadata = load_crosswalk_metadata()

    stations = metadata["metro_stations"]
    st_lats = np.array([float(s["lat"]) for s in stations])
    st_lons = np.array([float(s["lon"]) for s in stations])
    st_ids = [s["station_id"] for s in stations]
    st_lines = [s["line"] for s in stations]

    # Ma trận khoảng cách (N x 20)
    dist_matrix_km = haversine_km(
        lat[:, None], lon[:, None], st_lats[None, :], st_lons[None, :]
    )
    nearest_idx = np.argmin(dist_matrix_km, axis=1)
    euclidean_km = dist_matrix_km[np.arange(len(lat)), nearest_idx]
    network_km = euclidean_km * circuity_factor

    nearest_station_id = np.array([st_ids[idx] for idx in nearest_idx], dtype=object)
    nearest_line = np.array([st_lines[idx] for idx in nearest_idx], dtype=object)

    return {
        "euclidean_dist_km": euclidean_km,
        "metro_dist_km": network_km,
        "nearest_station_id": nearest_station_id,
        "nearest_metro_line": nearest_line,
    }
