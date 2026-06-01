---
aliases: [fronta, fronty, frontě, frontu, frontou, front, frontám, queue, FIFO, prioritní fronta, kruhové pole]
tags: [definice, datová-struktura, kurz/PA2]
---

# Fronta (Queue)

## Definice
**Fronta** je [[Abstraktní-datový-typ|ADT]] s disciplínou **FIFO** (First In, First Out) — prvky se odebírají v pořadí, v jakém byly vloženy.

## Operace
- `empty` — test prázdnosti,
- `enqueue` — přidá prvek na konec,
- `dequeue` — vyjme nejstarší prvek.

Ideálně všechny v konstantním čase.

## Implementace a složitost
- **Pole pevné délky.**
- **[[Nafukovací-pole]] (souvislý úsek):** vkládá na konec, odebírá posunem počítadla začátku; když je vpředu příliš místa, prvky se přesunou na začátek → vkládání **amortizovaně** $O(1)$.
- **Kruhové pole** (indexace modulo, `data[(i+first) % cap]`): pokud se nemění velikost podkladového pole, jsou **všechny operace** $O(1)$ i v nejhorším případě.
- **[[Spojový-seznam]]** s ukazatelem na konec: enqueue i dequeue $O(1)$.

V STL: `std::queue` (wrapper nad `deque`/`list`), případně `std::deque` (oboustranná fronta, přístup i indexem $O(1)$).

## Prioritní fronta
**Fronta s předbíháním:** `insert` (s prioritou, duplicity povoleny) a `extract_min` (vyjme libovolný prvek s nejmenší prioritou). Naivně polem je `extract_min` lineární; efektivní implementací je **[[Binární-halda]]** ($O(\log n)$ na operaci). V STL: `std::priority_queue`.

## Související
- [[Abstraktní-datový-typ]]
- [[Zásobník]]
- [[Binární-halda]]
- [[Spojový-seznam]]
