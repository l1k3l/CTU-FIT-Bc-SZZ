---
aliases: [analýza hlavních komponent, analýzy hlavních komponent, analýzou hlavních komponent, PCA, principal component analysis, hlavní komponenta, hlavní komponenty, hlavních komponent, varianční matice, kovarianční matice, výběrová varianční matice, redukce dimenzionality]
tags: [definice, kurz/ML2]
---

# Analýza hlavních komponent

## Definice

**Analýza hlavních komponent** (angl. *principal component analysis*, **PCA**) je lineární metoda **redukce dimenzionality** (nesupervizované učení). Pro dataset $X\in\mathbb R^{N,p}$ hledá $q$-rozměrný podprostor, na který **ortogonální projekce** dat má **minimální kvadratickou chybu** — ekvivalentně podprostor, ve kterém mají projektovaná data **maximální rozptyl**.

## Postup

1. **Středování:** $x_i'=x_i-\bar x$ (nutné: $\sum_i\lVert x_i-\mu\rVert^2$ je minimální pro $\mu=\bar x$).
2. **Výběrová varianční matice** $S=\tfrac1{N-1}X'^TX'\in\mathbb R^{p,p}$ — symetrická, pozitivně semidefinitní; $S_{ij}=\widehat{\operatorname{cov}}(X_i,X_j)$ (viz [[Kovariance]]).
3. **[[Spektrální-rozklad|Spektrální rozklad]]** $S$: vlastní čísla $\lambda_1\ge\dots\ge\lambda_p\ge0$, ortonormální vlastní vektory $b_1,\dots,b_p$. Podprostor tvoří prvních $q$ vektorů.

## Hlavní komponenty

Nové příznaky $T=\mathbf V^TX'$, $T_i=b_i^TX'$, jsou **hlavní komponenty**. Platí:

- **rozptyl $i$-té komponenty $=\lambda_i$** → vybíráme směry největšího rozptylu;
- komponenty jsou **nekorelované**;
- **podíl vysvětleného rozptylu** prvních $q$ komponent: $\dfrac{\lambda_1+\dots+\lambda_q}{\lambda_1+\dots+\lambda_p}$.

## Výpočet

Buď přímý spektrální rozklad $S$, nebo (numericky stabilnější) [[SVD|singulární rozklad]] středovaného $X'$. Počet komponent $q$ se volí z „elbow“ grafu vysvětleného rozptylu.

## Související

- [[Spektrální-rozklad]]
- [[SVD]]
- [[Kovariance]]
- [[Ortogonální-báze]]
- [[Nesupervizované-učení]]
