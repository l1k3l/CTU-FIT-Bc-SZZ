---
aliases: [spojitost, spojitá, spojitá funkce, spojité funkce, spojitý, spojitě, spojitost v bodě, nespojitost, nespojitá, continuity, continuous]
tags: [definice, kurz/MA1]
---

# Spojitost

## Definice

Funkce $f$ je **spojitá v bodě** $a \in D_f$, právě když
$$\lim_{x\to a} f(x) = f(a).$$
Tedy: limita v $a$ existuje a rovná se funkční hodnotě. (Nutně $a \in D_f$ — jinak $f(a)$ neexistuje a o spojitosti nemluvíme.)

**ε-δ tvar:** $\forall \varepsilon > 0\ \exists \delta > 0\ \forall x: |x-a| < \delta \Rightarrow |f(x)-f(a)| < \varepsilon$. Intuitivně: „$f(x)$ je blízko $f(a)$, je-li $x$ blízko $a$".

- **Spojitost zprava/zleva:** $\lim_{x\to a^\pm} f(x) = f(a)$. Funkce na okolí $a$ je spojitá v $a$ ⟺ je spojitá zprava i zleva.
- **Spojitá na intervalu** $J$: $f|_J$ je spojitá v každém bodě $J$. Množinu spojitých funkcí na $J$ značíme $C(J)$.

## Pravidla

- Součet, součin a (při $g(a)\neq 0$) podíl funkcí spojitých v $a$ je spojitý v $a$.
- Složení spojitých funkcí je spojité.
- Polynomy, $\sin,\cos,\exp,\ln$, odmocniny, $|x|$ jsou spojité na svých definičních oborech; spojitost se přenáší na inverzní funkci (pro ryze monotónní spojitou funkci).

## Vlastnosti spojitých funkcí

- **Metoda půlení intervalu (Bolzano):** je-li $f$ spojitá na $\langle a,b\rangle$ a $f(a)f(b) < 0$, existuje $c\in(a,b)$ s $f(c)=0$.
- Spojitý obraz intervalu je interval; spojitý obraz **uzavřeného** intervalu je uzavřený interval ⇒ spojitá funkce na $\langle a,b\rangle$ nabývá globálního maxima i minima.

## Typy nespojitostí

- **Odstranitelná** ($\lim_{x\to a} f$ existuje konečná, ale $\neq f(a)$ / $f(a)$ není def.) — lze dodefinovat.
- **Konečný skok** ($\lim_{x\to a^+} \neq \lim_{x\to a^-}$, obě konečné).
- **Nekonečná limita** nebo **neexistence limity** (např. $\sin\tfrac1x$ v $0$).

## Související

- [[Limita-funkce]]
- [[Derivace]]
