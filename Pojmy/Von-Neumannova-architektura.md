---
aliases: [von Neumannova architektura, von Neumannovy architektury, von Neumannově architektuře, von Neumann, von Neumannův počítač, Harvardská architektura, harvardská architektura, číslicový počítač]
tags: [definice, kurz/SAP]
---

# Von Neumannova architektura

## Definice
**Von Neumannova architektura** je koncepce číslicového počítače, v níž jsou **data i instrukce uloženy ve společné paměti** — z výpisu paměti nelze poznat, zda jde o instrukci nebo data (je třeba znát kontext). Počítač má **5 základních částí**:
1. **datová část — ALU** (aritmeticko-logická jednotka),
2. **řídicí část — řadič** (control unit),
3. **hlavní paměť** (paměťový subsystém),
4. **vstupní** a **5. výstupní** zařízení,

propojené **sběrnicí** (adresová / datová / řídicí). Procesor = ALU + registry + řadič.

**von Neumannovo úzké hrdlo (bottleneck):** výkon je omezen přenosem mezi procesorem a pamětí po společné sběrnici. Zmírnění: [[Cache|cache]], DMA.

## Harvardská architektura
**Oddělená paměť instrukcí a paměť dat** (adresují se nezávisle). Typická pro jednočipové mikropočítače (např. AVR). Umožňuje současné čtení instrukce i dat.

## Související
- [[Instrukční-cyklus]]
- [[Instrukční-soubor]]
- [[Paměťová-hierarchie]]
- [[Cache]]
