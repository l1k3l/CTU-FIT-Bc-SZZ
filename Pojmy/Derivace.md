---
aliases: [derivace, derivaci, derivací, derivace funkce, diferencovatelná, diferencovatelnost, tečna, tečny, tečnu, směrnice, derivative, differentiable, tangent]
tags: [definice, kurz/MA1]
---

# Derivace

## Definice

Nechť $f$ je definovaná na okolí bodu $a \in \mathbb{R}$. **Derivací** $f$ v bodě $a$ nazýváme (existuje-li) limitu
$$f'(a) = \lim_{x\to a} \frac{f(x) - f(a)}{x - a} = \lim_{h\to 0} \frac{f(a+h) - f(a)}{h} \in \mathbb{R}^*.$$
Je-li tato limita **konečná** ($f'(a) \in \mathbb{R}$), je $f$ **diferencovatelná** v $a$. **Derivace** $f'$ je funkce $x \mapsto f'(x)$ na množině bodů, kde existuje konečná derivace.

## Geometrický význam

$f'(a)$ je **směrnice tečny** grafu v bodě $(a, f(a))$: $f'(a) = \operatorname{tg}\alpha$, kde $\alpha$ je úhel tečny s osou $x$. Vzniká limitním procesem ze směrnic sečen $\frac{f(z)-f(a)}{z-a}$.

**Tečna** v $a$ (existuje-li $f'(a)$):
- $y = f(a) + f'(a)(x-a)$, je-li $f'(a) \in \mathbb{R}$;
- svislá přímka $x = a$, je-li $f$ spojitá v $a$ a $f'(a) = \pm\infty$.

## Vztah ke spojitosti

$f$ diferencovatelná v $a$ $\Rightarrow$ $f$ [[Spojitost|spojitá]] v $a$. **Obráceně neplatí** (např. $|x|$ v $0$ je spojitá, ale nemá derivaci — „zlom").

## Pravidla

- $(f+g)' = f' + g'$, $(cf)' = cf'$;
- **součin (Leibniz):** $(fg)' = f'g + fg'$;
- **podíl:** $\left(\frac fg\right)' = \frac{f'g - fg'}{g^2}$ ($g(a)\neq 0$);
- **složená funkce (řetízkové pravidlo):** $(f\circ g)'(a) = f'(g(a))\cdot g'(a)$;
- **inverzní funkce:** $f'(c) = \dfrac{1}{(f^{-1})'(f(c))}$.

Vyšší derivace: $f'' = (f')'$, …, $f^{(n)} = (f^{(n-1)})'$.

## Související

- [[Spojitost]]
- [[Lokální-extrém]]
- [[Konvexní-funkce]]
- [[Limita-funkce]]
