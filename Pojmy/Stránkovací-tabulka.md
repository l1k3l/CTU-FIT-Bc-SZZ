---
aliases: [stránkovací tabulka, stránkovací tabulky, stránkovací tabulce, stránkovací tabulku, stránkovacích tabulek, page table, ST]
tags: [definice, kurz/OSY]
---

# Stránkovací tabulka

## Definice
**Stránkovací tabulka** (ST, *page table*) je datová struktura (závislá na ISA
procesoru), v níž OS udržuje **mapování stránek VAS na rámce** hlavní paměti, spolu
s **řídicími bity**. OS udržuje ST pro každý proces; bázi drží registr **PTBR**.

Typický řádek ST (pro jednu stránku) obsahuje **číslo rámce** a řídicí bity:
- **P** (present) — zda je stránka v hlavní paměti,
- **A** (accessed) — zda se ke stránce přistupovalo,
- **D** (dirty) — zda byl obsah stránky modifikován,
- **C** (cache enabled/disabled), **W** (read/write), **X** (executable),
  **U** (user/supervisor), **G** (global — stránka platná pro všechny procesy).

Typy stránkovacích tabulek:
- **jednoúrovňová** — jeden řádek na každou stránku VAS; číslo stránky je index do
  tabulky (rychlá, ale paměťově náročná),
- **víceúrovňová** (*multilevel*) — virtuální adresa je posloupnost indexů do
  tabulek jednotlivých úrovní; v paměti musí být jen tabulky pokrývající používané
  oblasti (šetří paměť, pomalejší překlad),
- **invertovaná** — jeden řádek na každý **rámec** fyzické paměti; jedna tabulka pro
  celý systém, přístup pomocí hašovací funkce a zřetězení.

## Související
- [[Stránkování]]
- [[MMU]]
- [[TLB]]
- [[Výpadek-stránky]]
