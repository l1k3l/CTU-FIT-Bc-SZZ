---
aliases: [dělitelnost, dělitelnosti, dělitelností, dělitelnostech, dělitelný, dělitelná, dělitelné, dělí, dělitel, dělitele, dělitelem, dělitelům, násobek, násobku, násobky]
tags: [definice, kurz/DML]
---

# Dělitelnost

## Definice

Buďte $a, b \in \mathbb{Z}$. Říkáme, že $a$ **dělí** $b$, značíme $a \mid b$, jestliže
$$\exists k \in \mathbb{Z}: a \cdot k = b.$$

Pak $a$ je **(celočíselný) dělitel** $b$ a $b$ je **(celočíselný) násobek** $a$. Pokud $a$ nedělí $b$, píšeme $a \nmid b$.

## Vlastnosti

Pro libovolná $a, b, c \in \mathbb{Z}$:

1. $1 \mid n$ a $n \mid 0$ pro každé $n \in \mathbb{Z}$.
2. $a \mid b \iff |a| \mid |b|$.
3. $a \mid b \land b \neq 0 \Rightarrow |a| \leq |b|$.
4. $a \mid b \land a \mid c \Rightarrow a \mid (b + c)$.
5. $a \mid b \Rightarrow a \mid nb$ pro každé $n \in \mathbb{Z}$.
6. **Lineární kombinace:** $a \mid b \land a \mid c \iff (\forall m, n \in \mathbb{Z}) a \mid (mb + nc)$.

## Dělení se zbytkem

**Věta:** Pro $a \in \mathbb{Z}$ a $d \in \mathbb{N}$ existují **jednoznačná** $q, r \in \mathbb{Z}$:
$$a = qd + r, \quad 0 \leq r < d.$$

Číslo $r = a \bmod d$ se nazývá **zbytek po dělení**.

## Související

- [[Prvočíslo]]
- [[Eukleidův-algoritmus]]
- [[Kongruence]]
