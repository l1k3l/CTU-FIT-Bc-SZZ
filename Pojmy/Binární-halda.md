---
aliases: [binární halda, binární haldy, binární haldě, binární haldu, halda, haldy, haldě, haldu]
tags: [datová-struktura, kurz/AG1]
---

# Binární halda

## Definice

Datová struktura — úplný binární strom s **halda-vlastností**: klíč rodiče $\le$ klíče potomků (min-halda) nebo $\ge$ (max-halda).

## Operace (min-halda)

- `Insert(x)` — $O(\log n)$.
- `ExtractMin()` → vrchol s minimálním klíčem; $O(\log n)$.
- `DecreaseKey(x, k)` — sníží klíč prvku $x$ na $k$; $O(\log n)$.
- `HeapBuild(seznam)` — vytvoří haldu; $O(n)$.

## Použití

- Prioritní fronta v [[Dijkstra|Dijkstrově]] a [[Jarník|Jarníkově]] algoritmu.
- Heapsort.

## Související

- [[Dijkstra]]
- [[Jarník]]
