---
aliases: [instrukční soubor, instrukčního souboru, instrukční sada, soubor instrukcí, ISA, architektura souboru instrukcí, instruction set]
tags: [definice, kurz/SAP]
---

# Instrukční soubor (ISA)

## Definice
**ISA (Instruction Set Architecture)** = architektura souboru instrukcí — rozhraní mezi hardwarem a programem. **Instrukce** je příkaz zakódovaný jako číslo, který určuje *co* (operace), *s čím* (operandy), *kam* uložit výsledek a *kde* pokračovat. Operand bývá určen **adresou**, ne hodnotou.

**Formát instrukce:** operační znak + operandy; podle počtu adres 1-/2-/3-adresové.

## Tři základní třídy
- **Střadačová (akumulátorová):** jeden pracovní registr (střadač). Krátké instrukce, jednoduchý HW, ale **častá komunikace s pamětí**.
- **Zásobníková:** ALU pracuje s vrcholem HW zásobníku; krátké programy, ale jen sekvenční přístup.
- **GPR (registry pro všeobecné použití):** registry rychlejší než paměť, náhodný přístup; složitější překladač.

## Způsoby adresace
Přímá (implicitní / immediate / přímá adresa), nepřímá, relativní (vůči PC/registru), indexová, bázová, autoinkrementace/dekrementace, škálovatelná.

## Kategorie instrukcí
Přesuny dat (MOV, LD/ST, PUSH/POP), aritmetické a logické (ADD/SUB/CP, AND/OR/XOR), posuvy a rotace, skoky (nepodmíněné/podmíněné), volání podprogramů (CALL/RET) a přerušení (RETI).

## Související
- [[Instrukční-cyklus]]
- [[Von-Neumannova-architektura]]
