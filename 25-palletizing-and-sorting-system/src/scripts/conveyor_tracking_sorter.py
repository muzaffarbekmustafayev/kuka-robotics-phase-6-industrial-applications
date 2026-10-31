"""Conveyor Tracking (Line Tracking) & Automated Part Sorting Engine.

Calculates dynamic tracking transformations for objects moving on a conveyor:
    P_target(t) = P_detect + v_conv * (t - t_detect)
Monitors tracking window limits [X_min, X_max] and routes parts to class-specific pallets.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import numpy as np


@dataclass
class ConveyorPart:
    part_id: int
    part_type: str  # e.g., 'TYPE_A', 'TYPE_B'
    detect_time_s: float
    initial_pos_mm: np.ndarray  # [x, y, z] at detection trigger


class ConveyorTrackingSystem:
    r"""Simulates KUKA ConveyorTech / Line Tracking with encoder synchronization."""

    def __init__(self,
                 conveyor_velocity_mm_s: float = 150.0,
                 tracking_window_x: Tuple[float, float] = (250.0, 650.0),
                 pulley_diameter_mm: float = 100.0,
                 encoder_cpr: int = 4096):
        self.v_conv = conveyor_velocity_mm_s
        self.win_min, self.win_max = tracking_window_x
        # Pulse-to-mm scaling factor: pi * D / CPR
        self.mm_per_pulse = (np.pi * pulley_diameter_mm) / float(encoder_cpr)

    def encoder_pulses_to_distance(self, pulse_count: int) -> float:
        """Convert incremental encoder tick count to linear displacement in mm."""
        return float(pulse_count * self.mm_per_pulse)

    def get_part_position_at_time(self, part: ConveyorPart, current_time_s: float) -> np.ndarray:
        r"""Compute instantaneous position of moving workpiece:

        P(t) = P_0 + [v_conv * delta_t, 0, 0]^T
        """
        dt = current_time_s - part.detect_time_s
        if dt < 0:
            raise ValueError("Evaluation time cannot be earlier than detection time.")

        pos = part.initial_pos_mm.copy()
        pos[0] += self.v_conv * dt  # Conveyor moves along Base X
        return pos

    def evaluate_pick_feasibility(self, part: ConveyorPart, current_time_s: float) -> Dict[str, any]:
        """Check if part is currently within reachable and safe robot tracking window."""
        pos = self.get_part_position_at_time(part, current_time_s)
        x = pos[0]

        in_window = bool(self.win_min <= x <= self.win_max)
        is_missed = bool(x > self.win_max)
        is_approaching = bool(x < self.win_min)

        return {
            "part_id": part.part_id,
            "part_type": part.part_type,
            "current_pos_mm": pos,
            "in_window": in_window,
            "is_missed": is_missed,
            "is_approaching": is_approaching,
            "distance_to_window_exit_mm": float(max(0.0, self.win_max - x)),
        }


def main():
    print("=" * 65)
    print("Lesson 25: Conveyor Tracking (Line Tracking) & Sorting System")
    print("=" * 65)

    system = ConveyorTrackingSystem(
        conveyor_velocity_mm_s=200.0,
        tracking_window_x=(300.0, 700.0)
    )

    # Workpiece detected at photo-eye sensor at t = 0.0 s
    part1 = ConveyorPart(
        part_id=101,
        part_type="MOTOR_BRACKET",
        detect_time_s=0.0,
        initial_pos_mm=np.array([100.0, 250.0, 150.0])
    )

    print(f"\nConveyor Speed: {system.v_conv} mm/s")
    print(f"Tracking Window X: [{system.win_min}, {system.win_max}] mm")

    # Evaluate at multiple time checkpoints
    for t_check in [0.5, 1.5, 2.5, 3.5]:
        eval_res = system.evaluate_pick_feasibility(part1, current_time_s=t_check)
        p = np.round(eval_res["current_pos_mm"], 2)
        print(f"\nTime t = {t_check:.1f} s:")
        print(f"  Part Pos: {p.tolist()} mm")
        print(f"  In Tracking Window: {eval_res['in_window']}")
        print(f"  Distance to Window Exit: {eval_res['distance_to_window_exit_mm']:.2f} mm")


if __name__ == "__main__":
    main()
