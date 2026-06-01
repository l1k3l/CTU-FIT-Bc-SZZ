---
aliases: [slovník, slovníku, slovníkem, slovníky, slovníků, slovníkům, mapa, mapy, asociativní pole, tabulka, tabulky, tabulce, tabulku, tabulkou, tabulek]
tags: [definice, datová-struktura, kurz/AG1, kurz/PA2]
---

# Slovník

## Definice
**Slovník** (mapa, asociativní pole) je datová struktura reprezentující dynamickou podmnožinu prvků s klíči $K \subseteq \mathcal{U}$, kde $|K| \ll |\mathcal{U}|$. Podporuje operace:
- `Find(k)` — zjisti, zda prvek s klíčem $k$ leží v $K$ (případně vrať jeho hodnotu).
- `Insert(x)` — pokud klíč $x$ ještě není ve slovníku, vlož ho.
- `Delete(x)` — pokud klíč $x$ je ve slovníku, vymaž ho.

Klíče jsou **unikátní** a $\mathcal{U}$ je **univerzum** všech možných klíčů.

## Implementace
- **Bitové pole / tabulka s přímým adresováním** — $O(1)$ ale $\Theta(|\mathcal{U}|)$ paměti.
- **Seřazené pole** — $O(\log n)$ hledání, $O(n)$ vkládání/mazání.
- **Vyvážený [[BVS]]** (např. [[AVL-strom]]) — $O(\log n)$ na operaci.
- **[[Hešovací-tabulka]]** — $O(1)$ amortizovaně v průměrném případě.

## Použití v PA2 (tabulka / mapa)
V BI-PA2 jsou **tabulka = mapa = slovník** synonyma pro **asociativní** strukturu klíč → hodnota: kontejner hodnot typu `Value`, kde prvek je identifikován **klíčem** typu `Key`. Operace: `set(k,v)` (nastav), `get(k)` (získej), `erase(k)`, `contains(k)`. Implementace a složitosti jsou stejné jako u [[Množina|množiny]] (mapa = množina s netriviálním typem hodnoty). V STL: `std::map` (strom, $O(\log n)$), `std::unordered_map` (hešování, průměrně $O(1)$).

## Související
- [[Množina]]
- [[Hešovací-tabulka]]
- [[BVS]]
