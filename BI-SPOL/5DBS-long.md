---
studyplan: true
etapa: 5 · DBS — Hunka
qid: 5DBS
examiner: Hunka
topic: Relační DB, relační algebra, SQL (SELECT/DDL/DML/DCL/TCL), integritní omezení, ER→relační
readiness: in progress
tags:
  - otázka
  - kurz/DBS
  - otázka/5
  - todo
---

# Relační databáze, RA, SQL, integritní omezení

> **Otázka SZZ:** Relační databáze, dotazování v relační algebře, základní koncepce jazyka SQL (SELECT, DDL, DML, DCL, TCL), vyjádření integritních omezení v DDL.

Zdroje: BI-DBS přednášky 3 (Relační model a RA), 4 (SELECT 1), 6 (SELECT 2), 7 (TCL, DML, DDL, DCL) (Valenta, FIT ČVUT).

---

## 1. Relační databáze

### 1.1 Motivace
**Relační model dat** (Codd, 1970) je formální abstrakce textových souborů. Přináší:
- relační algebru a relační kalkul (dotazovací prostředky),
- metodiku pro posuzování kvality relačního schématu,
- metodiku pro návrh kvalitního relačního schématu (normalizace).

### 1.2 [[Relace|Relace]] — pojmy

![[Relace#Definice]]

**Intuitivně:** relace = tabulka, schéma relace = záhlaví tabulky. Tabulka ale **není** přesně relace:

![[Relace#Relace vs. tabulka]]

### 1.3 Schéma relační databáze

![[Relace#Schéma relační databáze]]

### 1.4 [[Klíč-schématu|Klíč schématu]]

![[Klíč-schématu#Definice]]

![[Klíč-schématu#Vlastnosti]]

**Příklad:** Pokud $R(\underline{a}, b, c)$, nemůže již být $R(a, \underline{b}, c)$ — minimální podmnožinou $\{a, b\}$ by pak nebyla.

### 1.5 [[Integritní-omezení|Integritní omezení]]

![[Integritní-omezení#Způsoby vyjádření IO]]

Konkrétní syntaxe IO v SQL DDL je v sekci 5 této otázky.

### 1.6 Dotaz nad schématem

**Dotaz** je výraz, který nad schématem $S$ vrací odpověď se schématem $T$. Vlastnosti:
- definičním oborem jsou všechna úložiště se schématem $S$,
- oborem hodnot relace se schématem $T$,
- data odpovědi pocházejí z databáze,
- odpověď nezávisí na fyzickém uložení dat.

**Dotazovací jazyk** je množina všech použitelných výrazů pro konstrukci dotazu.

---

## 2. Dotazování v relační algebře

**[[Relační-algebra|Relační algebra (RA)]]** je formální dotazovací jazyk nad relačním modelem.

### 2.1 Charakteristika
- Operand je vždy **celá relace**, výsledek je relace → lze řetězit.
- Vyhodnocuje se **zleva doprava**, unární operace mají přednost před binárními, prioritu mění **složené závorky**.
- RA řeší **pouze dotazování**, nikoli DML a DDL.
- RA byla **vzorem pro návrh SQL SELECT**. SELECT má dnes větší vyjadřovací možnosti (agregace, vnější spojení, řazení, …).
- Dotazovací jazyk, který umí vyjádřit každý výraz RA, je **relačně úplný** (např. SQL SELECT).

### 2.2 Selekce a projekce

**Selekce** (restrikce) — výběr n-tic splňujících podmínku $\varphi$:
$$R(\varphi) =_{def} \{u \mid u \in R \land \varphi(u)\}.$$
$\varphi$ je složený logický výraz typu $t_1 \Theta t_2$ nebo $t \Theta a$, kde $\Theta \in \{<, >, =, \le, \ge, \ne\}$ a $a$ je konstanta.

**Projekce** — výběr sloupců $C \subseteq A$:
$$R[C] =_{def} \{u[C] \mid u \in R\}.$$

**Překlad do SQL:**
```sql
-- R(φ)[A1,...,Aj]
select distinct A1, ..., Aj from R where φ;
```

### 2.3 Spojení

**Obecné Θ-spojení** $R[t_1 \Theta t_2] S$ s výsledkem $T(C)$:
$$R[t_1 \Theta t_2]S =_{def} \{u \mid u[A] \in R \land u[B] \in S \land u.t_1 \Theta u.t_2\},$$
kde $\Theta \in \{<, >, =, \le, \ge, \ne\}$. $C$ je zřetězením $A$ a $B$ — spol. atributy se opakují, je nutno přejmenovat.

**Přirozené spojení** $R \ast S$ s výsledkem $T(C)$, kde $C = A \cup B$ a výběr n-tic je dán **rovností na všech průnikových atributech** $A$ a $B$.

**Polospojení (semi-join)** — redukce $R$ na n-tice spojitelné se $S$:
- levé Θ-polospojení $R \prec t_1 \Theta t_2 \,S =_{def} \{R[t_1 \Theta t_2]S\}[A]$,
- pravé $R[t_1 \Theta t_2]\!\succ S =_{def} \{R[t_1 \Theta t_2]S\}[B]$,
- přirozené $R \prec\ast S =_{def} \{R \ast S\}[A]$.

Polospojení lze chápat jako **„syntaktickou zkratku"** za spojení následované projekcí (na $A$ resp. $B$); skutečná implementace bývá efektivnější než spojení + selekce.

**Antijoin** $R \overline{\prec\ast} S =_{def} R \setminus \{R \prec\ast S\}$ — n-tice $R$, které **nejsou** spojitelné s žádnou n-ticí $S$. Používá se v **query executoru** — objevuje se v **prováděcích plánech** SQL dotazů při vyhodnocení klauzule **`NOT EXISTS`**.

**Přejmenování** $R[A_1 \to B_1]$ — atribut $A_1$ přejmenován na $B_1$.

**Překlad do SQL:**
```sql
-- R [t1 Θ t2] S
select distinct * from R join S on (R.t1 Θ S.t2);

-- R * S
select distinct * from R natural join S;

-- R ≺* S  (semi-join, levé)
select distinct R.* from R natural join S;
```

### 2.4 Množinové operace
- **Sjednocení** $R \cup S$,
- **Průnik** $R \cap S$,
- **Rozdíl** $R \setminus S$ (též $R - S$),
- **Kartézský součin** $R \times S$.

V SQL: `UNION`, `INTERSECT`, `EXCEPT` (Oracle: `MINUS`), `CROSS JOIN`.

### 2.5 Relační dělení
$R \div S$ pro $R(X, Y), S(Y)$ — všechny hodnoty $x \in R[X]$, které v $R$ tvoří dvojici s **každým** $y \in S$.

**Definice přes minimální množinu operací:**
$$R \div S =_{def} R[X] \setminus \{\{R[X] \times S\} \setminus R\}[X].$$

**Idea:** zkoušíme **diskvalifikovat** $x$ — najít $y \in S$ takové, že $(x, y) \notin R$. Co se diskvalifikovat nepodaří, patří do výsledku.

### 2.6 Minimální množina operací

$$\{\times, \text{selekce}, \text{projekce}, \text{přejmenování} (\to), \cup, \setminus\}.$$

Ostatní operace jsou definované pomocí těchto (např. $R \cap S = R \setminus (R \setminus S)$, přirozené spojení $\ast$ pomocí $\times$, selekce, projekce).

### 2.7 Univerzální kvantifikátor
RA nemá $\forall$. Vyjádří se přes $\exists$:
$$\forall x. P(x) \equiv \neg \exists x. \neg P(x).$$

**Příklad (D8):** „Kina, kde dávají všechny filmy s Brandem."
- $K := MA\_NA\_PROGRAMU[NazevK]$ (kina něco hrají),
- $U := K \times \{FILM(Herec='Brando')[JmenoF]\}$ (univerzum párů),
- $R := MA\_NA\_PROGRAMU[NazevK, JmenoF]$ (reálné páry),
- $N := U \setminus R$ (nerealizované dvojice),
- $B := N[NazevK]$ (kina, která nehrají některý Brandův film),
- výsledek: $K \setminus B$.

Alternativně přes dělení: $MA\_NA\_PROGRAMU[NazevK, JmenoF] \div \{FILM(Herec='Brando')[JmenoF]\}$.

### 2.8 Příklad — komplexní výraz
„Herci, kteří hrají ve filmech promítaných v kině Mír."

RA:
$$\{\{MA\_NA\_PROGRAMU(NazevK='Mir')[JmenoF, Datum]\} \ast FILM\}[Herec \to Hvezda].$$

SQL ekvivalent:
```sql
select distinct herec as hvezda
from ma_na_programu natural join film
where nazevk = 'Mir';
```

---

## 3. Základní koncepce jazyka SQL

### 3.1 Charakteristika
- Říkáme **co** chceme získat, ne **jak** se to má udělat (deklarativní).
- Intuitivně srozumitelný zápis, připomíná anglické věty.
- Klíčová slova a názvy objektů nejsou case sensitive, **porovnání řetězců ano**.
- Standardizace: 1986, **1992** (poslední čistě relační), 1999, 2003, 2005, 2008, 2011, …
- Nový standard obvykle zahrnuje předchozí, ale postupně „nabaluje" další rysy (OO, XML, …).
- Implementace mají vlastní odchylky.

### 3.2 Rozdělení SQL

| Část | Plné jméno | Hlavní příkazy |
|---|---|---|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP` (tabulek, pohledů, IO) |
| **DML** | Data Manipulation Language | `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE` |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |
|  | Data Dictionary | systémový katalog |
|  | Jazyk modulů | packages, procedury, triggery |

### 3.3 SELECT — základní syntaxe

```sql
select [distinct | all] specifikace_sloupců
from specifikace_zdroje
[where podmínka_selekce]
[group by sloupce]
[having podmínka_na_skupiny]
[order by sloupce [asc|desc]];
```

`specifikace_zdroje` = tabulka | pohled | (vnořený dotaz) | spojení tabulek:
- `tab1 [LEFT|RIGHT|FULL] [OUTER] JOIN tab2 ON (podmínka)`,
- `tab1 [LEFT|RIGHT|FULL] [OUTER] JOIN tab2 USING (sloupce)`,
- `tab1 [LEFT|RIGHT|FULL] [OUTER] JOIN tab2 NATURAL JOIN ...`,
- `tab1 CROSS JOIN tab2`,
- `tab1, tab2` (starší syntaxe ekvivalentní `CROSS JOIN`).

**`USING` vs `NATURAL JOIN`:** `USING (sloupce)` je **bezpečnější** — explicitně vyjmenuje spojovací sloupce, takže nehrozí nechtěné spojení podle stejnojmenných atributů jako u `NATURAL JOIN`. **Ani jedno není v RA** (RA má jen Θ-spojení a přirozené spojení).

### 3.4 Pořadí vyhodnocení klauzulí SELECT

1. **FROM** — zdroj (spojení),
2. **WHERE** — selekce řádků,
3. **GROUP BY** — seskupení,
4. **SELECT** — agregační funkce + projekce + výrazy,
5. **HAVING** — selekce na výsledky agregace,
6. **ORDER BY** — řazení výsledku.

### 3.5 NULL hodnota a tříhodnotová logika

Všechny datové typy mají bottom prvek **NULL** (význam „UNKNOWN", „N/A"). Není to nula ani prázdný řetězec.

| `A` | `B` | `A AND B` | `A OR B` | `NOT A` |
|---|---|---|---|---|
| TRUE | TRUE | TRUE | TRUE | FALSE |
| TRUE | FALSE | FALSE | TRUE | FALSE |
| TRUE | NULL | NULL | TRUE | FALSE |
| FALSE | * | FALSE | (B) | TRUE |
| NULL | * | (B nebo NULL) | (B nebo NULL) | NULL |

- Pokud aspoň jeden operand `=, <>, <, >, ≤, ≥` je NULL, výsledek = NULL.
- Klauzule `WHERE` se vyhodnotí jako TRUE / FALSE / NULL; **řádek se vybere jen pro TRUE**.
- Operátory: `IS [NOT] NULL`, `COALESCE(v1, v2, ..., vn)` (vrátí první ne-NULL).

### 3.6 Agregace
**Agregační funkce:** `COUNT`, `SUM`, `MAX`, `MIN`, `AVG`. Aplikují se přes skupinu řádků.

- `COUNT(A)` ignoruje NULL hodnoty,
- `COUNT(*)` započítává i řádky s NULL,
- `COUNT(∅) = 0`,
- `SUM(∅) = NULL` (ostatní agregace nad prázdnou množinou též vrátí NULL — proto `COALESCE`).
- `agregační_funkce({ALL | DISTINCT} sloupec)` — `DISTINCT` počítá jen různé hodnoty, např. `COUNT(DISTINCT id_filmu)`.

Rozsahový predikát ve `WHERE`: `sloupec BETWEEN a AND b` (inkluzivně, ekvivalent `a ≤ sloupec ≤ b`).

**GROUP BY:** rozdělí řádky do skupin podle hodnot vybraných sloupců. V `SELECT` mohou figurovat **jen** seskupovací sloupce a agregační funkce.

**HAVING:** selekce **na výsledky** agregace (zatímco `WHERE` filtruje **před** seskupením).

### 3.7 Poddotazy (vnořené dotazy)
- **Nevztažený** — má samostatný význam, vyhodnotí se nezávisle.
- **Vztažený** (correlated) — odkazuje na nadřazený dotaz, vyhodnocuje se pro každý řádek vnějšího dotazu (obvykle dražší).

Pozice: v klauzulích `WHERE`, `SELECT`, `FROM`, `HAVING`. Predikáty: `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, `ANY`/`SOME`, `ALL`, srovnání `=, <>, <, >, …`.

### 3.8 Vnější spojení (OUTER JOIN)
Doplní řádky bez partnera v druhé relaci o **NULL** hodnoty: `LEFT [OUTER] JOIN`, `RIGHT [OUTER] JOIN`, `FULL [OUTER] JOIN`.

**Které sloupce zůstanou ve výstupu** (oblíbené doptávání): výstup spojení obsahuje sloupce **obou** relací; chce-li se jen jedna strana, vybírá se `R.*` / `S.*` v `SELECT`. U `LEFT JOIN` zůstanou všechny řádky levé relace a **chybějící sloupce pravé** relace se doplní `NULL` (u `RIGHT` opačně, u `FULL` z obou stran).

**Pozor:** RA pojmem semi-join označuje něco jiného (redukce na n-tice s partnerem) než SQL OUTER JOIN. SQL semi-join se obvykle realizuje pomocí `WHERE … IN (SELECT …)` nebo `EXISTS`.

### 3.9 Kvantifikace v SQL
- **Existenční $\exists x. P(x)$:** `[NOT] EXISTS (poddotaz)` — testuje neprázdnost. **U `EXISTS` nezáleží, co se vybírá v `SELECT` poddotazu** (píše se `SELECT 1` nebo `SELECT *`) — vyhodnocuje se jen (ne)prázdnost množiny výsledků.
- **Univerzální $\forall x. P(x)$:** v SQL přímo není; pomocí $\forall x.P(x) \equiv \neg \exists x. \neg P(x)$:
  ```sql
  -- Kina, která hrají všechna představení.
  select nazev
  from kina k
  where not exists (
    select 1 from predstaveni p where k.id <> p.id_kina
  );
  ```

### 3.10 Množinové operace v SQL
`UNION`, `INTERSECT`, `EXCEPT` (Oracle: `MINUS`). Mohou být s variantou `ALL` (neřeší duplicity, výrazně rychlejší). Pozor na **kompatibilitu množin** — stejný počet a typy atributů.

### 3.11 Predikáty IN, EXISTS, ANY/ALL

| Predikát | Význam |
|---|---|
| `x IN (mnozina)` | $x \in$ množině |
| `x NOT IN (mnozina)` | $x \notin$ množině |
| `EXISTS (poddotaz)` | $\exists$ řádek ve výsledku poddotazu |
| `x > ANY (mnozina)` | $\exists y$ ve mně, $x > y$ (≡ `> SOME`) |
| `x > ALL (mnozina)` | $\forall y$ ve mně, $x > y$ |

Pozor na NULL: `IN(∅) = FALSE`, `IN({NULL}) = UNKNOWN`, `EXISTS(∅) = FALSE`.

### 3.12 LIKE — porovnávání řetězců
- `%` — libovolná skupina znaků (i prázdná).
- `_` — právě jeden znak.
- `ESCAPE '\'` — zruší zástupný význam: `LIKE '%50\%%' ESCAPE '\\'`.

### 3.13 CASE
```sql
case <přepínač>
  when v1 then výraz1
  when v2 then výraz2
  ...
  else výraz3
end
```

### 3.14 SQL DML

#### `INSERT`
```sql
insert into Zakaznici (rod_c, jmeno) values ('4804230160', 'Novák');

insert into Kolik_kopii
  select rod_c, count(c_kopie) from Vypujcky group by rod_c;

-- Vytvoření tabulky + naplnění v jednom příkazu:
create table Kolik_kopii (rod_c char(10), pocet smallint)
  as select rod_c, count(c_kopie) from Vypujcky group by rod_c;
```

#### `UPDATE` / `DELETE`
```sql
update Zakaznici set jmeno = 'Gotzová' where rod_c = '4655292130';
delete from Filmy where jmeno_f = 'Puška';
```

`UPDATE` s vnořeným dotazem umí spočítat redundantní atributy:
```sql
update Zakaznici z
  set pocet_pujcek = (select count(*) from Vypujcky v where v.rod_c = z.rod_c);
```

#### `MERGE`
Kombinace `INSERT` + `UPDATE` podle referenční tabulky: existující záznam se updatuje, neexistující vloží.

### 3.15 Pohledy (VIEW)

**Pohled** je virtuální relace uložená v systémovém katalogu jako `SELECT`.

```sql
create view Prazaci as
  select c_ct, jmeno, adresa from Zakaznici where adresa like '%PRAHA%';

drop view Prazaci;
```

- Pohled je v dotazování **zaměnitelný s tabulkou**.
- DML nad pohledy: **simple view** (bez join, agregací, výrazů) lze, **complex view** vyžaduje `INSTEAD OF` triggery.
- `WITH CHECK OPTION` — kontrola, zda DML neporušuje predikát pohledu.
- **Materializovaný pohled** (`MATERIALIZED VIEW`) má fyzickou kopii dat (výkon, ale konzistence vyžaduje refresh).

### 3.16 SQL DCL

Schéma, uživatel, role (pozor: v Oracle `schema = user`, v PostgreSQL nikoliv).

```sql
grant select on V_Filmy to XNOVAKJ3;
grant all privileges on V_Filmy to public;
revoke insert on Filmy from XNOVAKJ3;
```

Grantovat lze (dle typu objektu): `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `ALTER`, `EXECUTE`, `INDEX`, `REFERENCE`. Vlastník objektu může grant udělit i jinému uživateli nebo roli.

### 3.17 SQL TCL

![[Transakce#Hranice transakce]]

```sql
begin transaction;
  update Account set amount = amount - 100 where id = 1;
  savepoint s1;
  update Account set amount = amount + 100 where id = 2;
commit; -- nebo rollback to s1; rollback;
```

**AUTOCOMMIT ON / OFF** se nastavuje na úrovni session. V insert skriptech vždy doporučeno explicitní `COMMIT`.

---

## 4. Vyjádření integritních omezení v DDL

### 4.1 CREATE TABLE — syntaxe
```sql
create table Tabulka (
  sloupec datovy_typ [io_sloupce [, io_sloupce ...]],
  ...
  [io_tabulky [, io_tabulky ...]]
);
```

**Příklad:**
```sql
create table Vypujcky (
  c_kopie char(3)        not null,
  c_zak   character(6)   not null,
  cena    decimal(5,2),
  rod_c   character(10)  not null,
  datum_v date
);
```

### 4.2 Omezení sloupce

| Omezení | Význam |
|---|---|
| `NOT NULL` | hodnota nesmí být `NULL` |
| `DEFAULT hodnota` | implicitní hodnota |
| `UNIQUE` | všechny hodnoty různé (NULL vícenásobné OK) |
| `PRIMARY KEY` | `UNIQUE` + `NOT NULL`, primární klíč |
| `REFERENCES tab(sl)` | cizí klíč, referenční integrita |
| `CHECK (podmínka)` | libovolný booleovský výraz |

### 4.3 Omezení tabulky
Stejné typy, ale **složené** (přes více sloupců). `NOT NULL` je speciální případ `CHECK`. Pojmenování není nutné, ale **vřele doporučené** — usnadňuje pozdější `ALTER TABLE ... DROP CONSTRAINT`.

**Příklad:**
```sql
create table Predstaveni (
  nazev_k character varying(20) not null,
  nazev_f character varying(20) not null,
  datum   date                  not null,
  constraint predstaveni_pk
    primary key (nazev_k, nazev_f),
  constraint predstaveni_kina_fk
    foreign key (nazev_k) references Kina,
  constraint predstaveni_filmy_fk
    foreign key (nazev_f) references Filmy
);
```

### 4.4 Referenční integrita — kaskádní reakce

![[Cizí-klíč#Syntax v SQL DDL]]

**Akce:**
- `NO ACTION` / `RESTRICT` — nesmaže/neupraví, pokud existuje záznam v $R$ odkazující na $S$.
- `CASCADE` — kaskádně smaže/upraví závislé záznamy.
- `SET NULL` — nastaví FK na NULL.
- `SET DEFAULT` — nastaví FK na default hodnotu.

**Příklad:**
```sql
create table Order_items (
  product_no integer references Products on delete restrict,
  order_id   integer references Orders   on delete cascade,
  quantity   integer,
  primary key (product_no, order_id)
);
```

### 4.5 Okamžik kontroly IO
- **IMMEDIATE** (default) — kontrola po každém DML.
- **DEFERRED** — kontrola odložená až na konec transakce.
- V Oracle navíc `ALTER TABLE ... DISABLE/ENABLE CONSTRAINT`.

### 4.6 ALTER TABLE, DROP TABLE
```sql
alter table Kina add pocet_mist integer;
alter table Kina add constraint kina_check_kapacita
  check (pocet_mist > 0);
alter table Kina drop constraint kina_check_kapacita;

drop table Kina cascade;
```

### 4.7 IO mimo DDL — procedurálně
IO typu „v kině se nehraje více než dvakrát týdně" nebo „jeden film se nehraje ve více než třech kinech" **nelze formulovat deklarativně**. Řeší se **procedurálně** triggery (na straně serveru) nebo v aplikaci (na straně klienta).

---

## 5. Co je potřeba na zkoušku znát

### Definice
- Relace, schéma relace, atribut, doména, n-tice, 1NF.
- Schéma relační databáze $(R, I)$, přípustná relační databáze.
- Klíč schématu (minimalita), primární a alternativní klíč.
- Cizí klíč, referenční integrita.
- Integritní omezení — deklarativní vs. procedurální.
- Dotaz, dotazovací jazyk, relační úplnost.
- Relační algebra — všechny operace.
- NULL, tříhodnotová logika.
- Pohled, materializovaný pohled.

### Algoritmy a formalismy
- Selekce, projekce, přejmenování — RA + SQL ekvivalent.
- Spojení (přirozené, Θ-, vnější), polospojení, antijoin — RA + SQL ekvivalent.
- Množinové operace v RA i SQL.
- Relační dělení — definice přes minimální množinu operací.
- Univerzální kvantifikace v RA i SQL přes $\neg \exists \neg$.
- Pořadí vyhodnocení klauzulí SELECT.

### Klíčové vlastnosti
- Minimální množina operací RA: $\{\times, \text{selekce}, \text{projekce}, \to, \cup, \setminus\}$.
- RA neřeší DML a DDL, jen dotazování.
- SELECT > RA: agregace, OUTER JOIN, ORDER BY, výrazy.
- DDL: `CREATE TABLE` + IO sloupce/tabulky + `ALTER`/`DROP`.
- DML: `INSERT`, `UPDATE`, `DELETE`, `MERGE`.
- DCL: `GRANT`, `REVOKE`.
- TCL: `COMMIT`, `ROLLBACK`, `SAVEPOINT`.
- Šest typů IO sloupce: `NOT NULL`, `DEFAULT`, `UNIQUE`, `PRIMARY KEY`, `REFERENCES`, `CHECK`.
- Akce při referenční integritě: `NO ACTION`, `RESTRICT`, `CASCADE`, `SET NULL`, `SET DEFAULT`.

### Typické doplňující otázky (doptávání)
> Z reálných zkušeností. **Hunka** je v komisi a DBS zkouší prakticky — chce **konkrétní SQL syntax a chování joinů**, ne teorii RA; je benevolentní a navádí. Otázku skoro vždy **zúží**.
- **Hunka:** „Které sloupce zůstanou ve výstupu jednotlivých joinů, zvlášť u outer join?" → §3.8, §2.3
- **Hunka:** „Napište konkrétní `SELECT` a jeho klauzule; jak byste sestavil dotaz?" → §3.3–3.4
- **Hunka:** „K čemu je `CHECK`? `ON DELETE CASCADE` (ne `DROP`!)? K čemu jsou pohledy?" → §4.2, §4.4, §3.15
- **Hunka:** „Vnější spojení na příkladu; (ne)vztažené poddotazy a kde se poddotazy mohou objevit." → §3.7–3.8
- **Borkovcová:** „Joiny jako množinové operace; `EXISTS` vs `IN`; `JOIN USING`." → §2.3, §3.11, §3.3
- **Pavlíček/Matoušek:** „Left join v SQL *i* RA na příkladu; jak udělat left join jen přirozeným spojením." → §2.3, §3.8
