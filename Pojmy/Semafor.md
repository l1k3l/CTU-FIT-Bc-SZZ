---
aliases: [semafor, semaforu, semaforem, semafory, semaforů, semaforům, semaphore]
tags: [definice, kurz/OSY]
---

# Semafor

## Definice
**Semafor** je blokující synchronizační nástroj, který obsahuje:
- **celočíselný čítač**,
- množinu vláken, která jsou na něm blokovaná.

Atomické operace:
- `sem_init(sem, value)` — nastaví čítač na `value` a vyprázdní frontu čekajících,
- `sem_wait(sem)` (operace **P**) — je-li čítač > 0, sníží ho o 1; jinak volající
  vlákno **zablokuje** a uloží do fronty,
- `sem_post(sem)` (operace **V**) — čeká-li nějaké vlákno ve frontě, jedno z nich
  probudí; jinak čítač **zvětší o 1**.

**Binární semafor** (inicializovaný na 1) slouží k vzájemnému vyloučení (≈
[[Zámek|zámek]]); **obecný semafor** typicky **počítá prostředky** (např. volná/plná
místa ve frontě u úlohy producent-konzument).

Příklady: Unix System V (`semget`, `semop`), POSIX `sem_t` (`sem_wait`, `sem_post`).

## Související
- [[Zámek]]
- [[Kritická-sekce]]
- [[Podmíněná-proměnná]]
