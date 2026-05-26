---
aliases: [DAG, DAGu, DAGy, DAGů, acyklický graf, acyklického grafu, acyklický orientovaný graf, orientovaný acyklický graf]
tags: [definice, kurz/AG1]
---

# DAG

## Definice

**DAG** (Directed Acyclic Graph) = [[Orientovaný-graf|orientovaný graf]] neobsahující orientovanou kružnici jako podgraf.

## Zdroj a stok

- **Zdroj** = vrchol bez vstupních hran.
- **Stok** = vrchol bez výstupních hran.

**Věta (o existenci zdroje a stoku):** Každý DAG má alespoň jeden zdroj a alespoň jeden stok.

*Důkaz sporem:* Kdyby neexistoval zdroj, do každého vrcholu by vedla hrana → můžeme jít zpět $v_1 \leftarrow v_2 \leftarrow \ldots$ a po $n$ krocích se musí nějaký vrchol zopakovat → cyklus, spor.

## Vztah k topologickému uspořádání

[[Topologické-uspořádání|Topologické uspořádání]] grafu existuje $\iff$ graf je DAG.

## Související

- [[Orientovaný-graf]]
- [[Topologické-uspořádání]]
- [[TopSort]]
