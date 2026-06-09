---
tags: [otázka, kurz/ML1, otázka/10, todo]
---

# 10 — Lineární regrese: MNČ, geometrie, kolinearita (zkrácená verze)

## 1. Model lineární regrese

Vysvětlovaná proměnná $Y$, příznaky $X_1,\dots,X_p$, vektor vah $w$. [[Lineární-regrese]]:
$$Y = w_0 + w_1 x_1 + \dots + w_p x_p + \varepsilon, \qquad \mathrm{E}\,\varepsilon = 0,$$
$w_0$ = **intercept**. S umělým příznakem $X_0 = 1$, $x = (1,x_1,\dots,x_p)^T$, $w = (w_0,\dots,w_p)^T$:
$$Y = w^T x + \varepsilon.$$
Trénovací data = **náhodný výběr** z modelu ($N$ párů $(Y_i,x_i)$), matice příznaků $\mathbf{X} \in \mathbb{R}^{N,p+1}$ (řádky $x_i^T$, 1. sloupec jedničky):
$$\mathbf{Y} = \mathbf{X}w + \varepsilon, \qquad \mathrm{E}\,\varepsilon = 0.$$
**Predikce:** $\hat Y = x^T\hat w$. Z $\mathrm{E}\,\varepsilon = 0$ je $\mathrm{E}\,Y = w^Tx$, takže $\hat Y$ = bodový odhad $\mathrm{E}\,Y$.

**Pravděpodobnostní interpretace (doptávají Petr i Dedecius!):** $\varepsilon$ = náhodná veličina; $\mathrm{E}\,\varepsilon=0$ ⇒ žádný systematický posun (bias). $\varepsilon_i$ i.i.d., **nejčastěji normální** $\varepsilon \sim N(0,\sigma^2)$ ⇒ $Y\mid x \sim N(w^Tx,\sigma^2)$ a OLS = MLE *(nad rámec slidů)*. **Intercept** $w_0$ = výchozí hodnota $Y$ při nulových příznacích; geometricky posouvá nadrovinu mimo počátek.

## 2. Metoda nejmenších čtverců

Kvadratická ztráta $L(Y,\hat Y) = (Y - \hat Y)^2$. [[Metoda-nejmenších-čtverců|MNČ]]: minimalizuj **reziduální součet čtverců**
$$\mathrm{RSS}(w) = \sum_{i=1}^N (Y_i - w^T x_i)^2 = \|\mathbf{Y} - \mathbf{X}w\|^2.$$
Trénování = optimalizace = hledání minima funkce více proměnných (nutná podmínka [[Gradient|gradient]] $= 0$).

**Gradient a normální rovnice:**
$$\nabla\,\mathrm{RSS} = -2\,\mathbf{X}^T(\mathbf{Y} - \mathbf{X}w) = 0 \;\Longleftrightarrow\; \boxed{\mathbf{X}^T\mathbf{X}\,w = \mathbf{X}^T\mathbf{Y}}.$$
*(Idea: parc. derivace RSS podle $w_j$, složky do vektoru.)* Rozměry: $\mathbf{X}^T\mathbf{X}\in\mathbb{R}^{p+1,p+1}$ čtvercová, $\mathbf{X}^T\mathbf{Y}\in\mathbb{R}^{p+1}$ (transpozice $\mathbf{X}^T$ kvůli navázání rozměrů).

**[[Hessova-matice|Hessova matice]]** $\mathbf{H}_{\mathrm{RSS}} = 2\mathbf{X}^T\mathbf{X}$ (nezávisí na $w$). $s^T\mathbf{X}^T\mathbf{X}s = \|\mathbf{X}s\|^2 \ge 0$ ⇒ PSD ⇒ RSS [[Konvexní-funkce|konvexní]] ⇒ každé řešení normální rovnice je **globální minimum**.

**OLS odhad** (při regulární $\mathbf{X}^T\mathbf{X}$, pak Hessián PD ⇒ ostré jediné minimum):
$$\hat w_{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}.$$

## 3. Geometrická interpretace

Minimalizace $\|\mathbf{Y} - \mathbf{X}w\|$ = nejkratší vzdálenost $\mathbf{Y}$ od **sloupcového prostoru** $\langle\mathbf{X}_{\bullet 0},\dots,\mathbf{X}_{\bullet p}\rangle = \{\mathbf{X}w\}$ (vektor $\mathbf{X}w$ je lin. kombinace sloupců).

Nejbližší bod = **ortogonální projekce**:
$$\mathbf{X}\hat w = \operatorname{proj}_{\langle\text{sloupce }\mathbf{X}\rangle}\mathbf{Y}.$$
Reziduum $\mathbf{Y} - \mathbf{X}\hat w \perp$ všem sloupcům $\Rightarrow (\mathbf{X}_{\bullet i})^T(\mathbf{Y}-\mathbf{X}\hat w)=0 \Rightarrow \mathbf{X}^T(\mathbf{Y}-\mathbf{X}\hat w)=0$ — **opět normální rovnice**. Jakékoli její řešení dává globální minimum.

## 4. Problém kolinearity

$\mathbf{X}^T\mathbf{X}$ regulární $\iff$ sloupce $\mathbf{X}$ **lineárně nezávislé** ($h(\mathbf{X}) = p+1$), neboť $\mathbf{X}s=0 \iff \mathbf{X}^T\mathbf{X}s=0$.

- **LN sloupce** ⇒ právě jedno řešení $\hat w_{\mathrm{OLS}}$.
- **LZ sloupce** ⇒ $\mathbf{X}^T\mathbf{X}$ singulární ⇒ **nekonečně mnoho řešení** (stejné, neostré globální min. RSS). Vždy nastává při $N < p+1$, nebo když jsou příznaky lin. závislé. Řešení s nejmenší normou: pseudoinverze $(\mathbf{X}^T\mathbf{X})^+$.
- **Kolinearita** = sloupce **skoro** lin. závislé: $\|\mathbf{X}u\| \gg \|\mathbf{X}v\| \doteq 0$. Inverze existuje, ale $\mathbf{X}^T\mathbf{X}$ **špatně podmíněná** (velké číslo podmíněnosti $\kappa$).

**Důsledky:** $\hat w_{\mathrm{OLS}}$ velmi citlivý na malé změny $\mathbf{Y}/\mathbf{X}$, velký rozptyl odhadu i predikcí, přeučení.

**Řešení:** redukce příznaků; regularizace — přidat člen k RSS (hřebenová regrese, $\mathbf{X}^T\mathbf{X}+\lambda E$, viz [[Lineární-regrese]] / ot. 11). Numericky stabilněji [[QR-rozklad|QR]] / [[SVD]] místo normální rovnice.

---

## Co odpovědět rychle

- **Model:** $Y = w^Tx + \varepsilon$, $\mathrm{E}\,\varepsilon=0$, intercept $w_0$, maticově $\mathbf{Y}=\mathbf{X}w+\varepsilon$; predikce $\hat Y = x^T\hat w$.
- **MNČ:** minimalizuj $\mathrm{RSS}(w) = \|\mathbf{Y}-\mathbf{X}w\|^2$; $\nabla=0 \Rightarrow$ **normální rovnice** $\mathbf{X}^T\mathbf{X}w=\mathbf{X}^T\mathbf{Y}$; Hessián $2\mathbf{X}^T\mathbf{X}$ PSD ⇒ konvexní ⇒ globální min; $\hat w_{\mathrm{OLS}}=(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$.
- **Geometrie:** $\mathbf{X}\hat w$ = ortogonální projekce $\mathbf{Y}$ na sloupcový prostor; reziduum $\perp$ sloupce → normální rovnice.
- **Kolinearita:** (skoro) LZ sloupce ⇒ $\mathbf{X}^T\mathbf{X}$ singulární/špatně podmíněná ⇒ neexistuje jednoznačné / nestabilní řešení, velký rozptyl, přeučení; řeší regularizace (hřeben. regrese) nebo redukce příznaků.
