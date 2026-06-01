---
aliases: [rozptyl, rozptylu, rozptylem, rozptyly, rozptylů, variance, var, směrodatná odchylka, směrodatnou odchylku, směrodatné odchylky, standardní odchylka, sd, σ²]
tags: [definice, kurz/PST]
---

# Rozptyl

## Definice

**Rozptyl** (variance) [[Náhodná-veličina|náhodné veličiny]] $X$ je průměrná kvadratická odchylka od [[Střední-hodnota|střední hodnoty]]:
$$\operatorname{var}X = \mathbb{E}\bigl[(X - \mathbb{E}X)^2\bigr] = \sigma^2.$$
**Směrodatná odchylka** $\operatorname{sd}X = \sigma = \sqrt{\operatorname{var}X}$ (stejné jednotky jako $X$).

## Výpočetní vzorec

$$\operatorname{var}X = \mathbb{E}(X^2) - (\mathbb{E}X)^2.$$
Důsledek: $(\mathbb{E}X)^2 \le \mathbb{E}(X^2)$.

## Vlastnosti

- $\operatorname{var}(aX + b) = a^2 \operatorname{var}X$;
- $\operatorname{var}(c) = 0$;
- $\operatorname{var}X \ge 0$ vždy;
- $\operatorname{var}(X \pm Y) = \operatorname{var}X + \operatorname{var}Y \pm 2\operatorname{cov}(X,Y)$; pro **nekorelované** (tedy i nezávislé) $X,Y$: $\operatorname{var}(X \pm Y) = \operatorname{var}X + \operatorname{var}Y$.

## Související

- [[Střední-hodnota]]
- [[Kovariance]]
- [[Náhodná-veličina]]
