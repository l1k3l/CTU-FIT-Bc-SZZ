---
aliases: [TLB, translation lookaside buffer, translation look-aside buffer]
tags: [definice, kurz/OSY]
---

# TLB (Translation Lookaside Buffer)

## Definice
**TLB** (*Translation Lookaside Buffer*) je rychlá vyrovnávací paměť v CPU/**[[MMU]]**
sloužící k **urychlení překladu** virtuálních adres na fyzické. Je implementována
jako *n*-cestná cache (paměť s omezeným stupněm asociativity) a uchovává informace o
**naposledy přeložených** virtuálních adresách (dvojice *číslo stránky → číslo
rámce*).

Počet položek TLB je výrazně menší než počet stránek/rámců. Položka obsahuje:
- *valid* bit (zda je položka platná),
- číslo stránky a číslo rámce,
- **ASID** (*address space ID* — identifikátor adresního prostoru),
- řídicí bity (de facto kopie řídicích bitů z řádku ST poslední úrovně).

Při překladu se nejdřív prohledá TLB:
- **TLB hit** ⇒ rychlý překlad bez přístupu do **[[Stránkovací-tabulka|ST]]**,
- **TLB miss** ⇒ překlad přes ST (a aktualizace TLB).

## Související
- [[MMU]]
- [[Stránkovací-tabulka]]
- [[Stránkování]]
