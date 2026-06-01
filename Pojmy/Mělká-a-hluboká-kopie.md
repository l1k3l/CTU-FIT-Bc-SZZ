---
aliases: [mělká kopie, mělké kopie, mělkou kopii, hluboká kopie, hluboké kopie, hlubokou kopii, mělká a hluboká kopie, kopírovací konstruktor, operátor přiřazení, pravidlo tří, pravidlo pěti, rule of three, shallow copy, deep copy]
tags: [definice, kurz/PA2]
---

# Mělká a hluboká kopie

## Definice
Při kopírování objektu, který vlastní odkazované prostředky (např. dynamicky alokovanou paměť přes [[Ukazatel|ukazatel]]):
- **Mělká kopie** (shallow) zkopíruje jen objekt samotný; odkazy (ukazatele) se **sdílí**. Rychlá, ale kopie nejsou nezávislé → riziko **dvojího uvolnění** a **úniku paměti**.
- **Hluboká kopie** (deep) zkopíruje i **odkazované objekty** → kopie je zcela **nezávislá**. Dražší, ale korektní.

Implicitně generované kopírování v C++ je **mělké** (kopíruje atributy člen po členu, ukazatele bitově). U tříd vlastnících prostředky je proto třeba kopírování implementovat ručně (hluboce).

```cpp
Array::Array(const Array& o) : size_(o.size_), data_(new int[o.size_]) {  // kopírovací konstruktor
  for (size_t i = 0; i < size_; i++) data_[i] = o.data_[i];
}
Array& Array::operator = (const Array& o) {        // kopírovací operátor přiřazení
  if (&o == this) return *this;                    // test sebepřiřazení
  delete[] data_;
  size_ = o.size_; data_ = new int[size_];
  for (size_t i = 0; i < size_; i++) data_[i] = o.data_[i];
  return *this;
}
```

## Pravidlo tří / pěti / nuly
- **Pravidlo tří:** definuje-li třída jedno z trojice **kopírovací konstruktor, kopírovací `operator=`, destruktor**, má definovat všechny tři.
- **Pravidlo pěti:** + přesouvací konstruktor a přesouvací `operator=` (rvalue reference `&&`, „ukradnou" prostředek a zdroj nechají v konzistentním prázdném stavu).
- **Pravidlo nuly:** nejlépe nevlastnit prostředky přímo (použít `std::unique_ptr`/`std::vector`/…) a kopírování/přesun nechat na překladači.
- `Array c = a;` je volání **kopírovacího konstruktoru**, ne `operator=`. Idiom **copy-and-swap** implementuje přiřazení přes parametr braný hodnotou a `swap`.

## Související
- [[Ukazatel]]
- [[Přetěžování-operátorů]]
- [[Třída]]
