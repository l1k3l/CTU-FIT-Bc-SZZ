---
aliases: [vlákno, vlákna, vláknu, vláknem, vláken, vláknům, vláknech]
tags: [definice, kurz/OSY]
---

# Vlákno

## Definice
**Vlákno** je výpočetní entita (proud instrukcí), které je přidělováno jádro CPU.
Historicky se nazývalo *light-weight process* (LWP).

Vlákna vytvořená v rámci jednoho **[[Proces|procesu]]** **sdílí většinu prostředků**
procesu — v Linuxu např. `mm_struct` (adresní prostor), `files_struct` (otevřené
soubory), `signal_struct`. **Vlastní** má každé vlákno:
- zásobník (lokální proměnné, historie volání),
- čítač instrukcí a aktuální hodnoty registrů (kontext),
- plánovací informace (priorita, čas na CPU).

Jádro udržuje pro každé vlákno mj. číslo vlákna (TID; na Linuxu PID), zásobník a
kontext. Vlákna jednoho procesu sdílí společné `tgid` (thread group ID).

## Související
- [[Proces]]
- [[Kritická-sekce]]
- [[Souběh]]
