---
aliases: [Hessova matice, Hessovy matice, Hessovou maticí, Hesseova matice, Hesseovy matice, Hesseovou maticí, Hessián, hessián, matice druhých derivací, Hessian, Hessian matrix]
tags: [definice, kurz/MA2]
---

# Hessova matice

## Definice

Buď $f:D_f\to\mathbb{R}$, $D_f\subset\mathbb{R}^n$. **Hessovou maticí** $\nabla^2 f(a)\in\mathbb{R}^{n,n}$ nazýváme matici druhých [[Parciální-derivace|parciálních derivací]]
$$\nabla^2 f(a)=\left(\frac{\partial^2 f}{\partial x_i\,\partial x_j}(a)\right)_{i,j=1}^n=\begin{pmatrix}\frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1\partial x_n}\\ \vdots & \ddots & \vdots\\ \frac{\partial^2 f}{\partial x_n\partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n^2}\end{pmatrix}(a).$$
Je to derivace [[Gradient|gradientu]] (resp. derivace) chápaná jako zobrazení $\mathbb{R}^n\to\mathbb{R}^n$. (Pozn.: „Hessián“ v české terminologii často značí $\det\nabla^2 f$.)

## Symetrie

Pořadí smíšených derivací obecně **nelze zaměnit**. Jsou-li ale všechny druhé parciální derivace spojité na okolí $a$, je $\nabla^2 f(a)$ **symetrická** (**Schwarzova–Clairautova věta**) — typický případ. Symetrickou matici lze chápat jako [[Kvadratická-forma|kvadratickou formu]].

## Použití (extrémy)

Hessova matice je analogem druhé derivace; o typu [[Lokální-extrém|extrému]] ve stacionárním bodě $a$ ($\nabla f(a)=\theta^T$) rozhoduje její **definitnost**:
- $\nabla^2 f(a)$ **PD** $\Rightarrow$ ostré lokální **minimum**;
- **ND** $\Rightarrow$ ostré lokální **maximum**;
- **ID** $\Rightarrow$ **sedlový bod** (extrém nenastává);
- **PSD/NSD** (a ne definitní) $\Rightarrow$ kritérium nerozhoduje.

## Související

- [[Parciální-derivace]]
- [[Gradient]]
- [[Kvadratická-forma]]
- [[Lokální-extrém]]
