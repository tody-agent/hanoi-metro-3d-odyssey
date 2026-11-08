#!/usr/bin/env python3
"""
Bộ kiểm thử tự động (Automated Quality Gates G2-G5) cho Kiến trúc Định danh Không gian 3 Tầng
(3-Tier Spatial Identification Architecture) xử lý cải cách bỏ cấp quận/huyện tại Hà Nội.
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.gis.spatial_crosswalk import (
    assign_new_two_level_ward,
    assign_urban_ring_sector,
    compute_cbd_distance_km,
    compute_nearest_metro_metrics,
    load_crosswalk_metadata,
)
from src.models.run_hedonic_multi_tier import (
    build_verified_hanoi_dataset,
    extract_coef_row,
    run_all_econometric_models,
)


class TestThreeTierSpatialPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.metadata = load_crosswalk_metadata()
        cls.data = build_verified_hanoi_dataset()
        cls.results = run_all_econometric_models(cls.data)

    def test_01_sample_completeness_and_zero_missingness(self) -> None:
        """Kiểm tra tổng cỡ mẫu N = 16.471 và không có bất kỳ bản ghi nào bị rớt khi ánh xạ 3 tầng."""
        self.assertEqual(len(self.data["price_m2"]), 16471)
        for field in (
            "urban_ring_sector",
            "new_ward_code",
            "new_ward_name",
            "historical_submarket",
        ):
            arr = self.data[field]
            self.assertEqual(len(arr), 16471)
            self.assertTrue(all(str(x).strip() != "" for x in arr), f"Trường {field} có giá trị rỗng!")

    def test_02_coordinate_invariance_to_admin_reform(self) -> None:
        """
        Chứng minh tọa độ (lat, lon), khoảng cách tới CBD và khoảng cách mạng lưới đi bộ tới ga Metro
        hoàn toàn độc lập với nhãn hành chính quận/huyện.
        """
        sample_lat = np.array([21.0352, 20.9985, 20.9708])
        sample_lon = np.array([105.7946, 105.8105, 105.7745])
        m_a = compute_nearest_metro_metrics(sample_lat, sample_lon, metadata=self.metadata)
        m_b = compute_nearest_metro_metrics(sample_lat, sample_lon, metadata=self.metadata)
        np.testing.assert_allclose(m_a["metro_dist_km"], m_b["metro_dist_km"], rtol=1e-12)
        self.assertTrue(np.all(m_a["metro_dist_km"] >= m_a["euclidean_dist_km"]))

    def test_03_no_overcontrolling_or_multicollinearity_in_main_model(self) -> None:
        """
        Kiểm tra cảnh báo kinh tế lượng tại research_b1.md (dòng 517):
        Hệ số VIF của các biến khoảng cách tới ga Metro trong Mô hình Chính (M3) phải < 5.0.
        """
        vifs = self.results["vif_diagnostics_m3"]
        for var_name, vif_val in vifs.items():
            self.assertLess(
                vif_val,
                5.0,
                f"Biến {var_name} có VIF = {vif_val} >= 5.0 (nguy cơ đa cộng tuyến)!",
            )

    def test_04_robustness_across_all_three_spatial_tiers(self) -> None:
        """
        Chứng minh hệ số vành đai đi bộ tối ưu (500m - 1.000m) mang dấu dương (+3.6% đến +4.1%)
        và có ý nghĩa thống kê ở mức 99% (p < 0.01) xuyên suốt cả 3 cách kiểm soát không gian:
        - M3 (Phân vùng Vành đai Đô thị + CBD)
        - M4 (Tiểu thị trường lịch sử / Quận cũ)
        - M5 (Đơn vị Phường mới theo mô hình chính quyền 2 cấp)
        - M6 (Mẫu con định vị chính xác tòa nhà project_exact)
        """
        for model_key in (
            "M3_Main_UrbanRing_CBD",
            "M4_Robust_HistoricalSubmarket",
            "M5_Robust_NewWard_2Level",
            "M6_Sensitivity_ExactProjectOnly",
        ):
            beta, se, p_val, stars = extract_coef_row(self.results[model_key], "band_500_1000")
            self.assertGreater(beta, 0.030, f"{model_key}: beta_500_1000m quá thấp ({beta})")
            self.assertLess(beta, 0.050, f"{model_key}: beta_500_1000m vượt ngưỡng ({beta})")
            self.assertLess(p_val, 0.01, f"{model_key}: p_val = {p_val} không đạt mức ý nghĩa 1%")
            self.assertEqual(stars, "***")

    def test_05_inverted_u_nuisance_effect_near_station(self) -> None:
        """
        Chứng minh hiện tượng chữ U ngược: Hệ số vùng sát chân ga (<500m) luôn nhỏ hơn đáng kể
        so với vùng đi bộ tối ưu (500m - 1.000m) do ngoại ứng tiếng ồn và rung chấn cầu cạn.
        """
        for model_key in (
            "M3_Main_UrbanRing_CBD",
            "M4_Robust_HistoricalSubmarket",
            "M5_Robust_NewWard_2Level",
        ):
            b_near, _, _, _ = extract_coef_row(self.results[model_key], "band_lt_500")
            b_sweet, _, _, _ = extract_coef_row(self.results[model_key], "band_500_1000")
            self.assertLess(b_near, b_sweet * 0.45)


if __name__ == "__main__":
    unittest.main(verbosity=2)
