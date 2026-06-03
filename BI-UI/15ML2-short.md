---
tags: [otázka, kurz/ML2, otázka/15, todo]
---

# 15 — Jádrová regrese (zkrácená verze)

## 1. Opakování regrese

[[Lineární-regrese]]: $Y=w^Tx+\varepsilon$, $\mathrm E\varepsilon=0$. [[Metoda-nejmenších-čtverců|MNČ]]: min $\mathrm{RSS}(w)=\lVert\boldsymbol Y-\mathbf Xw\rVert^2$ → $\hat w_{\mathrm{OLS}}=(\mathbf X^T\mathbf X)^{-1}\mathbf X^T\boldsymbol Y$.

**Hřebenová (ridge):** min $\lVert\boldsymbol Y-\mathbf Xw\rVert^2+\lambda\lVert w\rVert^2$ → $\hat w_\lambda=(\mathbf X^T\mathbf X+\lambda I')^{-1}\mathbf X^T\boldsymbol Y$ (jednoznačné pro $\lambda>0$).

## 2. Lineární model bázových funkcí

**Bázové funkce** $\varphi_1,\dots,\varphi_M:\mathcal X\to\mathbb R$ (LN), $\varphi(x)=(\varphi_1(x),\dots,\varphi_M(x))^T$ — nelineární transformace příznaků do $M$-rozm. prostoru.

**Model:** $Y=w^T\varphi(x)+\varepsilon$ — **lineární v $w$**, nelineární v $x$.

**Odhad** (design matrix $\boldsymbol\Phi_{ij}=\varphi_j(x_i)$): min $\lVert\boldsymbol Y-\boldsymbol\Phi w\rVert^2+\lambda w^Tw$ →
$$\hat w_\lambda=(\boldsymbol\Phi^T\boldsymbol\Phi+\lambda I)^{-1}\boldsymbol\Phi^T\boldsymbol Y,\qquad \hat Y=\hat w_\lambda^T\varphi(x).$$

Volby: $x_i$ (lineární), $x_i^2,x_kx_\ell$ (polynom.), $\log x_i,\sqrt{x_i}$, indikátory, RBF $h(\lVert x-x_i\rVert)$. Nevýhoda: $M$ velké → inverze $M\times M$ je $O(M^3)$.

## 3. Duální reprezentace

Hledáme $w=\boldsymbol\Phi^T\alpha$, $\alpha\in\mathbb R^N$. Dosazením:
$$\mathrm{RSS}_\lambda(\alpha)=\lVert\boldsymbol Y-G\alpha\rVert^2+\lambda\,\alpha^TG\alpha,\qquad G=\boldsymbol\Phi\boldsymbol\Phi^T.$$

**Věta:** pro $\lambda>0$ je $\min_\alpha\mathrm{RSS}_\lambda(\alpha)=\min_w\mathrm{RSS}_\lambda(w)$; převod $w^*=\boldsymbol\Phi^T\alpha^*$, $\alpha^*=\tfrac1\lambda(\boldsymbol Y-\boldsymbol\Phi w^*)$.

**Gramova matice** $G\in\mathbb R^{N,N}$, $G_{ij}=\varphi(x_i)^T\varphi(x_j)$ — symetrická, PSD.

**Řešení:** $\hat\alpha=(G+\lambda I)^{-1}\boldsymbol Y$ (PSD → $G+\lambda I$ reg.).

**Predikce:** $\hat Y=\sum_{i=1}^N\hat\alpha_i\,\varphi(x_i)^T\varphi(x)$. → body se vyskytují jen ve **skalárních součinech**.

## 4. Jádrový trik

[[Jádrová-funkce|Jádrová funkce]] $k(x,y)=\varphi(x)^T\varphi(y)$ → $G_{ij}=k(x_i,x_j)$.

**Jádrový trik:** nahraď $\varphi(x)^T\varphi(y)\to k(x,y)$; lze začít rovnou jádrem bez explicitních $\varphi$ → práce v implicitním (i $\infty$-rozm.) prostoru.

Celý model jen přes $k$:
$$\hat\alpha=(G+\lambda I)^{-1}\boldsymbol Y,\qquad \hat Y=\sum_{i=1}^N\hat\alpha_i\,k(x_i,x).$$

**Složitost:** $O(M^3)$ primárně vs. $O(N^3)$ duálně → pro $M\gg N$ vyhrává jádro.

**Jádra:** lineární $x^Ty$; polynomiální $(x^Ty+1)^n$; Gaussovské/RBF $e^{-\gamma\lVert x-y\rVert^2}$ ($\infty$-rozm.). Podmínka: symetrická PSD funkce.

**Jádrové modely:** $f(x)=\sum_j\alpha_j k(\mu_j,x)$; vector machine = středy v trénovacích bodech (totéž používá [[Metoda-podpůrných-vektorů|SVM]]).

---

## Co odpovědět rychle
- **Model bázových funkcí:** $Y=w^T\varphi(x)$ — lineární v $w$, nelineární v $x$; ridge řešení $(\boldsymbol\Phi^T\boldsymbol\Phi+\lambda I)^{-1}\boldsymbol\Phi^T\boldsymbol Y$.
- **Duálně:** $w=\boldsymbol\Phi^T\alpha$ → vše přes Gramovu matici $G_{ij}=\varphi(x_i)^T\varphi(x_j)$; $\hat\alpha=(G+\lambda I)^{-1}\boldsymbol Y$.
- **Jádrová funkce** $k(x,y)=\varphi(x)^T\varphi(y)$; **jádrový trik** = nahrazení skalárních součinů jádrem → implicitní vysoká dimenze.
- **Predikce** $\hat Y=\sum_i\hat\alpha_i k(x_i,x)$ = vážená kombinace trénovacích hodnot.
- **Jádra:** lineární, polynomiální $(x^Ty+1)^n$, RBF $e^{-\gamma\lVert x-y\rVert^2}$.
