---
aliases: [Chomského normální forma, Chomského NF, ChNF, Chomsky normal form, CNF]
tags: [definice, kurz/AAG]
---

# Chomského normální forma

## Definice

[[Bezkontextová-gramatika|BG]] $G = (N, \Sigma, P, S)$ je v **Chomského normální formě (ChNF)**, jestliže každé pravidlo v $P$ má jeden z tvarů:
1. $A \to BC$, kde $A, B, C \in N$,
2. $A \to a$, kde $A \in N, a \in \Sigma$,
3. $S \to \varepsilon$, výjimečně, pokud $\varepsilon \in L(G)$, a $S$ se nevyskytuje na pravé straně žádného pravidla.

## Věta o existenci

**Věta:** Pro každý bezkontextový jazyk $L$ existuje gramatika v ChNF, která ho generuje.

## Algoritmus převodu

**Vstup:** vlastní BG bez jednoduchých pravidel.

1. Pravidla $A \to BC$ a $A \to a$ ponech; $S \to \varepsilon$ ponech (pokud existuje).
2. Pro dlouhá pravidla $A \to X_1 X_2 \dots X_k$ ($k > 2$) zaveď pomocné neterminály $Y_{X_2 \dots X_k}, Y_{X_3 \dots X_k}, \dots$ a nahraď pravidlo posloupností $A \to X'_1 Y_{X_2 \dots X_k}, Y_{X_2 \dots X_k} \to X'_2 Y_{X_3 \dots X_k}, \dots$
3. Každý terminál $a$ ve smíšeném pravidle nahraď novým neterminálem $a'$ s pravidlem $a' \to a$.

## CYK algoritmus

Hlavní praktický důsledek ChNF: existence efektivního algoritmu rozhodování členství v $L(G)$.

**Věta:** Pro každou BG v ChNF lze v čase $O(n^3 |G|)$ rozhodnout, zda dané slovo délky $n$ patří do $L(G)$.

**Algoritmus CYK** (Cocke-Younger-Kasami):
- Tabulka $T[j, i]$ obsahuje neterminály, ze kterých lze derivovat podřetězec $x_j \dots x_{j+i-1}$ délky $i$ od pozice $j$.
- $T[j, 1] := \{A : A \to x_j \in P\}$.
- $T[j, i] := \{A : A \to BC \in P,\ B \in T[j, k],\ C \in T[j+k, i-k],\ 1 \le k < i\}$.
- $x \in L(G) \iff S \in T[1, n]$.

## Související
- [[Bezkontextová-gramatika]]
- [[Derivační-strom]]
