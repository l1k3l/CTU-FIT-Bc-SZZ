---
tags: [otázka, kurz/KAB, otázka/10, todo]
---

# 10 — Symetrické šifry: blokové, proudové, operační módy (zkrácená verze)

## 1. Symetrické šifry — rozdělení

$K_E$, $K_D$ stejné / snadno převoditelné; $c = E_K(m)$, $m = D_K(c)$.

| | **Bloková** | **Proudová** |
|---|---|---|
| jednotka | blok $t$ (dnes 128 b) | znak / bit |
| transformace | všechny bloky toutéž $E_K$ | každý znak jinou $E_{h_i}$ |
| difúze | dobrá (celý blok) | malá (1 znak) |
| chyba | celý blok | 1 znak |

Parametry: délka klíče, délka bloku, perioda hesla, IV, počet rund.

## 2. Proudové šifry

**Princip:** generátor hesla $h_i$ z klíče; $c_i = m_i \oplus h_i$ (šifrování = dešifrování). **IV** (otevřeně) → různé heslo při stejném klíči. **Synchronní** (heslo nezávisí na OT/ŠT, nutná synchronizace) × **asynchronní/samosynchronizující** ($h_i = f(k, c_{i-n..i-1})$).

- **Vernam (OTP):** náhodné heslo délky OT, jednorázové ⇒ **dokonalé utajení**.
- **RC4** (1987, SSL) — permutace $S$ na $\{0..255\}$ (KSA+PRGA), bez IV — **prolomena**.
- **Salsa20/ChaCha** (Bernstein) — **ARX** (sčítání, XOR, rotace) na $4\times4$ matici 32b slov, 20 rund, odolnost vůči časovým útokům; ChaCha20-Poly1305 (QUIC, OpenSSH).
- **A5/1** (GSM) — 3 LFSR (19/22/23 b) + **majority clocking** (nelinearita); $k_i = R1[18]\oplus R2[21]\oplus R3[22]$ — prolomena.

**Slabina – dvojí použití hesla:** $c \oplus c' = m \oplus m'$ → luštění. Nikdy neopakovat (klíč, IV).

## 3. Blokové šifry

**Princip:** bloky toutéž $E_K$; difúze (lavinový efekt) + konfúze střídáním S-boxů a permutací v rundách.
**Feistel:** $(L_{i+1}, R_{i+1}) = (R_i,\ L_i \oplus f(R_i, k_{i+1}))$ — dešifrování stejné, obrácené pořadí klíčů; $f$ nemusí být prostá.

| Šifra | Blok | Klíč | Rundy | Typ |
|---|---|---|---|---|
| DES | 64 | **56** | 16 | Feistel |
| 3DES | 64 | 112/168 | 48 | 3× DES (EDE) |
| AES | 128 | 128/192/256 | 10/12/14 | SPN |

- **DES:** Feistel, S-boxy = nelinearita; **slabina = krátký klíč 56 b** (prolomen hrubou silou).
- **3DES-EDE:** $E_{K_3}(D_{K_2}(E_{K_1}(m)))$, zpětně kompatibilní.
- **AES (Rijndael):** SubBytes, ShiftRows, MixColumns, AddRoundKey nad $GF(2^8)$; **není Feistel**, bez slabých klíčů.

## 4. Operační módy

| Mód | Předpis | Vlastnost / slabina |
|---|---|---|
| **ECB** | $\text{ŠT}_i = E_K(\text{OT}_i)$ | stejný OT → stejný ŠT; manipulace bloků |
| **CBC** | $\text{ŠT}_i = E_K(\text{OT}_i \oplus \text{ŠT}_{i-1})$, $\text{ŠT}_0=IV$ | difúze, náhodný IV; **nejpoužívanější**; sériový |
| **CFB** | $\text{ŠT}_i = \text{OT}_i \oplus E_K(\text{ŠT}_{i-1})$ | blok→proud, jen $E_K$, samosynchronní |
| **OFB** | $H{=}E_K(IV)$, $\text{ŠT}_i = \text{OT}_i \oplus H$, $H{\leftarrow}E_K(H)$ | synchronní proud; omezená perioda hesla |
| **CTR** | $\text{ŠT}_i = \text{OT}_i \oplus E_K(IV{+}i{-}1)$ | paralelní, náhodný přístup; nesmí opakovat čítač |
| **CBC-MAC** | CBC s $IV=0$, výstup = poslední blok | **integrita** + autentizace; ne nepopiratelnost |

Šifrování **nezajišťuje integritu** (řeší CBC-MAC). OFB/CTR mají slabinu dvojího použití hesla. **Solení IV:** šifruje se $IV'$ vypočtené z $IV$ a klíče.

---

## Co odpovědět rychle
- **Symetrická:** sdílený tajný klíč; blokové (bloky toutéž $E_K$) × proudové ($c_i = m_i \oplus h_i$).
- **Feistel** vs. **SPN (AES)**; DES 56b klíč = krátký → prolomen; 3DES EDE; AES 128b blok, bez slabých klíčů.
- **Proudové:** Vernam = dokonalé utajení; RC4, A5/1 (LFSR+majority), Salsa20/ChaCha (ARX). Slabina: dvojí použití hesla.
- **Módy:** ECB (slabý), **CBC** (difúze, IV, nejpoužívanější), CFB/OFB/CTR (blok→proud), CBC-MAC (integrita).
- **Šifrování ≠ integrita.** OFB/CTR: nesmí se opakovat heslo/čítač.
