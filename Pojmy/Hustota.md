---
aliases: [hustota, hustotu, hustoty, hustotě, hustotou, hustot, hustota pravděpodobnosti, sdružená hustota, density, probability density]
tags: [definice, kurz/PST]
---

# Hustota

## Definice

[[Náhodná-veličina|Náhodná veličina]] $X$ je **(absolutně) spojitá**, existuje-li nezáporná funkce $f_X$ (**hustota pravděpodobnosti**) taková, že
$$F_X(x) = \int_{-\infty}^{x} f_X(t)\,dt \qquad \forall x \in \mathbb{R}.$$

## Vlastnosti

- **normalizace:** $\displaystyle\int_{-\infty}^{+\infty} f_X(x)\,dx = 1$;
- $P(X = x) = 0$ pro všechna $x$ (proto $P(a < X \le b) = P(a \le X \le b) = \dots$);
- $f_X(x) = F_X'(x)$ v bodech, kde derivace existuje;
- $\displaystyle P(a < X \le b) = \int_a^b f_X(x)\,dx = F_X(b) - F_X(a)$;
- obecně $\displaystyle P(X \in B) = \int_B f_X(x)\,dx$;
- interpretace: $f_X(x)\,dx \approx P(x < X < x + dx)$ pro malé $dx$.

## Související

- [[Distribuční-funkce]]
- [[Náhodná-veličina]]
- [[Pravděpodobnostní-funkce]] (diskrétní analogie)
- [[Náhodný-vektor]] (sdružená hustota $f_{X,Y}$)
