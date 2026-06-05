---
aliases: [Karnaughova mapa, Karnaughovy mapy, Karnaughově mapě, Karnaughovou mapou, Karnaughovy mapy, K-mapa, mapa Karnaughova]
tags: [definice, kurz/SAP]
---

# Karnaughova mapa

## Definice
**Karnaughova mapa** je grafický nástroj pro **minimalizaci logické funkce** o malém počtu proměnných (do ~5–6). Je to obdélník rozdělený na $2^n$ polí (po jednom pro každý stavový index), do nichž se zapisuje hodnota funkce. Pole jsou uspořádána pomocí **Grayova kódu** tak, že **sousední pole se liší v hodnotě právě jedné proměnné** (sousední stavy). Sousednost je **cyklická** — krajní sloupce i krajní řádky spolu sousedí.

## Princip minimalizace
Hledáme **maximální skupiny (smyčky)** sousedních jedniček o velikosti mocniny dvou. Skupinu popisují jen ty proměnné, které se v ní **nemění**. Pojmy:
- **implikant** = krychle ležící celá v onsetu funkce;
- **prvoimplikant (přímá krychle)** = implikant, který už nelze zvětšit;
- **podstatný (esenciální) implikant** = pokrývá jedničku nepokrytou žádným jiným prvoimplikantem.

**Algoritmus:** najdi všechny prvoimplikanty → vyber všechny podstatné → doplň dalšími prvoimplikanty, aby byly pokryty všechny jedničky. Výsledek = **MNDF** (minimální disjunktní forma); duálně z nul lze získat **MNKF**.

## Neurčené stavy (*don't care*)
Kombinace, které nemohou nastat, se značí **×** a mohou se libovolně použít jako 0/1 pro zvětšení skupin a zjednodušení výrazu.

Pro mnoho proměnných se místo mapy používá **Quine–McCluskeyho metoda** (tabulková, programovatelná).

## Související
- [[Kombinační-obvod]]
- [[Booleova-algebra]]
