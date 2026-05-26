---
aliases: [AVL strom, AVL stromu, AVL stromem, AVL stromy, AVL stromů, AVL stromům, hloubkově vyvážený]
tags: [definice, datová-struktura, kurz/AG1]
---

# AVL strom

## Definice
**AVL strom** je [[BVS|binární vyhledávací strom]], který je **hloubkově vyvážený**:
$$\forall v: \; |h(L(v)) - h(R(v))| \le 1.$$

Pro každý vrchol $v$ definujeme **znaménko**
$$\delta(v) = h(R(v)) - h(L(v)) \in \{-1, 0, +1\}.$$

## Vlastnosti
**Věta:** Hloubkově vyvážený strom s $n$ vrcholy má hloubku $\Theta(\log n)$.

*Idea důkazu:* Minimální AVL strom hloubky $h$ má $A_h = A_{h-1} + A_{h-2} + 1$ vrcholů (Fibonacciho rekurence) ⟹ $A_h \ge (\sqrt{2})^h$ ⟹ hloubka stromu s $n$ vrcholy je $\le \log_{\sqrt{2}}(n) + 1 = \Theta(\log n)$.

## Operace
Operace `BVSShow`, `BVSMin`, `BVSPred`, `BVSFind` nemění tvar — fungují beze změny v čase $O(\log n)$.

**`AVLInsert`** a **`AVLDelete`** vloží/vyjmou vrchol jako u BVS a poté po cestě zpět do kořene **opravují** případné porušení hloubkové vyváženosti pomocí **[[Rotace-v-BVS|rotací]]**:
- **Jednoduchá rotace** (L nebo R) — když porušení je „lineární".
- **Dvojitá rotace** (LR nebo RL) — když porušení je „zalomené" (cik-cak).

Volba rotace závisí na znaménkách vrcholů na cestě porušení.

**Složitost:** `AVLInsert`, `AVLDelete`, `AVLFind` všechny $O(\log n)$ — hloubka je $\Theta(\log n)$ a na každé hladině provedeme $\Theta(1)$ operací.

## Související
- [[BVS]]
- [[Rotace-v-BVS]]
