---
aliases: [náhodný vektor, náhodného vektoru, náhodným vektorem, náhodné vektory, náhodných vektorů, sdružené rozdělení, sdružená distribuční funkce, marginální rozdělení, podmíněné rozdělení, random vector]
tags: [definice, kurz/PST]
---

# Náhodný vektor

## Definice

**Náhodný vektor** je $n$-tice [[Náhodná-veličina|náhodných veličin]] $X = (X_1, \dots, X_n)$ na témž pravděpodobnostním prostoru. Jeho **sdružená distribuční funkce** je
$$F_X(x) = P(X_1 \le x_1 \cap \dots \cap X_n \le x_n).$$
Pro dvojici: $F_{X,Y}(x,y) = P(X \le x \cap Y \le y)$.

## Popis rozdělení (pro $(X,Y)$)

- **Sdružená pravděpodobnostní funkce** (diskrétní): $P(X = x \cap Y = y)$, normalizace $\sum_{x,y} = 1$.
- **Sdružená [[Hustota|hustota]]** (spojité): $f_{X,Y} \ge 0$, $F_{X,Y}(x,y) = \int_{-\infty}^y\int_{-\infty}^x f_{X,Y}$, $\int\int f_{X,Y} = 1$, $f_{X,Y} = \partial^2 F_{X,Y}/\partial x\,\partial y$.

## Marginální rozdělení

Rozdělení jedné složky bez ohledu na druhou:
$$P(X = x) = \sum_{y} P(X = x \cap Y = y), \qquad f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y)\,dy.$$

## Podmíněné rozdělení

$\displaystyle P(X = x \mid Y = y) = \frac{P(X = x \cap Y = y)}{P(Y = y)}$, resp. podmíněná hustota $\displaystyle f_{X\mid Y}(x\mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}$ (pro $f_Y(y) > 0$). Podmíněná střední hodnota $\mathbb{E}(X \mid Y=y)$.

## Související

- [[Nezávislost-náhodných-veličin]]
- [[Kovariance]]
- [[Korelace]]
- [[Náhodná-veličina]]
