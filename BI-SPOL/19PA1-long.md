---
tags: [otázka, kurz/PA1, otázka/19, todo]
---

# Datové typy, alokace, spojové seznamy, moduly, překlad

> **Otázka SZZ:** Datové typy v programovacích jazycích. Staticky a dynamicky alokované proměnné, spojové seznamy. Modulární programování, procedury a funkce, vstupní a výstupní parametry. Překladač, linker, debugger.

Zdroje: BI-PA1 přednášky `l01-alg`, `l02-var`, `l05-func`, `l07-ptr_struct`, `l08-ptr`, `l11-link`, `l13-adt` (Balík, Trávníček, Vagner, Vogel, FIT ČVUT). Jazyk příkladů: C (překládané kompilátorem C++).

> ⚠️ **Debugger** není v žádných slidech BI-PA1 — tato část je zpracována ze standardní znalosti. Vše ostatní (vč. modulárního programování, preprocesoru a linkeru z přednášky 13 „Moduly, ADT") vychází ze slidů.

---

## 1. Datové typy v programovacích jazycích

### 1.1 Co je datový typ
Procesor pracuje jen s bajty a nezná jejich význam — má jen pravidla, jak bajty zpracovat. Aby šla informace (číslo, znak, …) uložit, musí být **zakódována do jednoho či více bajtů**. **[[Datový-typ]]** je vlastnost dat, která určuje:

1. **množinu možných hodnot**,
2. **množinu dovolených operací**,
3. **kódování** (jak je hodnota uložena, kolik bajtů zabírá).

**Proměnná** je pojmenovaný datový objekt obsahující hodnotu; identifikuje se jménem (jednoznačným identifikátorem). Ve vyšších jazycích má proměnná určitý datový typ, který se po dobu její existence **nemění** (**statická typovost**). Příklad: `int` v C — množina hodnot $[-2^{31}, 2^{31}-1]$, operace aritmetické, relační, přiřazení.

### 1.2 Klasifikace typů
- **Primitivní (vestavěné):** poskytuje je přímo jazyk.
- **Odvozené / programátorem definované:** struktury, pole, ukazatele, `enum`, `union`.

| Skupina | Typy v C |
|---|---|
| Logický | `bool` |
| Znakový | `char` (= malé celé číslo, kóduje znak dle ASCII/UNICODE) |
| Celočíselné | `char`, `short`, `int`, `long`, `long long` (se znaménkem i `unsigned`) |
| Reálné | `float`, `double`, `long double` |
| Bez hodnoty | `void` |
| Odvozené | pole, **struktura** (`struct`), **[[Ukazatel]]**, `enum`, `union` |

**Celočíselné typy (obvyklé velikosti):** `char` 1 B, `short` 2 B, `int`/`long` 4 B, `long long` 8 B. Norma C určuje jen **minimální** rozsahy; skutečné velikosti jsou implementačně závislé (přenositelnost C). Pro garantovanou velikost slouží `stdint.h` (`int16_t`, `uint32_t`, …), pro velikost objektu `size_t`. Od C23 je povinný **dvojkový doplněk**.

**Reálné typy** aproximují $\mathbb{R}$ semilogaritmicky (obvykle IEEE 754):
$$x = (-1)^s \cdot m \cdot b^e, \quad 1 \le m < b,$$
s omezeným rozsahem i přesností. Jen `sizeof(float) ≤ sizeof(double) ≤ sizeof(long double)`. Speciální hodnoty: `±0`, `inf`, `NaN`.

**Strukturované typy** sdružují více hodnot: **pole** (`int a[5]`, indexované od 0, přístup `[]`), **struktura** (`struct`, přístup `.` resp. `->` přes ukazatel).

### 1.3 Konverze
V C/C++ jsou číselné typy navzájem kompatibilní pro přiřazení; při konverzi může dojít ke ztrátě přesnosti (`float`→`int`) nebo dat (do kratšího typu).

---

## 2. Staticky a dynamicky alokované proměnné, spojové seznamy

### 2.1 Model paměti programu
OS dává programu iluzi vlastního adresního prostoru (4 GiB na 32-bit, 16 EiB na 64-bit). Program má úseky:

| Segment | Obsah |
|---|---|
| `.text` (kód) | strojový kód, jen pro čtení a spuštění |
| konstanty | jen pro čtení |
| `.data` | **inicializované** globální/`static` proměnné |
| `.bss` | **neinicializované** globální/`static` proměnné (vynulované) |
| **halda (heap)** | dynamicky alokovaná paměť, roste nahoru |
| **zásobník (stack)** | lokální proměnné a volání funkcí, mělký, roste dolů |

### 2.2 Druhy alokace
- **Statická alokace:** globální (a `static`) proměnné alokuje **kompilátor jedinkrát** v datovém segmentu; existují po celou dobu běhu, mají fixní velikost danou při kompilaci. Globální proměnné jsou vždy inicializovány nulou.
- **Automatická alokace (zásobník):** lokální proměnné funkce se alokují **při volání** na vrcholu zásobníku (režim **LIFO**) a uvolní se při návratu. Umožňuje rekurzi a šetří paměť. Lokální proměnná **není** automaticky inicializovaná. Zásobník je mělký (jednotky MiB) → nepatří na něj velká data; přetečení (nekonečná rekurze) shodí program.
- **Dynamická alokace (halda):** objekt vzniká **za běhu**, nemá jméno, přistupuje se k němu jen přes **[[Ukazatel]]**.

```c
int a = 10;          /* .data  — inicializovaná globální */
int b;               /* .bss   — neinicializovaná globální */
int main () {
  int x;             /* stack  — lokální */
  static int z;      /* .bss   — static lokální */
  int * p = (int *) malloc ( 100 * sizeof(*p) ); /* halda */
  free ( p );        /* uvolnění bloku */
}
```

### 2.3 Dynamická alokace v C
- `void * malloc(size_t size)` — rezervuje souvislý blok `size` bajtů, vrací ukazatel (nutno přetypovat). Obsah **není** definovaný; `calloc` blok vynuluje.
- `free(p)` — uvolní blok; každý blok je třeba uvolnit **právě jednou**.
- **V C není garbage collector.** Z toho plynou chyby:
  - **Memory leak** — ztratíme poslední ukazatel na blok (`p = q;`), blok zůstane nepřístupný a obsazený → vyčerpání paměti.
  - **Double free / dangling pointer** — opakované uvolnění nebo přístup do uvolněné paměti → pád.

**Kdy dynamická alokace:** velikost neznámá při kompilaci; velké pole/struktura (nevejde na zásobník); potřeba vytvořit objekt ve funkci a předat ho volajícímu. Jinak je lepší statická/automatická alokace (menší režie).

### 2.4 Spojové seznamy
**[[Spojový-seznam]]** je lineární spojová struktura: každý **uzel** obsahuje data a ukazatel na následující uzel; poslední ukazuje na `nullptr`.

```c
typedef struct TElement {
  int val;
  struct TElement *next;   // ukazatel na strukturu samu je dovolen
} TELEMENT;

TELEMENT * createElement ( int val, TELEMENT * next ) {
  TELEMENT * n = (TELEMENT *) malloc ( sizeof(*n) );
  n->val = val; n->next = next;
  return n;
}
```

**Operace** (vždy s pomocným ukazatelem, abychom neztratili hlavu):
- **Vložení na začátek** — `st = createElement(x, st);` — $O(1)$.
- **Průchod / hledání** — `while (st) { … st = st->next; }` — $O(n)$.
- **Uvolnění** — pozor zachovat `next` před `free`:
  ```c
  while ( st ) { TELEMENT * p = st->next; free(st); st = p; }
  ```
- **Vložení na konec** — bez ukazatele na poslední prvek $O(n)$ (musíme najít konec); s udržovaným ukazatelem na poslední prvek $O(1)$.

**Varianty:** jednosměrný, **obousměrný** (ukazatel i na předchůdce), **kruhový** (poslední → první), **se zarážkou (sentinel)** — prvek navíc na konci bez dat, který odstraní speciální případ prázdného seznamu a zjednoduší kód (nemění asymptotickou složitost).

**Seznam vs. pole:** seznam roste po prvku bez znalosti celkové velikosti a vkládá v $O(1)$ na známé místo; nemá ale přístup přes index v $O(1)$ a platí režii ukazatelů. Pole se musí dynamicky realokovat při růstu (viz [[Nafukovací-pole]]).

---

## 3. Modulární programování, procedury a funkce, vstupní a výstupní parametry

### 3.1 Modulární programování
Složitější programy se rozdělují do více **zdrojových souborů — modulů**. **Modul** je část programu poskytující určitou funkcionalitu zbytku programu (obvykle skupinu souvisejících úkolů — zpracování vstupu, výpočty s komplexními čísly, GUI). Moduly se chovají jako **černé krabičky** oddělené dobře definovaným **rozhraním (interface)**. Modul má dvě části:
- **specifikace** — seznam zdrojů, které modul poskytuje (datové typy, funkce, proměnné; v C++ třídy);
- **implementace** — vlastní realizace nabízených zdrojů.

Podpora modularity: Pascal — *jednotky* (units), Java — *třídy a balíčky*, **C/C++** — **hlavičkové soubory `.h`** + **implementační soubory `.c`/`.cpp`**.

- **Hlavičkový soubor `.h` (rozhraní):** prototypy funkcí, specifikace datových typů, deklarace `extern` sdílených proměnných. Užívá ho **kompilátor** (ví, které funkce/typy jsou použitelné) i **programátor** (ví, jak modul použít). **Neslouží** pro definice funkcí ani proměnných — definice v hlavičce vede k chybě **linkeru** (vícenásobně definovaný symbol).
- **Implementační soubor `.c`/`.cpp`:** definice funkcí a proměnných; `#include`uje vlastní `.h` (udrží konzistenci deklarací s implementací a načte definice typů).

**Sdílení mezi moduly:** funkce a typy se sdílejí přes `.h`. Sdílení **globálních proměnných** je možné (`extern` deklarace v `.h`, jediná definice + inicializace v jednom `.c`), ale **nedoporučuje se** — opodstatněné je jen pro sdílené konstanty (předpočítané tabulky).

> Přednáška 13 staví moduly na **abstraktních datových typech (ADT)** — typ je dán množinou hodnot a operací **nezávisle na implementaci** (modul pro komplexní čísla, zásobník, frontu). To je princip **information hiding**: rozhraní zůstává stejné, implementaci lze vyměnit.

### 3.2 Procedury a funkce
**Funkce** je podprogram řešící dílčí problém. Definice = **hlavička** + **tělo**:
```
typ jméno ( seznam formálních parametrů ) { tělo }
```
- **Funkce** vrací hodnotu (`return výraz`); je-li návratový typ jiný než `void` a funkce skončí bez `return`, je chování **nedefinované**.
- **Procedura** = funkce s návratovým typem `void` (nevrací hodnotu). Jazyk C samostatný pojem „procedura" nemá, používá `void` funkce.

**Deklarace vs. definice:** *deklarace* (prototyp) = hlavička + `;` — stačí k volání; *definice* dodává tělo (může být v jiném modulu/knihovně, deklarace pak bývá v hlavičkovém souboru). Funkci `foo` lze volat z `bar`, jen je-li její prototyp znám dříve.

### 3.3 Vstupní a výstupní parametry
**Formální parametry** jsou lokální proměnné funkce; při volání se naplní hodnotami **skutečných parametrů** (s případnou konverzí jako při přiřazení). Pořadí parametrů je významné.

- **Vstupní parametry — předání hodnotou (by value):** hodnota se **zkopíruje** do formálního parametru. **V C jsou parametry zásadně vstupní** — změna formálního parametru se **neprojeví** ve volajícím (kopie zpět neexistuje).
- **Výstupní parametry:** C je nemá; **simulují se ukazatelem** — volající předá **adresu** (`&x`) své proměnné, funkce ji **dereferencuje** a zapíše výsledek; po návratu hodnota ve volajícím zůstane. Má-li být výstupní parametr typu `T`, deklaruje se jako `T*`.

```c
void minMax ( int a, int b, int * min, int * max ) {  // min, max jsou výstupní
  if ( a < b ) { *min = a; *max = b; }
  else         { *min = b; *max = a; }
}
// volání:  minMax(a, b, &min, &max);
```
Příkladem výstupního parametru je i `scanf("%d", &x)`. Více hodnot lze vrátit také **zabalením do struktury** (`return struct`). Velkou strukturu jako vstupní parametr je lepší předat **ukazatelem** než kopírovat (výkon). Operátor `->`: `p->name ≡ (*p).name`.

---

## 4. Překladač, linker, debugger

> Slidy `l01` popisují rozdíl interpret/překladač, přednáška `l13` preprocesor a sestavení modulů (linker). **Debugger v žádných slidech není** — doplněn ze standardní znalosti.

### 4.1 Programovací jazyky
Jsou to **formální jazyky** popsané přesnou **gramatikou** (často **BNF — Backus-Naurova forma**); rozlišujeme **syntaxi** (jak se program zapisuje) a **sémantiku** (význam). Vysokoúrovňové jazyky (C, C++, Java, Pascal) jsou srozumitelné člověku, ale **nelze je přímo spustit** — musí být přeloženy do strojového kódu. Imperativní (procedurální) jazyk = sekvence příkazů zpracovávaných shora dolů; program se skládá z **deklarací** a **příkazů**.

### 4.2 Překladač vs. interpret
- **Interpretace:** zdroj se přeloží do interní formy, kterou **interpret za běhu provádí** spolu se vstupními daty.
- **Kompilace:** **překladač (compiler)** přeloží zdrojový kód do **strojového kódu**, který se pak spouští přímo nad vstupními daty.

### 4.3 Preprocesor
**Preprocesor** je **první fáze kompilace** modulu; jeho direktivy začínají `#`. Slouží pro:
- **vkládání hlavičkových souborů** — `#include <stdio.h>` (systémové) / `#include "complex.h"` (vlastní); může být vnořené;
- **makra** — `#define M_PI 3.14159`; makra s parametry `#define MAX(x,y) ((x)>(y)?(x):(y))` (parametry i celou substituci uzavírat do závorek, jinak chybný výsledek); ruší se `#undef`; substituce se neprovádí v řetězcích a komentářích; standardní makra `__DATE__`, `__TIME__`, `__FILE__`;
- **podmíněný překlad** — `#ifdef WIN32 … #else … #endif`; vynechaný text kompilátor vůbec nezpracuje (užitečné pro různé platformy/API a ladicí výstupy).

### 4.4 Překlad modulů a linker
Program z více modulů je třeba zkompilovat a **pospojovat** (link, build task). Typy souborů:

| Přípona | Význam |
|---|---|
| `.c`/`.cpp` | zdrojový soubor — definice funkcí |
| `.h` | hlavičkový soubor — deklarace, datové typy |
| `.o`/`.obj` | **objektový soubor** — strojový kód s **neřešenými referencemi** mezi moduly |
| `.a`/`.lib` | knihovna objektových souborů |
| `.so`/`.dll` | sdílená knihovna |
| `.exe` / bez přípony | **spustitelný soubor** |

Objektový soubor **importuje symboly** (např. volá funkci ze standardní knihovny) a **exportuje symboly** (např. funkci, která je v něm definována). **Linker (sestavovací program, task builder)** spojí objektové soubory a knihovny do spustitelného souboru a přitom **vyřeší reference** mezi nimi; chybějící nebo vícenásobně definovaný symbol hlásí jako chybu (link-time).

Sestavení řídí buď **IDE** (projekt = seznam modulů + volby pro kompilaci a sestavení; zná závislosti pro rekompilaci změněných modulů), nebo utilita **`make`** podle ručně psaného souboru **`Makefile`**.

**Fáze:** preprocesor → kompilátor (každý modul → `.o`, compile-time chyby) → linker (`.o` + knihovny → spustitelný soubor) → běh (run-time; C neprovádí běhové kontroly, např. přístup mimo pole).

### 4.5 Debugger
> Debugger není v žádných slidech BI-PA1 — standardní doplnění.

**Debugger (ladicí program)** umožňuje řízené spouštění programu kvůli hledání chyb:
- **breakpointy** (zastavení na zvoleném řádku),
- **krokování** (step into/over/out),
- **sledování proměnných** (watch) a obsahu paměti, zásobníku volání (call stack),
- inspekci hodnot a vyhodnocování výrazů za běhu.

### 4.6 Specifika jazyka C
C (Ritchie, 1972; normy C89/C99/C11/C23) je vysokoúrovňový jazyk umožňující i nízkoúrovňové operace (ukazatele, adresy), je portabilní a generuje efektivní kód; nevýhodou je, že **veškerá kontrola leží na programátorovi** (žádné běhové kontroly indexů ani platnosti ukazatelů). V BI-PA1 se píše v C, ale překládá kompilátorem C++ (důslednější kontrola), proto se objevují `nullptr`, `bool`.

---

## 5. Co je potřeba na zkoušku znát

### Definice
- Datový typ (množina hodnot + operace + kódování); statická typovost; klasifikace typů v C.
- Statická vs. automatická vs. dynamická alokace; segmenty paměti (`.data`/`.bss`/halda/zásobník).
- Ukazatel, reference `&`, dereference `*`, `nullptr`; `malloc`/`free`.
- Spojový seznam (uzel = data + ukazatel na následníka); varianty (jednosměrný/obousměrný/kruhový/se zarážkou).
- Modul (specifikace + implementace), rozhraní (`.h`) vs. implementace (`.c`/`.cpp`), oddělený překlad, information hiding (ADT).
- Funkce vs. procedura; deklarace (prototyp) vs. definice; formální vs. skutečné parametry.
- Vstupní (by value) vs. výstupní (přes ukazatel) parametry.
- Preprocesor (`#include`, `#define`/makra, podmíněný překlad); překladač; linker (objektové soubory, import/export symbolů, rozlišení referencí); debugger.

### Klíčové vztahy a složitosti
- Spojový seznam: vložení na začátek $O(1)$, na konec $O(n)$ (resp. $O(1)$ s ukazatelem na konec), hledání $O(n)$.
- V C je předání zásadně hodnotou; výstup jen přes ukazatel/strukturu.
- Memory leak vs. double free; proč zásobník nesnese velká data.

### Algoritmy / kód
- Vytvoření uzlu, vložení na začátek, průchod, hledání, korektní uvolnění spojového seznamu.
- Výstupní parametr přes ukazatel (`minMax`, `scanf`).
- Sestavovací pipeline preprocesor → překladač → linker → běh.
