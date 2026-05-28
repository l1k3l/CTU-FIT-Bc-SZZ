---
aliases: [regulární gramatika, regulární gramatiky, regulární gramatice, regulární gramatikou, regulárních gramatik, regulárním gramatikám, regulárními gramatikami, RG, pravolineární gramatika, levolineární gramatika]
tags: [definice, kurz/AAG]
---

# Regulární gramatika

## Definice

**Regulární gramatika** (typ 3 Chomského hierarchie) je [[Gramatika|gramatika]] $G = (N, \Sigma, P, S)$, kde každé pravidlo má **pravolineární** tvar
$$A \to aB \quad \text{nebo} \quad A \to a, \qquad A, B \in N,\ a \in \Sigma,$$
plus výjimečně $S \to \varepsilon$, pokud $S$ se nevyskytuje na pravé straně.

**Levolineární** varianta: $A \to Ba \mid a$ — generuje tutéž třídu jazyků.

**Pozor:** míchat pravolineární a levolineární pravidla v jedné gramatice **nelze** — výsledný jazyk pak nemusí být regulární.

## Vztah ke konečným automatům

**Věta (Chomsky):** Jazyk $L$ je [[Regulární-jazyk|regulární]] $\iff$ existuje regulární gramatika, která ho generuje.

### RG → NKA
- $Q := N \cup \{A\}$, $A \notin N$ (nový koncový stav),
- $\delta(B, a) := \{C : (B \to aC) \in P\} \cup \{A : (B \to a) \in P\}$,
- $q_0 := S$,
- $F := \{A\} \cup (\{S\}\ \text{pokud}\ S \to \varepsilon \in P)$.

### NKA → RG
- $N := Q$, $S := q_0$,
- $P := \{B \to aC : C \in \delta(B, a)\} \cup \{B \to a : \delta(B, a) \cap F \neq \emptyset\}$,
- přidat $S \to \varepsilon$, pokud $q_0 \in F$.

## Související
- [[Konečný-automat]]
- [[Regulární-výraz]]
- [[Regulární-jazyk]]
- [[Gramatika]]
- [[Bezkontextová-gramatika]]
