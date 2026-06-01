---
aliases: [dědičnost, dědičnosti, dědičností, dědění, dědit, zdědit, zděděný, předek, předka, potomek, potomka, bázová třída, odvozená třída, podtřída, nadtřída, inheritance]
tags: [definice, kurz/PA2]
---

# Dědičnost

## Definice
**Dědičnost** (inheritance) je odvození nové třídy (**potomek / odvozená třída / podtřída**) z existující třídy (**předek / bázová třída / nadtřída**). Vyjadřuje vztah *„je-to"* (is-a).

Potomek:
- **zdědí všechny atributy** předka (nelze je odebrat ani změnit jejich typ); může přidat nové,
- **zdědí všechny metody**; existující může **přepsat** (override — stejná signatura, jiná implementace) a může přidat nové.

```cpp
class CCounterMod : public CCounter {
  int m_Modulus;
public:
  CCounterMod(int v, int m) : CCounter(v % m) { m_Modulus = m; }  // volání konstruktoru předka
  void increment() { CCounter::increment(); m_Val %= m_Modulus; } // volání metody předka
};
```

## Módy dědičnosti
- **`public`** — zděděné členy si zachovají svou viditelnost (běžný případ, povoluje [[Polymorfismus]]).
- **`private`** (default u `class`) — zděděné členy nejsou mimo potomka viditelné; dědí se implementace, ale **potlačí se polymorfismus**.
- Default: `class B : A` ≡ `private`, `struct B : A` ≡ `public`.

## Přiřazování a paměťový obraz
- Instanci potomka lze přiřadit/uložit do předka, **opačně ne**. Předání potomka **hodnotou** do parametru typu předka způsobí *oříznutí* (object slicing) — viz [[Virtuální-metoda]].
- Paměťový obraz potomka = obraz předka + nové atributy.

## Související
- [[Třída]]
- [[Polymorfismus]]
- [[Virtuální-metoda]]
- [[Abstraktní-třída]]
