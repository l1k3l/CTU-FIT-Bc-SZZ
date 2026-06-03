---
tags: [otázka, kurz/ML1, otázka/12, todo]
---

# 12 — Logistická regrese (zkrácená verze)

## 1. Sestavení modelu pro binární klasifikaci

[[Logistická-regrese]] je metoda pro **klasifikaci** (ne regresi). Binární: $Y \in \{0,1\}$. Místo třídy predikujeme **pravděpodobnost** $\mathrm{P}(Y=1\mid x,w) \in [0,1]$.

Rozhodnutí stavíme na **lineární kombinaci** $w^T x = w_0 + w_1 x_1 + \dots + w_p x_p$ (intercept $x_0=1$), protlačené **sigmoidou** (analogie [[Lineární-regrese|lineární regrese]]).

**Sigmoida:** $\sigma(z) = \dfrac{e^z}{1+e^z} = \dfrac{1}{1+e^{-z}}$ — obor hodnot $(0,1)$, ostře rostoucí (prostá), $\sigma(0)=\tfrac12$, $\sigma^{-1}(x)=\ln\frac{x}{1-x}$, $1-\sigma(z)=\frac{1}{1+e^z}$.

**Model:**
$$\mathrm{P}(Y=1\mid x,w) = \sigma(w^T x) = \frac{e^{w^T x}}{1+e^{w^T x}}, \qquad \mathrm{P}(Y=0\mid x,w) = \frac{1}{1+e^{w^T x}}.$$

**Rozhodovací pravidlo:** $\hat Y = \mathbb{1}[\hat p > \tfrac12]$, kde $\hat p = \mathrm{P}(Y=1\mid x,w)$.

**Hranice rozhodnutí:** $\hat p = \tfrac12 \iff w^T x = 0$ → **nadrovina** v $\mathbb{R}^p$ (dim. $p-1$), tj. **lineární** hranice.

**Logit (log-odds):** $\ln\dfrac{\hat p}{1-\hat p} = w^T x$ (lineární v příznacích).

## 2. Trénování jako MLE odhad

Odhadujeme pravděpodobnosti, ne $Y$ → chyba se měří těžko. Parametry $w$ určíme metodou **MLE** ([[Maximální-věrohodnost|maximálně věrohodný odhad]], jde o [[Bodový-odhad]]).

**Myšlenka MLE:** zvol $w$ tak, aby **trénovací data byla nejpravděpodobnější**. (Mince: $7\times$1, $3\times$0 → maximalizuj $p^7(1-p)^3$, $\hat p_{\mathrm{MLE}}=\tfrac{7}{10}$.)

Značení $p_1(x,w)=\sigma(w^Tx)$, $p_0 = 1-p_1$. Jeden bod (Bernoulli): $p_{Y_i}(x_i,w) = \hat p_i^{\,Y_i}(1-\hat p_i)^{1-Y_i}$.

**Věrohodnostní funkce** (předpoklad [[Nezávislost-náhodných-veličin|nezávislosti]] bodů → součin):
$$L(w) = \prod_{i=1}^N p_{Y_i}(x_i,w).$$

**Log-věrohodnost** (logaritmus = ostře rostoucí, stejné extrémy):
$$\ell(w) = \ln L(w) = \sum_{i=1}^N \big(Y_i \ln p_1 + (1-Y_i)\ln p_0\big) = \sum_{i=1}^N \big(Y_i\, w^T x_i - \ln(1+e^{w^T x_i})\big).$$

**Křížová entropie:** binární cross-entropy $= -\ell(w)$ → **max. věrohodnosti $\iff$ min. cross-entropy**.

**Gradient:**
$$\frac{\partial\ell}{\partial w_j} = \sum_{i=1}^N x_{i;j}(Y_i - p_1(x_i,w)), \qquad \nabla\ell(w) = \mathbf{X}^T(\boldsymbol{Y} - \boldsymbol{P}),$$
kde $\boldsymbol{P} = (p_1(x_1,w),\dots,p_1(x_N,w))^T$.

**Účelová funkce je [[Konvexní-funkce|konvexní]]** → lokální max. (pokud existuje) je jediné = globální. Max. neexistuje pro **lineárně separabilní** třídy.

**Není uzavřené řešení** rovnice $\nabla\ell(w)=0$ (na rozdíl od lineární regrese) → **numericky**:
- **[[Gradient|gradientní]] vzestup:** $w^{(i+1)} = w^{(i)} + \alpha\,\mathbf{X}^T(\boldsymbol{Y} - \boldsymbol{P}(w^{(i)}))$, $\alpha$ = learning rate;
- **Newtonova metoda / IRLS**.

---

## Co odpovědět rychle

- **LR = klasifikace**, ne regrese; binární $Y\in\{0,1\}$, predikujeme $\hat p = \mathrm{P}(Y=1\mid x,w)$.
- **Model:** $\hat p = \sigma(w^T x)$, sigmoida $\sigma(z)=\frac{1}{1+e^{-z}}$, obor $(0,1)$.
- **Predikce:** $\hat Y = \mathbb{1}[\hat p > \tfrac12]$; **hranice** $w^T x=0$ = nadrovina (lineární).
- **Trénink = MLE:** maximalizuj věrohodnost $L(w)=\prod_i \hat p_i^{Y_i}(1-\hat p_i)^{1-Y_i}$ = data nejpravděpodobnější.
- **Log-věrohodnost** $\ell(w)=\sum_i(Y_i w^Tx_i - \ln(1+e^{w^Tx_i}))$; $-\ell$ = binární cross-entropy.
- **Gradient** $\nabla\ell(w)=\mathbf{X}^T(\boldsymbol{Y}-\boldsymbol{P})$; konvexní, bez uzavřeného řešení → gradientní vzestup / Newton (IRLS).
