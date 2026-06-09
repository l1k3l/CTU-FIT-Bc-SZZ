---
tags: [otázka, kurz/ZUM, otázka/22, todo]
---

# 22 — Heuristické prohledávání a A* (zkrácená verze)

## Ohodnocený prostor
[[Stavový-prostor|Ohodnocený stavový prostor]] $(S,A,c)$, cena akce $c:A\to\mathbb{R}_0^+$, **cena cesty** $C(p)=\sum_i c(a_i)$.
[[Dijkstra]]: $f=g$ (dosud ujetá cena), relaxace, optimální, $O(|A|+|S|\log|S|)$, ale **všesměrový**.

## Heuristika
[[Heuristika]] $h:S\to\mathbb{R}_0^+$ = odhad ceny cesty do nejbližšího cíle, $h(\text{cíl})=0$. Optimální $h^*$ = skutečná cena. *Příklad:* vzdušná vzdálenost na mapě.

## Best-first algoritmy

| Alg. | $f(s)$ | optimální? |
|---|---|---|
| Dijkstra | $g$ | ano |
| [[Hladové-prohledávání\|greedy]] | $h$ | **ne** ("tah na bránu") |
| **[[A-star\|A*]]** | $g+h$ | ano (viz níže) |

$A^* $: expanduje $\arg\min_{OPEN}(g+h)$, prioritní fronta dle $f$. ($h\equiv0\Rightarrow$ Dijkstra; bez $g\Rightarrow$ greedy.)

## Vlastnosti heuristik
- **přípustná:** $h(s)\le h^*(s)$ (nepřeceňuje, optimistická),
- **konzistentní (monotónní):** $h(x)-c(x,y)\le h(y)$ (trojúh. nerovnost); **konzistence ⇒ přípustnost**,
- **dominance:** $h_1\ge h_2 \Rightarrow h_1$ dominuje (méně expanzí, ne nutně rychleji).

**Optimalita A\*:** $h$ konzistentní ⇒ optimální i s CLOSED (grafové); $h$ přípustná, nekonzistentní ⇒ optimální jen bez CLOSED; $h$ nepřípustná ⇒ bez záruky.

---

## Co odpovědět rychle
- $h$: odhad zbývající ceny, $h(\text{cíl})=0$; **přípustná** $h\le h^*$, **konzistentní** $h(x)\le c(x,y)+h(y)$.
- **greedy** $f=h$ (neoptimální), **A\*** $f=g+h$ (optimální při konzistentní $h$).
- **dominance** $h_1\ge h_2$ ⇒ méně expanzí.
- **Doptávání:** heuristika, která **přeceňuje** ($h>h^*$), je nepřípustná → A* ztrácí optimalitu (např. euklid. vzdálenost na čtvrtou v bludišti = nepřípustná). Monotónnost ⇒ přípustnost, ne naopak.
