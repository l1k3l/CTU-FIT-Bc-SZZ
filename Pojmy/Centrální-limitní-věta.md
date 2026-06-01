---
aliases: [centrální limitní věta, centrální limitní věty, centrální limitní větou, CLV, CLT, central limit theorem, konvergence v distribuci]
tags: [věta, kurz/PST]
---

# Centrální limitní věta

## Znění

Nechť $X_1, X_2, \dots$ je posloupnost [[Nezávislost-náhodných-veličin|i.i.d.]] [[Náhodná-veličina|náhodných veličin]] s konečnou [[Střední-hodnota|střední hodnotou]] $\mathbb{E}X_i = \mu$ a konečným kladným [[Rozptyl|rozptylem]] $\operatorname{var}X_i = \sigma^2 > 0$. Pak standardizovaný [[Bodový-odhad|výběrový průměr]] konverguje **v distribuci** ke standardnímu [[Normální-rozdělení|normálnímu rozdělení]]:
$$\frac{\bar X_n - \mu}{\sigma/\sqrt{n}} \xrightarrow{\;D\;} N(0,1) \qquad (n \to \infty).$$
Ekvivalentně pro součet $S_n = \sum_i X_i$: $\dfrac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{D} N(0,1)$.

## Konvergence v distribuci

$X_n \xrightarrow{D} X$, jestliže $F_{X_n}(x) \to F_X(x)$ ve všech bodech spojitosti $F_X$.

## Význam

- Platí **bez ohledu** na rozdělení sčítaných veličin (stačí konečný rozptyl).
- Umožňuje pro **velká $n$** ($n \gtrsim 30$–$50$) sestavit přibližné [[Interval-spolehlivosti|intervaly spolehlivosti]] a [[Testování-hypotéz|testy]] o střední hodnotě i pro nenormální data.
- Souvisí se [[Zákon-velkých-čísel|zákonem velkých čísel]] (ten dává $\bar X_n \to \mu$; CLV popisuje *rychlost* a tvar fluktuací kolem $\mu$).

## Související

- [[Normální-rozdělení]]
- [[Bodový-odhad]]
- [[Interval-spolehlivosti]]
