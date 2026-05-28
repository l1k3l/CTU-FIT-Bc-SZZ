---
aliases: [uzamykací protokol, uzamykacího protokolu, uzamykacím protokolem, dvoufázový protokol, 2PL, two-phase locking, zámek, zámku, zámkem, zámky]
tags: [definice, kurz/DBS]
---

# Uzamykací protokol

## Motivace

Testování uspořádatelnosti rozvrhu post-hoc je drahé. **Uzamykací protokol** = množina pravidel pro zamykání/odmykání objektů během transakce taková, že **každý** rozvrh dobře formovaných a protokolem řízených transakcí bude uspořádatelný.

## Základní pojmy

- **Lock(A)** / **Unlock(A)** — zámek na objektu $A$.
- **Legální rozvrh** — objekt je uzamknut transakcí, kdykoli k němu chce přistupovat; transakce nečeká pokud zámek nikdo nedrží.
- **Dobře formovaná transakce:**
  - zamyká objekt, chce-li k němu přistupovat,
  - nezamyká objekt, který už drží,
  - neodmyká objekt, který nezamkla,
  - na konci nezůstane žádný objekt zamčený.

## Dvoufázový uzamykací protokol (2PL)

**Definice (dvoufázová transakce):**
1. **Fáze 1 (rostoucí):** transakce pouze **zamyká**, nic neodmyká.
2. **Fáze 2 (klesající):** od prvního odemknutí **už nezamyká**, pouze odemyká.

**Tvrzení:** Jestliže všechny transakce množiny $T$ jsou **dobře formované** a **dvoufázové**, pak každý jejich **legální rozvrh** je **uspořádatelný**.

**Striktní 2PL:** všechno se odmyká až na konci transakce (po COMMIT/ROLLBACK). Toto je standardní praktická varianta.

## Uváznutí (deadlock)

Dvoufázový protokol může vést k **uváznutí** — dvě transakce čekají na zámky, které drží druhá.

**Řešení:** detekce přes **graf závislostí**, nebo **timeout** pro získání zámku. Vyřeší se `ROLLBACK`em jedné transakce.

## Granularita zamykání

Obvykle na úrovni **řádků**. Lze i celé tabulky. Ve složitějších modelech (XML, grafy) jsou nutné stromové/grafové protokoly.

## Související

- [[Transakce]]
- [[ACID]]
- [[Stupně-izolace]]
