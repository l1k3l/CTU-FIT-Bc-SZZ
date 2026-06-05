---
aliases: [dekodér, dekodéru, dekodéry, dekodérem, dekodér 1 z N, kodér, enkodér]
tags: [definice, kurz/SAP]
---

# Dekodér

## Definice
**Dekodér** je [[Kombinační-obvod|kombinační obvod]] převádějící $n$-bitový binární kód na kód **„1 z $N$"** ($N=2^n$): aktivuje právě jeden výstup odpovídající hodnotě na vstupu (*one-hot*), ostatní jsou neaktivní. Každý výstup je jediný **minterm** vstupních proměnných, např. pro 2→4 dekodér:
$$y_0=\overline{x_1}\,\overline{x_0},\quad y_1=\overline{x_1}x_0,\quad y_2=x_1\overline{x_0},\quad y_3=x_1 x_0.$$

Často má **povolovací vstup (enable)**. Šetří vývody: pro $n$-bitovou adresu stačí $n$ vodičů místo $2^n$. Používá se k **adresnímu dekódování** (výběr řádku v paměti, výběr čipu) a tvoří jádro [[Multiplexor|multiplexoru]] a demultiplexoru.

**Kodér / enkodér** je obrácený obvod (1 z $N$ → binární kód); prioritní kodér řeší více současně aktivních vstupů.

## Související
- [[Multiplexor]]
- [[Kombinační-obvod]]
