---
aliases: [simulované žíhání, simulovaného žíhání, simulovaným žíháním, simulated annealing, simulované popouštění, simulované ochlazování]
tags: [algoritmus, kurz/ZUM]
---

# Simulované žíhání

## Princip

Rozšíření [[Hill-climbing|hill climbingu]] o řídicí parametr $t$ — **teplotu**. Lepšího souseda $y$ přijme vždy; **zhoršujícího** souseda přijme s pravděpodobností
$$P = e^{\,(f_{\text{new}} - f_{\text{curr}})\,/\,t}$$
(při maximalizaci je $f_{\text{new}} - f_{\text{curr}} \le 0$, tedy $P \in (0, 1]$; ekvivalent klasického $P = e^{-\Delta E / T}$, kde $\Delta E$ je míra zhoršení). Čím **větší zhoršení** a čím **nižší teplota**, tím menší $P$.

## Žíhání a chlazení

Analogie tepelného zpracování oceli: za vysoké teploty se atomy uvolní z mřížky, pomalým **chlazením** zapadnou do pravidelné mřížky. V optimalizaci:
- vysoké $t$ ⇒ často přijímá i zhoršující kroky → **explorace**, překonává údolí mezi lokálními optimy,
- $t \to 0$ ⇒ chová se jako čistý hill climbing.

Teplota se každou iteraci snižuje podle **rozvrhu chlazení**.

## Související

- [[Hill-climbing]], [[Tabu-prohledávání]], [[Lokální-extrém]]
