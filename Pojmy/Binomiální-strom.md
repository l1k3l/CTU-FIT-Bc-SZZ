---
aliases: [binomiální strom, binomiálního stromu, binomiálnímu stromu, binomiálním stromem, binomiální stromy, binomiálních stromů, binomiálních stromům]
tags: [definice, datová-struktura, kurz/AG1]
---

# Binomiální strom

## Definice
**Binomiální strom řádu $k$** (značíme $B_k$) je uspořádaný zakořeněný strom definovaný rekurzivně:
- $B_0$ je tvořen jediným vrcholem (kořenem).
- Pro $k \ge 1$ vznikne $B_k$ ze stromů $B_0, B_1, \dots, B_{k-1}$ přidáním nového kořene, jehož syny jsou (v tomto pořadí) kořeny těchto stromů.

**Alternativní (ekvivalentní) definice:** $B_k$ vznikne ze dvou kopií $B_{k-1}$ tím, že kořen jedné z nich připojíme jako nejpravějšího syna kořene druhé. (Tato definice ukazuje, jak rychle „slévat" stromy téhož řádu.)

## Vlastnosti
- $B_k$ má **$2^k$ vrcholů**.
- $B_k$ má **$k+1$ hladin** (kořen je na hladině 0).
- Kořen $B_k$ má **stupeň $k$**.
- Počet vrcholů $B_k$ na hladině $i$ je $\binom{k}{i}$ (odtud název **binomiální**).

## Použití
- Stavební kámen [[Binomiální-halda|binomiální haldy]] — $n$-prvková BH obsahuje strom $B_i$ právě tehdy, když $i$-tý bit dvojkového zápisu $n$ je 1.

## Související
- [[Binomiální-halda]]
- [[Binární-halda]]
