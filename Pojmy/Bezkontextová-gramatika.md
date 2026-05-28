---
aliases: [bezkontextová gramatika, bezkontextové gramatiky, bezkontextové gramatice, bezkontextovou gramatikou, bezkontextových gramatik, bezkontextovým gramatikám, bezkontextovými gramatikami, BG, CFG, context-free grammar, bezkontextový jazyk, bezkontextového jazyka, bezkontextové jazyky, CFL]
tags: [definice, kurz/AAG]
---

# Bezkontextová gramatika

## Definice

**Bezkontextová gramatika (BG, CFG)** je [[Gramatika|gramatika]] $G = (N, \Sigma, P, S)$ (typ 2 Chomského hierarchie), v níž každé pravidlo má tvar
$$A \to \alpha, \qquad A \in N,\ \alpha \in (N \cup \Sigma)^*.$$
Na levé straně je jediný neterminál — odtud „bezkontextová": pravidlo lze použít nezávisle na okolí $A$.

**Bezkontextový jazyk (CFL)** = jazyk generovatelný nějakou BG, ekvivalentně přijímaný nějakým (nedeterministickým) [[Zásobníkový-automat|zásobníkovým automatem]].

## Derivace, derivační strom, víceznačnost

**Levá / pravá derivace:** v každém kroku se přepisuje vždy nejlevější / nejpravější neterminál.

**[[Derivační-strom|Derivační strom]]:** bijekce mezi stromem a levou (i pravou) derivací; výsledek (yield) stromu = větná forma.

**Rozklad:** posloupnost čísel pravidel použitých během derivace. **Levý rozklad** = pořadí pravidel levé derivace; **pravý rozklad** = obrácené pořadí pravidel pravé derivace.

BG je **víceznačná**, pokud existuje věta se dvěma různými derivačními stromy. Ambiguita je obecně **nerozhodnutelná**; některé jazyky jsou **inherentně víceznačné**.

## Úpravy BG

- Test prázdnosti $L(G)$: $L(G) \neq \emptyset \iff S \in N_t$, kde $N_t$ je nejmenší množina neterminálů, ze kterých lze derivovat terminální řetězec.
- Odstranění nedostupných / zbytečných symbolů.
- Odstranění $\varepsilon$-pravidel a jednoduchých pravidel.
- **Vlastní BG**: bez cyklů, bez $\varepsilon$-pravidel, bez zbytečných symbolů. Každý CFL lze generovat vlastní BG.

## Normální formy

- **[[Chomského-NF|Chomského NF]]** (ChNF): pravidla $A \to BC$, $A \to a$, případně $S \to \varepsilon$.

Každý CFL má gramatiku v ChNF.

## Uzavřenost CFL

**Uzavřena na:** $\cup$, $\cdot$, $^*$.
**Není uzavřena na:** $\cap$, $\neg$.

(Naproti tomu **DCFL** — deterministické bezkontextové jazyky — jsou uzavřeny na doplněk, ale ne na $\cup$ ani $\cap$.)

## Související
- [[Gramatika]]
- [[Zásobníkový-automat]]
- [[Derivační-strom]]
- [[Chomského-NF]]
- [[Regulární-gramatika]]
