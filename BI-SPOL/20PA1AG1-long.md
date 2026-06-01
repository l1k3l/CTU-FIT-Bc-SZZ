---
tags: [otázka, kurz/PA1, kurz/AG1, otázka/20, todo]
---

# Složitost, vyhledávání a řazení

> **Otázka SZZ:** Časová a paměťová složitost algoritmů. Algoritmy vyhledávání (sekvenční, půlením intervalu), slučování a řazení (BubbleSort, SelectSort, InsertSort, MergeSort, QuickSort). Dolní mez složitosti řazení v porovnávacím modelu. Řazení v lineárním čase.

Zdroje: BI-PA1 přednáška `l09-cplx` (Balík, Trávníček, Vagner, Vogel); BI-AG1 přednášky 2, 8, 9 (Knop, Opler, Valla, FIT ČVUT).

---

## 1. Časová a paměťová složitost algoritmů

### 1.1 Výpočetní model RAM
**RAM** (Random Access Machine): paměť je pole celočíselných buněk adresovatelných celými čísly; program je konečná posloupnost sekvenčně prováděných instrukcí (aritmeticko-logické a řídicí — skoky, podmíněné skoky, zastavení). V každém kroku se provede právě jedna instrukce.

### 1.2 Definice složitosti
![[Časová-složitost#Definice]]

- **Časovou složitost neměříme experimentálně**, ale analýzou algoritmu — počítáme počet elementárních operací jako funkci velikosti vstupu $n$. Je nezávislá na jazyce a hardwaru; popisuje **trend** růstu.
- *Příklad (přesné počítání):* součet pole `arraySum` provede $T(n) = 3 + 3n$ operací.

### 1.3 Tři případy
Složitost závisí na konkrétních datech, proto rozlišujeme **nejhorší** (worst), **průměrný** (average) a **nejlepší** (best) případ. Pro lineární hledání: $T_{best}=3$, $T_{avg}=2+1{,}5n$, $T_{worst}=2+3n$. Průměrný případ bývá nejtěžší na analýzu, proto se často spokojíme s nejhorším.

### 1.4 Asymptotická notace
Zajímá nás trend, proto přejdeme k asymptotice: zachováme jen člen nejvyššího řádu a vynecháme multiplikativní konstanty. Používáme [[Asymptotická-notace|asymptotickou notaci]]:
$$T(n) \in O(f(n)) \iff \exists n_0\in\mathbb{N},\, c>0:\ \forall n \ge n_0:\ T(n) \le c\cdot f(n).$$

> BI-PA1 zavádí jen velké $O$; BI-AG1 používá i $\Omega$ (dolní mez) a $\Theta$ (těsná mez).

Třídy složitosti (vzestupně): $O(\log\log n) < O(\log n) < O(n) < O(n\log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$. Drobné modifikace (např. zarážka) zmenší jen konstantu, trend nezmění.

---

## 2. Algoritmy vyhledávání

### 2.1 Sekvenční (lineární) vyhledávání
Postupně porovnává prvky s hledanou hodnotou.
```c
int arraySearch ( int arr[], int n, int x ) {
  for ( int i = 0; i < n; i++ )
    if ( arr[i] == x ) return i;
  return -1;
}
```
**Složitost:** $T_{best}=O(1)$ (na začátku), $T_{worst}=O(n)$. **Nepotřebuje seřazené pole.**

*Optimalizace zarážkou:* hledanou hodnotu zapíšeme za poslední prvek (`arr[n]=x`), takže odpadne porovnání indexu s $n$ — z $T=3n+2$ na $T=2n+3$, stále $O(n)$ (jen menší konstanta).

### 2.2 Binární vyhledávání (půlením intervalu)
**Předpoklad: seřazené pole.** V každém kroku porovnáme hledané $x$ s prostředním prvkem a polovinu intervalu zahodíme.
```c
bool binarySearch ( int arr[], int n, int x ) {
  int lo = 0, hi = n - 1;
  while ( lo <= hi ) {
    int mid = lo + (hi - lo) / 2;     // ne (lo+hi)/2 — přetečení
    if      ( x < arr[mid] ) hi = mid - 1;
    else if ( x > arr[mid] ) lo = mid + 1;
    else return true;
  }
  return false;
}
```
**Složitost:** $T(n) = T(n/2) + O(1)$. Po $k$ krocích je $n/2^k = 1 \Rightarrow k = \log_2 n$, tedy **$O(\log n)$**. Pro velmi malá pole ($\sim 10$ prvků) může být lineární hledání rychlejší (menší skrytá konstanta).

---

## 3. Slučování a řazení

**Problém řazení:** dáno pole $a$ s $n$ hodnotami, uspořádat je tak, že $a[0] \le a[1] \le \dots \le a[n-1]$.

Vlastnosti řadicích algoritmů: **stabilita** (zachování pořadí stejných klíčů), **in-place** (paměť $O(1)$ navíc), **datová citlivost** (závislost na uspořádání vstupu).

### 3.1 Elementární (kvadratické) řazení

**BubbleSort (záměnou):** opakovaně porovnává sousední prvky a chybně uspořádané prohazuje. *Invariant:* po $k$-té iteraci je posledních $k$ prvků na svém místě.
```c
void bubbleSort ( int * a, int n ) {
  bool sorted;
  do { sorted = true;
    for ( int i = 0; i < n-1; i++ )
      if ( a[i] > a[i+1] ) { swap(&a[i], &a[i+1]); sorted = false; }
  } while ( !sorted );
}
```
$T_{worst} = O(n^2)$; s příznakem `sorted` je $T_{best} = O(n)$ na seřazeném poli. Stabilní, in-place.

**SelectSort (výběrem):** opakovaně najde minimum zbytku pole a prohodí ho na začátek nesetříděné části.
```c
void selectSort ( int * a, int n ) {
  for ( int i = 0; i < n-1; i++ ) {
    int imin = i;
    for ( int j = i+1; j < n; j++ ) if ( a[j] < a[imin] ) imin = j;
    if ( imin != i ) swap(&a[imin], &a[i]);
  }
}
```
Počet porovnání $\sum_{i} i = n(n-1)/2 = O(n^2)$ ve všech případech. **Šetří na počtu záměn** ($\le n-1$). In-place, není stabilní.

**InsertSort (vkládáním):** udržuje seřazený začátek a každý další prvek do něj zatřídí posunem.
```c
void insert ( int * a, int n, int x ) {
  int i;
  for ( i = n-1; i >= 0 && a[i] > x; i-- ) a[i+1] = a[i];
  a[i+1] = x;
}
void insertSort ( int * a, int n ) {
  for ( int i = 1; i < n; i++ ) insert(a, i, a[i]);
}
```
$T_{worst}=O(n^2)$, $T_{best}=O(n)$ (na seřazeném poli). Stabilní, in-place, datově citlivý.

| Algoritmus | best | avg | worst | paměť | stabilní | in-place |
|---|---|---|---|---|---|---|
| Bubble | $O(n)$* | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ano | ano |
| Select | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ne | ano |
| Insert | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ano | ano |

\* s příznakem `sorted`.

### 3.2 MergeSort (řazení sléváním)
Učebnicový příklad metody **[[Rozděl-a-panuj|rozděl a panuj]]**. Posloupnost o 1 prvku je seřazená; jinak rozdělíme na poloviny, obě rekurzivně seřadíme a **slijeme**.

![[MergeSort#Vlastnosti]]

**Procedura `Merge`** slévá dvě seřazené posloupnosti porovnáváním jejich čel:
```
Merge(x₁..xₘ ; y₁..yₙ):
  i:=1; j:=1; k:=1
  dokud i≤m a j≤n:
    pokud xᵢ ≤ yⱼ:  zₖ:=xᵢ; i++      // ≤ zaručuje stabilitu
    jinak:          zₖ:=yⱼ; j++
    k++
  doplň zbytek nevyčerpané posloupnosti
  vrať z₁..z_{m+n}
```
**Pozorování:** `Merge` přesune každý prvek právě jednou → čas $\Theta(n+m)$, pomocná paměť $\Theta(n+m)$.

**Věta:** Časová složitost MergeSortu je $\Theta(n\log n)$.
*Důkaz:* $T(1)=1$, $T(n)=2T(n/2)+cn$. Rozvinutím $T(n)=2^k T(n/2^k)+kcn$; pro $n/2^k=1$ je $k=\log n$, tedy $T(n)=\Theta(n)+cn\log n=\Theta(n\log n)$. $\square$

**Věta:** Paměťová složitost je $\Theta(n)$ (vždy běží jen jedno z rekurzivních volání; $M(n)=dn+M(n/2)$ je geometrická řada se součtem $\Theta(n)$).

### 3.3 QuickSort
![[QuickSort#Definice]]

```
QuickSort(X = x₁..xₙ):
  pokud n ≤ 1: vrať X
  p := pivot z X
  L := prvky < p;  S := prvky = p;  P := prvky > p
  vrať  QuickSort(L), S, QuickSort(P)
```

**Strom rekurzivních volání (SRV):** součet velikostí podproblémů na každé hladině je $\le n$, rozklad i spojení jsou lineární → na jedné hladině $O(n)$ práce.
- **Nejlepší/průměrný:** pivot ≈ medián (skoromedián) → velikosti klesají exponenciálně, hloubka $O(\log n)$, celkem $O(n\log n)$.
- **Nejhorší:** pivot je extrém → hladin $\Theta(n)$, celkem $\Theta(n^2)$.

**Věta:** Střední hodnota časové složitosti QuickSortu s **rovnoměrně náhodnou volbou pivota** je $O(n\log n)$.
*Důkaz (skica):* Stačí odhadnout počet porovnání ($O(1)$ práce na porovnání). Pro výstupní pořadí $y_1<\dots<y_n$ a $i<j$ buď $C_{ij}=1$, pokud byly $y_i,y_j$ porovnány. Porovnají se, právě když se z $\{y_i,\dots,y_j\}$ stane pivotem jako první $y_i$ nebo $y_j$, tedy s pravděpodobností $\mathbf{E}[C_{ij}] = \tfrac{2}{j-i+1}$. Pak
$$\mathbf{E}[C] = \sum_{i<j}\frac{2}{j-i+1} < 2n\sum_{d=2}^{n}\frac1d = 2n\cdot\Theta(\log n) = O(n\log n),$$
neboť harmonická řada $H_n = \Theta(\log n)$. $\square$

Při pevné pozici pivota hrozí $\Theta(n^2)$ od zlomyslného vstupu → **randomizace**. (Stejná myšlenka $L/S/P$ řeší i hledání $k$-tého nejmenšího prvku — QuickSelect, ve střední hodnotě $O(n)$.)

> **Optimální $O(n\log n)$ řadicí algoritmy:** HeapSort (přes [[Binární-halda|binární haldu]], $O(n\log n)$ in-place), MergeSort, QuickSort.

---

## 4. Dolní mez složitosti řazení v porovnávacím modelu

### 4.1 Porovnávací model
Algoritmus smí prvky pouze **porovnávat** a **přesouvat**. **Porovnání** `cmp(aᵢ,aⱼ)` v konstantním čase řekne, zda $a_i <, =, >\ a_j$. Uvažujeme **deterministické** algoritmy.

### 4.2 Věta o dolní mezi řazení
**Věta:** Každý deterministický algoritmus v porovnávacím modelu, který seřadí $n$-prvkovou posloupnost, použije v nejhorším případě **$\Omega(n\log n)$** porovnání.

*Důkaz (rozhodovací strom):*
- Uvažujme vstupy = permutace $\{1,\dots,n\}$ (různé prvky, takže $=$ nenastane).
- Algoritmus $S$ upravíme tak, aby nejprve provedl všechna porovnání a teprve nakonec přeházel prvky. Jeho běh popíšeme **rozhodovacím stromem** $T_S$: vnitřní vrcholy jsou porovnání se **dvěma** výsledky ($<$/$>$), listy jsou výstupní permutace přesunů.
- Dvě různé vstupní permutace musí skončit v **různých listech** (nelze je seřadit toutéž posloupností přesunů). Proto má $T_S$ alespoň $n!$ listů.
- Binární strom s $n!$ listy má hloubku $\ge \log(n!)$. Ze Stirlingovy formule $\log(n!) = \Omega(n\log n)$.
- Existuje tedy vstup, na němž $S$ provede $\ge \log(n!) = \Omega(n\log n)$ porovnání. $\square$

**Důsledek:** MergeSort, HeapSort i (randomizovaný) QuickSort jsou **asymptoticky optimální**.

**Důsledek (ExtractMin):** Každá implementace `ExtractMin` v binární haldě má $\Omega(\log n)$ — jinak by `HeapBuild` ($O(n)$) + $n\times$`ExtractMin` seřadilo v $o(n\log n)$, spor.

> Analogicky platí dolní mez **$\Omega(\log n)$ pro vyhledávání v seřazené posloupnosti** (ternární rozhodovací strom s $\ge n+1$ listy, hloubka $\ge \log_3 n$) → binární vyhledávání je optimální.

---

## 5. Řazení v lineárním čase

Tyto algoritmy seřadí rychleji než $O(n\log n)$, **aniž porušují dolní mez** — nepracují v porovnávacím modelu, ale využívají speciální vlastnost vstupu (omezený rozsah klíčů). Nelze je tedy použít na obecnou posloupnost.

### 5.1 CountingSort (počítací řazení)
Řadí $n$ celých čísel z $\{1,\dots,r\}$: spočítá histogram výskytů, z něj **prefixovým součtem** počáteční pozice, a podle nich umístí prvky.
```
CountingSort(x₁..xₙ ∈ {1..r}):
  pro j:=1..r: pocet[j]:=0
  pro i:=1..n: pocet[xᵢ]++                 // histogram
  zacatek[1]:=1
  pro j:=2..r: zacatek[j]:=zacatek[j-1]+pocet[j-1]   // prefixový součet
  pro i:=1..n: vystup[zacatek[xᵢ]]:=xᵢ; zacatek[xᵢ]++
  vrať vystup
```
**Časová i paměťová složitost $\Theta(n+r)$**, **stabilní**, není in-place. Pro $r=O(n)$ je lineární.

### 5.2 LexCountingSort / RadixSort (číslicové řazení)
Řadí $n$ k-tic z $\{1,\dots,r\}^k$ lexikograficky tak, že opakovaně použije **stabilní** CountingSort **od poslední souřadnice k první**:
```
LexCountingSort(X₁..Xₙ):
  pro i := k, k-1, …, 1:  setříď CountingSortem podle souřadnice i
```
**Věta:** Algoritmus řadí správně (indukcí přes souřadnice; stabilita CountingSortu zachová dříve setříděné pořadí).
**Složitost:** čas $\Theta(k(n+r))$, paměť $\Theta(kn+r)$ — lineární s délkou vstupu pro pevné $k,r$. Na stejném principu stojí **RadixSort** pro víceciferná čísla.

---

## 6. Co je potřeba na zkoušku znát

### Definice
- RAM model; časová a paměťová složitost (nejhorší/průměrný/nejlepší případ); asymptotická notace $O/\Omega/\Theta$.
- Stabilita, in-place, datová citlivost řadicího algoritmu.
- Porovnávací model, rozhodovací strom.

### Věty s důkazy
- **Dolní mez řazení $\Omega(n\log n)$** přes rozhodovací strom ($n!$ listů, hloubka $\ge\log(n!)=\Omega(n\log n)$, Stirling).
- Dolní mez vyhledávání $\Omega(\log n)$ (ternární strom).
- MergeSort $\Theta(n\log n)$ (rekurence $2T(n/2)+cn$), paměť $\Theta(n)$.
- QuickSort: střední hodnota $O(n\log n)$ (porovnání $y_i,y_j$ s pravd. $2/(j-i+1)$, harmonická řada).
- LexCountingSort korektní (indukce + stabilita).

### Algoritmy (pseudokód + složitost)
- Sekvenční hledání $O(n)$, binární hledání $O(\log n)$ (rekurence $T(n/2)+O(1)$).
- Bubble/Select/Insert $O(n^2)$ (best Insert/Bubble $O(n)$).
- MergeSort $\Theta(n\log n)$, `Merge` $\Theta(n+m)$.
- QuickSort (rozklad $L/S/P$): avg $O(n\log n)$, worst $\Theta(n^2)$.
- CountingSort $\Theta(n+r)$, LexCountingSort/RadixSort $\Theta(k(n+r))$.
