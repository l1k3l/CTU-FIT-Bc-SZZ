---
aliases: [primitivní funkce, primitivní funkci, primitivní funkcí, primitivní funkce k, neurčitý integrál, neurčitého integrálu, neurčitým integrálem, integrand, integrační konstanta, antiderivative, indefinite integral, primitive function]
tags: [definice, kurz/MA2]
---

# Primitivní funkce

## Definice (primitivní funkce)

Nechť $f$ je definovaná na intervalu $(a,b)$, kde $-\infty\le a<b\le+\infty$. Funkci $F$ splňující
$$F'(x)=f(x)\quad\text{pro každé }x\in(a,b)$$
nazýváme **primitivní funkcí** k $f$ na $(a,b)$. Taková $F$ je diferencovatelná, a tedy [[Spojitost|spojitá]] na $(a,b)$.

## Jednoznačnost a existence

- **Jednoznačnost (až na konstantu):** je-li $F$ primitivní k $f$ na $(a,b)$, pak $G$ je rovněž primitivní $\iff$ $G(x)=F(x)+C$ pro nějakou konstantu $C\in\mathbb{R}$. (Plyne z $(F-G)'=0\Rightarrow F-G$ konstantní.)
- **Postačující podmínka existence:** je-li $f$ spojitá na $(a,b)$, primitivní funkce existuje.

## Neurčitý integrál

Množinu **všech** primitivních funkcí k $f$ na $(a,b)$ nazýváme **neurčitým integrálem** a značíme
$$\int f(x)\,dx = F(x)+C.$$
$f$ je **integrand**, $x$ integrační proměnná, $C$ integrační konstanta. Je to procedura inverzní k [[Derivace|derivaci]]: $\big(\int f\big)'=f$ a $\int g'\,dx=g+C$.

## Vlastnosti

- **Linearita:** $\int(f+g)=\int f+\int g$, $\ \int(\alpha f)=\alpha\int f$.
- **Per partes:** $\int fg = fG-\int f'G$ (z derivace součinu).
- **Substituce:** $\int f(\varphi(x))\varphi'(x)\,dx = F(\varphi(x))+C$ (z derivace složené funkce).

Ne každá elementární funkce má elementární primitivní funkci (např. $\int e^{-x^2}dx$, $\int\tfrac{\sin x}{x}dx$).

## Související

- [[Riemannův-integrál]]
- [[Derivace]]
- [[Spojitost]]
