---
aliases: [Riemannův integrál, Riemannova integrálu, Riemannovým integrálem, určitý integrál, určitého integrálu, určitým integrálem, dolní součet, horní součet, dolní integrál, horní integrál, dělení intervalu, Newtonova formule, Riemann integral, definite integral]
tags: [definice, kurz/MA2]
---

# Riemannův integrál

## Konstrukce (Darbouxova)

Buď $f$ omezená na $J=\langle a,b\rangle$ a $\sigma=\{a=x_0<x_1<\dots<x_n=b\}$ **dělení** intervalu ($\Delta_i=x_i-x_{i-1}$). Definujeme **dolní** a **horní součet**
$$s(\sigma,f)=\sum_{i=1}^n \Delta_i\!\!\inf_{\langle x_{i-1},x_i\rangle}\!\!f,\qquad S(\sigma,f)=\sum_{i=1}^n \Delta_i\!\!\sup_{\langle x_{i-1},x_i\rangle}\!\!f,$$
a **dolní/horní integrál** jako $\sup_\sigma s(\sigma,f)$, resp. $\inf_\sigma S(\sigma,f)$.

## Definice

Shodují-li se dolní a horní integrál (a jsou konečné), nazýváme jejich společnou hodnotu **Riemannovým integrálem** $f$ na $\langle a,b\rangle$ a značíme $\int_a^b f(x)\,dx$. Geometricky: obsah plochy mezi grafem a osou $x$ (se znaménkem).

- **Postačující podmínka existence:** $f$ [[Spojitost|spojitá]] na $\langle a,b\rangle$ $\Rightarrow$ $\int_a^b f$ existuje a rovná se $\lim_{n}s(\sigma_n,f)=\lim_n S(\sigma_n,f)$ pro libovolnou normální posloupnost dělení ($\nu(\sigma_n)\to0$).
- Neexistuje např. pro Dirichletovu funkci (dolní integrál $0$, horní $1$).

## Vlastnosti

- **Linearita:** $\int_a^b(f+g)=\int_a^b f+\int_a^b g$, $\int_a^b cf = c\int_a^b f$.
- **Aditivita v mezích:** $\int_a^b f=\int_a^c f+\int_c^b f$.
- **Monotonie:** $f\le g$ na $\langle a,b\rangle\Rightarrow\int_a^b f\le\int_a^b g$.

## Newtonova–Leibnizova formule

Je-li $f$ spojitá na $\langle a,b\rangle$ s [[Primitivní-funkce|primitivní funkcí]] $F$, pak
$$\int_a^b f(x)\,dx = F(b)-F(a) = \big[F(x)\big]_a^b.$$
Propojuje určitý integrál s primitivní funkcí (důkaz přes Lagrangeovu větu o přírůstku). Umožňuje počítat integrál bez limitní definice.

## Související

- [[Primitivní-funkce]]
- [[Spojitost]]
- [[Číselná-řada]]
