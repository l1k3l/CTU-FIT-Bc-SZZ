---
aliases: [kvantil, kvantilu, kvantily, kvantilů, kvantilem, kvantilová funkce, medián, mediánu, kvartil, kvartily, kritická hodnota, kritické hodnoty, quantile, percentil]
tags: [definice, kurz/PST]
---

# Kvantil

## Definice

Nechť $X$ má [[Distribuční-funkce|distribuční funkci]] $F_X$ a $\alpha \in (0,1)$. **$\alpha$-kvantil** je
$$q_\alpha = \inf\{x : F_X(x) \ge \alpha\}.$$
Jako funkce $\alpha$ se nazývá **kvantilová funkce** a značí $F_X^{-1}(\alpha)$. Pro ryze rostoucí spojitou $F_X$ platí $F_X(q_\alpha) = \alpha$, tedy $F_X^{-1}$ je klasická inverze.

## Speciální kvantily

- $q_{0.5}$ — **medián** (míra polohy, analogie [[Střední-hodnota|střední hodnoty]]);
- $q_{0.25}$, $q_{0.75}$ — dolní / horní **kvartil**; $q_{0.75} - q_{0.25}$ je interkvartilové rozpětí (míra rozptýlení);
- **kritická hodnota** $c_\alpha = q_{1-\alpha}$ (horní $\alpha$-kvantil).

U [[Normální-rozdělení|normálního rozdělení]] se kvantily $N(0,1)$ značí $u_\alpha$, kritické hodnoty $z_\alpha$ (kde $P(Z > z_\alpha) = \alpha$). Kritické hodnoty rozdělení $\chi^2$, $t$, $F$ se používají v [[Interval-spolehlivosti|intervalech spolehlivosti]] a [[Testování-hypotéz|testech]].

## Související

- [[Distribuční-funkce]]
- [[Střední-hodnota]]
- [[Normální-rozdělení]]
