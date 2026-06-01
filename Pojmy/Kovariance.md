---
aliases: [kovariance, kovarianci, kovariancí, kovariancemi, covariance, cov, výběrová kovariance]
tags: [definice, kurz/PST]
---

# Kovariance

## Definice

Pro [[Náhodná-veličina|náhodné veličiny]] $X, Y$ s konečnými druhými momenty je **kovariance**
$$\operatorname{cov}(X, Y) = \mathbb{E}\bigl[(X - \mathbb{E}X)(Y - \mathbb{E}Y)\bigr] = \mathbb{E}[XY] - \mathbb{E}X\,\mathbb{E}Y.$$
Měří míru **lineární** závislosti $X$ a $Y$ (v původních jednotkách). Normovanou, bezrozměrnou verzí je [[Korelace|korelační koeficient]].

## Vlastnosti

- $\operatorname{cov}(X, X) = \operatorname{var}X$;
- symetrie: $\operatorname{cov}(X,Y) = \operatorname{cov}(Y,X)$;
- bilinearita: $\operatorname{cov}(aX + b, cY + d) = ac\,\operatorname{cov}(X,Y)$;
- $\operatorname{var}(aX + bY) = a^2\operatorname{var}X + b^2\operatorname{var}Y + 2ab\,\operatorname{cov}(X,Y)$.

## Nekorelovanost

$X, Y$ jsou **nekorelované**, pokud $\operatorname{cov}(X,Y) = 0$ (ekvivalentně $\mathbb{E}[XY] = \mathbb{E}X\,\mathbb{E}Y$).

**Věta:** [[Nezávislost-náhodných-veličin|Nezávislost]] $\Rightarrow$ nekorelovanost. Opačná implikace **neplatí** (nekorelovanost zachytí jen lineární vztah).

## Související

- [[Korelace]]
- [[Rozptyl]]
- [[Nezávislost-náhodných-veličin]]
- [[Náhodný-vektor]]
