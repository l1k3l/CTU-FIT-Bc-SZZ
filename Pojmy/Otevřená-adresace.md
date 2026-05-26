---
aliases: [otevřená adresace, otevřené adresace, otevřenou adresaci, uzavřené hešování, closed hashing, open addressing]
tags: [definice, datová-struktura, kurz/AG1]
---

# Otevřená adresace

## Definice
**Otevřená adresace** (Open addressing, Closed hashing) je metoda řešení kolizí v [[Hešovací-tabulka|hešovací tabulce]]: každá přihrádka obsahuje **přímo jeden prvek** (nebo je prázdná / náhrobek). Při kolizi se zkouší další přihrádky podle **vyhledávací posloupnosti** $h(k, 0), h(k, 1), \dots, h(k, m-1)$, která je ideálně **permutací** $\{0, \dots, m-1\}$.

Faktor naplnění je vždy $\alpha = n/m < 1$.

## Vyhledávací posloupnosti
- **Lineární přidávání** (Linear Probing): $h(k, i) = (f(k) + i) \bmod m$. Jednoduché, sekvenční přístup do paměti (cache-friendly), ale tvoří se **shluky** obsazených přihrádek.
- **Lineární přidávání s krokem $c$:** $h(k, i) = (f(k) + c \cdot i) \bmod m$, $c$ nesoudělné s $m$.
- **Dvojité hešování** (Double Hashing): $h(k, i) = (f(k) + i \cdot g(k)) \bmod m$, kde $g(k) \in \{1, \dots, m-1\}$ a $m$ je prvočíslo. Pro náhodné $f, g$ se chová jako plně náhodná posloupnost.

## Operace
- **`OpenFind(k)`**: pro $i = 0, \dots, m-1$ zkoušej $A[h(k, i)]$. Pokud klíč nalezen → úspěch; pokud prázdná přihrádka → neúspěch (klíč ve slovníku není).
- **`OpenInsert(x)`**: hledej první prázdnou přihrádku nebo náhrobek a vlož.
- **`OpenDelete(x)`**: prvek nahraď **náhrobkem** $\dagger$ (nelze označit prázdnou — přerušilo by to vyhledávací posloupnost).

## Náhrobky
Mazání pouze **označuje** prvek za smazaný, neuvolňuje místo. Když počet náhrobků překročí mez ($\sim m/4$), tabulka se **přehešuje** (rebuild).

## Efektivita
**Věta:** Pokud jsou vyhledávací posloupnosti náhodné permutace, pak neúspěšné hledání ve středu navštíví nejvýše $1/(1-\alpha)$ přihrádek.

## Související
- [[Hešovací-tabulka]]
- [[Hešování-s-řetízky]]
