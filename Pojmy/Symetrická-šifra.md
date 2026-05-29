---
aliases: [symetrická šifra, symetrické šifry, symetrickou šifrou, symetrických šifer, symetrické šifře, symetrická kryptografie, symetrické šifrování, symetrický kryptosystém, symetrické kryptosystémy]
tags: [definice, kurz/KAB]
---

# Symetrická šifra

## Definice

**Symetrická šifra** je šifrovací systém $(M, C, K, E, D)$, ve kterém jsou šifrovací klíč $K_E$ a dešifrovací klíč $K_D$ **stejné nebo se z jednoho snadno (výpočetně levně) odvodí druhý**. Odesílatel i příjemce proto musí sdílet tentýž tajný klíč.

Zašifrování bloku/znaku $m$: $c = E_K(m)$, dešifrování $m = D_K(c)$, kde $D_K = E_K^{-1}$.

## Rozdělení

Podle způsobu zpracování OT klíčem:

- **[[Bloková-šifra|Blokové šifry]]** — zpracovávají bloky délky $t$ znaků, všechny bloky **toutéž** transformací $E_K$ (DES, 3DES, AES).
- **[[Proudová-šifra|Proudové šifry]]** — z klíče generují proud hesla $h_1, h_2, \dots$ a každý znak šifrují jinou transformací $E_{h_i}$ (RC4, Salsa20/ChaCha, A5/1).

## Vlastnosti

- **Rychlé** — vhodné pro šifrování velkých objemů dat.
- **Slabina:** distribuce / sdílení tajného klíče. Při $n$ účastnících je potřeba $\binom{n}{2}$ klíčů. Řeší se ustavením klíče přes [[Diffie-Hellman]] nebo distribucí pomocí [[Asymetrická-šifra|asymetrické kryptografie]].
- **Nezajišťuje nepopiratelnost** (oba sdílejí klíč) — proto se na podpisy používá asymetrická kryptografie.

## Související

- [[Asymetrická-šifra]]
- [[Bloková-šifra]]
- [[Proudová-šifra]]
- [[Diffie-Hellman]]
