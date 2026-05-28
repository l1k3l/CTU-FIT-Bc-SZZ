---
aliases: [integritní omezení, integritního omezení, integritním omezením, integritních omezení, IO]
tags: [definice, kurz/DBS]
---

# Integritní omezení

## Definice

**Integritní omezení (IO)** jsou tvrzení, která musí být splněna v každé **přípustné relační databázi**. Tvoří součást schématu databáze $(R, I)$.

## Způsoby vyjádření IO

1. **Deklarativní** — při vytvoření schématu (DDL), kontroluje automaticky DBMS:
   - `PRIMARY KEY`, `FOREIGN KEY` (referenční integrita),
   - `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`.
2. **Procedurální na straně serveru** — triggery, stored procedures.
3. **Procedurální na straně klienta** — aplikační logika.

## Integritní omezení v SQL DDL

**Omezení sloupce** (column constraint):
- `NOT NULL` — hodnota nesmí být `NULL`.
- `DEFAULT hodnota` — implicitní hodnota, pokud není dodána.
- `UNIQUE` — všechny hodnoty musí být různé (NULL může vícekrát).
- `PRIMARY KEY` — primární klíč (= `UNIQUE` + `NOT NULL`).
- `REFERENCES` (cizí klíč).
- `CHECK (podmínka)` — libovolný booleovský výraz na úrovni řádku.

**Omezení tabulky** (table constraint): stejné typy, navíc **složená** omezení nad více sloupci. `NOT NULL` je speciální případ `CHECK`.

**Pojmenování IO:** `CONSTRAINT jméno_io …` — usnadňuje pozdější `ALTER TABLE … DROP CONSTRAINT`.

## Okamžik kontroly

- **IMMEDIATE** (default) — kontrola po každém DML.
- **DEFERRED** — kontrola odložená na konec transakce.
- V Oracle navíc `DISABLE/ENABLE CONSTRAINT`.

## Související

- [[Klíč-schématu]]
- [[Cizí-klíč]]
- [[Relace]]
- [[Transakce]]
