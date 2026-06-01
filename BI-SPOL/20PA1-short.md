---
tags: [otázka, kurz/PA1, kurz/AG1, otázka/20, todo]
---

# 20 — Složitost, vyhledávání a řazení (zkrácená verze)

## 1. Složitost
**[[Časová-složitost]]:** počet elementárních operací jako funkce velikosti vstupu $n$ (model **RAM**). Nezávisí na jazyce/HW.
- Případy: **nejhorší** (worst, nejčastěji), průměrný, nejlepší.
- [[Asymptotická-notace]]: $T(n)\in O(f)\iff \exists n_0,c>0:\,\forall n\ge n_0:\,T(n)\le c f(n)$. (AG1 navíc $\Omega,\Theta$.)
- Vlastnosti řazení: **stabilita**, **in-place**, datová citlivost.

## 2. Vyhledávání
- **Sekvenční:** projde prvky, $O(n)$, bez předpokladů.
- **Binární (půlením):** předpoklad **seřazené pole**; půlí interval, $T(n)=T(n/2)+O(1)=O(\log n)$. (`mid=lo+(hi-lo)/2`.)

## 3. Řazení
| Algoritmus | best | avg | worst | paměť | stab. | in-place |
|---|---|---|---|---|---|---|
| Bubble | $n$ | $n^2$ | $n^2$ | $1$ | ✓ | ✓ |
| Select | $n^2$ | $n^2$ | $n^2$ | $1$ | ✗ | ✓ |
| Insert | $n$ | $n^2$ | $n^2$ | $1$ | ✓ | ✓ |
| [[MergeSort]] | $n\log n$ | $n\log n$ | $n\log n$ | $n$ | ✓ | ✗ |
| [[QuickSort]] | $n\log n$ | $n\log n$ | $n^2$ | $\log n$ | ✗ | ✓ |

- **Bubble:** prohazuj sousedy; po $k$ kolech posledních $k$ na místě.
- **Select:** najdi minimum zbytku, prohoď dopředu; šetří záměny.
- **Insert:** zatřiď další prvek do seřazeného začátku posunem.
- **[[MergeSort]]:** rozděl na půlky, rekurzivně seřaď, **slij** (`Merge` $\Theta(n+m)$, každý prvek 1×). $T(n)=2T(n/2)+cn=\Theta(n\log n)$. Stabilní, out-of-place.
- **[[QuickSort]]:** pivot $p$ → $L(<p),S(=p),P(>p)$, rekurze na $L,P$. Avg $O(n\log n)$, worst $\Theta(n^2)$. **Randomizace** pivota: stř. hodnota $O(n\log n)$ (porovnání $y_i,y_j$ s pravd. $2/(j-i+1)$, harmonická řada).
- HeapSort: $O(n\log n)$ in-place (přes [[Binární-halda|haldu]]).

## 4. Dolní mez řazení (porovnávací model)
Prvky se jen **porovnávají**. **Věta:** každý deterministický porovnávací algoritmus potřebuje **$\Omega(n\log n)$** porovnání v nejhorším případě.
*Idea:* rozhodovací (binární) strom musí mít $\ge n!$ listů (různé permutace → různé listy) → hloubka $\ge\log(n!)=\Omega(n\log n)$ (Stirling). ⇒ Merge/Heap/Quick jsou optimální.
(Analogicky vyhledávání v seřazeném poli: $\Omega(\log n)$.)

## 5. Řazení v lineárním čase
Nepracují v porovnávacím modelu (využívají omezený rozsah klíčů) → neporušují dolní mez.
- **CountingSort** (čísla z $\{1..r\}$): histogram + prefixový součet + rozmístění. **$\Theta(n+r)$**, stabilní, ne in-place. Pro $r=O(n)$ lineární.
- **LexCountingSort / RadixSort** (k-tice / víceciferná čísla): opakovaně stabilní CountingSort **od poslední souřadnice**. $\Theta(k(n+r))$.

---

## Co odpovědět rychle
- **Složitost:** počet operací vs. $n$, RAM, nejhorší/průměrný/nejlepší, $O/\Omega/\Theta$.
- **Vyhledávání:** sekvenční $O(n)$; binární $O(\log n)$ (seřazené pole).
- **Elementární řazení** $O(n^2)$; **MergeSort/QuickSort/HeapSort** $O(n\log n)$ (QuickSort worst $n^2$).
- **Dolní mez $\Omega(n\log n)$** — rozhodovací strom, $n!$ listů, Stirling.
- **Lineární řazení:** CountingSort $\Theta(n+r)$, RadixSort $\Theta(k(n+r))$ — jen pro omezený rozsah klíčů.
