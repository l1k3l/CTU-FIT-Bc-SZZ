---
aliases: [metrika, metriky, metriku, metrikou, metrice, metrik, metrikám, metrikami, vzdálenostní funkce, metrický prostor]
tags: [definice, kurz/ML1]
---

# Metrika

## Definice

**Metrika** (též *vzdálenost*) na množině $\mathcal{X}$ je funkce $d : \mathcal{X} \times \mathcal{X} \to [0, +\infty)$ taková, že pro každé $x, y, z \in \mathcal{X}$ platí:

1. $d(x,y) \ge 0$ a $d(x,y) = 0 \iff x = y$ — **pozitivní definitnost**,
2. $d(x,y) = d(y,x)$ — **symetrie**,
3. $d(x,y) \le d(x,z) + d(z,y)$ — **trojúhelníková nerovnost**.

Dvojici $(\mathcal{X}, d)$ nazýváme **metrický prostor**.

> Jde o pojem *metrického prostoru* (vzdálenostní funkce na obecné množině), **odlišný** od grafové vzdálenosti (délka nejkratší cesty) — viz [[Vzdálenost]].

## Příklady metrik

Na $\mathbb{R}^p$ pro $x = (x_1,\dots,x_p)$, $y = (y_1,\dots,y_p)$:

| metrika | předpis |
|---|---|
| **eukleidovská** $L_2$ | $d_2(x,y) = \sqrt{\sum_{i=1}^p (x_i-y_i)^2}$ |
| **manhattanská** $L_1$ | $d_1(x,y) = \sum_{i=1}^p \lvert x_i-y_i\rvert$ |
| **Čebyševova** $L_\infty$ | $d_\infty(x,y) = \max_i \lvert x_i-y_i\rvert$ |
| **Minkowského** $L_q$ ($q\ge 1$) | $d_q(x,y) = \big(\sum_i \lvert x_i-y_i\rvert^q\big)^{1/q}$ |

Eukleidovská metrika je indukována standardním [[Skalární-součin|skalárním součinem]], $d_2(x,y) = \|x-y\|_2$ (viz [[Norma]]).

Na řetězcích: **Levenštejnova (editační) vzdálenost** — minimální počet vložení/smazání/nahrazení znaků. Pro porovnání směru vektorů se používá **kosinová** míra $\frac{\langle x\mid y\rangle}{\|x\|_2\,\|y\|_2}$; ta sama o sobě **není** metrika (porušuje axiomy), bývá označována jen jako *míra (ne)podobnosti*.

## Související

- [[Norma]]
- [[Skalární-součin]]
- [[Vzdálenost]] (grafová — jiný význam!)
- [[Shluková-analýza]]
