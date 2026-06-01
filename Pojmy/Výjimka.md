---
aliases: [výjimka, výjimky, výjimce, výjimku, výjimkou, výjimek, výjimkám, výjimkami, exception, ošetření chyb, zpracování chyb, try, catch, throw]
tags: [definice, kurz/PA2]
---

# Výjimka

## Definice
**Výjimka** (exception) je speciální chybový signál procházející řetězcem volání od volaného k volajícímu. Slouží k předání zpracování chyby z místa **detekce** (vnořená funkce obvykle neví, jak chybu vyřešit) do místa **rozhodnutí** (některý z volajících). C++ výjimky má, **C nikoli**.

Je to jeden ze tří mechanismů ošetření chyb:
1. **nelokální skok** (`setjmp`/`longjmp`) — přeskočené funkce neuvolní zdroje,
2. **návratová hodnota jako indikátor chyby** — vyžaduje rezervaci návratové hodnoty a kázeň všech funkcí v řetězci,
3. **výjimky** — vnořené funkce jsou o výjimce informovány a uvolní své zdroje **bez dalšího programování**; různé typy odlišují různé chyby a mohou nést data.

## Syntaxe
- **`throw výraz;`** — vyhodí výjimku; **typ** výrazu odlišuje výjimky, hodnota se předá nejbližšímu ovladači.
- **`try { … }`** + **`catch (Typ id) { … }`** (více `catch` za sebou); `catch (...)` zachytí libovolnou výjimku.

```cpp
try { f(-1); }
catch (const char * e) { std::cout << e; }
catch (const std::exception& e) { std::cerr << e.what(); }
```

Reálné programy vyhazují **objekty** (přes konstruktor → dočasný objekt): nesou lidsky čitelný popis i strojová data a lze je rozšiřovat dědičností.

## Vlastnosti
- **Šíření a odvíjení zásobníku:** ovladač zpracuje jen výjimky, které umí; ostatní se šíří dál. Při šíření přes funkce se **volají destruktory lokálních objektů** — ale **nikoli `delete`** dynamicky alokované paměti → nutno použít **RAII** (`std::unique_ptr`, `std::shared_ptr`), případně `catch(...) { uvolni; throw; }` (bare `throw;` přehodí dál).
- **Nezachycená výjimka** projde přes `main` a **ukončí program** (`terminate`); v tom případě destruktory lokálních objektů nemusí být zavolány → nevyhazujte výjimky bez ovladače v řetězci volání.
- **Standardní hierarchie** (`<stdexcept>`): `std::exception` (báze, metoda `what()`) → `std::logic_error` (`std::invalid_argument`, `std::out_of_range`), `std::runtime_error`, … Vlastní výjimky **nemusí** dědit z `std::exception`, ale je to rozumné. Chytáme **referencí** (`const std::exception&`), aby nedošlo k oříznutí.
- **`noexcept`:** funkce/metoda jím deklaruje, že výjimku nevyhazuje ani nepropouští; porušení → okamžité ukončení programu. Umožní efektivnější kód; důležité zejména u **destruktoru a přesouvacího konstruktoru** (např. `std::vector` efektivněji realokuje).

## Související
- [[Třída]]
- [[Mělká-a-hluboká-kopie]]
