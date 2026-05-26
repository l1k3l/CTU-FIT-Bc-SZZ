---
aliases: [BVS, binární vyhledávací strom, binárního vyhledávacího stromu, binárním vyhledávacím stromem, binární vyhledávací stromy, binárních vyhledávacích stromů]
tags: [definice, datová-struktura, kurz/AG1]
---

# Binární vyhledávací strom (BVS)

## Definice
**Binární vyhledávací strom (BVS)** je binární strom, v jehož každém vrcholu $v$ je uložen unikátní klíč $k(v)$ a pro každý vrchol platí:
- Pokud $a \in L(v)$ (levý podstrom), pak $k(a) < k(v)$.
- Pokud $b \in R(v)$ (pravý podstrom), pak $k(b) > k(v)$.

Tedy: **InOrder průchod** (levý podstrom — kořen — pravý podstrom) vrátí klíče vzestupně.

## Operace

| Operace | Popis | Složitost |
|---|---|---|
| `BVSShow(v)` | vzestupně vypiš klíče $T(v)$ | $O(|T(v)|)$ |
| `BVSMin(v)` / `BVSMax(v)` | nejmenší/největší klíč | $O(h)$ |
| `BVSFind(v, x)` | najdi vrchol s klíčem $x$ | $O(h)$ |
| `BVSPred(v, w)` / `BVSSucc(v, w)` | předchůdce/následník v InOrder | $O(h)$ |
| `BVSInsert(v, x)` | vlož klíč $x$ (jako list) | $O(h)$ |
| `BVSDelete(v, x)` | odstraň vrchol s klíčem $x$ | $O(h)$ |

kde $h = h(T(v))$ je **hloubka** stromu.

## Vyváženost a hloubka
- V nejlepším případě $h = \Omega(\log n)$, v nejhorším $h = O(n)$ (degenerovaný strom — např. vložení klíčů $1, 2, \dots, n$ v tomto pořadí).
- **Dokonale vyvážený BVS** ($\forall v: ||L(v)| - |R(v)|| \le 1$): existuje, $h = 1 + \lfloor \log n \rfloor$, ale **nelze ho udržovat** během vkládání/mazání v čase $O(\log n)$ (věta o $\Omega(n)$ složitosti alespoň jedné operace).
- Praktická řešení: **hloubkově vyvážené** stromy — [[AVL-strom|AVL stromy]] (kritérium $|h(L(v)) - h(R(v))| \le 1$), červeno-černé stromy, B-stromy, …

## Související
- [[AVL-strom]]
- [[Binární-halda]]
- [[Strom]]
