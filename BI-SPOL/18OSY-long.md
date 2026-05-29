---
tags: [otázka, kurz/OSY, otázka/18, hotovo]
---

# Virtualizace paměti stránkováním, překlad adres, tabulky stránek, náhrada stránek

> **Otázka SZZ:** Virtualizace hlavní paměti stránkováním, principy překladu virtuálních adres na fyzické, struktura tabulek stránek, algoritmy pro nahrazování stránek.

Zdroje: BI-OSY přednášky 8 (Virtuální paměť, stránkování) a 9 (Algoritmy pro náhradu stránek, návrh stránkovacích systémů) — Trdlička, Štepanovský, FIT ČVUT.

---

## 1. Virtualizace hlavní paměti stránkováním

### 1.1 Virtuální adresní prostor (VAS)
![[Virtuální-paměť#Definice]]

Každý **[[Proces]]** má svůj VAS s typickými segmenty `.text` (program), `.data`
(globální proměnné), heap (halda), knihovny a stack (zásobník); některé segmenty
(halda, zásobník) **mění velikost** za běhu. V Linuxu rozsahy přidělených
virtuálních adres a jejich přístupová práva popisují struktury `vm_area_struct`
(zřetězené přes `mm_struct`, na nějž ukazuje `task_struct->mm`).

### 1.2 Problém a princip stránkování
**Problém:** VAS jednoho procesu může být **větší než instalovaná hlavní paměť**
(32-bit proces adresuje $2^{32}$ B = 4 GB, 64-bit teoreticky $2^{64}$ B = 16 EB), a
OS spouští až tisíce procesů ⇒ **součet** velikostí VAS hlavní paměť dále přesahuje.
Většina procesů přitom reálně používá jen **zlomek** svého VAS.

**[[Stránkování|Stránkování]]** (řešení):
- VAS je rozdělen na stejně velké souvislé **stránky** (*pages*), typicky 4 KB
  (Intel) nebo 8 KB (SPARC),
- hlavní paměť na stejně velké **rámce** (*frames*),
- libovolná stránka může být umístěna do libovolného rámce; v hlavní paměti musí být
  jen **aktuálně používané** stránky, zbytek je odložen na disku.

### 1.3 Struktura virtuální a fyzické adresy
Virtuální i fyzická adresa se dělí na dvě části:
$$\text{VA} = (\underbrace{\text{číslo stránky (PN)}}_{m_1\ \text{bitů}},\ \underbrace{\text{offset}}_{m_2\ \text{bitů}}), \qquad
  \text{PA} = (\underbrace{\text{číslo rámce (FN)}}_{n\ \text{bitů}},\ \underbrace{\text{offset}}_{m_2\ \text{bitů}}).$$
**Offset** (poloha uvnitř stránky/rámce) má $\log_2(\text{velikost stránky})$ bitů a
při překladu se **nemění**. Překládá se pouze číslo stránky → číslo rámce (provádí
**[[MMU]]**).

> Příklad: stránka 4 KB ⇒ offset 12 bitů. 32-bit VA ⇒ číslo stránky 20 bitů
> ($2^{20}$ stránek). 16-bit CPU se stránkou 512 B ⇒ offset 9 bitů, číslo stránky
> 7 bitů ($2^7 = 128$ stránek).

---

## 2. Principy překladu virtuálních adres na fyzické

### 2.1 MMU a výpadek stránky
![[MMU#Definice]]

MMU přeloží číslo stránky na číslo rámce pomocí
**[[Stránkovací-tabulka|stránkovací tabulky]]**, jejíž bázi (číslo rámce) drží
**Page Table Base Register (PTBR)** — na x86 registr `CR3`. PTBR se mění při
přepnutí procesu.

![[Výpadek-stránky#Definice]]

### 2.2 Řídicí bity řádku ST
Řádek stránkovací tabulky obsahuje číslo rámce a řídicí bity (orientačně, liší se dle
architektury):
- **P** (present) — zda je stránka v hlavní paměti,
- **A** (accessed) — zda se ke stránce přistupovalo,
- **D** (dirty) — zda byl obsah stránky modifikován,
- **C** (cache enabled/disabled) — zda lze stránku cachovat (nelze pro registry
  periferií mapované do paměti),
- **W** (read/write), **X** (executable), **U** (user/supervisor — ochrana
  adresního prostoru jádra vynulováním bitu U),
- **G** (global) — stránka platná ve VAS všech procesů (MMU její překlad použije bez
  ohledu na proces).

### 2.3 TLB (Translation Lookaside Buffer)
![[TLB#Definice]]

### 2.4 Překlad krok za krokem
Pro každý přístup k paměti (s víceúrovňovou ST):
1. **Prohledá se TLB** podle čísla stránky (+ ASID).
   - **TLB hit** → získá se rámec, ověří se oprávnění → fyzická adresa.
   - **TLB miss** → pokračuje překlad přes ST.
2. **Prohledá se ST** (top-level → nižší úrovně).
   - Chybí-li platný záznam (P = 0) → **výpadek stránky** (page fault) → obsluha OS.
   - Neoprávněný přístup (např. zápis do read-only) → **access fault**.
   - Adresa mimo VAS → **segmentation fault**.
3. Sestaví se fyzická adresa (rámec + offset), aktualizuje se TLB.

Přechod uživatelský ↔ privilegovaný režim (systémové volání: x86 `syscall`/`iret`)
je rychlý — **nemění se adresní prostor** (PTBR). Pozn.: u zranitelnosti **Meltdown**
spekulativní provádění obcházelo ověření oprávnění; obranou je **KPTI** (oddělené ST
pro jádro).

---

## 3. Struktura tabulek stránek

OS udržuje **[[Stránkovací-tabulka|stránkovací tabulky (ST)]]** pro každý proces;
jejich struktura závisí na ISA. Tři typy:

### 3.1 Jednoúrovňová ST
Tabulka obsahuje **pro každou stránku VAS jeden řádek** (číslo rámce + řídicí bity).
Číslo stránky je přímo **index** do tabulky.
- **+** jednoduchý a rychlý překlad (jeden přístup do paměti),
- **−** plýtvání pamětí: i když proces používá jen zlomek VAS, ST musí mít řádek pro
  **každou** stránku.

> Příklad (32-bit CPU, stránka 4 KB): číslo stránky 20 bitů ⇒ ST má $2^{20}$ řádků;
> řádek ~4 B ⇒ ST = 4 MB **na proces**. Pro $2^7 = 128$ procesů → 512 MB jen na ST.

### 3.2 Víceúrovňová ST (multilevel)
ST se rozkládá do **$n$ úrovní**; virtuální adresa se skládá z $n$ indexů (do tabulek
jednotlivých úrovní) a offsetu. Tabulky úrovní $1,\dots,n-1$ obsahují *present* bit a
číslo rámce, kde začíná tabulka následující úrovně; tabulka úrovně $n$ obsahuje číslo
rámce samotné stránky.
- V paměti je vždy **top-level tabulka**; ostatní tabulky být v paměti **nemusí**,
  pokud proces nepoužívá stránky z odpovídající oblasti VAS ⇒ **šetří se paměť** (u
  procesů s malou alokací výrazně).
- **Cena:** pomalejší překlad (více přístupů do paměti) ⇒ nutnost TLB.

Příklady: **x86** dvouúrovňová (Page Directory `PDE` + Page Table `PTE`, indexy
10 + 10 + 12 b); **x86-64** čtyřúrovňová (PML4 → PDPT → PD → PT, 9+9+9+9+12 b,
52-bit fyzická adresa).

> Příklad (32-bit, 4 KB, dvouúrovňová, indexy 10+10+12): top-level $2^{10}$ řádků á
> 4 B; tabulka 2. úrovně $2^{10}$ řádků. Pro proces s `.text+.data` (4 MB) + heap
> (4 MB) + stack (4 MB) stačí top-level + pár tabulek 2. úrovně — výrazně méně než
> 4 MB jednoúrovňové ST.

### 3.3 Invertovaná ST
Jedna tabulka **pro celý systém** s **jedním řádkem na každý rámec** hlavní paměti.
Řádek obsahuje: číslo stránky nahrané do rámce, číslo procesu (jeho VAS), řídicí
bity a **index zřetězení (chain)**. Číslo stránky se hašovací funkcí přepočte na
index do tabulky; protože počet stránek > počet rámců, několik stránek se může
mapovat na stejný řádek ⇒ **zřetězení** (chain).
- **+** zabírá málo místa (úměrné fyzické paměti, ne VAS),
- **−** hledání je pomalé ⇒ nutná TLB.

Používala se v PowerPC a UltraSPARC.

> Příklad (32-bit, 4 KB, max. $2^{10}$ procesů): $2^{20}$ rámců ⇒ $2^{20}$ řádků; řádek
> (číslo stránky 20 b + řídicí bity + chain) ~8 B ⇒ jedna tabulka 8 MB pro **celý
> systém** (nezávisle na počtu procesů).

### 3.4 Srovnání

| Typ ST | Počet řádků | Paměť | Překlad |
|---|---|---|---|
| **Jednoúrovňová** | $2^{m_1}$ (na proces) | velká (na proces) | nejrychlejší |
| **Víceúrovňová** | dle používaných oblastí | malá (na proces) | pomalejší (více přístupů) |
| **Invertovaná** | počet rámců (na systém) | malá (na systém) | pomalé hledání (hash + chain) |

Pro urychlení používají všechny typy **TLB**.

---

## 4. Algoritmy pro nahrazování stránek (PRA)

### 4.1 Princip a požadavky
Když jsou (skoro) všechny rámce obsazené, je při výpadku stránky nutné nějaký rámec
uvolnit. Kroky:
1. **Výběr oběti** — algoritmus pro náhradu stránek (PRA) určí rámec k vyřazení.
2. **Ověření modifikace** — byla-li oběť modifikována (*dirty*), zapíše se její obsah
   na disk (do backing file nebo swapu); nemodifikovaná se jen zahodí.
3. **Aktualizace ST** — ve všech dotčených procesech se v odpovídajícím řádku vynuluje
   bit P (a poznamená umístění stránky na disku).

Požadavky na PRA: **minimalizovat počet výpadků stránky**, rychlost, jednoduchá
implementace. Algoritmy stojí na **principu časové a prostorové lokality** (k
instrukcím/datům se nepřistupuje náhodně).

> V příkladech níže se přistupuje ke stránkám v pořadí 2,3,2,1,5,2,4,5,3,2,5,2 do
> 3 rámců a, b, c. Při více možnostech se volí první rámec v abecedním pořadí.

### 4.2 Optimální algoritmus (OPT)
**Princip:** nahradí se stránka, jejíž **čas příštího přístupu je nejdelší**.
- **+** lze dokázat, že generuje **minimální** počet výpadků,
- **−** nelze realizovat (neznáme budoucnost) ⇒ slouží jen pro **porovnání** kvality
  reálných algoritmů. (Pro referenční řadu: 6 výpadků.)

### 4.3 NRU (Not Recently Used)
Pro každou stránku se pamatuje **R bit** (reference) a **D bit** (dirty), nastavované
HW při přístupu. OS **periodicky resetuje R** na 0 (aby R odlišoval nedávný přístup).
Stránky se dělí do 4 tříd:

| Třída | R | D |
|---|---|---|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 2 | 1 | 0 |
| 3 | 1 | 1 |

Nahradí se stránka z **neprázdné třídy s nejnižším číslem**. Jednoduchý, rozumná
implementace, relativně málo výpadků.

### 4.4 FIFO (First-In First-Out)
OS udržuje **seznam všech stránek** v hlavní paměti; nově nahraná stránka jde na
**konec** seznamu. Nahradí se stránka ze **začátku** (je v paměti nejdéle).
- **+** velmi jednoduchý,
- **−** nezohledňuje, jak často se ke stránce přistupuje (jen kdy byla nahrána) ⇒
  **relativně mnoho výpadků** (referenční řada: 9). Trpí Beladyho anomálií.

### 4.5 Clock
Modifikace FIFO. Seznam je **kruhová fronta**, ručička ukazuje na nejstarší položku;
každá stránka má **R bit** (při nahrání i přístupu nastaven na 1). Hledání oběti:
- R = 1 → resetuj R na 0, posuň ručičku dál,
- R = 0 → **nahraď** stránku, posuň ručičku.

(Referenční řada: 8 výpadků.) **Two-handed clock** (Unix SVR4) má dvě ručičky:
přední (fronthand) resetuje R, zadní (backhand) s odstupem (handspread) nahrazuje
stránky, které mají R stále 0.

### 4.6 LRU (Least Recently Used)
**Princip:** nahradí se stránka, ke které se **nepřistupovalo nejdelší dobu**.
- **+** dobrá aproximace optimálního algoritmu (referenční řada: 7 výpadků),
- **−** problematická implementace: nutné u každého přístupu zaznamenat „čas" a při
  náhradě porovnat časy všech stránek. HW realizace: každý řádek ST má položku
  `time-of-used` (logický čas z čítače inkrementovaného při každém přístupu);
  nahradí se stránka s nejmenší hodnotou.

### 4.7 Aging
**Softwarová simulace LRU.** Pro každou stránku: **R bit** a **$n$-bitový čítač C**.
OS periodicky pro každou stránku: (1) posune obsah C **doprava** o jeden bit,
(2) nastaví **nejvýznamnější** bit C na hodnotu R bitu, (3) resetuje R. Nahradí se
stránka s **nejmenší** hodnotou C.
- **+** menší režie než LRU,
- **−** není přesný LRU (pamatuje jen omezenou historii — `interval` × počet bitů C).

### 4.8 Náhrada stránek v Linuxu (doplnění)
Linux používá variantu LRU, která odděluje **anonymní** stránky (zásobník, halda) od
**souborově mapovaných**; pro každou skupinu vede dva seznamy (active / inactive).
Při náhradě je nutné **reverzní mapování**: pro daný rámec najít všechny procesy a
řádky ST, které na něj ukazují (přes `struct page` → `anon_vma` / `address_space` →
`vm_area_struct` → `mm_struct` → `pgd`), a aktualizovat je. Pro každý rámec se vede
`struct page` s čítačem `_refcount` (zvyšuje se při `mmap`/`fork` s Copy-on-Write).

---

## 5. Co je potřeba na zkoušku znát

### Definice
Virtuální paměť a VAS; stránka vs. rámec; stránkování; struktura virtuální/fyzické
adresy (číslo stránky/rámce + offset); MMU; PTBR (CR3); výpadek stránky; řídicí bity
(P, A, D, C, W, X, U, G); TLB (ASID, hit/miss); typy ST (jedno-/více-úrovňová,
invertovaná).

### Principy a postupy
- Proč stránkování (VAS > fyzická paměť, mnoho procesů) a co řeší (fragmentace).
- Překlad VA → PA: offset se nemění, MMU přeloží číslo stránky na rámec přes ST;
  postup TLB → ST → page fault / access fault / segmentation fault.
- Obsluha výpadku stránky (najdi volný rámec / vyber oběť, dirty → zápis na disk,
  nahraj stránku, aktualizuj ST, zopakuj instrukci).
- Umět spočítat paměťovou náročnost jednoúrovňové / víceúrovňové / invertované ST pro
  zadané parametry (velikost stránky, šířka adresy, počet procesů).

### Algoritmy pro náhradu stránek
- OPT (minimální výpadky, nerealizovatelný — referenční), NRU (R/D bity, 4 třídy),
  FIFO (seznam, nejstarší), Clock (kruhová fronta + R bit), LRU (nejdéle nepoužitá),
  Aging (SW simulace LRU s posuvným čítačem).
- Umět **ručně simulovat** obsazení rámců a počítat výpadky pro zadanou referenční
  řadu (jako v příkladech výše).
- Vědět, že OPT dává dolní mez výpadků, LRU/Aging jsou dobré aproximace, FIFO je
  nejhorší a trpí Beladyho anomálií.
