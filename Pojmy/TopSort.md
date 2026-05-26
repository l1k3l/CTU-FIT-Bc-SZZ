---
aliases: [TopSort, topologické řazení, Kahnův algoritmus]
tags: [algoritmus, kurz/AG1]
---

# TopSort (Kahnův algoritmus)

## Specifikace

**Vstup:** [[Orientovaný-graf|orientovaný graf]] $G$.

**Výstup:** [[Topologické-uspořádání|Topologické uspořádání]] (pokud existuje), nebo detekce cyklu.

## Idea

1. Spočti vstupní stupně všech vrcholů.
2. Vlož všechny **zdroje** (vrcholy se vstupním stupněm 0) do fronty.
3. Opakovaně vyjmi vrchol $z$, vypiš ho, sniž vstupní stupně jeho následníků; když některému klesne na 0, zařaď ho.
4. Pokud nakonec zbyly nezpracované vrcholy, graf obsahuje orientovaný cyklus.

## Složitost

$O(|V| + |E|)$ při reprezentaci [[Seznam-sousedů|polem následníků]].

## Související

- [[Topologické-uspořádání]]
- [[DAG]]
- [[Orientovaný-graf]]
