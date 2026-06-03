---
aliases: [Bayesova věta, Bayesovy věty, Bayesovu větu, Bayesův vzorec, Bayesovo pravidlo, Bayes, apriorní pravděpodobnost, aposteriorní pravděpodobnost, věta o úplné pravděpodobnosti, MAP, maximum a posteriori]
tags: [definice, kurz/ML2, kurz/PST]
---

# Bayesova věta

## Definice

**Bayesova věta** vyjadřuje podmíněnou pravděpodobnost jevu $A$ za podmínky $B$ pomocí opačné podmíněnosti:
$$\mathrm P(A\mid B)=\frac{\mathrm P(B\mid A)\,\mathrm P(A)}{\mathrm P(B)}.$$
Pro úplný systém disjunktních hypotéz $A_1,\dots,A_n$ (s $\sum_i\mathrm P(A_i)=1$) se jmenovatel rozepíše **větou o úplné pravděpodobnosti** $\mathrm P(B)=\sum_i\mathrm P(B\mid A_i)\mathrm P(A_i)$:
$$\mathrm P(A_k\mid B)=\frac{\mathrm P(B\mid A_k)\,\mathrm P(A_k)}{\sum_i\mathrm P(B\mid A_i)\,\mathrm P(A_i)}.$$
$\mathrm P(A_k)$ je **apriorní** pravděpodobnost (před pozorováním), $\mathrm P(A_k\mid B)$ je **aposteriorní** (po pozorování $B$).

## Použití v klasifikaci (ML2)

V generativní klasifikaci se pomocí Bayesovy věty počítá aposteriorní pravděpodobnost třídy:
$$\mathrm P(Y=y\mid X=x)\propto \mathrm P(X=x\mid Y=y)\,\mathrm P(Y=y).$$
Jmenovatel $\mathrm P(X=x)$ na $y$ nezávisí, takže pro **MAP odhad** (*maximum a posteriori*) $\hat Y=\arg\max_y\mathrm P(X=x\mid Y=y)\mathrm P(Y=y)$ odpadá. Tento princip stojí za [[Naivní-Bayesův-klasifikátor|naivním Bayesem]] i [[Lineární-diskriminační-analýza|LDA]]. Bayesovský přístup k odhadu parametrů zavádí apriorní rozdělení a aktualizuje je na aposteriorní (např. add-one / Laplaceovo vyhlazení).

## Související

- [[Naivní-Bayesův-klasifikátor]]
- [[Lineární-diskriminační-analýza]]
- [[Maximální-věrohodnost]]
- [[Nezávislost-náhodných-veličin]]
