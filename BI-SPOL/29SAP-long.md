---
tags: [otázka, kurz/SAP, otázka/29, hotovo]
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
**Oddělená paměť instrukcí a paměť dat** (adresují se nezávisle) → lze současně číst instrukci i data. Typická pro jednočipové mikropočítače (např. AVR).

### 1.3 Registry procesoru
- **PC (programový čítač)** — adresa zpracovávané instrukce; po jejím čtení se **inkrementuje** (pak ukazuje na následující).
- **IR / RI (registr instrukce)** — uchová přečtenou instrukci k dekódování (programátorovi nepřístupný).
- **střadač (akumulátor)** / **pracovní registry (GPR)**.
- **SP (ukazatel zásobníku)** — pro volání podprogramů a přerušení.
- **stavový registr (příznaky):** C (carry/přenos), V (overflow/přeplnění), N (záporný), Z (nulový), H (poloviční přenos), I (přerušení), …

### 1.4 Sběrnice
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

Fáze 1–3 = *fetch*, 4–5 = *execute*. Pohyb dat řídí **řídicí signály z řadiče**.

**Hierarchie řízení:** vyšší jazyk → (překladač) → jazyk symbolických instrukcí (JSI) → (assembler) → strojový kód → (procesor) → řídicí signály.

**Řadič** je sekvenční obvod realizující instrukční cyklus; bývá **obvodový** nebo **mikroprogramový** (dílčí mikrooperace uloženy jako **mikroinstrukce** v řídicí paměti = firmware). Pro synchronizaci vhodný **Mooreův** [[Konečný-automat|automat]].

> *Doplnění nad rámec slidů:* moderní procesory cyklus **zřetězují (pipelining)** — překrývají fáze sousedních instrukcí; brzdí je **hazardy** (datové/řídicí/strukturní).

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
- **Náhradní strategie:** **LRU** (nejdéle nepoužito), FIFO, random.

Vyšší stupeň asociativity → větší adresář (delší TAG, více srovnávačů) a složitější HW, ale méně výpadků.

> *Doplnění nad rámec slidů:* **střední doba přístupu** $t_{\text{stř}} = h\cdot t_{\text{cache}} + (1-h)\cdot t_{\text{HP}}$, kde $h$ = hit rate. Druhy výpadků (3C): **povinný** (compulsory, první přístup), **kapacitní** (capacity), **konfliktní** (conflict).

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
