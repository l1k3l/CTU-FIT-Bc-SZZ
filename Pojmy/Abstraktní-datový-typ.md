---
aliases: [abstraktní datový typ, abstraktního datového typu, abstraktnímu datovému typu, abstraktním datovým typem, abstraktní datové typy, abstraktních datových typů, ADT, ADTs, signatura, axiomy]
tags: [definice, kurz/PA2]
---

# Abstraktní datový typ (ADT)

## Definice
**Abstraktní datový typ (ADT)** definuje **množinu hodnot** a **množinu operací** nad nimi, a to **nezávisle na konkrétní implementaci**. (Na rozdíl od [[Datový-typ|datového typu]], který má i konkrétní paměťovou reprezentaci.)

ADT lze **formálně specifikovat**:
- **signaturou operací** = *definice syntaxe* (arita operandů, jejich typy, typ výsledku, notace), např. `push(_,_): stack, elem -> stack`;
- **množinou axiomů** = *definice sémantiky* (ekvivalence mezi výrazy reprezentujícími stav ADT, umožňují zjednodušovat výrazy).

Specifikace neříká nic o tom, jak rychle (a zda vůbec) lze ADT implementovat. Často se používá i **neformální** popis (sémantika slovy/obrázkem).

## Specifikace vs. implementace
- **Specifikace** = *co* — signatury + axiomy (rozhraní a chování), nezávislé na realizaci.
- **Implementace** = *jak* — konkrétní paměťová reprezentace a algoritmy operací. Imperativní jazyky vyžadují explicitní implementaci.
- **Datová struktura** = mezičlánek: rozhraní jako u ADT **+ paměťová reprezentace + algoritmy** (ve vhodném abstraktním modelu). V C++ se ADT typicky implementují jako **generické třídy** ([[Šablona|šablony]]).

Tentýž ADT lze implementovat různě (polem, [[Spojový-seznam|spojovou strukturou]], [[Strom|stromem]], …) s různými časovými složitostmi operací.

## Příklady ADT
[[Zásobník]], [[Fronta]], [[Pole]], [[Množina]], tabulka ([[Slovník]]), prioritní fronta.

## Související
- [[Datový-typ]]
- [[Zásobník]]
- [[Fronta]]
- [[Množina]]
