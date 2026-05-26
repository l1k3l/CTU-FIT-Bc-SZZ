---
tags: [otázka, kurz/AG1, otázka/4, todo]
---

# Datové struktury: haldy, BVS, hešování

> **Otázka SZZ:** Binární haldy, binomiální haldy. Binární vyhledávací stromy a jejich vyvažování. Hešovací tabulky.

Zdroje: BI-AG1 přednášky 4, 5, 6, 7 (Knop, Opler, Valla, FIT ČVUT).

---

## 1. Binární haldy

### 1.1 Motivace
Chceme dynamickou datovou strukturu pro reprezentaci množiny porovnatelných hodnot (priority úkolů). Operace:
- `Insert(x)` — vložení,
- `FindMin()` — nalezení momentálního minima,
- `ExtractMin()` — odstranění minima.

**Naivní řešení (neseřazené pole):** `Insert` $O(1)$, `FindMin`/`ExtractMin` $O(n)$. **Seřazené pole:** `FindMin` $O(1)$, ale `Insert` $O(n)$. Haldová struktura dosahuje $O(\log n)$ pro všechny tři.

### 1.2 Definice
**[[Binární-halda|Binární minimová halda]]** je datová struktura tvaru binárního stromu, v jehož každém vrcholu $x$ je klíč $k(x)$ a která splňuje:
1. **Tvar haldy:** Všechny hladiny kromě poslední jsou plně obsazené; poslední je zaplněna od levého okraje doprava.
2. **Haldové uspořádání:** Pro vrchol $v$ a jeho syna $s$ platí $k(v) \le k(s)$.

Analogicky **maximová halda** ($\ge$ místo $\le$). Implicitně dále uvažujeme minimovou.

**Pozorování:** Na cestě z libovolného vrcholu ke kořeni tvoří klíče nerostoucí posloupnost. V kořeni je globální minimum.

### 1.3 Počet hladin a listů
**Lemma:** Binární halda s $n$ prvky má $\lfloor \log n \rfloor + 1$ hladin.

*Důkaz:* Binární strom s $h$ úplnými hladinami má $2^0 + 2^1 + \dots + 2^{h-1} = 2^h - 1$ vrcholů. Z tvaru haldy plyne, že nová hladina přibude právě tehdy, když $n$ vzroste z $2^h - 1$ na $2^h$. Pro takové $n$ je $\lfloor \log n \rfloor + 1 = h + 1$, jak požadujeme. $\square$

**Lemma:** Halda s $n \ge 3$ prvky má $\lfloor n/2 \rfloor$ vnitřních vrcholů a $\lceil n/2 \rceil$ listů. *(Indukcí podle $n$.)*

### 1.4 Reprezentace v poli
Vrcholy očíslujeme po hladinách shora dolů a na nich zleva doprava (od 1 do $n$). Pak pro vrchol s indexem $i$:
- levý syn má index $2i$,
- pravý syn má index $2i + 1$,
- otec má index $\lfloor i/2 \rfloor$.

Haldu tak reprezentujeme v poli velikosti $n$ bez explicitních ukazatelů.

### 1.5 `HeapInsert`
```
Algoritmus HeapInsert(H, k)
(1) H.n := H.n + 1
(2) Vlož na první volnou pozici v poslední hladině H
    nový vrchol p s klíčem k
(3) BubbleUp(H, p)

BubbleUp(H, p)
(4) Dokud p ≠ H.root:
(5)     o := otec(p)
(6)     Pokud k(o) ≤ k(p): return
(7)     Prohoď k(o) a k(p)
(8)     p := o
```

**Idea:** Nový list může porušit haldové uspořádání mezi sebou a otcem. Pokud ano, prohodíme — to může porušit uspořádání o úroveň výš, takže bublání pokračuje nahoru až do kořene.

**Korektnost:** Před `BubbleUp` existuje nejvýše jedna hrana porušující haldové uspořádání — ta mezi novým listem a otcem. Bublání tuto poruchu posouvá výš až do bodu, kde otec má menší klíč, nebo do kořene (který otce nemá).

**Složitost:** $O(\log n)$ — projde maximálně logaritmický počet hladin, na každé $O(1)$.

### 1.6 `HeapExtractMin`
```
Algoritmus HeapExtractMin(H)
(1) r := H.root, x := k(r), ℓ := H.last
(2) Prohoď k(r) a k(ℓ)
(3) H.n := H.n - 1            // odřízni starý kořen (= ℓ)
(4) BubbleDown(r)
(5) return x

BubbleDown(v)
(6) Dokud v má alespoň jednoho syna:
(7)     s := syn v s nejmenším klíčem
(8)     Pokud k(v) ≤ k(s): return
(9)     Prohoď k(v) a k(s)
(10)    v := s
```

**Idea:** Tvar haldy nedovoluje smazat kořen přímo; smažeme **poslední list** $\ell$, jeho klíč přesuneme na pozici kořene a tento klíč „probubláme dolů" na své správné místo.

**Korektnost & složitost:** Analogicky jako `HeapInsert`, $O(\log n)$.

### 1.7 `HeapBuild` v čase $O(n)$
Naivně by $n$ volání `HeapInsert` dalo $O(n \log n)$. Lze rychleji: pole inicializujeme libovolně a opravujeme **zdola nahoru**.

```
HeapBuild
Vstup: prvky x_1, …, x_n
Výstup: halda H[1..n]
(1) Vlož prvky do pole: H[i] := x_i
(2) Pro i := ⌊n/2⌋, …, 1:
(3)     BubbleDown(H[i])
```

**Idea:** Listy ($\lceil n/2 \rceil$ posledních pozic) jsou triviálně 1-prvkové haldy. Bubláním dolů od `⌊n/2⌋` ke kořeni vždy spojíme dvě již opravené haldy s jejich rodičem.

**Věta:** `HeapBuild` má časovou složitost $O(n)$.

*Důkaz:* Procedura `BubbleDown` z $j$-té hladiny trvá $O(h-1-j)$, kde $h = \lfloor \log n \rfloor + 1$. Sečteme přes $2^j$ vrcholů hladiny $j$:
$$\sum_{j=0}^{h-1} 2^j(h-1-j) = \sum_{q=0}^{h-1} 2^{h-1-q} \cdot q \le n \sum_{q=0}^\infty \frac{q}{2^q} = O(n),$$
neboť řada $\sum q/2^q$ konverguje k konstantě (d'Alembertovo kritérium). $\square$

### 1.8 `HeapSort`
Vlož prvky do pole, zavolej `HeapBuild` ($O(n)$), pak $n$-krát zavolej `HeapExtractMin` ($O(\log n)$ každé). Celkem $O(n) + O(n \log n) = O(n \log n)$. Lze realizovat **in-place** (max-haldou nad polem a postupným zápisem maxima na konec pole).

### 1.9 Amortizovaná analýza — vsuvka
**Definice:** Operace $A$ má v daném kontextu **[[Amortizovaná-složitost|amortizovanou složitost]]** $O^*(f(n))$, pokud posloupnost $k$ operací trvá celkem $O(k \cdot f(n))$. Jednotlivé volání může být v nejhorším případě i řádově dražší.

**Příklady ze 4. přednášky:**
- **[[Nafukovací-pole]]:** `NPInsert` má amortizovanou složitost $\Theta^*(1)$ při zdvojnásobovací strategii (celkový čas $n$ vkládání je $\Theta(n)$, neboť $1 + 2 + 4 + \dots + 2^k < 2^{k+1} \le 2n$).
- **[[Binární-sčítačka]]:** `Inc` má amortizovanou složitost $O^*(1)$ — viz **bankéřova metoda**: každé operaci `Inc` přidělíme 2 mince. Jednu utratíme za inverzi prvního nulového bitu (0 → 1), druhou uložíme na nově vzniklý jedničkový bit. Invariant: **na každém jedničkovém bitu leží jedna naspořená mince**. Inverze jedniček zpět na nuly se hradí z těchto mincí. Celkem ≤ $2n$ inverzí v $n$ voláních.

Tyto dvě analýzy potřebujeme i pro binomiální haldu (`BHInsert`) a pro nafukovací hešovací tabulku.

---

## 2. Binomiální haldy

### 2.1 Motivace
Binární halda neumí rychle **slučovat** dvě haldy (musíme zavolat `HeapBuild` v $O(m+n)$). Chceme strukturu, kde **`Merge`** je $O(\log n)$ a **`Insert`** má amortizovaně $O^*(1)$. Binomiální halda patří do rodiny **mergeable heaps**.

### 2.2 [[Binomiální-strom|Binomiální strom]]

**Definice (rekurzivní):** Binomiální strom řádu $k$, značíme $B_k$, je uspořádaný zakořeněný strom:
- $B_0$ je tvořen jediným vrcholem (kořenem).
- Pro $k \ge 1$ získáme $B_k$ ze stromů $B_0, B_1, \dots, B_{k-1}$ přidáním nového kořene a napojením jejich kořenů (v tomto pořadí) jako synů nového kořene.

**Alternativní definice ($B'_k$):** $B'_0$ je jediný vrchol; $B'_k$ vznikne ze dvou stromů $B'_{k-1}$ tím, že kořen jednoho připojíme jako nejpravějšího syna kořene druhého.

**Lemma:** $B_k$ a $B'_k$ jsou izomorfní. *(Indukcí podle $k$.)*

**Vlastnosti $B_k$:**
- Počet hladin: $k + 1$.
- Stupeň kořene: $k$.
- Počet vrcholů: $2^k$.
- Počet vrcholů na hladině $i$: $\binom{k}{i}$ (proto „binomiální"). *(Pascalovo pravidlo + indukce.)*

### 2.3 Definice binomiální haldy
**[[Binomiální-halda|Binomiální halda]] (BH)** obsahující $n$ prvků je uspořádaná množina binomiálních stromů $\mathcal{T} = T_1, \dots, T_\ell$, kde:
- Stromy jsou uspořádány **vzestupně podle svého řádu**.
- $n = |V(T_1)| + \dots + |V(T_\ell)|$.
- Pro každé nezáporné $k$ je v $\mathcal{T}$ **nejvýše jeden** strom řádu $k$.
- Každý vrchol obsahuje klíč $k(v)$.
- V každém stromě platí **haldové uspořádání**: $\forall v$ a všechny jeho syny $s_j$ platí $k(v) \le k(s_j)$.

### 2.4 Klíčová vlastnost
**Tvrzení:** Binomiální strom $B_i$ se vyskytuje v $n$-prvkové BH **právě tehdy, když** ve dvojkovém zápisu $b_k b_{k-1} \dots b_0$ čísla $n$ je $b_i = 1$.

*Důkaz:* Každý $B_i$ má $2^i$ vrcholů a každý řád se vyskytuje nejvýše jednou ⟹ rozklad $n$ na velikosti stromů odpovídá dvojkovému zápisu. $\square$

**Důsledek:** $n$-prvková BH obsahuje **$O(\log n)$** binomiálních stromů.

### 2.5 Operace `BHFindMin`
Minimum se nachází v jednom z **kořenů** stromů $T_i$. Stačí projít seznam — $O(\log n)$. Pokud udržujeme globální ukazatel na minimový kořen, je `BHFindMin` v $O(1)$.

### 2.6 `BHMergeTree`
Slévá dva binomiální stromy **stejného řádu** $B_i$ do jednoho $B_{i+1}$.

```
Algoritmus BHMergeTree(T1, T2)
Vstup: stromy se řád(T1) = řád(T2)
(1) Pokud k(kořen(T1)) ≤ k(kořen(T2)):
(2)     Připoj kořen(T2) jako nejpravějšího syna kořene(T1).
(3)     T_out := T1
(4) Jinak:
(5)     Připoj kořen(T1) jako nejpravějšího syna kořene(T2).
(6)     T_out := T2
```

Výsledek je korektní $B_{i+1}$ s haldovým uspořádáním. Při vhodné reprezentaci (ukazatel na otce, nejpravějšího syna a levého sourozence) je `BHMergeTree` v čase $O(1)$.

### 2.7 `BHMerge`
**Idea:** Slučujeme dvě BH $A$ a $B$ tak, jako by se sčítaly dvě binární čísla — odzdola, s **přenosem** odpovídajícím stromu $carry_i$ řádu $i$. Pokud máme v daném řádu 0, 1, 2 nebo 3 stromy (z $A$, $B$ a $carry$):
- 0 nebo 1 strom → zapíšeme do výsledku.
- 2 stromy → slijeme `BHMergeTree`em, výsledek se stane $carry$ do dalšího řádu.
- 3 stromy → jeden zapíšeme, dva slijeme do $carry$.

**Věta:** `BHMerge(A, B)` je korektní a má časovou složitost $O(\log n)$.

*Důkaz:* Iterace běží přes řády 0 až $O(\log n)$, každá iterace má $O(1)$ práce (`BHMergeTree` v $O(1)$). $\square$

### 2.8 `BHInsert`
```
BHInsert(H, x):
(1) Vytvoř BH H' s jediným prvkem x
(2) BHMerge(H, H')
```

**V nejhorším případě:** $O(\log n)$.

**Tvrzení:** `BHInsert` má amortizovanou složitost **$\Theta^*(1)$**.

*Důkaz:* Posloupnost $n$ volání `BHInsert` na zpočátku prázdnou BH odpovídá $n$-krát operaci `Inc` v [[Binární-sčítačka|binární sčítačce]] — slévání stromů řádu $i$ odpovídá bitové inverzi $i$-tého bitu. Z amortizované analýzy sčítačky dostáváme $O^*(1)$. $\square$

**Důsledek:** `BHBuild` ($n$ volání `BHInsert`) trvá $O(n)$.

### 2.9 `BHExtractMin`
```
Algoritmus BHExtractMin(H)
(1) Najdi v H strom T, jehož kořen je minimum.
(2) Odpoj T z H.
(3) Odtrhni z T kořen.       // zbude posloupnost B_0, …, B_{k-1}
(4) Z těchto synů vytvoř novou BH H'.
(5) BHMerge(H, H').
```

**Časová složitost:** $O(\log n)$. Kroky (1)–(2) jsou v $O(1)$ s minimovým ukazatelem; (3)–(4) v $O(\log n)$ (kořen má nejvýše $\log n$ synů); slučování v $O(\log n)$.

### 2.10 Paměťová reprezentace BH
Každý prvek BH má 4 ukazatele:
- na otce,
- hodnotu $k(v)$,
- na levého sourozence,
- na nejpravějšího syna.

Tato reprezentace umožňuje `BHMergeTree` v $O(1)$ a vytvoření nové BH ze synů kořene v $O(\log n)$.

### 2.11 Srovnání binární vs. binomiální halda

| Operace | Binární halda | Binomiální halda |
|---|---|---|
| `Insert` | $O(\log n)$ nejhůř | $O(\log n)$ nejhůř, **amort. $\Theta^*(1)$** |
| `ExtractMin` | $O(\log n)$ | $O(\log n)$ |
| `Merge` | $O(n+m)$ (přes `HeapBuild`) | $O(\log n)$ |
| Paměť | menší (1 ukazatel/prvek nebo pole) | větší (4 ukazatele/prvek) |

---

## 3. Binární vyhledávací stromy a jejich vyvažování

### 3.1 Značení v binárním stromě
Pro vrchol $v$ binárního stromu $T$:
- $\ell(v), r(v)$ — levý / pravý syn,
- $L(v), R(v)$ — levý / pravý podstrom,
- $p(v)$ — otec,
- $T(v)$ — podstrom s kořenem $v$,
- $h(T)$ — hloubka stromu (počet hladin).

Pokud syn neexistuje, položíme ho roven $\emptyset$ a doplníme $h(T(\emptyset)) = 0$.

### 3.2 Definice [[BVS|BVS]]
**Binární vyhledávací strom (BVS)** je binární strom, v jehož každém vrcholu $v$ je uložen **unikátní** klíč $k(v)$ a pro každý vrchol platí:
- Pro $a \in L(v)$: $k(a) < k(v)$.
- Pro $b \in R(v)$: $k(b) > k(v)$.

**Důsledek (InOrder):** Procházení levý—kořen—pravý vrátí klíče **vzestupně**.

### 3.3 Operace BVS

| Operace | Význam | Složitost |
|---|---|---|
| `BVSShow(v)` | vzestupný výpis klíčů $T(v)$ | $\Theta(|T(v)|)$ |
| `BVSMin(v)` / `BVSMax(v)` | extrémy v $T(v)$ | $O(h)$ |
| `BVSFind(v, x)` | najdi vrchol s klíčem $x$ | $O(h)$ |
| `BVSPred(v, w)` / `BVSSucc(v, w)` | předchůdce/následník v InOrder | $O(h)$ |
| `BVSInsert(v, x)` | vlož nový vrchol s klíčem $x$ jako list | $O(h)$ |
| `BVSDelete(v, x)` | odstraň vrchol s klíčem $x$ | $O(h)$ |

#### `BVSFind`
```
BVSFind(v, x)
(1) Pokud v = ∅: return ∅
(2) Pokud x = k(v): return v
(3) Pokud x < k(v): return BVSFind(ℓ(v), x)
(4) Pokud x > k(v): return BVSFind(r(v), x)
```

#### `BVSInsert`
Hledá $x$ jako u `BVSFind`; pokud klíč nenajde, vloží nový list na jednoznačně určenou pozici.

#### `BVSDelete`
Čtyři případy podle počtu synů:
1. Vrchol neexistuje → nic.
2. Vrchol je list → odtrhni.
3. Vrchol má jednoho syna → nahraď ho tímto synem.
4. Vrchol $u$ má dva syny → najdi $w = \text{BVSMin}(r(u))$, přepiš $k(u) \leftarrow k(w)$ a smaž $w$ (ten má nejvýše jednoho syna, případy 2/3).

### 3.4 Tvar BVS závisí na pořadí vkládání
Stejnou množinu klíčů lze reprezentovat různými BVS — tvar závisí na pořadí vkládání. Hloubka tedy není určena množinou klíčů.

**Pozorování:** $h(T(v))$ je v nejlepším případě $\Omega(\log |T(v)|)$, v nejhorším $O(|T(v)|)$ (degenerovaný strom při vložení $1, 2, \dots, n$).

### 3.5 Dokonale vyvážený BVS
**Definice:** BVS je **dokonale vyvážený**, pokud pro každý $v$ platí $||L(v)| - |R(v)|| \le 1$.

Hloubka dokonale vyváženého BVS s $n$ vrcholy je $1 + \lfloor \log n \rfloor$, takže `BVSFind`, `BVSInsert`, `BVSDelete` by trvaly $O(\log n)$.

**Věta (negativní):** Pokud má BVS zůstávat dokonale vyvážený, pak při jakékoli implementaci je časová složitost aspoň jedné z operací `BVSInsert`/`BVSDelete` $\Omega(n)$ pro nekonečně mnoho různých $n$.

*Důkaz:* Uvažuj dokonale vyvážený BVS s klíči $1, \dots, n$, $n = 2^k - 1$. Tvar je jednoznačně určen (kořen je medián, …, všechna lichá čísla v listech). Po posloupnosti `Insert(n+1), Delete(1), Insert(n+2), Delete(2), …` strom alternuje: $i$-tá dvojice obsahuje hodnoty $i+1, \dots, i+n$, ve které jsou v listech buď všechna sudá nebo všechna lichá čísla. Pokaždé je tedy nutno **změnit označení u všech $\Omega(n)$ vrcholů**, zda jsou listy → aspoň jedna z operací trvá $\Omega(n)$. $\square$

### 3.6 [[AVL-strom|AVL stromy]]: hloubkové vyvážení
Kritérium dokonalého vyvážení je příliš striktní. Stačí udržovat hloubku $O(\log n)$:

**Definice:** BVS je **hloubkově vyvážený**, pokud pro každý vrchol $v$ platí
$$|h(L(v)) - h(R(v))| \le 1.$$

Pro každý vrchol definujeme **znaménko**
$$\delta(v) = h(R(v)) - h(L(v)) \in \{-1, 0, +1\}.$$
(Při porušení vyváženosti bude přechodně $\delta(v) = \pm 2$.)

**Věta:** Hloubkově vyvážený strom s $n$ vrcholy má hloubku $\Theta(\log n)$.

*Důkaz:* Označ $A_h$ minimální počet vrcholů HV stromu hloubky $h$. Pak $A_1 = 1$, $A_2 = 2$, $A_3 = 4$, …, a obecně $A_{h+1} = A_h + A_{h-1} + 1$ (kořen + dva minimální podstromy hloubky $h$ a $h-1$).

Indukcí dokážeme $A_{h+1} \ge 2^{h/2}$ (Fibonacciho posloupnost roste exponenciálně):
$$A_{h+1} = 1 + A_h + A_{h-1} > 2^{h/2} + 2^{(h-1)/2} = 2^{h/2}\left(\tfrac{1}{2} + \tfrac{1}{\sqrt 2}\right) > 2^{h/2}.$$

Tedy HV strom hloubky $h+1$ má aspoň $\sqrt{2}^h$ vrcholů, takže strom o $n$ vrcholech má hloubku $\le \log_{\sqrt 2}(n) + 1 = \Theta(\log n)$. $\square$

### 3.7 [[Rotace-v-BVS|Rotace]]
**Jednoduchá rotace doprava (R)** kolem hrany $\{x, y\}$, kde $y = \ell(x)$:
```
        x                y
       / \              / \
      y   C    →       A   x
     / \                  / \
    A   B                B   C
```
**Jednoduchá rotace doleva (L)** je zrcadlová symetrie ($y = r(x)$).

**Pozorování:** Rotace **zachovává BVS-uspořádání** (InOrder výpis se nemění), ale **mění hloubky podstromů**.

```
Algoritmus rotateLeft(x)
(1) y := r(x); r(x) := ℓ(y); ℓ(y) := x
(2) Přepoj ukazatele otce: p(r(x)) := x; p(y) := p(x); p(x) := y
(3) Přepočítej výšky h(T(x)), h(T(y))
```

**Pozorování:** Jednoduchá rotace **nestačí** v situacích cik-cak (zalomené porušení). Pak je nutná **dvojitá rotace** — sekvence dvou jednoduchých:
- **LR rotace**: nejprve L na $\{y, z\}$, pak R na $\{x, y\}$ (pro porušení tvaru „doleva—doprava").
- **RL rotace** symetricky.

### 3.8 `AVLInsert`
Vloží nový list standardně (`BVSInsert`, znaménko $\delta = 0$). Při návratu z rekurze propaguje **informaci, že se zvětšila hloubka podstromu**, a v každém vrcholu rozhoduje podle jeho znaménka:

Případ 1) Vrchol $x$ měl $\delta = +1$ (z protilehlého syna). Po prohloubení levého syna: $\delta \to 0$. Hloubka $T(x)$ se **nezměnila** → propagaci **zastavíme**.

Případ 2) Vrchol $x$ měl $\delta = 0$. Pak $\delta \to -1$ (pokud přišlo zleva). Hloubka $T(x)$ vzrostla o 1 → **pokračujeme**.

Případ 3) Vrchol $x$ měl $\delta = -1$, takže by se stalo $\delta = -2$. Je potřeba **vyvážit**. Označme $y = \ell(x)$, z něj přišla informace:
- 3a) $\delta(y) = -1$: jednoduchá rotace R kolem $\{x, y\}$ → $\delta(x) = \delta(y) = 0$, hloubka $T(x)$ se po opravě nezměnila ⟹ propagaci zastavíme.
- 3b) $\delta(y) = +1$: dvojitá rotace LR (nejprve L na $\{y, z\}$ pro $z = r(y)$, pak R na $\{x, y\}$). Hloubka $T(x)$ se po opravě nezměnila ⟹ zastavíme.
- 3c) $\delta(y) = 0$ nemůže nastat — nově přidaný list má znaménko 0 a informace o prohloubení se ze znaménka 0 nešíří dál.

V `AVLInsert` stačí **jedna** (jednoduchá nebo dvojitá) rotace na celý strom.

### 3.9 `AVLDelete`
Vyjme vrchol standardně (`BVSDelete`) a po cestě zpět propaguje **informaci o snížení hloubky**. Analogicky 3 případy podle znaménka vrcholu $x$:
- $\delta(x) = -1$: po snížení hloubky levého syna $\delta \to 0$, hloubka klesla → pokračujeme.
- $\delta(x) = 0$: $\delta \to +1$, hloubka nezměnila → zastavíme.
- $\delta(x) = +1$: $\delta \to +2$, vyvažujeme:
  - 3a) $\delta(y) = +1$: rotace L, $\delta = 0$, hloubka klesla → **pokračujeme**.
  - 3b) $\delta(y) = 0$: rotace L, $\delta(x) = +1$, $\delta(y) = -1$, hloubka **nezměnila** → zastavíme.
  - 3c) $\delta(y) = -1$: dvojitá rotace RL, hloubka klesla → pokračujeme.

**Pozor:** v `AVLDelete` může být potřeba **až $O(\log n)$ rotací** po cestě ke kořeni.

### 3.10 Složitost AVL operací
**Tvrzení:** `AVLInsert`, `AVLDelete`, `AVLFind` mají složitost $O(\log n)$.

*Důkaz:* Hloubka AVL stromu je vždy $\Theta(\log n)$. Operace `BVSFind`, `BVSInsert`, `BVSDelete` jsou tedy $O(\log n)$. Při vyvažování provedeme na každé hladině $\Theta(1)$ operací, celkem také $\Theta(\log n)$. $\square$

### 3.11 Další vyvážené BVS (přehled)
- **Červeno-černé stromy:** každý vrchol má barvu R/B, kořen + listy černé, žádné dva R za sebou, na všech cestách stejný počet B.
- **AA stromy, splay stromy, B-stromy, $B^+$ stromy** — varianty s různými kompromisy mezi hloubkou, počtem rotací a uložením.

---

## 4. Hešovací tabulky

### 4.1 [[Slovník|Slovník]]
**Slovník** (tabulka, mapa, asociativní pole) je datová struktura pro reprezentaci dynamické podmnožiny prvků s klíči $K \subseteq \mathcal{U}$ ($|K| \ll |\mathcal{U}|$). Operace:
- `Find(k)`,
- `Insert(x)`,
- `Delete(x)`.

**Implementace:**
- Bitové pole / přímé adresování — $O(1)$, ale $\Theta(|\mathcal{U}|)$ paměti.
- Seřazené pole — hledání $O(\log n)$, vkládání/mazání $O(n)$.
- Vyvážený [[BVS]] — $O(\log n)$.
- **[[Hešovací-tabulka]]** — $O(1)$ amortizovaně v průměrném případě.

### 4.2 Hešovací tabulka
Zvolíme konečné pole **přihrádek** $\mathcal{P} = \{0, \dots, m-1\}$ a **hešovací funkci** $h: \mathcal{U} \to \mathcal{P}$. Prvek s klíčem $k$ ukládáme do přihrádky $h(k)$.

Protože $m \ll |\mathcal{U}|$, vzniká **kolize** — více prvků padne do stejné přihrádky.

**Faktor naplnění:** $\alpha = n/m$.

### 4.3 Ideální hešovací funkce
- Vypočte $h(k)$ v čase $O(1)$ a neukládá data do paměti.
- Rozděluje univerzum **rovnoměrně**: $\forall i \ne j: ||h^{-1}(i)| - |h^{-1}(j)|| \le 1$.

**Fakt (neformální):** Při ideální funkci a rovnoměrně náhodných vstupních datech mají téměř všechny přihrádky $O(n/m)$ prvků a všechny operace jsou v průměru $O(n/m)$.

### 4.4 Příklady prakticky používaných hešovacích funkcí
- **Lineární kongruence:** $h(k) = ak \bmod m$, $m$ prvočíslo, $a$ nesoudělné (často $a \approx 0{,}618 \cdot m$).
- **Vyšší bity součinu** (pro $m = 2^\ell$): $h(k) = \lfloor (ak \bmod 2^w) / 2^{w-\ell} \rfloor$, $a$ lichá $w$-bitová konstanta.
- **Skalární součin** (pro posloupnosti $k_0, \dots, k_{d-1}$): $\left(\sum_{i=0}^{d-1} a_i k_i\right) \bmod m$.
- **Polynom:** $\left(\sum_{i=0}^{d-1} a^i k_i\right) \bmod m$ pro jednu konstantu $a$.

### 4.5 Nafukovací hešovací tabulka
Pokud faktor naplnění překročí konstantu $Z$ (např. $Z = 1$):
1. Zdvojnásob $m$.
2. Zvol novou hešovací funkci.
3. Všechny prvky **přehešuj** do nové tabulky.

Analogicky [[Nafukovací-pole|nafukovacímu poli]] je amortizovaná složitost vkládání $\Theta^*(1)$.

### 4.6 Řešení kolizí I: [[Hešování-s-řetízky|Hešování s řetízky]] (Chaining)
Tabulka je pole $m$ přihrádek, každá obsahuje **ukazatel na spojový seznam** (řetízek) prvků hešovaných do dané přihrádky.

**Operace:** Spočti $h(k)$, projdi řetízek.

**Složitost:**
- Při ideální hešovací funkci a rovnoměrně náhodných datech mají skoro všechny řetízky délku $O(n/m)$.
- Volbou $m = \Theta(n)$ dostaneme **konstantní** průměrnou složitost všech operací.

**Výhody:** mazání je triviální, faktor naplnění může být i $> 1$.

### 4.7 Řešení kolizí II: [[Otevřená-adresace|Otevřená adresace]] (Open addressing)
V tabulce $A[0], \dots, A[m-1]$ je v každé přihrádce **přímo jeden prvek** (nebo prázdná / náhrobek). Pro každý klíč $k$ máme **vyhledávací posloupnost**
$$h(k, 0), h(k, 1), \dots, h(k, m-1),$$
která je ideálně permutací $\{0, \dots, m-1\}$.

Vždy musí být $\alpha = n/m < 1$.

#### `OpenFind`
```
OpenFind(k)
(1) Pro i = 0, …, m-1:
(2)     j := h(k, i)
(3)     Pokud k(A[j]) = k: ohlas nalezení, skonči
(4)     Pokud A[j] je prázdná: ohlas neúspěch, skonči
(5) Ohlas neúspěch
```

#### Mazání — náhrobky
Pokud bychom přihrádku po smazaném prvku **prohlásili za prázdnou**, narušíme vyhledávací posloupnost pro pozdější klíče. Proto smazaný prvek označíme **náhrobkem** $\dagger$, který se chová:
- jako obsazená přihrádka při `OpenFind`,
- jako volná při `OpenInsert`.

Když počet náhrobků překročí mez ($\sim m/4$), tabulka se **přehešuje**.

```
OpenInsert(x)
(1) Pokud OpenFind(k(x)) najde k(x): skonči
(2) Pro i = 0, …, m-1:
(3)     j := h(k(x), i)
(4)     Pokud A[j] je prázdná nebo náhrobek:
(5)         A[j] := x; skonči
(6) Ohlas zaplnění tabulky
```

```
OpenDelete(x)
(1) Pro i = 0, …, m-1:
(2)     j := h(k(x), i)
(3)     Pokud A[j] = x: A[j] := †; skonči
(4)     Pokud A[j] je prázdná: skonči
```

### 4.8 Volba vyhledávací posloupnosti
- **Lineární přidávání** (Linear Probing): $h(k, i) = (f(k) + i) \bmod m$.
  - Výhoda: sekvenční přístup do paměti (cache-friendly).
  - Nevýhoda: vznikají **shluky** (clustery) obsazených přihrádek.
  - Pro dokonale náhodnou $f$ je střední počet probů při neúspěšném hledání $1/(1-\alpha)^2$ (bez důkazu).
- **Lineární přidávání s krokem $c$:** $h(k, i) = (f(k) + c \cdot i) \bmod m$, $c$ nesoudělné s $m$.
- **Dvojité hešování** (Double Hashing): $h(k, i) = (f(k) + i \cdot g(k)) \bmod m$, $g(k) \in \{1, \dots, m-1\}$, $m$ prvočíslo. Pro náhodné $f, g$ se chová **stejně dobře jako plně náhodné posloupnosti**.

### 4.9 Efektivita otevřené adresace
**Věta (o efektivitě otevřené adresace):** Pokud jsou vyhledávací posloupnosti náhodné permutace $\{0, \dots, m-1\}$, pak neúspěšné hledání navštíví ve střední hodnotě **nejvýše $1/(1-\alpha)$** přihrádek, kde $\alpha = n/m$.

*Důkaz (skica):* Označ $p_i$ pravděpodobnost, že hledání projde alespoň $i$ přihrádek (tedy přihrádky $h_1, \dots, h_{i-1}$ jsou obsazené). Indukcí:
$$p_{i+1} = p_i \cdot \frac{n - (i-1)}{m - (i-1)} \le p_i \cdot \frac{n}{m} = p_i \cdot \alpha,$$
tedy $p_{i+1} \le \alpha^i$. Označ $q_i$ pravděpodobnost navštívit **právě** $i$ přihrádek. Pro střední hodnotu $S = \sum_{i=1}^m i \cdot q_i$ platí $S = \sum_{i=1}^m p_i$ (přerovnání teleskopické sumy):
$$S = \sum_{i=1}^m p_i \le \sum_{i=1}^m \alpha^{i-1} < \sum_{i=0}^\infty \alpha^i = \frac{1}{1-\alpha}. \square$$

**Důsledek:** Pro $\alpha \le 0{,}5$ je střední počet probů $\le 2$, pro $\alpha = 0{,}9$ je $\le 10$.

### 4.10 Randomizace — vsuvka
**Diskrétní pravděpodobnostní prostor** $(\Omega, \mathbf{P})$: $\Omega$ konečná/spočetná množina elementárních jevů, $\mathbf{P}: \Omega \to [0,1]$ s $\sum_{\omega \in \Omega} \mathbf{P}(\omega) = 1$.

**Náhodná veličina:** $X: \Omega \to \mathbb{R}$.

**Střední hodnota:** $\mathbf{E}[X] = \sum_{\omega \in \Omega} X(\omega) \mathbf{P}(\omega)$.

**Linearita střední hodnoty:** $\mathbf{E}[\alpha X + \beta Y] = \alpha \mathbf{E}[X] + \beta \mathbf{E}[Y]$ (platí i pro závislé $X, Y$).

**Věta o opakování nezávislých pokusů:** Pravděpodobnost jevu $J$ v jednom pokusu je $p$. Pak střední doba čekání na první výskyt $J$ je $1/p$.

**Aplikace — kontrola násobení matic (Freivalds):** Pro $A, B, C \in \mathbb{Q}^{n \times n}$ chceme ověřit $C = AB$. Algoritmus `VerifyMM`: zvol náhodný vektor $x \in \{0,1\}^n$, spočti $y = A(Bx)$ a $z = Cx$; ohlaš $C = AB$ pokud $y = z$, jinak $C \ne AB$.
- Pokud $C = AB$, algoritmus odpoví správně **vždy**.
- Pokud $C \ne AB$, odpoví správně s pravděpodobností $\ge 1/2$.
- Časová složitost: $O(n^2)$ (dvě maticově-vektorová násobení).
- Opakováním 50× se chyba sníží pod $2^{-50} < 10^{-15}$.

---

## 5. Co je potřeba na zkoušku znát

### Definice
- Binární halda (tvar + haldové uspořádání); reprezentace v poli.
- Binomiální strom $B_k$ (rekurzivně); binomiální halda (uspořádaná množina, nejvýše jeden strom každého řádu, haldové uspořádání).
- Binární vyhledávací strom.
- Dokonale vyvážený BVS, hloubkově vyvážený BVS, AVL strom, znaménko vrcholu.
- Slovník (`Find`, `Insert`, `Delete`).
- Hešovací funkce, hešovací tabulka, kolize, faktor naplnění.
- Vyhledávací posloupnost při otevřené adresaci, náhrobek.
- Amortizovaná složitost.

### Věty s důkazy
- Počet hladin binární haldy = $\lfloor \log n \rfloor + 1$.
- `HeapBuild` v čase $O(n)$ (s d'Alembertovým kritériem).
- Strom $B_i$ je v $n$-prvkové BH ⟺ $i$-tý bit $n$ je 1; důsledek $O(\log n)$ stromů.
- Vlastnosti $B_k$: $2^k$ vrcholů, $k+1$ hladin, stupeň kořene $k$, hladina $i$ má $\binom{k}{i}$ vrcholů.
- Amortizovaná složitost `Inc` u binární sčítačky $= O^*(1)$ (bankéřova metoda) → `BHInsert` amortizovaně $\Theta^*(1)$.
- Amortizovaná složitost `NPInsert` $= \Theta^*(1)$.
- Hloubka AVL stromu $= \Theta(\log n)$ (Fibonacciho rekurence).
- Věta o nepoužitelnosti dokonalého vyvážení: aspoň jedna z `BVSInsert`, `BVSDelete` $= \Omega(n)$.
- Efektivita otevřené adresace: $\le 1/(1-\alpha)$ probů.

### Algoritmy (pseudokód + složitost)
- `HeapInsert`, `HeapExtractMin`, `HeapBuild`, `HeapSort`.
- `BHMergeTree`, `BHMerge`, `BHInsert`, `BHExtractMin`.
- `BVSFind`, `BVSInsert`, `BVSDelete`.
- `rotateLeft` / `rotateRight`, dvojitá LR/RL rotace.
- `AVLInsert` (3 případy podle znaménka), `AVLDelete` (3 případy s pokračováním).
- `OpenFind`, `OpenInsert`, `OpenDelete`.

### Datové struktury
- Binární halda (operace `Insert`, `FindMin`, `ExtractMin`, `Build`, $O(\log n)$ / $O(1)$ / $O(n)$).
- Binomiální halda (operace + `Merge` v $O(\log n)$, amortizovaný `Insert` $\Theta^*(1)$).
- AVL strom (všechny operace v $O(\log n)$, max. 1 rotace při `Insert`, $O(\log n)$ rotací při `Delete`).
- Hešovací tabulka s řetízky (průměrně $O(1)$) a s otevřenou adresací (linear/double probing).
- Nafukovací pole, binární sčítačka (jako amortizovaná zázemí).
