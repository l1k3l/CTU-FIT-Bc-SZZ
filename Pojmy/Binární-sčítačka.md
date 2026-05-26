---
aliases: [binární sčítačka, binární sčítačky, binární sčítačce, binární sčítačku]
tags: [definice, kurz/AG1]
---

# Binární sčítačka

## Definice
**Binární sčítačka** je sériový obvod, který uchovává bitovou reprezentaci čísla v $k$-bitových buňkách (0/1). Operace:
- `Inc(n)` — zvýší číslo $n$ o 1.
- `Add(n, m)` — přičte $m$ k $n$.

Implementace **ripple-carry**: přenos se postupně šíří zprava doleva.

## Amortizovaná analýza `Inc`
**Věta:** Celková složitost $n$ volání `Inc` (počítaná jako počet bitových inverzí) na vynulované sčítačce je $O(n)$, tedy [[Amortizovaná-složitost|amortizovaná složitost]] `Inc` je $O^*(1)$.

*Důkaz (bankéřova metoda):* Každému volání `Inc` přiřadíme **2 mince**. Operace `Inc` zaplatí 1 mincí za inverzi prvního nulového bitu (0 → 1). Druhou minci uloží na nově vzniklý jedničkový bit. Invariant: **na každém jedničkovém bitu je naspořena jedna mince**. Inverze jedniček zpět na nuly se hradí z nashromážděných mincí. Celkový počet inverzí v $n$ voláních ≤ $2n$. $\square$

## Souvislost s [[Binomiální-halda|binomiální haldou]]
Operace `BHInsert` odpovídá `Inc` v binární sčítačce: binomiální stromy $B_i$ v BH velikosti $n$ přesně odpovídají jedničkovým bitům dvojkového zápisu $n$. Slévání dvou stromů $B_i \to B_{i+1}$ pomocí `BHMergeTree` odpovídá bitovému přenosu. Proto je amortizovaná složitost `BHInsert` rovněž $\Theta^*(1)$.

## Související
- [[Amortizovaná-složitost]]
- [[Nafukovací-pole]]
- [[Binomiální-halda]]
