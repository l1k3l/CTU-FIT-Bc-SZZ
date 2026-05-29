---
aliases: [číselná řada, číselné řady, číselnou řadou, řada, řadu, řady, řad, částečný součet, částečné součty, konvergentní řada, divergentní řada, absolutní konvergence, absolutně konvergentní, geometrická řada, harmonická řada, number series, series]
tags: [definice, kurz/MA2]
---

# Číselná řada

## Definice

Pro [[Posloupnost|posloupnost]] $(a_k)_{k=0}^\infty$ nazýváme formální výraz
$$\sum_{k=0}^\infty a_k = a_0+a_1+a_2+\cdots$$
**číselnou řadou**. **Posloupnost částečných součtů** je $s_n=\sum_{k=0}^n a_k$. Řada je **konvergentní**, je-li $(s_n)$ [[Limita-posloupnosti|konvergentní]]; její **součet** je $\lim_{n\to\infty}s_n$. Jinak je **divergentní**.

(Pozor: posloupnost $(a_k)$ vs. řada $\sum a_k$ — řada je posloupnost jejích částečných součtů. Konvergence se nezmění změnou konečně mnoha členů.)

## Důležité řady

- **Geometrická:** $\sum_{k=0}^\infty q^k=\dfrac{1}{1-q}$ pro $|q|<1$ (jinak diverguje).
- **Harmonická:** $\sum_{k=1}^\infty \tfrac1k$ **diverguje**, ač $a_k\to0$.
- **$\sum k^\alpha$** konverguje $\iff \alpha<-1$.

## Absolutní konvergence

Řada $\sum a_k$ je **absolutně konvergentní**, konverguje-li $\sum|a_k|$. Platí: **absolutní konvergence $\Rightarrow$ konvergence** (ne naopak — viz $\sum\tfrac{(-1)^k}{k}$).

## Kritéria konvergence

- **Nutná podmínka:** $\sum a_k$ konverguje $\Rightarrow a_k\to0$ (vyvrací konvergenci, nestačí k ní).
- **Srovnávací:** $0\le|a_k|\le b_k$, $\sum b_k$ konv. $\Rightarrow \sum a_k$ abs. konv.
- **d'Alembertovo (podílové):** $a_k>0$; $\lim\tfrac{a_{k+1}}{a_k}<1\Rightarrow$ konv., $>1\Rightarrow$ div.
- **Leibnizovo:** $(a_k)$ monotónní $\to0\Rightarrow\sum(-1)^k a_k$ konverguje.
- **Integrální:** $f$ spojitá monotónní, $f(n)=a_n>0$; $\sum a_n$ konv. $\iff\int_1^\infty f$ konv.

## Související

- [[Posloupnost]]
- [[Limita-posloupnosti]]
- [[Riemannův-integrál]]
- [[Asymptotická-notace]]
