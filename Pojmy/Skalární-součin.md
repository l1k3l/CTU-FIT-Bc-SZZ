---
aliases: [skalární součin, skalárního součinu, skalárním součinem, skalární součiny, skalárních součinů, vnitřní součin, eukleidovský součin, unitární prostor, prostor se skalárním součinem]
tags: [definice, kurz/LA2]
---

# Skalární součin

## Definice

Buď $V$ vektorový prostor nad tělesem $T = \mathbb{R}$ nebo $T = \mathbb{C}$ (skalární součin lze rozumně zavést jen nad těmito tělesy). **Skalární součin** je zobrazení $\langle\,\cdot\mid\cdot\,\rangle : V \times V \to T$, které pro všechny $x, y, z \in V$ a $\alpha \in T$ splňuje axiomy:

1. **Linearita v druhém argumentu:** $\langle x \mid y + z\rangle = \langle x\mid y\rangle + \langle x\mid z\rangle$ a $\langle x \mid \alpha y\rangle = \alpha\langle x\mid y\rangle$.
2. **Hermitovská (konjugovaná) symetrie:** $\langle x\mid y\rangle = \overline{\langle y\mid x\rangle}$.
3. **Pozitivní definitnost:** $\langle x\mid x\rangle \ge 0$ a $\big(\langle x\mid x\rangle = 0 \iff x = \theta\big)$.

Dvojici $(V, \langle\,\cdot\mid\cdot\,\rangle)$ nazýváme **prostorem se skalárním součinem**, zkráceně **prehilbertův prostor** (značíme $\mathcal{H}$). Konečněrozměrný prostor se skalárním součinem nad $\mathbb{C}$ se nazývá **unitární prostor**.

## Reálný vs. komplexní případ

- **$T = \mathbb{C}$:** sdružení v 2. axiomu je nutné — zaručuje $\langle x\mid x\rangle \in \mathbb{R}$, aby měla smysl nerovnost ve 3. axiomu.
- **$T = \mathbb{R}$:** $\overline{a} = a$, takže 2. axiom se redukuje na běžnou symetrii $\langle x\mid y\rangle = \langle y\mid x\rangle$ a součin je lineární v obou argumentech.

Důsledek axiomů: **konjugovaná linearita v prvním argumentu** $\langle \alpha x\mid z\rangle = \overline{\alpha}\langle x\mid z\rangle$, $\langle x+y\mid z\rangle = \langle x\mid z\rangle + \langle y\mid z\rangle$; dále $\langle x\mid\theta\rangle = \langle\theta\mid x\rangle = 0$.

> Pozn.: volba linearity je konvence — některé materiály žádají linearitu v prvním argumentu.

## Norma indukovaná skalárním součinem

Každý skalární součin indukuje [[Norma|normu]] $\|x\| := \sqrt{\langle x\mid x\rangle}$ (korektní díky 3. axiomu).

## Cauchyho–Schwarzova nerovnost

Pro všechna $x, y \in \mathcal{H}$ platí
$$\big|\langle x\mid y\rangle\big| \le \|x\|\cdot\|y\|,$$
s rovností právě tehdy, když je soubor $(x, y)$ lineárně závislý. (V textbooku BI-LA2 značeno jako Schwarzova nerovnost.)

## Příklady

- **Standardní (eukleidovský) součin** na $T^n$: $x \bullet y = \sum_{j=1}^n \overline{x_j}\,y_j$ (na $\mathbb{R}^n$ je $x\bullet y = x^T y$).
- **Frobeniův součin** na prostoru [[Matice|matic]] $T^{m,n}$: $\langle A\mid B\rangle = \sum_{i,j} \overline{a_{ij}}\,b_{ij}$.
- **Vážený součin** na $\mathbb{R}^n$: $\langle x\mid y\rangle = x^T A y$ pro symetrickou pozitivně definitní $A$.
- **Integrální součin** na spojitých funkcích $\mathcal{C}(\langle 0,1\rangle)$: $\langle f\mid g\rangle = \int_0^1 f(x)g(x)\,dx$.

## Související

- [[Norma]]
- [[Ortogonální-báze]]
- [[Matice]]
