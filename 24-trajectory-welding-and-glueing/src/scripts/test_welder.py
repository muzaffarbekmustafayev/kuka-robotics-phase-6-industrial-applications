"""Unit tests for Space Curve Welding and Frenet Frame calculations."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from space_curve_welder import SpaceCurveWelder


def test_frenet_frame_orthonormality():
    tangent = np.array([10.0, 5.0, -2.0])
    T, N, B = SpaceCurveWelder.compute_frenet_frame(tangent)

    # Unit lengths
    assert np.isclose(np.linalg.norm(T), 1.0, atol=1e-6)
    assert np.isclose(np.linalg.norm(N), 1.0, atol=1e-6)
    assert np.isclose(np.linalg.norm(B), 1.0, atol=1e-6)

    # Mutual orthogonality: dot products = 0
    assert np.isclose(np.dot(T, N), 0.0, atol=1e-6)
    assert np.isclose(np.dot(T, B), 0.0, atol=1e-6)
    assert np.isclose(np.dot(N, B), 0.0, atol=1e-6)

    # Right-handed coordinate frame: det(R) = +1
    R = np.column_stack([T, N, B])
    assert np.isclose(np.linalg.det(R), 1.0, atol=1e-6)


def test_dispensing_flow_rate_proportionality():
    width, height = 4.0, 2.0
    welder = SpaceCurveWelder(bead_width_mm=width, bead_height_mm=height)

    # Area = pi * 4 * 2 / 4 = 2 * pi = 6.28318 mm^2
    expected_area = np.pi * 2.0
    assert np.isclose(welder.bead_area_mm2, expected_area, atol=1e-4)

    # Test flow rate at 30 mm/s
    seam = welder.sample_helical_weld_seam(feed_velocity_mm_s=30.0, num_points=10)
    expected_flow = 30.0 * expected_area
    assert np.allclose(seam["flow_rates_mm3_s"], expected_flow, atol=1e-3)
