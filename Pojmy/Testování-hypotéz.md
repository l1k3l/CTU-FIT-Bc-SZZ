---
aliases: [testování hypotéz, test hypotézy, testování hypotézy, hypotéza, hypotézy, nulová hypotéza, alternativní hypotéza, hladina významnosti, chyba prvního druhu, chyba druhého druhu, síla testu, p-hodnota, kritický obor, testová statistika, hypothesis testing]
tags: [definice, kurz/PST]
---

# Testování hypotéz

## Pojmy

Mějme [[Náhodný-výběr|náhodný výběr]] z rozdělení. **Hypotéza** je tvrzení o tomto rozdělení.
- **Nulová hypotéza** $H_0$ — tvrzení, které testujeme;
- **Alternativní hypotéza** $H_A$ — opačné tvrzení.

Za $H_0$ volíme tu, jejíž neoprávněné zamítnutí je závažnější; tvrzení, které chceme prokázat, je $H_A$ (zamítnutí $H_0$ je „silný" výsledek). Typy: **parametrické** (o hodnotě $\theta$) a **neparametrické** (o tvaru rozdělení — testy dobré shody).

## Chyby

| | $H_0$ platí | $H_0$ neplatí |
|---|---|---|
| zamítáme $H_0$ | **chyba 1. druhu** ($\alpha$) | správně |
| nezamítáme $H_0$ | správně | **chyba 2. druhu** ($\beta$) |

**Hladina významnosti** $\alpha$ = max. přípustná pravděpodobnost chyby 1. druhu (typicky $5\%$ či $1\%$). **Síla testu** $= 1 - \beta$. **p-hodnota** = nejmenší $\alpha$, na níž lze $H_0$ zamítnout.

## Test pomocí intervalu spolehlivosti

Pro $H_0: \theta = \theta_0$ sestrojíme $100(1-\alpha)\%$ [[Interval-spolehlivosti|interval spolehlivosti]] odpovídající alternativě a **zamítneme $H_0$, pokud $\theta_0$ v intervalu neleží**. Pravděpodobnost chyby 1. druhu je pak právě $\alpha$. (Oboustranná $H_A: \theta \ne \theta_0$ → oboustranný interval; jednostranná → jednostranný.)

Ekvivalentně lze použít **testovou statistiku** $T$ a **kritický obor** $W_\alpha$ (zamítneme, je-li $T \in W_\alpha$).

## Související

- [[Interval-spolehlivosti]]
- [[Bodový-odhad]]
- [[Náhodný-výběr]]
- [[Normální-rozdělení]]
