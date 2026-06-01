---
tags: [otázka, kurz/PA2, otázka/22, todo]
---

# Objektově orientované programování v C++

> **Otázka SZZ:** Objektově orientovaného programování v C++, zapouzdření, dědičnost, atributy a metody, statické atributy a metody, virtuální metody, polymorfismus, abstraktní třídy, výjimky, šablony, přetěžování operátorů, mělká a hluboká kopie.

Zdroje: BI-PA2 přednášky l02 (třídy), l03 (přetěžování operátorů), l04 (kopírování), l06 (2. polovina — výjimky), l07 (dědičnost a polymorfismus), l08 (abstraktní třídy), l09 (šablony) (Vagner, Vogel, FIT ČVUT).

---

## 1. Objektově orientované programování v C++

OOP je programovací styl: *analyzuj problém a urči participující entity a jejich interakce; entity implementuj jako třídy a objekty; interakce tvoří rozhraní (metody) tříd.* Oproti procedurálnímu stylu jsou **data a funkce sloučeny do objektů**.

**[[Třída]]** je popis datového typu — sdružuje **data** (členské proměnné / atributy) a **operace** (členské funkce / metody) tvořící rozhraní. Z pohledu návrhu je třída abstrakcí entity reálného světa. **Objekt** je **instance** třídy (proměnná daného typu); každý objekt má svou třídu a vlastní kopii instančních atributů, vzniká voláním konstruktoru a zaniká voláním destruktoru. V C++ nelze třídy tvořit za běhu (na rozdíl od jazyků s runtime reflexí).

```cpp
struct Array {
  Array();                 // konstruktor — deklarace končí středníkem
  Array(int x);            // přetížený konstruktor
  ~Array();                // destruktor
  size_t size() const;     // metoda
  size_t size_;            // členská proměnná (atribut)
};
size_t Array::size() const { return size_; }   // definice mimo třídu (bez ;)
```

- `class` i `struct` deklarují třídu; liší se jen **implicitní viditelností** (`class` → `private`, `struct` → `public`).
- Členy se zvenčí volají **tečkovou notací** (`x.size()`), uvnitř přímo nebo přes `this` (ukazatel na aktuální objekt) při kolizi jmen.

---

## 2. Zapouzdření

![[Zapouzdření#Definice]]

**Smysl zapouzdření** není mechanické skrytí dat (gettery/settery ke každé proměnné jsou anti-vzor), nýbrž **jasné, kontrolovatelné a vysokoúrovňové veřejné rozhraní**. To umožňuje nezávisle měnit implementaci nebo třídu zcela nahradit, dokud je dodrženo rozhraní; překladač navíc hlídá, že se neveřejná část nepoužívá nepovoleně. Rozhraní má dovolit potřebné operace, **ale ne více**.

---

## 3. Atributy a metody

- **Instanční atributy** (členské proměnné): každý objekt má vlastní; deklarují se bez klíčového slova.
- **Metody (členské funkce):** instanční metoda má implicitní `this` a přístup k atributům i k jiným metodám.
- **`const` metoda** (`size_t size() const;`) nesmí modifikovat atributy a lze ji volat i na `const` objektu. **Nekonstantní metodu na `const` objektu volat nelze.** Časté jsou **const/nekonstantní páry** (nekonstantní vrací referenci pro zápis, konstantní vrací hodnotu/`const` referenci):

```cpp
int&  at(size_t i);          // pro nekonstantní objekt
int   at(size_t i) const;    // pro const objekt (překladač preferuje nekonstantní)
```

- **Konstruktory a destruktory.** Konstruktor inicializuje atributy v **inicializačním listu** (`: a_(x), b_(y)`); není vhodné atribut nejprve implicitně inicializovat a pak v těle přepsat. Důležitá pravidla:
  - atributy se inicializují **v pořadí deklarace** ve třídě (ne v pořadí v inicializačním listu),
  - destruují se po těle destruktoru v **opačném** pořadí.
  - Lze delegovat (`Array(int v) : Array() { … }`) i volat konstruktor předka.
- Dynamicky se objekty alokují `new` (volá konstruktor) a ruší `delete` (volá destruktor); `malloc/free` nelze (nevolají konstruktor/destruktor).
- **Automaticky generované metody:** překladač generuje implicitní konstruktor (není-li žádný), destruktor, kopírovací/přesouvací konstruktor a `operator=`. Vynutit `= default`, zakázat `= delete`.

---

## 4. Statické atributy a metody

- **Statický (třídní) atribut** (`static`) je **sdílen všemi instancemi** třídy. Musí mít rezervovanou paměť — definici mimo třídu, nebo `inline` (od C++17). Přístup se řídí běžnými pravidly zapouzdření.
- **Statická (třídní) metoda** (`static`) je podobná obyčejné funkci: **nemá implicitní instanci, tedy ani `this`**, ani přístup k instančním atributům; má přístup ke statickým atributům a může volat jiné statické metody. Volá se kvalifikovaně `T::metoda()`.

```cpp
class T {
  int a;                       // instanční
  static inline int cnt = 0;   // statická — sdílená, definovaná přes inline
public:
  T(int x) { a = x; cnt++; }
  ~T() { cnt--; }
  static int count() { return cnt; }   // statická metoda (bez this)
};
// použití: T::count();
```
Typické použití: počítadlo živých instancí, sdílené konstanty, tovární metody.

---

## 5. Přetěžování operátorů

![[Přetěžování-operátorů#Definice]]

**Member vs. volná funkce.** Operátor jako **metoda** má levý operand `*this` a pravý jako parametr; jako **volná funkce** má oba operandy parametry. Klíčový rozdíl: u **metody nedochází ke konverzi levého operandu**, takže např. `2 - a` (kde `2` je `int` konvertovatelný na typ `a`) funguje jen je-li operátor **volná funkce**. Pro přístup k privátním členům bývá volná funkce `friend`.

```cpp
class CRat {
  int num_, den_;
public:
  CRat(int n = 0, int d = 1);                              // i konverzní konstruktor int→CRat
  CRat operator - (const CRat& b) const;                   // metoda: a - b
  friend CRat operator + (const CRat& a, const CRat& b);   // volná friend funkce
  friend std::ostream& operator << (std::ostream& os, const CRat& x);
};
```

**Pravidla a meze:**
- Přetěžovat lze jen **existující** operátory; **nelze měnit aritu, prioritu ani asociativitu** ani předefinovat sémantiku pro vestavěné typy.
- **Nelze přetížit:** `::`, `.`, `.*`, `?:`.
- **Jen jako metodu:** `=`, `()`, `[]`, `->`.
- **`operator<<` / `operator>>`** (streamy) musí být **volné funkce**; levý argument `std::ostream&`/`std::istream&`, návratový typ stejný (kvůli **řetězení** `cout << a << b`); bývají `friend`.
- **`operator[]`** jen metoda, typicky const/nekonstantní pár.
- Kombinované operátory mají dodržet `x @= y` ≡ `x = x @ y`; lze je vzájemně delegovat. Prefixní `++` vrací referenci, postfixní `++(int)` vrací hodnotu.
- Od C++20 lze generovat `operator<=>` (spaceship, lexikograficky dle pořadí atributů) a `operator==` přes `= default`.

---

## 6. Mělká a hluboká kopie

![[Mělká-a-hluboká-kopie#Definice]]

**Problém.** Implicitně generované kopírování kopíruje atributy člen po členu a ukazatele **bitově** → dvě instance sdílí tentýž blok (mělká kopie). To vede k **dvojímu uvolnění** a **úniku paměti** (přepsaný starý blok). V C++ se očekává, že kopírování provede **hlubokou** kopii — vlastněný blok je třeba zkopírovat.

```cpp
Array::Array(const Array& o) : size_(o.size_), data_(new int[o.size_]) {  // kopírovací konstruktor
  for (size_t i = 0; i < size_; i++) data_[i] = o.data_[i];
}
Array& Array::operator = (const Array& o) {        // kopírovací operátor přiřazení
  if (&o == this) return *this;                    // test sebepřiřazení (jinak by delete zničil zdroj)
  delete[] data_;
  size_ = o.size_; data_ = new int[size_];
  for (size_t i = 0; i < size_; i++) data_[i] = o.data_[i];
  return *this;
}
```

- **Test sebepřiřazení** (`&o == this`, porovnání adres) je v `operator=` nutný, v kopírovacím konstruktoru ne (nově vznikající objekt nemůže být zdrojem).
- `Array c = a;` volá **kopírovací konstruktor**, ne `operator=`.
- **Pravidlo tří:** definuje-li třída jedno z {kopírovací konstruktor, kopírovací `operator=`, destruktor}, má definovat všechny tři.
- **Pravidlo pěti:** + přesouvací konstruktor a `operator=` (rvalue reference `&&`, „ukradnou" zdroj a původní objekt nechají v konzistentním prázdném stavu). Pozn.: proměnná typu rvalue reference **je lvalue**, dál se musí předat přes `std::move`.
- **Pravidlo nuly:** nejlépe prostředky nevlastnit přímo (použít `std::unique_ptr`, `std::vector`) a vše nechat na překladači.
- Idiom **copy-and-swap:** `operator=` bere parametr **hodnotou** a jen prohodí (`swap`) obsah — řeší kopii i sebepřiřazení; pozor na `using std::swap;` (ADL), nikdy `std::swap(*this,o)` uvnitř (nekonečná rekurze).
- **Mělká kopie s počítáním referencí** (`std::shared_ptr`) + **copy-on-write** umožní rychlé sdílení, jež se navenek chová jako hluboká kopie (kopíruje se až při zápisu).

---

## 7. Dědičnost

![[Dědičnost#Definice]]

```cpp
class CCounterMod : public CCounter {       // : odděluje třídu od seznamu předků
  int m_Modulus;
public:
  CCounterMod(int v, int m) : CCounter(v % m) { m_Modulus = m; }  // konstruktor předka
  void increment() { CCounter::increment(); m_Val %= m_Modulus; } // metoda předka
};
```

- **`protected`** člen je přístupný v třídě a v jejích potomcích.
- **Módy dědičnosti:** `public` zachová viditelnosti zděděných členů (běžné, povoluje polymorfismus); `private` (default u `class`) dědí implementaci, ale **potlačí polymorfismus**.
- **Přiřazování:** instanci potomka lze přiřadit/uložit do předka, **opačně ne**. Paměťový obraz potomka = obraz předka + nové atributy.
- **C++ umožňuje vícenásobnou dědičnost** (struktura VMT se pak komplikuje).

---

## 8. Virtuální metody (statická vs. dynamická vazba)

![[Virtuální-metoda#Definice]]

- **Statická vazba** (nevirtuální metoda): metoda vybrána **při překladu** dle deklarovaného typu proměnné/ukazatele vlevo od `.`/`->`. Rychlejší, ale neumožňuje polymorfismus a vyžaduje, aby volající rozlišoval typy.
- **Dynamická vazba** (`virtual`): metoda vybrána **za běhu** dle skutečného typu objektu. Mírně pomalejší, ale: volající nemusí rozlišovat typy a **přidání nové odvozené třídy nevyžaduje úpravu existujícího kódu**.
- `virtual` stačí uvést u předka; `override` (C++11) nechá překladač ověřit překrytí (chrání před tichým **zastíněním** při nesouhlasu signatur/`const`).
- **Oříznutí (slicing):** předání objektu **hodnotou** do parametru typu předka vytvoří instanci předka → dynamická vazba nefunguje. Funguje jen přes **ukazatel/referenci**. (Java tento problém nemá — vždy předává referencí.)
- **Virtuální destruktor:** bázová třída s virtuálními metodami má mít `virtual ~T()`, aby `delete` přes ukazatel na předka zavolal destruktor potomka.

**Mechanismus VMT (tabulka virtuálních metod):** překladač pro každou třídu s virtuálními metodami vytvoří pole adres těchto metod; každý takový objekt nese **ukazatel na svou VMT** (nastaví konstruktor). Volání virtuální metody = index do VMT (**2× dereference**) + skok. Pořadí metod ve VMT se v podtřídách zachovává; nepřepsané metody přebírají adresu z předka, nové se přidají na konec.

---

## 9. Polymorfismus

![[Polymorfismus#Definice]]

Polymorfismus realizujeme přes **ukazatele/reference na bázovou třídu** + **virtuální metody**: voláme jednotné rozhraní a o výběr implementace dle skutečného typu se postará dynamická vazba.

```cpp
void tisk(const CElem& e) { std::cout << e; }   // funguje pro každou podtřídu CElem
```

Šablony bývají označovány za **compile-time polymorfismus** (generický kód řešený při překladu). Pro **downcast** s kontrolou typu za běhu slouží `dynamic_cast` (při neshodě vrací `nullptr`) a `typeid` (RTTI) — používat střídmě, jejich nadužívání ruší výhody polymorfismu.

---

## 10. Abstraktní třídy

![[Abstraktní-třída#Definice]]

```cpp
struct CCounter {                       // abstraktní třída — nelze instanciovat
  virtual ~CCounter() {}
  virtual void increment() = 0;         // čistě virtuální (abstraktní) metoda
  virtual std::string get() const = 0;
};
class CCounterInt : public CCounter {   // konkrétní podtřída implementuje rozhraní
  int m_Val = 0;
public:
  void increment() override { m_Val++; }
  std::string get() const override { return std::to_string(m_Val); }
};
```

Abstraktní třída dává **společné rozhraní** podtřídám — základ **heterogenních (polymorfních) datových struktur** (kontejner ukazatelů na bázovou třídu, prvky různých podtypů). Polymorfní hluboké kopírování se řeší virtuální metodou `clone()` (kovariantní návratový typ `CInt* clone() const override { return new CInt(*this); }`).

---

## 11. Šablony

![[Šablona#Definice]]

```cpp
template < typename T > T max(const T& a, const T& b) { return a < b ? b : a; }
template < typename T > struct Array { … };
```

- **Instanciace:** definice šablony **negeneruje kód**; vznikne až použitím s konkrétními parametry. Proto se implementace šablon píší do **hlavičkových souborů**.
- U **funkcí** se typové parametry obvykle **odvodí** z argumentů (bez konverzí); lze uvést explicitně (`max<double>(…)`). Při shodě s obyčejnou funkcí má **obyčejná funkce přednost**.
- U **tříd** se instanciují **jen použité metody** (lze tak držet `std::vector<unique_ptr<…>>` a selže až případné kopírování). Od C++17 **CTAD** odvodí parametry třídy (`std::vector v = {1,2,3};`).
- Parametr může být i **netypový** (číslo) nebo **parameter pack** (variadické šablony). **Specializace** (`template<> …`) mění implementaci pro konkrétní parametry (např. `std::vector<bool>`). Šablony jsou základ **STL**.

---

## 12. Výjimky

![[Výjimka#Definice]]

```cpp
try {
  CRat r(1, 0);                                  // konstruktor: if (den==0) throw std::invalid_argument(…)
} catch (const std::invalid_argument& e) {
  std::cerr << e.what();
} catch (...) { /* záchytný ovladač */ }
```

- **`throw výraz;`** — typ výrazu odlišuje výjimky, hodnota se předá nejbližšímu ovladači. Reálné programy vyhazují **objekty** (nesou popis i data, lze je rozšiřovat dědičností).
- **Šíření a odvíjení zásobníku:** ovladač zpracuje jen výjimky, které umí, ostatní se šíří dál. Při šíření přes funkce se **volají destruktory lokálních objektů**, ale **nikoli `delete`** dynamicky alokované paměti → **únik**. Řešení: **RAII** (`std::unique_ptr`/`std::shared_ptr`), případně `catch(...) { uvolni; throw; }` (bare `throw;` přehodí dál).
- **Nezachycená výjimka** projde přes `main` a **ukončí program** (`terminate`); pak nemusí být zavolány ani destruktory lokálních objektů → nevyhazujte výjimky, které v řetězci nemají ovladač.
- **Standardní hierarchie** (`<stdexcept>`): `std::exception` (báze, `what()`) → `std::logic_error` (`std::invalid_argument`, `std::out_of_range`), `std::runtime_error`, …; chytá se referencí. Vlastní výjimky nemusí dědit z `std::exception`, ale je to rozumné.
- **`noexcept`:** funkce jím slibuje, že výjimku nevyhodí ani nepropustí (porušení → `terminate`); důležité u **destruktoru a přesouvacího konstruktoru** (umožní efektivnější realokaci `std::vector`).

> Pozn.: BI-PA2 zařazuje výjimky do 2. poloviny přednášky l06 (po BFS/DFS), jako třetí mechanismus ošetření chyb vedle nelokálního skoku (`setjmp/longjmp`) a návratové hodnoty.

---

## 13. Co je potřeba na zkoušku znát

### Definice
Třída vs. objekt (instance); zapouzdření a tři modifikátory (`public/protected/private`); instanční vs. statický atribut/metoda; konstruktor/destruktor a inicializační list; přetížení operátoru; mělká vs. hluboká kopie; dědičnost (předek/potomek, módy); statická vs. dynamická vazba; virtuální / čistě virtuální metoda; polymorfismus; abstraktní třída; šablona a instanciace; výjimka.

### Mechanismy a pravidla
- VMT a dynamická vazba (2× dereference), virtuální destruktor, slicing.
- Pravidlo tří / pěti / nuly; test sebepřiřazení; `Array c = a;` je kopírovací konstruktor; copy-and-swap.
- `operator<<` jako friend volná funkce; metoda nekonvertuje levý operand (`2 - a` → volná funkce); co nelze přetížit (`:: . .* ?:`) a co jen jako metodu (`= () [] ->`).
- Šablony žijí v hlavičkách, instanciují se jen použité části, odvození bez konverzí.
- Výjimky: odvíjení zásobníku volá destruktory lokálních objektů, ne `delete` → RAII; `<stdexcept>`, `noexcept`.

### Kód, který umět napsat
Deklarace třídy s konstruktorem/destruktorem/`const` metodou; kopírovací konstruktor + `operator=` s hlubokou kopií a testem sebepřiřazení; abstraktní třída + override v podtřídě; jednoduchá šablona funkce a třídy; `try`/`catch` s `throw` objektu.

## Související pojmy
[[Třída]] · [[Zapouzdření]] · [[Dědičnost]] · [[Polymorfismus]] · [[Virtuální-metoda]] · [[Abstraktní-třída]] · [[Šablona]] · [[Výjimka]] · [[Přetěžování-operátorů]] · [[Mělká-a-hluboká-kopie]]
