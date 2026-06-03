---
aliases: [lineární diskriminační analýza, lineární diskriminační analýzy, LDA, linear discriminant analysis, kvadratická diskriminační analýza, QDA, Gaussovská diskriminační analýza, Fisherova lineární diskriminační analýza, FLDA, diskriminační analýza]
tags: [definice, kurz/ML2]
---

# Lineární diskriminační analýza

## Definice

**Lineární diskriminační analýza** (angl. *linear discriminant analysis*, **LDA**) je generativní klasifikátor, který modeluje podmíněné rozdělení příznaků v každé třídě **vícerozměrným [[Normální-rozdělení|normálním rozdělením]]** se **společnou** varianční maticí:
$$X\mid Y=y\sim N(\mu_y,\Sigma).$$
Díky shodné $\Sigma$ se v aposteriorní pravděpodobnosti kvadratický člen zkrátí a MAP odhad porovnává výrazy **lineární v $x$**:
$$\mathrm P(Y=y\mid X=x)=\frac{e^{\beta_y^Tx+\gamma_y}}{\sum_c e^{\beta_c^Tx+\gamma_c}},\quad \beta_y=\Sigma^{-1}\mu_y,\ \gamma_y=-\tfrac12\mu_y^T\Sigma^{-1}\mu_y+\log\pi_y.$$
**Rozhodovací hranice je nadrovina.** Připouští-li se různé $\Sigma_y$ pro každou třídu, jde o **kvadratickou diskriminační analýzu (QDA)** s kvadratickou hranicí.

## Souvislost s logistickou regresí

Binárně: $\mathrm P(Y=1\mid x)=\sigma(w^Tx+w_0)$ s $w=\Sigma^{-1}(\mu_1-\mu_0)$ — **tentýž tvar jako [[Logistická-regrese|logistická regrese]]**, liší se jen trénováním: LDA generativně ([[Maximální-věrohodnost|MLE]] pro $\pi_y,\mu_y,\Sigma$), logistická regrese diskriminativně.

## Fisherova LDA

Týž směr $w$ lze najít optimalizačně (bez předpokladu normality): maximalizací poměru mezitřídního a vnitrotřídního rozptylu $J(w)=\frac{w^TS_Bw}{w^TS_Ww}$, což vede na $S_W^{-1}S_Bw=\lambda w$ a $w=S_W^{-1}(\hat\mu_1-\hat\mu_0)$ = LDA. Pro $C$ tříd slouží jako **redukce dimenzionality** (až $C-1$ příznaků optimálních pro separabilitu, na rozdíl od [[Analýza-hlavních-komponent|PCA]], která třídy ignoruje).

## Související

- [[Normální-rozdělení]]
- [[Logistická-regrese]]
- [[Bayesova-věta]]
- [[Analýza-hlavních-komponent]]
- [[Maximální-věrohodnost]]
