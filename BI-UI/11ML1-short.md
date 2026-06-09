---
tags: [otázka, kurz/ML1, otázka/11, todo]
---

# 11 — Hřebenová regrese, očekávaná chyba modelu a její rozklad (zkrácená verze)

## 1. Hřebenová regrese ($L_2$ regularizace)

Varianta [[Lineární-regrese|lineární regrese]] s penalizací velkých koeficientů (řeší **kolinearitu** / přeučení). Minimalizujeme **regularizovaný RSS**:
$$\operatorname{RSS}_\lambda(w) = \|Y - \mathbf{X}w\|^2 + \lambda\sum_{i=1}^p w_i^2 = \|Y - \mathbf{X}w\|^2 + \lambda\,w^T\mathbf{I}'w, \qquad \lambda \ge 0.$$

- **Penalizace se PŘIČÍTÁ** (znaménko $+$), je úměrná **kvadrátu** $L_2$-normy ($\sum w_i^2$, ne $\sum|w_i|$ = Lasso). Záporné znaménko → bez minima, nesmysl.
- $\lambda = 0$ → obyčejná [[Metoda-nejmenších-čtverců|MNČ]] (OLS). $\lambda > 0$ → **smršťování** koeficientů. $\lambda\uparrow$ → silnější.
- **Intercept $w_0$ se NEpenalizuje** (suma od $i=1$): $\mathbf{I}'$ = jednotková matice s $0$ na pozici $(0,0)$.
- **Motivace = kolinearita** (otázka 10): $\mathbf{X}^T\mathbf{X}$ singulární → $+\lambda\mathbf{I}'$ ji zregularizuje.

**Gradient:** $\nabla\operatorname{RSS}_\lambda(w) = -2\mathbf{X}^T(Y - \mathbf{X}w) + 2\lambda\mathbf{I}'w$.

**Normální rovnice:**
$$(\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')\,w = \mathbf{X}^TY \;\Rightarrow\; \boxed{\hat{w}_\lambda = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')^{-1}\mathbf{X}^TY}, \quad \hat{Y} = x^T\hat{w}_\lambda.$$

**[[Hessova-matice|Hessova matice]]** $= 2(\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')$ je pro $\lambda > 0$ **PD** (neboť $s^T(\mathbf{X}^T\mathbf{X}+\lambda\mathbf{I}')s = \|\mathbf{X}s\|^2 + \lambda\sum s_i^2 > 0$) → matice regulární → **jednoznačné řešení existuje vždy** (na rozdíl od OLS při kolinearitě).

Pozn.: před regularizací příznaky **standardizovat**; varianta $\lambda\sum|w_i|$ = Lasso.

## 2. Očekávaná chyba a její rozklad

Model $Y = \mathbf{X}w + \varepsilon$, $\operatorname{E}\varepsilon = 0$ → $Y$ i $\hat{w}_\lambda$ jsou **[[Náhodný-vektor|náhodné vektory]]**. Pevný bod $x$, predikce $\hat{Y} = x^T\hat{w}_\lambda$, **kvadratická ztráta** $L(Y,\hat{Y}) = (Y-\hat{Y})^2$. **Předpoklad: nezávislost train/test** ($Y \perp \hat{Y}$).

**Rozklad (1. úroveň):**
$$\operatorname{E}L(Y,\hat{Y}) = \sigma^2 + \operatorname{MSE}(\hat{Y}), \qquad \sigma^2 = \operatorname{var}\varepsilon.$$
- $\sigma^2$ = **neredukovatelná / Bayesovská chyba** (šum, nelze odstranit).
- $\operatorname{MSE}(\hat{Y}) = \operatorname{E}(\hat{Y} - \operatorname{E}Y)^2$ = [[Bodový-odhad|MSE]] odhadu $\hat{Y}$ parametru $\operatorname{E}Y$.

**Rozklad (2. úroveň):**
$$\operatorname{MSE}(\hat{Y}) = (\operatorname{bias}\hat{Y})^2 + \operatorname{var}\hat{Y}, \qquad \operatorname{bias}\hat{Y} = \operatorname{E}\hat{Y} - \operatorname{E}Y.$$

**Finální dekompozice:**
$$\boxed{\operatorname{E}L(Y,\hat{Y}) = \sigma^2 + (\operatorname{bias}\hat{Y})^2 + \operatorname{var}\hat{Y}}$$

*Idea důkazu:* dvakrát „přičti a odečti“ — nejprve $\operatorname{E}Y$ (smíšený člen $=0$ z nezávislosti), pak $\operatorname{E}\hat{Y}$ uvnitř MSE (smíšený člen $=0$, neboť $\operatorname{E}(\hat{Y}-\operatorname{E}\hat{Y})=0$).

**Kompromis vychýlení–rozptyl (bias-variance tradeoff):** u ridge zhruba
$$(\operatorname{bias}\hat{Y})^2 \sim \Big(1 - \tfrac{1}{1+\lambda}\Big)^2, \qquad \operatorname{var}\hat{Y} \sim \Big(\tfrac{1}{1+\lambda}\Big)^2.$$
S rostoucím $\lambda$: **vychýlení↑, rozptyl↓**. MSE = (bias)² + var má **minimum** v optimálním $\lambda$. OLS ($\lambda=0$): nestranný, $\operatorname{bias}=0$, ale vysoký rozptyl.

V praxi: optimální $\lambda$ minimalizací odhadu MSE na validační množině / přes [[Křížová-validace|cross-validaci]]: $\operatorname{MSE} = \frac1n\sum_{i=1}^n (Y'_i - {x'_i}^T\hat{w}_\lambda)^2$.

---

## Co odpovědět rychle

- **Hřebenová regrese:** $\operatorname{RSS}_\lambda = \|Y-\mathbf{X}w\|^2 + \lambda\sum_{i=1}^p w_i^2$; intercept se nepenalizuje ($\mathbf{I}'$).
- **Odhad:** $\hat{w}_\lambda = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')^{-1}\mathbf{X}^TY$; Hessova matice PD pro $\lambda>0$ → řešení vždy existuje a je jediné.
- **Rozklad chyby:** $\operatorname{E}L = \sigma^2 + \operatorname{MSE}$, $\operatorname{MSE} = \operatorname{bias}^2 + \operatorname{var}$ → dohromady $\sigma^2 + \operatorname{bias}^2 + \operatorname{var}$.
- $\sigma^2$ = neredukovatelná (Bayesovská) chyba; $\operatorname{bias} = \operatorname{E}\hat{Y}-\operatorname{E}Y$, $\operatorname{var} = \operatorname{var}\hat{Y}$.
- **Tradeoff:** $\lambda\uparrow$ → bias↑, var↓; hledáme $\lambda$ s minimální MSE (validace / CV). OLS je nestranný (bias = 0).
