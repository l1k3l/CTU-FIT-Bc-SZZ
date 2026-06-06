---
aliases: [minimax, algoritmus minimax, minimaxu, minimaxem, minimaxový]
tags: [algoritmus, kurz/ZUM]
---

# Algoritmus Minimax

## Princip

Volí optimální tah v kořeni [[Herní-strom|herního stromu]] za předpokladu **perfektní hry soupeře**. Průchodem do hloubky vygeneruje strom (do max. hloubky $d$) a každému uzlu $x$ přiřadí hodnotu $\mathit{eval}[x]$:
- $\mathit{eval}[x] = u(x)$, je-li $x$ terminál (skutečná utilita) **nebo** byla v hloubce $d$ ukončena expanze (heuristická **evaluační funkce**);
- $\mathit{eval}[x] = \max_{a} \mathit{eval}[\sigma(x, a)]$ v uzlu **MAX**;
- $\mathit{eval}[x] = \min_{a} \mathit{eval}[\sigma(x, a)]$ v uzlu **MIN**.

Vrátí akci $\arg\max_a \mathit{eval}[\sigma(x_0, a)]$ v kořeni.

## Vlastnosti

- **Optimální** proti optimálně hrajícímu soupeři.
- Čas $O(b^d)$, prostor $O(b \cdot d)$ ($b$ = větvící faktor, $d$ = hloubka). V šachách $b \approx 35$ → základní Minimax je pro hlubší hledání neúnosný.
- Zrychlení beze ztráty výsledku: **[[Alfa-beta-prořezávání]]**.

## Související

- [[Alfa-beta-prořezávání]], [[Herní-strom]]
