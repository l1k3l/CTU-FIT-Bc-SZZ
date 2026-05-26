---
aliases: [Kruskal, Kruskalův algoritmus, Kruskalova algoritmu]
tags: [algoritmus, kurz/AG1]
---

# Kruskalův algoritmus

## Idea

Hladový algoritmus pro [[Minimální-kostra|minimální kostru]]. Seřaď hrany podle vah od nejlehčí. Procházej je v tomto pořadí; každou přidej, **pokud nevytvoří kružnici** (tedy její koncové vrcholy leží v různých komponentách aktuálního lesa).

Komponenty udržuj ve struktuře [[Union-Find|Union-Find]].

## Složitost

$O(|E| \log |V|)$:
- Seřazení hran: $O(|E| \log |E|) = O(|E| \log |V|)$.
- Union-Find operace s keříky: každá $O(\log n)$, celkem $O(|E| \log n + n \log n)$.

## Korektnost

Z [[Minimální-kostra|lemmatu o řezech]] (přidávaná nejlehčí hrana je nejlehčí v řezu mezi dvěma komponentami).

## Související

- [[Minimální-kostra]]
- [[Jarník]]
- [[Union-Find]]
