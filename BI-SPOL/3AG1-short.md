# 3 — Základy teorie grafů a grafové algoritmy (zkrácená verze)

## 1. Základní pojmy

- **Neorient. graf:** $G = (V, E)$, $E \subseteq \binom{V}{2}$. Značíme $n = |V|$, $m = |E|$.
- **Orient. graf:** $E$ obsahuje uspořádané dvojice $(u, v)$.
- **Sled** délky $k$: $v_0, e_1, v_1, \dots, e_k, v_k$, $e_i = \{v_{i-1}, v_i\}$.
- **Cesta:** sled bez opakování vrcholů.
- **Vzdálenost $d(u,v)$:** délka nejkratší $u$-$v$-cesty (nebo $+\infty$).
- **Stupeň $\deg(v)$:** počet hran obsahujících $v$. **List:** $\deg = 1$.
- **Princip sudosti:** $\sum_v \deg(v) = 2|E|$.
- **Podgraf**, **indukovaný podgraf $G[V']$**, **klika** (každé 2 vrcholy sousední).
- **Třídy:** $K_n$ (úplný), $K_{n_1, n_2}$ (úplný bipartitní), $P_n$ (cesta), $C_n$ (kružnice).
- **Strom:** souvislý a acyklický. **Les:** acyklický.

**Charakterizace stromů (ekvivalence):**
1. $G$ je strom.
2. $\forall u, v$: existuje právě jedna $u$-$v$-cesta.
3. $G$ souvislý a vynecháním libovolné hrany se rozpadne.
4. $G$ souvislý a $|E| = |V| - 1$.

**Reprezentace:** matice sousednosti $O(n^2)$, seznam sousedů $O(n+m)$.

---

## 2. BFS (procházení do šířky)

**Vstup:** $G$, vrchol $s$. **Výstup:** pole $D[v] = d(s, v)$, předchůdci $P[v]$.

**Idea:** Z $s$ šíříme „vlnu" pomocí **fronty (FIFO)**. Vrchol vyjmutý z fronty otevírá své nenalezené sousedy, nastavuje jim $D[w] = D[v] + 1$, $P[w] = v$, a přidává je do fronty.

**Hladina $H_i$** = vrcholy s $D = i$. Vrcholy v $H_i$ leží ve vzdálenosti $i$ od $s$.

**Vlastnosti:**
- Uzavřené = dosažitelné z $s$.
- $D[v] = d(s, v)$.
- $P[v]$ je předchůdce na nějaké nejkratší cestě.

**Složitost:** $O(|V| + |E|)$ při reprezentaci seznamem sousedů.

---

## 3. Souvislé komponenty

- **Souvislý graf:** $\forall u, v\ \exists\ u$-$v$-cesta.
- **Souvislá komponenta:** maximální (v inkluzi) souvislý indukovaný podgraf. Třídy ekvivalence relace „existuje cesta".
- $G$ souvislý $\iff$ má jednu komponentu.

**Algoritmus BFS_graf:** procházej vrcholy; z každého dosud nenalezeného spusť BFS. Každý běh najde jednu komponentu. Složitost $O(|V| + |E|)$.

**Orient. grafy:**
- **Slabě souvislý:** souvislá symetrizace $\text{sym}(G)$.
- **Silně souvislý:** $\forall u, v$ orient. cesta $u \to v$ i $v \to u$. (Naivně: BFS z každého vrcholu.)

---

## 4. Topologické uspořádání (TU)

**Definice:** Seřazení vrcholů $v_1, \dots, v_n$ orient. grafu tak, že $\forall (v_i, v_j) \in E: i < j$.

- **DAG** = orient. acyklický graf. **TU existuje $\iff$ graf je DAG.**
- **Zdroj** = vrchol bez vstupních hran. **Stok** = bez výstupních.
- **Věta:** Každý DAG má alespoň jeden zdroj a alespoň jeden stok.

**Algoritmus TopSort:** spočti vstupní stupně, zdroje vlož do fronty; opakovaně vyjmi vrchol, vypiš ho, sniž vstupní stupně následníkům a zařaď ty, jimž klesl na 0. Pokud na konci zbývají nezpracované vrcholy → graf obsahuje cyklus.

**Složitost:** $O(|V| + |E|)$.

---

## 5. Vzdálenosti v ohodnoceném grafu

- **Váha/délka** $\ell: E \to \mathbb{R}$, **délka cesty** = součet délek hran.
- **Vzdálenost** $d(u, v) = \min$ z délek $uv$-cest (nebo $+\infty$).

**Lemma (zjednodušování sledů):** Při kladných délkách lze každý sled zkrátit na cestu stejné nebo menší délky.

**Důsledek (trojúhelníková nerovnost):** $d(u, v) \le d(u, w) + d(w, v)$.

**Podčást nejkratší cesty je nejkratší cesta.**

**Záporné cykly** → nejkratší sled nedefinován. Hledání nejkr. cesty s obecnými vahami je NP-těžké.

---

## 6. Minimální kostra (MST)

- **Kostra** souvislého $G$: souvislý podgraf, který je stromem na $V$ (má $n - 1$ hran).
- **MST:** kostra s minimálním součtem vah.

**Elementární řez** určený $A, B = V \setminus A$ = množina hran s jedním koncem v $A$ a druhým v $B$.

**Lemma o řezech (unikátní váhy):** Nejlehčí hrana v každém elementárním řezu leží v každé MST. → Při unikátních vahách je MST jediná.

### Jarník (Prim)
**Idea:** Začni stromem o 1 vrcholu, opakovaně přidej nejlehčí hranu vedoucí ven ze stromu. Hladový algoritmus.

**Složitost:** naivně $O(|V| \cdot |E|)$; s binární haldou (klíč = váha nejlehčí hrany k vrcholu) $O(|E| \log |V|)$.

### Kruskal
**Idea:** Seřaď hrany podle vah. Procházej je od nejlehčí; přidávej, pokud koncové vrcholy leží v různých komponentách (jinak by vznikl cyklus). Komponenty udržuj ve struktuře **Union-Find**.

**Union-Find** (operace `Init`, `Find`, `Union`) — s reprezentací keříky (každý strom orient. do kořene, slučujeme připojením mělčího pod hlubší) má `Find` i `Union` v $O(\log n)$, hloubka keříku $\le \log n$.

**Složitost:** $O(|E| \log |V|)$ (dominuje řazení a $O(m)$ operací Find/Union).

---

## 7. Nejkratší cesty

| Algoritmus | Předpoklad | Výběr otev. vrcholu | Složitost |
|---|---|---|---|
| BFS | bez vah | fronta | $O(n + m)$ |
| Dijkstra | $\ell \ge 0$ | min. halda (min $h$) | $O(m \log n)$ |
| Bellman-Ford | bez záporných cyklů | obyč. fronta (FIFO) | $O(n \cdot m)$ |

(*$n = \lvert V \rvert$, $m = \lvert E \rvert$*)

### Dijkstra
**Idea:** Zobecnění BFS. Udržuj odhad $h(v)$ vzdálenosti. Opakovaně vyber otevřený vrchol s nejmenším $h$, **relaxuj** jej (pro každého následníka $w$ zkus zlepšit $h(w) := \min(h(w), h(v) + \ell(v, w))$) a uzavři.

**Klíčová vlastnost (monotonie M):** Uzavřený vrchol se už nikdy neotevře (díky kladným vahám). → Po skončení $h(v) = d(v_0, v)$.

**Implementace haldou:** klíče vrcholů v haldě = $h$; `ExtractMin` + `DecreaseKey` při relaxaci.

**Složitost:** naivně (lineární výběr minima) $O(n^2)$; s binární haldou $O(m \log n)$.

### Bellman-Ford
**Idea:** Stejný relaxační rámec, ale otevřené vrcholy v obyčejné frontě. Připouští záporné délky bez záporných cyklů.

**Fáze $F_i$:** vrcholy otevřené při relaxaci vrcholů z $F_{i-1}$.
**Vlastnost H:** Na konci fáze $F_i$ je $h(v) \le$ délka nejkratšího sledu z $v_0$ do $v$ o nejvýše $i$ hranách. Nejkratší cesta má $\le n - 1$ hran → po $n$ fázích algoritmus zastaví.

**Složitost:** $O(n \cdot m)$ ($n$ fází, každá fáze relaxuje každý vrchol nejvýše jednou → $O(m)$).

**SimpleBellman-Ford:** $n$-krát projdi všechny hrany a relaxuj. Také $O(n \cdot m)$.

---

## Co odpovědět rychle

- **BFS / souvislé komponenty:** $O(n+m)$ pomocí fronty.
- **Topologické uspořádání:** Kahnův alg. přes vstupní stupně, $O(n+m)$; detekuje cyklus.
- **MST:** Jarník ($O(m \log n)$, halda) / Kruskal ($O(m \log n)$, Union-Find s keříky).
- **Nejkratší cesty:** Dijkstra při $\ell \ge 0$ ($O(m \log n)$); Bellman-Ford pro záporné hrany bez záporných cyklů ($O(nm)$).
