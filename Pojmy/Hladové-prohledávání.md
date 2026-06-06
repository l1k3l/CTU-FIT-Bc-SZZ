---
aliases: [hladové prohledávání, hladového prohledávání, hladovým prohledáváním, hladový algoritmus, greedy search, greedy best-first, hladové nejlepší-první]
tags: [algoritmus, kurz/ZUM]
---

# Hladové prohledávání (greedy)

## Idea

Best-first strategie, která k expanzi vždy vybírá OPEN stav s **minimální [[Heuristika|heuristikou]]**:
$$s^* \in \arg\min_{s \in OPEN} h(s),$$
tj. řadí prioritní frontu podle $f(s) = h(s)$. Snaží se co nejrychleji („hladově") přiblížit cílovému stavu.

## Vlastnosti

- má „tah na bránu" (na rozdíl od [[Dijkstra|Dijkstry]], která prohledává všesměrově),
- **není optimální** — nalezená cesta nemusí být nejlevnější (zohledňuje jen odhad zbývající cesty, ne dosud ujetou cenu),
- rychlost i kvalita zcela závisí na kvalitě heuristiky; greedy se může nechat svést překážkou nebo jít zbytečnou oklikou.

> Pozor na kolizi zkratek: **BFS = Breadth-First Search** $\ne$ best-first search.

## Související

- [[A-star]] (= greedy zkombinované s dosud ujetou cenou), [[Heuristika]], [[Dijkstra]], [[Stavový-prostor]]
