---
tags: [otázka, kurz/ZUM, otázka/26, todo]
---

# 26 — Prohledávání herního stromu (Minimax) (zkrácená verze)

## Herní strom
Hra v extenzivní formě = [[Herní-strom|herní strom]] (uzly = stavy, hrany = tahy, listy = terminály s utilitou $u$). **Dvouhráčová zero-sum:** $u_1+u_2=0$, hráči **MAX** (max $u$, kořen) a **MIN** (min $u$). Kombinatorická exploze (šachy $\sim10^{45}$) → omezená hloubka $d$ + evaluační funkce.

## Minimax
[[Minimax]] (perfektní hra soupeře): ohodnocení uzlu
$$\mathit{eval}[x]=\begin{cases}u(x)&\text{list / hloubka }d\\\max_a \mathit{eval}[\sigma(x,a)]&\text{MAX}\\\min_a \mathit{eval}[\sigma(x,a)]&\text{MIN}\end{cases}$$
Vrátí akci $\arg\max$ v kořeni. **Optimální** proti optimálnímu soupeři; čas $O(b^d)$, prostor $O(b\cdot d)$.

## Alfa-beta prořezávání
[[Alfa-beta-prořezávání]]: stejný výsledek, ořezává. $\alpha$ = nejlepší zaručené pro MAX, $\beta$ = pro MIN (dědí se po cestě ke kořeni). MAX zvyšuje $\alpha$, MIN snižuje $\beta$; při **$\alpha\ge\beta$** prořež zbytek potomků.

**Pořadí tahů (heuristiky):** optimální (nejlepší tah první) → $O(b^{d/2})$ ($b\to\sqrt{b}$, **2× hloubka**); náhodné $\approx O(b^{3d/4})$. *Killer heuristic* (preferuj tah, co jinde ořezal).

## Evaluační funkce
Odhad kvality pozice v mezní hloubce. Požadavky: **rychlost** + **spolehlivost**. Úskalí: **problém horizontu** (ztráta těsně za hloubkou $d$), **quiescence search** (končit v klidných stavech).

---

## Co odpovědět rychle
- **Minimax:** MAX/MIN, $\mathit{eval}$ rekurzivně, optimální, $O(b^d)$.
- **Alfa-beta:** $\alpha/\beta$ meze, cutoff $\alpha\ge\beta$; optim. pořadí $O(b^{d/2})$.
- **Evaluační funkce** (rychlá, spolehlivá), problém horizontu, quiescence.
