---
aliases: [rekurze, rekurzi, rekurzí, rekurze, rekurzí, rekurzivní, rekurzivního, rekurzivního volání, rekurzivní volání, recursion]
tags: [definice, kurz/PA1, kurz/AG1]
---

# Rekurze

## Definice
**Rekurze** je způsob řešení problému, při kterém funkce (algoritmus) k vyřešení volá **sebe sama** na menší instanci téhož problému. Použitelná, právě když:
1. rekurzivní volání řeší **menší / jednodušší instanci**,
2. existuje **základní (triviální) případ**, kde rekurze končí bez dalšího volání.

## Zásobník volání
Každé zanoření vytvoří na **systémovém zásobníku** nový aktivační záznam s lokálními proměnnými volání. Hloubka rekurze tedy přímo určuje spotřebu paměti na zásobníku; příliš hluboká rekurze způsobí přetečení zásobníku.

## Rekurze vs. iterace
- Rekurzivní řešení pracuje **shora dolů**, je krátké a srozumitelné, ale má sklon k neefektivitě (např. opakovaný výpočet stejných podproblémů — naivní rekurzivní Fibonacci je $\Theta(\varphi^n)$).
- Iterativní řešení pracuje **zdola nahoru**; každou rekurzi lze převést na iteraci (a naopak).
- Opakované podproblémy řeší [[Dynamické-programování]] (memoizace / iterativní tabulka).

## Použití
- **Metoda [[Rozděl-a-panuj]]** (MergeSort, Karatsuba, QuickSelect).
- Klasické příklady: faktoriál, Euklidův algoritmus, Hanojské věže.

## Související
- [[Rozděl-a-panuj]]
- [[Dynamické-programování]]
- [[Časová-složitost]]
