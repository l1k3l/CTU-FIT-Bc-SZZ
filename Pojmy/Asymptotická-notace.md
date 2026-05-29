---
aliases: [asymptotická notace, asymptotické meze, asymptotická mez, asymptotická ekvivalence, Landauova notace, velké O, malé o, omega, theta, horní mez, dolní mez, těsná mez, big O, asymptotic notation]
tags: [definice, kurz/MA1]
---

# Asymptotická notace

Nástroje pro porovnávání chování dvou funkcí (či [[Posloupnost|posloupností]]), když se argument blíží k bodu $a$ (u posloupností vždy $n\to+\infty$). Předpokládá se, že $a$ je hromadným bodem a definiční obory se na okolí $a$ shodují.

## Definice (mez až na konstantu)

Pro $f, g$ a bod $a$:

| symbol | název | podmínka (na okolí $a$, $x \neq a$) | analogie |
|---|---|---|---|
| $f = O(g)$ | horní mez | $\exists c>0:\ \lvert f\rvert \le c\,\lvert g\rvert$ | $\le$ |
| $f = o(g)$ | striktní horní mez | $\forall c>0\ \exists U_a:\ \lvert f\rvert < c\,\lvert g\rvert$ | $<$ |
| $f = \Omega(g)$ | dolní mez | $\exists c>0:\ \lvert f\rvert \ge c\,\lvert g\rvert$ | $\ge$ |
| $f = \omega(g)$ | striktní dolní mez | $\forall c>0\ \exists U_a:\ \lvert f\rvert > c\,\lvert g\rvert$ | $>$ |
| $f = \Theta(g)$ | těsná mez | $\exists c_1,c_2>0:\ c_1\lvert g\rvert \le \lvert f\rvert \le c_2\lvert g\rvert$ | $=$ |

- „$=$" se čte jako příslušnost do množiny ($f \in O(g)$). Multiplikativní konstanta nemá na platnost vztahu vliv.
- $f = \Theta(g) \iff f = O(g) \land f = \Omega(g)$; $\Theta$ je relace **ekvivalence**.
- $f = \Omega(g) \iff g = O(f)$, $\ f = \omega(g) \iff g = o(f)$.

## Asymptotická ekvivalence ∼

$f \sim g$ pro $x\to a$, právě když existuje $u$ s $\lim_{x\to a} u(x) = 1$ a $f = u\cdot g$ na okolí $a$. Je to nejpřesnější vztah — **relace ekvivalence**. Platí $f\sim g \Rightarrow f = \Theta(g)$.

## Vyjádření pomocí limit

Je-li $g \neq 0$ na okolí $a$:
$$\lim \tfrac{f}{g} \in \mathbb{R} \Rightarrow f = O(g); \quad \lim \tfrac{f}{g} = 0 \iff f = o(g); \quad \lim \tfrac{f}{g} = 1 \iff f \sim g.$$
Pro posloupnosti navíc: $\lim \tfrac{a_n}{b_n} > 0 \Rightarrow \Omega$; $\ =+\infty \Rightarrow \omega$; $\ \in(0,+\infty) \Rightarrow \Theta$.

## Použití v jiných kurzech

V analýze algoritmů (BI-PA1, BI-PA2) se notace používá pro $n\to+\infty$ k popisu časové/paměťové **složitosti**; definice je shodná, jen specifikace bodu $+\infty$ se vynechává.

## Související

- [[Limita-posloupnosti]]
- [[Limita-funkce]]
- [[Amortizovaná-složitost]]
