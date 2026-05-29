---
aliases: [kvadratická forma, kvadratické formy, kvadratickou formou, kvadratických forem, definitnost, definitnosti, pozitivně definitní, pozitivně semidefinitní, negativně definitní, negativně semidefinitní, indefinitní, Sylvesterovo kritérium, úprava na čtverce, quadratic form, definiteness]
tags: [definice, kurz/MA2]
---

# Kvadratická forma

## Definice

Funkce $q:\mathbb{R}^n\to\mathbb{R}$ je **kvadratická forma**, existuje-li symetrická [[Matice|matice]] $M\in\mathbb{R}^{n,n}$ s
$$q(x)=\sum_{j,k=1}^n M_{j,k}\,x_j x_k = x^T M x = \langle x\mid Mx\rangle.$$
Vždy $q(\theta)=0$. (Předpoklad symetrie není omezující: $x^T A x = x^T\tfrac12(A+A^T)x$.) V 1D je $q(x)=\alpha x_1^2$.

## Definitnost

| typ | značka | podmínka |
|---|---|---|
| pozitivně definitní | PD | $q(x)>0$ pro každé $x\neq\theta$ |
| pozitivně semidefinitní | PSD | $q(x)\ge0$ pro každé $x$ |
| indefinitní | ID | $\exists x,y:\ q(x)>0,\ q(y)<0$ |
| negativně semidefinitní | NSD | $q(x)\le0$ pro každé $x$ |
| negativně definitní | ND | $q(x)<0$ pro každé $x\neq\theta$ |

(Konvence: každá PD je i PSD; jediná forma současně PSD i NSD je nulová.)

## Určování definitnosti

- **Vlastní čísla:** symetrická reálná matice je diagonalizovatelná s reálnými [[Vlastní-číslo|vlastními čísly]]. Forma je PD/PSD/ID/NSD/ND $\iff$ vlastní čísla $M$ jsou všechna kladná / nezáporná / s oběma znaménky / nekladná / záporná.
- **Úprava na čtverce:** vyjádříme $q(x)=\sum_{j=1}^k\alpha_j(\dots)^2$ ($k$ nezávislých čtverců). $k=n$ a všechna $\alpha_j>0\Rightarrow$ PD; $k<n$, $\alpha_j>0\Rightarrow$ PSD; smíšená znaménka $\Rightarrow$ ID; atd.
- **Sylvesterovo kritérium** (rohové minory $M_k=(M_{ij})_{i,j=1}^k$): $M$ je **PD** $\iff \det M_k>0\ \forall k$; **ND** $\iff (-1)^k\det M_k>0\ \forall k$. (Pro PSD/NSD nestačí neostré nerovnosti hlavních minorů — nutno všechny hlavní minory.)
- **Indefinitnost rychle:** různá znaménka na diagonále $M$ $\Rightarrow$ ID.

## Použití

Definitnost [[Hessova-matice|Hessovy matice]] rozhoduje o typu [[Lokální-extrém|lokálního extrému]] funkce více proměnných ve stacionárním bodě.

## Související

- [[Matice]]
- [[Vlastní-číslo]]
- [[Hessova-matice]]
- [[Determinant]]
