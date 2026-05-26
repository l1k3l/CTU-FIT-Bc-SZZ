---
aliases: [binomiální halda, binomiální haldy, binomiální haldě, binomiální haldu, binomiálních hald, binomiálním haldám, BH]
tags: [definice, datová-struktura, kurz/AG1]
---

# Binomiální halda

## Definice
**Binomiální halda (BH)** obsahující $n$ prvků je uspořádaná množina **[[Binomiální-strom|binomiálních stromů]]** $\mathcal{T} = T_1, \dots, T_\ell$, kde:
1. Stromy $T_i$ jsou uspořádány **vzestupně podle svého řádu**.
2. $n = |V(T_1)| + \dots + |V(T_\ell)|$.
3. Pro každý řád $k \ge 0$ se v $\mathcal{T}$ vyskytuje **nejvýše jeden** strom řádu $k$.
4. Každý vrchol $v$ obsahuje klíč $k(v)$.
5. V každém stromu $T_i$ platí **haldové uspořádání**: pro každý vrchol $v$ a jeho syny $s_j$ platí $k(v) \le k(s_j)$.

## Vlastnosti
**Tvrzení:** Strom $B_i$ se vyskytuje v $n$-prvkové BH právě tehdy, když ve dvojkovém zápisu $b_k b_{k-1} \dots b_0$ čísla $n$ je $b_i = 1$.

**Důsledek:** $n$-prvková BH obsahuje $O(\log n)$ binomiálních stromů.

## Operace a jejich složitost

| Operace | Složitost | Popis |
|---|---|---|
| `BHFindMin` | $O(1)$ | minimum (udržuje se ukazatel) |
| `BHMerge(A, B)` | $O(\log n)$ | sloučení dvou BH |
| `BHInsert(H, x)` | $O(\log n)$, amort. $\Theta^*(1)$ | vložení |
| `BHExtractMin` | $O(\log n)$ | odstranění minima |
| `BHBuild` | $O(n)$ | postavení z $n$ prvků |
| `BHDecreaseKey` / `BHDelete` / `BHIncreaseKey` | $O(\log n)$ | s ukazatelem na prvek |

**Klíčová idea:** Operace `BHMerge` zrcadlí **sčítání ve dvojkové soustavě** — slévání dvou stromů téhož řádu odpovídá přenosu (carry). `BHInsert` = `BHMerge` s jednoprvkovou BH = bitová inverze v [[Binární-sčítačka|binární sčítačce]] → amortizovaně $\Theta^*(1)$.

## Použití
- Patří do rodiny **mergeable heaps** — datových struktur podporujících rychlé sloučení dvou hald.

## Související
- [[Binomiální-strom]]
- [[Binární-halda]]
- [[Amortizovaná-složitost]]
