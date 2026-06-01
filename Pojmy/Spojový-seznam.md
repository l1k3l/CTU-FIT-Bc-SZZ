---
aliases: [spojový seznam, spojového seznamu, spojovému seznamu, spojovým seznamem, spojové seznamy, spojových seznamů, spojovým seznamům, zřetězený seznam, zřetězeného seznamu, lineární seznam, linked list, seznam]
tags: [definice, datová-struktura, kurz/PA1]
---

# Spojový seznam

## Definice
**Spojový (zřetězený) seznam** je lineární datová struktura tvořená **uzly**, kde každý uzel obsahuje data a **[[Ukazatel]] na následující uzel**. Poslední uzel ukazuje na `nullptr`. Jde o nejjednodušší **spojovou strukturu** — spoje vytvářejí relaci předchůdce → následník a každý prvek má nejvýše jednoho následníka.

```c
typedef struct TElement {
  int val;
  struct TElement *next;   // ukazatel na strukturu samu je dovolen
} TELEMENT;
```

## Varianty
- **Jednosměrný** (single linked) — uzel zná jen následníka.
- **Obousměrný** (double linked) — uzel zná následníka i předchůdce.
- **Kruhový** (cyclic) — poslední uzel ukazuje na první.
- **Se zarážkou (sentinel)** — jeden prvek navíc na konci bez dat; zjednoduší operace a odstraní speciální případ prázdného seznamu (nemění asymptotickou složitost).

## Operace a složitost
| Operace | Složitost |
|---|---|
| Vložení na začátek | $O(1)$ |
| Vložení na konec (bez ukazatele na konec) | $O(n)$ |
| Vložení na konec (s ukazatelem na poslední prvek) | $O(1)$ |
| Hledání / průchod | $O(n)$ |
| Vložení na správné místo (seřazený seznam) | $O(n)$ |

Oproti **poli**: seznam roste po jednom prvku bez znalosti celkové velikosti a vkládá v $O(1)$ na známé místo, ale neumožňuje přístup přes index v $O(1)$ a má režii ukazatelů.

## Použití v jiných kurzech
- **BI-AG1:** řetízky v [[Hešování-s-řetízky|hešování s řetízky]], seznamy sousedů u grafů ([[Seznam-sousedů]]).

## Související
- [[Ukazatel]]
- [[Hešování-s-řetízky]]
- [[Seznam-sousedů]]
