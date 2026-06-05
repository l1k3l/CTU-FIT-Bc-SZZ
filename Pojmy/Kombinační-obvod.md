---
aliases: [kombinační obvod, kombinačního obvodu, kombinačním obvodu, kombinační obvody, kombinačních obvodů, kombinační logický obvod]
tags: [definice, kurz/SAP]
---

# Kombinační obvod

## Definice
**Kombinační (logický) obvod** je obvod, ve kterém je každý výstup $out_i$ určen **pouze okamžitou kombinací hodnot vstupů** $in_j$ — nezávisí na historii (na pořadí předchozích vstupů). Nemá tedy paměť. Výstupy popisujeme logickými funkcemi $f:\{0,1\}^n\to\{0,1\}$ pomocí [[Booleova-algebra|Booleovy algebry]].

Kontrast: [[Sekvenční-obvod|sekvenční obvod]], jehož výstup závisí i na **posloupnosti** vstupů (má paměť přes zpětnou vazbu).

## Popis a kanonické tvary
- **Pravdivostní tabulka**, Boolova formule, jednotková krychle.
- **ÚNDF** (úplná normální disjunktivní forma) = součet **mintermů** (kanonický SOP).
- **ÚNKF** (úplná normální konjunktivní forma) = součin **maxtermů** (kanonický POS).
- Zkratší zápis přes seznam stavových indexů $\sum(\dots)$ / $\prod(\dots)$.

## Realizace na úrovni hradel
Dvojúrovňová realizace **AND-OR** (z MNDF), pro ASIC převedeno na **NAND-NAND** (resp. NOR-NOR). Minimalizace [[Karnaughova-mapa|mapou]] nebo algebraicky. Pozor na **hazardy** (různé zpoždění cest → krátký zákmit na výstupu).

## Typické kombinační bloky
[[Dekodér]], [[Multiplexor]], [[Sčítačka]], komparátor, převodníky kódů.

## Související
- [[Sekvenční-obvod]]
- [[Booleova-algebra]]
- [[Karnaughova-mapa]]
