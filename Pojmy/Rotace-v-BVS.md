---
aliases: [rotace, rotaci, rotace doleva, rotace doprava, dvojitá rotace, jednoduchá rotace, LR rotace, RL rotace]
tags: [definice, kurz/AG1]
---

# Rotace v BVS

## Definice
**Rotace** v [[BVS|binárním vyhledávacím stromě]] je lokální úprava tvaru stromu okolo hrany $\{x, y\}$, která **zachovává BVS-uspořádání** (vzestupný InOrder výpis), ale mění hloubky podstromů.

## Jednoduché rotace
**Rotace doprava** (R) okolo $\{x, y\}$, kde $y = \ell(x)$:
```
        x                y
       / \              / \
      y   C    →       A   x
     / \                  / \
    A   B                B   C
```
**Rotace doleva** (L) okolo $\{x, y\}$, kde $y = r(x)$, je zrcadlovou symetrií.

## Dvojité rotace
**LR rotace** = nejprve L na hraně $\{y, z\}$, pak R na hraně $\{x, y\}$. Používá se, když porušení vyváženosti tvoří „cik-cak" tvar.

**RL rotace** symetricky.

## Použití v [[AVL-strom|AVL stromech]]
Po vložení/odstranění vrcholu se po cestě k kořeni kontrolují znaménka $\delta(v) = h(R(v)) - h(L(v))$ a:
- při $\delta(x) = \pm 2$ se provede jednoduchá nebo dvojitá rotace podle znaménka syna, ze kterého přišlo prohloubení.

Každá rotace má složitost $O(1)$. V `AVLInsert` stačí **jedna** (jednoduchá nebo dvojitá) rotace, v `AVLDelete` jich může být až $O(\log n)$ po cestě ke kořeni.

## Související
- [[BVS]]
- [[AVL-strom]]
