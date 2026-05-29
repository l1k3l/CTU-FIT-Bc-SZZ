---
aliases: [parciální derivace, parciální derivaci, parciální derivací, parciálních derivací, parciální derivace podle, smíšená derivace, smíšené derivace, druhá parciální derivace, derivace ve směru, směrová derivace, partial derivative]
tags: [definice, kurz/MA2]
---

# Parciální derivace

## Definice

Buď $f:D_f\to\mathbb{R}$, $D_f\subset\mathbb{R}^n$, definovaná na okolí bodu $a$ a $j\in\hat n$. **Parciální derivací** $f$ v $a$ podle $j$-té proměnné nazýváme (existuje-li) limitu
$$\frac{\partial f}{\partial x_j}(a)=\lim_{h\to0}\frac{f(a+h e_j)-f(a)}{h},$$
kde $e_j$ je $j$-tý vektor standardní báze. Je to obyčejná [[Derivace|derivace]] funkce $g(t)=f(a+t e_j)$ v $0$.

**Výpočet:** derivujeme podle $x_j$ a na ostatní proměnné hledíme jako na konstanty (platí běžná pravidla — součin, podíl, složená funkce).

**Geometrický význam:** míra růstu/poklesu $f$ v bodě $a$ ve směru $j$-té souřadné osy.

## Vyšší a smíšené derivace

$$\frac{\partial^2 f}{\partial x_k\partial x_j}=\frac{\partial}{\partial x_k}\!\left(\frac{\partial f}{\partial x_j}\right).$$
Pořadí derivování **obecně nelze zaměnit**. Jsou-li ale všechny druhé parciální derivace spojité na okolí $a$, pak $\tfrac{\partial^2 f}{\partial x_k\partial x_j}=\tfrac{\partial^2 f}{\partial x_j\partial x_k}$ — **Schwarzova–Clairautova věta** (pak je [[Hessova-matice]] symetrická).

## Derivace ve směru

Pro jednotkový vektor $v$: $\partial_v f(a)=\lim_{h\to0}\tfrac{f(a+hv)-f(a)}{h}=\langle\nabla f(a)^T\mid v\rangle$. Největší je pro $v$ ve směru [[Gradient|gradientu]].

## Vztah k derivaci

Existence parciálních derivací **nestačí** k existenci totální derivace $Df(a)$ (matice nejlepší lineární aproximace); stačí ale spojitost všech prvních parciálních derivací na okolí. Má-li $f$ derivaci $Df(a)$, pak má i všechny parciální derivace a $Df(a)=\nabla f(a)$.

## Související

- [[Derivace]]
- [[Gradient]]
- [[Hessova-matice]]
