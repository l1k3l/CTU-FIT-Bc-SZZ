---
tags: [otázka, kurz/PA1, otázka/19, todo]
---

# 19 — Datové typy, alokace, seznamy, moduly, překlad (zkrácená verze)

## 1. Datové typy
**[[Datový-typ]]** určuje: množinu **hodnot** + množinu **operací** + **kódování** (počet bajtů). Vyšší jazyky: statická typovost (typ proměnné se nemění).

- **Primitivní:** `bool`, `char`, celočíselné (`short` 2 B, `int`/`long` 4 B, `long long` 8 B; se znaménkem i `unsigned`), reálné (`float`/`double`/`long double`, IEEE 754: $x=(-1)^s m\,b^e$), `void`.
- **Odvozené:** pole, **struktura**, **[[Ukazatel]]**, `enum`, `union`.

Norma C: jen min. rozsahy → `stdint.h` pro pevnou velikost, `size_t` pro velikosti.

## 2. Alokace + spojové seznamy
| Druh | Kde | Kdy | Život |
|---|---|---|---|
| statická | `.data`/`.bss` | kompilace | celý běh (globální/`static`) |
| automatická | zásobník (LIFO) | volání funkce | do návratu (lokální) |
| dynamická | halda | za běhu `malloc` | do `free` |

Zásobník je mělký → velká data na haldu. `malloc`/`free`, **bez GC**. Chyby: **memory leak** (ztráta ukazatele na blok), **double free / dangling** (pád).

**[[Spojový-seznam]]:** uzel = data + ukazatel na následníka; poslední → `nullptr`.
- vložení na začátek $O(1)$, na konec $O(n)$ (resp. $O(1)$ s ukazatelem na konec), hledání/průchod $O(n)$.
- varianty: jednosměrný / obousměrný / kruhový / **se zarážkou** (odstraní speciální případ prázdného seznamu).
- vs. pole: roste po prvku, vkládá $O(1)$ na známé místo; nemá index $O(1)$, režie ukazatelů.

## 3. Moduly, funkce, parametry
- **Modulární programování:** rozhraní `.h` (deklarace) × implementace `.c` (definice); **oddělený překlad** + linker; **information hiding**.
- **Funkce** vrací hodnotu (`return`); **procedura** = `void` funkce. Deklarace (prototyp) × definice (tělo).
- **Parametry:** formální (lokální proměnné) ← skutečné. **V C zásadně vstupní (by value)** — kopie, změna se neprojeví.
- **Výstupní parametr:** přes **ukazatel** — volající dá `&x`, funkce zapíše `*p = …` (např. `scanf("%d",&x)`); nebo vrátit **strukturu**.

## 4. Překladač, linker, debugger
- Jazyky = **formální** (gramatika, **BNF**); syntaxe × sémantika. Vysokoúrovňové nutno přeložit.
- **Interpret:** provádí interní formu za běhu. **Překladač (compiler):** zdroj → strojový kód.
- **Pipeline:** preprocesor → překladač (`.o`, compile-time chyby) → **linker** (spojí `.o`+knihovny, **rozlišení symbolů**, statické/dynamické linkování, link-time chyby) → běh (run-time).
- **Debugger:** breakpointy, krokování, watch proměnných, call stack.

---

## Co odpovědět rychle
- **Typ** = hodnoty + operace + kódování; primitivní vs. odvozené.
- **Alokace:** statická (kompilace, globální) / automatická (zásobník, lokální) / dynamická (halda, `malloc`, bez GC → leak, double free).
- **Spojový seznam:** uzel = data + ukazatel; začátek $O(1)$, konec/hledání $O(n)$.
- **Moduly:** `.h` rozhraní × `.c` implementace, oddělený překlad, linker spojí symboly.
- **C parametry: jen vstupní (kopie); výstup ukazatelem (`&`/`*`).**
- **Pipeline:** preprocesor → compiler (`.o`) → linker (symboly) → běh; debugger = breakpoint/krok/watch.
