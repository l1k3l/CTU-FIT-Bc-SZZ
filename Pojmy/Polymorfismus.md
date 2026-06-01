---
aliases: [polymorfismus, polymorfismu, polymorfismem, polymorfní, polymorfního, polymorphism, mnohotvarost]
tags: [definice, kurz/PA2]
---

# Polymorfismus

## Definice
**Polymorfismus** (mnohotvarost) v pojetí BI-PA2 znamená **run-time (subtypový) polymorfismus** realizovaný nástroji C++:
- existuje rozhraní dané **[[Virtuální-metoda|virtuálními metodami]]** (často [[Abstraktní-třída|abstraktní]]) třídy,
- s objekty pracujeme přes **ukazatele nebo reference** na bázovou třídu, takže za nimi mohou stát instance různých podtříd,
- voláme metody a **neřešíme skutečný typ** objektu — díky [[Dědičnost|dědičnosti]] a dynamické vazbě se zavolá implementace odpovídající skutečnému typu.

Přínos: existující kód není třeba měnit, když přidáme novou odvozenou třídu (volající nerozlišuje typy).

## Poznámka
- Pro polymorfismus je nutná **dynamická vazba** (virtuální metody) a přístup přes ukazatel/referenci; objekt předaný hodnotou se ořízne a chová se staticky.
- **Šablony** ([[Šablona]]) bývají označovány za *compile-time polymorfismus* (generický kód pro různé typy řešený při překladu).

## Související
- [[Virtuální-metoda]]
- [[Abstraktní-třída]]
- [[Dědičnost]]
- [[Šablona]]
