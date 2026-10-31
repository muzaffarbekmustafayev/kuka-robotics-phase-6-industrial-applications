# 3D Fazoviy Egri Chiziqlarni Payvandlash va Frenet-Serret Reperi

## 1. Fazoviy Egri Chiziqning Frenet-Serret Reperi
3D fazoda berilgan differensiallanuvchi egri chiziq $\mathbf{r}(s) \in \mathbb{R}^3$ ($s$ — yoy uzunligi parametri) bo'ylab asbobning harakat yo'nalishini aniqlash uchun Frenet-Serret reperi quriladi:

1. **Urinma vektor (Tangent):**
   $$\mathbf{T}(s) = \frac{d\mathbf{r}}{ds}, \quad \|\mathbf{T}(s)\| = 1$$
2. **Bosh normal vektor (Principal Normal):**
   $$\frac{d\mathbf{T}}{ds} = \kappa(s) \mathbf{N}(s) \implies \mathbf{N}(s) = \frac{1}{\kappa(s)} \frac{d\mathbf{T}}{ds}$$
   bu yerda $\kappa(s) = \|\mathbf{r}''(s)\|$ — egri chiziqning egriligi (curvature).
3. **Binormal vektor (Binormal):**
   $$\mathbf{B}(s) = \mathbf{T}(s) \times \mathbf{N}(s)$$

Ortogonal yo'nalish matritsasi:
$$R_{frenet}(s) = [\mathbf{T}(s), \mathbf{N}(s), \mathbf{B}(s)] \in SO(3)$$

---

## 2. Payvandlash Mash'alasi Orientatsiyasi (Lead and Tilt Angles)
Payvandlashda suyuqlantirilgan metall vannasini to'g'ri shakllantirish uchun gorelkaga hujum burchagi (Lead angle $\alpha_{lead}$) va yon qiyalik (Tilt angle $\beta_{tilt}$) beriladi:

$$R_{torch}(s) = R_{frenet}(s) \cdot R_y(\beta_{tilt}) \cdot R_x(\alpha_{lead})$$

---

## 3. Germetik Dozatorning Oqim Tezligi Balansi
Avtomobil oynalari va batareya bloklarini germetik yelimlashda chokning qalinligi bir xil bo'lishi shart. Hajmiy oqim tezligi robot chiziqli harakat tezligiga mutanosib ravishda boshqariladi:

$$\dot{Q}(t) = v_{tcp}(t) \cdot A_{bead}$$
bu yerda $A_{bead} = \frac{\pi \cdot w \cdot h}{4}$ — yelim chokining ko'ndalang kesim yuzi.
Tezlik oshganda oqim mutanosib oshiriladi, sekinlashuvda esa kamaytiriladi, bu esa chokning butun uzunlik bo'ylab bir xil sifatli bo'lishini ta'minlaydi. $\blacksquare$
