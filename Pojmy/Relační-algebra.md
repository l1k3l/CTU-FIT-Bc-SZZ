---
aliases: [relační algebra, relační algebry, relační algebře, relační algebrou, RA]
tags: [definice, kurz/DBS]
---

# Relační algebra

## Definice

**Relační algebra (RA)** je formální **dotazovací jazyk** nad relačním modelem dat. Operandem každé operace je celá relace, výsledkem také relace (lze řetězit). Vyhodnocuje se **zleva doprava**, unární operace mají přednost před binárními, prioritu mění **složené závorky**.

Dotazovací jazyk, který umí vyjádřit každý výraz RA, se nazývá **relačně úplný**. SQL `SELECT` je relačně úplný (a má navíc agregace, ORDER BY, …).

## Operace

### Unární

- **Selekce** $R(\varphi)$ — řádky $u \in R$ splňující $\varphi$.
  $R(\varphi) =_{def} \{u \mid u \in R \land \varphi(u)\}$.
- **Projekce** $R[C]$ — pouze sloupce $C \subseteq A$.
  $R[C] =_{def} \{u[C] \mid u \in R\}$.
- **Přejmenování** $R[A_1 \to B_1]$ — změna jména atributu.

### Spojení

- **Obecné (Θ-)spojení** $R[t_1 \Theta t_2] S$ — kartézský součin + selekce $u.t_1 \Theta u.t_2$.
- **Přirozené spojení** $R \ast S$ — spojení s rovností na všech průnikových atributech, výsledné atributy se nezduplikují.
- **Polospojení** (semi-join) $R \prec\ast S$ — n-tice $R$, které mají partnera v $S$. Definice: $R \prec\ast S =_{def} \{R \ast S\}[A]$.
- **Antijoin** $R \overline{\prec\ast} S$ — n-tice $R$, které partnera **nemají**: $R \setminus \{R \prec\ast S\}$.

### Množinové

- **Sjednocení** $R \cup S$,
- **Průnik** $R \cap S$,
- **Rozdíl** $R \setminus S$,
- **Kartézský součin** $R \times S$.

### Speciální

- **Relační dělení** $R \div S$ pro $R(X, Y), S(Y)$: vrací hodnoty $x \in R$, které v $R$ tvoří dvojici s **každým** $y \in S$.
  Definice přes minimální množinu: $R \div S =_{def} R[X] \setminus \{\{R[X] \times S\} \setminus R\}[X]$.

## Minimální množina operací

$\{\times, \text{selekce}, \text{projekce}, \to, \cup, \setminus\}$ — ostatní operace lze vyjádřit pomocí těchto.

## Související

- [[Relace]]
