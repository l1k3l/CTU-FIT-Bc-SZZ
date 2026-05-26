---
aliases: [minimální kostra, minimální kostry, minimální kostře, minimální kostru, MST, minimum spanning tree]
tags: [definice, věta, kurz/AG1]
---

# Minimální kostra (MST)

## Definice

Pro hranově ohodnocený souvislý [[Graf|graf]] $G$ s váhovou funkcí $w: E \to \mathbb{R}$ je **minimální kostra** taková [[Kostra|kostra]], která má mezi všemi kostrami **nejmenší součet vah hran** $w(K) = \sum_{e \in K} w(e)$.

## Elementární řez

Nechť $A \subseteq V$ a $B = V \setminus A$. **Elementární řez** určený $A, B$ je množina všech hran s jedním koncem v $A$ a druhým v $B$.

## Lemma o řezech (unikátní váhy)

Je-li $G$ souvislý ohodnocený graf s **unikátními vahami**, $R$ elementární řez a $e$ nejlehčí hrana v $R$, pak každá minimální kostra obsahuje $e$.

**Důsledek:** Souvislý graf s unikátními vahami má **právě jednu** MST. MST je jednoznačně určena uspořádáním hran podle vah, nikoli konkrétními hodnotami.

## Algoritmy

- [[Jarník]] (Prim) — $O(|E| \log |V|)$ s binární haldou.
- [[Kruskal]] — $O(|E| \log |V|)$ s Union-Find.

## Související

- [[Kostra]]
- [[Jarník]], [[Kruskal]]
