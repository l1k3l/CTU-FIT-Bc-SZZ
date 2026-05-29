---
aliases: [proces, procesu, procesem, procesy, procesů, procesům, procesech]
tags: [definice, kurz/OSY]
---

# Proces

## Definice
**Proces** je instance spuštěného programu/aplikace — entita, v rámci které jsou
alokovány prostředky (paměť, **[[Vlákno|vlákna]]**, otevřené soubory, zámky,
semafory, sokety, …). Implicitně má každý proces jedno hlavní („main") výpočetní
vlákno.

Jádro OS udržuje pro každý proces řadu datových struktur nezbytných pro:
- **identifikaci**: číslo procesu (PID), číslo rodičovského procesu (PPID), …
- **bezpečnost**: identita procesu (USER, RUSER),
- **správu paměti**: informace pro překlad virtuálních adres (page table),
- **správu FS**: tabulku deskriptorů souborů.

V Linuxu je proces reprezentován strukturou `task_struct`. Při vzniku nového
procesu je část datových struktur **zděděna** od rodiče a část **nastavena** na
nové hodnoty.

## Související
- [[Vlákno]]
- [[Virtuální-paměť]]
- [[Souběh]]
