---
tags: [otázka, kurz/DBS, otázka/5, todo]
---

# 5 — Relační DB, RA, SQL, IO (zkrácená verze)

## 1. Relační databáze

**[[Relace|Relace]]** = podmnožina $D_1 \times \dots \times D_n$, kde $D_i = \text{dom}(A_i)$. Schéma: $R(A_1:D_1, \dots, A_n:D_n)$.

| Relace | Tabulka |
|---|---|
| schéma relace | záhlaví |
| n-tice | řádek |
| atribut | sloupec |

Odlišnosti: v relaci **nezáleží pořadí**, **bez duplicit** (množina). 1NF = atomické atributy.

**Schéma RDB:** $(R, I)$ — relace + integritní omezení. **Přípustná RDB**: konkrétní relace splňující IO.

**[[Klíč-schématu|Klíč]]:** minimální podmnožina $K \subseteq A$ jednoznačně určující n-tici. Primární (PK) + alternativní.

**[[Cizí-klíč]] (FK):** $R[X] \subseteq S[Y]$, $Y$ klíč $S$. Referenční integrita.

**[[Integritní-omezení|IO]] — způsoby:** deklarativní (DDL, DBMS hlídá), procedurální server (trigger), procedurální klient (aplikace).

## 2. Relační algebra

**[[Relační-algebra|RA]]:** formální dotazovací jazyk; operandem celá relace, výsledek také relace, řetězí se. Zleva doprava, unární > binární, závorky.

**Minimální množina:** $\{\times, \text{sel}, \text{proj}, \to, \cup, \setminus\}$.

| Operace | Značení | Definice |
|---|---|---|
| Selekce | $R(\varphi)$ | $\{u \in R \mid \varphi(u)\}$ |
| Projekce | $R[C]$ | $\{u[C] \mid u \in R\}$ |
| Přejmenování | $R[A \to B]$ | změna jména |
| Θ-spojení | $R[t_1 \Theta t_2] S$ | kartéz + selekce |
| Přirozené | $R \ast S$ | spojení s rovností na průnik. atributech |
| Polospojení | $R \prec\ast S$ | $\{R \ast S\}[A]$ |
| Antijoin | $R \overline{\prec\ast} S$ | $R \setminus \{R \prec\ast S\}$ |
| Sjednocení | $R \cup S$ | množinové |
| Průnik | $R \cap S$ | množinové |
| Rozdíl | $R \setminus S$ | množinové |
| Kart. součin | $R \times S$ | množinové |
| Dělení | $R \div S$ | $R[X] \setminus \{\{R[X] \times S\} \setminus R\}[X]$ |

**Univerzální $\forall$ v RA:** přes $\forall x.P(x) \equiv \neg \exists x. \neg P(x)$, nebo přes dělení.

## 3. SQL — základ

**Rozdělení:**
- **DDL** — `CREATE`, `ALTER`, `DROP` (tabulky, pohledy, IO).
- **DML** — `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`.
- **DCL** — `GRANT`, `REVOKE`.
- **TCL** — `COMMIT`, `ROLLBACK`, `SAVEPOINT`.

### SELECT syntaxe
```sql
select [distinct] sloupce
from zdroj
[where φ]
[group by ...]
[having podmínka]
[order by ...];
```

**Pořadí vyhodnocení:** FROM → WHERE → GROUP BY → SELECT (agregace + projekce) → HAVING → ORDER BY.

**Spojení:** `JOIN ON` / `USING` / `NATURAL JOIN` / `CROSS JOIN` / `LEFT|RIGHT|FULL OUTER JOIN`. `USING` bezpečnější než `NATURAL` (explicitní sloupce), **ani jedno není v RA**. Outer join: chybějící sloupce druhé relace → `NULL`; `R.*`/`S.*` řídí, které sloupce zůstanou.

### NULL a 3-hodnotová logika
NULL = UNKNOWN, není 0 ani ''. Operace s NULL = NULL. `WHERE` propustí jen TRUE. Pomůcky: `IS [NOT] NULL`, `COALESCE(v1, v2, ...)`.

### Agregace
`COUNT`, `SUM`, `MAX`, `MIN`, `AVG`. `COUNT(*)` započítá NULL; `COUNT(A)` ne. `COUNT(∅)=0`, `SUM(∅)=NULL`. `COUNT(DISTINCT sl)`; rozsah `WHERE x BETWEEN a AND b`.

`GROUP BY` — v SELECT jen seskupovací sloupce + agregace. `HAVING` filtruje **po** agregaci.

### Poddotazy
- Nevztažený — sám o sobě smysl.
- Vztažený (correlated) — odkazuje na vnější dotaz.

Predikáty: `IN`, `EXISTS`, `ANY`/`SOME`, `ALL`, srovnání. U `EXISTS` nezáleží na obsahu `SELECT` poddotazu (jen ne/prázdnost); antijoin ≈ `NOT EXISTS`.

**Univerzální kvantifikace** v SQL: pomocí `NOT EXISTS (... NOT ...)`.

### Množinové operace
`UNION [ALL]`, `INTERSECT`, `EXCEPT` (Oracle `MINUS`). Kompatibilita: shodný počet a typy sloupců.

### DML
```sql
insert into T (sl1, sl2) values (...);
insert into T select ... from ...;
update T set sl = ... where ...;
delete from T where ...;
merge into target using source on (...) when matched then update ... when not matched then insert ...;
```

### Pohledy
```sql
create view V as select ... [with check option];
drop view V;
```
Virtuální relace (uložen SELECT). DML jen nad „simple view". Materialized view = fyzická kopie (refresh).

### DCL
```sql
grant select on T to user;
revoke insert on T from user;
```
Práva: `SELECT, INSERT, UPDATE, DELETE, ALTER, EXECUTE, INDEX, REFERENCE`.

### TCL
**[[Transakce]]** — session, COMMIT/ROLLBACK, SAVEPOINT. AUTOCOMMIT ON/OFF.

## 4. IO v DDL

```sql
create table T (
  sloupec typ [IO_sloupce ...],
  ...
  [IO_tabulky ...]
);
```

**IO sloupce:** `NOT NULL`, `DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `REFERENCES`, `CHECK`.

**IO tabulky:** totéž, navíc **složené** přes více sloupců. Pojmenování `CONSTRAINT jméno ...` — důrazně doporučeno.

```sql
create table Predstaveni (
  nazev_k varchar(20) not null,
  nazev_f varchar(20) not null,
  datum   date        not null,
  constraint predstaveni_pk primary key (nazev_k, nazev_f),
  constraint predstaveni_fk_kina  foreign key (nazev_k) references Kina,
  constraint predstaveni_fk_filmy foreign key (nazev_f) references Filmy
);
```

**Referenční integrita — akce:**
`NO ACTION` / `RESTRICT` / `CASCADE` / `SET NULL` / `SET DEFAULT`.

**Okamžik kontroly:** `IMMEDIATE` (default) vs. `DEFERRED` (konec transakce). Oracle: `DISABLE/ENABLE CONSTRAINT`.

**ALTER:**
```sql
alter table T add sloupec typ;
alter table T add constraint c check (...);
alter table T drop constraint c;
drop table T cascade;
```

**Nedeklarativní IO** (např. složité podmínky napříč tabulkami) → triggery nebo aplikace.

---

## Co odpovědět rychle

- **Relační databáze** = $(R, I)$. Relace = množina n-tic, schéma = struktura. 1NF, atomicita.
- **Klíč** = minimální podmnožina atributů jednoznačně určujících n-tici. PK + alternativní + cizí klíč (referenční integrita).
- **RA** — operandy/výsledky jsou relace; operace selekce, projekce, přejmenování, spojení (přirozené, Θ-, polo-, anti-), množinové, dělení. Min. množina $\{\times, \sigma, \pi, \to, \cup, \setminus\}$.
- **SQL** dělení: DDL / DML / DCL / TCL. SELECT je relačně úplný + agregace, OUTER JOIN, ORDER BY.
- **NULL** = UNKNOWN, propaguje se; jen TRUE v `WHERE` propustí řádek; `IS NULL`, `COALESCE`.
- **Agregace** + `GROUP BY` + `HAVING`. Pořadí: FROM-WHERE-GROUP-SELECT-HAVING-ORDER.
- **DDL IO sloupce:** `NOT NULL, DEFAULT, UNIQUE, PRIMARY KEY, REFERENCES, CHECK`. IO tabulky = totéž + složené.
- **Cizí klíč:** `REFERENCES T(sl) ON DELETE {NO ACTION|RESTRICT|CASCADE|SET NULL|SET DEFAULT}`. `IMMEDIATE` vs. `DEFERRED`.
- **TCL:** `COMMIT`, `ROLLBACK`, `SAVEPOINT`. AUTOCOMMIT pozor.
- Nedeklarativní IO → triggery / aplikace.
- **Doptávání (Hunka, v komisi):** chce konkrétní SQL syntax, ne teorii RA — joiny a **které sloupce zůstanou ve výstupu** (outer → NULL), `CHECK`, `ON DELETE CASCADE` (ne `DROP`), k čemu pohledy, (ne)vztažené poddotazy.
