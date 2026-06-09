---
tags: [otázka, kurz/ML1, otázka/13, todo]
---

# 13 — Evaluace modelů: testovací chyba, křížová validace, metriky (zkrácená verze)

## 1. Ztrátová funkce a chyby

$Y$ vysvětlovaná, $\boldsymbol X$ příznaky, $\hat Y(\boldsymbol X)$ predikce, $\hat p = \hat{\mathrm P}(Y=1\mid\boldsymbol X)$. **Ztrátová funkce** $L(Y,\hat Y)$:
- regrese: kvadratická $L = (Y-\hat Y)^2$, absolutní $L_1 = |Y-\hat Y|$;
- bin. klasifikace: cross-entropy $L(Y,\hat p) = -Y\log\hat p - (1-Y)\log(1-\hat p)$, predikce $\hat Y = \mathbb 1_{\hat p > 1/2}$. Cross-entropy jen pro modely odhadující $\hat p\in(0,1)$ (logistická regrese, NN, stromy).

**Metrika vs. loss:** loss = pro **trénink** (minimalizace, grad. sestup, hladká); metrika = vyhodnocení **po tréninku** (nemusí jít optimalizovat: accuracy, AUC). Tutéž loss lze použít i jako metriku, pokud dává smysl. **„Testovací chyba" = hodnota metriky nad TEST setem.**

**Trénovací chyba** $\overline{\mathrm{err}}_{\mathrm{train}} = \frac1N\sum_{i=1}^N L(Y_i,\hat Y(\boldsymbol x_i))$ — průměr ztráty na trénu. Je **optimisticky vychýlená** (model laděn na trénu → overfitting → podhodnocuje generalizační chybu). **Přeučení poznám:** trénovací chyba malá, testovací velká. Test „jako v produkci" = metriky na odděleném test setu.

Bin. klasif. trénovací ztráta = $-\frac1N\sum [Y_i\log\hat p_i + (1-Y_i)\log(1-\hat p_i)]$ = mínus log-věrohodnost maximalizovaná [[Logistická-regrese|logistickou regresí]] → minimalizace cross-entropy ↔ maximalizace [[Maximální-věrohodnost|věrohodnosti]] (totožná úloha).

**Testovací (generalizační) chyba:** $\mathrm{Err}_{\mathcal D} = \mathrm E(L(Y,\hat Y(\boldsymbol X))\mid\mathcal D)$, $\mathcal D$ = trénovací data. Odhad výběrovým průměrem na **nezávislých** test. datech:
$$\overline{\mathrm{err}}_{\mathrm{test}} = \frac{1}{N_{\mathrm{test}}}\sum_{i=1}^{N_{\mathrm{test}}} L(Y_i,\hat Y(\boldsymbol x_i)), \qquad \mathrm E(\overline{\mathrm{err}}_{\mathrm{test}}\mid\mathcal D) = \mathrm{Err}_{\mathcal D}\ \text{(nestranný)}.$$
**Očekávaná** testovací chyba: $\mathrm{Err} = \mathrm E(\mathrm{Err}_{\mathcal D}) = \mathrm E\,L(Y,\hat Y(\boldsymbol X))$.

## 2. Hold-out (rozdělení dat)

Dostatek dat → **trénovací / validační / testovací**:
- **trénovací** — trénink modelů s fixními hyperparametry;
- **validační** — výběr hyperparametrů a nejlepšího modelu (= *výběr modelu*);
- **testovací** — finální odhad testovací chyby (= *ohodnocení modelu*).

Pravidlo: stejná data nesmí sloužit k výběru i ohodnocení modelu. Tři části **disjunktní** a vybrané **náhodně** (před rozdělením permutovat); musí pocházet ze stejného rozdělení. Testovací množinu oddělit **co nejdříve** (před předzpracováním), držet striktně bokem. **Výjimka — chronologická data** (nestacionární jevy, burza): nepermutovat, test = nejnovější data.

## 3. Křížová validace

Když málo dat na 3 části → [[Křížová-validace]] (test. data oddělena, jde o výběr modelu).

**Idea $k$-fold:** trénovací data $\mathcal D$ náhodně rozděl na $k$ podobně velkých částí $\mathcal D_1,\dots,\mathcal D_k$ ($2\le k\le N$). Pro $j=1,\dots,k$ natrénuj na $\mathcal D\setminus\mathcal D_j$ a změř chybu $e_j$ na vynechané $\mathcal D_j$. Vrať průměr $\hat e = \frac1k\sum_{i=1}^k e_i$. Zopakuj pro všechny hyperparametry, vyber ty s **nejmenší** $\hat e$ a finální model **přetrénuj na celém** $\mathcal D$. Typicky $k = 5$–$10$.

**Leave-one-out (LOO):** $k = N$ — trénuj na všech bez 1 bodu, na něm měř; max. využití dat, výpočetně náročné.

Výhody vs. jedna validační množina: efektivnější využití dat, méně rozptýlený odhad. Pro fixní model je CV chyba odhadem $\mathrm{Err}$ (ne $\mathrm{Err}_{\mathcal D}$). Dvoustupňová CV (vnitřní = výběr modelu, vnější = odhad chyby) když nelze oddělit ani test. množinu.

## 4. Metriky regrese

| metrika | vzorec | vlastnost |
|---|---|---|
| MSE | $\frac1N\sum(Y_i-\hat Y_i)^2$ | penalizuje velké odchylky, citlivá na odlehlé |
| RMSE | $\sqrt{\frac1N\sum(Y_i-\hat Y_i)^2}$ | jako MSE, ale jednotky cílové proměnné |
| RMSLE | $\sqrt{\frac1N\sum(\log Y_i-\log\hat Y_i)^2}$ | relativní odchylky (nezáporné $Y$), méně citlivá |
| MAE | $\frac1N\sum|Y_i-\hat Y_i|$ | lineární, méně citlivá k odlehlým |
| $R^2$ | $1-\frac{\mathrm{RSS}}{\mathrm{SST}}$ | podíl vysvětlené variability; $\mathrm{RSS}=\sum(Y_i-\hat Y_i)^2$, $\mathrm{SST}=\sum(Y_i-\bar Y)^2$ |

## 5. Metriky klasifikace

Z **matice záměn** (confusion matrix), binární klasifikace:

| Skutečnost \\ Predikce | $\hat Y=1$ | $\hat Y=0$ | $\sum$ |
|---|---|---|---|
| $Y=1$ | TP | FN | $N_+ = \mathrm{TP}+\mathrm{FN}$ |
| $Y=0$ | FP | TN | $N_- = \mathrm{FP}+\mathrm{TN}$ |
| $\sum$ | $\hat N_+ = \mathrm{TP}+\mathrm{FP}$ | $\hat N_- = \mathrm{FN}+\mathrm{TN}$ | $N$ |

TP/TN správně, FP/FN špatně (FP = type I, FN = type II). Odvozené míry:

| míra | vzorec | alias |
|---|---|---|
| TPR / recall | $\mathrm{TP}/N_+$ | sensitivita, hit rate |
| FPR | $\mathrm{FP}/N_-$ | false alarm, type I rate |
| TNR | $\mathrm{TN}/N_-$ | specificita, selektivita |
| PPV / precision | $\mathrm{TP}/\hat N_+$ | positive predictive value |
| ACC (přesnost) | $\frac{\mathrm{TP}+\mathrm{TN}}{N}$ | nevhodná pro nevyvážené datasety |
| $F_1$ | $2\,\frac{\mathrm{PPV}\cdot\mathrm{TPR}}{\mathrm{PPV}+\mathrm{TPR}}$ | harm. průměr precision a recall |

**Práh $\tau$:** $\hat Y_\tau = \mathbb 1_{\hat p(\boldsymbol X) > \tau}$ ($\hat Y = \hat Y_{0.5}$). **ROC křivka** = graf TPR$_\tau$ vs. FPR$_\tau$; diagonála = náhodná predikce. **AUC** = plocha pod ROC: náhoda 0.5, dokonalý 1, typicky 0.5–1. **AUC = 1** ⇔ existuje práh $\tau$, který přesně klasifikuje všechny body ($\hat p$ dokonale odděluje třídy).

---

## Co odpovědět rychle

- **Ztrátová funkce:** regrese $(Y-\hat Y)^2$ / $|Y-\hat Y|$; klasifikace cross-entropy $-Y\log\hat p-(1-Y)\log(1-\hat p)$.
- **Trénovací chyba** = průměr ztráty na trénu, **podhodnocuje** generalizaci (overfitting). **Testovací chyba** $\mathrm{Err}_{\mathcal D}$ = stř. hodnota ztráty na novém $\boldsymbol X$; odhad = průměr na **nezávislých** test. datech (nestranný).
- **Hold-out:** trénovací (trénink) / validační (výběr modelu) / testovací (ohodnocení). Test data oddělit co nejdřív.
- **k-fold CV:** $k$ částí, $k$× trénuj na $k-1$, měř na vynechané, průměruj $\hat e$; vyber min, přetrénuj na celém $\mathcal D$. LOO = $k=N$. ($k=5$–$10$.)
- **Regrese:** MSE, RMSE (jednotky $Y$), MAE (méně citlivá), $R^2=1-\mathrm{RSS}/\mathrm{SST}$.
- **Klasifikace:** matice záměn (TP/FP/FN/TN) → ACC, precision (PPV), recall (TPR), $F_1$; ROC (TPR vs. FPR) + AUC. ACC selhává na nevyvážených datech.
- Cross-entropy = mínus log-věrohodnost logistické regrese; použitelná jen pro modely odhadující $\hat p$.
- **Metrika vs. loss:** loss → trénink (minimalizace), metrika → vyhodnocení po tréninku; tutéž loss lze měřit i na test setu. „Testovací chyba" = metrika nad TEST setem.
- **AUC = 1** ⇔ existuje práh, který přesně klasifikuje všechny body.
