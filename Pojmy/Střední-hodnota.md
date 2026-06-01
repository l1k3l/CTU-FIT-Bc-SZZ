---
aliases: [střední hodnota, střední hodnotu, střední hodnoty, střední hodnotě, střední hodnotou, středních hodnot, středním hodnotám, EX, E X, očekávaná hodnota, expectation, mean]
tags: [definice, kurz/PST]
---

# Střední hodnota

## Definice

**Střední hodnota** (expectation) [[Náhodná-veličina|náhodné veličiny]] $X$ je vážený průměr jejích možných hodnot:
$$\mathbb{E}X = \sum_{k} x_k\,P(X = x_k) \quad\text{(diskrétní)}, \qquad \mathbb{E}X = \int_{-\infty}^{+\infty} x\,f_X(x)\,dx \quad\text{(spojitá)}.$$
Existuje, právě když příslušná suma/integrál **absolutně konverguje**.

**Střední hodnota funkce:** $\displaystyle \mathbb{E}\,g(X) = \sum_k g(x_k)P(X=x_k)$ resp. $\int g(x)f_X(x)\,dx$ (není nutné znát rozdělení $g(X)$).

## Vlastnosti

- **linearita:** $\mathbb{E}(aX + bY) = a\,\mathbb{E}X + b\,\mathbb{E}Y$ (platí i pro závislé $X,Y$);
- monotonie: $X \ge 0 \Rightarrow \mathbb{E}X \ge 0$;
- konstanta: $\mathbb{E}c = c$;
- pro **nezávislé** $X, Y$: $\mathbb{E}(XY) = \mathbb{E}X\,\mathbb{E}Y$;
- $\mu_k = \mathbb{E}(X^k)$ je $k$-tý **moment**, $\mathbb{E}(X - \mathbb{E}X)^k$ $k$-tý **centrální moment**.

Interpretace: rovnovážný bod (těžiště) rozdělení. Robustnější mírou polohy je [[Kvantil|medián]].

## Související

- [[Rozptyl]]
- [[Náhodná-veličina]]
- [[Kvantil]]
- [[Kovariance]]
