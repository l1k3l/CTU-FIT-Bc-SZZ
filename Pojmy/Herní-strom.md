---
aliases: [herní strom, herního stromu, herním stromu, herní stromy, hra v extenzivní formě, hry v extenzivní formě, extenzivní forma, prohledávání herního stromu]
tags: [definice, kurz/ZUM]
---

# Herní strom (hra v extenzivní formě)

## Definice

**Hra v extenzivní formě** je dána stromem, jehož uzly jsou herní stavy a hrany tahy (akce). Formálně osmice $(\mathcal{N}, \mathcal{A}, H, T, \chi, \rho, \sigma, u)$:
- $H$ — **rozhodovací uzly**, $T$ — **terminální uzly (listy)**, $T \cap H = \emptyset$,
- $\chi(h)$ — akce dostupné v uzlu $h$, $\rho(h)$ — hráč na tahu,
- $\sigma : H \times \mathcal{A} \to H \cup T$ — *prostá* **funkce následnictví** (proto má graf tvar **stromu** = herní strom),
- $u_i : T \to \mathbb{R}$ — utilita hráče $N_i$ v listech.

**Dvouhráčová zero-sum hra:** $|\mathcal{N}| = 2$ a $u_1(t) + u_2(t) = 0$ ⇒ stačí jediná funkce $u$. Hráči: **MAX** (maximalizuje $u$, je na tahu v kořeni) a **MIN** (soupeř, minimalizuje). Výhra/remíza/prohra $\mapsto +1 / 0 / -1$.

## Velikost v praxi

Piškvorky $\sim 10^3$, dáma $\sim 10^{20}$, šachy $\sim 10^{45}$ konfigurací (Shannonovo číslo $10^{120}$ průběhů). → nutné prohledávání s **omezenou hloubkou** + heuristická **evaluační funkce** v listech.

## Související

- [[Minimax]], [[Alfa-beta-prořezávání]]
- [[Hra-v-normální-formě]] (normální forma — reprezentace maticí), [[Strom]]
