---
aliases: [hešování s řetízky, hashování s řetízky, řetízkování, chaining, otevřené hešování]
tags: [definice, datová-struktura, kurz/AG1]
---

# Hešování s řetízky

## Definice
**Hešování s řetízky** (Chaining, Open hashing) je metoda řešení kolizí v [[Hešovací-tabulka|hešovací tabulce]]: každá přihrádka $A[i]$ obsahuje **ukazatel na řetízek** (spojový seznam) všech prvků s $h(k) = i$.

## Operace
- `Find(k)`: spočti $h(k)$, projdi řetízek v dané přihrádce.
- `Insert(x)`: spočti $h(k(x))$, přidej $x$ na začátek (nebo konec) řetízku.
- `Delete(x)`: spočti $h(k(x))$, najdi a odeber $x$ z řetízku.

## Složitost
- Při ideální hešovací funkci a rovnoměrně náhodných datech mají skoro všechny řetízky délku $O(n/m) = O(\alpha)$.
- Pro $m = \Theta(n)$ vyjde **konstantní** průměrná složitost všech operací.

## Vlastnosti
- Mazání je **bezproblémové** (jen odebrání ze seznamu).
- Faktor naplnění $\alpha$ může být i $> 1$.
- Nevýhoda: dodatečná paměť na ukazatele.

## Související
- [[Hešovací-tabulka]]
- [[Otevřená-adresace]]
