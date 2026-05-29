---
aliases: [determinant, determinantu, determinantem, determinanty, determinantů, determinantech, det]
tags: [definice, kurz/LA1]
---

# Determinant

## Definice

**Determinant** přiřazuje čtvercové matici $A \in T^{n,n}$ skalár $\det A \in T$. Definuje se přes permutace,
$$\det A = \sum_{\pi \in S_n} \operatorname{sgn}(\pi) \prod_{i=1}^{n} a_{i,\pi(i)},$$
v praxi se počítá rozvojem nebo GEM (viz níže).

## Výpočet

- **Trojúhelníková matice:** $\det A = \prod_i a_{ii}$ (součin prvků na diagonále).
- **[[Gaussova-eliminace|GEM]]:** převedeme na horní trojúhelníkový tvar; úprava (G3) determinant nemění, prohození řádků (G1) mění znaménko, vynásobení řádku (G2) číslem $\alpha$ jej násobí $\alpha$. Složitost $O(n^3)$.
- **Laplaceův rozvoj** podle $k$-tého sloupce: $\det A = \sum_{i=1}^{n} (-1)^{i+k} a_{ik} \det A(i,k)$, kde $A(i,k)$ vznikne vynecháním $i$-tého řádku a $k$-tého sloupce.

## Vlastnosti

- $\det A \neq 0 \iff A$ je [[Regulární-matice|regulární]];
- $\det(AB) = \det A \cdot \det B$;
- $\det(A^T) = \det A$;
- $\det(A^{-1}) = (\det A)^{-1}$;
- podobné matice mají stejný determinant.

## Použití

- kritérium [[Regulární-matice|regularity]];
- [[Vlastní-číslo|charakteristický polynom]] $p_A(\lambda) = \det(A - \lambda E)$.

## Související

- [[Regulární-matice]]
- [[Vlastní-číslo]]
- [[Gaussova-eliminace]]
- [[Matice]]
