---
aliases: [stupeň izolace, stupně izolace, stupni izolace, úroveň izolace, úrovně izolace, isolation level]
tags: [definice, kurz/DBS]
---

# Stupně izolace

## Anomálie souběžného zpracování

- **Ztráta aktualizace** (lost update) — $T_2$ přepíše update $T_1$, který ještě nebyl potvrzen.
- **Dočasná aktualizace / dirty read** — $T_2$ přečte data, která $T_1$ změnila ale neodevzdala (a později může odvolat).
- **Neopakovatelné čtení** (non-repeatable read) — $T_1$ provede dvakrát `SELECT` nad stejnými řádky, mezitím je $T_2$ změní a potvrdí.
- **Fantom** (phantom read) — totéž, ale $T_2$ řádky **přidá nebo smaže**, takže $T_1$ dostane jinou množinu řádků.

## Stupně izolace (SQL standard)

| Stupeň | Dirty read | Non-repeatable | Fantom |
|---|---|---|---|
| **read uncommitted** (0) | povoleno | povoleno | povoleno |
| **read committed** (1) | zakázáno | povoleno | povoleno |
| **repeatable read** (2) | zakázáno | zakázáno | povoleno |
| **serializable** (3) | zakázáno | zakázáno | zakázáno |

(Ztráta aktualizace je zakázána už od read committed.)

**Standard** nařizuje implicitně `serializable`. V praxi se nejčastěji potkává `read committed` (default PostgreSQL i Oracle).

**Poznámka:** PostgreSQL ani Oracle neumožní nižší úroveň než `read committed`. MySQL s engine InnoDB umí totéž co PostgreSQL/Oracle.

## Související

- [[Transakce]]
- [[ACID]]
- [[Uzamykací-protokol]]
