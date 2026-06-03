---
aliases: [norma, normy, normu, normou, norem, norma vektoru, normou vektoru, eukleidovská norma, 2-norma, p-norma, velikost vektoru]
tags: [definice, kurz/LA2]
---

# Norma

Tato poznámka popisuje **vektorovou normu**. Maticové normy (kap. 7 BI-LA2) jsou samostatný pojem.

## Definice

Buď $V$ vektorový prostor nad $T = \mathbb{R}$ nebo $\mathbb{C}$. **Norma** je zobrazení $\|\cdot\| : V \to \mathbb{R}$, které pro všechna $x, y \in V$ a $\alpha \in T$ splňuje axiomy:

1. **Nezápornost:** $\|x\| \ge 0$.
2. **Definitnost:** $\|x\| = 0 \iff x = \theta$.
3. **Homogenita v absolutní hodnotě:** $\|\alpha x\| = |\alpha|\cdot\|x\|$.
4. **Trojúhelníková nerovnost:** $\|x + y\| \le \|x\| + \|y\|$.

Číslo $\|x\|$ se nazývá **velikost vektoru** $x$; číslo $d(x,y) := \|x - y\|$ je **vzdálenost** vektorů $x$ a $y$.

## Norma indukovaná skalárním součinem

V prostoru se [[Skalární-součin|skalárním součinem]] $\mathcal{H}$ definujeme normu
$$\|x\| := \sqrt{\langle x\mid x\rangle}.$$
Toto zobrazení je vždy normou: axiomy 1–3 plynou přímo z axiomů skalárního součinu, axiom 4 (trojúhelníková nerovnost) je důsledkem Cauchyho–Schwarzovy nerovnosti $|\langle x\mid y\rangle| \le \|x\|\|y\|$.

## p-normy

Na $T^n$ definujeme pro $p \in \langle 1, \infty\rangle$ **$p$-normu** ($x = (x_1, \dots, x_n)$):
$$\|x\|_p = \begin{cases} \big(|x_1|^p + \cdots + |x_n|^p\big)^{1/p} & p < \infty, \\ \max\{|x_1|, \dots, |x_n|\} & p = \infty. \end{cases}$$

| norma | předpis | význam |
|---|---|---|
| **1-norma** | $\|x\|_1 = \sum_j \lvert x_j\rvert$ | součtová (manhattanská) |
| **2-norma** (eukleidovská) | $\|x\|_2 = \big(\sum_j \lvert x_j\rvert^2\big)^{1/2}$ | indukovaná standardním součinem; přímá vzdálenost |
| **$\infty$-norma** (maximová) | $\|x\|_\infty = \max_j \lvert x_j\rvert$ | největší složka v abs. hodnotě |

Eukleidovská norma je norma indukovaná standardním (eukleidovským) skalárním součinem.

## Související

- [[Skalární-součin]]
