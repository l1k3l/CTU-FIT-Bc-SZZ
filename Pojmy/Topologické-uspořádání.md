---
aliases: [topologické uspořádání, topologického uspořádání, topologickému uspořádání, topologickým uspořádáním, TU]
tags: [definice, kurz/AG1]
---

# Topologické uspořádání

## Definice

**Topologické uspořádání** [[Orientovaný-graf|orientovaného grafu]] $G = (V, E)$ je takové seřazení vrcholů $v_1, \ldots, v_n$, že pro každou orientovanou hranu $(v_i, v_j) \in E$ platí $i < j$.

## Existence

**Topologické uspořádání existuje $\iff$ graf je [[DAG|DAG]].**

Pokud graf obsahuje orientovanou kružnici, nelze topologicky uspořádat.

## Výpočet

Algoritmus [[TopSort|TopSort]] (Kahn) najde TU v čase $O(|V| + |E|)$.

## Související

- [[DAG]]
- [[TopSort]]
- [[Orientovaný-graf]]
