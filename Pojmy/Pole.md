---
aliases: [pole, poli, polem, polí, polím, polích, array, vícedimenzionální pole, dvourozměrné pole, matice pole]
tags: [definice, datová-struktura, kurz/PA2]
---

# Pole (Array)

## Definice
**Pole** je datový kontejner organizující prvky v **$n$-dimenzionálním prostoru** s **náhodným přístupem v konstantním čase**: prvek je identifikován **$n$-ticí indexů**. Popis pole tvoří datový typ prvků, počet dimenzí a dolní/horní meze každé dimenze: `array[l_1..h_1, …, l_n..h_n] of T`; celkem $\prod_i (h_i - l_i + 1)$ prvků.

## Přístupová (mapovací) funkce
Prvky leží v souvislém paměťovém bloku; pozici prvku počítá **mapovací funkce**:
- 1D: `map(i) = i - l_1` (v C/C++ je `l_1 = 0`, tedy `map(i) = i`).
- Vícedimenzionální blok lze serializovat **po řádcích** (row-major, nejpravější index roste nejrychleji) nebo **po sloupcích** (column-major), případně přes **přístupové vektory** (Iliffeho vektory = pole polí, umožní i neobdélníkové matice).

## Statické vs. dynamické
- **Pole pevné délky** — velikost známá při překladu; vestavěné pole C/C++ se konvertuje na [[Ukazatel|ukazatel]] na nultý prvek (`a[i] == *(a+i)`).
- **Dynamické / [[Nafukovací-pole|nafukovací]] pole** — velikost lze měnit za běhu (zdvojnásobování kapacity), vkládání na konec amortizovaně $O(1)$.

Pole je základní stavební blok pro implementaci dalších ADT ([[Zásobník]], [[Fronta]], [[Množina]], [[Binární-halda]]). V STL: `std::array` (pevné), `std::vector` (nafukovací).

## Související
- [[Nafukovací-pole]]
- [[Ukazatel]]
- [[Abstraktní-datový-typ]]
