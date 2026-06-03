---
aliases: [metoda podpůrných vektorů, metody podpůrných vektorů, metodou podpůrných vektorů, SVM, support vector machine, podpůrný vektor, podpůrné vektory, podpůrných vektorů, separující nadrovina, odstup, margin, princip největšího odstupu, uvolněné proměnné, slack variables, ν-SVM]
tags: [definice, kurz/ML2]
---

# Metoda podpůrných vektorů

## Definice

**Metoda podpůrných vektorů** (angl. *support vector machine*, **SVM**) je klasifikátor pro binární klasifikaci $Y\in\{-1,1\}$ založený na **lineární diskriminační funkci**
$$f(x)=w^T\varphi(x)+w_0,\qquad \hat Y(x)=\operatorname{sgn} f(x),$$
jejíž **separující nadrovina** $f(x)=0$ je natrénovaná **principem největšího odstupu** (angl. *largest margin*): mezi všemi oddělujícími nadrovinami se volí ta s největší vzdáleností od nejbližšího trénovacího bodu.

## Optimalizační úloha

- **Hard margin** (separabilní data): $\min_{w,w_0}\tfrac12\lVert w\rVert^2$ za podmínek $Y_i(w^T\varphi(x_i)+w_0)\ge1$ — kvadratické programování.
- **Soft margin** (neseparabilní data): zavedení **uvolněných proměnných** $\xi_i\ge0$ a penalizace
$$\min_{w,w_0,\xi}\ \tfrac12\lVert w\rVert^2+C\sum_i\xi_i,\qquad Y_i(w^T\varphi(x_i)+w_0)\ge1-\xi_i,\ \ \xi_i\ge0.$$
Parametr $C$ řídí kompromis chyby/odstup (větší $C$ = slabší regularizace); $C=\tfrac1{\nu N}$ dává $\nu$-SVM.

## Duál a jádrový trik

Lagrangeův duál: $\max_a\ \sum_i a_i-\tfrac12\sum_{i,j}a_ia_jY_iY_jk(x_i,x_j)$ za $0\le a_i\le C$, $\sum_i a_iY_i=0$. Body se vyskytují jen ve skalárních součinech → **[[Jádrová-funkce|jádrový trik]]** umožňuje nelineární klasifikaci. Výsledek je jádrový model
$$f(x)=\sum_j a_jY_j\,k(x,x_j)+w_0.$$

## Podpůrné vektory

Řešení je **řídké**: $a_j=0$ pro správně klasifikované body mimo pás odstupu. Body s $a_j>0$ jsou **podpůrné vektory** a jediné určují polohu nadroviny ($0<a_j<C$ na hraně pásu, $a_j=C$ uvnitř pásu / chyba).

## Související

- [[Jádrová-funkce]]
- [[Norma]]
- [[Logistická-regrese]]
- [[Konvexní-funkce]]
