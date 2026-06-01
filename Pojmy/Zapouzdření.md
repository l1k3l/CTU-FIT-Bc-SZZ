---
aliases: [zapouzdření, zapouzdřením, zapouzdřit, zapouzdřený, viditelnost, přístupová práva, encapsulation]
tags: [definice, kurz/PA2]
---

# Zapouzdření

## Definice
**Zapouzdření** (encapsulation) je princip OOP, kdy třída řídí přístup ke svým členům pomocí **přístupových modifikátorů**:
- **`public`** — člen je přístupný komukoli,
- **`protected`** — člen je přístupný v třídě samé a v jejích **podtřídách** (viz [[Dědičnost]]),
- **`private`** — člen je přístupný jen v třídě samé.

`class` má implicitně `private`, `struct` implicitně `public`.

## Smysl
Cílem zapouzdření **není** samo o sobě skrytí dat (mechanické gettery/settery ke každé proměnné jsou anti-vzor), nýbrž **jasné, kontrolovatelné a dostatečně vysokoúrovňové veřejné rozhraní**. To umožňuje:
- nezávisle měnit implementaci či třídu zcela nahradit, dokud je dodrženo rozhraní,
- nechat překladač kontrolovat, že se neveřejná část nepoužívá nepovoleně.

Rozhraní má dovolit potřebné operace, **ale ne více** (skrýt implementační detaily).

## Související
- [[Třída]]
- [[Dědičnost]]
