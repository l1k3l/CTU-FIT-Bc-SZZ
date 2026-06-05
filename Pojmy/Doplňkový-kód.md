---
aliases: [doplňkový kód, doplňkového kódu, doplňkovém kódu, doplňkovým kódem, doplněk do dvou, dvojkový doplněk, two's complement, kód doplňkový]
tags: [definice, kurz/SAP]
---

# Doplňkový kód

## Definice
**Doplňkový kód** (doplněk do 2) zobrazuje celá čísla se znaménkem takto (M = modul řádové mřížky, $M=2^n$):
$$D(X)=\begin{cases} X & X \ge 0,\\ M + X & X < 0.\end{cases}$$
Znaménko je **organickou součástí obrazu** (ne oddělený bit jako u přímého kódu).

## Vlastnosti
- **Rozsah:** $-2^{n-1} \le X \le 2^{n-1}-1$ (asymetrický — o jedno záporné číslo více).
- **Jediná nula** (000…0) — odpadá problém dvou nul přímého kódu.
- **Negace:** $D(-X)=\overline{D(X)}+1$ (invertuj všechny bity a přičti „horkou jednič­ku").
- **Váha nejvyššího bitu je záporná:** $-2^{n-1}$.
- **Rozšíření znaménka** (sign extension): kopíruje se nejvyšší (znaménkový) bit → realizováno pouhými vodiči.

## Aritmetika
Sčítání i odčítání se provádí **jedním** obvodem: $A-B = D(A)+\overline{D(B)}+1$. **Přenos z nejvyššího řádu se ignoruje.** **Přeplnění (overflow)** $\ne$ přenos: nastane jen při shodných znaménkách operandů a opačném znaménku výsledku; detekce $over = p \oplus q$ (přenos do/z MSB) $= \overline a\,\overline b\, s + a b \overline s$.

Srovnej s **přímým kódem** (znaménko + absolutní hodnota, dvě nuly) a **aditivním kódem** ($A(X)=X+K$, posunutá nula — používán pro exponent v [[Pohyblivá-řádová-čárka|pohyblivé řádové čárce]]).

## Související
- [[Pohyblivá-řádová-čárka]]
- [[Sčítačka]]
