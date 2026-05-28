---
aliases: [transakce, transakci, transakcí, transakcím, transakcemi, transakcích]
tags: [definice, kurz/DBS]
---

# Transakce

## Definice

**Transakce** je sekvence akcí (DML + SELECT příkazů) nad databází, které spolu **logicky souvisí**, tj. je vhodné je vnímat jako jeden celek měnící stav databáze.

```
 čas  začátek T_i     průběh T_i      konec T_i
 ─────┬───────────────────────────────┬─────────
      │  DB konzistentní              │ DB musí
      │  → DB může být dočasně        │ být opět
      │    nekonzistentní             │ konzistentní
```

Transakční zpracování zajišťuje (dodržením vlastností **ACID**), že po skončení transakce (úspěšném i neúspěšném) zůstane databáze v konzistentním stavu — tj. splňuje všechna deklarovaná **integritní omezení**.

## Hranice transakce

**Konec:**
- Explicitní: `COMMIT` (potvrzení) nebo `ROLLBACK` (zrušení).
- Implicitní: ukončení session (klient určí commit/rollback).
- `SAVEPOINT` definuje značku uvnitř transakce, ke které lze vztáhnout `ROLLBACK`.

**Začátek:** typicky skončením předchozí transakce nebo vznikem session. Pozor na **AUTOCOMMIT**: ON = každý DML potvrzen automaticky; OFF = nutný explicitní commit/rollback.

## Stavový diagram

```
        ┌──────►  PC ──────► C
   A ───┤        │
        └──────► F ──────► AB
```

- **A**ctive — od začátku, probíhají DML.
- **P**artially **C**ommitted — po poslední operaci, před COMMIT.
- **C**ommitted — po úspěšném `COMMIT`.
- **F**ailed — nelze pokračovat.
- **AB**orted — po `ROLLBACK`, databáze v původním stavu.

## Související

- [[ACID]]
- [[Stupně-izolace]]
- [[Uzamykací-protokol]]
- [[Žurnál]]
- [[Integritní-omezení]]
