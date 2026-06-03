---
tags: [otázka, kurz/LA2, otázka/7, todo]
---

# 7 — Singulární rozklad (SVD) (zkrácená verze)

## 1. Definice

**SVD** matice $A \in \mathbb{R}^{m,n}$:
$$A = U \Sigma V^T,$$
- $U \in \mathbb{R}^{m,m}$ [[Ortogonální-matice|ortogonální]] (sloupce = **levé** sing. vektory $u_i$),
- $V \in \mathbb{R}^{n,n}$ ortogonální (sloupce = **pravé** sing. vektory $v_i$),
- $\Sigma \in \mathbb{R}^{m,n}$ diagonální, na diagonále $p = \min(m,n)$ **singulárních čísel** $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_p \ge 0$.

Platí $A v_i = \sigma_i u_i$. **Plný** tvar: $U, V$ čtvercové ortogonální. **Redukovaný (úsporný)** ($m \ge n$): $\hat U \in \mathbb{R}^{m,n}$ s ON sloupci, $\hat\Sigma \in \mathbb{R}^{n,n}$, $V \in \mathbb{R}^{n,n}$; $A = \hat U\hat\Sigma V^T$.

**Existence:** SVD má **každá** matice $A \in \mathbb{R}^{m,n}$.
*Idea důkazu:* $\sigma_1 = \lVert A\rVert_2$, najdi $v_1, u_1$ s $Av_1 = \sigma_1 u_1$, doplň na ON báze → blok $\binom{\sigma_1\ \ w^T}{\theta\ \ B}$, z vlastnosti 2-normy $w = \theta$, na $B$ indukce.

**Geometrie:** obraz jednotkové sféry je hyperelipsa s poloosami $\sigma_i u_i$; $\sigma_i$ = škálování, $u_i$ = směry, $v_i$ = vzory poloos.

## 2. Vlastnosti

- **Vztah k vlastním číslům:** nenulová $\sigma_i = \sqrt{\lambda_i(A^TA)}$ (= $\sqrt{\lambda_i(AA^T)}$).
  $V$ = ON báze [[Vlastní-číslo|vlastních vektorů]] $A^TA$; $U$ = ON báze vl. vektorů $AA^T$.
  *(Idea: $A^TA = V\Sigma^T\Sigma V^T$ je diagonalizace $A^TA$.)*
- **Hodnost** $h(A) = r$ = počet nenulových $\sigma_i$. *(Idea: $h(A) = h(\Sigma)$, ortog. násobení nemění hodnost.)*
- **Normy:** $\lVert A\rVert_2 = \sigma_1$, $\lVert A\rVert_F = \sqrt{\sigma_1^2 + \cdots + \sigma_r^2}$ (viz [[Norma]]).
- **Báze:** $\operatorname{Im}A = \langle u_1,\dots,u_r\rangle$, $\ker A = \langle v_{r+1},\dots,v_n\rangle$.
- **vs. [[Spektrální-rozklad|spektrální rozklad]]:** SVD má dvě ON báze ($U \ne V$), existuje vždy, pro každou matici; spektrální má jednu (ne nutně ON) bázi, jen pro čtvercové, ne vždy. Pro symetrickou $A$: $\sigma_i = |\lambda_i|$.
- **Jednoznačnost:** $\sigma_i$ jednoznačné; pro jednoduché nenulové $\sigma_i$ je $v_i$ (a tím $u_i$) určen až na znaménko.

**Aproximace nízké hodnosti (Eckart–Young):** $A = \sum_{j=1}^r \sigma_j u_j v_j^T$ (matice hodnosti 1). Ořezání
$$A_\nu = \sum_{j=1}^\nu \sigma_j u_j v_j^T$$
je **nejlepší** aproximace hodnosti $\le \nu$ v 2-normě (i Frobeniově): $\lVert A - A_\nu\rVert_2 = \sigma_{\nu+1}$. *(Použití: komprese, šum, ML.)*

**Pseudoinverze:** $A^+ = V\Sigma^+ U^T$ (invertujeme **nenulová** $\sigma_i$). Pro regulární $A$: $A^{-1} = V\Sigma^{-1}U^T$, $\kappa(A) = \sigma_1/\sigma_n$. Řeší [[Metoda-nejmenších-čtverců|nejmenší čtverce]] $x = A^+b$.

## 3. Výpočet

**Ručně (přes $A^TA$):**
1. spočti $A^TA$ (nebo $AA^T$ — tu menší);
2. vlastní čísla $\lambda_i$ seřaď sestupně → $\sigma_i = \sqrt{\lambda_i}$ na diagonálu $\Sigma$;
3. $V$ = **ON báze** vlastních podprostorů $A^TA$ (pozor: u násobných / nuly nestačí znormalizovat);
4. $u_j = \tfrac{1}{\sigma_j} A v_j$ z $AV = U\Sigma$; chybějící sloupce $U$ doplň na ON bázi.

**Numericky (velké matice):** ne přes $A^TA$ (zvětšuje chybu). Dvě fáze: (1) Golubova–Kahanova **bidiagonalizace** (Householder, ortog. zleva/zprava — nemění $\sigma_i$); (2) iterace (QR / divide-and-conquer) na diagonální tvar.

---

## Co odpovědět rychle

- **Definice:** $A = U\Sigma V^T$, $U,V$ ortogonální, $\Sigma$ diagonální s $\sigma_1 \ge \cdots \ge 0$. Existuje pro každou matici.
- **Singulární čísla** = $\sqrt{\text{vlastní čísla } A^TA}$; $V$ z vl. vektorů $A^TA$, $U$ z $AA^T$.
- **Hodnost** = počet nenulových $\sigma_i$; $\lVert A\rVert_2 = \sigma_1$.
- **Eckart–Young:** ořezání na $\nu$ největších $\sigma$ = nejlepší aproximace hodnosti $\nu$ v 2-normě.
- **Pseudoinverze** $A^+ = V\Sigma^+U^T$; inverze regulární $A^{-1} = V\Sigma^{-1}U^T$.
- **Výpočet:** ručně diagonalizace $A^TA$; numericky bidiagonalizace + QR iterace.
