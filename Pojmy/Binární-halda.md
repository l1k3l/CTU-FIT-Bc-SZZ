---
aliases: [binární halda, binární haldy, binární haldě, binární haldu, halda, haldy, haldě, haldu]
tags: [datová-struktura, kurz/AG1]
---

# Binární halda

## Definice

**Binární minimová halda** je datová struktura tvaru binárního stromu, v jehož každém vrcholu $x$ je uložen klíč $k(x)$ a která splňuje dvě vlastnosti:
1. **Tvar haldy:** Strom má všechny hladiny kromě poslední plně obsazené; poslední hladina je zaplněna od levého okraje směrem k pravému.
2. **Haldové uspořádání:** Je-li $v$ vrchol a $s$ jeho syn, platí $k(v) \le k(s)$.

V kořeni je tedy globální minimum. Analogicky se definuje **maximová halda** ($\ge$ místo $\le$).

**Počet hladin:** $\lfloor \log n \rfloor + 1$.

**Reprezentace v poli:** Vrcholy očíslujeme po hladinách 1 až $n$; pak vrchol $i$ má levého syna $2i$, pravého $2i+1$, otce $\lfloor i/2 \rfloor$.

## Operace (min-halda)

- `HeapInsert(H, k)` — vlož klíč $k$ (na konec, pak `BubbleUp`); $O(\log n)$.
- `HeapFindMin(H)` — vrať klíč kořene; $O(1)$.
- `HeapExtractMin(H)` → vrátí a odstraní minimum (kořen vymění s posledním listem, `BubbleDown`); $O(\log n)$.
- `HeapDecreaseKey(H, x, k)` — sníží klíč prvku $x$ na $k$; $O(\log n)$.
- `HeapBuild(x_1, \dots, x_n)` — vytvoří haldu zdola nahoru (`BubbleDown` od $\lfloor n/2 \rfloor$ ke kořeni); $O(n)$.

## Použití

- Prioritní fronta v [[Dijkstra|Dijkstrově]] a [[Jarník|Jarníkově]] algoritmu.
- `HeapSort`: $O(n \log n)$ in-place.

## Související

- [[Dijkstra]]
- [[Jarník]]
- [[Binomiální-halda]]
