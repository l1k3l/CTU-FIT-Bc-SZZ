---
aliases: [kostra, kostry, kostře, kostru, kostrou, koster, kostrám, kostrách]
tags: [definice, kurz/AG1]
---

# Kostra

## Definice

Nechť $G = (V, E)$ je [[Souvislost|souvislý]] [[Graf|graf]]. **Kostra** $G$ je podgraf $K$, pro který $V(K) = V$ a $K$ je [[Strom|strom]].

- Kostra má $|V| - 1$ hran (z charakterizace stromů).
- Nesouvislé grafy nemají kostru; každá souvislá komponenta má svou kostru.

## Konstrukce libovolné kostry

Hrany do předchůdců ($P$-pole z [[BFS|BFS]]) tvoří kostru. Spustíme BFS, vrátíme $\{\{P[v], v\} : v \neq s\}$. Čas $O(|V| + |E|)$.

## Související

- [[Minimální-kostra]]
- [[Strom]]
- [[BFS]]
