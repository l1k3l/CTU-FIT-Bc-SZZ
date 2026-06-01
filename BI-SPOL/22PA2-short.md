---
tags: [otázka, kurz/PA2, otázka/22, todo]
---

# 22 — OOP v C++ (zkrácená verze)

## 1. Třída a objekt
- **[[Třída]]** = popis datového typu: data (atributy) + operace (metody). **Objekt** = instance třídy.
- `class` vs `struct`: jen default viditelnost (`private` vs `public`).
- Konstruktor (volá se při vzniku, `new`), destruktor (`~T`, při zániku, `delete`). Inicializační list `: a_(x)`; atributy se inicializují **v pořadí deklarace**, ruší v opačném.

## 2. [[Zapouzdření]]
- `public` (komukoli) / `protected` (třída + potomci) / `private` (jen třída).
- Cíl není skrýt data, ale dát **stabilní vysokoúrovňové rozhraní** → lze měnit implementaci.

## 3. Atributy a metody
- Instanční metoda má `this`. **`const` metoda** nemodifikuje atributy; jen ji lze volat na `const` objektu. const/nekonstantní pár (`int& at(i)` / `int at(i) const`).

## 4. Statické atributy a metody (`static`)
- **Statický atribut** = sdílený všemi instancemi (definice mimo třídu / `inline`).
- **Statická metoda** = bez `this`, bez instančních atributů; volá se `T::f()`.

## 5. [[Přetěžování-operátorů]]
- Operátor = zkratka pro funkci/metodu: `a+b` → `operator+(a,b)`. Nemění aritu/prioritu.
- **Nelze:** `:: . .* ?:`. **Jen metoda:** `= () [] ->`.
- Metoda nekonvertuje levý operand → `2 - a` vyžaduje **volnou funkci**. `operator<<` = volná `friend` funkce, vrací `ostream&` (řetězení).

## 6. [[Mělká-a-hluboká-kopie]]
- **Mělká** = kopíruje ukazatele (sdílení) → double free / leak. **Hluboká** = kopíruje i odkazovaná data (nezávislá). Default kopie je mělká.
- **Pravidlo tří:** kop. konstruktor + kop. `operator=` + destruktor (vše, nebo nic). **Pravidlo pěti** (+ move `&&`), **pravidlo nuly** (vlastnit přes `unique_ptr`/`vector`).
- `operator=` má **test sebepřiřazení** `if (&o==this) return *this;`. `Array c = a;` = kopírovací konstruktor.

```cpp
Array(const Array& o): n_(o.n_), d_(new int[o.n_]) { …kopíruj… }
Array& operator=(const Array& o){ if(&o==this)return *this; delete[] d_; …; return *this; }
```

## 7. [[Dědičnost]]
- Potomek (odvozená) dědí z předka (bázová): zdědí atributy + metody, může přidat/přepsat (override).
- `: public Base` (zachová viditelnost), `private` (potlačí polymorfismus). `protected` = třída + potomci.
- Potomka lze přiřadit předkovi, **ne naopak**.

## 8. [[Virtuální-metoda|Virtuální metody]] (vazba)
- **Statická vazba** (default): dle typu proměnné, při překladu. **Dynamická vazba** (`virtual`): dle skutečného typu, za běhu → nutná pro polymorfismus.
- Funguje jen přes **ukazatel/referenci** (hodnotou → **oříznutí/slicing**). `override` hlídá překrytí. **Virtuální destruktor** u báze.
- **VMT** = tabulka adres virt. metod; objekt má ukazatel na VMT; volání = 2× dereference.

## 9. [[Polymorfismus]]
- Práce s objekty přes ukazatel/referenci na bázi + virtuální metody; voláme rozhraní, neřešíme typ. Přidání podtřídy nemění volající kód.
- Šablony = compile-time polymorfismus. `dynamic_cast` (neshoda → `nullptr`), `typeid` (RTTI) — střídmě.

## 10. [[Abstraktní-třída|Abstraktní třídy]]
- **Čistě virtuální metoda** = `virtual … = 0;`. **Abstraktní třída** má aspoň jednu → **nelze instanciovat**, lze mít ukazatel/referenci.
- Definuje **rozhraní (interface)**; podtřídy ho implementují. Základ heterogenních struktur, virtuální `clone()`.

## 11. [[Šablona|Šablony]]
- `template<typename T>` parametrizuje funkci/třídu typem (i netypovým parametrem). Základ STL, „compile-time polymorfismus".
- **Definice negeneruje kód** → instanciace až při použití → píší se do **hlaviček**. U tříd se instanciují jen použité metody. Specializace `template<>`.

## 12. [[Výjimka|Výjimky]]
- `throw výraz;` (typ rozlišuje), `try{}` `catch(T&){}` … `catch(...)`. Šíří se k volajícímu, dokud ji někdo nechytí; nezachycená → `terminate`.
- Odvíjení zásobníku **volá destruktory lokálních objektů**, ale **ne `delete`** dynamiky → **RAII** (`unique_ptr`). `<stdexcept>`: `std::exception` (báze, `what()`), `logic_error`, `out_of_range`, `runtime_error`. `noexcept` (dtor, move).

---

## Co odpovědět rychle
- **Hluboká vs mělká kopie** → pravidlo tří, test sebepřiřazení, copy-and-swap.
- **Polymorfismus** = ukazatel/reference na bázi + `virtual` + dynamická vazba (VMT, 2× dereference); hodnotou se objekt ořízne.
- **Abstraktní třída** = aspoň jedna `=0` metoda, nelze instanciovat = rozhraní.
- **Šablony** žijí v hlavičkách, instanciují se až použitím.
- **Výjimky**: unwinding volá destruktory, ne delete → RAII.
