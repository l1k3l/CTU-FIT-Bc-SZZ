---
tags: [otázka, kurz/PA1, kurz/AG1, otázka/21, todo]
---

# Rozděl a panuj, rekurze vs. iterace, dynamické programování

> **Otázka SZZ:** Rekurzivní rozklad problému na podproblémy metodou Rozděl-a-panuj. Rekurze vs iterace. Dynamické programování.

Zdroje: BI-PA1 přednáška `l10-recursion` (Balík, Trávníček, Vagner, Vogel); BI-AG1 přednášky 8 (Rozděl a Panuj) a 10 (Dynamické programování) (Knop, Opler, Valla, FIT ČVUT).

---

## 1. Rekurzivní rozklad metodou Rozděl a panuj

### 1.1 Rekurze
![[Rekurze#Definice]]

**Zásobník volání:** každé zanoření vytvoří na systémovém zásobníku **aktivační záznam** s lokálními proměnnými. Hloubka rekurze určuje spotřebu paměti na zásobníku; příliš hluboká rekurze ho přeteče. *(Příklad: rekurzivní výpis posloupnosti v obráceném pořadí — hodnoty se vypisují až při „odvíjení" zásobníku.)*

### 1.2 Metoda Rozděl a panuj
![[Rozděl-a-panuj#Definice]]

Složitost se popisuje rekurentní rovnicí $T(n)=a\,T(n/b)+f(n)$ a řeší se **rozvinutím** nebo součtem práce **přes hladiny stromu rekurzivních volání (SRV)**.

> Slidy BI-AG1 neuvádějí Master theorem (kuchařkovou větu) — rekurence řeší ručně rozvinutím a geometrickou řadou (odkaz na BI-MA2).

### 1.3 Příklady

**MergeSort** — viz [[MergeSort]]: rozdělení na poloviny + slévání, $T(n)=2T(n/2)+cn=\Theta(n\log n)$.

**Násobení dvou $n$-ciferných čísel.** Rozklad $x = x_U\cdot 10^{n/2}+x_L$, $y = y_U\cdot 10^{n/2}+y_L$:
$$xy = x_U y_U 10^{n} + (x_U y_L + x_L y_U)10^{n/2} + x_L y_L.$$
- **Naivní** (4 součiny polovičních čísel): $T(n)=4T(n/2)+\Theta(n)=\Theta(n^2)$ — rozklad nepomohl.
- **Karatsuba** (3 součiny díky $x_U y_L + x_L y_U = (x_U+x_L)(y_U+y_L) - x_U y_U - x_L y_L$): $T(n)=3T(n/2)+\Theta(n)$.

**Věta:** Karatsuba má složitost $\Theta(n^{\log_2 3})\approx\Theta(n^{1{,}59})$.
*Důkaz:* Na $i$-té hladině SRV je $3^i$ podproblémů velikosti $n/2^i$, práce $\Theta(n\,(3/2)^i)$; hloubka $\log n$. Součet je geometrická řada s kvocientem $3/2$:
$$T(n)=\Theta\!\Big(n\sum_{i=0}^{\log n}(3/2)^i\Big)=\Theta\big(n\,(3/2)^{\log n}\big)=\Theta(n\cdot n^{\log_2 3 - 1})=\Theta(n^{\log_2 3}).\ \square$$
*(Obdobně Strassenovo násobení matic: $7$ součinů → $O(n^{\log_2 7})$.)*

**QuickSelect** ($k$-tý nejmenší prvek bez řazení) — rozklad na $L/S/P$ jako [[QuickSort]]; rekurze jen do jedné části:
- nejhorší případ (extrémní pivot) $\Theta(n^2)$;
- s pivotem ≈ medián $T(n)=T(n/2)+\Theta(n)=\Theta(n)$ (geometrická řada).
- **RandomQuickSelect** (náhodný pivot, dokud není **skoromedián** = prvek v prostředních dvou čtvrtinách): ve střední hodnotě **$O(n)$** (2 pokusy/fázi, velikosti klesají faktorem $3/4$).

---

## 2. Rekurze vs. iterace

| | Rekurze (shora dolů) | Iterace (zdola nahoru) |
|---|---|---|
| Postup | od obecné instance k triviální | od triviální instance k obecné |
| Kód | krátký, srozumitelný | obvykle delší |
| Paměť | aktivační záznamy na zásobníku | $O(1)$ stavu (bez zásobníku) |
| Riziko | přetečení zásobníku, opakované podproblémy | — |

**Vzájemná převoditelnost:** každou rekurzi lze přepsat iterativně a naopak (faktoriál, Euklidův algoritmus, násobení, Fibonacci, MergeSort). Demonstrují to párové implementace.

**Motivace pro DP — naivní rekurzivní Fibonacci** ($f_n=f_{n-1}+f_{n-2}$):
```c
int fib ( int n ) { if ( n <= 2 ) return 1; return fib(n-1) + fib(n-2); }
```
**Pozorování (BI-AG1):** `FibRec(n)` má složitost $\Theta(F(n))=\Theta(\varphi^{\,n})$, $\varphi=\tfrac{1+\sqrt5}{2}\approx 1{,}618$.
*Důkaz:* SRV je plný binární strom; každý list vrací $1$ a součet listů je $F(n)$, takže listů je přesně $F(n)$ a vnitřních vrcholů nejvýše tolik. $\square$

Stejné podproblémy se počítají mnohokrát. **Iterativní řešení zdola nahoru** je lineární:
```c
int fib ( int n ) {
  int a = 1, b = 1;
  for ( int i = 3; i <= n; i++ ) { int t = a + b; a = b; b = t; }
  return n <= 2 ? 1 : b;
}
```
$\Rightarrow$ $\Theta(n)$. Odstranění opakovaných výpočtů je přesně myšlenka **dynamického programování**.

---

## 3. Dynamické programování

![[Dynamické-programování#Definice]]

### 3.1 Dvě realizace
- **Memoizace (shora dolů):** rekurze, která před výpočtem nahlédne do tabulky $T$; je-li hodnota uložena, vrátí ji, jinak ji spočte a uloží.
- **Iterativní řešení (zdola nahoru):** tabulka se vyplní bez rekurze ve vhodném pořadí od triviálních případů.

**Obecný postup:** (1) formuluj rekurzivní rozklad, (2) najdi opakované podproblémy, (3) zaveď tabulku, vyplň triviální instance, (4) vyplň zbytek (memoizací nebo iterativně) a případně si pamatuj volby pro **konstrukci** řešení.

### 3.2 Fibonacci
`FibMem`/`FibIter` vyplní tabulku $T[1..n]$ → **$O(n)$** čas i paměť (každé políčko se spočte jednou v $O(1)$).

### 3.3 Nejdelší rostoucí podposloupnost (NRP)
Vstup $x_1,\dots,x_n$; hledáme nejdelší rostoucí podposloupnost. Nechť $D[i]$ = délka nejdelší RP **začínající** prvkem $x_i$:
$$D[i] = 1 + \max\{\,D[j] : j>i,\ x_j > x_i\,\}\quad(\text{prázdné max} = 0).$$
- Naivní rekurze: $O(2^n)$ (SRV je podstrom binomiálního stromu $B_n$).
- DP (tabulka od $i=n$ k $1$): **$O(n^2)$**. Pamatováním následníka $N[i]$ se NRP **zrekonstruuje**.
- **Grafový pohled:** vrcholy $x_0=-\infty,\dots,x_{n+1}=+\infty$, hrany na potenciální následníky → hledání **nejdelší cesty v [[DAG|acyklickém grafu]]** v [[Topologické-uspořádání|topologickém uspořádání]] ($O(n^2)$). DP je často ekvivalentní hledání cesty ve vhodném grafu.

### 3.4 Editační (Levenshteinova) vzdálenost
$L(x,y)$ = nejmenší počet operací **vložení / smazání / záměny znaku** převádějících řetězec $x$ ($m$ znaků) na $y$ ($n$ znaků). Rekurence pro prefixy/sufixy: shodují-li se první znaky, $L=L(x',y')$; jinak
$$L = 1 + \min\{\,L(x',y')\ (\text{záměna}),\ L(x',y)\ (\text{smazání}),\ L(x,y')\ (\text{vložení})\,\}.$$
Báze: prázdný řetězec → délka druhého. Tabulka $M[1..m{+}1, 1..n{+}1]$ → **čas i paměť $O(mn)$**.

### 3.5 Další příklady (přehled)
- **Optimalizace [[BVS]] dle četností klíčů** $p_i$ (minimalizace $\sum h(i)p_i$): zkoušíme každý kořen, $M[\ell,u]$ přes rozsahy → **$O(n^3)$** čas, $O(n^2)$ paměť.
- **Minimální triangulace konvexního mnohoúhelníku:** $M[i,j]$ přes zkoušení třetího vrcholu trojúhelníka u hrany $a_ia_j$ → **$O(n^3)$** čas, $O(n^2)$ paměť. (Počet triangulací je Catalanovo číslo $2^{\Theta(n)}$, proto naivní rekurze exponenciální.)

### 3.6 DP vs. Rozděl a panuj
Obě metody rozkládají problém rekurzivně. **Rozděl a panuj** předpokládá **nezávislé** podproblémy; **DP** těží z **opakujících se** podproblémů — jejich řešení uchovává a znovu používá, čímž z exponenciální složitosti dělá polynomiální.

---

## 4. Co je potřeba na zkoušku znát

### Definice
- Rekurze (menší instance + základní případ), zásobník volání / aktivační záznam.
- Metoda Rozděl a panuj (rozděl–vyřeš–sluč), rekurence $T(n)=aT(n/b)+f(n)$.
- Dynamické programování; překrývající se podproblémy a optimální podstruktura; memoizace vs. iterativní (zdola nahoru).

### Věty a rozbory
- MergeSort $\Theta(n\log n)$; naivní násobení $\Theta(n^2)$; **Karatsuba $\Theta(n^{\log_2 3})$** (důkaz přes geometrickou řadu nad SRV).
- Naivní `FibRec` $\Theta(\varphi^n)$ (počet listů SRV $=F(n)$) vs. iterativní/DP $O(n)$.
- QuickSelect: medián-pivot $\Theta(n)$, náhodný (skoromedián) ve stř. hodnotě $O(n)$.

### Algoritmy a složitosti
- D&P: MergeSort, Karatsuba, QuickSelect (rekurence + řešení).
- DP: Fibonacci $O(n)$, NRP $O(n^2)$ (+ grafový pohled / nejdelší cesta v DAG), editační vzdálenost $O(mn)$, optimalizace BVS a triangulace mnohoúhelníku $O(n^3)$.
- Rekurze ↔ iterace: vzájemná převoditelnost; iterace odstraní zásobníkovou režii a opakované podproblémy.
