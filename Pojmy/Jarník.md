---
aliases: [Jarník, Jarníkův algoritmus, Jarníkova algoritmu, Prim, Primův algoritmus]
tags: [algoritmus, kurz/AG1]
---

# Jarníkův algoritmus (Prim)

## Idea

Hladový (greedy) algoritmus pro [[Minimální-kostra|minimální kostru]]. Začneme stromem o 1 vrcholu. Opakovaně přidáme **nejlehčí hranu**, která vede mezi dosud vytvořeným stromem a zbytkem grafu.

## Implementace binární haldou

Vrcholy uchováváme v minimové [[Binární-halda|binární haldě]], klíčem je „vzdálenost od stromu":
- `ExtractMin` → vrchol $u$ s minimálním $d$, přidáme ho do $T$.
- Pro sousedy $v$ z $u$ použijeme `DecreaseKey`, pokud nová hrana zlepší jejich $d$.

## Složitost

$O(|E| \log |V|)$ s binární haldou: $|V|$-krát `ExtractMin` = $O(|V| \log |V|)$, nejvýše $|E|$-krát `DecreaseKey` = $O(|E| \log |V|)$.

## Korektnost

Z [[Minimální-kostra|lemmatu o řezech]]: hrana přidaná Jarníkem je nejlehčí hranou elementárního řezu mezi stromem $T$ a zbytkem $V \setminus V(T)$, tedy patří do každé MST.

## Související

- [[Minimální-kostra]]
- [[Kruskal]]
- [[Binární-halda]]
