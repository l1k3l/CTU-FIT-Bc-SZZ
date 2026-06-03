---
tags: [otázka, kurz/ML1, otázka/8, todo]
---

# 8 — Rozhodovací stromy, náhodné lesy, AdaBoost (zkrácená verze)

## 1. Rozhodovací stromy

Supervizované učení $Y \approx f(X_1,\dots,X_p)$; klasifikace (málo hodnot $Y$) vs. regrese (spojité $Y$).

[[Rozhodovací-strom]]: zakořeněný strom, vnitřní vrcholy = rozhodovací pravidla nad příznaky, listy = predikce $Y$. **Predikce** = průchod od kořene; v listu:
- klasifikace → **majoritní třída** (hlasování, při shodě náhodně);
- regrese → **průměr** $Y$ z listu.

**Budování (shora dolů, hladově).** Optimální strom je **NP-úplný** problém → hladový algoritmus (**ID3 → C4.5/C5 → CART**): rekurzivně vyber příznak (a práh) maximalizující dělicí kritérium, rozděl $\mathcal{D}$ na $\mathcal{D}_L,\mathcal{D}_R$, opakuj na obou; konec při **zastavovací podmínce** (max hloubka, málo dat, nízký zisk). Hladový ≠ optimální. Složitost konstrukce polynomiální v $N, p$.

### Dělicí kritéria
Míra neuspořádanosti množiny $\mathcal{D}$, $p_i$ = rel. četnost $i$-té hodnoty $Y$:
$$H(\mathcal{D}) = -\sum_i p_i \log p_i \qquad GI(\mathcal{D}) = 1 - \sum_i p_i^2 = \sum_i p_i(1-p_i).$$
**Informační zisk:** $IG(\mathcal{D},X_i) = H(\mathcal{D}) - t_0 H(\mathcal{D}_0) - t_1 H(\mathcal{D}_1)$, $t_j = \#\mathcal{D}_j/\#\mathcal{D}$. Vyber příznak s **max** $IG$.

| | Entropie $H$ | Gini index $GI$ |
|---|---|---|
| vzorec | $-\sum p_i \log p_i$ | $1-\sum p_i^2$ |
| max (bin., $p=\tfrac12$) | $1$ (bit) | $0{,}5$ |
| čistá množina | $0$ | $0$ |
| interpretace | nejistota | pravděp. chybné klasifikace |

### Spojité příznaky
Pravidlo $X \le d$. Algoritmus: setřiď hodnoty $x_1<\dots<x_\ell$, zkus prahy $X \le (x_{i-1}+x_i)/2$, vyber dle max $IG$. Spojitý příznak se může ve stromu objevit **vícekrát**. (Nominální kat. příznaky → one-hot encoding; ordinální → očíslovat.)

### Regresní stromy (spojité $Y$)
Predikce listu = **průměr** $Y$. Kritérium místo entropie = **MSE** $=\tfrac1N\sum_j(Y_j-\overline{Y})^2$ (≈ rozptyl), minimalizuj $\mathrm{MSE}(\mathcal{D}) - t_L\mathrm{MSE}(\mathcal{D}_L) - t_R\mathrm{MSE}(\mathcal{D}_R)$. Alternativa **MAE** $=\tfrac1N\sum|Y_i-\overline{Y}|$.

### Hyperparametry, přeučení
**Přesnost** $=\frac{\text{správně}}{\text{vše}}$, chyba $=1-$přesnost. Data → **trénovací / validační / testovací**. **Přeučení (overfitting):** hlubší strom = nižší trénovací chyba, ale testovací chyba má minimum a pak roste. **Ladění hyperparametrů** (`max_depth`, …) na **validačních** datech (vyber min. chybu); finální chyba měřena na **testovacích**. Alternativa [[Křížová-validace|křížová validace]]. Prořezávání = `min_samples_leaf`, `max_leaf_nodes`, `min_impurity_decrease`, … proti přeučení.
**Výhody:** nenáročnost na data, interpretovatelnost, rychlé učení. **Nevýhody:** nerobustnost (citlivost na změnu dat → velký rozptyl), jen binární stromy, snadné přeučení.

## 2. Bagging — náhodný les

**Ensemble:** místo 1 modelu více modelů, predikce zkombinovány.

**Bootstrap** = výběr řádků **s opakováním** (datasety $\mathcal{D}_1,\dots,\mathcal{D}_n$ velikosti $\approx\#\mathcal{D}$).

**Náhodný les:** na každém $\mathcal{D}_i$ nauč strom $T_i$ jen na **náhodné podmnožině příznaků** (velikost $\sqrt{p}$); stromy = podmodely (*base learners*). Agregace:
- klasifikace → **majority vote** (většinové hlasování);
- regrese → **průměr** $\hat{Y} = \tfrac1n\sum_i\hat{Y}_i$.

**Hyperparametry:** `n_estimators` (počet stromů), `max_depth`, `max_features` ($=\sqrt{p}$).

**Proč funguje:** stromy mají **velký rozptyl** → randomizace (bootstrap + `max_features`) dá pestré podmodely; průměrování **redukuje rozptyl**. Robustní, odolný vůči přeučení; ztráta interpretovatelnosti.

## 3. Boosting — AdaBoost

Více podmodelů, finální = **vážená** kompozice. Na rozdíl od baggingu podmodely **závislé, sekvenční**: $n$-tý strom má **zvýšené váhy** bodů, které $(n{-}1)$-tý klasifikoval špatně.

**Váhy bodů** $w_i$ (`sample_weight`): entropie i podíly $t_L,t_R$ v $IG$ se počítají **váženě** → strom správně predikuje hlavně body s vysokou vahou.

**AdaBoost (popis):** $w_i = 1/N$, $m=1$; opakuj do `n_estimators`:
- nauč strom $T^{(m)}$ na $\mathcal{D}$ s vahami $w_i$;
- chyba $e^{(m)} = $ součet vah špatně klasifikovaných (pokud $0$ → konec);
- příspěvek modelu $\alpha^{(m)} = \texttt{lr}\cdot\log\dfrac{1-e^{(m)}}{e^{(m)}}$ (menší chyba ⇒ větší $\alpha$);
- špatným bodům $w_i \leftarrow w_i\exp(\alpha^{(m)})$, pak **normalizuj** ($\sum w_i = 1$).

**Finální rozhodnutí:** sečti $\alpha^{(m)}$ stromů hlasujících pro $Y=1$ a zvlášť pro $Y=0$; vyber větší součet (**vážené hlasování**).

`learning_rate` = regularizace (nižší ⇒ odolnější vůči přeučení, ale víc stromů). Podmodely = slabé modely (mělké stromy). Boosting **redukuje vychýlení (bias)**.

### Bagging vs. boosting
| | Bagging (náhodný les) | Boosting (AdaBoost) |
|---|---|---|
| podmodely | nezávislé, paralelní | závislé, sekvenční |
| data | bootstrap | $\mathcal{D}$ s vahami bodů |
| agregace | majority vote / průměr | vážené hlasování ($\alpha^{(m)}$) |
| redukuje | **rozptyl** | **vychýlení** |

---

## Co odpovědět rychle

- **Strom:** vnitřní vrcholy = pravidla, listy = majorita (klasif.) / průměr (regrese); predikce = průchod. Optimální strom NP-úplný → hladově (ID3/CART).
- **Kritéria:** entropie $-\sum p_i\log p_i$, Gini $1-\sum p_i^2$, info zisk $IG = H(\mathcal{D}) - \sum_j t_j H(\mathcal{D}_j)$; regrese → MSE.
- **Spojité příznaky:** zkoušej prahy $X\le(x_{i-1}+x_i)/2$ mezi setříděnými hodnotami.
- **Přeučení:** hlubší = nižší train chyba, test chyba má minimum; ladění hyperparametrů na validačních datech.
- **Náhodný les:** bootstrap + strom na $\sqrt{p}$ náhodných příznacích; hlasování/průměr; redukuje rozptyl; `n_estimators`, `max_features`.
- **AdaBoost:** sekvenční, váhy bodů; chyba $e^{(m)}$, příspěvek $\alpha^{(m)}=\texttt{lr}\log\frac{1-e^{(m)}}{e^{(m)}}$; špatným bodům roste váha; finální vážené hlasování; redukuje bias.
- **Bagging vs boosting:** nezávislé/paralelní vs. závislé/sekvenční; rozptyl vs. vychýlení.
