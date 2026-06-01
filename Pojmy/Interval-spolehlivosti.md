---
aliases: [interval spolehlivosti, intervalu spolehlivosti, intervalem spolehlivosti, intervaly spolehlivosti, intervalů spolehlivosti, konfidenční interval, konfidenčního intervalu, intervalový odhad, intervalové odhady, hladina spolehlivosti, confidence interval]
tags: [definice, kurz/PST]
---

# Interval spolehlivosti

## Definice

Nechť $X_1, \dots, X_n$ je [[Náhodný-výběr|náhodný výběr]] z rozdělení s parametrem $\theta$. Interval $(L, U)$ s mezemi danými statistikami $L = L(X)$, $U = U(X)$ takový, že
$$P(L < \theta < U) = 1 - \alpha,$$
je **$100(1-\alpha)\%$ interval spolehlivosti** (konfidenční interval); $1-\alpha$ je **hladina spolehlivosti**. Pro **oboustranný** symetrický interval volíme $P(\theta < L) = P(U < \theta) = \alpha/2$. **Jednostranné** intervaly $(L, +\infty)$ resp. $(-\infty, U)$.

## Obecný postup

1. najdi **pivotovou statistiku** $H(\theta)$ závisející na $\theta$ i na výběru, se **známým rozdělením**;
2. najdi meze $h_L, h_U$ s $P(h_L < H(\theta) < h_U) = 1-\alpha$;
3. úpravou nerovností osamostatni $\theta$.

## Intervaly pro střední hodnotu $\mu$ ($N(\mu,\sigma^2)$)

- **známý $\sigma^2$:** $\bar X_n \pm z_{\alpha/2}\,\dfrac{\sigma}{\sqrt n}$, $\;z_{\alpha/2}$ kritická hodnota [[Normální-rozdělení|$N(0,1)$]];
- **neznámý $\sigma^2$:** $\bar X_n \pm t_{\alpha/2,\,n-1}\,\dfrac{s_n}{\sqrt n}$, $\;t$ kritická hodnota Studentova rozdělení ($n-1$ st. volnosti), neboť $\frac{\bar X_n-\mu}{s_n/\sqrt n}\sim t_{n-1}$.

Pro nenormální data lze tytéž intervaly použít **přibližně** při velkém $n$ ([[Centrální-limitní-věta|CLV]]).

## Interval pro rozptyl $\sigma^2$ ($N(\mu,\sigma^2)$)

$\left(\dfrac{(n-1)s_n^2}{\chi^2_{\alpha/2,n-1}},\ \dfrac{(n-1)s_n^2}{\chi^2_{1-\alpha/2,n-1}}\right)$, neboť $\frac{(n-1)s_n^2}{\sigma^2}\sim\chi^2_{n-1}$ (jen pro normální rozdělení).

## Související

- [[Bodový-odhad]]
- [[Testování-hypotéz]]
- [[Normální-rozdělení]]
- [[Centrální-limitní-věta]]
