---
aliases: [RSA, šifra RSA, RSA šifra, RSA šifry, kryptosystém RSA, RSA kryptosystém]
tags: [definice, kurz/KAB]
---

# RSA

## Definice

**RSA** (Rivest, Shamir, Adleman) je [[Asymetrická-šifra|asymetrický kryptosystém]] založený na **modulárním umocňování** a na obtížnosti **faktorizace** velkého čísla.

Generování klíčů:
1. Zvol velká [[Prvočíslo|prvočísla]] $p, q$, spočti $n = pq$ a $\varphi(n) = (p-1)(q-1)$ ([[Eulerova-funkce|Eulerova funkce]]).
2. Zvol veřejný exponent $e$, $1 < e < n$, s $\gcd(e, \varphi(n)) = 1$.
3. Spočti soukromý exponent $d = e^{-1} \bmod \varphi(n)$ ([[Eukleidův-algoritmus|rozšířený Eukleidův algoritmus]]).
4. **Veřejný klíč** $VK = (n, e)$, **soukromý klíč** $SK = (n, d)$.

Šifrování a dešifrování:
$$c = m^{e} \bmod n, \qquad m = c^{d} \bmod n.$$

## Korektnost

Protože $ed \equiv 1 \pmod{\varphi(n)}$, je $ed = k\varphi(n) + 1$, a z [[Eulerova-funkce|Eulerovy věty]] $m^{\varphi(n)} \equiv 1 \pmod n$:
$$c^{d} = m^{ed} = m^{k\varphi(n)+1} = (m^{\varphi(n)})^{k}\, m \equiv m \pmod n.$$

## Bezpečnost

- Ze znalosti $p, q$ (tedy $\varphi(n)$) lze snadno dopočítat $d$. Bez nich je nalezení $\varphi(n)$ stejně těžké jako **faktorizace $n$**.
- Nebylo prokázáno dešifrování RSA bez faktorizace $n$ ⇒ bezpečnost stojí na obtížnosti faktorizace.
- Prvočísla $p, q$ je nutné volit dostatečně velká a „bezpečně“ (velký prvočíselný faktor $p-1, q-1$; $p \neq q$ dostatečně).

## Urychlení

- **Malý veřejný exponent** $e$ s nízkou Hammingovou váhou (např. $2^{16}+1$).
- **RSA-CRT** — dešifrování přes Čínskou větu o zbytcích modulo $p$ a $q$ s čísly poloviční délky (4–8× rychlejší).

## Použití

Šifrování, distribuce klíčů a **[[Digitální-podpis|RSA digitální podpis]]** ($S = m^{d} \bmod n$, ověření $m = S^{e} \bmod n$).

## Související

- [[Asymetrická-šifra]]
- [[Eulerova-funkce]]
- [[Eukleidův-algoritmus]]
- [[Prvočíslo]]
- [[Digitální-podpis]]
