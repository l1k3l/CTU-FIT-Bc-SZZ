---
aliases: [virtuální paměť, virtuální paměti, virtuální pamětí, virtuálního adresního prostoru, VAS, virtual memory]
tags: [definice, kurz/OSY]
---

# Virtuální paměť

## Definice
**Virtuální paměť** je abstrakce, při níž každý **[[Proces|proces]]** používá vlastní
**virtuální adresní prostor (VAS)** — jednorozměrný logický prostor adres, který se
(pomocí HW a OS) mapuje do fyzické hlavní paměti. Instrukce a data procesu používají
**virtuální adresy** (vztažené k začátku VAS).

VAS typicky obsahuje segmenty `.text` (program), `.data` (globální proměnné),
*heap* (halda), knihovny a *stack* (zásobník).

Motivace:
- VAS jednoho procesu může být **větší než instalovaná hlavní paměť** (ve 32-bit
  OS adresuje proces $2^{32}$ B, v 64-bit teoreticky $2^{64}$ B),
- OS umožňuje běh až tisíců procesů ⇒ **součet jejich VAS** opět přesahuje fyzickou
  paměť.

Řešením je **[[Stránkování]]**: VAS je rozdělen na malé kousky a v hlavní paměti
musí být jen kousky aktuálně používané, zbytek je odložen na disku.

## Související
- [[Stránkování]]
- [[MMU]]
- [[Stránkovací-tabulka]]
- [[Výpadek-stránky]]
