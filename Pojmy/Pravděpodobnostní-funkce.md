---
aliases: [pravděpodobnostní funkce, pravděpodobnostní funkci, pravděpodobnostní funkcí, pravděpodobnostní funkce hodnot, diskrétní hustota, pravděpodobnosti hodnot, probability mass function, pmf]
tags: [definice, kurz/PST]
---

# Pravděpodobnostní funkce

## Definice

Pro **diskrétní** [[Náhodná-veličina|náhodnou veličinu]] $X$ nabývající hodnot $\{x_1, x_2, \dots\}$ je **pravděpodobnostní funkce** (též *diskrétní hustota*) předpis
$$x \mapsto P(X = x), \qquad k = 1, 2, \dots$$
Nenulová jen pro hodnoty $x_k$, kterých $X$ nabývá.

## Vlastnosti

- **normalizace:** $\displaystyle\sum_{\text{all } x_k} P(X = x_k) = 1$;
- $\displaystyle P(X \in B) = \sum_{x_k \in B} P(X = x_k)$;
- vztah k [[Distribuční-funkce|distribuční funkci]]: $\displaystyle F_X(x) = \sum_{k:\, x_k \le x} P(X = x_k)$ a (při $x_1 < x_2 < \dots$) $P(X = x_k) = F_X(x_k) - F_X(x_{k-1})$.

Spojitou analogií je [[Hustota|hustota]] $f_X$ (sumy se nahradí integrály).

## Související

- [[Náhodná-veličina]]
- [[Hustota]]
- [[Distribuční-funkce]]
