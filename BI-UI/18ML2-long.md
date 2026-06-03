---
tags: [otázka, kurz/ML2, otázka/18, todo]
---

# Generativní modely — naivní Bayes a LDA

> **Otázka SZZ:** Generativní modely – naivní Bayes, lineární diskriminační analýza.

Zdroje: BI-ML2 (FIT ČVUT), přednášky 5 a 6 — Klasifikace pomocí podmíněné pravděpodobnosti (Bayesova věta, MAP), Naivní Bayesův klasifikátor a modely marginálních rozdělení, Generativní vs. diskriminativní přístup, Gaussovská/kvadratická diskriminační analýza, Lineární diskriminační analýza (LDA, Fisherova LDA).

Značení: $X=(X_1,\dots,X_p)^T$ náhodný vektor příznaků, $Y$ diskrétní vysvětlovaná proměnná s oborem $\mathcal Y$, $\pi_y=\mathrm P(Y=y)$, $N_y$ počet bodů třídy $y$, $\mu_y,\Sigma_y$ střední vektor a varianční matice třídy $y$.

---

## 1. Generativní vs. diskriminativní přístup

Klasifikaci $\hat Y=\arg\max_y\mathrm P(Y=y\mid X=x)$ (tzv. **MAP odhad**, *maximum a posteriori*) lze stavět dvěma způsoby:

- **Generativní přístup** — modeluje **sdruženou** pravděpodobnost $\mathrm P(X=x,Y=y)=\mathrm P(X=x\mid Y=y)\,\mathrm P(Y=y)$, tj. odhaduje $\mathrm P(X=x\mid Y=y)$ a $\mathrm P(Y=y)$. Obsahuje úplnou informaci o rozdělení, ze kterého data vznikla → umí i **generovat** nová pozorování. Patří sem **naivní Bayes**, **(L)DA**.
- **Diskriminativní přístup** — modeluje **přímo** $\mathrm P(Y=y\mid X=x)$ (nebo rovnou predikuje $Y$) bez modelu sdruženého rozdělení. Patří sem **[[Logistická-regrese|logistická regrese]]**, **neuronové sítě**, (v širším smyslu) **rozhodovací stromy**. Většina dnes nejpoužívanějších metod je tohoto typu.

---

## 2. Klasifikace přes podmíněnou pravděpodobnost (Bayesova věta)

Chceme $\mathrm P(Y=y\mid X=x)$. Generativně použijeme **[[Bayesova-věta|Bayesovu větu]]**:
$$\mathrm P(Y=y\mid X=x)=\frac{\mathrm P(X=x\mid Y=y)\,\mathrm P(Y=y)}{\mathrm P(X=x)},\qquad \mathrm P(X=x)=\sum_{y\in\mathcal Y}\mathrm P(X=x\mid Y=y)\,\mathrm P(Y=y).$$
Jmenovatel $\mathrm P(X=x)$ **nezávisí na $y$**, proto pro MAP odhad odpadá:
$$\mathrm P(Y=y\mid X=x)\propto \mathrm P(X=x\mid Y=y)\,\mathrm P(Y=y),\qquad \boxed{\ \hat Y=\arg\max_{y\in\mathcal Y}\mathrm P(X=x\mid Y=y)\,\mathrm P(Y=y).\ }$$
Odhad $\mathrm P(Y=y)$ je triviální (podíl tříd); problém je odhadnout $\mathrm P(X=x\mid Y=y)$ ve vysoké dimenzi.

---

## 3. Naivní Bayesův klasifikátor

**Naivní předpoklad:** za podmínky $Y=y$ jsou všechny příznaky **[[Nezávislost-náhodných-veličin|nezávislé]]**:
$$\mathrm P(X=x\mid Y=y)=\prod_{i=1}^p\mathrm P(X_i=x_i\mid Y=y).$$
**MAP odhad naivního Bayese:**
$$\hat Y=\arg\max_{y\in\mathcal Y}\ \mathrm P(Y=y)\prod_{i=1}^p\mathrm P(X_i=x_i\mid Y=y).$$

**Vlastnosti.** Předpoklad nezávislosti je obvykle nepravdivý, přesto NB často funguje velmi dobře:

- Rozklad na **marginály** příznaky **separuje** → každou $\mathrm P(X_i=x_i\mid Y=y)$ odhadujeme nezávisle na ostatních. To **odolává prokletí dimenzionality**: na rozumný odhad marginály stačí málo dat a počet potřebných dat neroste s počtem příznaků.
- Odhad sdruženého $\mathrm P(X=x\mid Y=y)$ bývá špatný, ale **nám jde jen o MAP** — ten zůstane správný, pokud skutečná třída dostane nejvyšší (byť nepřesnou) pravděpodobnost. To je častá situace.

---

## 4. Modely marginálních rozdělení a jejich odhad

Marginálu $\mathrm P(X_i\mid Y=y)$ modelujeme podle typu příznaku; parametry odhadujeme **[[Maximální-věrohodnost|maximální věrohodností]]** (MLE):

| Příznak | Model | MLE odhad | Bayesovský (smoothed) odhad |
|---|---|---|---|
| binární $\{0,1\}$ | $\mathrm{Be}(p_y)$ | $\hat p_y=\dfrac{N_{1,y}}{N_{1,y}+N_{0,y}}$ | $\dfrac{N_{1,y}+1}{N_{1,y}+N_{0,y}+2}$ |
| kategorický ($k$ hodnot) | $\mathrm{Cat}(p_y)$ | $\hat p_{j,y}=\dfrac{N_{j,y}}{\sum_l N_{l,y}}$ | $\dfrac{N_{j,y}+1}{\sum_l N_{l,y}+k}$ |
| spojitý | $N(\mu_y,\sigma_y^2)$ | $\hat\mu_y=\tfrac1{N_y}\sum x_i,\ \hat\sigma_y^2=\tfrac1{N_y}\sum(x_i-\hat\mu_y)^2$ | — |

**Problém kolapsu.** Nevyskytne-li se hodnota v trénovací množině třídy $y$ ($N_{j,y}=0$), je MLE odhad $0$ → celý součin pro tu třídu je $0$ a MAP tu třídu **nikdy** nepredikuje (bez ohledu na ostatní příznaky).

**Bayesovský odhad (řešení kolapsu).** Místo frekventistického odhadu zavedeme **apriorní rozdělení** parametru (znalost před daty), např. **Beta** pro Bernoulliho. Bayesovou větou získáme **aposteriorní rozdělení** $f_p(p\mid x)\propto \mathrm P(X=x\mid p)f_p(p)$ a bodový odhad jako jeho střední hodnotu. Pro rovnoměrné apriori (Beta(1,1)) vyjde
$$\hat p_y=\frac{N_{1,y}+1}{N_{1,y}+N_{0,y}+2}\quad(\textbf{add-one / Laplaceovo vyhlazení}),$$
které na kolaps netrpí. U spojitého příznaku se nejčastěji bere **Gaussovo** rozdělení (GaussianNB).

*Aplikace — klasifikace textů (bag-of-words).* Dokument = vektor četností slov ze slovníku $D$; třídu modeluje **multinomické** rozdělení s $\hat p_{j,y}=\frac{N_{j,y}}{N_y}$ (resp. add-one $\frac{N_{j,y}+1}{N_y+|D|}$). Numericky se počítá v logaritmech (součin → součet log) a normalizace se řeší **log-sum-exp trikem** $\log\sum_y e^{-b_y}=-B+\log\sum_y e^{B-b_y}$, $B=\min_y b_y$, proti podtečení.

---

## 5. Gaussovská a kvadratická diskriminační analýza (QDA)

Pro spojité příznaky modelujeme sdružené $X\mid Y=y$ **vícerozměrným [[Normální-rozdělení|normálním rozdělením]]**.

**Definice (vícerozměrné normální rozdělení).** Pro $\mu\in\mathbb R^p$ a symetrickou PSD $\Sigma\in\mathbb R^{p,p}$ má **[[Náhodný-vektor|náhodný vektor]]** $X\sim N(\mu,\Sigma)$, právě když $c^TX\sim N(c^T\mu,c^T\Sigma c)$ pro každé $c$. Pro pozitivně definitní $\Sigma$ je to spojité rozdělení s hustotou
$$f_X(x)=\frac{1}{(2\pi)^{p/2}|\Sigma|^{1/2}}\,e^{-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)},\qquad \mathrm E\,X_i=\mu_i,\ \Sigma_{ij}=\operatorname{cov}(X_i,X_j).$$

**Gaussovská diskriminační analýza:** $X\mid Y=y\sim N(\mu_y,\Sigma_y)$, MAP $\hat Y=\arg\max_y f_{X\mid y}(x)\,\pi_y$. Při dosazení hustoty se porovnávají **kvadratické** výrazy $(x-\mu_y)^T\Sigma_y^{-1}(x-\mu_y)$ → **kvadratická diskriminační analýza (QDA)**, hranice jsou kvadriky. (Je-li $\Sigma_y$ diagonální, jsou příznaky nezávislé → speciální případ **gaussovský naivní Bayes**.)

MLE odhady: $\hat\pi_y=\frac{N_y}{N}$, $\hat\mu_y=\frac1{N_y}\sum_{i:y_i=y}x_i$, $\hat\Sigma_y=\frac1{N_y}\sum_{i:y_i=y}(x_i-\hat\mu_y)(x_i-\hat\mu_y)^T$.

---

## 6. Lineární diskriminační analýza (LDA)

**Speciální případ:** všechny třídy mají **stejnou** varianční matici $\Sigma_y=\Sigma$. Pak se v hustotě člen $(2\pi)^{-p/2}|\Sigma|^{-1/2}e^{-\frac12 x^T\Sigma^{-1}x}$ na $y$ **nezávisí** a ve zlomku se zkrátí. Po zavedení
$$\beta_y=\Sigma^{-1}\mu_y,\qquad \gamma_y=-\tfrac12\mu_y^T\Sigma^{-1}\mu_y+\log\pi_y$$
dostaneme **softmax** lineárních výrazů
$$\mathrm P(Y=y\mid X=x)=\frac{e^{\beta_y^Tx+\gamma_y}}{\sum_{c}e^{\beta_c^Tx+\gamma_c}}.$$
MAP tak porovnává výrazy **lineární v $x$** → **lineární diskriminační analýza (LDA)**, **rozhodovací hranice je nadrovina** $(\beta_y-\beta_{y'})^Tx=\gamma_{y'}-\gamma_y$.

**Souvislost s logistickou regresí (binárně, třídy 0/1).**
$$\mathrm P(Y=1\mid X=x)=\sigma(w^Tx+w_0),\quad w=\Sigma^{-1}(\mu_1-\mu_0),\quad w_0=-\tfrac12 w^T(\mu_1+\mu_0)+\log\tfrac{\pi_1}{\pi_0}.$$
Tentýž tvar jako **[[Logistická-regrese|logistická regrese]]** — liší se jen **trénováním**: LDA generativně (MLE pro $\pi_y,\mu_y,\Sigma$), logistická regrese diskriminativně.

MLE odhady LDA: $\hat\pi_y=\frac{N_y}{N}$, $\hat\mu_y=\frac1{N_y}\sum_{i:y_i=y}x_i$, sdílená $\hat\Sigma=\frac1N\sum_y\sum_{i:y_i=y}(x_i-\hat\mu_y)(x_i-\hat\mu_y)^T$.

### 6.1 Fisherova LDA (FLDA) — optimalizační pohled

K témuž směru $w$ lze dojít i bez předpokladu normality — analogicky PCA, projekcí do směru $w$ tak, aby data byla **dobře separovatelná**. Pro binární klasifikaci hledáme $w$ maximalizující odstup projektovaných průměrů při malých rozptylech tříd:
$$J(w)=\frac{(m_1-m_0)^2}{s_0^2+s_1^2}=\frac{w^TS_Bw}{w^TS_Ww},$$
kde **mezitřídní** $S_B=(\hat\mu_1-\hat\mu_0)(\hat\mu_1-\hat\mu_0)^T$ a **vnitrotřídní** $S_W=\sum_{i:y_i=0}(x_i-\hat\mu_0)(x_i-\hat\mu_0)^T+\sum_{i:y_i=1}(x_i-\hat\mu_1)(x_i-\hat\mu_1)^T$. Maximum řeší zobecněný problém vlastních čísel $S_W^{-1}S_Bw=\lambda w$, odkud (až na konstantu)
$$w=S_W^{-1}(\hat\mu_1-\hat\mu_0),$$
což je **shodné** s LDA (neboť $S_W=N\hat\Sigma$). To dává LDA optimalizační interpretaci a FLDA pravděpodobnostní interpretaci (při normalitě + shodných variancích).

**Více tříd ($C$):** FLDA se používá jako **redukce dimenzionality** — hledá $W$ (sloupce kolmé) maximalizující $\frac{\det(W^TS_BW)}{\det(W^TS_WW)}$, řešení přes vlastní vektory $S_W^{-1}S_B$; produkuje až $C-1$ příznaků optimálních pro separabilitu tříd (na rozdíl od PCA, která ignoruje třídy).

---

## Co je potřeba na zkoušku znát

### Definice
- **Generativní model:** modeluje $\mathrm P(X=x,Y=y)$; **diskriminativní:** modeluje přímo $\mathrm P(Y=y\mid X=x)$.
- **MAP odhad:** $\hat Y=\arg\max_y\mathrm P(X=x\mid Y=y)\mathrm P(Y=y)$ (přes [[Bayesova-věta|Bayesovu větu]], jmenovatel odpadá).
- **Naivní Bayes:** podmíněná nezávislost příznaků → $\mathrm P(X=x\mid Y=y)=\prod_i\mathrm P(X_i=x_i\mid Y=y)$.
- **Vícerozměrné $N(\mu,\Sigma)$:** hustota $\propto e^{-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)}$, $\Sigma_{ij}=\operatorname{cov}(X_i,X_j)$.

### Věty / odvození
- **QDA** ($\Sigma_y$ různé) → kvadratická hranice; **LDA** ($\Sigma_y=\Sigma$) → lineární hranice (nadrovina), softmax $e^{\beta_y^Tx+\gamma_y}$.
- **LDA $\equiv$ tvar logistické regrese:** $\mathrm P(Y=1\mid x)=\sigma(w^Tx+w_0)$, $w=\Sigma^{-1}(\mu_1-\mu_0)$; liší se trénováním (generativní vs. diskriminativní).
- **FLDA:** $\max J(w)=\frac{w^TS_Bw}{w^TS_Ww}$ → $S_W^{-1}S_Bw=\lambda w$ → $w=S_W^{-1}(\hat\mu_1-\hat\mu_0)$ = LDA.

### Odhady / postup
- **NB marginály (MLE + add-one):** Bernoulli, kategorické, Gaussovo; kolaps $N_{j,y}=0$ → Laplaceovo vyhlazení $\frac{N_{j,y}+1}{\cdots+k}$.
- **QDA/LDA MLE:** $\hat\pi_y=N_y/N$, $\hat\mu_y$ = třídní průměr, $\hat\Sigma$ (sdílená pro LDA).
- **log-sum-exp** proti podtečení; **FLDA** pro více tříd = redukce dimenze ($\le C-1$ příznaků, lepší než PCA pro klasifikaci).
