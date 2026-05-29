---
aliases: [MMU, memory management unit, jednotka správy paměti]
tags: [definice, kurz/OSY]
---

# MMU (Memory Management Unit)

## Definice
**MMU** (*Memory Management Unit*) je hardwarová jednotka, která ve spolupráci s OS
zajišťuje **překlad virtuálních adres na fyzické**. Proces má díky ní iluzi, že celý
jeho **[[Virtuální-paměť|virtuální adresní prostor]]** je v hlavní paměti, a pro
adresaci instrukcí/dat používá pouze virtuální adresy.

Princip:
- bázi (číslo rámce) **[[Stránkovací-tabulka|stránkovací tabulky]]** aktuálního
  procesu drží **Page Table Base Register (PTBR)** (na x86 registr `CR3`),
- MMU pomocí ST přeloží číslo stránky na číslo rámce a sestaví fyzickou adresu,
- není-li požadovaná stránka v hlavní paměti (neplatný *present* bit), MMU vyvolá
  přerušení — **[[Výpadek-stránky|výpadek stránky]]** — a OS stránku nahraje,
- pro urychlení překladu MMU využívá **[[TLB]]** (cache nedávno přeložených adres).

## Související
- [[Stránkování]]
- [[Stránkovací-tabulka]]
- [[TLB]]
- [[Výpadek-stránky]]
