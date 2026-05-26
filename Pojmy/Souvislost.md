---
aliases: [souvislost, souvislosti, souvislý, souvislého, souvislému, souvislém, souvislým, souvislé, souvislých, souvislými, nesouvislý]
tags: [definice, kurz/AG1]
---

# Souvislost

## Definice

[[Graf|Graf]] $G$ je **souvislý**, jestliže pro každé dva jeho vrcholy $u, v$ existuje $u$-$v$-[[Cesta|cesta]]. Jinak je **nesouvislý**.

**Tvrzení:** Binární relace $u \leftrightsquigarrow v \iff$ existuje $u$-$v$-cesta je ekvivalence; její třídy indukují [[Souvislá-komponenta|souvislé komponenty]].

## Orientované grafy

- **Slabě souvislý** orientovaný graf: [[Orientovaný-graf|symetrizace]] $\text{sym}(G)$ je souvislá.
- **Silně souvislý** orientovaný graf: pro každé dva vrcholy $u, v$ existuje orientovaná cesta $u \to v$ **a současně** $v \to u$.

Slabou souvislost testujeme [[BFS|BFS]] na symetrizaci. Silnou lze naivně řešit BFS z každého vrcholu.

## Související

- [[Souvislá-komponenta]]
- [[Cesta]]
- [[BFS]]
