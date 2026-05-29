---
aliases: [gradient, gradientu, gradientem, gradienty, gradient funkce, nabla, totální derivace, derivace vektorové funkce, tečná rovina, gradient (vector), Jacobian]
tags: [definice, kurz/MA2]
---

# Gradient

## Definice

Buď $f:D_f\to\mathbb{R}$, $D_f\subset\mathbb{R}^n$, s konečnými všemi [[Parciální-derivace|parciálními derivacemi]] v bodě $a$. **Gradientem** $f$ v $a$ nazýváme **řádkový** vektor
$$\nabla f(a)=\operatorname{grad}f(a)=\left(\frac{\partial f}{\partial x_1}(a),\dots,\frac{\partial f}{\partial x_n}(a)\right)\in\mathbb{R}^{1,n}.$$

## Vztah k derivaci funkce

**Derivací** zobrazení $F:D_F\to\mathbb{R}^m$ ($D_F\subset\mathbb{R}^n$) v $a$ je matice $DF(a)\in\mathbb{R}^{m,n}$ taková, že
$$\lim_{x\to a}\frac{\lVert F(x)-F(a)-DF(a)(x-a)\rVert}{\lVert x-a\rVert}=0,$$
tj. $F(x)\approx F(a)+DF(a)(x-a)$ (nejlepší lineární aproximace). Pokud existuje, je $DF(a)_{i,j}=\tfrac{\partial F_i}{\partial x_j}(a)$ (jednoznačná). Pro $m=1$ je $Df(a)=\nabla f(a)$ — proto je gradient řádkový.

## Význam

- **Tečná rovina** ke grafu $z=f(x)$ v $a$: $\ z=f(a)+\nabla f(a)\cdot(x-a)$.
- **Směr největšího růstu:** $\partial_v f(a)=\langle\nabla f(a)^T\mid v\rangle$ je maximální pro $v=\nabla f(a)^T/\lVert\nabla f(a)\rVert$ (využívá gradientní metoda / spádový sestup).
- **Nutná podmínka extrému:** v [[Lokální-extrém|lokálním extrému]] s existujícím gradientem je $\nabla f(a)=\theta^T$ (**stacionární bod**).

## Související

- [[Parciální-derivace]]
- [[Hessova-matice]]
- [[Lokální-extrém]]
- [[Derivace]]
