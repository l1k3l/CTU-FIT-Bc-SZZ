---
aliases: [Bellman-Ford, Bellmanův-Fordův algoritmus, Bellmanův-Fordův, Bellman-Fordův algoritmus, SimpleBellman-Ford]
tags: [algoritmus, kurz/AG1]
---

# Bellman-Ford

## Specifikace

**Vstup:** [[Orientovaný-graf|orientovaný graf]] s **libovolnými** délkami hran $\ell: E \to \mathbb{R}$, **bez záporných cyklů**.

**Výstup:** [[Vzdálenost|vzdálenosti]] $d(v_0, v)$ a předchůdci pro všechny $v$.

## Idea

Stejný relaxační rámec jako [[Dijkstra|Dijkstra]], ale otevřené vrcholy ukládáme do **obyčejné fronty (FIFO)**. Bereme vždy nejstarší.

## Fáze a klíčová vlastnost

**Fáze $F_i$:** $A_0 = \{v_0\}$; $A_i$ = vrcholy otevřené při relaxaci vrcholů z $A_{i-1}$.

**Vlastnost H:** Na konci fáze $F_i$ je $h(v) \le \ell(S)$, kde $S$ je nejkratší $v_0$-$v$-sled o **nejvýše $i$ hranách**.

**Důsledek:** Nejkratší cesta má $\le n - 1$ hran → po $n$ fázích už k žádné změně nedojde a algoritmus skončí.

## Složitost

$O(|V| \cdot |E|)$. Jedna fáze relaxuje každý vrchol nejvýše jednou ($O(|E|)$), fází je $|V|$.

## SimpleBellman-Ford

Ještě jednodušší varianta: $n$-krát projdi všechny hrany a relaxuj. Také $O(|V| \cdot |E|)$.

## Související

- [[Vzdálenost]]
- [[Dijkstra]]
- [[BFS]]
