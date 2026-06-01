---
aliases: [náhodný výběr, náhodného výběru, náhodným výběrem, náhodné výběry, náhodných výběrů, výběr, realizace náhodného výběru, i.i.d. výběr, random sample]
tags: [definice, kurz/PST]
---

# Náhodný výběr

## Definice

**Náhodný výběr** rozsahu $n$ z rozdělení $F$ je $n$-tice **nezávislých** a **stejně rozdělených** ([[Nezávislost-náhodných-veličin|i.i.d.]]) [[Náhodná-veličina|náhodných veličin]] $X_1, \dots, X_n$ s [[Distribuční-funkce|distribuční funkcí]] $F$.

**Realizace náhodného výběru** (data) je $n$-tice konkrétních pozorovaných čísel $x_1, \dots, x_n$.

## Souvislosti

- Východisko **matematické statistiky**: na základě realizace odhadujeme neznámé rozdělení / jeho parametr $\theta$ (volíme parametrickou třídu $\{F_\theta : \theta \in \Theta\}$).
- **Statistika** = libovolná funkce náhodného výběru nezávislá na $\theta$ (např. [[Bodový-odhad|výběrový průměr]] $\bar X_n$).
- Tvar rozdělení odhadujeme **histogramem** a **empirickou distribuční funkcí** $F_n(x) = \tfrac1n\sum_{i=1}^n \mathbf{1}_{\{X_i \le x\}}$.

## Související

- [[Bodový-odhad]]
- [[Interval-spolehlivosti]]
- [[Testování-hypotéz]]
- [[Centrální-limitní-věta]]
- [[Nezávislost-náhodných-veličin]]
