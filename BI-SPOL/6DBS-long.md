---
studyplan: true
etapa: "5 · DBS — Hunka"
qid: "6DBS"
examiner: "Hunka"
topic: "Transakce a jejich vlastnosti — ACID"
readiness: nezačato
tags: [otázka, kurz/DBS, otázka/6, todo]
---

# Transakce a jejich vlastnosti — ACID

> **Otázka SZZ:** Transakce a jejich vlastnosti - ACID.

Zdroje: BI-DBS přednáška 8 (Transakce a transakční zpracování, Valenta, FIT ČVUT).

---

## 1. Transakční zpracování — kontext

### 1.1 Dva základní požadavky na DBMS
1. **Chránit data** — ve smyslu odolnosti vůči různým haváriím serveru.
2. **Poskytnout korektní, rychlý a asynchronní přístup** většímu množství současně pracujících uživatelů.

### 1.2 Moduly DBMS
- **Řízení souběžného zpracování** (concurrency control) — zajišťuje, že každý uživatel vidí konzistentní stav databáze bez ohledu na to, že více uživatelů asynchronně přistupuje ke stejným údajům.
- **Zotavení z chyb** (recovery) — zajišťuje, že stav databáze není narušen v případě softwarové, systémové nebo mediální chyby.

---

## 2. Definice transakce

### 2.1 [[Transakce|Transakce]]

![[Transakce#Definice]]

### 2.2 Hranice transakce

![[Transakce#Hranice transakce]]

### 2.3 Stavový diagram transakce

![[Transakce#Stavový diagram]]

### 2.4 Příklady transakcí

**Převod peněz mezi účty:**
```sql
begin transaction;
  update Account set amount = amount - 100 where id = A;
  update Account set amount = amount + 100 where id = B;
commit;
```

Pokud druhý `UPDATE` selže, je nutné odvolat (`ROLLBACK`) první — jinak se peníze ztratí.

**Přihlášení studenta z termínu T1 na T2:**
IO: „student nesmí být přihlášen na dva budoucí termíny z jednoho předmětu."
- Pokud se zápis na T2 podaří, škrtne se T1.
- V rámci transakce je IO **dočasně porušeno** (student je krátkodobě na obou). Bez transakcí by mohlo selhat tak, že nebude přihlášen na žádný.

---

## 3. ACID — vlastnosti transakcí

![[ACID#A — Atomicity (atomicita)]]

![[ACID#C — Consistency (konzistence)]]

![[ACID#I — Isolation / Independence (nezávislost, izolace)]]

![[ACID#D — Durability (trvanlivost, persistence)]]

### 3.1 Vztah ACID ↔ moduly DBMS

![[ACID#Vztah ACID ↔ moduly DBMS]]

---

## 4. Zotavení z chyb (Atomicity + Durability)

### 4.1 Třídy chyb

**Globální (více transakcí):**
- Spadnutí systému (výpadek proudu) — ztráta výpočetní paměti.
- Systémové chyby (uváznutí, odumření klient–server komunikace) — neovlivní celou databázi.
- Mediální chyby (incident na disku) — ohrozí databázi nebo její část.

**Lokální (jedna transakce):**
- Logické chyby — odchytávány na úrovni transakce explicitním `ROLLBACK` (porušení IO, dělení nulou).

### 4.2 [[Žurnál|Transakční žurnál]]

![[Žurnál#Definice]]

![[Žurnál#K čemu slouží]]

### 4.3 Obnova po pádu

![[Žurnál#Obnova po pádu]]

**Synchronizační body** (checkpoints) = časové známky v žurnálu a v hlavičkách DB souborů; slouží k nalezení místa v žurnálu, odkud je třeba začít s rekonstrukcí.

### 4.4 Obnova z chyb médií

![[Žurnál#Obnova z chyby médií]]

---

## 5. Nezávislost (Isolation) — souběžné zpracování

### 5.1 Prokládání transakcí

Transakce $T_1, T_2, \dots, T_N$ se skládají z dílčích operací. **Rozvrh** = pořadí provádění dílčích operací v čase. Maximalizace paralelismu = úloha **rozvrhovače**.

**Sériový rozvrh:** operace každé transakce drží pohromadě. Pro $N$ transakcí existuje $N!$ různých sériových rozvrhů.

**Paralelní rozvrh:** operace mohou být prokládány.

### 5.2 Anomálie souběžného zpracování

![[Stupně-izolace#Anomálie souběžného zpracování]]

**Příklad — ztráta aktualizace:**

| T1 | T2 | Stav |
|---|---|---|
| READ(X) → x=80, x:=x-5 | | X=80, T1 chce 75 |
| | READ(X) → x=80, x:=x+4 | X=80, T2 chce 84 |
| WRITE(X) | | X=75 |
| | WRITE(X) | X=84 |

Přestože by „správný" výsledek byl 79 (80 − 5 + 4), je nakonec 84.

**Příklad — dočasná aktualizace (dirty read):**

| T1 | T2 |
|---|---|
| READ(X), x:=x−5, WRITE(X) | |
| | READ(X), x:=x+4, WRITE(X) |
| READ(Z) — chyba transakce, ROLLBACK | |

Po `ROLLBACK` T1 je update T2 založen na již odvolaných změnách.

### 5.3 [[Stupně-izolace|Stupně izolace]]

![[Stupně-izolace#Stupně izolace (SQL standard)]]

---

## 6. Uspořádatelnost rozvrhu

### 6.1 Kompatibilita operací

Definice uspořádatelnosti se zakládá na kompatibilitě operací READ a WRITE:
- Dvě operace jsou **konfliktní**, pokud výsledky jejich různého sériového volání nejsou ekvivalentní.

| | $READ_j(A)$ | $WRITE_j(A)$ |
|---|---|---|
| $READ_i(A)$ | + | − |
| $WRITE_i(A)$ | − | − |

(+ kompatibilní, − konfliktní)

### 6.2 Uspořádatelnost (vzhledem ke konfliktům)

**Definice:** Máme rozvrhy $S_1, S_2$ pro množinu transakcí $T = T_1, \dots, T_N$. Tyto rozvrhy jsou **ekvivalentní (vzhledem ke konfliktům)**, jsou-li splněny dvě podmínky:
- Vyskytuje-li se v $S_1$ `READ(A)` v $T_i$ a tato hodnota vznikla z `WRITE(A)` v $T_j$, potom totéž musí být zachováno v $S_2$.
- Vyvolá-li v $S_1$ poslední operaci `WRITE(A)` $T_i$, pak totéž musí být i v $S_2$.

Jinak řečeno: **relativní pořadí konfliktních operací nad stejnými objekty je v obou rozvrzích stejné**.

**Rozvrh je uspořádatelný**, jestliže existuje sériový rozvrh s ním ekvivalentní.

### 6.3 Precedenční graf

**Precedenční graf rozvrhu** $S$ je orientovaný graf $\{U, H\}$:
- $U = \{T_i \mid i = 1, 2, \dots, n\}$,
- $H = \{h_{ik}(A)\}$, kde hrana z $T_i$ do $T_k$ říká, že rozvrh může být ekvivalentní pouze takovému sériovému, ve kterém $T_i$ předchází $T_k$.

**Konstrukce:** Z uzlu $T_j$ povede hrana k uzlu $T_k$, jestliže:
- $T_j$ volá `WRITE(A)` před tím, než $T_k$ volá `READ(A)` (v $T_k$ se z DB čte hodnota, kterou napsala $T_j$),
- $T_j$ volá `READ(A)` před tím, než $T_k$ volá `WRITE(A)` (v $T_j$ se čte hodnota dříve, než ji $T_k$ změní),
- poslední `WRITE(A)` v $T_j$ předchází poslednímu volání `WRITE(A)` v $T_k$.

### 6.4 Testování uspořádatelnosti

**Tvrzení 1:** Rozvrh je uspořádatelný (ekvivalentní nějakému sériovému) **právě tehdy**, jestliže v jeho precedenčním grafu **neexistuje cyklus**.

**Tvrzení 2:** Dva rozvrhy jsou ekvivalentní, jestliže mají stejný precedenční graf.

**Poznámka:** Mohou existovat rozvrhy, které nejsou ekvivalentní žádnému sériovému (mají cyklus), a přesto produkují stejný výsledek jako některý sériový. Existují i alternativní definice korektnosti rozvrhů.

---

## 7. Uzamykací protokoly

### 7.1 Motivace
Testování uspořádatelnosti post-hoc je v praxi neúnosně drahé. Místo toho **konstruovat transakce podle pravidel** tak, aby každý jejich rozvrh byl uspořádatelný. Soustava takových pravidel = **protokol**.

### 7.2 Základní pojmy

**Jednoduchý model:** Objekt může být v daném čase uzamčen nejvýše jednou transakcí. Operace: `Lock(A)`, `Unlock(A)`. Uzamykající transakce smí provádět `READ` a `WRITE`.

![[Uzamykací-protokol#Základní pojmy]]

**Pozor:** Samotná legálnost rozvrhu nezaručuje uspořádatelnost.

### 7.3 [[Uzamykací-protokol|Dvoufázový uzamykací protokol (2PL)]]

![[Uzamykací-protokol#Dvoufázový uzamykací protokol (2PL)]]

**Důkaz uspořádatelnosti (idea):** Pro každou transakci existuje **bod uzamykání** (lock point) — okamžik posledního zamknutí. Lze ukázat, že v precedenčním grafu nemůže vzniknout cyklus, protože pořadí lock pointů určuje sériové pořadí ekvivalentního rozvrhu.

**Striktní 2PL** — všechny zámky se uvolní až po `COMMIT`/`ROLLBACK`. Toto je standardní praktická varianta (zaručuje navíc recoverable schedules).

### 7.4 Uváznutí (deadlock)

![[Uzamykací-protokol#Uváznutí (deadlock)]]

**Příklad:**
| T11 | T12 |
|---|---|
| LOCK(B), READ(B), WRITE(B) | |
| | LOCK(A), READ(A) |
| LOCK(A) — čeká → | LOCK(B) — čeká → |

Obě transakce čekají na zámek držený druhou. Detekce: **graf závislostí** nebo **timeout**.

### 7.5 Granularita zamykání

Obvykle na úrovni **řádků** (řádkové zámky). Lze i celé tabulky. Ve složitějších strukturách (XML, grafy, stromy) jsou nutné speciální stromové/grafové uzamykací protokoly.

---

## 8. Závěrečné shrnutí

| Vlastnost | Implementace |
|---|---|
| Atomicity | žurnál + UNDO; ROLLBACK ji zajišťuje explicitně |
| Consistency | algoritmy DML kontrolují IO; transakce může obsahovat více DML/SELECT pro postupné dosažení konzistence |
| Isolation | dvoufázový uzamykací protokol; volba stupně izolace připouští anomálie pro vyšší propustnost |
| Durability | žurnál + REDO + checkpointy |

Implementace v PostgreSQL a Oracle se liší — viz článek Laurenz Albe „Implementace a rozdíly transakčního zpracování v PostgreSQL a Oracle".

---

## 9. Co je potřeba na zkoušku znát

### Definice
- Transakce, hranice (COMMIT/ROLLBACK/SAVEPOINT), stavový diagram (A, PC, C, F, AB).
- ACID — atomicita, konzistence, nezávislost (izolace), trvanlivost.
- Transakční žurnál — formát změnových vektorů, COMMIT/ROLLBACK/checkpoint záznamy.
- Anomálie: ztráta aktualizace, dirty read, neopakovatelné čtení, fantom.
- Stupně izolace: read uncommitted, read committed, repeatable read, serializable.
- Rozvrh, sériový vs. paralelní, uspořádatelnost (vzhledem ke konfliktům).
- Konfliktní/kompatibilní operace.
- Precedenční graf.
- Zámek, dobře formovaná transakce, legální rozvrh.
- Dvoufázový uzamykací protokol (2PL); striktní 2PL.
- Uváznutí (deadlock).

### Klíčová tvrzení
- **Tvrzení o uspořádatelnosti:** rozvrh je uspořádatelný ⟺ jeho precedenční graf je acyklický.
- **Tvrzení o 2PL:** každý legální rozvrh dobře formovaných dvoufázových transakcí je uspořádatelný.
- Rozvrhy se stejným precedenčním grafem jsou ekvivalentní.
- Standard SQL nařizuje implicitní stupeň izolace `serializable`, v praxi se používá `read committed`.

### Mechanismy a struktury
- Transakční žurnál: formát, použití pro UNDO/REDO, checkpoint.
- Obnova po pádu: Roll Forward + Roll Back.
- Obnova z chyby médií: archivní mód (PITR) vs. nearchivní.
- Detekce deadlocku: graf závislostí nebo timeout.
- Granularita zamykání: řádek vs. tabulka.
