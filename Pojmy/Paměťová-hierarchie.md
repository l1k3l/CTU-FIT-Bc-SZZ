---
aliases: [paměťová hierarchie, paměťové hierarchie, paměťovou hierarchií, hierarchie pamětí, princip lokality, lokalita odkazů]
tags: [definice, kurz/SAP]
---

# Paměťová hierarchie

## Definice
**Paměťová hierarchie** je víceúrovňové uspořádání pamětí, které vyvažuje protichůdné požadavky na **rychlost, kapacitu a cenu**. Vyšší (bližší procesoru) vrstvy jsou rychlé, malé a drahé; nižší vrstvy pomalé, velké a levné.

| vrstva | realizace | doba přístupu | kapacita |
|---|---|---|---|
| registry | klopné obvody | jednotky ns | desítky–stovky B |
| **[[Cache]]** (L1/L2/L3) | statická RAM (SRAM) | ~1–10 ns | kB–MB |
| hlavní paměť | dynamická RAM (DRAM) | ~50 ns | GB |
| vnější paměť | magnetický disk / SSD | ms / µs | GB–TB |
| záložní paměť | optické disky, páska | s | TB |

## Princip lokality
Hierarchie funguje díky **lokalitě odkazů**:
- **časová lokalita** — nedávno použitá data budou pravděpodobně použita znovu (→ uchovat v rychlé paměti);
- **prostorová lokalita** — bude se přistupovat k datům poblíž (→ přenášet po **blocích**).

Nejpoužívanější data se drží na nejvyšší vrstvě; cílem je optimální poměr **výkon × cena**.

## Související
- [[Cache]]
- [[Von-Neumannova-architektura]]
