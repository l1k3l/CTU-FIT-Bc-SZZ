---
tags: [otázka, kurz/ML2, otázka/16, todo]
---

# 16 — Metoda podpůrných vektorů (SVM) (zkrácená verze)

## 1. Diskriminační funkce

Binární klasifikace $Y\in\{-1,1\}$. **Lineární diskriminační funkce**
$$f(x)=w^T\varphi(x)+w_0,\qquad \hat Y(x)=\operatorname{sgn}f(x).$$
**Hranice** $w^Tu+w_0=0$ = nadrovina, normála $w$, vzdálenost od počátku $d=-\frac{w_0}{\lVert w\rVert}$.

**Signovaná vzdálenost** bodu od hranice: $r=\dfrac{f(x)}{\lVert w\rVert}$. Znaménko $f$ dělí prostor na poloprostory ($\hat Y=\pm1$).

## 2. Princip největšího odstupu (hard margin)

Pro lineárně separabilní data vyber nadrovinu s **největším odstupem** (margin = vzdálenost k nejbližšímu bodu).
$$\max_{w,w_0}\min_i \frac{Y_i(w^T\varphi(x_i)+w_0)}{\lVert w\rVert}.$$
Normalizace škály: pro nejbližší bod $Y_j f(x_j)=1$ → $\forall i:\ Y_i f(x_i)\ge1$, odstup $=\frac1{\lVert w\rVert}$.

**Úloha (QP):** $\displaystyle\min_{w,w_0}\tfrac12\lVert w\rVert^2$ za $Y_i(w^T\varphi(x_i)+w_0)\ge1\ \forall i$. Konvexní → globální optimum.

**Podpůrné vektory** = body s aktivní vazbou ($Y_if(x_i)=1$) → určují polohu nadroviny. Odtud název SVM.

## 3. Neseparabilní případ (soft margin)

**Uvolněné proměnné** $\xi_i\ge0$: měkká podmínka $Y_if(x_i)\ge1-\xi_i$. ($\xi_i=0$ vně pásu správně; $0<\xi_i\le1$ uvnitř pásu; $\xi_i>1$ chyba.) $\sum_i\xi_i$ = mez počtu chyb.
$$\min_{w,w_0,\xi}\tfrac12\lVert w\rVert^2+C\sum_i\xi_i,\quad \xi_i\ge0,\ Y_if(x_i)\ge1-\xi_i.$$
**$C$:** větší $C$ = **slabší** regularizace (méně chyb, riziko přeučení); malé $C$ = silná regularizace. $C=\frac1{\nu N}$ → $\nu$-SVM ($\nu$ = podíl chyb).

## 4. Duál + jádrový trik

$$\max_a\ \sum_i a_i-\tfrac12\sum_{i,j}a_ia_jY_iY_j\,k(x_i,x_j),\quad 0\le a_i\le C,\ \sum_i a_iY_i=0,$$
[[Jádrová-funkce|jádro]] $k(x_i,x_j)=\varphi(x_i)^T\varphi(x_j)$ → body jen ve skalárních součinech → **jádrový trik** (nelineární SVM, např. RBF).

$w=\sum_j a_jY_j\varphi(x_j)$ → **jádrový model**
$$f(x)=\sum_{j}a_jY_j\,k(x,x_j)+w_0,\qquad \hat Y=\operatorname{sgn}f(x).$$

**Vlastnosti:** řešení **řídké** ($a_j=0$ pro správně klasifikované mimo pás); podpůrné vektory = $a_j>0$ ($0<a_j<C$ na hraně pásu, $a_j=C$ uvnitř/chyba). Větší $C$ → řidší.

---

## Co odpovědět rychle
- **Diskriminační funkce** $f(x)=w^T\varphi(x)+w_0$, hranice = nadrovina, vzdálenost $r=f(x)/\lVert w\rVert$.
- **Largest margin** → normalizace → **min $\tfrac12\lVert w\rVert^2$ s.t. $Y_if(x_i)\ge1$** (QP).
- **Soft margin:** $+C\sum\xi_i$, $Y_if(x_i)\ge1-\xi_i$; velké $C$ = slabá regularizace.
- **Duál** $\max_a \sum a_i-\tfrac12\sum a_ia_jY_iY_jk(x_i,x_j)$ → **jádrový trik** → nelineární.
- **Výsledek:** $f(x)=\sum_j a_jY_jk(x,x_j)+w_0$, řídké, **podpůrné vektory** = $a_j>0$.
