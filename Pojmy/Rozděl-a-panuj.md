---
aliases: [rozděl a panuj, rozděl-a-panuj, metoda rozděl a panuj, metodou rozděl a panuj, rozděluj a panuj, divide and conquer, divide-and-conquer, divide et impera]
tags: [definice, kurz/AG1, kurz/PA1]
---

# Rozděl a panuj

## Definice
**Rozděl a panuj** (divide and conquer) je návrhová metoda algoritmů založená na [[Rekurze|rekurzi]]:
1. **Rozděl** vstup na jednu či více menších instancí téhož problému,
2. **Vyřeš** je rekurzivně (triviální instanci přímo),
3. **Sluč** dílčí řešení do řešení celého problému.

Na rozdíl od [[Dynamické-programování|dynamického programování]] jsou podproblémy **nezávislé** (neopakují se).

## Rekurence a její řešení
Složitost se popisuje rekurentní rovnicí typu
$$T(n) = a\,T(n/b) + f(n),$$
kde $a$ je počet podproblémů, $n/b$ jejich velikost a $f(n)$ čas na rozdělení a sloučení. Řeší se rozvinutím (substitucí) nebo součtem přes hladiny **stromu rekurzivních volání**.

## Příklady
| Algoritmus | Rekurence | Složitost |
|---|---|---|
| [[MergeSort]] | $2T(n/2)+\Theta(n)$ | $\Theta(n\log n)$ |
| Binární vyhledávání | $T(n/2)+\Theta(1)$ | $\Theta(\log n)$ |
| Násobení (naivní rozklad) | $4T(n/2)+\Theta(n)$ | $\Theta(n^2)$ |
| Karatsuba | $3T(n/2)+\Theta(n)$ | $\Theta(n^{\log_2 3})\approx\Theta(n^{1{,}59})$ |
| QuickSelect (medián pivot) | $T(n/2)+\Theta(n)$ | $\Theta(n)$ |

## Související
- [[Rekurze]]
- [[Dynamické-programování]]
- [[MergeSort]], [[QuickSort]]
