---
aliases: [sčítačka, sčítačky, sčítačce, sčítačku, sčítaček, poloviční sčítačka, úplná sčítačka, paralelní sčítačka, sčítačka/odčítačka, half adder, full adder]
tags: [definice, kurz/SAP]
---

# Sčítačka

## Definice
**Sčítačka** je [[Kombinační-obvod|kombinační obvod]] sčítající binární čísla po jednotlivých řádech.

- **Poloviční sčítačka (half adder)** — sečte 2 bity bez vstupního přenosu:
  $$s = a \oplus b, \qquad q = a \cdot b.$$
- **Úplná sčítačka (full adder)** — sečte 2 bity a vstupní přenos $p$:
  $$s = a \oplus b \oplus p, \qquad q = ab + p(a\oplus b) = M_3(a,b,p)\ \text{(majorita)}.$$

## Paralelní sčítačka (ripple-carry)
Kaskáda $n$ úplných sčítaček, přenos se šíří zprava doleva ($p_{i+1}=q_i$). **Zpoždění $O(n)$** — výsledek je správný až po průchodu přenosu všemi řády.

**Zrychlení — predikce přenosu (carry-lookahead):** ze vstupů se předem počítají signály *generate* $G_i=a_ib_i$ a *propagate* $P_i=a_i\oplus b_i$; přenosy $q_i=G_i+P_i q_{i-1}$ lze rozepsat a spočítat **dvouúrovňově** (konstantní zpoždění) za cenu více hradel.

## Sčítačka/odčítačka
Jediný obvod sčítá i odečítá v [[Doplňkový-kód|doplňkovém kódu]]: řídicí signál **Odčítej** vede do XOR hradel na operandu $B$ (negace = jedničkový doplněk) a současně jako vstupní přenos do nejnižšího řádu („horká jednička" → +1). Přeplnění (overflow) $= q_n \oplus q_{n-1}$.

## Související
- [[Doplňkový-kód]]
- [[Kombinační-obvod]]
- [[Binární-sčítačka]]
