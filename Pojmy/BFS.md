---
aliases: [BFS, prohledávání do šířky, procházení do šířky, breadth-first search]
tags: [algoritmus, kurz/AG1, kurz/ZUM]
---

# BFS — prohledávání do šířky

## Specifikace

**Vstup:** [[Graf|graf]] $G = (V, E)$ a vrchol $s \in V$.

**Výstup:**
- Pole [[Vzdálenost|vzdáleností]] $D[v] = d(s, v)$ (resp. `undef`, pokud $v$ není dosažitelný).
- Pole předchůdců $P[v]$ na nějaké nejkratší $s$-$v$-[[Cesta|cestě]].

## Idea

Z $s$ šíříme „vlnu" pomocí **fronty (FIFO)**. Vrchol vyjmutý z fronty otevírá své nenalezené sousedy a nastavuje jim $D[w] = D[v] + 1$, $P[w] = v$.

**Hladina $H_i$** = množina vrcholů s $D = i$ (= vrcholy ve vzdálenosti $i$ od $s$).

## Vlastnosti (3 hlavní)

1. Po skončení jsou uzavřené přesně vrcholy dosažitelné ze $s$.
2. Pro každý uzavřený vrchol $D[v] = d(s, v)$.
3. $P[v]$ je předchůdce $v$ na nějaké nejkratší $s$-$v$-cestě.

## Složitost

**$O(|V| + |E|)$** při reprezentaci [[Seznam-sousedů|seznamem sousedů]].

## Aplikace

- [[Souvislá-komponenta|Souvislé komponenty]] (algoritmus BFS_graf).
- Libovolná [[Kostra|kostra]] (BFS strom).
- [[Vzdálenost|Vzdálenosti]] v neohodnoceném grafu.

## Použití v ZUM

Ve [[Stavový-prostor|stavovém prostoru]] je BFS **neinformovaná strategie**: list k expanzi se vybírá frontou (FIFO), strom se buduje „po patrech".
- **úplná**; najde cestu s **nejmenším počtem hran** (optimální při jednotkových cenách akcí),
- čas i paměť rostou **exponenciálně** s hloubkou řešení ($O(b^d)$) → pro praktické úlohy AI nepoužitelná.

Pseudokód je shodný s grafovým BFS, jen `open` je fronta a pracuje se s (často implicitně daným, i nekonečným) stavovým prostorem. Ohodnocené hrany řeší [[Dijkstra]].

## Související

- [[Vzdálenost]], [[Cesta]]
- [[Dijkstra]] (zobecnění na ohodnocený graf)
- [[Souvislá-komponenta]]
- [[Seznam-sousedů]]
