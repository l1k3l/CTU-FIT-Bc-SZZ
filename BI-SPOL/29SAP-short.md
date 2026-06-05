# 29SAP — Architektura, instrukční cyklus, ISA, paměti, cache (zkrácená verze)

## 1. Architektura
**[[Von-Neumannova-architektura|von Neumann]]:** data i instrukce ve **společné paměti** (nutný kontext). 5 částí: **ALU**, **řadič**, **hlavní paměť**, **vstup**, **výstup**; procesor = ALU + registry + řadič; propojeno **sběrnicí** (adresová/datová/řídicí). **Bottleneck** = společná sběrnice CPU↔paměť → cache, DMA.
**Harvard:** oddělená paměť instrukcí a dat (AVR).
**Registry:** PC (adresa instrukce, inkrementuje se), IR (registr instrukce), střadač/GPR, SP, stavový registr (C, V, N, Z…).

## 2. Instrukční cyklus
**fetch** (čtení instrukce do IR, PC++) → **dekódování** → **čtení operandů** → **provedení (execute)** → **uložení výsledku** → **přerušení?**. Řídí řídicí signály z řadiče; řadič = sekvenční obvod (obvodový / mikroprogramový), vhodný **Mooreův** automat.

## 3. ISA — soubor instrukcí
**[[Instrukční-soubor|ISA]]** = rozhraní HW/program; instrukce = *co, s čím, kam, kde dál*; formát = op. znak + operandy (1/2/3-adresové). Paměť bytová, big-/little-endian.

**Tři třídy:**
- **střadačová** — 1 registr; krátké instr., ale častá komunikace s pamětí.
- **zásobníková** — vrchol HW zásobníku; krátké programy, jen sekvenční přístup.
- **GPR** — sada registrů; rychlé, náhodný přístup, méně přístupů do paměti; složitější překladač. *(+ RISC vs CISC, load/store)*

**Adresace:** přímá (immediate / přímá adresa), nepřímá, relativní (PC), indexová/bázová, autoinkr./dekr., škálovatelná.
**Kategorie:** přesuny (MOV, LD/ST, PUSH/POP), arit./log. (ADD/ADC/SUB/CP, AND/OR/XOR), posuvy/rotace, skoky (JMP, podmíněné), CALL/RET, přerušení (RETI).

## 4. Paměťová hierarchie
**[[Paměťová-hierarchie|Hierarchie]]** (rychlost↑ kapacita↓ cena↑ směrem k CPU): registry → **cache (SRAM)** → hlavní paměť (**DRAM**) → disk/SSD → záloha. Funguje díky **lokalitě**: **časová** (znovupoužití) + **prostorová** (blízká data → přenos po **blocích**).
- **SRAM** = klopné obvody, rychlá, drahá, volatilní → cache; **DRAM** = dynamická, **refresh**, levná → hlavní paměť.
- dělení výběru: **adresovatelné (RAM)** vs **asociativní (CAM, podle klíče)**; ROM/EPROM/FLASH = nonvolatilní.
- paměťový obvod: matice + dekodér řádků + výběr sloupců (MUX); signály CS, WE, OE.
- *virtuální paměť:* stránkování (stránky pevné délky, tabulka stránek) / segmentace (proměnná délka, báze+offset).

## 5. Cache (skrytá paměť)
**[[Cache|Cache]]** = malá rychlá SRAM s kopiemi nejpoužívanějších položek HP; **průhledná**, **asociativní** přístup (podle obsahu), místo dekodéru má **adresář**.
**Adresa = TAG | adr (řádek) | výběr z bloku (offset).** Data po **blocích**.
**Mapování:** přímé (stupeň 1) · skupinově N-cestné · plně asociativní (paralelní porovnání, ~3× plocha).
**hit/miss:** čte se zároveň z cache i HP; bit platnosti P.
**Zápis:** write-through (cache + HP) / write-back (jen cache, do HP při uvolnění, Dirty bit). **Náhrada:** LRU, FIFO, random.

Bity: offset = log₂(blok), adr = log₂(kapacita/stupeň) − offset, TAG = zbytek.

---

## Co odpovědět rychle
- von Neumann = společná paměť dat+instrukcí; 5 částí; bottleneck → cache/DMA.
- Instrukční cyklus: fetch–decode–execute–(store)–přerušení.
- 3 třídy ISA: střadačová / zásobníková / GPR (kompromis délka instrukce ↔ přístupy do paměti).
- Hierarchie funguje díky lokalitě; cache asociativní, adresa = TAG/řádek/offset; write-through vs write-back, LRU.
