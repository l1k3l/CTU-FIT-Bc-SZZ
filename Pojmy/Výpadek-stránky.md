---
aliases: [výpadek stránky, výpadku stránky, výpadky stránek, výpadkem stránky, page fault]
tags: [definice, kurz/OSY]
---

# Výpadek stránky (page fault)

## Definice
**Výpadek stránky** (*page fault*) je přerušení, které vyvolá **[[MMU]]** při pokusu
o přístup na virtuální stránku, jež **není v hlavní paměti** (řádek
**[[Stránkovací-tabulka|stránkovací tabulky]]** má neplatný *present* bit P).

Obsluha výpadku v OS:
1. ověří platnost virtuální adresy a oprávněnost přístupu (jinak *segmentation fault*),
2. **získá volný rámec** — není-li volný, vybere oběť **algoritmem pro náhradu
   stránek**; byla-li oběť modifikována (*dirty*), zapíše ji na disk a aktualizuje
   ST všech dotčených procesů,
3. nahraje požadovanou stránku do rámce — ze **zdrojového souboru** (spustitelný
   soubor, mmap), ze **swapovacího souboru**, nebo ji **vynuluje** (heap, stack,
   anonymní paměť),
4. aktualizuje ST (číslo rámce, P = 1) a **zopakuje** přerušenou instrukci.

## Související
- [[Stránkování]]
- [[MMU]]
- [[Stránkovací-tabulka]]
- [[Virtuální-paměť]]
