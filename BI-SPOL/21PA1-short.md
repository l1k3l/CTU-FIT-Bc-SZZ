---
tags: [otázka, kurz/PA1, kurz/AG1, otázka/21, todo]
---

# 21 — Rozděl a panuj, rekurze vs. iterace, DP (zkrácená verze)

## 1. Rozděl a panuj
**[[Rekurze]]:** funkce volá sebe sama na menší instanci + základní případ. Každé zanoření = aktivační záznam na zásobníku (hloubka = paměť).

**[[Rozděl-a-panuj]]:** rozděl vstup → rekurzivně vyřeš (podproblémy **nezávislé**) → slij. Rekurence $T(n)=a\,T(n/b)+f(n)$, řeší se rozvinutím / součtem přes hladiny SRV.

| Algoritmus | rekurence | složitost |
|---|---|---|
| [[MergeSort]] | $2T(n/2)+\Theta(n)$ | $\Theta(n\log n)$ |
| Bin. vyhledávání | $T(n/2)+\Theta(1)$ | $\Theta(\log n)$ |
| Násobení naivně | $4T(n/2)+\Theta(n)$ | $\Theta(n^2)$ |
| Karatsuba | $3T(n/2)+\Theta(n)$ | $\Theta(n^{\log_2 3})\approx n^{1{,}59}$ |
| QuickSelect (medián) | $T(n/2)+\Theta(n)$ | $\Theta(n)$ |

(Master theorem AG1 neuvádí — rekurence ručně.)

## 2. Rekurze vs. iterace
- Rekurze = shora dolů, krátká, ale zásobník + opakované podproblémy.
- Iterace = zdola nahoru, $O(1)$ stav. **Vzájemně převoditelné.**
- **Motivace DP:** naivní `fib` rekurzivně $\Theta(\varphi^n)$ (SRV plný binární strom, $F(n)$ listů) × iterativně $O(n)$.

## 3. Dynamické programování
**[[Dynamické-programování|DP]]:** rekurzivní rozklad, kde se **podproblémy opakují** → spočti jednou, ulož do tabulky. Předpoklady: **překrývající se podproblémy** + **optimální podstruktura**. (Liší se od R&P, kde jsou podproblémy nezávislé.)

- **Memoizace** (shora dolů): rekurze + lookup do tabulky.
- **Iterativně** (zdola nahoru): vyplň tabulku ve vhodném pořadí.

| Úloha | rekurence / klíč | složitost |
|---|---|---|
| Fibonacci | $T[k]=T[k-1]+T[k-2]$ | $O(n)$ |
| NRP | $D[i]=1+\max_{j>i,\,x_j>x_i}D[j]$ | $O(n^2)$ |
| Editační vzdálenost | $1+\min\{$záměna, smazání, vložení$\}$ | $O(mn)$ |
| Optimalizace [[BVS]] | zkoušení kořene přes rozsahy | $O(n^3)$ |
| Triangulace mnohoúhelníku | třetí vrchol u hrany | $O(n^3)$ |

NRP ≡ **nejdelší cesta v [[DAG]]** (DP je často hledání cesty v grafu).

---

## Co odpovědět rychle
- **Rozděl a panuj:** rozděl–vyřeš–slij, nezávislé podproblémy, $T(n)=aT(n/b)+f(n)$. MergeSort $n\log n$, Karatsuba $n^{1{,}59}$.
- **Rekurze vs. iterace:** převoditelné; rekurze krátká ale zásobník + opakované výpočty (fib $\varphi^n$ vs. $n$).
- **DP:** opakující se podproblémy → tabulka (memoizace / zdola nahoru). NRP $n^2$, edit. vzdálenost $mn$.
- **DP × R&P:** opakující se vs. nezávislé podproblémy.
