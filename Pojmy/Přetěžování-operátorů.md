---
aliases: [přetěžování operátorů, přetížení operátoru, přetížený operátor, přetížit operátor, přetěžování operátoru, operator overloading]
tags: [definice, kurz/PA2]
---

# Přetěžování operátorů

## Definice
**Přetížení operátoru** dává existujícímu operátoru nový význam pro nové (uživatelské) typy. Přetížený operátor není nic jiného než **zkrácený zápis volání funkce/metody** — `a + b` se přeloží jako `operator+(a, b)` (funkce) nebo `a.operator+(b)` (metoda).

```cpp
CRat operator + (const CRat& a, const CRat& b);   // volná funkce: oba operandy
CRat CRat::operator + (const CRat& b) const;        // metoda: levý operand je *this
```

## Pravidla a meze
- Přetěžovat lze jen **existující** operátory; **nelze měnit aritu, prioritu ani asociativitu** a nelze předefinovat sémantiku pro vestavěné typy.
- **Nelze přetížit:** `::`, `.`, `.*`, `?:`.
- **Jen jako metodu:** `=`, `()`, `[]`, `->`.
- **Forma:** metoda nedělá konverzi levého operandu — pro symetrii (např. `2 - a`) je nutná **volná funkce**; pro přístup k privátním členům bývá `friend`.
- `operator<<` / `operator>>` (streamy) musí být volné funkce; levý argument `std::ostream&`/`std::istream&`, návratový typ stejný (kvůli řetězení).
- Doporučuje se dodržet očekávanou sémantiku (`x @= y` ≡ `x = x @ y`); od C++20 lze generovat `operator<=>` a `operator==` přes `= default`.

## Související
- [[Třída]]
- [[Mělká-a-hluboká-kopie]]
