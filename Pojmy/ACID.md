---
aliases: [ACID, atomicita, konzistence, izolace, nezávislost, trvanlivost, atomicity, consistency, independence, isolation, durability]
tags: [definice, kurz/DBS]
---

# ACID

Čtyři vlastnosti, které musí garantovat **transakční zpracování**, aby zajistilo konzistenci databáze.

## A — Atomicity (atomicita)

Transakce musí proběhnout **buď celá, nebo vůbec**. Žádné částečné efekty se v databázi neprojeví — pokud transakce skončí chybou nebo `ROLLBACK`em, všechny dosavadní změny se odvolají.

**Implementace:** **[[Žurnál]]** (transakční log) + operace `UNDO` a `REDO`.

## C — Consistency (konzistence)

Transakce transformuje databázi z **konzistentního stavu do jiného konzistentního stavu** (uvnitř transakce smí být DB dočasně nekonzistentní). Po skončení musí být splněna všechna integritní omezení.

**Implementace:** automatická kontrola **[[Integritní-omezení|integritních omezení]]** v algoritmech DML operací; transakce může seskupit více DML/SELECT pro postupné dosažení konzistence.

## I — Isolation / Independence (nezávislost, izolace)

Dílčí efekty jedné (probíhající) transakce nejsou viditelné jiným transakcím. Souběžné transakce se navzájem nesmí ovlivnit „špatným způsobem".

**Implementace:** dvoufázový **[[Uzamykací-protokol]]** (2PL) + dobře formované transakce. Volbou **[[Stupně-izolace|stupně izolace]]** lze připustit některé anomálie pro vyšší propustnost.

## D — Durability (trvanlivost, persistence)

Efekty úspěšně **potvrzené** transakce (COMMIT) jsou **trvale uloženy** v databázi — odolné vůči pádu systému, výpadku napájení, ztrátě bufferu apod.

**Implementace:** **[[Žurnál]]** + checkpointy + `REDO` po restartu.

## Vztah ACID ↔ moduly DBMS

| Vlastnost | Zajišťuje |
|---|---|
| Atomicity | recovery modul (žurnál, UNDO) |
| Consistency | DML enforcement + IO + struktura transakce |
| Isolation | concurrency control (uzamykání) |
| Durability | recovery modul (žurnál, REDO, checkpoint) |

## Související

- [[Transakce]]
- [[Žurnál]]
- [[Uzamykací-protokol]]
- [[Stupně-izolace]]
