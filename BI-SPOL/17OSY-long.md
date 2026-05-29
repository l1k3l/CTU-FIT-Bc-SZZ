---
tags: [otázka, kurz/OSY, otázka/17, hotovo]
---

# Procesy a vlákna, synchronizace, uváznutí

> **Otázka SZZ:** Procesy a vlákna, jejich implementace, nástroje pro synchronizaci vláken. Klasické synchronizační úlohy. Uváznutí (deadlock) vláken (alokace prostředků, Coffmanovy podmínky, strategie pro řešení uváznutí).

Zdroje: BI-OSY přednášky 2 (Procesy a vlákna), 3 (Synchronizace vláken), 4 (Klasické synchronizační úlohy), 5 (Uváznutí vláken) — Trdlička, Štepanovský, FIT ČVUT.

---

## 1. Procesy a vlákna a jejich implementace

### 1.1 Program
**Program (aplikace)** je v systému reprezentován spustitelným binárním souborem
uloženým v sekundární paměti (disk). Formát je závislý na OS (ELF na Unixu, PE na
Windows) a obsahuje:
- **TEXT** = spustitelný binární kód,
- **DATA** = proměnné a jejich hodnoty,
- další informace (např. o sdílených knihovnách).

### 1.2 Proces
**[[Proces]]** je instance spuštěného programu — entita, v rámci které jsou alokovány
prostředky (paměť, vlákna, otevřené soubory, zámky, semafory, sokety). Implicitně má
každý proces jedno hlavní („main") vlákno.

Jádro OS udržuje pro každý proces datové struktury pro:
- **identifikaci** — PID (číslo procesu), PPID (číslo rodičovského procesu),
- **bezpečnost** — identita (USER, RUSER),
- **správu paměti** — informace pro překlad virtuálních adres (page table),
- **správu FS** — tabulku deskriptorů souborů.

V Linuxu je proces reprezentován strukturou `task_struct` (mj. `pid`, `tgid`,
`*files`, `*mm`, `*signal`, `exit_state`, `exit_code`, ukazatele na rodiče a
potomky). Procesy tvoří stromovou hierarchii (každý zná svého rodiče i potomky).

**Adresní prostor procesu** (s jedním vláknem) obsahuje TEXT+DATA, haldu (heap,
`malloc`/`calloc`), knihovny a zásobník (stack — historie volání, lokální proměnné).

### 1.3 Vytvoření a ukončení procesu
Nový proces vznikne, když existující proces zavolá systémové volání (na Unixu
`fork(2)`, `execve(2)`; na Windows `CreateProcessA`).

- **`fork()`** — vytvoří nový proces jako **kopii** volajícího. Vrací v rodiči
  číslo (PID) potomka, v potomkovi 0 (při chybě −1). Adresní prostor rodiče se
  „zkopíruje" potomkovi (v praxi pomocí Copy-on-Write), čítač instrukcí ukazuje na
  instrukci za `fork()`. Rodič i potomek běží „nezávisle".
- **`execve(filename, …)`** — přepíše adresní prostor volajícího obsahem zadaného
  souboru a začne ho vykonávat od začátku.
- **`wait(&status)`** — zablokuje rodiče, dokud jeden z potomků neskončí; přečte
  jeho návratový kód (`waitpid` čeká na konkrétního potomka).

Typický vzor: `fork()` → v potomkovi `execve()`, v rodiči `wait()`.

**Ukončení procesu**: jádro předá návratový kód rodiči, ukončí všechna vlákna a
uvolní adresní prostor. Proces se ukončí sám (konec programu, `exit(3)`), nebo ho
ukončí jádro (fatální chyba, přijatý signál). V Linuxu `exit` zapíše návratovou
hodnotu do `task_struct`, nastaví stav **zombie** a notifikuje rodiče; rodič
zombie „vyzvedne" pomocí `wait()`. Skončí-li rodič dřív, sirotky adoptuje proces
`init`.

### 1.4 Vlákno
**[[Vlákno]]** je výpočetní entita (proud instrukcí), které je přidělováno jádro CPU
(historicky *light-weight process*). Vlákna v rámci procesu **sdílí většinu
prostředků** (v Linuxu `mm_struct`, `files_struct`, `signal_struct`), ale **vlastní**
má každé vlákno:
- zásobník (lokální proměnné, historie volání),
- čítač instrukcí a hodnoty registrů (kontext),
- plánovací informace (priorita, čas na CPU).

V adresním prostoru procesu s více vlákny má proto **každé vlákno vlastní zásobník**.
Jádro udržuje pro každé vlákno TID; vlákna jednoho procesu sdílí `tgid`.

### 1.5 Vytvoření a ukončení vlákna
Procesy se implicitně vytvoří s jedním „main" vláknem. Další vlákna se vytváří přes
API/knihovny: POSIX Threads (`pthread`), OpenMP, proprietární API (WinAPI), nebo
vestavěnou podporu jazyka (C++11, Java).

POSIX:
- `pthread_create(&tid, attr, start_routine, arg)` — vytvoří vlákno vykonávající
  funkci `start_routine`; do `tid` uloží jeho číslo,
- `pthread_join(tid, &ret)` — volající čeká na dokončení vlákna `tid`.

Vlákno skončí, když skončí jeho funkce, nebo voláním `pthread_exit()`. Hlavní vlákno
končí na konci `main()` (`return 0`) — spolu s ním končí **všechna** vlákna se
stejným `tgid`. Volání `exit()` z libovolného místa ukončí všechna vlákna procesu.

### 1.6 Multitasking a multithreading
- **Process-based multitasking** — více procesů, každý s jedním vláknem.
- **Thread-based multitasking (multithreading)** — jeden proces s více vlákny
  (sdílí prostředky). Obecně může běžet více procesů, každý s více vlákny.

### 1.7 Plánování vláken, přepínání kontextu, stavy
Jádro OS a vytvořená vlákna sdílí omezený počet jader CPU. Jedno vlákno může být v
jednom okamžiku zpracováváno jedním logickým jádrem; vlákna se na jádrech střídají
**preemptivním plánováním**:
- vláknu je přiděleno volné jádro na základě plánovacích kritérií (např. priorita)
  na dobu **časového kvanta**,
- jádro je vláknu odebráno při uplynutí kvanta (přerušení časovače), při systémovém
  volání (V/V operace), nebo při jiném přerušení.

**Přepínání kontextu** je mechanismus, při kterém se vlákna vystřídají v používání
jádra CPU. *Kontext* = informace nutné pro pozdější obnovení přerušeného vlákna
(čítač instrukcí, registry). Probíhá ve třech krocích: (1) uloží se kontext
původního vlákna, (2) jádro naplánuje další vlákno, (3) nastaví se jeho kontext.

**Stavy vlákna** (co se s vláknem právě děje):

| Stav | Význam |
|---|---|
| **Idle** | vzniká nové vlákno |
| **Ready** | vlákno čeká na přidělení jádra CPU |
| **Running** | vlákno je zpracováváno jádrem CPU |
| **Blocked** | vlákno čeká na událost (dokončení V/V, příchod signálu, …) |
| **Zombie** | vlákno je ukončováno, ale ještě není vše dokončeno |
| **Free** | vlákno bylo zcela zrušeno (teoretický stav) |

Přechody: Idle → Ready → Running; Running ↔ Ready (preempce); Running → Blocked →
Ready (čekání na událost); Running → Zombie → Free (ukončení).

### 1.8 Časově závislé chyby a kritická sekce (motivace pro synchronizaci)
Deterministický algoritmus vytvoří ze stejných vstupů vždy stejné výsledky.
**[[Souběh|Časově závislá chyba]] (race condition)** je situace, kdy více vláken
používá společné sdílené prostředky a výsledek závisí na **rychlosti** vláken.

Příklad: dvě vlákna provedou `counter++`, což se přeloží na `load R,A` / `inc R` /
`store A,R`. Při nevhodném prokládání instrukcí se jedna inkrementace „ztratí".
Časově závislé chyby mají **náhodný výskyt** ⇒ špatně se detekují.

**[[Kritická-sekce]]** je část programu, kde vlákno používá sdílené prostředky.
*Sdružené kritické sekce* dvou vláken se týkají stejného prostředku. **Vzájemné
vyloučení**: vlákna se nesmí nacházet ve stejné sdružené kritické sekci současně.

Pravidla pro korektní paralelní program:
1. žádné předpoklady o rychlosti vláken a počtu jader,
2. zajistit výlučný přístup ke sdíleným prostředkům (žádné vlákno však nesmí čekat
   na vstup do KS nekonečně dlouho),
3. mimo KS nesmí být vlákno blokováno ostatními.

---

## 2. Nástroje pro synchronizaci vláken

### 2.1 Přehled
Synchronizační nástroje existují na třech úrovních:
- **Hardware** — atomické instrukce (SPARC `cas`, `ldstub`, `swap`; x86-64 `xchg`,
  `cmpxchg`; RISC-V `amoswap`, `lr/sc`).
- **Jádro OS** — spin locks, reader-writer locks, dispatcher objects.
- **Aplikace** — roury, signály, semafory, fronty zpráv (Unix); mutexy, semafory,
  podmíněné proměnné (POSIX); konstrukce jazyka (C++, Java).

Vzájemné vyloučení lze docílit dvěma způsoby: **aktivním čekáním** (busy waiting) a
**blokujícími systémovými voláními / knihovními funkcemi**.

### 2.2 Aktivní čekání (busy waiting, spinning)
Sdílená proměnná indikuje obsazenost KS. Před vstupem vlákno ve smyčce „aktivně"
testuje proměnnou, dokud se sekce neuvolní; pak ji zamkne. Po opuštění odemkne.

**Naivní řešení proměnnou `lock`** (0 = odemčeno, 1 = zamčeno) **nefunguje**:
```
while (lock == 1);   // busy wait
lock = 1;            // enter CR
critical_region();
lock = 0;            // leave CR
```
Mezi testem `while` a zápisem `lock = 1` může dojít k přepnutí kontextu — obě vlákna
projdou testem a obě vstoupí do KS. Problém je, že test a nastavení **nejsou
atomické**.

**Instrukce TSL (test-and-set-lock)** — hypotetická atomická instrukce, která ve
dvou krocích (1) načte slovo z paměti do registru a (2) nastaví slovo na nenulovou
hodnotu. Protože je **atomická**, řeší korektní zamykání i ve více-jádrových
systémech se sdílenou pamětí:
```
enter_region:
    tsl REGISTER, LOCK   ; atomicky: zkopíruj LOCK do registru a nastav LOCK=1
    cmp REGISTER, #0     ; byl zámek 0?
    jne enter_region     ; ne (byl nastaven) → smyčka
    ret                  ; ano → vstup do CR

leave_region:
    store LOCK, #0        ; zámek = 0
    ret
```
Reálné ISA mají varianty (`cas`, `xchg`, `cmpxchg`, `lr/sc`).

**Vlastnosti.** Výhoda: minimální režie, čeká-li se krátce. Nevýhoda: čekající
vlákno zatíží jedno jádro na 100 %; může vést k **inverznímu prioritnímu problému**.

**Inverzní prioritní problém** (při prioritním plánování s fixní prioritou a
omezeném počtu jader): vlákno A s nízkou prioritou je v KS, vlákno B s vyšší
prioritou aktivně čeká na vstup do KS a všechna jádra jsou obsazena vlákny s vyšší
prioritou než A. A se nikdy nenaplánuje → neuvolní KS → B čeká věčně.

### 2.3 Blokující volání
Blokující systémové volání/knihovní funkce si pomocí datových struktur pamatuje stav
KS a seznam čekajících vláken:
- **zamčená sekce**: volající vlákno se zablokuje (stav *Blocked*, přestane mu být
  přidělováno CPU ⇒ **pasivně** čeká),
- **odemčená sekce**: vlákno se nezablokuje, jen si poznamená, že sekce je zamčená,
  a vstoupí,
- po opuštění KS se probudí jedno čekající vlákno (nebo se sekce označí jako
  odemčená).

**Vlastnosti.** Výhoda: čekání nepředstavuje žádnou režii (vlákno nezatěžuje CPU).
Nevýhoda: začátek/konec čekání představují režii (nutná změna stavu vlákna v jádře).
⇒ Vyplatí se při delším očekávaném čekání.

#### Zámky (mutexy)
**[[Zámek]]** (mutex) si pamatuje stav (zamčený/odemčený) a množinu blokovaných
vláken. Atomické operace `mutex_lock` (zamkne, nebo zablokuje volající) a
`mutex_unlock` (probudí jedno blokované vlákno, nebo odemkne).

#### Podmíněné proměnné
**[[Podmíněná-proměnná]]** je svázaná se zámkem. `cond_wait(var, mutex)` atomicky
uvolní `mutex` a zablokuje volající, dokud není proměnná signalizována (po probuzení
je `mutex` opět zamčen). `cond_signal(var)` odblokuje aspoň jedno vlákno. Předchozí
signály se **neukládají**; podmínka se testuje v cyklu **`while`** (kvůli změně
podmínky jiným vláknem a **falešným probuzením** — *spurious wakeup*).

#### Semafory
**[[Semafor]]** obsahuje celočíselný čítač a množinu blokovaných vláken.
`sem_wait` (P): čítač > 0 → sníží o 1, jinak blokuje. `sem_post` (V): čeká-li někdo,
probudí ho, jinak zvýší čítač o 1. Binární semafor (init 1) ≈ zámek, obecný počítá
prostředky. (V C++ standardně nejsou.)

#### Bariéry
**[[Bariéra]]** synchronizuje iterační výpočty: má čítač (síla) a frontu.
`barrier_wait` sníží čítač a blokuje, dokud poslední příchozí nedosáhne 0 — pak
probudí všechna vlákna a čítač se resetuje.

---

## 3. Klasické synchronizační úlohy

Cíle řešení: **správné** (bez časově závislých chyb, uváznutí, livelocku,
hladovění), **optimální** (maximální souběžnost) a **spravedlivé** (žádné vlákno
nepředbíhá ostatní).

### 3.1 Producent-konzument
Vlákna si vyměňují data přes sdílenou paměť (frontu) o omezené velikosti $N$.
**Producent** vkládá data, **konzument** je vybírá. Problémy: (1) výlučný přístup k
frontě, (2) prázdná fronta → blokovat konzumenta, (3) plná fronta → blokovat
producenta.

**Řešení semafory** — `mutex` (výlučný přístup), `empty` (počet volných míst, init
$N$), `full` (počet plných míst, init 0):
```
producer:                          consumer:
  item = produce_item();             sem_wait(&full);   // je co vybrat?
  sem_wait(&empty);  // je místo?    mutex_lock(&mtx);
  mutex_lock(&mtx);                  remove_item(&item);
  insert_item(item);                 mutex_unlock(&mtx);
  mutex_unlock(&mtx);                sem_post(&empty);  // uvolnil jsem místo
  sem_post(&full);   // přidal jsem  consume_item(item);
```
(Pořadí `sem_wait` před `mutex_lock` je důležité — opačné pořadí vede k uváznutí.)
Lze řešit i podmíněnými proměnnými (`cv_empty`, `cv_full`) s testem ve `while`.

### 3.2 Večeřící filozofové
$N$ filozofů sedí u kulatého stolu, mezi sousedy je jedna vidlička (celkem $N$). Aby
filozof jedl, musí získat **obě** sousední vidličky. Stavy: přemýšlí / má hlad /
jí. Optimum: současně může jíst až $\lfloor N/2 \rfloor$ filozofů.

- **Naivní řešení** (vezmi levou, pak pravou) → **uváznutí**, vezmou-li všichni
  současně levou vidličku a čekají na pravou. Varianta „vrať levou, zkus později" →
  hrozí **livelock**.
- **Správné (neoptimální)**: celý stůl s vidličkami je jedna KS chráněná jedním
  mutexem ⇒ jí vždy jen jeden filozof.
- **Správné optimální**: mutex + $N$ semaforů (po jednom na filozofa) + pole stavů.
  Funkce `test(i)` povolí filozofa `i` jíst, jen pokud má hlad a oba sousedé nejedí
  (`sem_post(&s[i])`); `take_forks`/`put_forks` chrání mutex a po odložení vidliček
  testují oba sousedy. Alternativně mutex + $N$ podmíněných proměnných.

### 3.3 Čtenáři-písaři
Sdílený prostředek, dva typy vláken: **čtenáři** (jen čtou) a **písaři** (modifikují).
Modifikovat smí jen jeden písař a jen když nikdo nečte; číst může více čtenářů
současně. Cíle: optimum (souběžné čtení) + spravedlnost (nikdo nepředbíhá).

- **Správné (neoptimální)**: prostředek = KS pod jedním mutexem ⇒ přistupuje vždy
  jen jeden (i čtenáři se vylučují) — není optimální.
- **Optimální (s hladověním)**: čítač čtenářů `rc` chráněný `mutex_rc`; první čtenář
  zamkne `mutex_db`, poslední ho odemkne; písař drží `mutex_db`. Více čtenářů čte
  současně, ale **písaři mohou hladovět** (stálý příliv čtenářů).
- **Optimální spravedlivé (FIFO)**: protože většina API negarantuje probouzení v
  pořadí FIFO, udržuje se explicitní **fronta čekajících** (zřetězený seznam
  podmíněných proměnných s typem R/W a čítači `rc`, `wc`, `wrc`, `wwc`). Vlákno se
  zařadí na konec fronty a probouzí se v pořadí příchodu.

### 3.4 Spící holič
$N$ holičů, $N$ křesel na holení, $M$ křesel pro čekající. Není-li zákazník, holič
spí; přijde-li zákazník, buď probudí spícího holiče, počká na volném křesle, nebo
(je-li plno) odejde. **Řešení**: mutex (výlučný přístup k čítači čekajících `wc`) +
dva semafory `customers` (čekající zákazníci) a `barbers` (volní holiči). Řešení je
optimální (stříhá max. počet holičů), ale **nespravedlivé** (holič probudí
libovolného zákazníka → hrozí hladovění); spravedlnost by zajistila FIFO fronta.

---

## 4. Uváznutí (deadlock)

### 4.1 Výpočetní prostředky a jejich alokace
**Výpočetní prostředek** může být fyzický (paměť, tiskárna) nebo logický (proměnná,
soubor, mutex). **Sdílený** prostředek smí v jednom okamžiku používat jen jedno
vlákno ⇒ nutné vzájemné vyloučení.

Typy podle odnímatelnosti:
- **odnímatelné (preemptable)** — již alokovaný prostředek lze vláknu bez rizika
  odebrat (např. odložení stránky paměti na disk),
- **neodnímatelné (nonpreemptable)** — nelze odebrat bez rizika (tiskárna). Bohužel
  většina prostředků je neodnímatelná.

Sekvence použití prostředku: **alokace** → **použití** → **uvolnění**. Při alokaci
(žádosti) může být vlákno blokováno (`mutex_lock`, `sem_wait`), blokováno na čas
(`mutex_trylock`) nebo neblokováno (`fork`, `malloc`).

### 4.2 Alokační graf
**Alokační graf** znázorňuje alokaci prostředků vlákny — je to **orientovaný graf**
se dvěma typy uzlů (prostředky / vlákna):
- hrana **prostředek → vlákno**: vlákno má prostředek alokovaný,
- hrana **vlákno → prostředek**: vlákno na prostředek čeká.

**Každá smyčka v grafu představuje uváznutí** (vlákna ve smyčce čekají a nemohou
pokračovat). Uváznutí závisí na pořadí alokace prostředků.

### 4.3 Definice uváznutí
![[Uváznutí#Definice]]

### 4.4 Coffmanovy podmínky
![[Uváznutí#Coffmanovy podmínky]]

### 4.5 Strategie pro řešení uváznutí

#### Pštrosí strategie
Problém se **ignoruje** (řeší se jen částečně / zásahem uživatele). Opodstatněná,
když je mnoho různě se chovajících vláken/prostředků a pravděpodobnost uváznutí je
malá (řešení by bylo příliš drahé). Praktické řešení většiny univerzálních OS — jádro
je navrženo jako „deadlock free", na úrovni procesů se problém řeší jen částečně
(limity, `ulimit -a`). Nepřijatelné ve „fault tolerant" systémech.

#### Prevence uváznutí
Založena na **porušení aspoň jedné** Coffmanovy podmínky:
1. **Vzájemné vyloučení** — nelze porušit bez rizika časově závislých chyb (pokud
   prostředek používá více vláken pro čtení i zápis).
2. **Neodnímatelnost** — uložit (zapamatovat) stav prostředku, aby šel obnovit
   (např. přepnutí kontextu při sdílení jádra CPU).
3. **Drž a čekej** — zná-li vlákno dopředu všechny potřebné prostředky, alokuje je
   **všechny najednou** předem (vede k horšímu využití prostředků).
4. **Kruhové čekání** — prostředkům se přidělí jedinečná čísla
   ($F: R \to \mathbb{N}$, prosté) a vlákno je smí alokovat **jen ve vzrůstajícím
   pořadí** ⇒ v alokačním grafu nevznikne smyčka. Vhodné očíslování nemusí vždy
   existovat; řeší se ve fázi návrhu/kompilace.

> Příklad: naivní večeřící filozofové uváznou, vezmou-li všichni levou vidličku.
> Alokují-li vidličky ve vzrůstajícím pořadí čísel, k uváznutí nedojde.

#### Předcházení vzniku uváznutí
Založeno na **opatrné alokaci** za znalosti budoucích požadavků. Stav systému
popisují:
- existence prostředků $E = [E_1,\dots,E_m]$, vektor volných $F = [F_1,\dots,F_m]$,
- matice požadavků $Q$ (celkové požadavky vláken), matice přidělení $A$, matice
  chybějících $M = Q - A$.

**Bezpečný stav** = existuje pořadí přidělování prostředků vláknům, které garantuje
postupné uspokojení **všech** vláken. **Bankéřův algoritmus**: prostředek se přidělí,
jen pokud systém zůstane v bezpečném stavu, jinak vlákno čeká.

*Test bezpečnosti*: opakovaně hledej vlákno, jehož chybějící požadavky ($M$) lze
uspokojit volnými prostředky $F$; takové vlákno „doběhne" a uvolní své prostředky
(přičti $A$ k $F$). Jsou-li takto uspokojena všechna vlákna → bezpečný stav.

Nutná podmínka: požadavky vláken musí být **známy předem**. Nejsou-li, uváznutí
nelze předejít.

#### Detekce a zotavení
Strategie **počítá s uváznutím**: pravidelně ho detekuje a odstraní. Dvě fáze:
- **Detekce** — algoritmus podobný testu bezpečnosti, ale s **aktuálními** požadavky
  $Q^c$ (current request matrix): postupně „označuj" vlákna, jejichž aktuální
  požadavky lze uspokojit volnými prostředky $C$, a přičítej jejich alokované
  prostředky. **Neoznačená vlákna na konci jsou uvázlá.**
- **Zotavení** — uvolnit část prostředků (poruší se smyčka): ukončení všech uvázlých
  vláken, postupné ukončování, nebo návrat (rollback) a restart z dříve uloženého
  stavu.

Standardní nástroje OS pro detekci: `ps` (stav vláken), `gstack` (zásobníky vláken),
ladicí nástroje (Valgrind).

---

## 5. Co je potřeba na zkoušku znát

### Definice
Program, proces (`task_struct`, PID/PPID/TID/TGID, adresní prostor); vlákno (sdílené
vs. vlastní prostředky); stavy vlákna (Idle/Ready/Running/Blocked/Zombie/Free);
přepínání kontextu; časově závislá chyba (souběh); kritická sekce a vzájemné
vyloučení; zámek, semafor (P/V), podmíněná proměnná, bariéra; uváznutí; alokační
graf; Coffmanovy podmínky; bezpečný stav.

### Mechanismy a postupy
- Vytvoření/ukončení procesu (`fork`/`execve`/`wait`/`exit`) a vlákna
  (`pthread_create`/`join`/`exit`).
- Aktivní čekání: proč `lock` proměnná nestačí, instrukce TSL (enter/leave region),
  inverzní prioritní problém.
- Blokující volání: zámky, podmíněné proměnné (proč `while`), semafory, bariéry +
  jejich výhody/nevýhody (režie vs. zátěž CPU).
- Klasické úlohy: producent-konzument (semafory `mutex`/`empty`/`full`), večeřící
  filozofové (naivní → deadlock, optimální se semafory), čtenáři-písaři (hladovění,
  FIFO), spící holič.

### Uváznutí
- Coffmanovy podmínky (umět vyjmenovat a vysvětlit, že 1.–3. jsou nutné, 4. =
  uváznutí, nesplnění jedné ⇒ bez uváznutí).
- 4 strategie: pštrosí, prevence (porušení podmínek), předcházení (bezpečný stav +
  bankéřův algoritmus), detekce a zotavení.
- Umět ručně provést test bezpečnosti / detekci nad maticemi $Q$, $A$, $M$, $F$.
