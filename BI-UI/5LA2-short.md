---
tags: [otázka, kurz/LA2, otázka/5, todo]
---

# 5 — QR rozklad a metoda nejmenších čtverců (zkrácená verze)

## 1. Ortogonální matice

$Q \in \mathbb{R}^{n,n}$ **ortogonální** $\iff Q^TQ = QQ^T = E \iff Q^{-1} = Q^T$. Sloupce tvoří ON bázi. Obecněji **ON sloupce:** $Q \in \mathbb{R}^{m,n}$, $Q^TQ = E_n$.

**Vlastnosti:** zachovává skalární součin $(Qx)^T(Qy)=x^Ty$ i normu $\|Qx\|_2 = \|x\|_2$; $\det Q = \pm1$; $|\lambda|=1$ (komplexní možné); $\kappa_2(Q)=1$ (nezvětšuje zaokrouhlovací chyby — proto v numerice); součin OG je OG.

## 2. QR rozklad

[[QR-rozklad]] matice $A \in \mathbb{R}^{m,n}$, $m\ge n$:
- **redukovaný** $A = \hat{Q}\hat{R}$: $\hat{Q}\in\mathbb{R}^{m,n}$ ON sloupce, $\hat{R}\in\mathbb{R}^{n,n}$ horní trojúhelníková;
- **úplný** $A = QR$: $Q\in\mathbb{R}^{m,m}$ ortogonální, $R\in\mathbb{R}^{m,n}$ horní trojúh. (posl. $m-n$ řádků nul).

Z redukovaného → úplný: doplnit $\hat{Q}$ o ON bázi $\langle q_1,\dots,q_n\rangle^\perp$.

**Existence:** každá $A$ ($m\ge n$). **Jednoznačnost:** při $h(A)=n$ a $r_{jj}>0$ právě jeden redukovaný.

## 3. Výpočet QR — tři metody

- **Gramův–Schmidt:** ortogonalizace sloupců, $a_j = \sum_{i\le j} r_{ij}q_i$, $r_{ij}=q_i^Ta_j$, $r_{jj}=\|z_j\|$. Dává přímo $\hat{Q}$. Klasický **nestabilní**, modifikovaný **stabilní**. $\sim 2mn^2$.
- **Householder (zrcadlení):** reflektor $F = E - \tfrac{2}{\|v\|^2}vv^T$ s $v = \operatorname{sgn}(x_1)\|x\|e_1 + x$ vynuluje **celý sloupec** pod diagonálou najednou; $R = Q^TA = Q_n\cdots Q_1A$. $\det F = -1$.
- **Givens (rotace):** $G = \begin{psmallmatrix}c&s\\-s&c\end{psmallmatrix}$, $c=\tfrac{x_i}{\sqrt{x_i^2+x_j^2}}$, $s=\tfrac{x_j}{\sqrt{x_i^2+x_j^2}}$ vynuluje **jeden prvek** (řádky $i,j$); $\det G = 1$.

| metoda | nuluje | složitost | vhodná pro |
|---|---|---|---|
| Gram–Schmidt | — (ortogonalizace) | $\sim 2mn^2$ | dává $\hat{Q}$; modif. = stabilní |
| Householder | celý sloupec | $2mn^2-\tfrac23 n^3$ | plné matice (nejméně op.) |
| Givens | jeden prvek | $\sim 3mn^2-n^3$ | řídké matice, paralelizace |

Princip triangularizace: najdi OG $Q_i$, aby $Q_k\cdots Q_1 A = R$; pak $Q^T=Q_k\cdots Q_1$, $A=QR$ (součin OG je OG). $Q$ se nekonstruuje explicitně.

## 4. Metoda nejmenších čtverců

Přeurčená soustava $Ax=b$ ($m>n$, obvykle bez řešení). [[Metoda-nejmenších-čtverců|MNČ]]: hledáme $x$ minimalizující $\|b-Ax\|_2$ (reziduum).

**Normální rovnice:** $x$ řeší MNČ $\iff$
$$A^TA\,x = A^Tb, \qquad (h(A)=n:\ x = (A^TA)^{-1}A^Tb).$$

**Geometrie:** $Ax = \operatorname{proj}_{\operatorname{Im}A}b$ (ortogonální projekce $b$ na sloupcový prostor). Reziduum $b-Ax \perp \operatorname{Im}A$, tj. $A^T(b-Ax)=\theta$ → odtud normální rovnice. Vždy řešitelná; jediné řešení $\iff h(A)=n$.

## 5. MNČ pomocí QR

$\operatorname{proj}_{\operatorname{Im}A}b = \hat{Q}\hat{Q}^Tb$, dosadíme $A=\hat{Q}\hat{R}$ a vynásobíme $\hat{Q}^T$:
$$\boxed{\hat{R}\,x = \hat{Q}^T b} \quad\text{(zpětná substituce)}, \qquad \min\|b-Ax\| = \|Q'^Tb\|.$$

**Proč stabilnější než normální rovnice:** $A^TA$ má $\kappa = \kappa(A)^2$ (velká ztráta přesnosti), kdežto QR pracuje jen s OG transformacemi ($\kappa_2(Q)=1$, nezvětšují chyby), podmíněnost zůstává $\kappa(A)$. Cena: ~2× více operací. Pro nejhorší úlohy [[SVD]].

---

## Co odpovědět rychle

- **OG matice:** $Q^TQ=E$, zachovává normu i skalární součin, $\det=\pm1$, $\kappa_2=1$.
- **QR:** $A=QR$, $Q$ OG/ON sloupce, $R$ horní trojúh.; existuje vždy ($m\ge n$).
- **Výpočet:** Gram–Schmidt (stabilní modif.), Householder (celý sloupec, plné matice), Givens (1 prvek, řídké/paralelně).
- **MNČ:** minimalizuj $\|b-Ax\|$; normální rovnice $A^TAx=A^Tb$; geometricky projekce $b$ na $\operatorname{Im}A$, reziduum $\perp$.
- **MNČ přes QR:** $\hat{R}x=\hat{Q}^Tb$ — stabilnější ($\kappa(A)$ vs. $\kappa(A)^2$ u norm. rovnic).
