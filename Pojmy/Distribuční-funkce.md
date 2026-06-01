---
aliases: [distribuční funkce, distribuční funkci, distribuční funkcí, distribučních funkcí, distribučními funkcemi, distribuční, CDF, cumulative distribution function]
tags: [definice, kurz/PST]
---

# Distribuční funkce

## Definice

**Distribuční funkce** [[Náhodná-veličina|náhodné veličiny]] $X$ je
$$F_X(x) = P(X \le x), \qquad x \in \mathbb{R}.$$
Jednoznačně určuje pravděpodobnostní rozdělení $X$.

## Vlastnosti

Funkce $F$ je distribuční funkcí nějaké náhodné veličiny $\iff$ splňuje:
1. **neklesající:** $x < y \Rightarrow F(x) \le F(y)$;
2. **limity:** $\displaystyle\lim_{x\to-\infty} F(x) = 0$, $\displaystyle\lim_{x\to+\infty} F(x) = 1$;
3. **spojitá zprava:** $\displaystyle\lim_{y\to x^+} F(y) = F(x)$.

## Použití

- $P(X > x) = 1 - F(x)$;
- $P(x < X \le y) = F(y) - F(x)$;
- $P(X < x) = \lim_{y\to x^-} F(y)$;
- $P(X = x) = F(x) - \lim_{y\to x^-} F(y)$ (velikost skoku v bodě $x$).

**Diskrétní** $X$: $F$ je schodovitá, skok v $x_k$ o velikosti $P(X = x_k)$.
**Spojitá** $X$: $F$ je spojitá, $F(x) = \int_{-\infty}^x f_X(t)\,dt$ a $f_X(x) = F'(x)$ tam, kde derivace existuje.

## Související

- [[Náhodná-veličina]]
- [[Hustota]]
- [[Pravděpodobnostní-funkce]]
- [[Kvantil]]
