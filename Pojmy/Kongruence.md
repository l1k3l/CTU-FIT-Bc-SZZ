---
aliases: [kongruence, kongruenci, kongruencí, kongruencím, kongruencemi, kongruencích, kongruentní, kongruentního, kongruentními, modulo, modulární aritmetika, modulární aritmetiky, modulární aritmetiku]
tags: [definice, kurz/DML]
---

# Kongruence

## Definice

Nechť $a, b \in \mathbb{Z}$, $m \in \mathbb{N}$, $m \geq 2$. Říkáme, že $a$ je **kongruentní s $b$ modulo $m$**, značíme
$$a \equiv b \pmod m,$$
právě když $m \mid (a - b)$. Číslo $m$ se nazývá **modulus** (modul). Samotné $\equiv \pmod m$ je **relace kongruence modulo $m$**.

## Ekvivalentní vyjádření

Pro $a, b \in \mathbb{Z}$ a $m \geq 2$ jsou ekvivalentní:
1. $a \equiv b \pmod m$.
2. $a - b \equiv 0 \pmod m$.
3. $\exists k \in \mathbb{Z}: a = b + km$.
4. $a \bmod m = b \bmod m$ (mají stejné zbytky po dělení $m$).

## Vlastnosti

Relace $\equiv \pmod m$ je **reflexivní, symetrická, tranzitivní** — tedy je to relace ekvivalence.

**Zachovává $+, -, \cdot$ a mocninu:** Nechť $a \equiv b \pmod m$ a $c \equiv d \pmod m$. Pak
- $a \pm c \equiv b \pm d \pmod m$,
- $a c \equiv b d \pmod m$,
- $a^k \equiv b^k \pmod m$ pro $k \in \mathbb{N}$.

**Krácení v modulu:** Pro $d = \gcd(m, c)$:
$$ac \equiv bc \pmod m \iff a \equiv b \pmod{m/d}.$$
Speciálně lze krátit beze změny modula, právě když $\gcd(m, c) = 1$.

## $\mathbb{Z}_m$ a inverze

**Definice:** $\mathbb{Z}_m = \{0, 1, \dots, m-1\}$ s operacemi
$$a +_m b := (a + b) \bmod m, \quad a \cdot_m b := (a \cdot b) \bmod m.$$

**Multiplikativní inverze** $a^{-1}$ k $a \in \mathbb{Z}_m$ je prvek splňující $a \cdot_m a^{-1} = 1$.

**Věta:** Multiplikativní inverze k $a$ v $\mathbb{Z}_m$ existuje **právě tehdy, když $\gcd(a, m) = 1$**, a je jediná. Najde se REA aplikovaným na LDR $ax + my = 1$.

**Důsledek:** Pro prvočíselný modul $p$ má každý nenulový prvek $\mathbb{Z}_p$ inverzi ⇒ $(\mathbb{Z}_p, +_p, \cdot_p)$ je **konečné těleso**.

## Související

- [[Dělitelnost]]
- [[Eukleidův-algoritmus]]
- [[Eulerova-funkce]]
