---
aliases: [podmíněná proměnná, podmíněné proměnné, podmíněnou proměnnou, podmíněných proměnných, condition variable]
tags: [definice, kurz/OSY]
---

# Podmíněná proměnná

## Definice
**Podmíněná proměnná** je blokující synchronizační nástroj svázaný se
**[[Zámek|zámkem]]**; pamatuje si vlákna, která jsou na ní blokovaná. Operace:

- `cond_wait(var, mutex)` — musí být volána se zamčeným `mutex`; **atomicky**
  uvolní `mutex` a zablokuje volající vlákno, dokud není proměnná opět
  signalizována. Po probuzení (návratu) je `mutex` opět zamčen.
- `cond_signal(var)` — odblokuje aspoň jedno z blokovaných vláken.

Důležité vlastnosti:
- **předchozí signály se neukládají** (signál na proměnnou, na níž nikdo nečeká,
  je ztracen),
- podmínka se testuje **v cyklu `while`** (ne `if`) — kvůli možnosti, že podmínku
  mezitím změnilo jiné probuzené vlákno, a kvůli **falešným probuzením**
  (*spurious wakeup*), kdy se vlákno probudí bez odpovídajícího `cond_signal()`.

Příklady: POSIX `pthread_cond_t` (`pthread_cond_wait/_signal/_broadcast`),
C++ `std::condition_variable`.

## Související
- [[Zámek]]
- [[Semafor]]
- [[Bariéra]]
