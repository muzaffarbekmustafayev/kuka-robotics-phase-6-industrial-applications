"""Unit tests for Conveyor Tracking and Sorting System."""

import sys
from pathlib import Path
import numpy as np
import pytest

sys.path.append(str(Path(__file__).parent))

from conveyor_tracking_sorter import ConveyorTrackingSystem, ConveyorPart


def test_encoder_scaling():
    # Pulley diameter = 100 mm -> circumference = 100 * pi = 314.159 mm
    # 4096 counts per rev
    system = ConveyorTrackingSystem(pulley_diameter_mm=100.0, encoder_cpr=4096)
    dist = system.encoder_pulses_to_distance(4096)
    assert np.isclose(dist, np.pi * 100.0, atol=1e-3)


def test_conveyor_part_tracking_and_window():
    system = ConveyorTrackingSystem(
        conveyor_velocity_mm_s=100.0,
        tracking_window_x=(200.0, 500.0)
    )

    part = ConveyorPart(
        part_id=1,
        part_type="GEAR_BOX",
        detect_time_s=1.0,
        initial_pos_mm=np.array([50.0, 200.0, 100.0])
    )

    # At t = 1.0 s: pos = 50 mm (approaching, not yet in window)
    res_1 = system.evaluate_pick_feasibility(part, current_time_s=1.0)
    assert res_1["is_approaching"] is True
    assert res_1["in_window"] is False

    # At t = 3.0 s: pos = 50 + 100 * 2 = 250 mm (inside window [200, 500])
    res_2 = system.evaluate_pick_feasibility(part, current_time_s=3.0)
    assert res_2["in_window"] is True
    assert res_2["is_missed"] is False

    # At t = 6.0 s: pos = 50 + 100 * 5 = 550 mm (missed, passed window)
    res_3 = system.evaluate_pick_feasibility(part, current_time_s=6.0)
    assert res_3["in_window"] is False
    assert res_3["is_missed"] is True
