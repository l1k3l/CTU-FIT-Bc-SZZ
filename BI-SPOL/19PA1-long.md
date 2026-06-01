---
tags: [otázka, kurz/PA1, otázka/19, todo]
---

# Datové typy, alokace, spojové seznamy, moduly, překlad

> **Otázka SZZ:** Datové typy v programovacích jazycích. Staticky a dynamicky alokované proměnné, spojové seznamy. Modulární programování, procedury a funkce, vstupní a výstupní parametry. Překladač, linker, debugger.

Zdroje: BI-PA1 přednášky `l01-alg`, `l02-var`, `l05-func`, `l07-ptr_struct`, `l08-ptr`, `l11-link` (Balík, Trávníček, Vagner, Vogel, FIT ČVUT). Jazyk příkladů: C (překládané kompilátorem C++).

> ⚠️ **Modulární programování, linker a debugger** nejsou v dostupných slidech BI-PA1 (patří do přednášky 13 „Moduly, ADT", jejíž PDF v materiálech chybí). Tyto části jsou zpracovány ze standardní znalosti; při studiu ověř proti slidům přednášky 13.

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
> Tato podsekce není ve slidech BI-PA1 (přednáška 13 „Moduly, ADT"). Standardní obsah:

**Modulární programování** rozkládá program na **moduly** (překladové jednotky) s jasně odděleným **rozhraním** a **implementací**. V C/C++ je modul typicky dvojice souborů:
- **hlavičkový soubor `.h`** — *rozhraní*: deklarace funkcí, typů a konstant, které modul nabízí ostatním;
- **zdrojový soubor `.c`** — *implementace*: definice (těla) funkcí.

Ostatní moduly `#include`ují jen `.h`. Každý `.c` se překládá **odděleně** (separate compilation) do objektového souboru; **linker** je spojí. Princip **information hiding** (skrytí implementace, „black box") snižuje provázanost, umožňuje znovupoužití a nezávislý překlad/testování modulů. (Souvisí s abstraktními datovými typy — ADT.)

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

> Slidy BI-PA1 popisují jen rozdíl interpret/překladač; **linker a debugger v nich nejsou** — doplněno ze standardní znalosti.

### 4.1 Programovací jazyky
Jsou to **formální jazyky** popsané přesnou **gramatikou** (často **BNF — Backus-Naurova forma**); rozlišujeme **syntaxi** (jak se program zapisuje) a **sémantiku** (význam). Vysokoúrovňové jazyky (C, C++, Java, Pascal) jsou srozumitelné člověku, ale **nelze je přímo spustit** — musí být přeloženy do strojového kódu. Imperativní (procedurální) jazyk = sekvence příkazů zpracovávaných shora dolů; program se skládá z **deklarací** a **příkazů**.

### 4.2 Překladač vs. interpret
- **Interpretace:** zdroj se přeloží do interní formy, kterou **interpret za běhu provádí** spolu se vstupními daty.
- **Kompilace:** **překladač (compiler)** přeloží zdrojový kód do **strojového kódu**, který se pak spouští přímo nad vstupními daty.

### 4.3 Sestavovací pipeline (standardní doplnění)
1. **Preprocesor** — zpracuje `#include`, `#define`, makra → čistý zdrojový text.
2. **Překladač (compiler)** — přeloží každou překladovou jednotku do **objektového souboru** (`.o`); zde vznikají **syntaktické a typové chyby** (compile-time).
3. **Linker (sestavovací program)** — spojí objektové soubory a knihovny do spustitelného souboru; **rozlišuje symboly** (přiřazuje volání funkcí jejich definicím v jiných modulech), hlásí **nedefinované / vícenásobně definované symboly** (link-time chyby).
   - **Statické linkování** — kód knihovny se vloží do výsledného souboru.
   - **Dynamické linkování** — knihovna (`.dll`, `.so`) se připojí až za běhu.
4. **Běh (run-time)** — zde se projeví logické chyby a chyby jako přístup mimo pole či dereference `nullptr` (C neprovádí běhové kontroly).

### 4.4 Debugger
**Debugger (ladicí program)** umožňuje řízené spouštění programu kvůli hledání chyb:
- **breakpointy** (zastavení na zvoleném řádku),
- **krokování** (step into/over/out),
- **sledování proměnných** (watch) a obsahu paměti, zásobníku volání (call stack),
- inspekci hodnot a vyhodnocování výrazů za běhu.

### 4.5 Specifika jazyka C
C (Ritchie, 1972; normy C89/C99/C11/C23) je vysokoúrovňový jazyk umožňující i nízkoúrovňové operace (ukazatele, adresy), je portabilní a generuje efektivní kód; nevýhodou je, že **veškerá kontrola leží na programátorovi** (žádné běhové kontroly indexů ani platnosti ukazatelů). V BI-PA1 se píše v C, ale překládá kompilátorem C++ (důslednější kontrola), proto se objevují `nullptr`, `bool`.

---

## 5. Co je potřeba na zkoušku znát

### Definice
- Datový typ (množina hodnot + operace + kódování); statická typovost; klasifikace typů v C.
- Statická vs. automatická vs. dynamická alokace; segmenty paměti (`.data`/`.bss`/halda/zásobník).
- Ukazatel, reference `&`, dereference `*`, `nullptr`; `malloc`/`free`.
- Spojový seznam (uzel = data + ukazatel na následníka); varianty (jednosměrný/obousměrný/kruhový/se zarážkou).
- Modul, rozhraní (`.h`) vs. implementace (`.c`), oddělený překlad, information hiding.
- Funkce vs. procedura; deklarace (prototyp) vs. definice; formální vs. skutečné parametry.
- Vstupní (by value) vs. výstupní (přes ukazatel) parametry.
- Překladač, linker (rozlišení symbolů), debugger.

### Klíčové vztahy a složitosti
- Spojový seznam: vložení na začátek $O(1)$, na konec $O(n)$ (resp. $O(1)$ s ukazatelem na konec), hledání $O(n)$.
- V C je předání zásadně hodnotou; výstup jen přes ukazatel/strukturu.
- Memory leak vs. double free; proč zásobník nesnese velká data.

### Algoritmy / kód
- Vytvoření uzlu, vložení na začátek, průchod, hledání, korektní uvolnění spojového seznamu.
- Výstupní parametr přes ukazatel (`minMax`, `scanf`).
- Sestavovací pipeline preprocesor → překladač → linker → běh.
