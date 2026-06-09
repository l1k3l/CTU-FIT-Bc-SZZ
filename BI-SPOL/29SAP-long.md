---
studyplan: true
etapa: 1 · SAP — Daňhel
qid: 29SAP
examiner: Daňhel
topic: Architektura počítače, instrukční cyklus, ISA, paměťová hierarchie, cache
readiness: in progress
tags:
  - otázka
  - kurz/SAP
  - otázka/29
  - hotovo
---

# Architektura počítače, instrukční cyklus, ISA, paměti a cache

> **Otázka SZZ:** Architektura číslicového počítače, instrukční cyklus počítače, základní třídy souborů instrukcí (ISA). Paměťový subsystém počítače, paměťová hierarchie, skrytá paměť (cache).

Zdroje: BI-SAP, `struktura_procesoru.pdf`, `pametovy_system_pocitace.pdf`, `sap-10-pameti.pdf` (H. Kubátová, KČN FIT ČVUT).

---

## 1. Architektura číslicového počítače

### 1.1 Von Neumannova architektura
**[[Von-Neumannova-architektura|Von Neumannova architektura]]** ukládá **data i instrukce do společné paměti** — z obsahu paměti nelze poznat, zda jde o instrukci nebo data (nutný kontext). Počítač má **5 základních částí**:

1. **datová část — ALU** (aritmeticko-logická jednotka),
2. **řídicí část — řadič** (control unit),
3. **hlavní paměť** (paměťový subsystém),
4. **vstupní zařízení**,
5. **výstupní zařízení**.

**Procesor** = ALU + adresové a pracovní registry + řadič. Jednotky jsou propojeny **sběrnicí**.

**von Neumannovo úzké hrdlo (bottleneck):** výkon je omezen rychlostí přenosu mezi procesorem a pamětí po společné sběrnici. Zmírnění: [[Cache|cache]], **DMA** (Direct Memory Access — přenos dat přímo mezi pamětí a V/V bez procesoru; jistá odchylka od von Neumanna).

### 1.2 Harvardská architektura
**Oddělená paměť instrukcí a paměť dat** (adresují se nezávisle, vlastní sběrnice) → lze **současně číst instrukci i data** (vyšší propustnost, není von Neumannovo úzké hrdlo). Typická pro jednočipové mikropočítače (např. AVR).

### 1.3 Proč PC používá von Neumanna a vestavěné systémy Harvarda? (časté doptávání)
- **Osobní počítač = von Neumann**, protože společná paměť je **flexibilní**: velikost programu a dat není pevně dělená, **program lze zpracovávat jako data** (zavaděče, překladače, JIT, OS, který nahrává programy). Univerzální stroj potřebuje měnitelný obsah paměti.
- **Vestavěné systémy = Harvard**, protože **program se (skoro) nemění** — uložen v ROM/FLASH, zatímco data v RAM; jde tedy použít **různé typy paměti** a **jednodušší/levnější sběrnici** pro každou. Oddělení dává i vyšší rychlost a bezpečnost (data nepřepíšou kód).

> *Doplnění nad rámec slidů:* moderní procesory jsou navenek von Neumann, ale uvnitř mají **rozdělenou L1 cache** na instrukční a datovou (split I/D cache) — tedy **Harvard na úrovni cache**. „Harvard je levnější" = jednodušší sběrnice, ne nutně levnější celkově.

### 1.4 Registry procesoru
- **PC (programový čítač)** — adresa zpracovávané instrukce; po jejím čtení se **inkrementuje** (pak ukazuje na následující).
- **IR / RI (registr instrukce)** — uchová přečtenou instrukci k dekódování (programátorovi nepřístupný).
- **střadač (akumulátor)** / **pracovní registry (GPR)**.
- **SP (ukazatel zásobníku)** — pro volání podprogramů a přerušení.
- **stavový registr (příznaky):** C (carry/přenos), V (overflow/přeplnění), N (záporný), Z (nulový), H (poloviční přenos), I (přerušení), …

### 1.5 Sběrnice
**Sběrnice** = vodiče + pravidla pro propojení jednotek. Podsběrnice: **adresová (AB)**, **datová (DB)**, **řídicí (CB)**. Adresy a data mohou být **časově multiplexovány**. Přidělování (řeší kolize) **centralizované** nebo **distribuované**.

---

## 2. Instrukční cyklus

[[Instrukční-cyklus|Řadič]] zpracovává instrukce v opakovaném cyklu:

1. **Čtení instrukce (fetch)** — z adresy v PC se instrukce přečte do IR; PC se inkrementuje.
2. **Dekódování instrukce** — z IR se zjistí operace, počet a typ operandů, délka.
3. **Čtení operandů** — podle způsobu adresace.
4. **Provedení instrukce (execute)** — výpočet v ALU.
5. **Uložení výsledku.**
6. **Přerušení?** — kontrola žádosti; návrat na začátek cyklu.

Podle obrázku 5.3 se fáze sdružují: **fetch** = čtení instrukce + dekódování (fáze 1–2), **execute** = čtení operandů + provedení + uložení výsledku (fáze 3–5). Pohyb dat řídí **řídicí signály z řadiče**.

**Hierarchie řízení:** vyšší jazyk → (překladač) → jazyk symbolických instrukcí (JSI) → (assembler) → strojový kód → (procesor) → řídicí signály.

**Řadič** je sekvenční obvod realizující instrukční cyklus; bývá **obvodový** nebo **mikroprogramový** (dílčí mikrooperace uloženy jako **mikroinstrukce** v řídicí paměti = firmware). Pro synchronizaci vhodný **Mooreův** [[Konečný-automat|automat]].

### 2.1 Přerušení (časté doptávání)
**Přerušení (interrupt)** = mechanismus, kterým procesor **přeruší** běžící program, vykoná **obsluhu přerušení** (podprogram, ISR) a poté se **vrátí** k přerušenému programu.

- **Kdy může nastat:** žádost se kontroluje na **konci instrukčního cyklu** (fáze „Přerušení?") — tedy **až po dokončení právě prováděné instrukce**, ne uprostřed ní (instrukce je nejmenší nedělitelná jednotka).
- **Co se při něm děje:** na **zásobník** se uloží **návratová adresa (obsah PC)** a obvykle i **obsah stavového registru (příznaky)** — protože obsluha by je přepsala; do PC se zapíše adresa obsluhy (často z **vektoru přerušení**). Po obsluze se návrat provede instrukcí **RETI** (ne RET — RETI navíc obnoví příznaky a informuje řadič přerušení).
- **Typy:** **vnější (HW)** od V/V zařízení přes **řadič přerušení** (řeší priority); **vnitřní** vyvolané procesorem (dělení nulou, porušení ochrany paměti, **výpadek stránky**); **softwarové** = speciální instrukce (systémové volání OS).

### 2.2 Zřetězení (pipelining)
Moderní procesory cyklus **zřetězují** — překrývají fáze sousedních instrukcí (zatímco se jedna provádí, další se dekóduje a třetí se čte) jako montážní linka. **Výhoda:** vyšší propustnost — v ideálním stavu se dokončí ~1 instrukce za takt, i když jedna instrukce trvá více taktů. **Bez zřetězení** procesor začne další instrukci až po úplném dokončení předchozí (nižší využití jednotek). Brzdí ho **hazardy** (datové — závislost na výsledku; řídicí — skoky; strukturní — sdílený prostředek), řeší se bublinami, předbíháním (forwarding) a predikcí skoků.

---

## 3. Základní třídy souborů instrukcí (ISA)

### 3.1 Definice
**[[Instrukční-soubor|ISA (Instruction Set Architecture)]]** = architektura souboru instrukcí — rozhraní mezi HW a programem. **Instrukce** je příkaz zakódovaný jako číslo, určující *co* (operace), *s čím* (operandy), *kam* uložit výsledek a *kde* pokračovat. Operand bývá určen **adresou** (ne hodnotou).

**Formát instrukce:** operační znak + operandy; podle počtu adres **1-, 2-, 3-adresové**. Paměť je **slabikově (bytově) organizovaná**; delší položky se ukládají jako **big-endian** (nejvyšší slabika na nižší adrese — IBM 360, Motorola) nebo **little-endian** (nižší slabika na nižší adrese — Intel x86).

### 3.2 Tři základní třídy ISA
| třída | princip | výhody | nevýhody |
|---|---|---|---|
| **střadačová** | jeden pracovní registr (střadač), implicitní operand ALU | krátké instrukce, jednoduchý HW a dekódování | **častá komunikace s pamětí** |
| **zásobníková** | ALU pracuje s vrcholem HW zásobníku | krátké instrukce (operandy implicitní) i programy | jen sekvenční přístup, nelze minimalizovat přístupy do paměti |
| **GPR** (registry pro všeobecné použití) | sada rovnocenných registrů | registry rychlé, náhodný přístup, mezivýsledky a lokální proměnné → méně přístupů do paměti | omezený počet registrů, složitější překladač |

**Proč se dnes používá GPR (a víceadresové ISA), když dřív ne? (časté doptávání)**
- **Registry jsou rychlé a přístupné náhodně** → mezivýsledky a lokální proměnné drží v registrech ⇒ **méně přístupů do (pomalé) paměti** = klíč k výkonu. Střadačová/zásobníková ISA musí často komunikovat s pamětí.
- **Dřív** byl HW drahý (málo tranzistorů → málo registrů) a stačily jednoduché stroje; **dnes** je tranzistorů dost na velké registrové pole a chytrý překladač, který registry umí přidělit. Víceadresové instrukce navíc usnadňují **paralelizaci** (nezávislé operandy lze zpracovat souběžně, vhodné pro zřetězení), zatímco zásobníková/střadačová struktura vnucuje sériové zpracování přes jediný vrchol/střadač.
- **Cena:** GPR ISA má **omezený počet registrů**, **složitější překladač** a delší přepnutí kontextu.

> *Doplnění nad rámec slidů:* GPR architektury se dále dělí na **register-register (load/store)** a **register-memory**; podle filozofie návrhu se rozlišuje **RISC** (málo jednoduchých instrukcí stejné délky, load/store) vs **CISC** (mnoho složitých instrukcí proměnné délky).

### 3.3 Způsoby adresace operandů
- **Přímá:** implicitní (určen op. znakem), **immediate** (konstanta v instrukci), **přímá adresa** (do paměti / číslo registru).
- **Nepřímá:** instrukce obsahuje adresu, na níž je teprve adresa operandu.
- **Relativní:** operand určen offsetem k registru (často **PC** u skoků).
- **Indexová / bázová:** součet báze + index (pro pole, matice).
- **Autoinkrementace/dekrementace** (zásobník: PUSH/POP), **škálovatelná** (×1, 2, 4, 8).

### 3.4 Kategorie instrukcí
Přesuny dat (MOV, LD/ST, PUSH/POP), aritmetické a logické (ADD, ADC s přenosem, SUB, SBC, CP = porovnání; AND/OR/XOR), **posuvy a rotace** (LS, AS, RO, RC přes carry), **skoky** (nepodmíněný JMP, podmíněné BRxy podle příznaků), **volání podprogramů** (CALL/RET — návratová adresa na zásobník), **přerušení** (vnější HW / vnitřní / softwarové; návrat RETI, na zásobník i stavový registr).

---

## 4. Paměťový subsystém a paměťová hierarchie

### 4.1 Paměťová hierarchie
**[[Paměťová-hierarchie|Paměťová hierarchie]]** vyvažuje **rychlost, kapacitu a cenu** — vyšší vrstvy (blíž procesoru) jsou rychlé, malé, drahé; nižší pomalé, velké, levné:

| vrstva | realizace | doba přístupu | kapacita |
|---|---|---|---|
| registry | klopné obvody | jednotky ns | desítky–stovky B |
| **cache** (L1/L2/L3) | statická RAM (SRAM) | ~1–10 ns | kB–MB |
| hlavní (operační) paměť | dynamická RAM (DRAM) | ~50 ns | GB |
| vnější paměť | magnetický disk / SSD | ~ms / µs | GB–TB |
| záložní paměť | CD/DVD, páska, flash | ~s | TB |

**Které paměti jsou uvnitř procesoru? (časté doptávání)** Registry, **cache L1/L2** (často i L3) a [[TLB]] jsou **na čipu**; hlavní paměť (DRAM) a níže jsou mimo.

**Proč jsou registry malé, když jsou nejrychlejší — proč jich nemít hodně místo paměti? (časté doptávání)**
- Čím **větší paměť, tím delší přístup** (delší adresové dekodéry, větší kapacitní zátěž vodičů, fyzická vzdálenost) — velké registrové pole by už nebylo „registrově rychlé".
- Každý registr musí být **přímo adresovatelný v instrukci**: víc registrů = víc adresových bitů = **delší instrukce** a horší hustota kódu.
- Registry jsou drahé na plochu čipu. Proto se staví **hierarchie**: málo rychlých registrů nahoře, hodně levné kapacity dole.

### 4.2 Princip lokality
Hierarchie funguje díky **lokalitě odkazů**:
- **časová lokalita** — nedávno použitá data budou pravděpodobně použita znovu (→ uchovat v rychlé paměti);
- **prostorová lokalita** — bude se přistupovat k blízkým datům (→ přenášet po **blocích**).

### 4.3 Dělení pamětí
- **podle použití:** hlavní, vnější, skrytá (cache);
- **podle výběru položek:** **adresovatelné (RAM)**, **asociativní (CAM** — výběr podle obsahu/klíče**)**, sériové, zásobník (LIFO), fronta (FIFO);
- **podle možnosti zápisu:** **RWM/RAM** — **SRAM** (statická, klopné obvody, rychlá, drahá → cache), **DRAM** (dynamická, vyžaduje **refresh**, levnější → hlavní paměť); **ROM/PROM** (permanentní), **EPROM/EEPROM/FLASH** (semipermanentní);
- **podle napájení:** **volatilní** (SRAM, DRAM — ztratí obsah) vs **nonvolatilní** (ROM, FLASH).

### 4.4 Terminologie a typický paměťový obvod
**Paměťová buňka** (1 bit) → **paměťové místo** (slovo, čtené najednou) → **paměťová matice**, vybíraná **adresou**; **kapacita** = max. počet položek. Typický obvod: paměťová matice + **dekodér řádků** (1 z N) + **výběr sloupců (multiplexor)** + čtecí/zapisovací zesilovače + řídicí logika. Řídicí signály (často aktivní v 0): **CS** (Chip Select), **WE** (Write Enable), **OE** (Output Enable). Kapacity jsou mocniny 2 (kvůli adresovému dekodéru).

### 4.5 Virtualizace paměti (stránkování, segmentace)
**Virtuální paměť** vytváří logický prostor větší než fyzická hlavní paměť:
- **Stránkování** — logický prostor dělen na **stránky** pevné délky, fyzický na **rámce**; překlad přes **tabulku stránek** (příznak přítomnosti, Dirty bit). Chybí-li stránka → přerušení a načtení z disku.
- **Segmentace** — dělení na **segmenty** proměnné délky; logická adresa = báze + offset.

---

## 5. Skrytá paměť (cache)

### 5.1 Účel a princip
**[[Cache|Cache (skrytá paměť)]]** je malá rychlá paměť (SRAM) mezi procesorem a hlavní pamětí, obsahující **kopie nejčastěji používaných položek** HP. Funguje díky **principu lokality**, je pro programátora **zcela průhledná** a bývá přímo na čipu. Přístup je **asociativní** (podle **obsahu / klíče**, ne podle adresy) — místo adresového dekodéru má **adresář**.

### 5.2 Rozdělení adresy a mapování
Adresa se dělí na **3 části**: **TAG (podklíč)** | **adr (řádek/index)** | **výběr z bloku (offset)**. Data se uchovávají po **blocích (řádcích)** o velikosti např. 16 nebo 32 B.

- **Přímo mapovaná** (stupeň asociativity 1) — položka jen na **jednom** řádku; realizovatelná běžnou RAM.
- **Skupinově (N-cestně) asociativní** — položka na jednom z $N$ míst.
- **Plně asociativní** — položka kdekoli (stupeň asociativity = kapacita); paralelní porovnání klíče se všemi položkami adresáře (XOR + AND), ale ~3× větší plocha čipu.

**Výpočet bitů adresy:** výběr z bloku = $\log_2(\text{velikost bloku})$; adr = $\log_2(\text{kapacita}/\text{stupeň asociativity}) - \text{bity bloku}$; TAG = zbytek šířky fyzické adresy.
*Příklad:* 32b adresa, cache 4 KB, stupeň 4, blok 16 B → blok = 4 b, adr = $\log_2(1\,\text{KB}) - 4 = 6$ b, TAG = $32-6-4 = 22$ b; srovnávacích obvodů $4\times22=88$.

### 5.3 Zásah, výpadek, zápis
- **Zásah (hit)** / **výpadek (miss):** čtení se zahájí **současně z cache i HP**; při zásahu se cyklus HP nedokončí, při výpadku se data přečtou z HP (a uloží do cache). **Bit platnosti P** říká, zda položka adresáře platí.
- **Zápis:** **průběžný (write-through)** — zapíše se do cache i HP zároveň; **odložený (write-back)** — jen do cache, do HP až při uvolnění bloku, a to jen byl-li modifikován (řídí **Dirty bit**).
- **Náhradní (vyhazovací) strategie** — který blok uvolnit při výpadku: **LRU** (nejdéle nepoužito), **FIFO**, **random**, pseudo-LRU.

Vyšší stupeň asociativity → větší adresář (delší TAG, více srovnávačů) a složitější HW, ale méně výpadků.

> **Pozor (časté doptávání):** algoritmy pro **náhradu bloků v cache** nejsou totéž jako algoritmy pro **náhradu stránek** při stránkování (§4.5), ale jsou **principiálně podobné** (LRU/FIFO/…). Liší se měřítkem a tím, kdo je realizuje: výměnu v cache řeší **hardware** v ns, výměnu stránek řeší **OS** při výpadku stránky (page fault) v řádu ms.

### 5.4 TLB — cache principu aplikovaný na překlad adres (časté doptávání)
Plně/skupinově asociativní cache se v procesoru používá nejen pro data: **[[TLB]] (Translation Lookaside Buffer)** je malá asociativní cache **naposledy přeložených adres** (číslo stránky → číslo rámce), která urychluje překlad virtuálních adres a vyhne se opakovanému procházení stránkovací tabulky. Bývá **plně nebo n-cestně asociativní** — to je typická odpověď na „kde v procesoru najdeš plně asociativní paměť". Podrobně viz otázka **18 OSY**.

> *Doplnění nad rámec slidů:* **střední doba přístupu** $t_{\text{stř}} = h\cdot t_{\text{cache}} + (1-h)\cdot t_{\text{HP}}$, kde $h$ = hit rate. Druhy výpadků (3C): **povinný** (compulsory, první přístup), **kapacitní** (capacity), **konfliktní** (conflict). **Block size** (velikost bloku): větší blok těží z prostorové lokality, ale zvyšuje penalizaci při výpadku.

---

## 6. Co je potřeba na zkoušku znát

### Definice
von Neumannova vs Harvardská architektura; 5 částí počítače; PC, IR, SP, stavový registr; sběrnice (AB/DB/CB); instrukční cyklus (fetch–decode–execute); ISA, formát instrukce; 3 třídy ISA (střadačová/zásobníková/GPR); způsoby adresace; paměťová hierarchie, lokalita; SRAM vs DRAM; cache, mapování (přímé/asociativní), TAG/adr/offset, write-through/back, LRU.

### Souvislosti
- Proč hierarchie funguje = **lokalita** (časová/prostorová).
- von Neumannovo úzké hrdlo → cache, DMA.
- Tři třídy ISA = kompromis mezi délkou instrukce a počtem přístupů do paměti.
- Cache je asociativní (podle obsahu), adresa = TAG | adr | offset; vyšší asociativita = méně výpadků, ale dražší HW.

### Vzorce
- Bity adresy cache: blok = $\log_2$(velikost bloku); adr = $\log_2$(kapacita/stupeň) − bity bloku; TAG = zbytek.
- (Doplněk) $t_{\text{stř}}=h\,t_{\text{cache}}+(1-h)\,t_{\text{HP}}$.

### Typické doplňující otázky (doptávání)
> Z reálných zkušeností (Daňhel, Kohlík, Kubátová, Borecký, Dostál, Štěpanovský…). Tato otázka se skoro vždy **zúží** na jednu polovinu.
- **Rozdíl von Neumann × Harvard, proč PC používá von Neumanna a ne Harvarda?** → §1.1–1.3.
- **Vyjmenuj fáze instrukčního cyklu** (nezapomeň na **dekódování!**) → §2.
- **Co je přerušení, co se při něm děje, kdy může nastat, co se uloží na zásobník, jak se z něj vrací?** → §2.1.
- **Jak funguje zřetězení (pipelining), jaké má výhody, jak by to bylo bez něj?** → §2.2.
- **Jaké jsou třídy ISA a proč se dnes používá GPR / 2+ adresové instrukce?** → §3.2.
- **Proč funguje paměťová hierarchie** (lokalita) a **které paměti jsou v procesoru**; **proč jsou registry malé, když jsou rychlé?** → §4.1.
- **Co je asociativita cache, kde najdeš plně asociativní paměť (TLB)** a **jak/čím se nahrazují bloky v cache** (a čím se to liší od náhrady stránek)? → §5.
- Časté „zapomenuté" komponenty: **vstupně-výstupní rozhraní** (5. část počítače), **dekódování** ve fázích cyklu.
