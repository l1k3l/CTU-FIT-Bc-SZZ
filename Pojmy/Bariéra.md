---
aliases: [bariéra, bariéry, bariéru, bariéře, bariér, bariérám, barrier]
tags: [definice, kurz/OSY]
---

# Bariéra

## Definice
**Bariéra** je blokující synchronizační nástroj umožňující jednoduše
synchronizovat **iterační výpočty** (např. paralelní výpočet mocniny matice).
Obsahuje:
- **čítač** definující sílu bariéry (počet vláken nutných k jejímu „prolomení"),
- frontu vláken, která jsou na bariéře blokovaná.

Atomické operace:
- `barrier_init(bar, value)` — nastaví čítač na `value` a vyprázdní frontu,
- `barrier_wait(bar)` — je-li čítač > 1, sníží ho o 1 a **zablokuje** volající
  vlákno; jinak (poslední příchozí) **probudí všechna** blokovaná vlákna a čítač
  se znovu nastaví na původní hodnotu.

Vlákna tak na bariéře čekají, dokud danou fázi/iteraci nedokončí všechna, a teprve
pak společně pokračují další iterací.

## Související
- [[Semafor]]
- [[Podmíněná-proměnná]]
- [[Kritická-sekce]]
