---
aliases: [sekvenční obvod, sekvenčního obvodu, sekvenčním obvodu, sekvenční obvody, sekvenčních obvodů, synchronní sekvenční obvod, SSO]
tags: [definice, kurz/SAP]
---

# Sekvenční obvod

## Definice
**Sekvenční obvod (SO)** je obvod, ve kterém hodnoty výstupů závisí nejen na okamžité kombinaci vstupů, ale i na **posloupnosti** předchozích vstupů — obvod si musí pamatovat **historii** (vnitřní stav). Paměť je realizována **zpětnou vazbou** přes [[Klopný-obvod|klopné obvody]]. Matematickým modelem SO je **[[Konečný-automat|konečný automat]] (Mealyho / Mooreův)**.

**Huffmanův model:** kombinační část (počítá výstupy a následující stav) + paměťová část (registr stavu z klopných obvodů), uzavřená zpětnou vazbou a řízená hodinami CLK.

## Synchronní vs asynchronní
- **Asynchronní SO:** stav se může měnit kdykoli (paměť = pouhé vodiče se zpětnou vazbou); obtížné časování.
- **Synchronní SO (SSO):** stav se mění jen v okamžicích daných **hodinovým signálem (CLK)**; v praxi převažuje.

## Kódování stavů
Pro $n$ stavů je třeba $m=\lceil\log_2 n\rceil$ stavových proměnných ($2^{m-1}<n\le 2^m$). Volba kódu ovlivňuje složitost kombinační části.

## Související
- [[Kombinační-obvod]]
- [[Klopný-obvod]]
- [[Konečný-automat]]
- [[Čítač]]
