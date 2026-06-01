---
aliases: [zákon velkých čísel, zákona velkých čísel, zákonem velkých čísel, slabý zákon velkých čísel, silný zákon velkých čísel, ZVČ, SZVČ, LLN, Čebyševova nerovnost, Markovova nerovnost]
tags: [věta, kurz/PST]
---

# Zákon velkých čísel

## Znění

Nechť $X_1, X_2, \dots$ jsou [[Nezávislost-náhodných-veličin|i.i.d.]] [[Náhodná-veličina|náhodné veličiny]] se [[Střední-hodnota|střední hodnotou]] $\mathbb{E}X_i = \mu$. Pak [[Bodový-odhad|výběrový průměr]] $\bar X_n = \tfrac1n\sum_i X_i$ konverguje k $\mu$:

- **Slabý ZVČ** (konečný [[Rozptyl|rozptyl]] $\sigma^2$): $\bar X_n \xrightarrow{P} \mu$, tj. $\forall \varepsilon>0:\ \lim_{n\to\infty} P(|\bar X_n - \mu| \ge \varepsilon) = 0$.
- **Silný ZVČ** (stačí existence $\mu$): $\bar X_n \xrightarrow{\text{s.j.}} \mu$ (konvergence skoro jistě).

## Pomocné nerovnosti

- **Markovova:** pro $X \ge 0$ a $a > 0$ je $P(X \ge a) \le \dfrac{\mathbb{E}X}{a}$.
- **Čebyševova:** $P(|X - \mathbb{E}X| \ge \varepsilon) \le \dfrac{\operatorname{var}X}{\varepsilon^2}$.

Slabý ZVČ plyne z Čebyševovy nerovnosti pro $\bar X_n$ (kde $\operatorname{var}\bar X_n = \sigma^2/n \to 0$).

## Význam

ZVČ zaručuje **konzistenci** výběrového průměru jako [[Bodový-odhad|odhadu]] střední hodnoty. Doplňuje jej [[Centrální-limitní-věta|centrální limitní věta]], která popisuje rozdělení fluktuací $\bar X_n$ kolem $\mu$.

## Související

- [[Centrální-limitní-věta]]
- [[Bodový-odhad]]
- [[Střední-hodnota]]
