---
aliases: [žurnál, žurnálu, žurnálem, žurnály, transakční žurnál, transakčního žurnálu, transaction log, log soubor]
tags: [definice, kurz/DBS]
---

# Žurnál

## Definice

**Transakční žurnál** (transaction log) je log soubor obsahující sekvenci **změnových vektorů** ve formátu:

```
< transID, blockID, old data, new data >
```

Speciální vektory existují pro `COMMIT`, `ROLLBACK` a **checkpoint** (synchronizace database buffer cache s disk bloky; každý checkpoint má jednoznačné System Change Number, SCN).

## K čemu slouží

- **Atomicity** — pomocí `UNDO` lze vrátit změny nedokončené transakce.
- **Durability** — pomocí `REDO` lze obnovit potvrzené ale fyzicky neuložené transakce po pádu.

(ROLLBACK uvnitř session a tzv. read consistency obvykle používají jiné datové struktury, nikoliv žurnál.)

## Obnova po pádu

Dvě fáze:
1. **Roll Forward** — přehrání žurnálu (REDO všech potvrzených transakcí, jejichž data ještě nebyla zapsána na disk).
2. **Roll Back** — UNDO všech transakcí, které nebyly v době pádu dokončeny.

## Obnova z chyby médií

- **Archivní mód:** záložní kopie (Backup) + REDO ze žurnálu od okamžiku zálohy. Umožňuje **Point In Time Recovery (PITR)**.
- **Nearchivní mód:** návrat k poslední plné záloze; data po záloze ztracena.

## Implementace v Oracle

Žurnál má formu (minimálně) dvou souborů pevné velikosti, které se **cyklicky přepisují** (log switch).

## Související

- [[Transakce]]
- [[ACID]]
