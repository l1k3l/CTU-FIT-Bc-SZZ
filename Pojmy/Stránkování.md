---
aliases: [stránkování, stránkováním, stránka, stránky, stránek, stránce, rámec, rámce, rámců, rámci, paging, page, frame]
tags: [definice, kurz/OSY]
---

# Stránkování

## Definice
**Stránkování** (*paging*) je technika virtualizace hlavní paměti:

- **virtuální adresní prostor (VAS)** procesu je rozdělen na stejně velké souvislé
  úseky — **stránky** (*pages*); velikost stránky je závislá na architektuře CPU,
  typicky 4 KB (Intel), 8 KB (SPARC),
- **hlavní (fyzická) paměť** je rozdělena na stejně velké úseky — **rámce**
  (*frames*),
- libovolnou stránku lze namapovat do libovolného rámce; ve fyzické paměti musí být
  jen **aktuálně používané** stránky, zbytek je odložen na disku.

**Struktura adresy.** Virtuální i fyzická adresa se dělí na dvě části:
$$\text{VA} = (\text{číslo stránky},\ \text{offset}), \qquad
  \text{PA} = (\text{číslo rámce},\ \text{offset}).$$
Offset (poloha uvnitř stránky/rámce) se při překladu nemění; **[[MMU]]** překládá
číslo stránky na číslo rámce pomocí **[[Stránkovací-tabulka|stránkovací tabulky]]**.

Stránkování elegantně řeší **fragmentaci** hlavní paměti a její nedostatek.

## Související
- [[Virtuální-paměť]]
- [[MMU]]
- [[Stránkovací-tabulka]]
- [[Výpadek-stránky]]
