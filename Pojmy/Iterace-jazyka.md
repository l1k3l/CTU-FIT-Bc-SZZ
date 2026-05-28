---
aliases: [iterace jazyka, iteraci jazyka, iterací jazyka, Kleeneho hvězdice, Kleeneho uzávěr, Kleene star, Kleeneova hvězdice, Kleeneova iterace, hvězdičkový uzávěr]
tags: [definice, kurz/AAG]
---

# Iterace jazyka (Kleeneho hvězdice)

## Definice

Pro jazyk $L \subseteq \Sigma^*$:
- **mocnina jazyka:** $L^0 = \{\varepsilon\}$, $L^{n} = L \cdot L^{n-1}$ pro $n \ge 1$,
- **iterace (Kleeneho hvězdice):** $L^* = \bigcup_{n \ge 0} L^n$,
- **pozitivní iterace (Kleeneho plus):** $L^+ = \bigcup_{n \ge 1} L^n = L \cdot L^*$.

Tedy $L^*$ obsahuje všechny řetězce, které vzniknou zřetězením libovolného (i nulového) počtu slov z $L$; $L^+$ vyžaduje alespoň jedno slovo.

## Vlastnosti

- $\Sigma^* = (\Sigma_1)^*$, kde $\Sigma_1 = \{a : a \in \Sigma\}$ — všechny jednoznakové jazyky abecedy.
- $(L^*)^* = L^*$.
- $L^* = \{\varepsilon\} \cup L^+$.
- $\varepsilon \in L^*$ vždy.
- Pokud $\varepsilon \in L$, pak $L^+ = L^*$.

## Vztah ke regulárním výrazům

Iterace je jednou ze tří základních operací v definici [[Regulární-výraz|regulárních výrazů]]: $(x)^*$ označuje $L(x)^*$. Z **Kleeneho věty** plyne, že [[Regulární-jazyk|regulární jazyky]] jsou uzavřeny na iteraci.

## Konstrukce na konečném automatu

Pro [[Konečný-automat|NKA-$\varepsilon$]] $M$ s jazykem $L$ se sestrojí $M^*$ s $L(M^*) = L^*$: přidá se nový počáteční stav $q'_0$ s $\varepsilon$-přechodem do $q_0$, z každého koncového stavu se přidá $\varepsilon$-přechod zpět do $q_0$, a $F' := F \cup \{q'_0\}$ (aby $M^*$ přijímal i $\varepsilon$).

## Související
- [[Regulární-výraz]]
- [[Regulární-jazyk]]
