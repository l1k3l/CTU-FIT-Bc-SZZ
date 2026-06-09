---
studyplan: true
etapa: "6 · ZUM — Holeňa"
qid: "21ZUM"
examiner: "Holeňa"
topic: "Stavový prostor, neinformované prohledávání (DFS, BFS), stromová expanze"
readiness: nezačato
tags: [otázka, kurz/ZUM, otázka/21, todo]
---

# Stavový prostor a neinformované prohledávání

> **Otázka SZZ:** Stavový prostor a neinformované prohledávání, stromová expanze, náhodné prohledávání, prohledávání do hloubky a do šířky.

Zdroje: BI-ZUM (FIT ČVUT), přednáška 2 — *Stavový prostor a jeho prohledávání*.

Značení: stavy $S$, akce $A$, počáteční stav $\mathcal{I}$, koncové stavy $G$, následníci $\Gamma(s)$; struktura otevřených uzlů `open`, uzavřených `closed`, tabulka předchůdců `prev`.

---

## 1. Stavový prostor

Řada problémů (navigace, logické úlohy a hry, plánování, optimalizace, symbolická integrace) se převádí na **prohledávání stavového prostoru**.

**[[Stavový-prostor|Stavový prostor]]** je [[Orientovaný-graf|orientovaný graf]] $(S, A)$, který lze prohledávat:
- **uzly reprezentují stavy** (množina $S$) — popis stavu řešeného problému,
- **hrany reprezentují akce** (množina $A \subseteq S \times S$) — umožňují přechod mezi stavy.

Úloha je zadána **počátečním stavem** $\mathcal{I} \in S$ a množinou **koncových (cílových) stavů** $G \subseteq S$. **Následníci** stavu $s$:
$$\Gamma(s) = \{\, s' \in S \mid (s, s') \in A \,\}.$$
**(Orientovaná) cesta** z $s_1$ do $s_n$ je posloupnost $(s_1, a_1, s_2, a_2, \dots, a_{n-1}, s_n)$ s $a_i = (s_i, s_{i+1})$, $s_{i+1} \in \Gamma(s_i)$.

V této přednášce hrany **nemají váhy** — řešíme úlohu **hledání cesty** z $\mathcal{I}$ do $G$ (ne hledání cílového stavu). Ohodnocené akce a cena cesty přicházejí až u [[22ZUM-long|heuristického prohledávání (ot. 22)]].

**Příklady stavových prostorů (přednáška):** navigace na mapě (stavy = obce, akce = přejezdy), hra „Lišák" / 15-puzzle, symbolická integrace (stavy = výrazy, akce = úpravy), problém $N$ dam.

---

## 2. Stromová expanze

Hledání cesty v grafu $(S,A)$ se převádí na konstrukci **prohledávacího stromu** — [[Strom|orientovaného kořenového stromu]] s kořenem $\mathcal{I}$, jehož každá cesta existuje i v grafu.

**Algoritmus (stromová expanze):**
1. Vytvoř kořen $\mathcal{I}$ (jednoprvkový strom).
2. Dokud žádný list není koncový, opakuj: vyber „nějaký" list a proveď **expanzi** — připoj všechny jeho následníky z $(S, A)$.

Funkčnost, efektivita i optimalita závisejí *jen na pravidle výběru listu*:
- volíme uzly k cíli → efektivní; volíme uzly mimo cíl → nemusí nikdy skončit; volíme uzly mimo nejkratší cestu → **suboptimální** řešení.

**Tři stavy uzlu** (zákaz duplicit ve stromě): **FRESH** (nenalezen) · **OPEN** (nalezen, neexpandován) · **CLOSED** (nalezen a expandován). Při expanzi se nepřipojují uzly už OPEN/CLOSED.

**Společné schéma algoritmů.** Liší se *pouze datovou strukturou* `open` (množina / fronta / zásobník):

```
open ← {I};  closed ← {};  prev ← init_table()
while open ≠ {} do
    x ← vyber_a_odeber(open)          # liší se podle strategie
    if x ∈ G then return reconstruct_path(prev, x)
    for all y ∈ Γ(x) do
        if y ∉ (open ∪ closed) then
            open ← open ∪ {y};  prev[y] ← x
    closed ← closed ∪ {x}
```

Cestu rekonstruujeme zpětně přes tabulku předchůdců: `x ← prev[x]` od cíle ke kořeni.

**Kritéria hodnocení strategie:** úplnost (skončí s řešením?), optimalita (nejlevnější/nejkratší?), časová a paměťová složitost (v $b$ = větvící faktor, $d$ = hloubka řešení).

---

## 3. Náhodné prohledávání (Random search)

Triviální strategie: `open` je **neuspořádaná množina**, z níž se v každém kroku vybírá k expanzi **náhodný** list.

- V praxi **nepoužitelné** — může „zabloudit" do nesmyslných oblastí prostoru, řešení nemusí být optimální.
- Použitelné jen pro zcela triviální problémy, kde nepožadujeme optimalitu.

---

## 4. Prohledávání do šířky — BFS

**[[BFS|Prohledávání do šířky]]:** `open` je **fronta (FIFO)** → strom se expanduje **systematicky po patrech** (nejprve všechny uzly hloubky $i$, pak $i+1$).

- **Úplné**; výsledná cesta má **nejmenší možný počet hran** (optimální při jednotkových cenách).
- Nároky na **paměť i čas rostou exponenciálně** s délkou nejkratší cesty k cíli ($O(b^d)$) → pro praktické úlohy AI nepoužitelné.

**Proč se v praxi nepoužívá, i když vždy najde nejkratší cestu?** Limitující je **paměť** — BFS musí současně držet v `open` celé jedno patro stromu (řádově $b^d$ uzlů). Pro větvící faktor $b = 10$ a hloubku cíle $d = 20$ je to $10^{20}$ uzlů — neuložitelné v paměti ani neprohledatelné v reálném čase. (Čas roste stejně rychle, ale binding constraint je paměť.)

BFS je speciálním případem [[Dijkstra|Dijkstrova algoritmu]] (ot. 22) pro **jednotkové ceny hran** — fronta FIFO vydává uzly přesně v pořadí rostoucí vzdálenosti (= ceny) od $\mathcal{I}$.

Pseudokód = společné schéma s `open = fronta`, `enqueue`/`dequeue`. *Příklad:* u problému $N$ dam BFS zbytečně expanduje všechny přípustné konfigurace $1, 2, \dots, N-1$ dam.

---

## 5. Prohledávání do hloubky — DFS

**[[DFS|Prohledávání do hloubky]]:** `open` je **zásobník (LIFO)** → strategie se vždy snaží o co největší **zanoření** (expanduje první nejhlubší list). Pseudokód je identický s BFS až na záměnu fronty za zásobník (`push`/`pop`).

- **Paměťově nenáročné** (efektivně drží jen aktuální větev).
- **Není optimální** — najde *nějakou*, často značně suboptimální cestu.
- Úplnost: na konečném grafu (díky `closed`) ano; na nekonečném ne.
- **Implementace:** buď **iterativně** s explicitním zásobníkem (`open = stack`, kód výše), nebo **rekurzivně** přes zásobník volání (zanoř se do prvního následníka, po návratu pokračuj dalším). Obě varianty jsou ekvivalentní.
- Vhodné, kde nelze „bloudit" a je žádoucí se rychle vzdálit počátku — např. $N$ dam: DFS rychle skládá platné konfigurace a snaží se co nejdřív umístit $N$-tou dámu.

**BFS vs. DFS:** stejný kód, jiná struktura `open`. Fronta ⇒ optimalita v počtu hran za cenu paměti; zásobník ⇒ úspora paměti za cenu optimality.

---

## Co je potřeba na zkoušku znát

### Definice
- **Stavový prostor** $(S, A)$: uzly = stavy, hrany = akce; úloha $(\mathcal{I}, G)$; následníci $\Gamma(s)$.
- **Prohledávací strom**, **expanze** listu, stavy uzlu **FRESH/OPEN/CLOSED**.
- Kritéria: **úplnost, optimalita, čas, paměť** ($b$, $d$).

### Algoritmy (společné schéma, liší se strukturou `open`)
- **Náhodné** — `open` = množina, náhodný výběr; nepoužitelné, neoptimální.
- **BFS** — `open` = fronta (FIFO); úplné, optimální v počtu hran, čas i paměť $O(b^d)$.
- **DFS** — `open` = zásobník (LIFO); paměťově úsporné, neoptimální, na nekonečném grafu neúplné.

### Návaznost
- Ohodnocené hrany (cena cesty) + informované prohledávání ([[Dijkstra]], [[A-star|A*]]) → [[22ZUM-long|otázka 22]].

### Typické doplňující otázky (doptávání)
*(Atribuovaní zkoušející ze zkušeností 2021–2024 — Smítková Janků; otázku ale na komisi 2026 zadává Holeňa. Obsah je kanonický pro okruh.)*
- **Smítková Janků:** „Jaká je podmínka zastavení algoritmu?" → cíl se testuje **při odebrání uzlu z `open`** (`if x ∈ G then return`), ne při jeho generování → §2.
- **Smítková Janků:** „Proč se v reálu nepoužívá BFS, i když vždy najde nejkratší cestu? Našel by cíl v grafu s větvením 10 a hloubkou 20?" → exponenciální **paměť** $O(b^d)$; $10^{20}$ uzlů → ne v reálném čase ani paměti → §4.
- **Smítková Janků:** „Jaká je spojitost Dijkstry a BFS?" → BFS = Dijkstra pro jednotkové ceny hran → §4.
- **Smítková Janků:** „Jak se implementuje DFS — iterativně, nebo rekurzivně?" → explicitní zásobník vs. zásobník volání, ekvivalentní → §5.
- **Smítková Janků:** „Definujte přesně stavový prostor / stavy uzlu" → $(S,A)$, FRESH/OPEN/CLOSED → §1–2.
