---
aliases: [virtuální metoda, virtuální metody, virtuální metodě, virtuální metodu, virtuálních metod, virtuální funkce, dynamická vazba, dynamické vazby, statická vazba, pozdní vazba, virtual, VMT]
tags: [definice, kurz/PA2]
---

# Virtuální metoda

## Definice
**Virtuální metoda** je členská metoda označená klíčovým slovem `virtual`, u níž se volaná implementace určuje **dynamickou vazbou** — až za běhu podle **skutečného typu** objektu, nikoli podle typu ukazatele/reference.

- **Statická vazba** (nevirtuální metody): metoda je vybrána při **překladu** podle deklarovaného typu proměnné/ukazatele vlevo od `.`/`->`. Rychlejší, ale neumožňuje [[Polymorfismus|polymorfismus]].
- **Dynamická vazba** (virtuální metody): metoda je vybrána za **běhu** podle objektu. Mírně pomalejší, ale umožňuje polymorfismus.

```cpp
struct CCounter { virtual void increment() { m_Val++; } };
struct CCounterMod : CCounter { void increment() override { … } };
CCounter* p = new CCounterMod;
p->increment();        // CCounterMod::increment() — dynamická vazba
```

- `virtual` stačí uvést u předka (potomci dědí dynamickou vazbu). `override` (C++11) nechá překladač ověřit, že metoda skutečně překrývá; brání tichému zastínění.
- **Virtuální destruktor** — bázová třída s virtuálními metodami má mít `virtual ~T()`, aby `delete` přes ukazatel na předka zavolal správný destruktor potomka.
- Dynamická vazba funguje jen přes **ukazatel/referenci**; objekt předaný hodnotou se *ořízne* (slicing) a chová se staticky.

## Mechanismus VMT
**VMT** (virtual method table, tabulka virtuálních metod) je překladačem vytvořené pole adres virtuálních metod, jedno pro každou třídu s virtuálními metodami. Každý takový objekt nese **ukazatel na svou VMT** (nastaví konstruktor). Volání = index do VMT (2× dereference) + skok. Pořadí metod ve VMT se v podtřídách zachovává, nové metody se přidávají na konec.

## Související
- [[Polymorfismus]]
- [[Abstraktní-třída]]
- [[Dědičnost]]
