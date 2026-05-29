---
aliases: [hašovací funkce, hašovací funkci, hašovací funkcí, hašovacích funkcí, kryptografická hašovací funkce, haš, haše, hash, hašový kód, otisk, message digest]
tags: [definice, kurz/KAB]
---

# Hašovací funkce

> [!note] Nezaměňovat s hešováním u datových struktur
> Tato (kryptografická) **hašovací funkce** je jednosměrná a bezkolizní. Liší se od hešovací funkce u [[Hešovací-tabulka|hešovacích tabulek]] (datová struktura), kde stačí rovnoměrné rozdělení a kolize se naopak řeší ([[Hešování-s-řetízky]], [[Otevřená-adresace]]).

## Definice

Mějme $d \in \mathbb{N}$ a množinu $X$ všech binárních řetězců délky $0$ až $d$. Funkce $h : X \to \{0,1\}^n$ je **(kryptografická) hašovací funkce**, je-li **[[Jednosměrná-funkce|jednosměrná]] 1. typu a bezkolizní**. Každému vstupu přiřadí **haš** (otisk) pevné délky $n$ bitů.

## Bezpečnostní vlastnosti

Požaduje se, aby se $h$ chovala jako **náhodné orákulum** (na stejný vstup stejný výstup, na nový vstup náhodný výběr).

- **Jednosměrnost (odolnost proti nalezení vzoru):** z $h(M)$ nelze najít $M$.
- **Bezkoliznost 1. řádu (collision resistance):** je neschůdné najít $M \neq M'$ s $h(M) = h(M')$.
- **Bezkoliznost 2. řádu (2nd-preimage):** k danému $M$ je neschůdné najít $M' \neq M$ s $h(M') = h(M)$.

**Narozeninový paradox:** kolize 1. řádu se u $n$-bitové haše najde s ~50 % pravděpodobností už po cca $2^{n/2}$ zprávách (ne $2^{n-1}$). Proto délka haše určuje odolnost vůči kolizím.

## Konstrukce

- **Merkle–Damgård (DM):** iterativní zpracování zarovnané zprávy po blocích $M_i$ kompresní funkcí $f$:
$$H_i = f(H_{i-1}, M_i), \quad H_0 = IV.$$
Je-li $f$ bezkolizní, je bezkolizní i celá hašovací funkce. Zarovnání: bit `1`, nuly a **64-bitová délka zprávy** (Merkle–Damgårdovo zesílení).
- **Davies–Meyer** (kompresní funkce z blokové šifry): $H_i = E_{M_i}(H_{i-1}) \oplus H_{i-1}$.

## Příklady a použití

- **SHA-1** (160 b, prolomená), **SHA-2** (SHA-256/384/512), **SHA-3**.
- Použití: kontrola **integrity**, ukládání **hesel** (se solí), **[[Digitální-podpis|digitální podpis]]** (podepisuje se haš), **[[HMAC]]**, odvozování klíčů.

## Související

- [[Jednosměrná-funkce]]
- [[Digitální-podpis]]
- [[HMAC]]
- [[Hešovací-tabulka]]
