---
aliases: [derivační strom, derivačního stromu, derivačnímu stromu, derivačním stromem, derivační stromy, derivačních stromů, derivačním stromům, derivačními stromy, parse tree, syntaktický strom, abstraktní syntaktický strom]
tags: [definice, kurz/AAG]
---

# Derivační strom

## Definice

**Derivační strom** v [[Gramatika|gramatice]] $G = (N, \Sigma, P, S)$ je strom s vlastnostmi:
1. uzly jsou ohodnoceny terminály, neterminály nebo $\varepsilon$,
2. **kořen** je ohodnocen $S$,
3. uzel s alespoň jedním následovníkem je ohodnocen neterminálem,
4. jsou-li $n_1, \dots, n_k$ následovníci uzlu ohodnoceného $A$ a jsou-li ohodnoceni zleva doprava $A_1, \dots, A_k$, pak $A \to A_1 \dots A_k$ je pravidlo v $P$,
5. listy zleva doprava tvoří **výsledek (yield)** stromu — větnou formu (nebo větu, pokud listy jsou samé terminály).

## Bijekce s derivacemi

Derivačnímu stromu odpovídá:
- právě jedna **levá derivace** (přepisuje vždy nejlevější neterminál),
- právě jedna **pravá derivace** (přepisuje vždy nejpravější neterminál).

**Rozklad věty** = posloupnost čísel pravidel použitých během derivace. **Levý rozklad** = pořadí pravidel levé derivace; **pravý rozklad** = obrácené pořadí pravidel pravé derivace.

## Víceznačnost

[[Bezkontextová-gramatika|BG]] je **víceznačná**, pokud existuje věta $w \in L(G)$ se dvěma různými derivačními stromy. Klasický příklad: dangling else
$$S \to \mathtt{if}\ b\ \mathtt{then}\ S\ \mathtt{else}\ S \mid \mathtt{if}\ b\ \mathtt{then}\ S \mid a.$$

Některé jazyky jsou **inherentně víceznačné** — neexistuje pro ně žádná jednoznačná gramatika. Rozhodování ambiguity dané BG je **nerozhodnutelné**.

## Použití

Syntaktická analýza (parsing) je proces konstrukce derivačního stromu pro vstupní větu, viz [[Zásobníkový-automat]] (top-down → levý rozklad, bottom-up → pravý rozklad) a CYK algoritmus pro Chomského normální formu.

## Související
- [[Bezkontextová-gramatika]]
- [[Gramatika]]
- [[Chomského-NF]]
- [[Zásobníkový-automat]]
