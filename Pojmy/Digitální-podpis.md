---
aliases: [digitální podpis, digitálního podpisu, digitálním podpisem, digitální podpisy, digitálních podpisů, elektronický podpis]
tags: [definice, kurz/KAB]
---

# Digitální podpis

## Definice

**Digitální podpis** je obvykle asymetrické kryptografické schéma, ve kterém:

- **podepisující** vytvoří podpis svým **soukromým klíčem** $SK$,
- **kdokoli** ho ověří **veřejným klíčem** $VK$ podepisujícího.

Podpis je skupina bitů závislá na **celém** podepisovaném dokumentu a na tajné informaci (soukromém klíči). V praxi se nepodepisuje zpráva přímo, ale její **[[Hašovací-funkce|haš]]** (kratší, a [[Hašovací-funkce|bezkoliznost]] brání podvržení jiné zprávy se stejnou haší).

## Požadované vlastnosti

- **Autentizace / nezfalšovatelnost** — podpis nelze napodobit nikým jiným než podepisujícím; **ověřitelnost** příjemcem.
- **Integrita** — podepsanou zprávu nelze změnit, aniž by se podpis zneplatnil.
- **Nepopiratelnost** — podepisující nemůže později popřít, že dokument podepsal (proto symetrické techniky jako [[HMAC]] či CBC-MAC podpisem nejsou — sdílený klíč nezaručuje nepopiratelnost).

## RSA digitální podpis

Podpis zprávy $m$ (resp. její haše): $S = m^{d} \bmod n$ soukromým klíčem $(d, n)$.
Ověření veřejným klíčem $(e, n)$: spočti $m' = S^{e} \bmod n$ a porovnej s haší zprávy. Funguje, protože $(m^d)^e = m^{de} \equiv m \pmod n$ (viz [[RSA]]).

## Kategorie

- **Přímé** (direct) — mezi dvěma subjekty; problém: při popření nemá kdo svědčit.
- **Arbitrované** (arbitrated) — důvěryhodná třetí strana ověřuje podpisy.

Další schémata: **DSA**, **ElGamal**, **ECDSA** (založené na [[Problém-diskrétního-logaritmu|DLP]]).

## Související

- [[RSA]]
- [[Hašovací-funkce]]
- [[Asymetrická-šifra]]
- [[Certifikát]]
- [[Problém-diskrétního-logaritmu]]
