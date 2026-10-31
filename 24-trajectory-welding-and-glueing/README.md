# 24-Dars: Fazoviy payvandlash va germetik yelimlash (Frenet-Serret Reperi)
## 3D Space Curve Arc Welding & Precision Dispensing/Glueing

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-6-industrial-applications-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA KR 6 R900-2 manipulyatorida 3D fazoviy egri chiziqlar bo'ylab payvandlash (Arc Welding) va germetik yelimlash (Dispensing / Glueing) texnologik jarayonlarini dasturlash: Frenet-Serret fazoviy reperi ($\mathbf{T}, \mathbf{N}, \mathbf{B}$), payvandlash gorelkasi orientatsiyasi (Lead / Tilt angles) hamda robot harakat tezligiga mutanosib material sarfi ($\dot{Q} = v \cdot A$) balansini hisoblash.

---

### 📊 2. Natija (Result)
1. **Python 3D Payvandlash va Dozalash Modeli (`space_curve_welder.py`):**
   - Fazoviy egri chiziq bo'yicha ortonormal Frenet-Serret bazisini qurish.
   - Doimiy ekstruziya qalinligini ta'minlovchi dinamik oqim hisobi: $\dot{Q}(t) = v_{tcp}(t) \cdot A_{bead}$.
   - Parametrik spiral chok traektoriyasini generatsiya qilish.
2. **KRL Ishlab chiqarish dasturi (`WELD_PATH.src` va `WELD_PATH.dat`):**
   - Sanoat payvandlash/dozator triggerlari (`$OUT[20]`, `$OUT[21]`), KUKA Spline harakat bloki (`SPLINE ... ENDSPLINE`).
3. **Pytest Unit Testlari (`test_welder.py`):**
   - Frenet reperi ortogonalligi, o'ng qo'l qoidasi ($\det R = +1$) va oqim tezligi proporsionalligi (2/2 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$\mathbf{T}(s) = \frac{d\mathbf{r}}{ds}, \quad \mathbf{N}(s) = \frac{1}{\kappa} \frac{d\mathbf{T}}{ds}, \quad \mathbf{B}(s) = \mathbf{T} \times \mathbf{N}, \quad \dot{Q}(t) = v_{tcp}(t) \cdot A_{bead}$$

Nazariya va formulalar [**docs/derivations.md**](./docs/derivations.md) da keltirilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python modelini tekshirish:
```bash
uv run --with numpy python src/scripts/space_curve_welder.py
```

Konsol chiqishi:
```
=================================================================
Lesson 24: 3D Curve Arc Welding, Frenet Frames & Dispensing Flow
=================================================================

Bead Cross-Section Area: 9.82 mm^2
Dispenser Flow Rate:     196.35 mm^3/s at 20 mm/s feed

Generated 3D Welding Seam Waypoints:
  Point #1: Pos=[ 80.00,   0.00,   0.00] mm | Det(R)=1.00
  Point #2: Pos=[ 56.57,  56.57,   3.12] mm | Det(R)=1.00
  Point #3: Pos=[  0.00,  80.00,   6.25] mm | Det(R)=1.00
  Point #4: Pos=[-56.57,  56.57,   9.38] mm | Det(R)=1.00
  Point #5: Pos=[-80.00,   0.00,  12.50] mm | Det(R)=1.00
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_welder.py
```
Natija: `2 passed in 0.12s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
