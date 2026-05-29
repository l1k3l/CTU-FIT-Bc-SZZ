---
aliases: [HMAC, klíčovaný haš, klíčovaný hašovací kód, MAC, autentizační kód zprávy]
tags: [definice, kurz/KAB]
---

# HMAC

## Definice

**HMAC** (Keyed-Hash Message Authentication Code) je autentizační kód zprávy, který hašuje nejen zprávu $M$, ale spolu s ní i **tajný klíč** $K$. Na rozdíl od MAC založeného na blokové šifře používá **[[Hašovací-funkce|hašovací funkci]]** $H$ (např. HMAC-SHA-256). Definováno ve FIPS PUB 198.

Pro blok kompresní funkce velikosti $b$ bitů, klíč $K$ doplněný nulami na $K^{+}$ a konstanty $ipad = \texttt{0x36}^{\,b/8}$, $opad = \texttt{0x5C}^{\,b/8}$:
$$\mathrm{HMAC}_K(M) = H\big((K^{+} \oplus opad)\,\|\,H((K^{+} \oplus ipad)\,\|\,M)\big),$$
kde $\|$ je zřetězení.

## Vlastnosti a použití

- **Nepadělatelný integritní kód** — bez znalosti $K$ nelze ke změněné zprávě dopočítat platný HMAC (samotná haš to neumí — útočník by ji přepočítal).
- **Autentizace původu dat** — správný HMAC dokládá, že odesílatel znal $K$.
- **Průkaz znalosti (challenge–response):** $response = \mathrm{HMAC}_K(challenge)$ dokazuje znalost $K$, aniž by se $K$ vyzradil.
- Jako symetrická technika **nezaručuje nepopiratelnost** (na rozdíl od [[Digitální-podpis|digitálního podpisu]]).

## Související

- [[Hašovací-funkce]]
- [[Digitální-podpis]]
