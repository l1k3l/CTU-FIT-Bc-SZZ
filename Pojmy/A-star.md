---
aliases: [A*, A star, áčko, algoritmus A*, algoritmu A*, algoritmem A*, A-star]
tags: [algoritmus, kurz/ZUM]
---

# Algoritmus A*

## Idea

Kombinuje [[Dijkstra|Dijkstrovu]] dosud ujetou cenu $g(s)$ a [[Hladové-prohledávání|hladový]] [[Heuristika|heuristický]] odhad zbývající cesty $h(s)$. K expanzi volí OPEN stav minimalizující
$$f(s) = g(s) + h(s).$$
Má tedy „tah na bránu" (jako greedy) i nárok na optimalitu (jako Dijkstra). `open` je prioritní fronta dle $f$; je-li k uzlu nalezena levnější cesta, klíč $f$ se aktualizuje (relaxace).

Speciální případy: $h \equiv 0 \Rightarrow$ [[Dijkstra]]; vynechání $g \Rightarrow$ [[Hladové-prohledávání|greedy]].

## Optimalita (podmínky)

- $h$ **monotónní (konzistentní)** $\Rightarrow$ $h$ je i přípustná a A* (s množinou CLOSED, tj. grafové prohledávání) **najde optimální řešení**;
- $h$ **přípustná, ale nekonzistentní** $\Rightarrow$ A* je optimální, *jen nepoužívá-li CLOSED* (stromové prohledávání / znovuotevírání uzlů);
- $h$ **nepřípustná** $\Rightarrow$ optimalita není zaručena.

A* je optimální algoritmus pro danou heuristiku — „lepší algoritmus neexistuje, zbývá jen zlepšovat heuristiky".

## Související

- [[Heuristika]], [[Hladové-prohledávání]], [[Dijkstra]], [[Stavový-prostor]]
