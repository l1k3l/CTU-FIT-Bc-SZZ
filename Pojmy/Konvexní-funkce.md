---
aliases: [konvexní, konvexní funkce, konvexita, konvexnost, konkávní, konkávní funkce, konkavita, konkávnost, ryze konvexní, ryze konkávní, inflexní bod, inflexní body, convex, concave, inflection point]
tags: [definice, kurz/MA1]
---

# Konvexní funkce

## Definice (pomocí tečny)

Nechť $f$ je [[Derivace|diferencovatelná]] v bodě $a$. $f$ je **ryze konvexní** (resp. **ryze konkávní**) v $a$, právě když existuje okolí $U_a$ tak, že pro $x \in U_a\setminus\{a\}$ leží body $(x, f(x))$ **nad** (resp. **pod**) tečnou:
$$f(x) > f(a) + f'(a)(x-a) \quad (\text{resp. } <).$$
Připustíme-li i rovnost (body na tečně), jde o **konvexní** (resp. konkávní) funkci. Na intervalu $J$: spojitá a (ryze) konvexní/konkávní v každém bodě $J^\circ$. Platí: $f$ konkávní ⟺ $-f$ konvexní.

## Definice (pomocí sečny, bez derivace)

$f$ je konvexní na $J$, právě když pro každé $x_1 < x_2 < x_3$ z $J$ leží bod $(x_2, f(x_2))$ pod (nebo na) přímkou spojující $(x_1, f(x_1))$ a $(x_3, f(x_3))$. (Pokrývá i nediferencovatelné funkce jako $|x|$.)

## Kritérium (druhá derivace)

Má-li $f$ druhou derivaci na $J^\circ$:
$$f''(x) \ge 0 \text{ na } J^\circ \iff f \text{ konvexní na } J; \qquad f''(x) > 0 \text{ na } J^\circ \Rightarrow f \text{ ryze konvexní}.$$
Pro konkávnost se nerovnosti otočí. Druhou implikaci **nelze obrátit** ($x^4$ je ryze konvexní, ale $f''(0)=0$).

## Inflexní bod

Bod $c$, v němž je $f$ spojitá a mění se v něm konvexita na konkavitu (nebo naopak) — tj. $f$ je ryze konvexní na $(c-\delta, c)$ a ryze konkávní na $(c, c+\delta)$, nebo naopak. Typicky kandidáti: body s $f''(c)=0$.

## Související

- [[Derivace]]
- [[Lokální-extrém]]
- [[Asymptota]]
