---
aliases: [šablona, šablony, šabloně, šablonu, šablonou, šablon, šablonám, generické programování, generická třída, generická funkce, template, parametrizace typem]
tags: [definice, kurz/PA2]
---

# Šablona

## Definice
**Šablona** (template) je nástroj C++ pro **parametrizaci** entit (funkcí, tříd, proměnných, `using`) typem nebo hodnotou. Před deklaraci/definici se uvede `template < parametry >`. Parametrem může být **typ** (`typename T` / `class T`), **netypový parametr** (celé číslo, ukazatel, …) nebo jiná šablona.

```cpp
template < typename T > T max(const T& a, const T& b) { return a < b ? b : a; }
template < typename T > struct Array { … };
```

Šablony jsou základem **generického programování** a celé **STL**. Bývají označovány za *compile-time polymorfismus*.

## Instanciace
**Definice šablony negeneruje žádný kód.** Kód vznikne až **instanciací** — použitím šablony s konkrétními parametry. Důsledky:
- Implementace šablon musí být dostupná v místě použití → typicky se píší do **hlavičkových souborů**.
- U šablon tříd se instanciují **jen skutečně použité metody**.
- U funkcí se typové parametry obvykle **odvodí** z argumentů (bez konverzí); lze je i uvést explicitně (`max<double>(…)`).
- Šablony fungují na principu *duck-typingu* — požadavky na `T` jsou implicitní (chybný typ → chyba až při instanciaci).
- **Specializace** (`template<> …`) umožní jinou implementaci pro konkrétní parametry (např. `std::vector<bool>`).

## Související
- [[Polymorfismus]]
- [[Třída]]
