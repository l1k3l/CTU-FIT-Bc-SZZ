---
aliases: [bloková šifra, blokové šifry, blokovou šifrou, blokových šifer, blokové šifře, blokové šifrování]
tags: [definice, kurz/KAB]
---

# Bloková šifra

## Definice

Nechť $A$ je abeceda $q$ symbolů, $t \in \mathbb{N}$ a $M = C$ množina všech řetězců délky $t$ nad $A$. **Bloková šifra** je šifrovací systém $(M, C, K, E, D)$, kde pro každý klíč $k \in K$ je $E_k$ transformace zašifrování a $D_k$ dešifrování, přičemž
$$c_i = E_k(m_i), \qquad m_i = D_k(c_i).$$

**Podstatné:** všechny bloky OT jsou šifrovány **toutéž** transformací $E_k$ a všechny bloky ŠT dešifrovány **toutéž** $D_k$ (na rozdíl od [[Proudová-šifra|proudové šifry]]).

## Základní parametry

- **Délka bloku** $N$: dnes 128 b (dříve 64 b — DES, 3DES, IDEA).
- **Délka klíče** $|k|$: DES 56 b, 3DES 112/168 b, AES 128/192/256 b.
- **Počet rund** (iterací): DES 16, AES 10/12/14.
- **Konstrukce:** Feistelova síť (DES, 3DES) × substitučně-permutační síť (AES — *není* Feistelovská).

Kvalitní bloková šifra dosahuje **difúze** (rozprostření vlivu jednoho bitu OT do mnoha bitů ŠT) i **konfúze** (složitý vztah ŠT ↔ klíč) — typicky střídáním substitucí (S-boxy) a permutací.

## Příklady

DES, TripleDES (3DES), **AES** (Rijndael), IDEA, CAST.

## Operační módy

Použití na zprávu delší než jeden blok řeší **operační módy**: ECB, CBC, CFB, OFB, CTR, CBC-MAC. Samotná šifra ani módy (kromě CBC-MAC) **nezajišťují integritu**.

## Související

- [[Symetrická-šifra]]
- [[Proudová-šifra]]
- [[Hašovací-funkce]]
