---
aliases: [abstraktní třída, abstraktní třídy, abstraktní třídě, abstraktní třídu, abstraktních tříd, abstraktní metoda, abstraktní metody, čistě virtuální metoda, čistě virtuální, rozhraní, interface, abstract class]
tags: [definice, kurz/PA2]
---

# Abstraktní třída

## Definice
**Abstraktní (čistě virtuální) metoda** je [[Virtuální-metoda|virtuální metoda]], která je deklarovaná, ale nemá implementaci — místo těla má `= 0`:

```cpp
struct CCounter {
  virtual ~CCounter() {}
  virtual void increment() = 0;   // čistě virtuální (abstraktní) metoda
  virtual std::string get() const = 0;
};
```

**Abstraktní třída** je třída s **alespoň jednou** abstraktní metodou. Vlastnosti:
- **Nemá instance** (nelze ji vytvořit `new`/lokálně), lze však deklarovat **ukazatele a reference** na ni.
- Abstraktní metody definují **rozhraní (interface)**, které musí každá neabstraktní podtřída implementovat (`override`).

## Použití
- Společné rozhraní pro skupinu podtříd → základ pro [[Polymorfismus|polymorfismus]] a **heterogenní (polymorfní) datové struktury** (kontejner ukazatelů na bázovou třídu, prvky různých podtypů se společným rozhraním).
- Polymorfní hluboké kopírování přes virtuální `clone()` (kovariantní návratový typ).

## Související
- [[Virtuální-metoda]]
- [[Polymorfismus]]
- [[Dědičnost]]
