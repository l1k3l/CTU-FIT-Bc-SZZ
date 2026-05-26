---
tags: [otázka, kurz/AG1, otázka/4, todo]
---

# 4 — Haldy, BVS, hešování (zkrácená verze)

## 1. Binární halda

**[[Binární-halda|Binární minimová halda]]** = binární strom splňující:
1. **Tvar haldy:** všechny hladiny kromě poslední plné, poslední plněna zleva doprava.
2. **Haldové uspořádání:** $k(\text{otec}) \le k(\text{syn})$.

Počet hladin: $\lfloor \log n \rfloor + 1$. V kořeni minimum.

**Reprezentace v poli:** vrchol $i$ má syny $2i, 2i+1$, otce $\lfloor i/2 \rfloor$.

| Operace | Složitost | Idea |
|---|---|---|
| `Insert` | $O(\log n)$ | vlož na konec, `BubbleUp` |
| `FindMin` | $O(1)$ | kořen |
| `ExtractMin` | $O(\log n)$ | prohoď kořen s posledním listem, sniž $n$, `BubbleDown` |
| `HeapBuild` | $O(n)$ | `BubbleDown` od $\lfloor n/2 \rfloor$ ke kořeni |
| `HeapSort` | $O(n \log n)$ | `HeapBuild` + $n$× `ExtractMin` |

**Důkaz $O(n)$ pro `HeapBuild`:** $\sum_{j=0}^{h-1} 2^j (h-1-j) = O\left(n \sum_q q/2^q\right) = O(n)$.

## 2. Binomiální halda

**[[Binomiální-strom|$B_k$]]** rekurzivně: $B_0$ = vrchol; $B_k$ = nový kořen s syny $B_0, \dots, B_{k-1}$.

Vlastnosti $B_k$: **$2^k$ vrcholů**, $k+1$ hladin, stupeň kořene $k$, hladina $i$ má $\binom{k}{i}$ vrcholů.

**[[Binomiální-halda|BH]]** = uspořádaná množina $\mathcal{T} = T_1, \dots, T_\ell$ binomiálních stromů: vzestupně podle řádu, nejvýše jeden strom každého řádu, haldové uspořádání.

**Klíčové pozorování:** $B_i \in$ BH velikosti $n$ ⟺ $i$-tý bit $n$ je $1$. → BH má $O(\log n)$ stromů.

| Operace | Složitost |
|---|---|
| `BHFindMin` | $O(1)$ (s ukazatelem) |
| `BHMerge` | $O(\log n)$ |
| `BHInsert` | $O(\log n)$, **amort. $\Theta^*(1)$** |
| `BHExtractMin` | $O(\log n)$ |
| `BHBuild` | $O(n)$ |

**`BHMergeTree`** ($O(1)$): při slévání dvou $B_i$ připoj větší kořen pod menší → $B_{i+1}$.

**`BHMerge`** = binární sčítání: pro každý řád 0…log $n$, počet stromů ze 3 zdrojů ($A_i, B_i, carry_i$) určí výstup a carry. **Amortizovaná $\Theta^*(1)$ vkládání** plyne z amortizované analýzy [[Binární-sčítačka|binární sčítačky]] (`Inc` = $O^*(1)$ přes bankéřovu metodu — 2 mince/`Inc`, po jedné na každém jedničkovém bitu).

**`BHExtractMin`:** vyjmi minimový strom $T$, odtrhni jeho kořen → ze synů (postrom) vznikne nová BH $H'$, slij `BHMerge(H, H')`.

## 3. Binární vyhledávací stromy

**[[BVS]]:** binární strom s unikátními klíči, $\forall v$: $L(v) < k(v) < R(v)$.

**InOrder** výpis (levý—kořen—pravý) vrátí klíče vzestupně.

| Operace | Složitost |
|---|---|
| `BVSFind, BVSMin, BVSPred, BVSInsert, BVSDelete` | $O(h)$ |
| `BVSShow` | $O(n)$ |

**Hloubka** $h \in [\Omega(\log n), O(n)]$. Tvar závisí na pořadí vkládání.

**Mazání s 2 syny:** $w := \text{BVSMin}(r(u))$, přepiš $k(u) \leftarrow k(w)$, smaž $w$ (nejvýše 1 syn).

### Vyvažování

**Dokonale vyvážený BVS:** $\forall v$: $||L(v)| - |R(v)|| \le 1$, hloubka $1 + \lfloor \log n \rfloor$.

**Věta (negativní):** Udržet dokonalou vyváženost při `Insert`/`Delete` vyžaduje $\Omega(n)$ aspoň u jedné operace pro nekonečně mnoho $n$. (Alternující dvojice `Insert(i+n), Delete(i)` mění označení listů → $\Omega(n)$ změn.)

### [[AVL-strom|AVL strom]]

**Hloubkově vyvážený:** $\forall v$: $|h(L(v)) - h(R(v))| \le 1$.

**Znaménko:** $\delta(v) = h(R(v)) - h(L(v)) \in \{-1, 0, +1\}$.

**Věta:** Hloubka AVL stromu s $n$ vrcholy $= \Theta(\log n)$.

*Idea:* $A_{h+1} = A_h + A_{h-1} + 1$ (Fibonacci) ⟹ $A_h \ge (\sqrt 2)^{h-1}$ ⟹ $h \le \log_{\sqrt 2}(n) + 1$.

### [[Rotace-v-BVS|Rotace]]
- **Jednoduchá L / R** (kolem hrany $\{x, y\}$) — zachovává BVS-uspořádání, mění hloubky.
- **Dvojitá LR / RL** — sekvence dvou jednoduchých pro „cik-cak" porušení.

**`AVLInsert`:** vlož jako list ($\delta = 0$), zpětně propaguj „zvětšení hloubky". V každém vrcholu $x$ podle $\delta(x)$:
- $\delta = $ ±1 (souhlasné) → $\delta = $ 0, zastav.
- $\delta = 0$ → $\delta = \pm 1$, pokračuj.
- $\delta = $ ∓1 → $\delta = \mp 2$, vyvažuj: podle $\delta(y)$ syna jednoduchá nebo dvojitá rotace. **1 rotace stačí**, hloubka se po opravě nezmění → zastav.

**`AVLDelete`:** analogicky, propaguj „snížení hloubky". Může vyžadovat **až $O(\log n)$ rotací** po cestě ke kořeni.

**Složitost `AVLInsert`/`Delete`/`Find`:** $O(\log n)$.

## 4. Hešovací tabulky

**[[Slovník]]:** dynamická množina s `Find`, `Insert`, `Delete` nad klíči $K \subseteq \mathcal{U}$.

**[[Hešovací-tabulka]]:** pole přihrádek $\mathcal{P} = \{0, \dots, m-1\}$ + hešovací funkce $h: \mathcal{U} \to \mathcal{P}$. Prvek s klíčem $k$ ukládáme do $h(k)$.

**Faktor naplnění:** $\alpha = n/m$.

**Kolize:** $m \ll |\mathcal{U}|$ ⟹ více klíčů padne do téže přihrádky.

**Ideální hešovací funkce:** $O(1)$ výpočet, rozděluje univerzum rovnoměrně. Pak skoro všechny přihrádky mají $O(n/m)$ prvků a operace jsou $O(n/m)$ v průměru.

**Příklady:** $h(k) = ak \bmod m$ (lineární kongruence, $\gcd(a,m)=1$); skalární součin pro posloupnosti; vyšší bity součinu.

### Řešení kolizí

**[[Hešování-s-řetízky]]** (Chaining): každá přihrádka = ukazatel na spojový seznam. Mazání bezproblémové. Pro $m = \Theta(n)$ je průměrná složitost operací **konstantní**.

**[[Otevřená-adresace]]** (Open addressing): přímo jeden prvek/přihrádku; při kolizi zkus další podle **vyhledávací posloupnosti** $h(k, 0), h(k, 1), \dots$ (ideálně permutace).

| Strategie | Vzorec |
|---|---|
| Linear Probing | $h(k, i) = (f(k) + i) \bmod m$ |
| Lin. s krokem $c$ | $h(k, i) = (f(k) + c \cdot i) \bmod m$, $\gcd(c, m) = 1$ |
| Double Hashing | $h(k, i) = (f(k) + i \cdot g(k)) \bmod m$, $m$ prvočíslo |

**Mazání:** nelze označit prázdnou (přerušilo by vyhledávací posloupnosti). Označ **náhrobkem** $\dagger$: chová se jako obsazená pro `Find`, jako volná pro `Insert`. Když náhrobků $> m/4$, **přehešuj**.

**Věta (efektivita OA):** Při náhodných permutacích jako vyhledávacích posloupnostech je střední počet probů při neúspěšném hledání $\le 1/(1-\alpha)$.

*Idea:* $p_i$ = pravd. že hledání projde $\ge i$ přihrádek. $p_{i+1} \le \alpha \cdot p_i$ ⟹ $p_i \le \alpha^{i-1}$. Střední hodnota = $\sum_i p_i \le \sum_i \alpha^{i-1} < 1/(1-\alpha)$ (geometrická řada).

### Nafukovací hešovací tabulka
Když $\alpha > Z$, zdvojnásob $m$, zvol novou $h$, přehešuj. Amortizovaně $\Theta^*(1)$ (analogie [[Nafukovací-pole]]).

---

## Co odpovědět rychle

- **Binární halda:** úplný binární strom $+$ haldové uspořádání. Insert/Extract $O(\log n)$, Build $O(n)$.
- **Binomiální halda:** mergeable; `Merge` $O(\log n)$, `Insert` amort. $\Theta^*(1)$ (analogie binární sčítačky).
- **AVL strom:** hloubkově vyvážený BVS, hloubka $\Theta(\log n)$, vyvažování rotacemi; Insert v 1 rotaci, Delete až $\log n$ rotací.
- **Hešování s řetízky:** spojové seznamy, $m = \Theta(n)$ → průměrně $O(1)$.
- **Otevřená adresace:** linear / double probing, náhrobky pro mazání, věta $\le 1/(1-\alpha)$.
- **Amortizovaně:** nafukovací pole, binární sčítačka, `BHInsert`, nafukovací hešovací tabulka — všechno $\Theta^*(1)$.
