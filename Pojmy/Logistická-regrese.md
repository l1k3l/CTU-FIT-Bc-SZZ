---
aliases: [logistická regrese, logistické regrese, logistickou regresí, logistické regresi, logistickou regresi, logistická regresní, logistický regresní model, sigmoida, logistická funkce]
tags: [definice, kurz/ML1]
---

# Logistická regrese

## Definice

**Logistická regrese** je parametrický model pro **binární klasifikaci**. Pro binární vysvětlovanou proměnnou $Y \in \{0,1\}$, vektor příznaků $x = (1, x_1,\dots,x_p)^T$ (s interceptem $x_0 = 1$) a koeficienty $w = (w_0,\dots,w_p)^T$ modeluje pravděpodobnost třídy $1$ jako lineární kombinaci příznaků protlačenou **sigmoidou**:
$$\mathrm{P}(Y=1 \mid x, w) = \sigma(w^T x) = \frac{1}{1 + e^{-w^T x}}, \qquad \mathrm{P}(Y=0 \mid x, w) = 1 - \sigma(w^T x).$$
Predikce se řídí pravidlem $\hat Y = \mathbb{1}[\,\sigma(w^T x) > \tfrac12\,]$; rozhodovací hranice $w^T x = 0$ je **nadrovina** (lineární klasifikátor). **Logit** (log-odds) je lineární v příznacích: $\ln\frac{\hat p}{1-\hat p} = w^T x$.

## Trénování

Parametry $w$ se odhadují metodou [[Maximální-věrohodnost|maximální věrohodnosti]] (MLE) — maximalizací $L(w) = \prod_i \hat p_i^{\,Y_i}(1-\hat p_i)^{1-Y_i}$, ekvivalentně minimalizací binární křížové entropie. Účelová funkce je [[Konvexní-funkce|konvexní]], nemá uzavřené řešení — řeší se numericky (gradientní vzestup, Newton / IRLS).

## Související

- [[Lineární-regrese]]
- [[Maximální-věrohodnost]]
- [[Bodový-odhad]]
