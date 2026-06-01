---
aliases: [dynamické programování, dynamického programování, dynamickému programování, dynamickým programováním, dynamickém programování, DP, dynamic programming, memoizace, memoizaci]
tags: [definice, kurz/AG1]
---

# Dynamické programování

## Definice
**Dynamické programování (DP)** je návrhová technika založená na rekurzivním rozkladu problému na podproblémy, která využívá toho, že se při rozkladu **podproblémy opakují**. Místo opakovaného výpočtu se každé řešení podproblému spočte jednou a **uloží do tabulky**. Vede k mnohem rychlejším algoritmům než přímočará [[Rekurze|rekurze]].

**Předpoklady:**
- **Překrývající se podproblémy** — během rozkladu vzniká jen polynomiálně mnoho různých podproblémů, které se opakovaně vyskytují.
- **Optimální podstruktura** — optimální řešení se skládá z optimálních řešení podproblémů.

(Tím se DP liší od [[Rozděl-a-panuj|rozděl a panuj]], kde jsou podproblémy nezávislé.)

## Dvě realizace
- **Memoizace (shora dolů, top-down):** rekurze, která před výpočtem nahlédne do tabulky; je-li hodnota uložena, vrátí ji, jinak ji spočte a uloží.
- **Iterativní řešení (zdola nahoru, bottom-up):** tabulka se vyplní bez rekurze ve vhodném pořadí od triviálních případů k celému problému.

## Obecný postup
1. Formuluj řešení rekurzivně rozkladem na podproblémy.
2. Identifikuj opakované výpočty.
3. Zaveď tabulku s řešeními podproblémů, vyplň triviální instance.
4. Vyplň zbytek (memoizací nebo iterativně), případně si pamatuj volby pro **konstrukci** optimálního řešení.

## Příklady (BI-AG1)
Fibonacci ($O(n)$), nejdelší rostoucí podposloupnost ($O(n^2)$), editační (Levenshteinova) vzdálenost ($O(mn)$), optimalizace BVS dle četností ($O(n^3)$), minimální triangulace mnohoúhelníku ($O(n^3)$). DP je často ekvivalentní hledání cesty ve vhodném [[DAG|acyklickém grafu]].

## Související
- [[Rekurze]]
- [[Rozděl-a-panuj]]
- [[DAG]]
