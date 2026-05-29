---
aliases: [souběh, souběhu, časově závislá chyba, časově závislé chyby, časově závislých chyb, race condition, race conditions]
tags: [definice, kurz/OSY]
---

# Souběh (časově závislá chyba)

## Definice
**Souběh** (*race condition*, časově závislá chyba) je situace, kdy dvě nebo více
**[[Vlákno|vláken]]** používá společné sdílené prostředky (sdílené proměnné,
soubory, …) a **výsledek deterministického algoritmu je závislý na rychlosti**
jednotlivých vláken, tj. na pořadí, v jakém k prostředkům přistupují.

Klíčové vlastnosti:
- výsledek je nedeterministický, přestože jednotlivá vlákna vykonávají
  deterministický kód,
- chyby vykazují **náhodný výskyt** ⇒ špatně se detekují (ladicí nástroje jako
  Valgrind pomohou, ale nejsou spolehlivé),
- předchází se jim **správným návrhem** paralelního programu — zajištěním
  vzájemného vyloučení v [[Kritická-sekce|kritických sekcích]].

## Související
- [[Kritická-sekce]]
- [[Uváznutí]]
- [[Vlákno]]
