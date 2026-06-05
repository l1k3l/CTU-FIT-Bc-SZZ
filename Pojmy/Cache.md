---
aliases: [cache, cache paměť, skrytá paměť, skryté paměti, skrytou pamětí, vyrovnávací paměť, rychlá vyrovnávací paměť, mezipaměť]
tags: [definice, kurz/SAP]
---

# Cache

## Definice
**Cache (skrytá paměť)** je malá rychlá paměť (SRAM) vložená mezi procesor a hlavní paměť, která obsahuje **kopie nejčastěji používaných položek** hlavní paměti. Funguje díky [[Paměťová-hierarchie#Princip lokality|principu lokality]] a je pro programátora **zcela průhledná**. Přístup je **asociativní** — ne podle adresy, ale podle **obsahu (klíče)**; místo adresového dekodéru má **adresář**.

## Mapování (organizace)
Adresa se dělí na tři části: **TAG (podklíč)** | **adr (řádek/index)** | **výběr z bloku (offset)**. Data se uchovávají po **blocích (řádcích)**.
- **Přímo mapovaná** (stupeň asociativity 1) — položka jen na jednom místě; realizovatelná běžnou RAM.
- **Skupinově (N-cestně) asociativní** — položka na jednom z $N$ míst.
- **Plně asociativní** — položka kdekoli (stupeň asociativity = kapacita); paralelní porovnání se všemi položkami adresáře, ale ~3× větší plocha čipu.

## Činnost a strategie
- **Zásah (hit)** / **výpadek (miss):** čtení se zahájí současně z cache i HP; při zásahu se cyklus HP nedokončí.
- **Zápis:** **průběžný (write-through)** — zapíše se do cache i HP zároveň; **odložený (write-back)** — jen do cache, do HP až při uvolnění bloku (řídí **Dirty bit**).
- **Náhradní strategie:** **LRU** (nejdéle nepoužito), FIFO, random.
- **Bit platnosti (P)** označuje, zda položka adresáře obsahuje platná data.

Vyšší stupeň asociativity → větší adresář a složitější HW (více srovnávacích obvodů), ale méně výpadků.

## Související
- [[Paměťová-hierarchie]]
- [[Von-Neumannova-architektura]]
