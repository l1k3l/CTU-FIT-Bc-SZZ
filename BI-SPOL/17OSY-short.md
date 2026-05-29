---
tags: [otázka, kurz/OSY, otázka/17, hotovo]
---

# 17 — Procesy a vlákna, synchronizace, uváznutí (zkrácená verze)

## 1. Procesy a vlákna

- **[[Proces]]:** instance spuštěného programu; entita, v níž jsou alokovány prostředky (paměť, vlákna, soubory, zámky). Jádro drží `task_struct` (PID, PPID, page table, deskriptory souborů). Adr. prostor: TEXT/DATA, heap, knihovny, stack.
- **[[Vlákno]]:** proud instrukcí, jednotka plánování CPU. Vlákna procesu **sdílí** adr. prostor a soubory; **vlastní** mají zásobník, čítač instrukcí, registry (kontext), prioritu. Sdílí `tgid`.
- **Vznik/zánik procesu:** `fork()` (kopie, vrací PID/0), `execve()` (přepíše adr. prostor), `wait()` (čeká na potomka), `exit()`. Sirotky adoptuje `init`.
- **Vznik/zánik vlákna:** `pthread_create`, `pthread_join`, `pthread_exit`. Konec `main()`/`exit()` ukončí celý proces.
- **Plánování:** preemptivní, vlákno dostane jádro na **časové kvantum**. **Přepínání kontextu** = uložit kontext, naplánovat, obnovit kontext.
- **Stavy:** Idle → Ready ↔ Running → Blocked → Ready; Running → Zombie → Free.

**[[Souběh]] (race condition):** výsledek závisí na rychlosti/prokládání vláken (např. `counter++` = load/inc/store). Náhodný výskyt.
**[[Kritická-sekce]]:** část programu se sdíleným prostředkem. **Vzájemné vyloučení:** max. 1 vlákno ve sdružené KS.

---

## 2. Synchronizační nástroje

**Úrovně:** HW (atomické instr. `cas`, `xchg`, `cmpxchg`), jádro OS, aplikace (POSIX).

### Aktivní čekání (busy waiting)
- Vlákno ve smyčce testuje sdílenou proměnnou. **Proměnná `lock` sama nestačí** — test + zápis nejsou atomické (dvě vlákna vstoupí).
- **Instrukce TSL** (test-and-set-lock): atomicky načte slovo a nastaví ho ≠ 0. `enter_region`: `tsl`, je-li bylo ≠ 0 → smyčka.
- **+** malá režie při krátkém čekání; **−** zatíží jádro na 100 %, **inverzní prioritní problém** (nízkoprior. vlákno v KS drží vysokoprior. vlákno).

### Blokující volání (pasivní čekání)
Vlákno přejde do **Blocked** (nezatěžuje CPU). **−** režie na změnu stavu; vyplatí se při delším čekání.
- **[[Zámek]] (mutex):** stav + fronta. `lock` (zamkne/blokuje), `unlock` (probudí 1).
- **[[Podmíněná-proměnná]]:** `cond_wait(var,mtx)` atom. odemkne mtx + blokuje; `cond_signal`. Signály se neukládají; test ve **`while`** (falešná probuzení).
- **[[Semafor]]:** čítač + fronta. `wait` (P): >0 → −1, jinak blokuj. `post` (V): čeká-li někdo probuď, jinak +1. Binární ≈ zámek.
- **[[Bariéra]]:** čítač síly; `wait` blokuje, dokud poslední nedosáhne 0 → probudí všechny.

---

## 3. Klasické synchronizační úlohy

Cíle: **správné** (bez chyb/uváznutí/livelocku/hladovění), **optimální** (souběžnost), **spravedlivé** (FIFO).

- **Producent-konzument:** fronta velikosti $N$. Semafory `mutex`, `empty` (init $N$), `full` (init 0). Pořadí: producent `wait(empty)`→`lock`→vlož→`unlock`→`post(full)`; konzument zrcadlově. (Opačné pořadí `wait`/`lock` → deadlock.)
- **Večeřící filozofové:** $N$ filozofů, $N$ vidliček, potřeba obou sousedních. Naivní (levá, pak pravá) → **deadlock**; „vrať a zkus znovu" → livelock. Optim.: mutex + $N$ semaforů + stavy (filozof jí, jen když oba sousedé nejedí). Max. $\lfloor N/2\rfloor$ jí současně.
- **Čtenáři-písaři:** čte víc současně, píše jen 1 (a nikdo nečte). Čítač čtenářů + `mutex_db` (1. čtenář zamkne, poslední odemkne) → optim., ale **písaři hladoví**. Spravedlivé = explicitní **FIFO fronta**.
- **Spící holič:** mutex + semafory `customers`, `barbers`. Optim., ale nespravedlivé (hladovění) bez FIFO fronty.

---

## 4. Uváznutí (deadlock)

- **Prostředky:** fyzické/logické; **odnímatelné** (paměť) vs. **neodnímatelné** (tiskárna). Sekvence: alokace → použití → uvolnění.
- **Alokační graf:** orient. graf vlákna/prostředky; hrana prostředek→vlákno (drží), vlákno→prostředek (čeká). **Smyčka = uváznutí.**
- **[[Uváznutí]]:** několik vláken čeká na událost, kterou může vyvolat jen jedno z čekajících → žádné nepokračuje.

**Coffmanovy podmínky (uváznutí ⇔ všechny 4 současně):**
1. **Vzájemné vyloučení** (prostředek nelze sdílet),
2. **Neodnímatelnost** (nelze násilím odebrat),
3. **Drž a čekej** (drží a žádá o další),
4. **Kruhové čekání** (smyčka čekání).

(1–3 nutné, 4 = samotné uváznutí. Nesplnění aspoň jedné ⇒ bez uváznutí.)

**Strategie:**
- **Pštrosí** — ignoruj (řeší uživatel). Většina univerzálních OS.
- **Prevence** — poruš Coffmanovu podmínku: drž-a-čekej (alokuj vše najednou) / kruhové čekání (alokuj prostředky ve vzrůstajícím očíslování).
- **Předcházení** — alokuj jen pokud zůstane **bezpečný stav** (existuje pořadí uspokojení všech). **Bankéřův algoritmus** (matice $Q$ požadavků, $A$ přidělení, $M=Q-A$, vektor volných $F$). Nutná znalost požadavků předem.
- **Detekce a zotavení** — připusť, detekuj (test s aktuálními požadavky $Q^c$ — neoznačená vlákna jsou uvázlá), zotav (ukončení vláken / rollback + restart).

---

## Co odpovědět rychle

- **Proces** = kontejner prostředků; **vlákno** = jednotka plánování, sdílí adr. prostor procesu.
- **Synchronizace:** aktivní čekání (TSL, plýtvá CPU) vs. blokující (mutex/semafor/cond. proměnná/bariéra, pasivní).
- **Semafor:** čítač; `wait`=P (−1/blokuj), `post`=V (probuď/+1).
- **Coffman:** vzáj. vyloučení, neodnímatelnost, drž-a-čekej, kruhové čekání.
- **Strategie:** pštrosí / prevence / předcházení (bankéř, bezpečný stav) / detekce + zotavení.
