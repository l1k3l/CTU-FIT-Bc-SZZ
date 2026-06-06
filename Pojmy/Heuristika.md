---
aliases: [heuristika, heuristiky, heuristikou, heuristik, heuristická funkce, heuristické funkce, přípustná heuristika, přípustnost, monotónní heuristika, monotónnost, konzistentní heuristika, konzistence, dominance heuristiky, optimální heuristika]
tags: [definice, kurz/ZUM]
---

# Heuristika

## Definice

V [[Stavový-prostor|ohodnoceném stavovém prostoru]] $(S, A, c)$ s množinou cílů $G$ je **heuristika** (heuristická funkce) libovolná funkce
$$h : S \to \mathbb{R}_0^+,$$
kde $h(s)$ je **odhad ceny** nejlevnější cesty z $s$ do nejbližšího cíle a $h(s_g) = 0$ pro každý $s_g \in G$. Slouží jako „orákulum" radící, který uzel je výhodnější expandovat.

**Optimální heuristika** $h^*(s)$ = *skutečná* cena nejlevnější cesty z $s$ do cíle. Dominuje všechny přípustné heuristiky; lepší sestrojit nelze.

## Přípustnost (admissibility)

$h$ je **přípustná**, je-li
$$\forall s \in S : h(s) \le h^*(s),$$
tj. nikdy nepřeceňuje — je „optimistická". Příklad: vzdušná (euklidovská) vzdálenost na mapě je přípustná, protože pozemní vzdálenost je vždy $\ge$ vzdušná.

## Monotónnost / konzistence

$h$ je **monotónní (konzistentní)**, je-li
$$\forall (x, y) \in A : h(x) - c(x, y) \le h(y)$$
(ekvivalentně trojúhelníková nerovnost $h(x) \le c(x, y) + h(y)$). Platí: **konzistence $\Rightarrow$ přípustnost**.

## Dominance

Pro přípustné $h_1, h_2$: $h_1$ **dominuje** $h_2$, je-li $\forall s : h_1(s) \ge h_2(s)$. Dominující (informativnější) heuristika expanduje v [[A-star|A*]] „v průměru" méně uzlů — ale *nemusí* být rychlejší (může mít vyšší cenu výpočtu na uzel). Hledá se kompromis: informativní vs. levná heuristika.

## Související

- [[A-star]], [[Hladové-prohledávání]], [[Dijkstra]]
- [[Stavový-prostor]]
