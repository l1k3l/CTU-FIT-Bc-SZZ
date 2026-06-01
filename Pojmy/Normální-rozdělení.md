---
aliases: [normální rozdělení, normálního rozdělení, normálním rozdělení, normálním rozdělením, Gaussovo rozdělení, Gaussova rozdělení, normální, gaussovské, standardní normální rozdělení, normal distribution, N(μ,σ²)]
tags: [definice, kurz/PST]
---

# Normální rozdělení

## Definice

[[Náhodná-veličina|Náhodná veličina]] $X$ má **normální (Gaussovo) rozdělení** s parametry $\mu \in \mathbb{R}$ a $\sigma^2 > 0$, značíme $X \sim N(\mu, \sigma^2)$, má-li [[Hustota|hustotu]]
$$f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \qquad x \in \mathbb{R}.$$
Platí $\mathbb{E}X = \mu$, $\operatorname{var}X = \sigma^2$. [[Distribuční-funkce|Distribuční funkci]] nelze vyjádřit analyticky.

**Standardní normální rozdělení** $N(0,1)$ má distribuční funkci $\Phi$ (tabelovaná).

## Standardizace

$$X \sim N(\mu, \sigma^2) \;\Longrightarrow\; Z = \frac{X - \mu}{\sigma} \sim N(0, 1),$$
takže $F_X(x) = \Phi\!\bigl(\tfrac{x-\mu}{\sigma}\bigr)$. Obecně transformace $Z = (X-\mu)/\sigma$ dává $\mathbb{E}Z = 0$, $\operatorname{var}Z = 1$ pro libovolné rozdělení.

## Vlastnosti

- součet nezávislých normálních je normální: $\sum_{i=1}^n N(\mu, \sigma^2) \sim N(n\mu, n\sigma^2)$;
- klíčové pro statistiku: [[Centrální-limitní-věta|CLV]] činí z $N(0,1)$ limitní rozdělení standardizovaného [[Bodový-odhad|výběrového průměru]].

## Související

- [[Centrální-limitní-věta]]
- [[Kvantil]]
- [[Hustota]]
- [[Interval-spolehlivosti]]
