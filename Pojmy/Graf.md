---
aliases: [graf, grafu, grafem, grafy, grafů, grafům, grafech]
tags: [definice, kurz/AG1]
---

# Graf

## Definice

**Neorientovaný graf** je uspořádaná dvojice $G = (V, E)$, kde
- $V$ je neprázdná konečná množina **vrcholů**,
- $E \subseteq \binom{V}{2}$ je množina **hran** (dvouprvkových podmnožin $V$).

Značení: $V(G)$, $E(G)$, $n = |V|$, $m = |E|$. Hrana $e = \{u, v\}$ má **koncové vrcholy** $u, v$; $u, v$ jsou **sousedé** a jsou **incidentní** s $e$.

## Důležité třídy grafů

- **Úplný graf $K_n$** (klika na $n$ vrcholech): $E = \binom{V}{2}$.
- **Úplný bipartitní graf $K_{n_1, n_2}$**: vrcholy ve dvou partitách, hrany mezi všemi dvojicemi z $A \times B$.
- **Cesta $P_n$**, **kružnice $C_n$**.
- **Doplněk $\overline{G} = (V, \binom{V}{2} \setminus E)$**.

## Související

- [[Orientovaný-graf]]
- [[Sled]], [[Cesta]], [[Vzdálenost]]
- [[Stupeň-vrcholu]], [[Princip-sudosti]]
- [[Podgraf]], [[Klika]]
- [[Strom]], [[Souvislost]]
- [[Matice-sousednosti]], [[Seznam-sousedů]]
