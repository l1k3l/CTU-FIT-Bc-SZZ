---
aliases: [nafukovací pole, nafukovacího pole, nafukovacímu poli, nafukovací pole, nafukovacích polí, nafukovacím polím]
tags: [definice, datová-struktura, kurz/AG1]
---

# Nafukovací pole

## Definice
**Nafukovací pole** je dynamické 1D pole, do kterého postupně přidáváme prvky, aniž bychom dopředu znali jejich celkový počet. Při zaplnění se velikost pole **zdvojnásobí** a obsah překopíruje.

## Strategie `NPInsert`
- Počáteční kapacita $m_0 = 1$ (nebo malá konstanta).
- Označme $m$ aktuální kapacitu, vkládáme $i$-tý prvek a v poli je již $i-1$ prvků.
- Pokud $i \le m$: vlož na pozici $i$, $O(1)$.
- Pokud $i > m$: alokuj nové pole velikosti $2m$, překopíruj, dealokuj staré, vlož.

## Amortizovaná analýza
**Věta:** Celková složitost posloupnosti $n$ operací `NPInsert` na zpočátku prázdném nafukovacím poli je $\Theta(n)$, tedy [[Amortizovaná-složitost|amortizovaná složitost]] je $\Theta^*(1)$.

*Důkaz (agregační):* Samotná vkládání stojí $\Theta(n)$. Zvětšování probíhá při $i = 2^k$ a stojí $\Theta(2^k)$. Součet $\Theta(2^0 + 2^1 + \dots + 2^k) = \Theta(2^{k+1} - 1) < 2n$. Celkem $\Theta(n)$. $\square$

**Pozn.:** Při zdvojnásobení dostáváme $\Theta^*(1)$. Při zvětšení o pevnou konstantu $c$ by amortizovaná složitost byla $\Theta^*(n)$ (nestačí).

## Použití
- Dynamické pole v reálných implementacích (`std::vector`, `ArrayList`, …).
- Nafukovací **[[Hešovací-tabulka]]** — stejný princip pro $m$ přihrádek.

## Související
- [[Amortizovaná-složitost]]
- [[Binární-sčítačka]]
- [[Hešovací-tabulka]]
