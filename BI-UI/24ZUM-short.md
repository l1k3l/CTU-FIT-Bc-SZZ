---
tags: [otázka, kurz/ZUM, otázka/24, todo]
---

# 24 — Genetické a evoluční algoritmy (zkrácená verze)

## Princip
[[Genetický-algoritmus|Evoluční algoritmy]] = populační iterativní optimalizace (přírodní výběr). **Genotyp** (reprezentace) vs **fenotyp** (význam), **fitness** = kriteriální funkce, **jedinec / populace / generace**.

**Schéma:** Inicializace → ( **selekce** → **křížení** → **mutace** → **náhrada** )* dokud neplatí ukončovací podmínka.

## Genetické operátory
- **Selekce:** ruletová ($P_i=f_i/\sum_j f_j$), turnajová (nejlepší z $k$).
- **Křížení:** jedno-/dvou-/n-bodové, uniformní (výměna info mezi 2 rodiči).
- **Mutace:** bit-flip, prav. $p_m\approx10^{-2}$ (drobná náhodná změna).

## Paradigmata

| | reprezentace | mutace | křížení |
|---|---|---|---|
| **GA** (Holland) | binární $\{0,1\}^n$ | bit-flip | ano |
| **GP** (Koza) | [[Strom\|stromy]] (programy) | subtree/point/shrink | výměna podstromů |
| **EP** (Fogel) | [[Konečný-automat\|stavové automaty]] | tabulka přechodů | **NE** |
| **ES** (Rechenberg) | reálné $\mathbb{R}^n$ | gaussovská + self-adapt. $\sigma$ | uniformní |

ES notace: $(\mu+\lambda)$ elitní / $(\mu,\lambda)$ jen potomci; $(1+\lambda)\approx$ hill climbing. Pravidlo **1/5** (úspěšnost mutace → úprava $\sigma$).

## Optimalizace
**Explorace** (mutace) vs **exploatace** (selekce); řídí selekční tlak + míra mutace. Hrozba: **předčasná konvergence** (= uvíznutí v lok. optimu); zmírnění: niching.

---

## Co odpovědět rychle
- **Operátory:** selekce (ruletová/turnajová), křížení (1-/2-/n-bod/uniformní), mutace (bit-flip $p_m$).
- **GA** = binární, **GP** = stromy/programy, **EP** = automaty (jen mutace), **ES** = reálné vektory (gauss + self-adapt $\sigma$).
- **Explorace vs exploatace**, **předčasná konvergence**.
- **Doptávání (ruletová podrobně):** kolo s výsečemi $\propto$ fitness, výběr přes kumulativní $P_i$, nezáporné fitness, dominance jedince → předčasná konvergence. Únik z lok. optima v GP: ↑mutace / niching / restart.
