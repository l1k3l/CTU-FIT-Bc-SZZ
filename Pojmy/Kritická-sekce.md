---
aliases: [kritická sekce, kritické sekce, kritickou sekci, kritických sekcí, kritickými sekcemi, critical section]
tags: [definice, kurz/OSY]
---

# Kritická sekce

## Definice
**Kritická sekce** je část programu, kde vlákno používá sdílené prostředky (např.
sdílenou proměnnou, sdílený soubor).

- **Sdružené kritické sekce** — kritické sekce dvou (nebo více)
  **[[Vlákno|vláken]]**, které se týkají **stejného** sdíleného prostředku.
- **Vzájemné vyloučení** (*mutual exclusion*) — vláknům není dovoleno sdílet
  stejný prostředek ve stejném čase ⇒ vlákna se **nesmí nacházet ve stejné
  sdružené kritické sekci současně**.

Vzájemné vyloučení lze zajistit aktivním čekáním (busy waiting) nebo blokujícími
nástroji ([[Zámek|zámky]], [[Semafor|semafory]], [[Podmíněná-proměnná|podmíněnými proměnnými]]).

## Související
- [[Souběh]]
- [[Zámek]]
- [[Semafor]]
