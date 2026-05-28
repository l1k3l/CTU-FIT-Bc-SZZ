---
aliases: [Eukleidův algoritmus, Eukleidova algoritmu, Eukleidovým algoritmem, EA, REA, EEA, rozšířený Eukleidův algoritmus, gcd, gcd(a,b), největší společný dělitel, největšího společného dělitele, Bézoutova rovnost, Bézoutovy koeficienty, Bézoutovými koeficienty]
tags: [definice, algoritmus, kurz/DML]
---

# Eukleidův algoritmus

## Největší společný dělitel

**Definice:** Pro $a, b \in \mathbb{Z}$ je $n \in \mathbb{N}_0$ **největším společným dělitelem** $a, b$ (značíme $n = \gcd(a, b)$), jestliže
- $n \mid a \land n \mid b$,
- $(\forall d \in \mathbb{N}_0)\big((d \mid a \land d \mid b) \Rightarrow d \mid n\big)$.

Čísla $a, b$ jsou **nesoudělná**, právě když $\gcd(a, b) = 1$.

## Lemma (klíč pro EA)

Pro libovolné $a, b, c \in \mathbb{Z}$:
$$\gcd(a + cb, b) = \gcd(a, b).$$

## Eukleidův algoritmus (EA)

Pro $a \geq b > 0$ definujme rekurentně
$$r_1 = a,\ r_2 = b,\quad r_n = r_{n-2} \bmod r_{n-1} \text{ pro } n \geq 3.$$

Posloupnost $(r_n)$ je striktně klesající a nezáporná, takže existuje nejmenší $k$ s $r_{k+1} = 0$. Pak
$$\gcd(a, b) = r_k$$
(poslední nenulový zbytek).

**Korektnost** plyne z opakované aplikace lemmatu: $\gcd(a, b) = \gcd(r_2, r_3) = \cdots = \gcd(r_k, 0) = r_k$.

## Bézoutova rovnost

**Věta:** Pro každé $a, b \in \mathbb{Z}$ existují $m, n \in \mathbb{Z}$ taková, že
$$\gcd(a, b) = m \cdot a + n \cdot b.$$

Dvojici $(m, n)$ nazýváme **Bézoutovy koeficienty** (nejsou jednoznačné). Navíc $\gcd(a, b)$ je **nejmenší kladné** celé číslo vyjádřitelné jako $ma + nb$.

## Rozšířený Eukleidův algoritmus (REA / EEA)

REA vedle $r_n$ udržuje koeficienty $\alpha_n, \beta_n$ splňující $r_n = \alpha_n a + \beta_n b$:

$$\alpha_1 = 1,\ \beta_1 = 0,\quad \alpha_2 = 0,\ \beta_2 = 1,$$
$$q_{n-1} = \lfloor r_{n-2} / r_{n-1} \rfloor,$$
$$\alpha_n = \alpha_{n-2} - q_{n-1} \alpha_{n-1},\quad \beta_n = \beta_{n-2} - q_{n-1} \beta_{n-1}.$$

Po skončení ($r_k = \gcd(a, b)$, $r_{k+1} = 0$) máme
$$\gcd(a, b) = \alpha_k \cdot a + \beta_k \cdot b.$$

REA tedy řeší současně:
- výpočet $\gcd(a, b)$,
- nalezení Bézoutových koeficientů,
- řešení lineární diofantické rovnice $ax + by = c$,
- výpočet multiplikativní inverze v $\mathbb{Z}_m$.

## Vztah s lcm

$$\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |a| \cdot |b|.$$

Důsledek: $\operatorname{lcm}(a, b) = \frac{|a||b|}{\gcd(a, b)}$ — počítáme rychle přes EA, bez faktorizace.

## Související

- [[Dělitelnost]]
- [[Prvočíslo]]
- [[Kongruence]]
