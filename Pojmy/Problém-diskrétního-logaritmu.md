---
aliases: [problém diskrétního logaritmu, problému diskrétního logaritmu, diskrétní logaritmus, diskrétního logaritmu, diskrétním logaritmem, PDL, DLP]
tags: [definice, kurz/KAB]
---

# Problém diskrétního logaritmu

## Definice

Nechť $G$ je grupa, $b \in G$ a $y \in G$ je mocninou $b$. **Diskrétní logaritmus** prvku $y$ o základu $b$ je číslo $k$ takové, že $b^{k} = y$; značíme $\log_b y$.

**Problém diskrétního logaritmu (PDL/DLP):** k zadaným $b, y$ nalézt $k = \log_b y$.

- Je-li $G$ cyklická a $b$ její **generátor**, $\log_b y$ existuje pro všechna $y \in G$.
- V grupě $\mathbb{Z}_p^{*}$ (násobení modulo prvočíslo $p$) **není znám** algoritmus řešící PDL v polynomiálním čase (v nejhorším případě). Naproti tomu v aditivní grupě $\mathbb{Z}_p$ se PDL řeší snadno (Eukleidovým algoritmem).

## Vlastnosti

Pro cyklickou grupu $G$ řádu $n$ s generátorem $g$ platí (analogie „běžného“ logaritmu):
$$\log_g 1 = 0,\quad \log_g g^{k} = k,\quad \log_g(a^{k}) = k\log_g a,\quad \log_g(ab) = \log_g a + \log_g b.$$

## Útoky

Hrubá síla je $O(n)$. Efektivnější (stále exponenciální) algoritmy: **Baby-step giant-step**, **Pollardův $\rho$**, **Pohlig–Hellman**, **index kalkulus**, **funkční síto** (nejrychlejší známý). Náročnost PDL v $\mathbb{Z}_p^{*}$ je srovnatelná s faktorizací čísla podobné velikosti.

## Využití

Bezpečnost asymetrických systémů: **[[Diffie-Hellman|Diffie–Hellmanův]]** protokol, **ElGamal**, **DSA**, **ECDSA**. I když útočník zná $g^{a}$ a $g^{b}$, nedokáže bez $a$ nebo $b$ spočítat $g^{ab}$ (Diffie–Hellmanův problém, DHP — není těžší než DLP).

## Související

- [[Diffie-Hellman]]
- [[Asymetrická-šifra]]
