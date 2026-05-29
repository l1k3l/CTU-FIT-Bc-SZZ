---
aliases: [proudová šifra, proudové šifry, proudovou šifrou, proudových šifer, proudové šifře, proudové šifrování, keystream, heslo, key-stream]
tags: [definice, kurz/KAB]
---

# Proudová šifra

## Definice

**Proudová šifra** se skládá z generátoru $G$, zobrazení $E$ a $D$. Pro klíč $k \in K$ generátor $G$ vytvoří **proud hesla** (keystream) $h_1, h_2, \dots$ a každý znak OT je šifrován **jinou** transformací:
$$c_1 = E_{h_1}(m_1),\ c_2 = E_{h_2}(m_2),\ \dots$$

Moderní proudové šifry pracují nad abecedou $\{0,1\}$ a substituce je posun (XOR):
$$c_i = m_i \oplus h_i, \qquad m_i = c_i \oplus h_i.$$
Zašifrování a dešifrování jsou tedy **stejná** operace.

Lze ji chápat jako [[Bloková-šifra|blokovou šifru]] s blokem délky 1, kde je ale každý „blok“ zpracován jinou substitucí.

## Synchronní × asynchronní

- **Synchronní** — proud hesla nezávisí na OT ani ŠT; odesílatel a příjemce musí být přesně synchronizováni (ztráta znaku ŠT naruší celý zbytek).
- **Asynchronní (samosynchronizující)** — heslo závisí na $n$ předchozích znacích ŠT: $h_i = f(k, c_{i-n}, \dots, c_{i-1})$; po $n+1$ správných znacích se obnoví synchronizace.

## Vlastnosti

- **Malá propagace chyby** — chyba v jednom znaku ŠT se projeví jen v jednom znaku OT (u blokové šifry ovlivní celý blok).
- **Slabina — dvojí použití hesla:** dva ŠT $c, c'$ pod stejným heslem dají $c_i \oplus c_i' = m_i \oplus m_i'$ → eliminace hesla, luštění jako knižní šifra. Proto se používá náhodný **inicializační vektor (IV)** přenášený otevřeně.

## Příklady

- **Vernamova šifra (OTP)** — náhodné heslo stejně dlouhé jako OT, použité jen jednou ⇒ **dokonalé utajení**.
- **RC4** (prolomená), **Salsa20/ChaCha20**, **A5/1** (GSM).

## Související

- [[Symetrická-šifra]]
- [[Bloková-šifra]]
