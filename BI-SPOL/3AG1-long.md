---
tags: [otázka, kurz/AG1, otázka/3, hotovo]
---

# Základy teorie grafů a grafové algoritmy

> **Otázka SZZ:** Základní pojmy teorie grafů. Grafové algoritmy: procházení grafu do šířky, určení souvislých komponent, topologické uspořádání, vzdálenosti v grafech, konstrukce minimální kostry a nejkratších cest v ohodnoceném grafu.

Zdroje: BI-AG1 přednášky 1, 2, 3, 11, 12 (Knop, Opler, Valla, FIT ČVUT).

---

## 1. Základní pojmy teorie grafů

### 1.1 Neorientovaný graf
**[[Graf|Neorientovaný graf]]** je uspořádaná dvojice $G = (V, E)$, kde
- $V$ je neprázdná konečná množina **vrcholů**,
- $E$ je množina **hran**; hrana je dvouprvková podmnožina $V$, značíme $\{u, v\}$.

Značení: $V(G)$, $E(G)$, $n = |V(G)|$, $m = |E(G)|$. Množinu všech možných hran značíme $\binom{V}{2}$.

Pokud $e = \{u, v\} \in E$, pak $u, v$ jsou **koncové vrcholy** hrany $e$, $u$ je **sousedem** $v$ a $u, v$ jsou **incidentní** s $e$.

### 1.2 Orientovaný graf
**[[Orientovaný-graf|Orientovaný graf]]** $G = (V, E)$, kde $E$ je množina **orientovaných hran** — uspořádaných dvojic $(u, v)$. Říkáme, že $u$ je předchůdce $v$ a $v$ je následník $u$. Orientovaná hrana $(u, u)$ je **smyčka**.

### 1.3 Sled, cesta, vzdálenost
- **[[Sled]]** délky $k$: sekvence $v_0, e_1, v_1, e_2, \dots, e_k, v_k$ taková, že $e_i = \{v_{i-1}, v_i\} \in E$.
- **[[Cesta]]**: sled, ve kterém se neopakují vrcholy (a tedy ani hrany).
- **$s$-$t$-cesta**: cesta s počátečním vrcholem $s$ a koncovým $t$ (povolujeme $s=t$, pak má cesta nulovou délku).
- **Délka cesty** = počet hran v ní.
- **[[Vzdálenost]]** $d(s,t)$ = délka nejkratší $s$-$t$-cesty (nebo $+\infty$, neexistuje-li).

### 1.4 Důležité třídy grafů
- **Úplný graf $K_n$ ([[Klika|klika]]):** graf na $n$ vrcholech, kde $E = \binom{V}{2}$.
- **Úplný bipartitní graf $K_{n_1, n_2}$:** vrcholy rozdělené do partit $A, B$ velikostí $n_1, n_2$; hrany jdou mezi všemi dvojicemi z $A \times B$ ($|E| = n_1 \cdot n_2$).
- **Cesta $P_n$:** graf $(\{1,\dots,n\}, \{\{i,i+1\}\})$.
- **Kružnice $C_n$:** $P_n$ doplněná o hranu $\{n, 1\}$, $n \ge 3$.
- **Doplněk $\overline{G}$ grafu $G = (V, E)$:** $(V, \binom{V}{2} \setminus E)$.

### 1.5 Stupně vrcholů
- $\deg_G(v)$ = **[[Stupeň-vrcholu|stupeň]]** vrcholu $v$ = počet hran obsahujících $v$.
- $N_G(v)$ = **(otevřené) okolí** $v$ = množina jeho sousedů.
- $N_G[v] = N_G(v) \cup \{v\}$ = **uzavřené okolí**.
- $r$-**regulární** graf: každý vrchol má stupeň $r$.
- **Izolovaný vrchol:** vrchol stupně 0.

**Věta ([[Princip-sudosti|princip sudosti]]):** $\displaystyle\sum_{v \in V} \deg_G(v) = 2|E|$.

**Důsledky:** V každém grafu je počet vrcholů lichého stupně sudý. Každý regulární graf lichého stupně má sudý počet vrcholů.

### 1.6 Podgraf, indukovaný podgraf, klika
- **[[Podgraf]]** $H$ grafu $G$: $V(H) \subseteq V(G)$ a $E(H) \subseteq E(G)$.
- **[[Podgraf|Indukovaný podgraf]]** $G[V']$: $V(H) = V' \subseteq V(G)$ a $E(H) = E(G) \cap \binom{V'}{2}$.
- **[[Klika]]** v $G$: podmnožina vrcholů, z nichž každé dva jsou sousední.

### 1.7 Izomorfismus
**Izomorfismus** $f: V(G) \to V(H)$: bijekce taková, že $\{u, v\} \in E(G) \iff \{f(u), f(v)\} \in E(H)$. Grafy jsou pak **izomorfní** ($G \simeq H$). Obecný problém izomorfismu je výpočetně obtížný.

**Automorfismus** = izomorfismus s grafem samotným; ukazuje symetrii grafu.

### 1.8 Stromy a lesy
- **[[Strom]]:** souvislý graf bez kružnic (acyklický).
- **[[Les]]:** graf bez kružnic.
- **[[List]]:** vrchol stupně 1.

**Věta (o existenci listů):** Každý strom s alespoň 2 vrcholy obsahuje alespoň 2 listy.

**Věta (o trhání listů):** $G$ je strom $\iff$ $G - v$ je strom (pro list $v$).

**Věta (charakterizace stromů).** Pro graf $G = (V, E)$ jsou ekvivalentní:
1. $G$ je strom.
2. Pro každé dva vrcholy $u, v \in V$ existuje právě jedna $u$-$v$-cesta.
3. $G$ je souvislý a vynecháním libovolné hrany vznikne nesouvislý graf.
4. $G$ je souvislý a $|E| = |V| - 1$.

### 1.9 Reprezentace v paměti
- **[[Matice-sousednosti|Matice sousednosti]]** $A_G$: čtvercová matice $n \times n$, $a_{ij} = 1$ pokud $\{v_i, v_j\} \in E$, jinak 0. Paměť: $O(n^2)$.
- **[[Seznam-sousedů|Seznam sousedů]]** (resp. následníků): pro každý vrchol uchováváme seznam jeho sousedů. Paměť: $O(n + m)$.

---

## 2. Procházení grafu do šířky ([[BFS]])

### 2.1 Specifikace
**Vstup:** Neorientovaný graf $G = (V, E)$ a vrchol $s \in V$.

**Výstup:**
- Pole vzdáleností $D[v] = d(s, v)$, resp. `undef`, pokud $v$ není ze $s$ dosažitelný.
- Pole předchůdců $P[v]$ = vrchol před $v$ na nějaké nejkratší $s$-$v$-cestě.

### 2.2 Algoritmus

```
Algoritmus BFS(graf G, vrchol s):
(1)  Pro každý vrchol v ∈ V(G):
(2)      stav[v] := nenalezený
(3)      D[v] := P[v] := undef
(4)  Q := fronta obsahující jediný vrchol s
(5)  stav[s] := otevřený
(6)  D[s] := 0, P[s] := ⊥
(7)  Dokud je fronta Q neprázdná:
(8)      Odeber z Q první vrchol, nechť to je v
(9)      Pro všechny sousedy w vrcholu v:
(10)         Pokud stav[w] = nenalezený:
(11)             stav[w] := otevřený
(12)             D[w] := D[v] + 1
(13)             P[w] := v
(14)             Přidej w na konec fronty Q
(15)     stav[v] := uzavřený
(16) Vrať (D, P)
```

### 2.3 BFS hladiny
- **Hladina $H_0 = \{s\}$.**
- Fáze $F_0$ = otevření všech sousedů $s$.
- **Hladina $H_i$** = množina všech vrcholů otevřených a vložených do $Q$ ve fázi $F_{i-1}$.
- Vrcholy v $H_i$ jsou přesně ty s $D[v] = i$ — leží ve vzdálenosti $i$ od $s$.

### 2.4 Správnost (3 vlastnosti)
1. Po skončení jsou uzavřené přesně vrcholy dosažitelné ze $s$.
2. Pro každý uzavřený vrchol platí $D[v] = d(s, v)$.
3. $P[v] = w$, kde $w$ je předchůdce $v$ na nějaké nejkratší $s$-$v$-cestě.

**Klíčový argument (vlastnost 2):** Indukcí podle hladin. Kdyby existovala cesta $P$ z $s$ do $v$ délky $j < i$ (kde $v \in H_i$), pak by podle holubníkového principu na $P$ existovaly dva sousední vrcholy ve dvou nesousedních hladinách — to není možné, protože dva sousední vrcholy na cestě musí ležet ve dvou sousedních hladinách.

### 2.5 Časová složitost
**Věta:** BFS při reprezentaci grafu seznamem sousedů má časovou složitost $O(|V| + |E|)$.

Každý vrchol je vložen do $Q$ nejvýše jednou; vnější cyklus má $\le |V|$ iterací; každou hranu projdeme nejvýše dvakrát (z obou stran).

---

## 3. Určení souvislých komponent

### 3.1 Souvislost
**Graf $G$ je [[Souvislost|souvislý]]**, jestliže pro každé dva jeho vrcholy $u, v$ existuje $u$-$v$-cesta. Jinak je **nesouvislý**.

### 3.2 Souvislá komponenta
**Indukovaný podgraf $H$ grafu $G$ je [[Souvislá-komponenta|souvislou komponentou]]**, pokud
- je souvislý a
- neexistuje žádný souvislý podgraf $F \neq H$ takový, že $H \subseteq F$.

(Tedy komponenta je v inkluzi maximální souvislý podgraf.)

**Pozorování:** $G$ je souvislý $\iff$ obsahuje jedinou souvislou komponentu.

**Tvrzení:** Binární relace $u \leftrightsquigarrow v \iff \exists\, u\text{-}v\text{-cesta}$ je ekvivalence; její třídy indukují souvislé komponenty.

### 3.3 Algoritmus BFS_graf
Spustíme BFS opakovaně z každého dosud nenalezeného vrcholu — každý běh BFS najde jednu souvislou komponentu.

```
Algoritmus BFS_graf (graf G):
(1)  Pro každý vrchol u ∈ V(G):
(2)      stav[u] := nenalezený
(3)      D[u] := P[u] := undef
(4)  Pro každý vrchol s ∈ V(G):
(5)      Pokud stav[s] = nenalezený:
(6)          BFS(G, s)
(7)  Vrať (D, P)
```

**Časová složitost:** $O(|V| + |E|)$ — každý vrchol vyjmeme z globálního seznamu nejvýše jednou; přes všechny komponenty dohromady projdeme každou hranu nejvýše dvakrát.

**Alternativa:** DFS_graf (procházení do hloubky), rekurzivně.

### 3.4 Slabá a silná souvislost (orientované grafy)
- **Symetrizace $\text{sym}(G)$** orientovaného grafu = neorientovaný graf, kde $\{u,v\}$ je hrana $\iff (u,v) \in E$ nebo $(v,u) \in E$.
- **Slabě souvislý** orientovaný graf: $\text{sym}(G)$ je souvislý.
- **Silně souvislý** orientovaný graf: pro každé dva vrcholy $u, v$ existuje orientovaná cesta z $u$ do $v$ **a současně** z $v$ do $u$.

Slabou souvislost testujeme BFS na symetrizaci. Silnou lze naivně řešit spuštěním BFS z každého vrcholu; efektivnější algoritmy v BI-AG2.

---

## 4. Topologické uspořádání

### 4.1 Motivace: nástroj `make`
Závislosti mezi moduly tvoří orientovaný graf — chceme moduly seřadit tak, aby závislosti šly „zleva doprava".

### 4.2 Definice
**[[Topologické-uspořádání|Topologické uspořádání]] (TU)** orientovaného grafu $G = (V, E)$ je takové seřazení vrcholů $v_1, \dots, v_n$, že pro každou orientovanou hranu $(v_i, v_j) \in E$ platí $i < j$.

**Pozorování:** Pokud graf obsahuje **cyklus** (orientovanou kružnici), nelze topologicky uspořádat.

**Definice ([[DAG]]):** Orientovaný graf je **acyklický** (Directed Acyclic Graph), pokud neobsahuje orientovanou kružnici jako podgraf.

### 4.3 Zdroj a stok
- **Zdroj:** vrchol bez vstupních hran.
- **Stok:** vrchol bez výstupních hran.

**Věta (o existenci zdroje a stoku):** Každý orientovaný acyklický graf obsahuje alespoň jeden zdroj a alespoň jeden stok.

*Důkaz sporem:* Kdyby neexistoval zdroj, do každého vrcholu by vedla nějaká hrana → procházíme zpět $v_1 \leftarrow v_2 \leftarrow v_3 \leftarrow \dots$ a po $n$ krocích se musí nějaký vrchol zopakovat → cyklus, spor.

### 4.4 Algoritmus TopSort

```
Algoritmus TopSort(orientovaný G):
(1)  Q := prázdná fronta
(2)  δ[] := pole vstupních stupňů vrcholů G, vynulované
(3)  Pro každou hranu (u, v) ∈ E(G):
(4)      δ[v]++
(5)  Vlož do Q všechny vrcholy z s δ[z] = 0       // zdroje
(6)  Dokud Q není prázdná:
(7)      Odeber prvek z ze začátku fronty Q
(8)      Vypiš z
(9)      Pro každou hranu (z, w) vedoucí ze z:
(10)         δ[w]--
(11)         Pokud δ[w] = 0: zařaď w do Q
(12) Pokud nebyly zpracovány všechny vrcholy:
(13)     graf G obsahuje orientovaný cyklus
```

**Idea:** Průběžně počítej vstupní stupně, zdroje zařazuj do fronty, vyjímej z fronty a snižuj vstupní stupně následníků; když i ten klesne na 0, zařaď.

### 4.5 Správnost a složitost
**Věta:** [[TopSort]] buď vrátí korektní TU acyklického grafu, nebo detekuje cyklus.

**Věta:** Časová i paměťová složitost je $O(|V| + |E|)$ při reprezentaci polem následníků.

---

## 5. Vzdálenosti v grafech

### 5.1 Neohodnocené grafy
Vzdálenost = délka nejkratší cesty (počet hran). Hledáme algoritmem **BFS** v čase $O(|V| + |E|)$.

### 5.2 Hranově ohodnocené grafy
- **Váhová funkce** $w: E \to \mathbb{R}$ (přednáška o kostře) nebo **délka** $\ell: E \to \mathbb{R}$ (přednáška o cestách).
- **Délka cesty** = součet délek jejích hran.
- **Vzdálenost $d(u, v)$** v ohodnoceném grafu = minimum z délek všech $u$-$v$-cest (nebo $+\infty$).

### 5.3 Vlastnosti vzdáleností
**Lemma (o zjednodušování sledů):** Pokud jsou délky hran kladné, pak pro každý $u$-$v$-sled existuje $u$-$v$-cesta stejné nebo menší délky.

**Důsledek (trojúhelníková nerovnost):** Pro kladné délky platí $d(u, v) \le d(u, w) + d(w, v)$.

**Důsledek:** Je-li $P$ nejkratší $u$-$v$-cesta a $w \in P$, pak její podčást $P_{uw}$ je nejkratší $u$-$w$-cesta.

### 5.4 Záporné délky
- Při **záporném cyklu** není nejkratší sled definován (vždy lze udělat ještě kratší).
- Bez záporných cyklů má smysl mluvit o nejkratší cestě i pro záporné hrany.
- Pro **obecná** ohodnocení (včetně záporných) je hledání nejkratší cesty **NP-těžké**.

---

## 6. Minimální kostra (MST)

### 6.1 Kostra grafu
Nechť $G = (V, E)$ je souvislý graf. Podgraf $K$ je **[[Kostra|kostrou]]** $G$, pokud $V(K) = V$ a $K$ je strom.

- Kostra má $|V| - 1$ hran (z charakterizace stromů).
- Nesouvislé grafy nemají kostru; každá souvislá komponenta kostru má.

### 6.2 Minimální kostra
Pro **hranově ohodnocený** souvislý graf $G$ s váhovou funkcí $w: E \to \mathbb{R}$ je **[[Minimální-kostra|minimální kostra]]** taková kostra, která má mezi všemi kostrami **nejmenší součet vah hran** $w(K) = \sum_{e \in K} w(e)$.

### 6.3 Najít libovolnou kostru — modifikace BFS
Hrany do předchůdců (pole $P$ z BFS) tvoří kostru. Spustíme BFS, vrátíme $\{\{P[v], v\} : v \neq s\}$. Časová složitost: $O(|V| + |E|)$.

**Věta:** Hrany do předchůdců v BFS na souvislém grafu tvoří kostru.

### 6.4 [[Jarník|Jarníkův (Primův) algoritmus]]

**Idea:** Hladově (greedy). Začneme stromem o 1 vrcholu. Opakovaně přidáme **nejlehčí hranu**, která vede mezi dosud vytvořeným stromem a zbytkem grafu.

```
Algoritmus MinKostraJarník(G = (V, E), w: E → ℝ)
(1) v₀ := libovolný vrchol grafu
(2) T := strom obsahující vrchol v₀ a žádné hrany
(3) Dokud existuje hrana {u, v} taková,
                  že u ∈ V(T) a v ∉ V(T):
(4)     Přidej nejlehčí takovou hranu spolu s v do T
(5) Vrať T
```

### 6.5 Důkaz korektnosti

**Pojem elementárního řezu:** Nechť $A \subseteq V$ a $B = V \setminus A$. **Elementární řez** určený množinami $A, B$ je množina všech hran s jedním koncem v $A$ a druhým v $B$.

**Lemma (o řezech s unikátními vahami):** Je-li $G$ souvislý ohodnocený graf s unikátními vahami, $R$ elementární řez a $e$ nejlehčí hrana v $R$, pak každá minimální kostra obsahuje $e$.

*Důkaz obměnou:* Kdyby kostra $T$ neobsahovala $e = \{a, b\}$, pak existuje cesta $P(a,b)$ v $T$ překračující $R$ v nějaké hraně $f$. Záměnou $f \to e$ dostaneme kostru $T'$ s $w(T') = w(T) - w(f) + w(e) < w(T)$ (díky unikátnosti). Tedy $T$ nebyla minimální.

**Věta:** Souvislý graf s unikátními vahami má **právě jednu** minimální kostru a Jarníkův algoritmus ji vytvoří.

**Důsledek:** Minimální kostra je jednoznačně určena uspořádáním hran podle vah, nikoli konkrétními hodnotami.

### 6.6 Implementace přes binární haldu

Vrcholy uchováváme v minimové [[Binární-halda|binární haldě]], klíčem je „vzdálenost od stromu":
- `HeapExtractMin` → vrchol $u$ s minimálním $d$, přidáme ho do $T$.
- Pro sousedy $v$ z $u$ použijeme `HeapDecreaseKey`, pokud nová hrana zlepší jejich $d$.

**Věta:** Časová složitost Jarníkova algoritmu s binární haldou je $O(|E| \log |V|)$.

*Důkaz:* $|V|$-krát `ExtractMin` = $O(|V| \log |V|)$, plus nejvýše $|E|$-krát `DecreaseKey` = $O(|E| \log |V|)$.

### 6.7 [[Kruskal|Kruskalův algoritmus]]

**Idea:** Také hladově. Seřaď hrany podle vah od nejlehčí. Procházej je v tomto pořadí; každou přidej, pokud nevytvoří cyklus (tedy její koncové vrcholy leží v různých komponentách aktuálního lesa).

```
Algoritmus MinKostraKruskal(G = (V, E), w: E → ℝ)
(1) Seřaď hrany podle vah: w(e₁) ≤ ... ≤ w(eₘ)
(2) T := (V, ∅)                  // počáteční les bez hran
(3) U := Init(V)                 // Union-Find inicializace
(4) Pro i := 1, ..., m opakuj:
(5)     označ u, v krajní vrcholy hrany eᵢ
(6)     a := Find(u);  b := Find(v)
(7)     Pokud a ≠ b:
(8)         E(T) := E(T) ∪ {eᵢ}
(9)         Union(a, b)
(10) Vrať T
```

### 6.8 Struktura [[Union-Find]]
Reprezentuje rozklad množiny $X$. Operace:
- `Init(X)` — každý prvek ve vlastní množině.
- `Find(u)` — identifikátor množiny obsahující $u$.
- `Union(u, v)` — sjednotí množiny obsahující $u$ a $v$.

**Implementace keříky:** každá množina = strom orientovaný do kořene. Při `Union` připojíme mělčí keřík pod kořen hlubšího (a hloubku případně zvedneme o 1).

**Lemma (o hloubce keříků):** Keřík s $h$ hladinami obsahuje alespoň $2^{h-1}$ vrcholů. Tedy hloubka $\le \log n$.

**Složitosti:** `Init` $O(n)$, `Find` $O(\log n)$, `Union` $O(\log n)$.

### 6.9 Časová složitost Kruskala
$$O(m \log n + T_i(n) + m \cdot T_f(n) + n \cdot T_u(n))$$
S keříky $\Rightarrow O(m \log n + n + m \log n + n \log n) = O(m \log n) = O(|E| \log |V|)$.

### 6.10 Srovnání

| Algoritmus | Idea | Struktura | Složitost |
|---|---|---|---|
| Jarník | rozšiřuj jeden strom o nejlehčí hranu na hranici | binární halda | $O(|E| \log |V|)$ |
| Kruskal | seřaď hrany, postupně přidávej nejlehčí, hlídej cykly | Union-Find s keříky | $O(|E| \log |V|)$ |

---

## 7. Nejkratší cesty v ohodnoceném grafu

### 7.1 [[Dijkstra|Dijkstrův algoritmus]]

**Vstup:** Orientovaný graf $G = (V, E)$ s **kladnými** délkami $\ell: E \to \mathbb{R}^+$ a počáteční vrchol $v_0$.

**Výstup:** Vzdálenosti $d(v_0, v)$ pro všechny $v \in V$.

**Idea:** Zobecnění BFS. Místo „vlny" v lineárním čase máme „budíky" $h(v)$ — odhad vzdálenosti. Vždy zpracujeme vrchol s nejmenším $h$ (jeho budík zazvoní jako první).

#### Stavy vrcholů: nenalezený / otevřený (má nastaveno $h$) / uzavřený (relaxován).

```
Algoritmus Dijkstra(G, ℓ: E → ℝ⁺, v₀)
(1)  Pro všechny vrcholy v:
(2)      stav(v) := nenalezený
(3)      h(v) := +∞;  P(v) := ⊥
(4)  stav(v₀) := otevřený
(5)  h(v₀) := 0
(6)  Dokud existují nějaké otevřené vrcholy:
(7)      Vyber otevřený vrchol v, jehož h(v) je nejmenší.
(8)      Pro všechny následníky w vrcholu v:        // relaxace v
(9)          Pokud h(w) > h(v) + ℓ((v, w)):
(10)             h(w) := h(v) + ℓ((v, w))
(11)             stav(w) := otevřený
(12)             P(w) := v
(13)     stav(v) := uzavřený
(14) Vrať pole vzdáleností h a pole předchůdců P
```

**Definice (relaxace vrcholu):** Přepočítání ohodnocení $h(w)$ pro všechny následníky $w$ vrcholu $v$.

### 7.2 Správnost Dijkstrova algoritmu

**Věta:** Při kladných délkách hran se Dijkstra zastaví a po skončení mají všechny dosažitelné vrcholy $h(v) = d(v_0, v)$.

Dokazuje se přes 4 vlastnosti:

- **(O) Ohodnocení:** $h(v)$ nikdy neroste; je-li konečné, je to délka nějakého $v_0$-$v$-sledu.
- **(M) Monotonie:** $h(z) \le h(o)$ pro $z$ uzavřený a $o$ otevřený. **Dijkstra nikdy neotevře již uzavřený vrchol.**
- **(D) Dosažitelnost:** Po zastavení jsou uzavřené přesně vrcholy dosažitelné z $v_0$.
- **(V) Vzdálenost:** Po zastavení je $h(w) = d(v_0, w)$ pro všechna $w$.

### 7.3 Časová složitost Dijkstry
- **Naivně** (lineární průchod otevřených vrcholů): $O(n^2)$.
- **S binární haldou:** $O(|E| \log |V|)$ — analogicky jako Jarník.

```
Algoritmus DijkstraHalda(G, ℓ: E → ℝ⁺, v₀)
(1)  Pro všechny v ∈ V:  h(v) := +∞;  P(v) := ⊥
(2)  h(v₀) := 0
(3)  H := HeapBuild(V) uspořádanou podle klíčů h
(4)  Dokud H neprázdná:
(5)      v := HeapExtractMin(H)
(6)      Pro všechny následníky w vrcholu v:
(7)          Pokud w ∈ H ∧ h(w) > h(v) + ℓ((v,w)):
(8)              P(w) := v
(9)              HeapDecreaseKey(H, w, h(v) + ℓ((v,w)))
(10) Vrať P a h
```

### 7.4 Hrany záporné délky

- Pokud existuje **záporný cyklus**, nejkratší sled není definován.
- Bez záporných cyklů má cesta smysl, ale Dijkstra **selhává** (může otevírat vrcholy opakovaně a má exponenciální složitost; vlastnost M neplatí, protože záporná hrana může „zlevnit" už uzavřený vrchol).

### 7.5 Relaxační algoritmus (obecný rámec)

Zobecnění Dijkstry: vybírej k relaxaci **libovolný** otevřený vrchol (nemusí mít nejmenší $h$).

```
Algoritmus Relaxace(G, ℓ: E → ℝ, v₀)
(7)  v := nějaký otevřený vrchol
(8)  Pro všechny následníky w vrcholu v:   // relaxace
(9)      Pokud h(w) > h(v) + ℓ((v, w)):
(10)         h(w) := h(v) + ℓ((v, w))
(11)         stav(w) := otevřený
(12)         P(w) := v
(13) stav(v) := uzavřený
```

Vlastnosti O, D, V platí pro **jakoukoli** strategii výběru otevřeného vrchol.

### 7.6 [[Bellman-Ford|Bellmanův-Fordův algoritmus]]

**Vstup:** Orientovaný graf s **libovolnými** délkami hran, **bez záporných cyklů**.

**Strategie výběru:** otevřené vrcholy ukládáme do **obyčejné fronty** (FIFO), bereme vždy nejstarší.

```
Algoritmus Bellman-Ford(G, ℓ: E → ℝ, v₀)
(1)  Pro všechny vrcholy v:
(2)      stav(v) := nenalezený;  h(v) := +∞;  P(v) := ⊥
(3)  stav(v₀) := otevřený;  h(v₀) := 0
(4)  Vlož v₀ do fronty
(5)  Dokud je fronta neprázdná:
(6)      Vyjmi první vrchol z fronty a označ ho v
(7)      Pro všechny následníky w vrcholu v:
(8)          Pokud h(w) > h(v) + ℓ((v, w)):
(9)              h(w) := h(v) + ℓ((v, w))
(10)             Pokud stav(w) ≠ otevřený:
(11)                 Přidej w do fronty
(12)             stav(w) := otevřený
(13)             P(w) := v
(14)     stav(v) := uzavřený
(15) Vrať pole vzdáleností h a pole předchůdců P
```

### 7.7 Fáze a klíčová vlastnost

**Fáze $F_i$:** $A_0 = \{v_0\}$; $A_i$ = množina vrcholů otevřených při relaxaci vrcholů z $A_{i-1}$.

**Vlastnost H:** Na konci fáze $F_i$ je $h(v) \le \ell(S)$, kde $S$ je nejkratší $v_0$-$v$-sled o **nejvýše $i$ hranách**.

**Důsledek:** Po fázi $F_{n-1}$ jsou všechna ohodnocení shora omezena délkami nejkratších cest (cesta má nejvýše $n-1$ hran). Ve fázi $F_n$ se už nic nezmění a algoritmus se zastaví.

### 7.8 Složitost
**Věta:** V grafu bez záporných cyklů najde Bellman-Ford všechny vzdálenosti z $v_0$ v čase $O(|V| \cdot |E|)$.

Jedna fáze: každý vrchol relaxován nejvýše jednou → $O(|E|)$. Fází je $|V|$.

### 7.9 SimpleBellman-Ford
Ještě jednodušší (ale neudává fáze):

```
SimpleBellman-Ford(G, ℓ, v₀)
(1)  Pro všechny vrcholy v:  h(v) := +∞;  P(v) := ⊥
(2)  h(v₀) := 0
(3)  Pro i := 1, ..., n:
(4)      Pro každou hranu (u, v) ∈ E(G):
(5)          Pokud h(v) > h(u) + ℓ((u, v)):
(6)              h(v) := h(u) + ℓ((u, v))
(7)              P(v) := u
(8)  Vrať h, P
```

Také $O(|V| \cdot |E|)$.

### 7.10 Srovnání algoritmů nejkratších cest

| Algoritmus | Předpoklady | Strategie | Složitost |
|---|---|---|---|
| **BFS** | neohodnocený graf | fronta (FIFO) | $O(|V| + |E|)$ |
| **Dijkstra** | $\ell \ge 0$ | minimová halda (min $h$) | $O(|E| \log |V|)$ |
| **Bellman-Ford** | bez záporných cyklů | obyčejná fronta | $O(|V| \cdot |E|)$ |

---

## 8. Co je potřeba na zkoušku znát

### Definice
Graf (neorientovaný, orientovaný); sled, cesta, vzdálenost; stupeň; podgraf; klika; strom, les, list; kostra; minimální kostra; topologické uspořádání; DAG; souvislost; souvislá komponenta; slabá/silná souvislost.

### Věty s důkazy
- Princip sudosti.
- Charakterizace stromů (ekvivalence 4 podmínek).
- Existence listů (a věta o trhání listů).
- Konečnost a správnost BFS (3 vlastnosti).
- Časová složitost BFS, $O(|V| + |E|)$.
- Existence zdroje a stoku v DAG.
- Správnost TopSortu.
- Lemma o řezech (jednoznačnost MST pro unikátní váhy).
- Správnost Jarníkova algoritmu, složitost s haldou.
- Správnost Kruskala přes řezy; složitost s Union-Find/keříky.
- Vlastnosti O, M, D, V Dijkstry — alespoň M a V.
- Lemma o zjednodušování sledů + trojúhelníková nerovnost.
- Konečnost a složitost Bellman-Forda.

### Algoritmy (pseudokód + složitost)
BFS, BFS_graf, TopSort, MinKostraJarník (i s haldou), MinKostraKruskal (i s Union-Find), Dijkstra (i s haldou), Bellman-Ford / SimpleBellman-Ford.

### Datové struktury
- Reprezentace grafu: matice sousednosti vs. seznam sousedů.
- Binární halda (operace `ExtractMin`, `DecreaseKey`, $O(\log n)$).
- Union-Find s keříky (operace `Init`, `Find`, `Union`).
