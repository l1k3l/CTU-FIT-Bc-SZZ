---
aliases: [mocninná metoda, mocninné metody, mocninnou metodou, mocninné metodě, power iteration, dominantní vlastní číslo, dominantního vlastního čísla, rayleighův podíl, rayleighova podílu, inverzní mocninná metoda, posunutá mocninná metoda]
tags: [definice, kurz/LA2]
---

# Mocninná metoda

## Definice

**Mocninná metoda** (power iteration) je iterační metoda pro výpočet **dominantního** [[Vlastní-číslo|vlastního čísla]] matice $A \in \mathbb{R}^{n,n}$ a jemu příslušného vlastního vektoru. Dominantní vlastní číslo je v absolutní hodnotě největší.

Iteruje se posloupnost znormovaných vektorů
$$\frac{x}{\|x\|_2},\ \frac{Ax}{\|Ax\|_2},\ \frac{A^2 x}{\|A^2 x\|_2},\ \dots, \qquad v^{(k)} := \frac{A^k x}{\|A^k x\|_2} = \frac{A v^{(k-1)}}{\|A v^{(k-1)}\|_2},$$
tj. v každém kroku: vynásob maticí $A$ a [[Norma|znormuj]].

## Konvergence

Předpoklad: dominantní vlastní číslo $\lambda_1$ je **jednoduché** v absolutní hodnotě, tj. $|\lambda_1| > |\lambda_2| \ge \dots \ge |\lambda_n|$, a startovní vektor $x$ není kolmý na příslušný vlastní vektor $q_1$ ($\alpha_1 \neq 0$ v rozkladu do báze vlastních vektorů).

Pak (až na znaménko / násobek)
$$\frac{A^k x}{\|A^k x\|_2} \to q_1.$$
**Idea:** v bázi vlastních vektorů $x = \sum_i \alpha_i q_i$ je $A^k x = \lambda_1^k\big(\alpha_1 q_1 + \sum_{i\ge2}\alpha_i (\lambda_i/\lambda_1)^k q_i\big)$; protože $|\lambda_i/\lambda_1| < 1$, ostatní členy vymizí a prosadí se $q_1$.

**Rychlost konvergence** je dána poměrem $\left|\dfrac{\lambda_2}{\lambda_1}\right|$ (lineární konvergence vlastního vektoru). Selhává, pokud dominantní vlastní číslo není jednoduché v absolutní hodnotě (např. $\lambda = 1, -1$ — posloupnost osciluje).

## Rayleighův podíl

Pro odhad samotného vlastního čísla z aproximace vlastního vektoru slouží **Rayleighův podíl**
$$r(y) = \frac{y^T A y}{y^T y}, \qquad y \neq \theta.$$
Pro skutečný vlastní vektor $x$ (k $\lambda$) platí $r(x) = \lambda$. Pro symetrické matice $\lambda^{(k)} = r(v^{(k)})$ konverguje k $\lambda_1$ rychleji (řád $|\lambda_2/\lambda_1|^{2k}$) než samotný vlastní vektor.

## Varianty a využití

- **Inverzní mocninná metoda:** aplikace mocninné metody na $A^{-1}$ najde vlastní číslo **nejmenší** v absolutní hodnotě (dominantní vlastní číslo $A^{-1}$ je $1/\lambda_{\min}$).
- **Posunutá (inverzní) iterace:** aplikace na $(A - \mu E)^{-1}$ s odhadem $\mu$ najde vlastní číslo nejbližší $\mu$; iterace Rayleighova podílu volí $\mu$ adaptivně.
- **Deflace:** pro další vlastní čísla symetrické matice se iteruje v ortogonálním doplňku již nalezených vlastních vektorů.
- Vhodná pro **řídké** či implicitně zadané matice (stačí umět spočítat $Av$) a pro výpočet jen dominantního páru. Aplikace: PageRank.

## Související

- [[Vlastní-číslo]]
- [[QR-algoritmus]]
- [[Norma]]
- [[Spektrální-rozklad]]
