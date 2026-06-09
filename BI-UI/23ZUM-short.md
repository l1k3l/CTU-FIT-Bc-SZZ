---
tags: [otázka, kurz/ZUM, otázka/23, todo]
---

# 23 — Lokální prohledávání (zkrácená verze)

## Princip
Pro úlohy, kde je důležitý **jen cílový stav, ne cesta**. Optimalizační problém $x^*\in\arg\max_{x\in X}f(x)$ ($f$ = kriteriální funkce). Obecné $f$ je těžké (NP, struktura neznámá) → **iterativní optimalizace** (pokus–omyl, jeden kandidát + jeho **okolí**). Bez derivací.

## Hill climbing
[[Hill-climbing]]: generuj souseda, přejdi k němu, je-li lepší ("jdi do kopce"). Varianty: **first-choice** (1 soused), **steepest ascent** ($k$ sousedů, nejlepší), **restarty**.

**Problém lokálního minima:** uvázne v [[Lokální-extrém|lokálním optimu]] / na plošině / hřbetu — únik vyžaduje **dočasně zhoršující krok**. (+ prokletí dimenzionality.) Dilema velikosti okolí: malé → uvázne; velké → míjí optima.

## Zmírnění

**[[Simulované-žíhání]]:** přidá teplotu $t$; zhoršujícího souseda přijme s prav.
$$P=e^{(f_{\text{new}}-f_{\text{curr}})/t}\quad(\le 1).$$
Větší zhoršení / nižší $t$ → menší $P$. Vysoké $t$ = explorace, $t\to0$ = hill climbing. Teplota klesá (rozvrh chlazení). *(Analogie: žíhání oceli.)*

**[[Tabu-prohledávání]]:** **tabu list** zakazuje návrat do navštívených oblastí → vynucený sestup z „dobytého vrcholu", brání oscilaci. Tabu list dle metriky (euklid./Hamming/strukturální).

> Žíhání = únik **pravděpodobnostní**; tabu = únik **deterministický** (paměť).

---

## Co odpovědět rychle
- **Lokální prohledávání:** jeden kandidát + okolí, max $f$, cesta nezajímá.
- **Hill climbing** uvázne v **lokálním optimu** (nedělá zhoršující krok).
- **Simulované žíhání:** $P=e^{(f_{\text{new}}-f_{\text{curr}})/t}$, vysoké $t$ explorace.
- **Tabu:** tabu list zakáže návrat → vynucený sestup; drží **víc stavů** (často s omez. délkou).
- **Doptávání (Kordík trvá na vzorci žíhání!):** $P=e^{(f_{\text{new}}-f_{\text{curr}})/t}$. Lokální vs. globální: lokální = jen okolí 1 kandidáta (riziko lok. optima), globální/systematické (ot. 21–22) = celý prostor.
