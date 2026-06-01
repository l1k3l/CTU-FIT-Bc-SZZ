---
aliases: [korelace, korelaci, korelací, korelační koeficient, korelačního koeficientu, korelačním koeficientem, nekorelované, nekorelovanost, correlation, ρ]
tags: [definice, kurz/PST]
---

# Korelace

## Definice

Pro [[Náhodná-veličina|náhodné veličiny]] $X, Y$ s kladnými rozptyly je **korelační koeficient**
$$\rho(X, Y) = \frac{\operatorname{cov}(X, Y)}{\sigma_X\,\sigma_Y} = \frac{\operatorname{cov}(X,Y)}{\sqrt{\operatorname{var}X}\,\sqrt{\operatorname{var}Y}}.$$
Je to [[Kovariance|kovariance]] **standardizovaných** veličin: $\rho(X,Y) = \mathbb{E}\!\left[\tfrac{X-\mathbb{E}X}{\sigma_X}\cdot\tfrac{Y-\mathbb{E}Y}{\sigma_Y}\right]$. Bezrozměrná míra **lineární** závislosti.

## Vlastnosti

- $-1 \le \rho(X,Y) \le 1$ (ze Schwarzovy nerovnosti);
- invariance vůči rostoucí lineární transformaci: $\rho(aX+b, cY+d) = \rho(X,Y)$ pro $a,c>0$;
- $\rho(X,Y) = \pm 1 \iff$ existují $a > 0, b$ s $Y = \pm aX + b$ (úplná lineární závislost);
- $\rho = 0 \iff X, Y$ **nekorelované**.

[[Nezávislost-náhodných-veličin|Nezávislost]] $\Rightarrow \rho = 0$; opačně to neplatí.

## Související

- [[Kovariance]]
- [[Nezávislost-náhodných-veličin]]
- [[Rozptyl]]
