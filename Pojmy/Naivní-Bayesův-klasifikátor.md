---
aliases: [naivní Bayes, naivního Bayese, naivní Bayesův klasifikátor, naivního Bayesova klasifikátoru, Naive Bayes, gaussovský naivní Bayes, add-one smoothing, Laplaceovo vyhlazení, MAP odhad]
tags: [definice, kurz/ML2]
---

# Naivní Bayesův klasifikátor

## Definice

**Naivní Bayesův klasifikátor** (angl. *Naive Bayes*) je generativní klasifikátor založený na [[Bayesova-věta|Bayesově větě]] a **naivním předpokladu**, že za podmínky třídy $Y=y$ jsou všechny příznaky **[[Nezávislost-náhodných-veličin|nezávislé]]**:
$$\mathrm P(X=x\mid Y=y)=\prod_{i=1}^p\mathrm P(X_i=x_i\mid Y=y).$$
Predikce je MAP odhad
$$\hat Y=\arg\max_{y}\ \mathrm P(Y=y)\prod_{i=1}^p\mathrm P(X_i=x_i\mid Y=y).$$

## Modely marginál a odhady

Marginálu $\mathrm P(X_i\mid Y=y)$ modelujeme podle typu příznaku, parametry odhadujeme [[Maximální-věrohodnost|MLE]]:

- **binární** → $\mathrm{Be}(p_y)$, $\hat p_y=\frac{N_{1,y}}{N_{1,y}+N_{0,y}}$;
- **kategorický** → $\mathrm{Cat}(p_y)$, $\hat p_{j,y}=\frac{N_{j,y}}{\sum_l N_{l,y}}$;
- **spojitý** → $N(\mu_y,\sigma_y^2)$ (gaussovský naivní Bayes).

**Kolaps:** chybí-li hodnota v trénovacích datech ($N_{j,y}=0$), je odhad 0 → třída se nikdy nepredikuje. Řešení = **add-one / Laplaceovo vyhlazení** (Bayesovský odhad s rovnoměrným apriori): $\hat p_y=\frac{N_{1,y}+1}{N_{1,y}+N_{0,y}+2}$.

## Vlastnosti

Předpoklad nezávislosti je obvykle nepravdivý, přesto NB často funguje dobře: marginály se odhadují separátně (odolnost vůči prokletí dimenzionality) a pro správný MAP stačí, aby skutečná třída měla nejvyšší pravděpodobnost. Časté použití: klasifikace textů (bag-of-words, multinomický model).

## Související

- [[Bayesova-věta]]
- [[Nezávislost-náhodných-veličin]]
- [[Maximální-věrohodnost]]
- [[Lineární-diskriminační-analýza]]
