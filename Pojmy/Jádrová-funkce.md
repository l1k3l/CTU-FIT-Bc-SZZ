---
aliases: [jádrová funkce, jádrové funkce, jádrovou funkcí, jádro, jádra, jádrem, jádrový trik, jádrového triku, kernel, kernel function, kernel trick, Gramova matice, Gaussovské jádro, RBF jádro, polynomiální jádro, lineární jádro]
tags: [definice, kurz/ML2]
---

# Jádrová funkce

## Definice

**Jádrová funkce** (angl. *kernel function*) je funkce $k:\mathcal X\times\mathcal X\to\mathbb R$, kterou lze zapsat jako **skalární součin** transformací vstupů nějakou vektorovou funkcí bázových funkcí $\varphi:\mathcal X\to\mathbb R^M$:
$$k(x,y)=\varphi(x)^T\varphi(y).$$
Aby funkce $k$ byla jádrem (a odpovídala nějakému $\varphi$), musí být **symetrická a pozitivně semidefinitní** (Mercerova podmínka): pro libovolné body je matice $[k(x_i,x_j)]_{i,j}$ symetrická PSD.

## Jádrový trik

**Jádrový trik** (angl. *kernel trick*): v algoritmu, kde se vstupy vyskytují pouze ve tvaru skalárních součinů $\varphi(x)^T\varphi(y)$, nahradíme tyto součiny přímým výpočtem $k(x,y)$. Není pak třeba $\varphi$ explicitně vyčíslovat — lze **implicitně pracovat v příznakovém prostoru vysoké (i nekonečné) dimenze**. Často se rovnou volí jádro $k$ bez konstrukce $\varphi$.

**Gramova matice** $G\in\mathbb R^{N,N}$, $G_{i,j}=k(x_i,x_j)$, je symetrická a pozitivně semidefinitní; shrnuje všechny párové skalární součiny trénovacích bodů.

## Příklady jader

- **lineární:** $k(x,y)=x^Ty$;
- **polynomiální:** $k(x,y)=(x^Ty+1)^n$ (implicitně všechny monomy stupně $\le n$);
- **Gaussovské / RBF:** $k(x,y)=e^{-\gamma\lVert x-y\rVert^2}$ — radiální (závisí jen na $\lVert x-y\rVert$), odpovídá nekonečně-rozměrnému prostoru.

## Použití v ML2

- **Jádrová regrese** (otázka 15) — duální reprezentace ridge regrese: $\hat\alpha=(G+\lambda I)^{-1}\boldsymbol Y$, predikce $\hat Y=\sum_i\hat\alpha_i k(x_i,x)$.
- **[[Metoda-podpůrných-vektorů|SVM]]** (otázka 16) — jádrový trik převede lineární klasifikátor na nelineární.

## Související

- [[Skalární-součin]]
- [[Lineární-regrese]]
- [[Metoda-podpůrných-vektorů]]
- [[Norma]]
