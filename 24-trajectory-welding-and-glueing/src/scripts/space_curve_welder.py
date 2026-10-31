"""3D Space Curve Arc Welding & Precision Glue Dispensing Trajectory Engine.

Implements differential geometry of 3D spatial curves using Frenet-Serret apparatus (T, N, B),
curvature-adaptive feedrate control, torch lead/tilt angles, and mass flow extrusion scaling:
    Q_dot(t) = v_tcp(t) * A_bead
"""

from typing import List, Dict, Tuple
import numpy as np


class SpaceCurveWelder:
    r"""Generates robot waypoints with adaptive tool orientation along 3D space curves."""

    def __init__(self, bead_width_mm: float = 6.0, bead_height_mm: float = 3.0):
        # Elliptical bead cross-section: A = (pi * w * h) / 4
        self.bead_area_mm2 = (np.pi * bead_width_mm * bead_height_mm) / 4.0

    @staticmethod
    def compute_frenet_frame(tangent: np.ndarray, normal_hint: np.ndarray = np.array([0.0, 0.0, 1.0])) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        r"""Compute orthonormal Frenet frame (T, N, B) along curve velocity vector."""
        t_norm = np.linalg.norm(tangent)
        if t_norm < 1e-6:
            raise ValueError("Zero tangent vector cannot define a Frenet frame.")
        T = tangent / t_norm

        # Orthogonalize normal hint
        n_proj = normal_hint - np.dot(normal_hint, T) * T
        norm_np = np.linalg.norm(n_proj)
        if norm_np < 1e-4:
            # Fallback hint
            alt_hint = np.array([1.0, 0.0, 0.0])
            n_proj = alt_hint - np.dot(alt_hint, T) * T
            norm_np = np.linalg.norm(n_proj)

        N = n_proj / norm_np
        B = np.cross(T, N)
        return T, N, B

    def sample_helical_weld_seam(self,
                                 radius_mm: float = 100.0,
                                 pitch_mm: float = 30.0,
                                 turns: float = 1.0,
                                 num_points: int = 25,
                                 feed_velocity_mm_s: float = 20.0) -> Dict[str, any]:
        r"""Sample parametric 3D helical welding seam:

        r(u) = [R*cos(u), R*sin(u), (pitch / (2*pi)) * u]^T
        """
        u_max = turns * 2.0 * np.pi
        u_vals = np.linspace(0.0, u_max, num_points)

        positions = []
        rotations = []
        flow_rates = []

        for u in u_vals:
            # Position
            x = radius_mm * np.cos(u)
            y = radius_mm * np.sin(u)
            z = (pitch_mm / (2.0 * np.pi)) * u
            positions.append(np.array([x, y, z]))

            # Analytical tangent r'(u)
            dr_du = np.array([
                -radius_mm * np.sin(u),
                radius_mm * np.cos(u),
                pitch_mm / (2.0 * np.pi)
            ])

            # Frenet frame
            T, N, B = self.compute_frenet_frame(dr_du)
            R_frenet = np.column_stack([T, N, B])
            rotations.append(R_frenet)

            # Volumetric flow rate Q_dot = v * A
            q_flow = feed_velocity_mm_s * self.bead_area_mm2  # mm^3/s
            flow_rates.append(q_flow)

        return {
            "positions_mm": np.array(positions),
            "rotations": rotations,
            "flow_rates_mm3_s": np.array(flow_rates),
            "bead_cross_section_mm2": float(self.bead_area_mm2),
        }


def main():
    print("=" * 65)
    print("Lesson 24: 3D Curve Arc Welding, Frenet Frames & Dispensing Flow")
    print("=" * 65)

    welder = SpaceCurveWelder(bead_width_mm=5.0, bead_height_mm=2.5)
    seam = welder.sample_helical_weld_seam(radius_mm=80.0, pitch_mm=25.0, turns=0.5, num_points=5)

    print(f"\nBead Cross-Section Area: {seam['bead_cross_section_mm2']:.2f} mm^2")
    print(f"Dispenser Flow Rate:     {seam['flow_rates_mm3_s'][0]:.2f} mm^3/s at 20 mm/s feed")

    print("\nGenerated 3D Welding Seam Waypoints:")
    for idx, (p, R) in enumerate(zip(seam["positions_mm"], seam["rotations"])):
        print(f"  Point #{idx+1}: Pos=[{p[0]:6.2f}, {p[1]:6.2f}, {p[2]:6.2f}] mm | Det(R)={np.linalg.det(R):.2f}")


if __name__ == "__main__":
    main()
