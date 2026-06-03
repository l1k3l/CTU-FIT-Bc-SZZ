---
aliases: [ortogonální matice, ortogonální matici, ortogonální maticí, ortogonálních matic, ortogonální matice, unitární matice, matice s ortonormálními sloupci]
tags: [definice, kurz/LA2]
---

# Ortogonální matice

## Definice

Čtvercovou matici $Q \in \mathbb{R}^{n,n}$ nazýváme **ortogonální** (zkráceně **OG matice**), pokud platí
$$Q^T Q = Q Q^T = E_n, \qquad \text{ekvivalentně} \qquad Q^{-1} = Q^T,$$
tedy transpozice ortogonální matice je zároveň její inverzí.

Obecnější pojem je **matice s ortonormálními sloupci**: matice $Q \in \mathbb{R}^{m,n}$ ($m \ge n$) s vlastností $Q^T Q = E_n$. Pro $Q_{:i} \cdot Q_{:j} = \delta_{ij}$ (Kroneckerovo delta), tj. sloupce tvoří ortonormální soubor. Ortogonální matice je čtvercová matice s ortonormálními sloupci (a díky čtvercovosti i s ortonormálními řádky).

## Vlastnosti

Pro ortogonální $Q \in \mathbb{R}^{n,n}$ a vektory $x, y \in \mathbb{R}^n$:

- **Zachování skalárního součinu:** $(Qx)^T(Qy) = x^T y$ — proto „ortogonální“: $x \perp y \Rightarrow Qx \perp Qy$.
- **Zachování (eukleidovské) [[Norma|normy]]:** $\|Qx\|_2 = \|x\|_2$ (izometrie).
- **Determinant:** $\det Q = \pm 1$ (z $(\det Q)^2 = 1$). Hodnota $+1$ odpovídá rotaci, $-1$ zrcadlení.
- **Vlastní čísla** mají $|\lambda| = 1$ (mohou být i komplexní, např. matice rotace).
- **Číslo podmíněnosti** $\kappa_2(Q) = 1$; násobení OG maticí nezvětší zaokrouhlovací chyby — proto velký význam v numerice.
- **Invariance maticových norem:** $\|QA\|_2 = \|A\|_2 = \|AR\|_2$ a totéž pro Frobeniovu normu $\|\cdot\|_F$.
- **Součin** dvou ortogonálních matic je ortogonální: $(Q_1 Q_2)^{-1} = Q_2^T Q_1^T = (Q_1 Q_2)^T$.
- **Transpozice** $Q^T$ je opět ortogonální.

## Příklady

- Matice **rotace** v $\mathbb{R}^2$: $\begin{pmatrix}\cos\varphi & \sin\varphi \\ -\sin\varphi & \cos\varphi\end{pmatrix}$ ($\det = 1$).
- Matice **zrcadlení** (Householderův reflektor) $E - \tfrac{2}{\|v\|_2^2} v v^T$ ($\det = -1$).

## Související

- [[QR-rozklad]]
- [[Ortogonální-báze]]
- [[Norma]]
- [[Skalární-součin]]
- [[Matice]]
