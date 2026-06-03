---
tags: [otázka, kurz/ML2, otázka/17, todo]
---

# 17 — Redukce dimenzionality: PCA a LLE (zkrácená verze)

## 1. Motivace

**Prokletí dimenzionality:** ve vysoké dimenzi jsou body řídké a daleko (slupka krychle). **Hypotéza variet:** reálná data leží podél variet menší dimenze → hledáme zobrazení do nižší dimenze. Jde o [[Nesupervizované-učení|nesupervizované učení]].

Dvě třídy: **lineární projekce** (PCA) vs. **manifold learning** (LLE, t-SNE, ...).

## 2. Ortogonální projekce

Podprostor $V\subseteq\mathbb R^p$ dim. $q$, [[Ortogonální-báze|ortonormální báze]] $b_1,\dots,b_p$. Rozklad $x=v_x+u_x$ ($v_x\in V$, $u_x\perp V$). S $\mathbf V\in\mathbb R^{p,q}$ ($\mathbf V^T\mathbf V=I_q$):
$$t_x=\mathbf V^Tx,\quad v_x=\mathbf V\mathbf V^Tx,\qquad T_q=X\mathbf V\ (\text{redukce}).$$
Pythagoras: $\lVert x\rVert^2=\lVert v_x\rVert^2+\lVert u_x\rVert^2$.

## 3. Analýza hlavních komponent (PCA)

**Cíl:** najít $V$ minimalizující chybu projekce $\sum_i\lVert u_{x_i'}\rVert^2$.

1. **Středování** $x_i'=x_i-\bar x$ (min. $\sum\lVert x_i-\mu\rVert^2$ je v $\mu=\bar x$).
2. **Varianční matice** $S=\frac1{N-1}X'^TX'$ — symetrická PSD (výběrová [[Kovariance|kovariance]]).
3. **PCA:** [[Spektrální-rozklad|spektrální rozklad]] $S$ → vlastní čísla $\lambda_1\ge\dots\ge\lambda_p\ge0$, vlastní vektory $b_i$; $\mathbf V$ = prvních $q$ vektorů.

**Optimalita:** chyba projekce $=(N-1)(\lambda_{q+1}+\dots+\lambda_p)$ — minimální. Ekvivalentně: **max. rozptylu** projekce.

**Hlavní komponenty** $T=\mathbf V^TX'$:
- rozptyl $T_i=\lambda_i$ → směry **největšího rozptylu**;
- komponenty **nekorelované** ($\widehat{\operatorname{cov}}(T_i,T_j)=0$ pro $i\ne j$);
- vysvětlený rozptyl $q$ komp.: $\frac{\lambda_1+\dots+\lambda_q}{\lambda_1+\dots+\lambda_p}$.

**Výpočet:** spektrální rozklad $S$, nebo [[SVD]] matice $X'$ (stabilnější). Volba $q$: elbow graf. $q=p$ → jen rotace do ortonormální báze.

## 4. Lokálně lineární vnoření (LLE)

Manifold learning — zachovává **lokální** strukturu (PCA jen globální lineární).

**Dvoufázové:**
1. **Váhy:** pro každý $x_i$ jeho $k$ nejbližších sousedů; $\mathbf W^*=\arg\min\sum_i\lVert x_i-\sum_j w_{ij}x_j\rVert^2$ za $w_{ij}=0$ mimo $k$-NN, $\sum_j w_{ij}=1$.
2. **Vnoření:** $\mathbf Z^*=\arg\min\sum_i\lVert z_i-\sum_j w_{ij}^* z_j\rVert^2$, $z_i\in\mathbb R^q$ — zachová váhy.

($k>p$ → modifikované LLE. Další: MDS, Isomap, t-SNE, UMAP.)

---

## Co odpovědět rychle
- **Redukce dim.** kvůli prokletí dimenzionality; hypotéza variet → lineární (PCA) vs. manifold (LLE).
- **PCA:** středovat → $S=\frac1{N-1}X'^TX'$ → vlastní vektory s největšími $\lambda$ = hlavní komponenty; rozptyl komp. $=\lambda_i$, nekorelované, max. rozptyl / min. chyba projekce. Výpočet přes spektrální rozklad / SVD.
- **LLE:** (1) lokální váhy z $k$-NN ($\sum_j w_{ij}=1$), (2) nízkodim. vnoření zachovávající tytéž váhy.
