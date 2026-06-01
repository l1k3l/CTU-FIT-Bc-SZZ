---
aliases: [nezávislost náhodných veličin, nezávislost, nezávislé, nezávislých, nezávislými, nezávislé náhodné veličiny, nezávislá, i.i.d., independence]
tags: [definice, kurz/PST]
---

# Nezávislost náhodných veličin

## Definice

[[Náhodná-veličina|Náhodné veličiny]] $X, Y$ jsou **nezávislé**, pokud pro všechna $x, y \in \mathbb{R}$ jsou jevy $\{X \le x\}$ a $\{Y \le y\}$ nezávislé:
$$P(X \le x \cap Y \le y) = P(X \le x)\,P(Y \le y), \quad\text{tj.}\quad F_{X,Y}(x,y) = F_X(x)\,F_Y(y).$$
Obecně $X_1, \dots, X_n$ jsou nezávislé, jestliže $P(X \le x) = \prod_{i=1}^n P(X_i \le x_i)$ pro každé $x \in \mathbb{R}^n$.

## Kritéria

- **Diskrétní:** $P(X = x \cap Y = y) = P(X = x)\,P(Y = y)$ pro všechna $x, y$.
- **Spojité:** $f_{X,Y}(x,y) = f_X(x)\,f_Y(y)$ pro všechna $x, y$.
- **Faktorizace:** lze-li $f_{X,Y}(x,y) = g(x)\,h(y)$ (součin funkce jen $x$ a funkce jen $y$), pak jsou $X, Y$ nezávislé.

## Důsledky

- nezávislost $\Rightarrow$ **nekorelovanost** ($\operatorname{cov}(X,Y) = 0$); opačně ne;
- $\mathbb{E}(XY) = \mathbb{E}X\,\mathbb{E}Y$;
- $\operatorname{var}(X + Y) = \operatorname{var}X + \operatorname{var}Y$;
- hustota/pravděpodobnost součtu nezávislých veličin = **konvoluce**; součet nezávislých $N(\mu_i, \sigma_i^2)$ je opět normální.

## Související

- [[Náhodný-vektor]]
- [[Kovariance]]
- [[Korelace]]
- [[Náhodný-výběr]] (i.i.d. = nezávislé + stejně rozdělené)
