---
tags: [otázka, kurz/DBS, otázka/6, todo]
---

# 6 — Transakce a ACID (zkrácená verze)

## 1. Transakce

**[[Transakce]]** = sekvence DML+SELECT, které logicky souvisejí, vnímáno jako jeden celek měnící stav DB. Před a po transakci je DB **konzistentní**, uvnitř může být dočasně nekonzistentní.

**Hranice:**
- Konec: explicitně `COMMIT` / `ROLLBACK`, implicitně konec session, nebo `SAVEPOINT` jako značka.
- Začátek: konec předchozí transakce / vznik session. Pozor na **AUTOCOMMIT** ON/OFF.

**Stavy:** Active → Partially Committed → Committed; Active → Failed → Aborted.

## 2. ACID

**[[ACID]]** — vlastnosti, které zajišťuje transakční zpracování:

| | Vlastnost | Význam | Implementace |
|---|---|---|---|
| **A** | Atomicity | celá nebo vůbec | žurnál + UNDO |
| **C** | Consistency | DB konzist. → DB konzist. | kontrola IO v DML, struktura transakce |
| **I** | Isolation/Independence | efekty neviditelné jiným transakcím | 2PL + stupně izolace |
| **D** | Durability | potvrzené efekty trvalé | žurnál + REDO + checkpoint |

## 3. Anomálie a stupně izolace

**[[Stupně-izolace|Anomálie]]:**
- **Ztráta aktualizace** — T2 přepíše update T1, který nebyl committed.
- **Dirty read** (dočasná aktualizace) — T2 čte data, která T1 napsala a později odvolá.
- **Neopakovatelné čtení** — T1 čte stejný řádek dvakrát, mezitím T2 update + commit.
- **Fantom** — totéž, ale T2 přidá/smaže řádky.

**Stupně izolace:**

| Stupeň | Dirty read | Non-repeatable | Fantom |
|---|---|---|---|
| read uncommitted | povoleno | povoleno | povoleno |
| read committed | zakázáno | povoleno | povoleno |
| repeatable read | zakázáno | zakázáno | povoleno |
| **serializable** (default standardu) | zakázáno | zakázáno | zakázáno |

V praxi se nejčastěji potkává `read committed`.

## 4. Uspořádatelnost

**Konfliktní operace:** $READ_i(A)$ vs. $WRITE_j(A)$ a $WRITE_i(A)$ vs. $WRITE_j(A)$. $READ_i$ vs. $READ_j$ jsou kompatibilní.

**Uspořádatelný rozvrh** = existuje sériový rozvrh s ním ekvivalentní (relativní pořadí konfliktních operací nad stejnými objekty je stejné).

**Precedenční graf** $G(U, H)$ — uzly = transakce; hrana $T_j \to T_k$ pokud:
- $T_j$ WRITE(A) před $T_k$ READ(A),
- $T_j$ READ(A) před $T_k$ WRITE(A),
- poslední WRITE(A) $T_j$ před posledním WRITE(A) $T_k$.

**Tvrzení:** Rozvrh je uspořádatelný ⟺ jeho precedenční graf je **acyklický**.

## 5. Uzamykací protokoly

**[[Uzamykací-protokol|2PL]]:**

**Dobře formovaná transakce:** zamyká před přístupem, nezamyká už zamknuté, neodmyká cizí, na konci nic zamčeného.

**Legální rozvrh:** objekt musí být zamknutý, kdykoli k němu transakce přistupuje; čeká, je-li zamčen jinde.

**Dvoufázová transakce:**
1. Fáze 1 (rostoucí) — jen zamyká.
2. Fáze 2 (klesající) — od prvního odemknutí už nezamyká.

**Tvrzení:** Jsou-li všechny transakce dobře formované a dvoufázové, **každý jejich legální rozvrh je uspořádatelný**.

**Striktní 2PL** — vše se odmyká až na konci (po COMMIT/ROLLBACK). Praktická varianta.

**Uváznutí (deadlock):** dvě transakce čekají na zámky, které drží druhá. Řešení: detekce (graf závislostí), nebo timeout → `ROLLBACK` jedné. Granularita: typicky řádek.

## 6. Zotavení (recovery)

**[[Žurnál]]** = sekvence změnových vektorů `<transID, blockID, old, new>` + COMMIT/ROLLBACK/checkpoint záznamy.

**Po pádu** (dvě fáze):
1. **Roll Forward** — REDO všech potvrzených, ale ne fyzicky uložených.
2. **Roll Back** — UNDO všech nedokončených.

**Chyba médií:**
- **Archivní mód** — backup + REDO ze žurnálu = Point In Time Recovery.
- **Nearchivní** — zpět k poslední záloze.

**Třídy chyb:** globální (pád systému, médií, deadlock) vs. lokální (logické v transakci → explicitní ROLLBACK).

---

## Co odpovědět rychle

- **Transakce** = logicky související sekvence DML; DB konzist. → uvnitř může být nekonzistentní → DB opět konzist.
- **A**tomicity — celá nebo vůbec → **žurnál + UNDO**.
- **C**onsistency — IO před i po → kontrola v DML.
- **I**solation — neviditelnost dílčích efektů → **2PL** + stupně izolace.
- **D**urability — potvrzené efekty trvalé → **žurnál + REDO + checkpoint**.
- **Stupně izolace** (4): read uncommitted < read committed < repeatable read < serializable; v praxi `read committed`.
- **Anomálie:** ztráta updatu, dirty read, non-repeatable read, fantom.
- **Uspořádatelnost** ⟺ acyklický precedenční graf.
- **2PL:** dobře formované + dvoufázové transakce → každý legální rozvrh uspořádatelný. Striktní 2PL = odmyká až na konci.
- **Deadlock** → detekce / timeout → ROLLBACK jedné.
- **Recovery po pádu:** Roll Forward (REDO commited) + Roll Back (UNDO nedokončené).
