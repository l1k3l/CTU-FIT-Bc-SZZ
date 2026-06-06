---
studyplan: true
etapa: "6 · ZUM — Holeňa"
qid: "26ZUM"
examiner: "Holeňa"
topic: "Herní strom, Minimax, alfa-beta prořezávání"
readiness: nezačato
tags: [otázka, kurz/ZUM, otázka/26, todo]
---

# Prohledávání herního stromu (Minimax)

> **Otázka SZZ:** Prohledávání herního stromu: Algoritmus Minimax, alfa-beta prořezávání a heuristiky.

Zdroje: BI-ZUM (FIT ČVUT), přednáška 8 — *Hry v extenzivní formě, Algoritmus Minimax*.

Značení: hráči MAX (△) a MIN (▽), hodnota uzlu $\mathit{eval}[x]$, utilita $u$, větvící faktor $b$, hloubka $d$, meze $\alpha$, $\beta$.

---

## 1. Herní strom (hra v extenzivní formě)

Hry jako piškvorky, šachy, dáma, Go se reprezentují **extenzivní formou** = stromem. **[[Herní-strom|Herní strom]]** formálně: osmice $(\mathcal{N}, \mathcal{A}, H, T, \chi, \rho, \sigma, u)$ — rozhodovací uzly $H$, terminální uzly (listy) $T$, dostupné akce $\chi(h)$, hráč na tahu $\rho(h)$, *prostá* **funkce následnictví** $\sigma$ (díky níž má graf tvar **stromu**), utility $u_i : T \to \mathbb{R}$ v listech.

**Dvouhráčová zero-sum hra:** $|\mathcal{N}| = 2$, $u_1(t) + u_2(t) = 0$ ⇒ stačí jediná funkce $u$ a dva hráči:
- **MAX** (△) — je na tahu v kořeni, **maximalizuje** $u$,
- **MIN** (▽) — soupeř, **minimalizuje** $u$. Výhra / remíza / prohra $\mapsto +1 / 0 / -1$.

**Perfektní hra** = hráč v každém tahu volí *bezchybnou* akci (maximalizuje zaručenou hodnotu při pesimistickém očekávání soupeřovy reakce). V praxi je perfektní hra neúnosná kvůli **kombinatorické explozi**: piškvorky $\sim 10^3$, dáma $\sim 10^{20}$, šachy $\sim 10^{45}$ konfigurací (Shannonovo číslo $10^{120}$ průběhů) → nutné **prohledávání s omezenou hloubkou** + heuristická **evaluační funkce** v listech.

---

## 2. Algoritmus Minimax

**[[Minimax|Minimax]]** volí optimální tah v kořeni za předpokladu perfektní hry soupeře. Průchodem do hloubky vygeneruje strom (do max. hloubky $d$ z kořene $x_0$ typu MAX) a při uzavírání uzlu $x$ mu přiřadí hodnotu:
$$
\mathit{eval}[x] =
\begin{cases}
u(x) & x \text{ je terminál (skutečná utilita) nebo dosažena hloubka } d \text{ (heuristická evaluace)},\\[2pt]
\max_{a \in \chi(x)} \mathit{eval}[\sigma(x, a)] & x \text{ je uzel MAX},\\[2pt]
\min_{a \in \chi(x)} \mathit{eval}[\sigma(x, a)] & x \text{ je uzel MIN}.
\end{cases}
$$
Vrátí akci $a \in \arg\max_{a \in \chi(x_0)} \mathit{eval}[\sigma(x_0, a)]$.

**Příklad** (kořen MAX, druhá úroveň MIN, listy ohodnoceny):
- levý MIN $= \min(4, 2, 8) = 2$, prostřední MIN $= \min(7, 9) = 7$, pravý MIN $= \min(6, 1, 5) = 1$,
- kořen MAX $= \max(2, 7, 1) = \mathbf{7}$ → MAX volí prostřední větev.

**Vlastnosti:** optimální proti optimálnímu soupeři; čas $O(b^d)$, prostor $O(b \cdot d)$. V šachách je průměrný větvící faktor $b \approx 35$ → základní Minimax je pro hlubší hledání neúnosný a je nutné jej optimalizovat (alfa-beta).

---

## 3. Alfa-beta prořezávání

**[[Alfa-beta-prořezávání|Alfa-beta prořezávání]]** dává **stejný výsledek** jako Minimax, ale neprochází větve, které nemohou ovlivnit rozhodnutí v kořeni. Po cestě ke kořeni se udržují dvě meze:
- $\alpha$ = nejlepší (největší) hodnota dosud zaručená pro **MAX**,
- $\beta$ = nejlepší (nejmenší) hodnota dosud zaručená pro **MIN**.

Expandovaný potomek **dědí** $\alpha, \beta$ rodiče (kořen startuje s $\alpha = -\infty$, $\beta = +\infty$). V uzlu MAX se zvyšuje $\alpha$, v uzlu MIN snižuje $\beta$. Jakmile **$\alpha \ge \beta$** („překřížení" — interval $(\alpha, \beta)$ je prázdný, včetně případu $\alpha = \beta$), zbývající potomci aktuálního uzlu se **prořežou** — nemohou výsledek změnit.

```
MAX uzel: zkoumej potomky, α ← max(α, eval[potomek]); je-li α ≥ β, prořež zbytek
MIN uzel: zkoumej potomky, β ← min(β, eval[potomek]); je-li α ≥ β, prořež zbytek
```

### Vliv uspořádání tahů (heuristiky)
Zrychlení závisí na **pořadí expanze** uzlů:
- **optimální** pořadí (nejlepší tah první): $O(b^{d/2})$ — efektivní větvící faktor $b \to \sqrt{b}$, což **zdvojnásobí** prohledatelnou hloubku,
- **náhodné** pořadí: přibližně $O(b^{3d/4})$ (pro $b < 1000$).

K dobrému pořadí slouží heuristiky uspořádání akcí (útok > defenziva) a např. **killer heuristic** — prioritizuj tah, který už jinde ve stromě způsobil prořez.

---

## 4. Heuristická evaluační funkce

Pro hry příliš velké na hledání až k terminálům: v **mezní hloubce** $d$ se uzel ohodnotí **evaluační funkcí** (odhad kvality pozice), tyto hodnoty se použijí jako „listy" v Minimaxu. Vše tedy závisí na kvalitě evaluace.

**Požadavky:** **rychlost** (nejdůležitější) a **spolehlivost** (hodnota koreluje s kvalitou stavu). Příklad: v šachách „materiální" indikátory (vážený počet figur).

**Úskalí:**
- **problém horizontu (horizon effect):** v hloubce $d$ vypadá pozice dobře, ale těsně za „horizontem" ($d+1$) hrozí ztráta (např. vzetí dámy), kterou hledání nevidí,
- **quiescence search:** expanzi končit jen v „klidných" stavech, po nichž bezprostředně nehrozí divoké výměny figur.

> Mimo rámec otázky: alternativy k Minimaxu — neuronové sítě (Blondie24), Monte Carlo Tree Search + deep/reinforcement learning (AlphaGo, 2016).

---

## Co je potřeba na zkoušku znát

### Definice
- **Herní strom** (extenzivní forma); dvouhráčová **zero-sum** hra; hráči **MAX/MIN**; utilita v listech.
- **Minimax hodnota:** MAX = max potomků, MIN = min potomků, list = $u$ / evaluace.
- **$\alpha$ / $\beta$:** nejlepší zaručená hodnota pro MAX / MIN po cestě ke kořeni; cutoff **$\alpha \ge \beta$**.

### Algoritmy a složitost
- **Minimax:** optimální proti optimálnímu soupeři; čas $O(b^d)$, prostor $O(b \cdot d)$.
- **Alfa-beta:** stejný výsledek, prořezává; optimální pořadí $O(b^{d/2})$ ($b \to \sqrt{b}$, dvojnásobná hloubka), náhodné $\approx O(b^{3d/4})$.

### Heuristiky
- **Evaluační funkce** v mezní hloubce: rychlost + spolehlivost.
- **Problém horizontu**, **quiescence search**, **killer heuristic** (uspořádání tahů).
