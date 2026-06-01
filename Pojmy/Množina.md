---
aliases: [množina, množiny, množině, množinu, množinou, množin, množinám, množinách, set, charakteristický vektor]
tags: [definice, datová-struktura, kurz/PA2]
---

# Množina (Set)

## Definice
**Množina** je [[Abstraktní-datový-typ|ADT]] — kontejner prvků typu `T` **bez duplikátů**.

**Základní operace:** `insert` (vložení), `erase` (odstranění), `contains` (test přítomnosti).
**Další operace:** sjednocení (`union`), průnik (`intersection`), rovnost (`equal`), podmnožina (`subset`), výpis prvků.

Množina je úzce příbuzná s **tabulkou / mapou** (viz [[Slovník]]): množina = mapa s jednoprvkovým typem hodnoty; mapa = množina klíčonosných struktur. Detailněji se popisuje množina (má více operací), mapa je analogická.

## Implementace a složitost
| implementace | insert | erase | contains | ∪ / ∩ | equal |
|---|---|---|---|---|---|
| charakteristický vektor | $O(1)$ | $O(1)$ | $O(1)$ | $O(\|U\|)$ | $O(\|U\|)$ |
| neseřazené pole / seznam | $O(n)$ | $O(n)$ | $O(n)$ | $O(nm)$ | $O(n^2)$ |
| seřazené **pole** | $O(n)$ | $O(n)$ | $O(\log n)$ | $O(n{+}m)$ | $O(n)$ |
| seřazený **seznam** | $O(n)$ | $O(n)$ | $O(n)$ | $O(n{+}m)$ | $O(n)$ |
| vyvážený [[BVS|strom]] | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n{+}m)$ | $O(n{+}m)$ |
| [[Hešovací-tabulka|hešování]] | $O(1)^*$ | $O(1)^*$ | $O(1)^*$ | $O(n{+}m)$ | $O(n{+}m)$ |

- **Charakteristický vektor** (bool/bitové pole) — složitost závisí na velikosti **univerza**, ne množiny; paměť $\Theta(|U|)$.
- **Seřazené pole** umožní binární hledání ($O(\log n)$ contains), množinové operace mergem $O(n+m)$; **seřazený seznam** binární hledání neumožní (contains $O(n)$).
- ($^*$ = průměrný případ u hešování; nevyvážený strom má $O(n)$ v nejhorším případě.)

V STL: `std::set` (červeno-černý strom, $O(\log n)$), `std::unordered_set` (hešování, průměrně $O(1)$).

## Související
- [[Slovník]]
- [[BVS]]
- [[Hešovací-tabulka]]
- [[Abstraktní-datový-typ]]
