---
aliases: [mergesort, merge sort, řazení sléváním, řazení slučováním, slévání, slučování, merge, slévání seřazených posloupností]
tags: [definice, algoritmus, kurz/AG1]
---

# MergeSort

## Definice
**MergeSort** (řazení sléváním) je řadicí algoritmus typu [[Rozděl-a-panuj|rozděl a panuj]]: posloupnost o 1 prvku je seřazená; jinak ji rozdělíme na poloviny ($\lfloor n/2\rfloor$ a $\lceil n/2\rceil$), obě rekurzivně seřadíme a **slijeme** procedurou `Merge`.

`Merge` slévá dvě seřazené posloupnosti v čase $\Theta(n+m)$ tak, že opakovaně přesouvá menší z čel obou posloupností — každý prvek přesune právě jednou (vyžaduje pomocnou paměť $\Theta(n+m)$).

## Vlastnosti
| Vlastnost | Hodnota |
|---|---|
| Časová složitost | $\Theta(n\log n)$ ve všech případech |
| Paměťová složitost | $\Theta(n)$ (out-of-place) |
| Stabilní | ano |
| Datová citlivost | ne (necitlivý) |

**Rekurence:** $T(n)=2T(n/2)+cn$. Rozvinutím $T(n)=2^k T(n/2^k)+kcn$; pro $n/2^k=1$ je $k=\log n$, tedy $T(n)=\Theta(n)+cn\log n=\Theta(n\log n)$.

## Související
- [[Rozděl-a-panuj]]
- [[QuickSort]]
- [[Časová-složitost]]
