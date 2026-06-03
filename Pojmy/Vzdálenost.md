---
aliases: [vzdálenost, vzdálenosti, vzdáleností, vzdálenostem, vzdálenostech, vzdálenostmi]
tags: [definice, kurz/AG1]
---

# Vzdálenost

## Definice

**Vzdálenost** $d(s, t)$ je délka nejkratší $s$-$t$-[[Cesta|cesty]] (nebo $+\infty$, pokud neexistuje).

V hranově ohodnoceném grafu s délkami $\ell: E \to \mathbb{R}$ je $d(u, v) = \min$ z délek (součtů vah) všech $u$-$v$-cest.

## Vlastnosti (kladné délky)

- **Trojúhelníková nerovnost:** $d(u, v) \le d(u, w) + d(w, v)$.
- **Podčást nejkratší cesty je nejkratší cesta:** je-li $P$ nejkratší $u$-$v$-cesta a $w \in P$, pak $P_{uw}$ je nejkratší $u$-$w$-cesta.

## Záporné délky

Při **záporném cyklu** není nejkratší sled definován. Pro libovolná ohodnocení (včetně záporných) je hledání nejkratší cesty NP-těžké.

## Související

- [[Metrika]] — obecná vzdálenostní funkce na množině (metrický prostor); jiný význam než grafová vzdálenost zde.
- [[Cesta]], [[Sled]]
- [[BFS]] (neohodnocený graf)
- [[Dijkstra]] ($\ell \ge 0$)
- [[Bellman-Ford]] (bez záporných cyklů)
