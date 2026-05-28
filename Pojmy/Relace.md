---
aliases: [relace, relaci, relací, relacích, relacím, relacemi]
tags: [definice, kurz/DBS]
---

# Relace

## Definice

Mějme:
- jména **atributů** $[A_1, A_2, \dots, A_n]$,
- **domény** atributů $D_i = \text{dom}(A_i)$ (1NF požaduje, aby atributy byly **atomické**),
- **n-tici** $(a_1, a_2, \dots, a_n)$, kde $a_i \in D_i$.

**Relace** $R$ je podmnožina kartézského součinu $D_1 \times D_2 \times \dots \times D_n$.

**Schéma relace:** $R(A_1 : D_1, A_2 : D_2, \dots, A_n : D_n)$, zkráceně $R(A)$.

## Relace vs. tabulka

| Relace | Tabulka |
|---|---|
| schéma relace | záhlaví tabulky |
| jméno atributu | jméno sloupce |
| atribut | sloupec |
| n-tice | řádek |

**Odlišnosti:**
- V relaci **nezáleží na pořadí** n-tic.
- Relace **neobsahují duplicitní** n-tice (jsou to množiny).

## Schéma relační databáze

$(R, I)$, kde $R = \{R_1, \dots, R_n\}$ je množina relací a $I$ je množina **integritních omezení**.

**Přípustná relační databáze** se schématem $(R, I)$ je množina konkrétních relací $\{R_1^*, \dots, R_n^*\}$ takových, že jejich n-tice vyhovují tvrzením v $I$.

## Související

- [[Klíč-schématu]]
- [[Cizí-klíč]]
- [[Integritní-omezení]]
- [[Relační-algebra]]
