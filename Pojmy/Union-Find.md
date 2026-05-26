---
aliases: [Union-Find, union-find, Disjoint-Set-Union, DSU]
tags: [datová-struktura, kurz/AG1]
---

# Union-Find

## Definice

Datová struktura reprezentující rozklad množiny $X$ na disjunktní třídy. Operace:

- `Init(X)` — každý prvek ve vlastní množině.
- `Find(u)` — identifikátor (kořen) množiny obsahující $u$.
- `Union(u, v)` — sjednotí množiny obsahující $u$ a $v$.

## Implementace keříky

Každá množina = strom orientovaný do kořene. Při `Union` připojíme **mělčí keřík pod kořen hlubšího** (případně zvedneme hloubku o 1).

**Lemma o hloubce keříků:** Keřík s $h$ hladinami obsahuje alespoň $2^{h-1}$ vrcholů → hloubka $\le \log n$.

## Složitosti (s keříky)

- `Init` $O(n)$.
- `Find` $O(\log n)$.
- `Union` $O(\log n)$.

(Optimalizovaná verze s union-by-rank + path-compression dosahuje téměř $O(1)$ amortizovaně — $O(\alpha(n))$ kde $\alpha$ je inverzní Ackermannova funkce.)

## Použití

- [[Kruskal|Kruskalův algoritmus]] pro [[Minimální-kostra|MST]].
- Detekce cyklů v lese.

## Související

- [[Kruskal]]
- [[Strom]]
