---
studyplan: true
etapa: "4 · ML1 / ML2 — Dedecius + Holeňa"
qid: "15ML2"
examiner: "Holeňa"
topic: "Jádrová regrese: lineární model bázových funkcí, jádrový trik"
readiness: nezačato
hot: true
tags: [otázka, kurz/ML2, otázka/15, todo]
---

# Jádrová regrese

> **Otázka SZZ:** Jádrová regrese – lineární model bázových funkcí, jádrový trik.

Zdroje: BI-ML2 (FIT ČVUT), přednáška 1 — Opakování lineární a hřebenové regrese, Lineární model bázových funkcí, Duální reprezentace, Gramova matice, Jádrový trik, Jádrové funkce, Jádrové modely.

Značení: $X_1,\dots,X_p$ příznaky, $x\in\mathcal X\subseteq\mathbb R^p$ vektor příznaků, $Y$ vysvětlovaná (spojitá) proměnná, $N$ počet trénovacích bodů, $\mathbf X\in\mathbb R^{N,p}$ matice příznaků (body v řádcích), $\boldsymbol Y=(Y_1,\dots,Y_N)^T$, $w$ vektor vah, $\lambda\ge 0$ regularizační hyperparametr, $\varphi=(\varphi_1,\dots,\varphi_M)^T$ vektor bázových funkcí, $\boldsymbol\Phi\in\mathbb R^{N,M}$ matice návrhu (design matrix), $\alpha\in\mathbb R^N$ duální proměnné, $G$ Gramova matice, $k$ jádrová funkce.

---

## 1. Opakování: lineární a hřebenová regrese

### 1.1 Lineární regrese

![[Lineární-regrese#Definice]]

V bodě $x$ predikujeme $\hat Y=\hat w^T x$; ze statistického pohledu je $\hat Y$ bodovým odhadem $\mathrm E\,Y=w^T x$. Váhy se hledají **[[Metoda-nejmenších-čtverců|metodou nejmenších čtverců]]** (MNČ) minimalizací reziduálního součtu čtverců
$$\mathrm{RSS}(w)=\sum_{i=1}^N (Y_i-x_i^T w)^2=\lVert \boldsymbol Y-\mathbf X w\rVert^2.$$
Minimum řeší **normální rovnice** $\mathbf X^T\mathbf X w=\mathbf X^T\boldsymbol Y$ (odpovídá $\nabla\mathrm{RSS}(w)=0$); je-li $\mathbf X^T\mathbf X$ regulární, je řešení jediné: $\hat w_{\mathrm{OLS}}=(\mathbf X^T\mathbf X)^{-1}\mathbf X^T\boldsymbol Y$.

### 1.2 Hřebenová (ridge) regrese

Není-li $\mathbf X^T\mathbf X$ regulární (kolinearita) nebo hrozí přeučení, přidáme **$L_2$-regularizaci**. Hřebenová regrese minimalizuje
$$\mathrm{RSS}_\lambda(w)=\lVert \boldsymbol Y-\mathbf X w\rVert^2+\lambda\sum_{i=1}^p w_i^2,\qquad \lambda\ge 0.$$
Normální rovnice $\mathbf X^T\mathbf X w+\lambda I' w=\mathbf X^T\boldsymbol Y$ (kde $I'$ je jednotková matice s nulou na pozici interceptu) má pro každé $\lambda>0$ jednoznačné řešení
$$\hat w_\lambda=(\mathbf X^T\mathbf X+\lambda I')^{-1}\mathbf X^T\boldsymbol Y,$$
protože $\mathbf X^T\mathbf X+\lambda I'$ je regulární pro každé $\lambda>0$. Pro $\lambda=0$ dostáváme zpět OLS.

---

## 2. Lineární model bázových funkcí

Lineární regrese umí modelovat jen **lineární** závislost na vstupních příznacích. Základní rozšíření spočívá v **nahrazení příznaků jejich (nelineárními) transformacemi**.

**Definice (bázové funkce).** Pro $M\in\mathbb N$ uvažujme $M$ lineárně nezávislých funkcí $\varphi_1,\dots,\varphi_M:\mathcal X\to\mathbb R$. Tyto **bázové funkce** (angl. *basis functions*) transformují původní příznaky do nového $M$-rozměrného příznakového prostoru; zapíšeme je do vektorové funkce $\varphi(x)=(\varphi_1(x),\dots,\varphi_M(x))^T$.

**Model.** Vysvětlovaná proměnná je modelována jako **lineární model v novém prostoru**:
$$Y=w_1\varphi_1(x)+\dots+w_M\varphi_M(x)+\varepsilon=w^T\varphi(x)+\varepsilon,\qquad \mathrm E\,\varepsilon=0.$$
Model je **lineární v parametrech** $w$ (proto „lineární model“), ale **nelineární ve vstupních příznacích** $x$. Intercept lze schovat do vhodné konstantní bázové funkce.

**Odhad.** Pro trénovací množinu zavedeme matici návrhu $\boldsymbol\Phi\in\mathbb R^{N,M}$ s $\boldsymbol\Phi_{i,j}=\varphi_j(x_i)$, takže $\boldsymbol Y=\boldsymbol\Phi w+\varepsilon$. Minimalizujeme regularizovaný RSS
$$\mathrm{RSS}_\lambda(w)=\lVert\boldsymbol Y-\boldsymbol\Phi w\rVert^2+\lambda w^T w,$$
s normální rovnicí $\boldsymbol\Phi^T\boldsymbol\Phi w+\lambda w=\boldsymbol\Phi^T\boldsymbol Y$ a jednoznačným řešením (pro $\lambda>0$)
$$\hat w_\lambda=(\boldsymbol\Phi^T\boldsymbol\Phi+\lambda I)^{-1}\boldsymbol\Phi^T\boldsymbol Y,\qquad \hat Y=\hat w_\lambda^T\varphi(x).$$

**Obvyklé volby bázových funkcí.**

- $\varphi(x)=x_i$ — přímo příznaky (původní lineární model);
- $\varphi(x)=x_i^2,\ x_kx_\ell$ — mocniny a součiny příznaků → **polynomiální regrese**;
- $\varphi(x)=\log x_i,\ \sqrt{x_i},\ \sin x_i,\dots$ — nelineární transformace jednotlivých příznaků;
- $\varphi(x)=\mathbb 1_{(a,b)}(x_i)$ — indikátory množin (rozdělení prostoru na kousky);
- $\varphi(x)=h(\lVert x-x_i\rVert)$ — **radiální bázové funkce** centrované v trénovacích bodech.

Bez speciálních znalostí volíme **mnoho** bázových funkcí a regularizujeme (hřebenová regrese). Nevýhoda: počet bázových funkcí $M$ může být obrovský → matice $\boldsymbol\Phi^T\boldsymbol\Phi$ je $M\times M$ a její inverze stojí $O(M^3)$. Řešením je duální reprezentace.

---

## 3. Duální reprezentace a Gramova matice

Klíčové pozorování: optimální $w$ leží v podprostoru generovaném transformovanými trénovacími body. Hledejme proto $w$ ve tvaru
$$w=\boldsymbol\Phi^T\alpha,\qquad \alpha\in\mathbb R^N,$$
tj. $w$ je lineární kombinací řádků $\boldsymbol\Phi$ (vektorů $\varphi(x_1),\dots,\varphi(x_N)$). Dosazením do $\mathrm{RSS}_\lambda(w)$ dostaneme **duální účelovou funkci**
$$\mathrm{RSS}_\lambda(\alpha)=\lVert\boldsymbol Y-\boldsymbol\Phi\boldsymbol\Phi^T\alpha\rVert^2+\lambda\,\alpha^T\boldsymbol\Phi\boldsymbol\Phi^T\alpha.$$

**Věta (ekvivalence primární a duální úlohy).** Pro $\lambda>0$ platí $\min_\alpha\mathrm{RSS}_\lambda(\alpha)=\min_w\mathrm{RSS}_\lambda(w)$. Navíc: minimalizuje-li $w^*$ primární úlohu, pak $\alpha^*=\tfrac1\lambda(\boldsymbol Y-\boldsymbol\Phi w^*)$ minimalizuje duální; minimalizuje-li $\alpha^*$ duální, pak $w^*=\boldsymbol\Phi^T\alpha^*$ minimalizuje primární.

*Idea důkazu.* Z normální rovnice primární úlohy $\boldsymbol\Phi^T(\boldsymbol Y-\boldsymbol\Phi w^*)-\lambda w^*=0$ plyne $w^*=\tfrac1\lambda\boldsymbol\Phi^T(\boldsymbol Y-\boldsymbol\Phi w^*)=\boldsymbol\Phi^T\alpha^*$, takže omezení $w=\boldsymbol\Phi^T\alpha$ optimum neztrácí; protože navíc vždy $\min_\alpha\ge\min_w$ (jde o zúžení), nastává rovnost. Obrácený směr ověříme dosazením $w^*=\boldsymbol\Phi^T\alpha^*$ do primární normální rovnice. $\blacksquare$

**Gramova matice.** Definujeme
$$G=\boldsymbol\Phi\boldsymbol\Phi^T\in\mathbb R^{N,N},\qquad G_{i,j}=\varphi(x_i)^T\varphi(x_j).$$
$G$ je **symetrická a pozitivně semidefinitní**, neboť $a^TGa=\lVert\boldsymbol\Phi^T a\rVert^2\ge 0$. Duální RSS pak je
$$\mathrm{RSS}_\lambda(\alpha)=\lVert\boldsymbol Y-G\alpha\rVert^2+\lambda\,\alpha^T G\alpha.$$

**Explicitní řešení.** Z $\nabla\mathrm{RSS}_\lambda(\alpha)=-2G(\boldsymbol Y-G\alpha)+2\lambda G\alpha=0$ plyne $G(\boldsymbol Y-G\alpha-\lambda\alpha)=0$; jelikož $(G+\lambda I)$ je pro $\lambda>0$ regulární (G je PSD),
$$\boxed{\ \hat\alpha=(G+\lambda I)^{-1}\boldsymbol Y\ }.$$

**Predikce.** V bodě $x$ je $\hat Y=\hat w^T\varphi(x)=\hat\alpha^T\boldsymbol\Phi\varphi(x)$, tedy
$$\boxed{\ \hat Y=\sum_{i=1}^N\hat\alpha_i\,\varphi(x_i)^T\varphi(x)\ }.$$

Důležité: v duální reprezentaci se transformované body $\varphi(\cdot)$ vyskytují **pouze ve tvaru skalárních součinů** $\varphi(x_i)^T\varphi(x_j)$ a $\varphi(x_i)^T\varphi(x)$.

---

## 4. Jádrová funkce a jádrový trik

**Definice ([[Jádrová-funkce|jádrová funkce]]).** Funkce $k:\mathbb R^p\times\mathbb R^p\to\mathbb R$ daná
$$k(x,y)=\varphi(x)^T\varphi(y)$$
je **jádrová funkce** (angl. *kernel function*). Pak $G_{i,j}=k(x_i,x_j)$, tj. **Gramova matice je plně určena jádrovou funkcí**.

Dosazením do předchozích vzorců dostaneme **celý model vyjádřený jen pomocí $k$**:
$$\hat\alpha=(G+\lambda I)^{-1}\boldsymbol Y,\quad G_{i,j}=k(x_i,x_j),\qquad \hat Y=\sum_{i=1}^N\hat\alpha_i\,k(x_i,x).$$

**Jádrový trik (kernel trick).** Skalární součiny $\varphi(x)^T\varphi(y)$ v (případně velmi vysokorozměrném) příznakovém prostoru **nahradíme přímým výpočtem jádrové funkce** $k(x,y)$. Přirozeným rozšířením je **začít rovnou jádrovou funkcí** bez explicitního zavedení bázových funkcí — to umožňuje **implicitně** pracovat v příznakových prostorech vysoké, dokonce nekonečné dimenze, aniž bychom $\varphi$ kdy vyčíslili.

**Výpočetní výhoda.** Primární úloha invertuje matici $M\times M$ ($O(M^3)$), duální matici $N\times N$ ($O(N^3)$). Je-li $M\gg N$, je duální (jádrová) cesta výrazně levnější.

**Interpretace.** Predikce $\hat Y=\sum_i\hat\alpha_i k(x_i,x)$ je **vážená lineární kombinace** hodnot trénovacích bodů s vahami danými jádrovou funkcí — predikci tak lze interpretovat (body podobné $x$ podle $k$ přispívají více).

*Příklad (výpočetní úspora).* Regrese nad $1000$ obrázky $32\times32=1024$ pixelů. Kvadratické jádro $k(x,y)=(x^Ty+1)^2$ odpovídá lineárnímu modelu v prostoru dimenze $525\,825$. S jádrovým trikem invertujeme matici $1000\times1000$ místo $525\,825\times525\,825$.

---

## 5. Příklady jádrových funkcí

- **Lineární jádro:** $k(x,y)=x^Ty$ (pro $\varphi(x)=x$).
- **Polynomiální jádro:** $k(x,y)=(x^Ty+1)^n$. Implicitně definuje všechny monomy stupně $\le n$. Např. pro $p=2,n=2$:
$$(x^Ty+1)^2=\big(1,\sqrt2x_1,\sqrt2x_2,x_1^2,x_2^2,\sqrt2x_1x_2\big)\big(1,\sqrt2y_1,\sqrt2y_2,y_1^2,y_2^2,\sqrt2y_1y_2\big)^T,$$
tj. $6$ bázových funkcí.
- **Gaussovské (RBF) jádro:** $k(x,y)=e^{-\gamma\lVert x-y\rVert^2}$ — **radiální** bázová funkce (závisí jen na $\lVert x-y\rVert$), odpovídá **nekonečně-rozměrnému** příznakovému prostoru.

Aby vše „dobře fungovalo“, musí být $k$ **symetrická a pozitivně semidefinitní** funkce (Mercerova podmínka), typicky nezáporná. Existují i jádra pro nečíselné vstupy (řetězce, grafy).

---

## 6. Jádrové modely (kernel machines)

Skutečný model nechť je $Y=f(x)+\varepsilon$, $\mathrm E\,\varepsilon=0$. 

- Lineární model bázových funkcí hledá $f(x)=\sum_{j=1}^M w_j\varphi_j(x)$.
- **Obecný jádrový model** (angl. *kernel machine*): $f(x)=\sum_{j=1}^K\alpha_j\,k(\mu_j,x)$ se středovými body $\mu_1,\dots,\mu_K$.
- **Speciální případ** (angl. *vector machine*): středové body = trénovací body, $f(x)=\sum_{j=1}^N\alpha_j\,k(x_j,x)$.

Právě tento regresní model jsme získali pomocí jádrového triku — je to **jádrová (ridge) regrese**. Stejný trik se používá u **[[Metoda-podpůrných-vektorů|SVM]]** (otázka 16).

---

## Co je potřeba na zkoušku znát

### Definice
- **Lineární model bázových funkcí:** $Y=w^T\varphi(x)+\varepsilon$, $\varphi=(\varphi_1,\dots,\varphi_M)^T$ LN bázové funkce; lineární v $w$, nelineární v $x$.
- **Jádrová funkce:** $k(x,y)=\varphi(x)^T\varphi(y)$, symetrická, pozitivně semidefinitní.
- **Gramova matice:** $G=\boldsymbol\Phi\boldsymbol\Phi^T$, $G_{i,j}=k(x_i,x_j)$, symetrická PSD.

### Věty s důkazy
- **Ekvivalence primární/duální úlohy** ($\lambda>0$): $\min_\alpha\mathrm{RSS}_\lambda(\alpha)=\min_w\mathrm{RSS}_\lambda(w)$, převod $w^*=\boldsymbol\Phi^T\alpha^*$, $\alpha^*=\tfrac1\lambda(\boldsymbol Y-\boldsymbol\Phi w^*)$.
- **Explicitní řešení:** $\hat\alpha=(G+\lambda I)^{-1}\boldsymbol Y$ (z $\nabla\mathrm{RSS}_\lambda(\alpha)=0$, PSD $\Rightarrow$ $G+\lambda I$ regulární).

### Algoritmy / postup
- **Jádrová ridge regrese:** sestav $G_{ij}=k(x_i,x_j)$ → $\hat\alpha=(G+\lambda I)^{-1}\boldsymbol Y$ → predikce $\hat Y=\sum_i\hat\alpha_i k(x_i,x)$.
- **Jádrový trik:** nahraď $\varphi(x)^T\varphi(y)\to k(x,y)$; práce v implicitním (i nekonečně-rozměrném) prostoru.
- **Složitost:** primárně $O(M^3)$ vs. duálně $O(N^3)$ — pro $M\gg N$ vyhrává jádro.
- **Jádra:** lineární $x^Ty$, polynomiální $(x^Ty+1)^n$, Gaussovské/RBF $e^{-\gamma\lVert x-y\rVert^2}$.
