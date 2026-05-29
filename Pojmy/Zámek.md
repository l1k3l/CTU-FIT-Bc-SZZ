---
aliases: [zámek, zámku, zámkem, zámky, zámků, mutex, mutexu, mutexem, mutexy]
tags: [definice, kurz/OSY]
---

# Zámek (mutex)

## Definice
**Zámek** (často *mutex*, MUTual EXclusion lock) je blokující synchronizační
nástroj pro vzájemné vyloučení. Pamatuje si:
- svůj stav (zamčený / odemčený),
- množinu vláken, která jsou na něm blokovaná.

Atomické operace:
- `mutex_lock` — je-li zámek odemčený, zamkne ho; je-li zamčený, **zablokuje**
  volající vlákno (přejde do stavu *Blocked* a přestane mu být přidělováno CPU
  ⇒ *pasivně* čeká),
- `mutex_unlock` — je-li nějaké vlákno blokované, probudí jedno z nich; jinak
  zámek odemkne.

Příklady: POSIX `pthread_mutex_t` (`pthread_mutex_lock/_unlock/_trylock`),
C++ `std::mutex`, `std::lock_guard`.

## Související
- [[Kritická-sekce]]
- [[Semafor]]
- [[Podmíněná-proměnná]]
