---
aliases: [posloupnost, posloupnosti, posloupností, posloupnostem, posloupnostech, posloupnostmi, vybraná posloupnost, podposloupnost, podposloupnosti, konvergentní, divergentní, sequence, subsequence]
tags: [definice, kurz/MA1]
---

# Posloupnost

## Definice

**Reálná (číselná) posloupnost** je zobrazení $a : \mathbb{N} \to \mathbb{R}$. Hodnotu $a(n)$ značíme $a_n$ ($n$-tý člen) a celou posloupnost $(a_n)_{n=1}^{\infty}$. (V tomto textu jsou posloupnosti vždy nekonečné.)

## Základní vlastnosti

- **Monotonie:** $(a_n)$ je **rostoucí** ($a_n \le a_{n+1}$), **klesající** ($a_n \ge a_{n+1}$), **ostře** rostoucí/klesající (s ostrou nerovností). Monotónní = rostoucí nebo klesající; **ryze monotónní** = ostře rostoucí nebo ostře klesající.
- **Omezenost:** $(a_n)$ je **omezená**, právě když $\exists K > 0\ \forall n: |a_n| < K$.
- **Konstantní:** $\exists c\ \forall n: a_n = c$ (⟺ rostoucí i klesající zároveň).

## Hromadný bod posloupnosti

$\alpha \in \mathbb{R}^*$ je **hromadný bod** $(a_n)$, právě když v každém okolí $\alpha$ leží **nekonečně mnoho** členů posloupnosti. (Liší se od hromadného bodu množiny — záleží na opakování členů.)

## Vybraná posloupnost (podposloupnost)

Je-li $(k_n)$ **ostře rostoucí** posloupnost přirozených čísel, je $(a_{k_n})_{n=1}^{\infty}$ **vybraná** z $(a_n)$. Bod $\alpha$ je hromadným bodem $(a_n)$ ⟺ existuje vybraná posloupnost s [[Limita-posloupnosti|limitou]] $\alpha$.

## Konvergence

$(a_n)$ je **konvergentní**, právě když $\lim_{n\to\infty} a_n \in \mathbb{R}$ (konečná limita); jinak **divergentní**.

- **Bolzano–Weierstrass:** každá omezená posloupnost má hromadný bod (lze z ní vybrat konvergentní podposloupnost).
- **O limitě monotónní posloupnosti:** každá monotónní posloupnost má limitu; je konečná ⟺ posloupnost je omezená.
- **Bolzano–Cauchy:** $(a_n)$ konverguje ⟺ $\forall \varepsilon > 0\ \exists N\ \forall n,m > N: |a_n - a_m| < \varepsilon$.

## Související

- [[Limita-posloupnosti]]
- [[Limita-funkce]]
- [[Asymptotická-notace]]
