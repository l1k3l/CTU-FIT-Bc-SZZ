---
aliases: [bodový odhad, bodového odhadu, bodovým odhadem, bodové odhady, bodových odhadů, odhad, statistika, výběrový průměr, výběrového průměru, výběrový rozptyl, výběrová směrodatná odchylka, nestrannost, nestranný odhad, konzistence, konzistentní odhad, point estimate]
tags: [definice, kurz/PST]
---

# Bodový odhad

## Definice

**Bodový odhad** parametru $\theta$ je **statistika** $\hat\theta_n = \hat\theta_n(X_1, \dots, X_n)$ — funkce [[Náhodný-výběr|náhodného výběru]], která nezávisí na $\theta$. Jakožto funkce náhodných veličin je sám náhodnou veličinou.

## Nejužívanější odhady

- **výběrový průměr** (odhad [[Střední-hodnota|střední hodnoty]] $\mu$): $\displaystyle \bar X_n = \frac1n\sum_{i=1}^n X_i$;
- **výběrový rozptyl** (odhad [[Rozptyl|rozptylu]] $\sigma^2$): $\displaystyle s_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar X_n)^2$ (dělení $n-1$ kvůli nestrannosti);
- výběrová [[Kovariance|kovariance]] $s_{X,Y}$, výběrový [[Korelace|korelační koeficient]] $r$.

## Vlastnosti odhadu

- **nestrannost (nevychýlenost):** $\mathbb{E}\hat\theta_n = \theta$ pro všechna $\theta$ (bez systematické chyby);
- **konzistence:** $\hat\theta_n \xrightarrow{P} \theta$ pro $n \to \infty$. Postačující podmínka: $\mathbb{E}\hat\theta_n \to \theta$ a $\operatorname{var}\hat\theta_n \to 0$;
- **nejlepší nestranný odhad** = nestranný s nejmenším rozptylem (mez Rao–Cramér).

$\bar X_n$ je nestranný a konzistentní odhad $\mu$ ($\mathbb{E}\bar X_n = \mu$, $\operatorname{var}\bar X_n = \sigma^2/n$); $s_n^2$ je nestranný a konzistentní odhad $\sigma^2$.

## Metody konstrukce

- **metoda momentů** — položíme výběrové momenty rovny teoretickým a vyřešíme pro $\theta$;
- **[[Maximální-věrohodnost|metoda maximální věrohodnosti]] (MLE)** — maximalizujeme věrohodnostní funkci $L(\theta; x) = \prod_i f_\theta(x_i)$.

## Související

- [[Náhodný-výběr]]
- [[Interval-spolehlivosti]]
- [[Zákon-velkých-čísel]]
- [[Střední-hodnota]]
