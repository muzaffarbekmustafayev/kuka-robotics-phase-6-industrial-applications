# 25-Dars: Dinamik konveyer kuzatish (Conveyor Tracking) va avtomatlashtirilgan saralash
## Conveyor Tracking (Line Tracking), Automated Sorting & Palletizing

[![Phase](https://img.shields.io/badge/Phase-kuka-robotics-phase-6-industrial-applications-blue.svg)](#)
[![Robot: KUKA KR 6 R900-2](https://img.shields.io/badge/KUKA-KR%206%20R900--2%20(AGILUS)-orange.svg)](https://www.kuka.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../LICENSE)

---

### 🎯 1. Maqsad (Goal)
KUKA ConveyorTech texnologiyasi asosida harakatlanayotgan konveyer lentasidagi mahsulotlarni to'xtatmasdan ushlab olish (Conveyor Tracking / Line Tracking), enkoder impulslari orqali dinamik nishon pozitsiyasini hisoblash, kuzatish oynasi ($[X_{min}, X_{max}]$) nazorati va mahsulot turiga ko'ra saralab palletlarga taxlash tizimini yaratish.

---

### 📊 2. Natija (Result)
1. **Python Konveyer Kuzatuv Dvigateli (`conveyor_tracking_sorter.py`):**
   - Enkoder impulslari orqali lentaning chiziqli siljishini hisoblash ($\Delta s = N \cdot \pi D / CPR$).
   - Dinamik nishon pozitsiyasi: $\mathbf{P}(t) = \mathbf{P}_0 + \mathbf{v}_{conv} \cdot \Delta t$.
   - Sinxron kuzatuv oynasi ($[X_{min}, X_{max}]$) holat mashinasi (Approaching, In Window, Missed).
2. **KRL Ishlab chiqarish dasturi (`CONVEYOR_TRACK.src` va `CONVEYOR_TRACK.dat`):**
   - Dinamik baza yangilanishi (`$BASE = BASE_DATA[2] : fDynamicOffset`), pnevmatik tutqich va ikki yo'nalishli saralovchi palletizatsiya (`PLACE_PALLET_A()`, `PLACE_PALLET_B()`).
3. **Pytest Unit Testlari (`test_conveyor.py`):**
   - Enkoder masshtablash omili va oyna chegaralari filtrlari (2/2 test o'tdi).

---

### 🧮 3. Matematik apparat (Mathematics)

$$s(t) = N_{pulses} \cdot \frac{\pi D_{pulley}}{N_{cpr}}, \quad \mathbf{P}(t) = \mathbf{P}_0 + [v_{conv} \Delta t, 0, 0]^T, \quad X_{min} \le P_x(t) \le X_{max}$$

To'liq nazariya va matematik isbotlar [**docs/derivations.md**](./docs/derivations.md) da berilgan.

---

### 💻 4. Ishga tushirish va tekshirish (Execution & Verification)

Python simulyatorini tekshirish:
```bash
uv run --with numpy python src/scripts/conveyor_tracking_sorter.py
```

Konsol chiqishi:
```
=================================================================
Lesson 25: Conveyor Tracking (Line Tracking) & Sorting System
=================================================================

Conveyor Speed: 200.0 mm/s
Tracking Window X: [300.0, 700.0] mm

Time t = 0.5 s:
  Part Pos: [200.0, 250.0, 150.0] mm
  In Tracking Window: False
  Distance to Window Exit: 500.00 mm

Time t = 1.5 s:
  Part Pos: [400.0, 250.0, 150.0] mm
  In Tracking Window: True
  Distance to Window Exit: 300.00 mm

Time t = 2.5 s:
  Part Pos: [600.0, 250.0, 150.0] mm
  In Tracking Window: True
  Distance to Window Exit: 100.00 mm

Time t = 3.5 s:
  Part Pos: [800.0, 250.0, 150.0] mm
  In Tracking Window: False
  Distance to Window Exit: 0.00 mm
```

Unit testlarni bajarish:
```bash
uv run --with numpy --with pytest pytest src/scripts/test_conveyor.py
```
Natija: `2 passed in 0.11s`.

---

🔗 **[Bosh Mundarija / Return to Master Syllabus](https://github.com/muzaffarbekmustafayev/kuka-industrial-robotics-syllabus)**
