---
aliases: [matice sousednosti, matice sousedností, matici sousednosti, maticí sousednosti]
tags: [datová-struktura, kurz/AG1]
---

# Matice sousednosti

## Definice

Reprezentace [[Graf|grafu]]. Čtvercová matice $A_G$ rozměru $n \times n$:

$$a_{ij} = \begin{cases} 1 & \text{pokud } \{v_i, v_j\} \in E \\ 0 & \text{jinak} \end{cases}$$

Pro neorientovaný graf je $A_G$ symetrická.

## Paměť

$O(n^2)$.

## Trade-off vs. seznam sousedů

- Test sousednosti dvou konkrétních vrcholů: $O(1)$ (lepší než seznam).
- Iterace přes všechny sousedy $v$: $O(n)$ (horší než seznam pro řídký graf).

## Související

- [[Seznam-sousedů]]
- [[Graf]]
