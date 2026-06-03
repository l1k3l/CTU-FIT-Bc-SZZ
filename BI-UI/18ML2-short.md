---
tags: [otázka, kurz/ML2, otázka/18, todo]
---

# 18 — Generativní modely: naivní Bayes, LDA (zkrácená verze)

## 1. Generativní vs. diskriminativní

- **Generativní:** modeluje sdružené $\mathrm P(X=x,Y=y)=\mathrm P(X=x\mid Y=y)\mathrm P(Y=y)$ → umí generovat data. (naivní Bayes, LDA/QDA)
- **Diskriminativní:** modeluje přímo $\mathrm P(Y=y\mid X=x)$. ([[Logistická-regrese|log. regrese]], NN, stromy)

## 2. Bayes + MAP

[[Bayesova-věta|Bayesova věta]]: $\mathrm P(Y=y\mid X=x)\propto\mathrm P(X=x\mid Y=y)\mathrm P(Y=y)$ (jmenovatel $\mathrm P(X=x)$ na $y$ nezávisí).
$$\hat Y=\arg\max_y\ \mathrm P(X=x\mid Y=y)\,\mathrm P(Y=y)\quad(\text{MAP}).$$

## 3. Naivní Bayes

**Předpoklad:** za $Y=y$ jsou příznaky [[Nezávislost-náhodných-veličin|nezávislé]]:
$$\hat Y=\arg\max_y\ \mathrm P(Y=y)\prod_{i=1}^p\mathrm P(X_i=x_i\mid Y=y).$$
Marginály se odhadují **separátně** → odolnost vůči prokletí dimenzionality. Předpoklad bývá nepravdivý, ale MAP často přesto správný.

**Marginály (MLE):** Bernoulli $\hat p_y=\frac{N_{1,y}}{N_{1,y}+N_{0,y}}$; kategorické $\hat p_{j,y}=\frac{N_{j,y}}{\sum_l N_{l,y}}$; spojité $N(\mu_y,\sigma_y^2)$ s MLE $\hat\mu_y,\hat\sigma_y^2$.

**Kolaps** ($N_{j,y}=0\Rightarrow$ odhad 0 → třída nikdy nepredikována). Řešení = **Bayesovský odhad** (apriori Beta) = **add-one / Laplace**: $\hat p_y=\frac{N_{1,y}+1}{N_{1,y}+N_{0,y}+2}$ (kategoricky $\frac{N_{j,y}+1}{\sum_l N_{l,y}+k}$).

(Texty: bag-of-words → multinomický model; log-sum-exp proti podtečení.)

## 4. Gaussovská DA → QDA → LDA

Vícerozm. [[Normální-rozdělení|normální]]: $f_X(x)\propto e^{-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)}$, $\Sigma_{ij}=\operatorname{cov}(X_i,X_j)$. Model $X\mid Y=y\sim N(\mu_y,\Sigma_y)$, MAP $\arg\max_y f_{X\mid y}(x)\pi_y$.

- **Σ_y různé** → porovnání **kvadratických** výrazů → **QDA** (kvadratická hranice). Σ_y diagonální = gaussovský naivní Bayes.
- **Σ_y = Σ stejné** → kvadratický člen se zkrátí, zůstane **lineární** v $x$:
$$\mathrm P(Y=y\mid x)=\frac{e^{\beta_y^Tx+\gamma_y}}{\sum_c e^{\beta_c^Tx+\gamma_c}},\quad \beta_y=\Sigma^{-1}\mu_y,\ \gamma_y=-\tfrac12\mu_y^T\Sigma^{-1}\mu_y+\log\pi_y.$$
→ **LDA**, hranice = **nadrovina**.

**Binárně:** $\mathrm P(Y=1\mid x)=\sigma(w^Tx+w_0)$, $w=\Sigma^{-1}(\mu_1-\mu_0)$ — **tvar logistické regrese**, jen trénováno generativně (MLE $\hat\pi_y,\hat\mu_y,\hat\Sigma$).

**Fisher LDA:** max $J(w)=\frac{w^TS_Bw}{w^TS_Ww}$ ($S_B$ mezitřídní, $S_W$ vnitrotřídní) → $S_W^{-1}S_Bw=\lambda w$ → $w=S_W^{-1}(\hat\mu_1-\hat\mu_0)$ = LDA. Pro $C$ tříd: redukce dimenze na $\le C-1$ (lepší pro klasifikaci než PCA).

---

## Co odpovědět rychle
- **MAP:** $\hat Y=\arg\max_y \mathrm P(X=x\mid Y=y)\mathrm P(Y=y)$ (Bayes, jmenovatel odpadá).
- **Naivní Bayes:** podmíněná nezávislost → součin marginál; odhady MLE + add-one (proti kolapsu).
- **QDA** = Gauss s různými Σ (kvadratická hranice); **LDA** = stejné Σ (lineární hranice).
- **LDA binárně** = $\sigma(w^Tx+w_0)$, $w=\Sigma^{-1}(\mu_1-\mu_0)$ — jako log. regrese, jiné trénování.
- **Fisher LDA:** max poměr mezi-/vnitrotřídního rozptylu → $w=S_W^{-1}(\hat\mu_1-\hat\mu_0)$.
