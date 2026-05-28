---
aliases: [Eulerova funkce, Eulerovy funkce, Eulerově funkci, Eulerovu funkci, Eulerovou funkcí, totient, totientů, ϕ, φ]
tags: [definice, kurz/DML]
---

# Eulerova funkce

## Definice

**Eulerova funkce** $\varphi: \mathbb{N} \to \mathbb{N}$ přiřadí každému $n \in \mathbb{N}$ počet přirozených čísel menších nebo rovných $n$, která jsou s $n$ **nesoudělná**:
$$\varphi(n) := \big|\{k \in \mathbb{N} : k \leq n \land \gcd(k, n) = 1\}\big|.$$

## První hodnoty

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\varphi(n)$ | 1 | 1 | 2 | 2 | 4 | 2 | 6 | 4 | 6 | 4 | 10 | 4 |

## Klíčové vlastnosti

**Na prvočíslech:** $p \in \mathbb{N}$ je prvočíslo $\iff \varphi(p) = p - 1$.

**Na mocninách prvočísel:** Pro prvočíslo $p$ a $\alpha \in \mathbb{N}$:
$$\varphi(p^\alpha) = p^\alpha - p^{\alpha-1} = p^\alpha\left(1 - \frac{1}{p}\right).$$

**Multiplikativita:** Pokud $\gcd(m, n) = 1$, pak
$$\varphi(mn) = \varphi(m) \cdot \varphi(n).$$

## Výpočet z faktorizace

Pro $m = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k}$:
$$\varphi(m) = m \left(1 - \frac{1}{p_1}\right)\left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right).$$

**Příklad:** $\varphi(100) = \varphi(2^2 \cdot 5^2) = 100 \cdot \tfrac{1}{2} \cdot \tfrac{4}{5} = 40$.

**Pozn. (RSA):** Není znám efektivní algoritmus pro výpočet $\varphi(n)$ bez prvočíselné faktorizace $n$ — na této obtížnosti stojí bezpečnost šifry RSA.

## Eulerova věta

**Věta:** Nechť $m \in \mathbb{N}$, $m \geq 2$, a $a \in \mathbb{N}$ je nesoudělné s $m$. Pak
$$a^{\varphi(m)} \equiv 1 \pmod m.$$

Tato věta zobecňuje [[Malou Fermatovu větu]] — pro prvočíselné $m$ je $\varphi(m) = m - 1$.

**Důsledek (inverze):** Pokud $\gcd(a, m) = 1$, pak $a^{\varphi(m) - 1}$ je multiplikativní inverzí $a$ modulo $m$ (protože $a \cdot a^{\varphi(m) - 1} = a^{\varphi(m)} \equiv 1$).

## Související

- [[Prvočíslo]]
- [[Kongruence]]
- [[Dělitelnost]]
