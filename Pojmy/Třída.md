---
aliases: [třída, třídy, třídě, třídu, třídou, tříd, třídám, třídách, objekt, objektu, objektem, objekty, objektů, objektům, instance, instancí, instanci, class, konstruktor, destruktor]
tags: [definice, kurz/PA2]
---

# Třída a objekt

## Definice
**Třída** (class) je popis datového typu — uživatelsky definovaný typ, který sdružuje **data** (členské proměnné / atributy / položky) a **operace** (členské funkce / metody) tvořící jeho rozhraní. Z pohledu návrhu je třída abstrakcí entity reálného světa.

**Objekt** je **instance** třídy — proměnná daného typu. Každý objekt má svou třídu a vlastní kopii instančních atributů; vzniká voláním **konstruktoru**, zaniká voláním **destruktoru**.

```cpp
struct Array {           // class i struct deklarují třídu
  Array();               // konstruktor (deklarace končí ;)
  ~Array();              // destruktor
  size_t size() const;   // metoda; definice mimo třídu: size_t Array::size() const {…}
  size_t size_;          // členská proměnná (atribut)
};
```

- **`class` vs `struct`** se liší jen implicitní viditelností: `class` → `private`, `struct` → `public`.
- Přístup k členům zvenčí přes tečkovou notaci (`x.size()`); uvnitř přímo, případně přes `this` (ukazatel na aktuální objekt) při kolizi jmen.

## Atributy a metody
- **Instanční** atribut má každý objekt vlastní; **statický** (`static`) je sdílen všemi instancemi třídy (musí mít definici mimo třídu nebo `inline`).
- **Instanční metoda** má `this` a přístup k instančním i statickým členům; **statická metoda** (`static`) `this` nemá — chová se jako obyčejná funkce s přístupem ke statickým členům (volá se `T::metoda()`).
- **`const` metoda** nesmí modifikovat atributy a lze ji volat i na `const` objektu; nekonstantní metodu na `const` objektu volat nelze. Časté jsou `const`/nekonstantní páry (`int at(size_t) const` vs `int& at(size_t)`).
- **Konstruktor** inicializuje atributy v **inicializačním listu** (`: a_(x), b_(y)`); atributy se inicializují **v pořadí deklarace** a destruují v opačném pořadí. Překladač generuje implicitní konstruktor, destruktor, kopírovací/přesouvací konstruktor a `operator=` (lze vynutit `= default`, zakázat `= delete`).

## Související
- [[Zapouzdření]]
- [[Dědičnost]]
- [[Mělká-a-hluboká-kopie]]
- [[Datový-typ]]
