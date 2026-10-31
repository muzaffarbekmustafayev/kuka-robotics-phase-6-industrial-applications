# Dinamik Konveyer Kuzatish (Line Tracking) va Saralash Matematikasi

## 1. Enkoder Impulslari va Chiziqli Siljish
Konveyer harakatini robotga sinxronlashtirish uchun yetakchi valga o'rnatilgan inkremental enkoder impulslari ishlatiladi:

$$s_{conv}(t) = N_{ticks}(t) \cdot \frac{\pi \cdot D_{pulley}}{N_{cpr}}$$

bu yerda:
- $D_{pulley}$ — lenta vali diametri;
- $N_{cpr}$ — enkoderning bir aylanishdagi impulslari (Counts Per Revolution);
- $\Delta s_{pulse} = \frac{\pi D}{N_{cpr}}$ — bitta impulsning metrik o'lchami (resolution).

---

## 2. Dinamik Obyekt Pozitsiyasi va Sinxron Ushlash
Fotosensor nurni kesib o'tgan vaqt $t_0$ da obyektning boshlang'ich pozitsiyasi $\mathbf{P}_0 = [X_0, Y_0, Z_0]^T$ bo'lsin.
Konveyer bo'ylab doimiy $v_{conv}$ tezlikda harakatlanayotgan obyektning $t$ paytidagi pozitsiyasi:

$$\mathbf{P}_{target}(t) = \mathbf{P}_0 + \begin{bmatrix} v_{conv} \cdot (t - t_0) \\ 0 \\ 0 \end{bmatrix}$$

Robot $t_{pick}$ paytida ushlashni amalga oshirish uchun uning TCP nuqtasi harakat yo'nalishidagi tezlikka tenglashishi kerak:
$$\mathbf{v}_{tcp}(t_{pick}) = [v_{conv}, 0, 0]^T$$

---

## 3. Dinamik Kuzatish Oynasi (Tracking Window $[X_{min}, X_{max}]$)
Manipulyator faqat uning ishchi xavfsiz zonasiga kiruvchi masofada sinxronlasha oladi:

$$\chi_{valid}(t) = \begin{cases} 
1, & \text{agar } X_{min} \le P_{target, x}(t) \le X_{max} \\
0, & \text{aksincha (Missed yoki Approaching)}
\end{cases}$$

Obyekt $X_{max}$ dan o'tib ketsa, robot to'xtatilib, xatolik qayd etiladi va konveyer datchigi keyingi detalni kutadi. $\blacksquare$
