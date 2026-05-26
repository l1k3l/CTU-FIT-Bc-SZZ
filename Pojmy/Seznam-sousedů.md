---
aliases: [seznam sousedů, seznamy sousedů, seznam sousedu, seznam následníků, pole následníků]
tags: [datová-struktura, kurz/AG1]
---

# Seznam sousedů

## Definice

Reprezentace [[Graf|grafu]]. Pro každý vrchol uchováváme seznam jeho sousedů (resp. **následníků** v [[Orientovaný-graf|orientovaném grafu]]).

## Paměť

$O(|V| + |E|)$.

## Trade-off vs. matice sousednosti

- Iterace přes všechny sousedy $v$: $O(\deg v)$ (optimální).
- Test sousednosti dvou konkrétních vrcholů: $O(\deg v)$ (horší než matice).

Pro **řídké grafy** je seznam sousedů preferovaný; většina grafových algoritmů ([[BFS]], [[Dijkstra]], [[Jarník]] aj.) předpokládá tuto reprezentaci.

## Související

- [[Matice-sousednosti]]
- [[Graf]]
