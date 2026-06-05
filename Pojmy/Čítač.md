---
aliases: [čítač, čítače, čítači, čítačem, čítačů, counter, vratný čítač, modulo čítač]
tags: [definice, kurz/SAP]
---

# Čítač

## Definice
**Čítač** je [[Sekvenční-obvod|sekvenční obvod]] (speciální typ registru), který v sobě zahrnuje funkci **inkrementu** (popř. dekrementu) — postupně prochází posloupností stavů. Je sestaven z [[Klopný-obvod|klopných obvodů]] a jeho chování je popsáno [[Konečný-automat|konečným automatem]] (Mealy/Moore).

## Dělení
- **Úplný čítač:** modulo $2^n$ (čítá do 4, 8, 16, …); **neúplný:** modulo jiné než mocnina 2 (do 10, 60, …).
- **Synchronní** (všechny KO řízeny společným CLK) vs **asynchronní** (přenos se šíří mezi KO).
- **Vratný (up/down)** — čítá nahoru i dolů podle řídicího vstupu.
- Kód stavů: binární, **Grayův** (mění se jen 1 bit), 1-z-N. U čítačů se stavový kód obvykle volí **rovný požadovanému výstupu** → odpadá výstupní logika.

Příklad (M4, řídicí vstup $E$ = enable, D klopné obvody): $D_{q_0}=q_0\oplus E$, $D_{q_1}=Eq_0\oplus q_1$, výstup $Y=q_1q_0$.

## Související
- [[Sekvenční-obvod]]
- [[Klopný-obvod]]
- [[Konečný-automat]]
