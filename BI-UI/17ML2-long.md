---
tags: [otázka, kurz/ML2, otázka/17, todo]
---

# Redukce dimenzionality — PCA a LLE

> **Otázka SZZ:** Redukce dimenzionality – analýza hlavních komponent (PCA), lokálně lineární vnoření.

Zdroje: BI-ML2 (FIT ČVUT), přednášky 3 a 4 — Motivace (prokletí dimenzionality, hypotéza variet), Ortogonální projekce, Analýza hlavních komponent (PCA), Manifold learning — lokálně lineární vnoření (LLE).

Značení: $X\in\mathbb R^{N,p}$ dataset ($N$ bodů v řádcích, $p$ příznaků), $V\subseteq\mathbb R^p$ podprostor dimenze $q$, $\mathbf V\in\mathbb R^{p,q}$ matice s ortonormální bází $V$ ve sloupcích, $\bar x$ výběrový průměr, $X'$ středovaný dataset, $\lambda_i$ vlastní čísla, $b_i$ vlastní vektory.

---

## 1. Motivace: prokletí dimenzionality a hypotéza variet

**Prokletí dimenzionality** (z BI-ML1): v jednotkové krychli dimenze $d$ s rovnoměrně rozloženými body leží v podkrychli o hraně $(1-\varepsilon)$ jen $(1-\varepsilon)^d\cdot100\%$ bodů — pro velké $d$ téměř nic (např. $d=100$, slupka tloušťky $0{,}01$ obsahuje $86{,}7\%$ bodů). Body jsou tedy ve vysoké dimenzi řídké a daleko od sebe → predikce vyžaduje velké extrapolace a je nespolehlivá. Doplnit data nelze: pro $100$ příznaků by bylo třeba $10^{100}$ bodů (víc než atomů ve vesmíru $\sim10^{80}$).

**Hypotéza variet** (angl. *manifold hypothesis*): reálná mnohorozměrná data se ve skutečnosti vyskytují **podél variet** (nelineárních obdob lineárních variet) **mnohem menší dimenze** (např. MNIST: $784$ pixelů, ale platných číslic je nepatrný zlomek; švýcarská rolka: 2D plocha zatočená ve 3D). Dává proto smysl hledat zobrazení dat do prostoru menší dimenze.

**Dvě třídy metod redukce dimenzionality** (jde o **[[Nesupervizované-učení|nesupervizované učení]]**):

- **lineární projekce** — ortogonální projekce na lineární podprostor (PCA);
- **manifold learning** — nelineární metody zachycující obecnou strukturu variety (LLE, Isomap, t-SNE, UMAP).

---

## 2. Ortogonální projekce na podprostor

Mějme $q$-rozměrný podprostor $V\subseteq\mathbb R^p$ se standardním **[[Skalární-součin|skalárním součinem]]**. Každý $x\in\mathbb R^p$ se **jednoznačně** rozloží
$$x=v_x+u_x,\qquad v_x\in V,\ u_x\perp V,$$
kde $v_x$ je **ortogonální projekce** $x$ na $V$. Mějme **[[Ortogonální-báze|ortonormální bázi]]** $b_1,\dots,b_p$ tak, že $b_1,\dots,b_q$ tvoří bázi $V$. Pak $x=\sum_i\tau_i b_i$ s $\tau_i=x^Tb_i$ a
$$v_x=\sum_{i=1}^q\tau_i b_i,\qquad u_x=\sum_{i=q+1}^p\tau_i b_i.$$

Maticově (s $\mathbf V\in\mathbb R^{p,q}$ obsahující $b_1,\dots,b_q$ ve sloupcích, $\mathbf V^T\mathbf V=I_q$): souřadnice projekce $t_x=\mathbf V^Tx\in\mathbb R^q$, samotná projekce $v_x=\mathbf V t_x=\mathbf V\mathbf V^Tx$. Pro celý dataset:
$$T_q=X\mathbf V\in\mathbb R^{N,q}\quad(\text{redukovaná reprezentace}),\qquad X\mathbf V\mathbf V^T\in\mathbb R^{N,p}\quad(\text{projekce v původním prostoru}).$$
Z ortogonality plyne **Pythagoras**: $\lVert x\rVert^2=\lVert v_x\rVert^2+\lVert u_x\rVert^2$ a $\lVert v_x\rVert^2=\lVert t_x\rVert^2$.

---

## 3. Analýza hlavních komponent (PCA)

**Cíl.** Pro dané $q$ najít podprostor $V$ minimalizující **kvadratickou chybu projekce** datasetu, $\sum_i\lVert x_i'-v_{x_i'}\rVert^2=\sum_i\lVert u_{x_i'}\rVert^2$.

**Krok 1 — středování.** Nejprve dataset vystředíme: $x_i'=x_i-\bar x$, kde $\bar x=\frac1N\sum_i x_i$. Středování je nutné: výraz $\sum_i\lVert x_i-\mu\rVert^2$ nabývá minima pro $\mu=\bar x$, takže nezávisle na $V$ vede středování k nejmenší možné chybě projekce.

**Krok 2 — varianční matice.** Dataset chápeme jako **[[Náhodný-výběr|náhodný výběr]]** z rozdělení příznaků. **Výběrová [[Kovariance|kovariance]]** příznaků je
$$\widehat{\operatorname{cov}}(X_i,X_j)=\tfrac1{N-1}\sum_{k}(x_{k;i}-\bar x_i)(x_{k;j}-\bar x_j)=\tfrac1{N-1}(X'^TX')_{ij},$$
tedy **výběrová varianční matice** je $S=\tfrac1{N-1}X'^TX'\in\mathbb R^{p,p}$ — **symetrická, pozitivně semidefinitní** (na diagonále výběrové rozptyly).

**Krok 3 — řešení (PCA).** Symetrická PSD matice $S$ má **[[Spektrální-rozklad|spektrální rozklad]]**: ortonormální bázi vlastních vektorů $b_1,\dots,b_p$ s nezápornými vlastními čísly $\lambda_1\ge\dots\ge\lambda_p\ge0$ ($X'^TX'b_i=(N-1)\lambda_i b_i$). **Podprostor $V$ tvoří prvních $q$ vlastních vektorů** (s největšími vlastními čísly). Tento postup je **analýza hlavních komponent (PCA)**.

**Optimalita (důkaz).** Pro tuto volbu je chyba projekce
$$\sum_{i=1}^N\lVert u_{x_i'}\rVert^2=\sum_{j=q+1}^p b_j^T X'^TX' b_j=(N-1)\sum_{j=q+1}^p\lambda_j=(N-1)(\lambda_{q+1}+\dots+\lambda_p).$$
Pro libovolný jiný $q$-rozměrný podprostor je chyba $(N-1)\sum_i\gamma_i\lambda_i$ s $0\le\gamma_i\le1$, $\sum_i\gamma_i=p-q$, a nikdy nemůže být menší → výběr $q$ největších vlastních čísel je optimální. Ekvivalentně (díky Pythagoru) minimalizace chyby = **maximalizace rozptylu** projektovaných bodů.

**Hlavní komponenty.** Nové příznaky $T=\mathbf V^TX'$, $T_i=b_i^TX'$, se nazývají **hlavní komponenty** (angl. *principal components*). Jejich statistická interpretace:
$$\bar T_i=0,\qquad \widehat{\operatorname{cov}}(T_i,T_j)=\begin{cases}\lambda_i & i=j,\\ 0 & i\ne j.\end{cases}$$

- **Rozptyl $i$-té hlavní komponenty $=\lambda_i$** → výběrem $q$ komponent vybíráme **směry největšího rozptylu** dat.
- Hlavní komponenty jsou **nekorelované** (mimodiagonální kovariance jsou nulové).
- **Podíl vysvětleného rozptylu** $q$ komponentami: $\dfrac{\lambda_1+\dots+\lambda_q}{\lambda_1+\dots+\lambda_p}$.

**Numerika a volba $q$.**

- Výpočet: buď přímý **[[Spektrální-rozklad|spektrální rozklad]]** matice $\tfrac1{N-1}X'^TX'$, nebo **[[SVD|singulární rozklad]]** matice $X'$ (numericky stabilnější).
- Počet komponent $q$: z **„elbow“ grafu** (vysvětlený rozptyl vs. $q$, hledá se bod zlomu).
- Pro $q=p$ se neztratí žádná informace — jen přechod do ortonormální báze; sloupce $T_q$ jsou pak ortogonální ($T_q^TT_q=(N-1)\Lambda$).

---

## 4. Lokálně lineární vnoření (LLE)

**Problém PCA:** zachycuje jen **globální lineární** strukturu; selhává u nelineárních variet (švýcarská rolka). **Manifold learning** se soustředí na **lokální** strukturu.

**Lokálně lineární vnoření** (angl. *locally linear embedding*, **LLE**) sleduje, jak každý bod závisí **lineárně na svém okolí**, a hledá nízkodimenzionální reprezentaci, která tyto **lokální vztahy zachová**. Je **dvoufázové**:

**Fáze 1 — váhy lokálních vztahů.** Pro každý bod $x_i$ najdi jeho $k$ nejbližších sousedů a váhy $w_{i,j}$ tak, aby $x_i$ byl co nejlépe rekonstruován jako vážený průměr sousedů:
$$\mathbf W^*=\arg\min_{\mathbf W}\sum_{i=1}^N\Big\lVert x_i-\sum_j w_{i,j}x_j\Big\rVert^2,\quad\text{za}\quad w_{i,j}=0\ \text{pro}\ x_j\notin k\text{-NN}(x_i),\ \ \sum_j w_{i,j}=1.$$

**Fáze 2 — vnoření.** Najdi $q$-rozměrnou reprezentaci $z_i\in\mathbb R^q$, která **zachová stejné váhy**:
$$\mathbf Z^*=\arg\min_{\mathbf Z}\sum_{i=1}^N\Big\lVert z_i-\sum_j w_{i,j}^*\,z_j\Big\rVert^2.$$

Body $z_i^*$ tvoří výsledné vnoření. (Idea: nejprve se z původních dat naučí lokální struktura — váhy; poté se najde nízkodimenzionální reprezentace, která ji nejlépe zachovává.)

**Poznámka.** Je-li $k>p$, jsou sousedé lineárně závislí → používá se **modifikované LLE**. Další metody manifold learningu: MDS, Isomap, t-SNE, UMAP.

---

## Co je potřeba na zkoušku znát

### Definice
- **Hypotéza variet:** reálná data leží podél variet menší dimenze.
- **Ortogonální projekce:** $x=v_x+u_x$, $v_x=\mathbf V\mathbf V^Tx$, redukce $T_q=X\mathbf V$ ($\mathbf V^T\mathbf V=I_q$).
- **Varianční matice (výběrová):** $S=\tfrac1{N-1}X'^TX'$ — symetrická PSD; diagonála = výběrové rozptyly.
- **Hlavní komponenty:** $T=\mathbf V^TX'$, $T_i=b_i^TX'$; rozptyl $T_i=\lambda_i$, nekorelované.

### Věty s důkazy
- **Optimalita PCA:** podprostor z $q$ vlastních vektorů $S$ s největšími $\lambda_i$ minimalizuje chybu projekce $(N-1)(\lambda_{q+1}+\dots+\lambda_p)$; minimalizace chyby $\equiv$ maximalizace rozptylu (Pythagoras).
- **Nutnost středování:** $\sum_i\lVert x_i-\mu\rVert^2$ min. pro $\mu=\bar x$.

### Algoritmy
- **PCA:** středování → varianční matice $S$ → spektrální rozklad (nebo SVD $X'$) → $\mathbf V$ = $q$ vlastních vektorů s největšími $\lambda$ → $T_q=X'\mathbf V$. Volba $q$ z elbow grafu / vysvětleného rozptylu $\frac{\sum_{i\le q}\lambda_i}{\sum_i\lambda_i}$.
- **LLE (dvoufázové):** (1) váhy $\mathbf W^*$ z $k$-NN rekonstrukce ($\sum_j w_{ij}=1$); (2) vnoření $\mathbf Z^*$ zachovávající váhy v $\mathbb R^q$.
