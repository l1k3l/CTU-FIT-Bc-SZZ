---
aliases: [alfa-beta prořezávání, alfa-beta ořezávání, alfa-beta prořezáváním, alpha-beta pruning, alfa-beta, alfabeta, alfa-beta prořez]
tags: [algoritmus, kurz/ZUM]
---

# Alfa-beta prořezávání

## Princip

Optimalizace [[Minimax|Minimaxu]], která vrací **stejný výsledek**, ale neprochází větve, jež nemohou ovlivnit rozhodnutí v kořeni. Po cestě ke kořeni se udržují dvě meze:
- $\alpha$ = nejlepší (největší) hodnota dosud zaručená pro **MAX**,
- $\beta$ = nejlepší (nejmenší) hodnota dosud zaručená pro **MIN**.

Expandovaný potomek **dědí** $\alpha, \beta$ rodiče. V uzlu MAX se aktualizuje (zvyšuje) $\alpha$, v uzlu MIN se aktualizuje (snižuje) $\beta$. Jakmile **$\alpha \ge \beta$** („překřížení" — interval $(\alpha, \beta)$ je prázdný), zbývající potomci aktuálního uzlu se **prořežou** (nemohou výsledek změnit).

## Vliv uspořádání tahů

Zrychlení závisí na **pořadí expanze** uzlů:
- **optimální** pořadí (nejlepší tah první): $O(b^{d/2})$ — efektivní větvící faktor $b \to \sqrt{b}$, což **zdvojnásobí** prohledatelnou hloubku;
- **náhodné** pořadí: přibližně $O(b^{3d/4})$.

K dobrému pořadí pomáhají heuristiky (např. *killer heuristic* — prioritizuj tah, který už jinde ve stromě způsobil prořez).

## Související

- [[Minimax]], [[Herní-strom]]
