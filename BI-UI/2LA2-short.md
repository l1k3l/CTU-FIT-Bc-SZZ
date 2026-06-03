---
tags: [otázka, kurz/LA2, otázka/2, todo]
---

# 2 — Skalární součin a norma vektoru (zkrácená verze)

$V$ je VP nad $T = \mathbb{R}$ nebo $\mathbb{C}$; $\theta$ nulový vektor; $\overline{z}$ komplexně sdružené. Značíme $\langle x \mid y\rangle$, $\|x\|$, $\mathcal{H} = (V, \langle\,\cdot\mid\cdot\,\rangle)$.

## 1. Skalární součin

**Def.** $\langle\,\cdot\mid\cdot\,\rangle : V \times V \to T$ je [[Skalární-součin|skalární součin]], platí-li pro $x,y,z \in V$, $\alpha \in T$:

1. **linearita ve 2. arg.:** $\langle x \mid y+z\rangle = \langle x\mid y\rangle + \langle x\mid z\rangle$, $\quad \langle x \mid \alpha y\rangle = \alpha\langle x\mid y\rangle$;
2. **hermitovská symetrie:** $\langle x\mid y\rangle = \overline{\langle y\mid x\rangle}$ (na $\mathbb{R}$ jen $\langle x\mid y\rangle = \langle y\mid x\rangle$);
3. **pozitivní definitnost:** $\langle x\mid x\rangle \ge 0$ a $\langle x\mid x\rangle = 0 \iff x = \theta$.

$\mathcal{H} = (V, \langle\,\cdot\mid\cdot\,\rangle)$ = **prehilbertův prostor**. Na $\mathbb{C}$ je sdružení v ax. 2 nutné, aby $\langle x\mid x\rangle \in \mathbb{R}$.

**Vlastnosti** (z axiomů): konjug. linearita v 1. arg. $\langle \alpha x\mid z\rangle = \overline{\alpha}\langle x\mid z\rangle$, $\langle x+y\mid z\rangle = \langle x\mid z\rangle + \langle y\mid z\rangle$; $\langle x\mid\theta\rangle = \langle\theta\mid x\rangle = 0$.

**Příklady:** standardní (eukleidovský) na $T^n$: $x\bullet y = \sum_{j=1}^n \overline{x_j}\,y_j$ (na $\mathbb{R}^n$: $x^T y$); Frobeniův na maticích $\langle A\mid B\rangle = \sum_{i,j}\overline{a_{ij}}\,b_{ij}$; vážený $x^T A y$ ($A$ symetrická poz. definitní); integrální na funkcích $\langle f\mid g\rangle = \int_0^1 f g\,dx$.

## 2. Norma

**Def.** $\|\cdot\| : V \to \mathbb{R}$ je [[Norma|norma]], platí-li pro $x,y \in V$, $\alpha \in T$:

1. $\|x\| \ge 0$;
2. $\|x\| = 0 \iff x = \theta$;
3. $\|\alpha x\| = |\alpha|\cdot\|x\|$ (homogenita v abs. hodnotě);
4. $\|x+y\| \le \|x\| + \|y\|$ (trojúhelníková nerovnost).

$\|x\|$ = velikost vektoru; $d(x,y) = \|x-y\|$ = vzdálenost.

**Norma indukovaná skalárním součinem:** $\|x\| := \sqrt{\langle x\mid x\rangle}$ — vždy je to norma (ax. 1–3 přímo z axiomů SS, ax. 4 ze Schwarze).

**Příklady norem** ($x \in T^n$):

| norma | předpis |
|---|---|
| **1-norma** | $\|x\|_1 = \sum_j \lvert x_j\rvert$ |
| **2-norma** (eukleidovská) | $\|x\|_2 = \big(\sum_j \lvert x_j\rvert^2\big)^{1/2}$ — indukovaná std. součinem |
| **$\infty$-norma** (max) | $\|x\|_\infty = \max_j \lvert x_j\rvert$ |
| **$p$-norma**, $p\in\langle1,\infty)$ | $\|x\|_p = \big(\sum_j \lvert x_j\rvert^p\big)^{1/p}$ |

## 3. Klíčové nerovnosti

**Schwarzova (Cauchyho–Schwarzova):** $\big|\langle x\mid y\rangle\big| \le \|x\|\cdot\|y\|$. Rovnost $\iff (x,y)$ lineárně závislý.
*(idea: $\langle x-\lambda y\mid x-\lambda y\rangle \ge 0$ pro $\lambda = \langle y\mid x\rangle/\|y\|^2$.)*

**Trojúhelníková:** $\|x+y\| \le \|x\| + \|y\|$ (z $\|x+y\|^2 = \|x\|^2 + 2\,\mathrm{Re}\langle x\mid y\rangle + \|y\|^2$ a Schwarze).

---

## Co odpovědět rychle

- **Skalární součin:** linearita ve 2. arg. + hermitovská symetrie $\langle x\mid y\rangle = \overline{\langle y\mid x\rangle}$ + pozitivní definitnost; na $\mathbb{R}$ symetrie bez pruhu.
- **Norma:** nezápornost, $\|x\|=0\iff x=\theta$, $\|\alpha x\| = |\alpha|\|x\|$, trojúhelníková nerovnost.
- **Indukovaná norma:** $\|x\| = \sqrt{\langle x\mid x\rangle}$ — každému SS přísluší norma.
- **Cauchy–Schwarz:** $|\langle x\mid y\rangle| \le \|x\|\|y\|$; rovnost $\iff$ LZ.
- **$p$-normy:** 1-norma (součet), 2-norma (eukleidovská), ∞-norma (max).
