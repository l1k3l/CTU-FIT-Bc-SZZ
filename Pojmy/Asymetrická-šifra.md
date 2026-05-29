---
aliases: [asymetrická šifra, asymetrické šifry, asymetrickou šifrou, asymetrických šifer, asymetrická kryptografie, asymetrické šifrování, asymetrický kryptosystém, asymetrické kryptosystémy, kryptografie veřejného klíče, šifra veřejného klíče, kryptosystém veřejného klíče, systém veřejného klíče]
tags: [definice, kurz/KAB]
---

# Asymetrická šifra

## Definice

**Asymetrická šifra** (kryptografie veřejného klíče) používá **dvojici klíčů**:

- **veřejný klíč** $VK$ — zveřejní se, slouží k šifrování (resp. k ověření podpisu),
- **soukromý klíč** $SK$ — drží jen vlastník, slouží k dešifrování (resp. k podpisu).

Klíčová podmínka: **výpočet $SK$ ze znalosti $VK$ je výpočetně neschůdný.** Kdokoli může Alici poslat zprávu zašifrovanou $VK_A$, ale dešifrovat ji umí jen Alice se svým $SK_A$.

## Princip

Asymetrická šifra je [[Jednosměrná-funkce|jednosměrná funkce s padacími dvířky]]: snadno se počítá jedním směrem, zpětný chod je bez znalosti soukromého klíče (padacích dvířek) neschůdný. Bezpečnost stojí na výpočetně těžkých problémech:

| Problém | Kryptosystémy |
|---|---|
| Faktorizace velkého čísla $n = pq$ | [[RSA]] |
| [[Problém-diskrétního-logaritmu\|Diskrétní logaritmus]] (DLP) | [[Diffie-Hellman]], ElGamal, DSA, ECDSA |

## Použití

- **Šifrování** zpráv pro daného adresáta (jeho $VK$).
- **Distribuce tajných (symetrických) klíčů** — řeší problém sdílení klíče u [[Symetrická-šifra|symetrických šifer]].
- **[[Digitální-podpis]]** — podpis $SK$, ověření $VK$.

V praxi se kombinuje s [[Symetrická-šifra|symetrickou šifrou]] (hybridní schéma): asymetricky se přenese symetrický klíč relace, jím se pak šifrují data (asymetrické operace jsou pomalé).

## Související

- [[Symetrická-šifra]]
- [[RSA]]
- [[Diffie-Hellman]]
- [[Problém-diskrétního-logaritmu]]
- [[Digitální-podpis]]
- [[Certifikát]]
