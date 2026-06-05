---
aliases: [instrukční cyklus, instrukčního cyklu, instrukčním cyklu, fetch-decode-execute, cyklus instrukce]
tags: [definice, kurz/SAP]
---

# Instrukční cyklus

## Definice
**Instrukční cyklus** je opakovaný sled fází, podle kterého [[Von-Neumannova-architektura|řadič]] zpracovává jednu instrukci:

1. **Čtení instrukce** (fetch) — z adresy v **PC** se přečte instrukce do registru instrukce **IR**; PC se **inkrementuje**.
2. **Dekódování instrukce** — z IR se zjistí operace, počet a typ operandů.
3. **Čtení operandů** (operand fetch) — podle způsobu adresace.
4. **Provedení instrukce** (execute) — výpočet v ALU.
5. **Uložení výsledku** (write back).
6. **Přerušení?** — kontrola žádosti o přerušení, návrat na začátek cyklu.

Fáze 1–3 bývají označovány jako **fetch**, fáze 4–5 jako **execute**. Pohyb dat řídí **řídicí signály z řadiče**. Řadič je vhodné realizovat jako **Mooreův** [[Konečný-automat|automat]] (obvodový nebo mikroprogramový).

## Klíčové registry
**PC** (programový čítač — adresa instrukce), **IR** (registr instrukce), **střadač / GPR**, **SP** (ukazatel zásobníku), **stavový registr** (příznaky: carry, overflow, zero, negative…).

## Související
- [[Von-Neumannova-architektura]]
- [[Instrukční-soubor]]
