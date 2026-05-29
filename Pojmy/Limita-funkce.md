---
aliases: [limita funkce, limity funkce, limitu funkce, limita, limity, limitě, limitou, jednostranná limita, limita zprava, limita zleva, limit of a function]
tags: [definice, kurz/MA1]
---

# Limita funkce

## Definice

Mějme funkci $f : A \to \mathbb{R}$, **hromadný bod** $a \in \mathbb{R}^*$ množiny $A$ a bod $b \in \mathbb{R}^*$. Funkce $f$ má v bodě $a$ **limitu** $b$, právě když pro každé okolí $U_b$ existuje okolí $U_a$ tak, že
$$\forall x \in (A \cap U_a) \setminus \{a\}:\ f(x) \in U_b.$$
Značíme $\lim_{x\to a} f(x) = b$. Tento pojem zahrnuje i limitu posloupnosti ($\mathbb{N}$ má jediný hromadný bod $+\infty$).

## ε-δ tvar (pro $a, b \in \mathbb{R}$)

$$\lim_{x\to a} f(x) = b \iff \forall \varepsilon > 0\ \exists \delta > 0\ \forall x \in D_f\ \big(0 < |x-a| < \delta \Rightarrow |f(x)-b| < \varepsilon\big).$$

**Důležité:** limita v $a$ závisí jen na chování $f$ na okolí $a$ **mimo** bod $a$. Může být různá od $f(a)$, ba $f$ v $a$ nemusí být ani definovaná.

## Jednostranná limita

$\lim_{x\to a^+} f = \lim_{x\to a}(f|_{A\cap(a,\infty)})$ (zprava), analogicky zleva. Platí:
$$\lim_{x\to a} f = b \iff \lim_{x\to a^+} f = \lim_{x\to a^-} f = b.$$
Různé (nebo neexistující) jednostranné limity ⇒ oboustranná limita neexistuje.

## Vlastnosti

- **Jednoznačnost** limity.
- **Heineho věta:** $\lim_{x\to a} f(x) = b$ ⟺ pro **každou** posloupnost $x_n \to a$ s $x_n \in D_f \setminus\{a\}$ platí $f(x_n) \to b$. (Nástroj k vyvracení limit.)

## Související

- [[Spojitost]]
- [[Limita-posloupnosti]]
- [[Asymptotická-notace]]
