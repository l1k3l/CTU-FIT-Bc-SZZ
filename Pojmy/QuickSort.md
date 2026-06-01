---
aliases: [quicksort, quick sort, rychlé řazení, řazení pomocí pivota, partition, pivot]
tags: [definice, algoritmus, kurz/AG1]
---

# QuickSort

## Definice
**QuickSort** je řadicí algoritmus typu [[Rozděl-a-panuj|rozděl a panuj]]. Vybere se **pivot** $p$ a vstup se rozdělí na tři části: $L$ (prvky $< p$), $S$ (prvky $= p$), $P$ (prvky $> p$). Rekurzivně se seřadí $L$ a $P$ (část $S$ je již seřazená) a výsledek je zřetězení $L, S, P$.

## Vlastnosti
| Případ | Časová složitost |
|---|---|
| Nejlepší / průměrný (medián-like pivot) | $\Theta(n\log n)$ |
| Nejhorší (extrémní pivot) | $\Theta(n^2)$ |

- **Věta:** Střední hodnota časové složitosti QuickSortu s **rovnoměrně náhodnou volbou pivota** je $O(n\log n)$. (Klíč: dvojice $y_i, y_j$ se porovná s pravděpodobností $2/(j-i+1)$; $\mathbf{E}[\text{počet porovnání}] = O(n\log n)$ přes harmonickou řadu.)
- Stabilita: standardně **nestabilní**. V praxi obvykle **in-place**.
- Randomizace volby pivota chrání před zlomyslným vstupem vynucujícím $\Theta(n^2)$.

Stejná myšlenka rozkladu $L/S/P$ řeší i hledání $k$-tého nejmenšího prvku (**QuickSelect**, ve střední hodnotě $O(n)$).

## Související
- [[MergeSort]]
- [[Rozděl-a-panuj]]
- [[Časová-složitost]]
