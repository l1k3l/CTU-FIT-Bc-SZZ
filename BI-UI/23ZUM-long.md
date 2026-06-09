---
studyplan: true
etapa: "6 · ZUM — Holeňa"
qid: "23ZUM"
examiner: "Holeňa"
topic: "Lokální prohledávání, hill-climbing, lokální minimum, tabu search, simulované žíhání"
readiness: nezačato
tags: [otázka, kurz/ZUM, otázka/23, todo]
---

# Lokální prohledávání

> **Otázka SZZ:** Principy lokálního prohledávání, metody typu hill-climbing. Problém lokálního minima a metody jeho zmírnění (tabu search, simulované žíhání).

Zdroje: BI-ZUM (FIT ČVUT), přednáška 4 — *Algoritmy lokálního prohledávání (iterativní optimalizace)*.

Značení: kriteriální funkce $f : X \to \mathbb{R}$, aktuální řešení $x$, soused $y$, okolí, teplota $t$, tabu list.

---

## 1. Principy lokálního prohledávání

Pro mnoho problémů je **cesta irelevantní, důležitý je jen cílový stav** (problém $N$ dam, lineární regrese, optimalizace vektoru z $\mathbb{R}^n$ či $\{0,1\}^n$). Pak řešíme **optimalizační problém**: najít
$$x^* \in \arg\max_{x \in X} f(x),$$
kde $X$ je množina přípustných řešení a $f$ **kriteriální (účelová) funkce**. (Maximalizace a minimalizace jsou ekvivalentní, $\arg\max f = \arg\min (-f)$.)

Speciální „snadné" třídy (nejmenší čtverce, lineární a konvexní programování) mají spolehlivé algoritmy. **Obecný** problém je ale velmi těžký (NP-úplné úlohy, struktura $f$ nemusí být známá) → nasazujeme **algoritmy iterativní optimalizace** (lokální prohledávání): metodou **pokus–omyl** postupně zlepšují kandidáta a využívají informaci o $f$ získanou během běhu. Protože o $f$ nic nepředpokládáme, **nelze** použít metody z analýzy (hledání nulové derivace).

Naivní metody: **brute-force** (systematické navzorkování — neúnosné ve vyšších dimenzích) a **náhodná optimalizace** (vzorkuje náhodné body) — obě neefektivní, neberou v potaz info o $f$.

**Lokální vs. globální (systematické) prohledávání.** Lokální prohledávání udržuje **jediného aktuálního kandidáta** a zkoumá jen jeho **okolí** — neudržuje cesty ani systematické pokrytí prostoru. Je paměťově úsporné a rychlé, ale **může uváznout v lokálním optimu** (negarantuje globální optimum). Systematické prohledávání (BFS/DFS/A*, ot. 21–22) naopak prochází celý stavový strom a globální optimum najde, za cenu exponenciální paměti.

---

## 2. Hill climbing

**[[Hill-climbing|Hill climbing]]** pracuje s jediným kandidátem $x$: generuje body v jeho **okolí** (sousedství) a přejde k sousedovi, je-li lepší. Analogie: šplhání do kopce — „rozhlížíme se a jdeme nahoru".

Generování souseda: vektor z $\mathbb{R}^n$ ve vzdálenosti $\le \varepsilon$; binární vektor lišící se v $\le k$ bitech; u $N$ dam konfigurace s přesunutou jednou dámou; obecně sousední uzel ve stavovém prostoru.

```
x ← random_state();  i ← 0
while ¬good_enough(x) ∧ i < max_iter do
    y ← random_neighbor(x)
    if f(y) > f(x) then x ← y
    i ← i + 1
return x
```

**Varianty:**
- **základní (first-choice/stochastic):** 1 náhodný soused, přijmi, je-li lepší (kód výše),
- **steepest ascent (nejstrmější stoupání):** vygeneruj $k$ sousedů, vyber nejlepšího,
- **s restarty:** spouštěj opakovaně (např. 1000×) z náhodných počátků.

---

## 3. Problém lokálního minima

Dva největší problémy hill climbingu (a iterativní optimalizace vůbec):

1. **Lokální optimum / minimum** — algoritmus uvázne v **[[Lokální-extrém|lokálním extrému]]**, na **plošině** nebo **hřbetu**. K dalšímu zlepšení by byl nutný *dočasně zhoršující krok*, který hill climbing zásadně nedělá.
2. **Prokletí dimenzionality** — objem prostoru roste exponenciálně s dimenzí, nelze proto dostatečně hustě navzorkovat okolí bodu.

**Dilema velikosti okolí:** malé okolí ⇒ uvázneme v lokálním optimu (nepřekonáme údolí); velké okolí ⇒ míjíme lokální optima velkými kroky. Řešení → simulované žíhání a tabu prohledávání.

---

## 4. Simulované žíhání

**[[Simulované-žíhání|Simulované žíhání]]** rozšiřuje hill climbing o řídicí parametr $t$ — **teplotu**. Lepšího souseda přijme vždy; **zhoršujícího** přijme s pravděpodobností
$$P = e^{\,(f_{\text{new}} - f_{\text{curr}})\,/\,t}$$
(při maximalizaci je $f_{\text{new}} - f_{\text{curr}} \le 0$, takže $P \in (0, 1]$; jde o klasické $P = e^{-\Delta E / T}$ s $\Delta E$ = míra zhoršení). **Čím větší zhoršení a čím nižší teplota, tím menší $P$.**

```
x ← random_state();  t ← high
while t ≥ 0 do
    y ← random_neighbor(x)
    if f(y) > f(x) then x ← y
    else if P(f(x), f(y), t) ≥ random(0,1) then x ← y    # přijmi zhoršení
    t ← decrease(t)
return x
```

**Analogie (žíhání oceli):** za vysoké teploty se atomy uvolní z mřížky, pomalým **chlazením** zapadnou pravidelně. Vysoké $t$ ⇒ hodně zhoršujících kroků (explorace), $t \to 0$ ⇒ chování jako čistý hill climbing. Teplota klesá podle **rozvrhu chlazení**.

---

## 5. Tabu prohledávání

**[[Tabu-prohledávání|Tabu prohledávání]]** brání oscilaci a nutí algoritmus opustit lokální optimum. Zavádí **tabu list** — popis částí prostoru, kam se kandidát nesmí vrátit. Vyšplhá-li algoritmus na vrchol, je nucen „dobytý vrchol" opustit a zahájit **vynucený sestup**; navštívené oblasti se postupně zakazují (tabu list roste a vytlačuje hledání do neprozkoumaných oblastí).

Tabu list typicky obsahuje **více stavů / oblastí najednou** (ne jen poslední) — postupně se do něj přidávají navštívené stavy (v některých variantách i více než jeden za krok), často s **omezenou délkou** (po čase nejstarší zákazy expirují, jinak by hledání zamrzlo).

Podoba tabu listu je daná podobností / metrikou na stavech: euklidovská či cosinová vzdálenost ($\mathbb{R}^n$), Hammingova vzdálenost ($\{0,1\}^n$), strukturální podobnost (grafy/stromy).

**Žíhání vs. tabu:** žíhání uniká z lokálního optima *pravděpodobnostně* (občas přijme zhoršení), tabu *deterministicky* pomocí paměti (zakáže návrat).

> Za hranicí jednoho kandidáta jsou **populační metody** (více vzájemně interagujících řešení) — viz [[24ZUM-long|genetické a evoluční algoritmy (ot. 24)]].

---

## Co je potřeba na zkoušku znát

### Definice
- **Optimalizační problém** $x^* \in \arg\max_{x\in X} f(x)$; $f$ = kriteriální funkce.
- **Lokální prohledávání / iterativní optimalizace:** jeden kandidát, okolí, pokus–omyl.
- **Lokální optimum**, plošina, hřbet; **prokletí dimenzionality**.

### Metody
- **Hill climbing** (first-choice / steepest ascent / restarty): jdi k lepšímu sousedovi; uvázne v lokálním optimu.
- **Simulované žíhání:** přijmi zhoršení s $P = e^{(f_{\text{new}} - f_{\text{curr}})/t}$; vysoké $t$ = explorace, $t \to 0$ = hill climbing.
- **Tabu prohledávání:** tabu list zakazuje návrat do navštívených oblastí → vynucený sestup z lokálního optima.

### Pointa
Lokální minimum překonáme jen *dočasně zhoršujícím krokem* — žíhání ho připustí pravděpodobnostně, tabu ho vynutí pamětí.

### Typické doplňující otázky (doptávání)
*(Atribuovaní zkoušející ze zkušeností 2023–2025 — Kordík, Smítková Janků; na komisi 2026 zadává Holeňa. Okruh je v posledních letech častý a Kordík na vzorec žíhání trvá.)*
- **Kordík:** „Napište vzoreček s pravděpodobností, že simulované žíhání zvolí horší stav." → $P = e^{(f_{\text{new}} - f_{\text{curr}})/t}$ (klasické $e^{-\Delta E/T}$) → §4. *(Doptával se na něj výslovně a studentovi ho nakonec nadiktoval — mít ho přesně.)*
- **Kordík:** „Jaký je rozdíl mezi globálním a lokálním prohledáváním?" → lokální = okolí jednoho kandidáta, hrozí lokální optimum; globální/systematické (ot. 21–22) projde celý prostor → §1.
- **Kordík:** „Přidává se do tabu listu víc stavů?" → ano, tabu list typicky drží více oblastí, často s omezenou délkou → §5.
