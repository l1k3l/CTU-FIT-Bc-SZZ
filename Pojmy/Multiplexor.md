---
aliases: [multiplexor, multiplexoru, multiplexory, multiplexorem, multiplexer, MUX, demultiplexor, selektor]
tags: [definice, kurz/SAP]
---

# Multiplexor

## Definice
**Multiplexor (MUX)** je [[Kombinační-obvod|kombinační obvod]], který podle hodnoty $n$ **výběrových (adresových)** vstupů $s_{n-1}\dots s_0$ propojí na jediný výstup právě jeden z $2^n$ **datových** vstupů $d_0\dots d_{2^n-1}$:
$$y=\sum_{k=0}^{2^n-1} m_k(s)\cdot d_k,$$
kde $m_k(s)$ je minterm výběrových proměnných odpovídající indexu $k$. Pro 4-1 MUX:
$$y=\overline{s_1}\,\overline{s_0}\,d_0+\overline{s_1}s_0 d_1+s_1\overline{s_0}d_2+s_1 s_0 d_3.$$

**Struktura:** multiplexor v sobě obsahuje **[[Dekodér|dekodér]]** výběrových vstupů + pole hradel AND-OR. Slouží mj. k výběru sběrnice a jako univerzální realizace logických funkcí.

## Demultiplexor
Obrácená funkce: jeden datový vstup $x$ se podle adresy přivede na jeden z výstupů (ostatní = 0). Strukturálně je to dekodér s daty $x$ jako povolovacím vstupem (enable).

## Související
- [[Dekodér]]
- [[Kombinační-obvod]]
