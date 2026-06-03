---
tags: [otázka, kurz/ML1, otázka/11, todo]
---

# Hřebenová regrese, očekávaná chyba modelu a její rozklad

> **Otázka SZZ:** Hřebenová regrese, očekávaná chyba modelu a její rozklad.

Zdroje: BI-ML1 (FIT ČVUT), přednáška 6 — sekce 21 Hřebenová regrese, sekce 22 Vztah vychýlení a rozptylu, sekce 23 Modely bázových funkcí, sekce 24 Statistické vlastnosti lineární regrese; printed str. 44–48.

Značení: $\mathbf{X} \in \mathbb{R}^{N,p+1}$ matice příznaků (řádky = pozorování, první sloupec jedniček pro intercept), $w = (w_0, w_1, \dots, w_p)^T$ vektor koeficientů ($w_0$ = intercept), $\lambda \ge 0$ regularizační parametr (hyperparametr), $\mathbf{I}' \in \mathbb{R}^{p+1,p+1}$ jednotková matice s nulou na pozici interceptu (tj. $\mathbf{I}'_{00} = 0$, jinak diagonála $1$), $\hat{w}_\lambda$ hřebenový odhad parametrů, $x = (1, x_1, \dots, x_p)^T$ pevný bod, $\hat{Y} = x^T\hat{w}_\lambda$ predikce, $Y$ skutečná hodnota, $\varepsilon$ šum, $\sigma^2 = \operatorname{var}\varepsilon$. $\|\cdot\|$ eukleidovská norma, $\operatorname{E}$ střední hodnota, $\operatorname{var}$ rozptyl.

---

## 1. Hřebenová regrese

### 1.1 Motivace — kolinearita a $L_2$ regularizace

**Hřebenová regrese** (angl. *ridge regression*, Hoerl–Kennard 1970), nazývaná též **$L_2$ regularizace**, se k problému **kolinearity** příznaků staví zavedením **penalizačního členu** úměrného kvadrátu **[[Norma|normy]]** vektoru koeficientů $w$.

Připomeňme model **[[Lineární-regrese|lineární regrese]]**: hodnota cílové veličiny v bodě $x$ je
$$Y = w_0 + w_1 x_1 + \dots + w_p x_p + \varepsilon = x^T w + \varepsilon, \qquad \operatorname{E}\varepsilon = 0.$$
Obyčejná **[[Metoda-nejmenších-čtverců|metoda nejmenších čtverců]]** (OLS) hledá $\hat{w}^{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^TY$. Jsou-li sloupce $\mathbf{X}$ téměř lineárně závislé (kolinearita), je $\mathbf{X}^T\mathbf{X}$ špatně podmíněná až **singulární** — odhad je nestabilní, koeficienty nabývají velkých hodnot a model přeučuje (overfitting). Hřebenová regrese tento problém řeší tím, že velké koeficienty penalizuje.

### 1.2 Regularizovaný reziduální součet čtverců

Minimalizujeme **regularizovaný reziduální součet čtverců**
$$\operatorname{RSS}_\lambda(w) = \|Y - \mathbf{X}w\|^2 + \lambda \sum_{i=1}^p w_i^2,$$
který závisí na parametru $\lambda \ge 0$. Pozorování:

- **Pro $\lambda = 0$** dostáváme $\operatorname{RSS}_0(w) = \operatorname{RSS}(w)$ — tj. obyčejnou metodu nejmenších čtverců.
- **Pro $\lambda > 0$** se v minimu míří na takové vektory $w$, které mají co nejmenší složky → koeficienty se **smršťují** (shrinkage) k nule. Čím větší $\lambda$, tím silnější smršťování.
- **Intercept $w_0$ se NEpenalizuje** (suma běží od $i=1$, ne od $0$). Jedná se totiž pouze o vertikální posun zajišťující předpoklad $\operatorname{E}\varepsilon = 0$ modelu, a je tedy vhodné ho neomezovat.

### 1.3 Maticový zápis a matice $\mathbf{I}'$

Penalizaci bez interceptu zapíšeme maticí
$$\mathbf{I}' = \begin{pmatrix} 0 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{pmatrix} \in \mathbb{R}^{p+1,p+1},$$
tj. jednotková matice s nulou na pozici $(0,0)$ odpovídající interceptu. Pak
$$\sum_{i=1}^p w_i^2 = w^T\mathbf{I}'w, \qquad \operatorname{RSS}_\lambda(w) = \|Y - \mathbf{X}w\|^2 + \lambda\, w^T\mathbf{I}'w.$$

### 1.4 Gradient a normální rovnice

Gradient regularizovaného RSS:
$$\nabla\operatorname{RSS}_\lambda(w) = -2\mathbf{X}^T(Y - \mathbf{X}w) + 2\lambda\mathbf{I}'w.$$
Položením $\nabla\operatorname{RSS}_\lambda(w) = \mathbf{0}$ dostaneme (ekvivalent) **normální rovnice** hřebenové regrese:
$$\mathbf{X}^TY - \mathbf{X}^T\mathbf{X}w - \lambda\mathbf{I}'w = \mathbf{0}, \qquad\text{tj.}\qquad (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')\,w = \mathbf{X}^TY.$$

### 1.5 Pozitivní definitnost Hessovy matice a jednoznačnost řešení

**[[Hessova-matice|Hessova matice]]** funkce $\operatorname{RSS}_\lambda$ je
$$\mathbf{H}_{\operatorname{RSS}_\lambda}(w) = 2\mathbf{X}^T\mathbf{X} + 2\lambda\mathbf{I}' = 2(\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}').$$

**Věta (PD Hessovy matice).** Pro $\lambda > 0$ je matice $\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}'$ **pozitivně definitní** (PD), tedy regulární.

*Důkaz.* Pro každé $s = (s_0, s_1, \dots, s_p)^T \in \mathbb{R}^{p+1}$, $s \ne \mathbf{0}$, a $\lambda > 0$ platí
$$s^T(\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')s = (\mathbf{X}s)^T(\mathbf{X}s) + \lambda\, s^T\mathbf{I}'s = \|\mathbf{X}s\|^2 + \lambda\sum_{i=1}^p s_i^2 \ge 0.$$
Zbývá ukázat ostrou nerovnost. Oba sčítance jsou nezáporné; rovnost nule by vyžadovala současně $\|\mathbf{X}s\|^2 = 0$ a $\sum_{i=1}^p s_i^2 = 0$. Druhá podmínka dá $s_1 = \dots = s_p = 0$, tedy $s = (s_0, 0, \dots, 0)^T \ne \mathbf{0}$, čili $s_0 \ne 0$. Pak ovšem $\mathbf{X}s = (s_0, \dots, s_0)^T \ne \mathbf{0}$ (první sloupec $\mathbf{X}$ jsou samé jedničky), takže $\|\mathbf{X}s\|^2 > 0$ — spor. Tedy
$$s^T(\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')s > 0 \quad\text{pro všechna } s \ne \mathbf{0}. \qquad\square$$

Hessova matice je tedy pozitivně definitní a matice $\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}'$ regulární. **Pro $\lambda > 0$ tak vždy existuje jednoznačné řešení** normální rovnice, odpovídající globálnímu minimu konvexní $\operatorname{RSS}_\lambda$:
$$\boxed{\;\hat{w}_\lambda = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')^{-1}\mathbf{X}^TY\;}$$

Na rozdíl od OLS, kde regularita $\mathbf{X}^T\mathbf{X}$ vyžaduje plnou hodnost sloupců $\mathbf{X}$ (tedy řešení nemusí existovat / být jednoznačné při kolinearitě), je u hřebenové regrese řešení **vždy** jednoznačné. To je hlavní praktická výhoda — proto „hřeben“ (přidání $\lambda$ na diagonálu „zvedne hřbet“ matice a učiní ji regulární).

Predikce v pevném bodě $x$ je potom opět
$$\hat{Y} = x^T\hat{w}_\lambda.$$

### 1.6 Vliv $\lambda$ a standardizace příznaků

Parametr $\lambda$ řídí míru regularizace: $\lambda \to 0$ → OLS (žádné smršťování); $\lambda \to \infty$ → všechny koeficienty (kromě interceptu) jdou k nule. Optimální $\lambda$ se obvykle volí pomocí **[[Křížová-validace|křížové validace]]** (viz §2.6).

Před aplikací hřebenové regrese je obvyklé příznaky **standardizovat**, aby byly rozsahově srovnatelné a penalizovány stejně:
$$X'_i = \frac{X_i - \bar{X}_i}{\sqrt{s^2_{X_i}}}, \qquad \bar{X}_i = \frac1N\sum_{j=1}^N x_{j;i}, \quad s^2_{X_i} = \frac{1}{N-1}\sum_{j=1}^N (x_{j;i} - \bar{X}_i)^2.$$
Bez standardizace by příznak s velkým rozsahem dostal nepřiměřeně malou penalizaci. Existují i jiné formy regularizace, např. $\lambda\sum_{i=1}^p |w_i|$ (**Lasso**, $L_1$ regularizace).

---

## 2. Očekávaná chyba modelu a její rozklad

### 2.1 Předpoklady a kvadratická ztráta

V modelu pro trénovací množinu $Y = \mathbf{X}w + \varepsilon$ je $\varepsilon$ **[[Náhodný-vektor|náhodný vektor]]** s $\operatorname{E}\varepsilon = \mathbf{0}$. Z toho plyne, že i $Y$ je náhodný vektor a tedy i odhad parametrů $\hat{w}_\lambda = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')^{-1}\mathbf{X}^TY$ je **náhodný vektor**.

Uvažujme pevný bod $x = (1, x_1, \dots, x_p)^T \in \mathbb{R}^{p+1}$ a zkoumejme **očekávanou chybu** měřenou pomocí **kvadratické ztrátové funkce** při predikci skutečné hodnoty $Y = x^Tw + \varepsilon$ pomocí $\hat{Y} = x^T\hat{w}_\lambda$:
$$L(Y, \hat{Y}) = (Y - \hat{Y})^2.$$

Klíčový **předpoklad: nezávislost trénovacích a testovacích dat**, tj. nezávislost $Y$ a $\hat{Y}$ (testovací šum $\varepsilon$ ve $Y$ je nezávislý na trénovacích datech, z nichž je $\hat{Y}$ spočteno). V důsledku jsou $Y$ a $\hat{Y}$ nezávislé.

### 2.2 Pomocné lemma (smíšený člen)

**Lemma.** Při nezávislosti $Y$ a $\hat{Y}$ platí
$$\operatorname{E}\!\big((Y - \operatorname{E}Y)(\operatorname{E}Y - \hat{Y})\big) = 0.$$

*Důkaz.* Roznásobíme a využijeme linearitu **[[Střední-hodnota|střední hodnoty]]** a nezávislost (díky níž $\operatorname{E}(Y\hat{Y}) = \operatorname{E}Y\cdot\operatorname{E}\hat{Y}$):
$$
\begin{aligned}
\operatorname{E}\!\big((Y - \operatorname{E}Y)(\operatorname{E}Y - \hat{Y})\big)
&= \operatorname{E}\!\big(Y(\operatorname{E}Y) - (Y\hat{Y}) - (\operatorname{E}Y)^2 + (\operatorname{E}Y)\hat{Y}\big) \\
&= (\operatorname{E}Y)^2 - \operatorname{E}(Y\hat{Y}) - (\operatorname{E}Y)^2 + \operatorname{E}Y\cdot\operatorname{E}\hat{Y} \\
&= -\operatorname{E}(Y\hat{Y}) + \operatorname{E}Y\cdot\operatorname{E}\hat{Y} = 0. \qquad\square
\end{aligned}
$$

### 2.3 Rozklad první úrovně: neredukovatelná chyba + MSE

**Věta (rozklad očekávané chyby).** Za výše uvedených předpokladů platí
$$\operatorname{E}L(Y, \hat{Y}) = \sigma^2 + \operatorname{MSE}(\hat{Y}),$$
kde $\sigma^2 = \operatorname{var}\varepsilon = \operatorname{var}Y$ a $\operatorname{MSE}(\hat{Y}) = \operatorname{E}(\hat{Y} - \operatorname{E}Y)^2$.

*Důkaz.* Doplníme a odečteme $\operatorname{E}Y$ a využijeme lemma z §2.2:
$$
\begin{aligned}
\operatorname{E}L(Y, \hat{Y}) = \operatorname{E}(Y - \hat{Y})^2
&= \operatorname{E}\big(Y - \operatorname{E}Y + \operatorname{E}Y - \hat{Y}\big)^2 \\
&= \operatorname{E}(Y - \operatorname{E}Y)^2 + 2\underbrace{\operatorname{E}\!\big((Y - \operatorname{E}Y)(\operatorname{E}Y - \hat{Y})\big)}_{=\,0} + \operatorname{E}(\hat{Y} - \operatorname{E}Y)^2 \\
&= \operatorname{E}(Y - \operatorname{E}Y)^2 + \operatorname{E}(\hat{Y} - \operatorname{E}Y)^2.
\end{aligned}
$$
První člen je $\operatorname{var}Y$; protože $Y = x^Tw + \varepsilon$ s konstantním $x^Tw$, je $\operatorname{var}Y = \operatorname{var}\varepsilon = \sigma^2$. Druhý člen je z definice $\operatorname{MSE}(\hat{Y})$. Tedy
$$\operatorname{E}L(Y, \hat{Y}) = \sigma^2 + \operatorname{MSE}(\hat{Y}). \qquad\square$$

**Interpretace.**
- $\sigma^2$ je **neredukovatelná chyba** daná náhodností (šumem) v modelu — nazývá se též **Bayesovská chyba** (*Bayes error*). Žádný model ji nemůže odstranit.
- $\operatorname{MSE}(\hat{Y})$ je **střední kvadratická chyba odhadu** $\hat{Y}$ jakožto **[[Bodový-odhad|bodového odhadu]]** parametru $\operatorname{E}Y = x^Tw$ (angl. *mean squared error*). Tuto část lze volbou modelu / $\lambda$ ovlivnit.

### 2.4 Rozklad druhé úrovně: MSE = vychýlení² + rozptyl

**Věta (rozklad MSE na bias a varianci).** Pro střední kvadratickou chybu odhadu platí
$$\operatorname{MSE}(\hat{Y}) = (\operatorname{bias}\hat{Y})^2 + \operatorname{var}\hat{Y},$$
kde **vychýlení** $\operatorname{bias}\hat{Y} = \operatorname{E}\hat{Y} - \operatorname{E}Y$ (angl. *bias*).

*Důkaz.* Doplníme a odečteme $\operatorname{E}\hat{Y}$ uvnitř MSE:
$$
\begin{aligned}
\operatorname{MSE}(\hat{Y}) = \operatorname{E}(\hat{Y} - \operatorname{E}Y)^2
&= \operatorname{E}\big(\hat{Y} - \operatorname{E}\hat{Y} + \operatorname{E}\hat{Y} - \operatorname{E}Y\big)^2 \\
&= \operatorname{E}(\operatorname{E}\hat{Y} - \operatorname{E}Y)^2 + \operatorname{E}(\hat{Y} - \operatorname{E}\hat{Y})^2 + 2\operatorname{E}\!\big((\hat{Y} - \operatorname{E}\hat{Y})(\operatorname{E}\hat{Y} - \operatorname{E}Y)\big).
\end{aligned}
$$
V posledním (smíšeném) členu je $(\operatorname{E}\hat{Y} - \operatorname{E}Y)$ konstanta a $\operatorname{E}(\hat{Y} - \operatorname{E}\hat{Y}) = 0$, takže člen je $2\cdot 0\cdot(\operatorname{E}\hat{Y} - \operatorname{E}Y) = 0$. Zbývá
$$
\operatorname{MSE}(\hat{Y}) = \underbrace{(\operatorname{E}\hat{Y} - \operatorname{E}Y)^2}_{(\operatorname{bias}\hat{Y})^2} + \underbrace{\operatorname{E}(\hat{Y} - \operatorname{E}\hat{Y})^2}_{\operatorname{var}\hat{Y}} = (\operatorname{bias}\hat{Y})^2 + \operatorname{var}\hat{Y}. \qquad\square
$$
(Zde $\operatorname{E}(\operatorname{E}\hat{Y} - \operatorname{E}Y)^2 = (\operatorname{E}\hat{Y} - \operatorname{E}Y)^2$, neboť výraz uvnitř je konstanta, a $\operatorname{E}(\hat{Y} - \operatorname{E}\hat{Y})^2 = \operatorname{var}\hat{Y}$ je z definice **[[Rozptyl|rozptylu]]**.)

### 2.5 Finální dekompozice a kompromis vychýlení–rozptyl

Spojením obou rozkladů dostáváme **finální dekompozici očekávané chyby**:
$$\boxed{\;\operatorname{E}L(Y, \hat{Y}) = \sigma^2 + (\operatorname{bias}\hat{Y})^2 + \operatorname{var}\hat{Y}\;}$$

Očekávaná chyba modelu je tedy součtem **neredukovatelné chyby**, **kvadrátu vychýlení** odhadu a **rozptylu** odhadu.

U hřebenové regrese lze ukázat, že (hodně zjednodušeně) platí
$$(\operatorname{bias}\hat{Y})^2 \sim \Big(1 - \frac{1}{1+\lambda}\Big)^2 \quad\text{a}\quad \operatorname{var}\hat{Y} \sim \Big(\frac{1}{1+\lambda}\Big)^2.$$
To znamená, že **s rostoucím $\lambda$ vychýlení roste a rozptyl klesá**. Toto chování v závislosti na hyperparametru modelu je typické a nazývá se **kompromis vychýlení–rozptyl** (*bias-variance tradeoff*):

- **Malé $\lambda$** (slabá regularizace) → flexibilní model: nízké vychýlení, vysoký rozptyl (přeučení, overfitting).
- **Velké $\lambda$** (silná regularizace) → tuhý model: vysoké vychýlení, nízký rozptyl (podučení, underfitting).
- $\operatorname{MSE}(\hat{Y}) = (\operatorname{bias})^2 + \operatorname{var}$ má jako součet rostoucí a klesající složky **minimum** v nějaké **optimální** hodnotě $\lambda$. Pro $\lambda = 0$ (OLS) je $\operatorname{bias} = 0$ (OLS je nestranný — viz §3), ale rozptyl bývá vysoký; mírná regularizace tak může celkovou chybu **snížit**.

Pro $\lambda = 0$ (OLS) je odhad nestranný, $\operatorname{bias}\hat{Y} = 0$, a celá $\operatorname{MSE}$ je tvořena rozptylem.

### 2.6 Odhad chyby v praxi

Hledáme optimální $\lambda$, pro které je chyba modelu nejmenší. V praxi neznáme $\operatorname{E}L$ analyticky, proto minimalizujeme **odhad MSE** na **validační množině** dat, případně odhad MSE pomocí **[[Křížová-validace|cross-validace]]**. Pro validační množinu $(Y'_i, x'_i)$ velikosti $n$:
$$\operatorname{MSE} = \frac1n\sum_{i=1}^n \big(Y'_i - {x'_i}^T\hat{w}_\lambda\big)^2.$$

---

## 3. Doplněk: modely bázových funkcí a nestrannost OLS

### 3.1 Modely bázových funkcí

Doposud byl model lineární ve vstupních proměnných, $Y = x^Tw + \varepsilon$, a umí tedy modelovat jen lineární funkci vstupů. Rozšíření za obzor linearity spočívá v nahrazení původních příznaků jejich **transformovanými variantami** — **bázovými funkcemi** (angl. *basis functions*).

Pro $M \in \mathbb{N}$ vezmeme $M$ funkcí $\varphi_1, \dots, \varphi_M : \mathbb{R}^p \to \mathbb{R}$, přidáme $\varphi_0(x) = 1$ a poskládáme do $\varphi(x) = (1, \varphi_1(x), \dots, \varphi_M(x))^T$. Modelem vztahu $Y$ a $x$ je opět lineární model (v koeficientech)
$$Y = \sum_{j=0}^M w_j\varphi_j(x) + \varepsilon = \varphi(x)^Tw + \varepsilon.$$
Maticově pro trénovací data $Y = \mathbf{\Phi}w + \varepsilon$, kde $\mathbf{\Phi} = (\varphi(x_1)^T; \dots; \varphi(x_N)^T) \in \mathbb{R}^{N,M+1}$. Postup je **zcela analogický**: minimalizujeme $\operatorname{RSS}_\lambda(w) = \|Y - \mathbf{\Phi}w\|^2 + \lambda\,w^T\mathbf{I}'w$ s řešením
$$\hat{w}_\lambda = (\mathbf{\Phi}^T\mathbf{\Phi} + \lambda\mathbf{I}')^{-1}\mathbf{\Phi}^TY, \qquad \hat{Y} = \varphi(x)^T\hat{w}_\lambda.$$

Obvyklé volby bázových funkcí: $\varphi(x) = x_i$ (přímo příznaky); $\varphi(x) = x_i^2,\ x_kx_\ell$ (mocniny a součiny → polynomiální regrese); $\varphi(x) = \log(x_i), \sqrt{x_i}, \sin(x_i)$ (nelineární transformace); $\varphi(x) = \mathbb{1}_{(a,b)}(x_i)$ (indikátory množin → kouskové modelování); $\varphi(x) = h(\|x - x_i\|)$ (**radiální bázové funkce** centrované v trénovacích bodech). Nemáme-li speciální znalost systému, volíme typicky **velké množství bázových funkcí a používáme hřebenovou regresi** (či jinou regularizaci) k potlačení přeučení.

### 3.2 Nestrannost OLS (kontext pro vychýlení)

**Věta (nestrannost OLS).** Odhad $\hat{w}^{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^TY$ získaný metodou nejmenších čtverců je za předpokladu $\operatorname{E}\varepsilon = \mathbf{0}$ **nestranný**, tj. $\operatorname{E}\hat{w}^{\mathrm{OLS}} = w$.

*Důkaz.* Z linearity střední hodnoty: $\operatorname{E}Y = \operatorname{E}(\mathbf{X}w + \varepsilon) = \mathbf{X}w$. Dále
$$\operatorname{E}\hat{w}^{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\operatorname{E}Y = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{X}w = w. \qquad\square$$

Důsledkem je nestrannost predikce: $\operatorname{E}\hat{Y} = x^T\operatorname{E}\hat{w}^{\mathrm{OLS}} = x^Tw = \operatorname{E}Y$, tedy $\operatorname{bias}\hat{Y} = \operatorname{E}\hat{Y} - \operatorname{E}Y = 0$ pro OLS. Hřebenová regrese ($\lambda > 0$) tuto nestrannost **záměrně obětuje** (zavádí vychýlení) výměnou za snížení rozptylu — což je podstata kompromisu z §2.5.

---

## Co je potřeba na zkoušku znát

### Definice
- **Hřebenová regrese:** minimalizace $\operatorname{RSS}_\lambda(w) = \|Y - \mathbf{X}w\|^2 + \lambda\sum_{i=1}^p w_i^2 = \|Y - \mathbf{X}w\|^2 + \lambda\,w^T\mathbf{I}'w$; intercept se nepenalizuje, $\mathbf{I}'$ = jednotková matice s $0$ na pozici interceptu.
- **Hřebenový odhad:** $\hat{w}_\lambda = (\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')^{-1}\mathbf{X}^TY$, predikce $\hat{Y} = x^T\hat{w}_\lambda$.
- **Vychýlení (bias):** $\operatorname{bias}\hat{Y} = \operatorname{E}\hat{Y} - \operatorname{E}Y$; **rozptyl** $\operatorname{var}\hat{Y} = \operatorname{E}(\hat{Y} - \operatorname{E}\hat{Y})^2$; **MSE odhadu** $\operatorname{MSE}(\hat{Y}) = \operatorname{E}(\hat{Y} - \operatorname{E}Y)^2$.
- **Neredukovatelná (Bayesovská) chyba:** $\sigma^2 = \operatorname{var}\varepsilon$.

### Věty
- **Normální rovnice hřebenové regrese:** $(\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')w = \mathbf{X}^TY$; Hessova matice $2(\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}')$ je pro $\lambda > 0$ **PD** → jednoznačné řešení existuje vždy.
- **Rozklad očekávané chyby (1. úroveň):** $\operatorname{E}L(Y, \hat{Y}) = \sigma^2 + \operatorname{MSE}(\hat{Y})$ (předpoklad nezávislosti train/test, kvadratická ztráta).
- **Rozklad MSE (2. úroveň):** $\operatorname{MSE}(\hat{Y}) = (\operatorname{bias}\hat{Y})^2 + \operatorname{var}\hat{Y}$.
- **Finální dekompozice:** $\operatorname{E}L(Y, \hat{Y}) = \sigma^2 + (\operatorname{bias}\hat{Y})^2 + \operatorname{var}\hat{Y}$.
- **Bias-variance tradeoff:** s rostoucím $\lambda$ vychýlení↑, rozptyl↓; MSE má minimum v optimálním $\lambda$. OLS ($\lambda = 0$) je nestranný ($\operatorname{bias} = 0$).

### Algoritmy
- **Výpočet hřebenového odhadu:** sestav $\mathbf{X}^T\mathbf{X} + \lambda\mathbf{I}'$ a $\mathbf{X}^TY$ → vyřeš (vždy regulární pro $\lambda > 0$) → $\hat{w}_\lambda$.
- **Volba $\lambda$:** minimalizace odhadu MSE na validační množině, $\operatorname{MSE} = \frac1n\sum_{i=1}^n (Y'_i - {x'_i}^T\hat{w}_\lambda)^2$, případně přes [[Křížová-validace|cross-validaci]]; před regularizací standardizovat příznaky.
- **Modely bázových funkcí:** nahraď $\mathbf{X} \to \mathbf{\Phi}$ (transformované příznaky $\varphi$), pak $\hat{w}_\lambda = (\mathbf{\Phi}^T\mathbf{\Phi} + \lambda\mathbf{I}')^{-1}\mathbf{\Phi}^TY$.
