---
tags: [komise, strategie, otázka]
---

# Zkušební komise (SZZ léto 2026) — analýza otázek

Analýza historie otázek (`question_history1.csv`, `question_history2.csv`) protkaná se složením **mé komise** (`komise.txt`) a oficiálním zadáním otázek ([[BI-SPOL.21]] 1–30, [[BI-UI.21]] 1–26).

Cíl: zúžit, **na co se nejvíc soustředit**, podle toho, kdo mě zkouší a co historicky vyžadují.

> **Metodika.** Z obou CSV jsem vytáhl všechny řádky, kde zkoušející = člen mé komise (včetně variant zápisu jména „Příjmení Jméno“ / „Jméno Příjmení“). Každou historickou otázku jsem namapoval na číslo oficiální otázky. „Petr" jako jméno (Špaček, Klán, Fišer…) jsem odfiltroval — beru jen **Petr Ivo**.

---

## Formát zkoušky (a co z něj plyne)

- **Dvě otázky, přiřazené komisí.** Dostanu **dvě** otázky — jednu ze **společných předmětů** ([[BI-SPOL.21|BI-SPOL]] 1–30) a jednu ze **specializace umělá inteligence** ([[BI-UI.21|BI-UI]] 1–26). **Nelosuje se — otázky přiřazuje komise.** Vybírá tedy z toho, co sama umí vyzkoušet → historie otázek členů komise je **přímá předpověď**, ne jen statistika.
- **Zúžení je možné, ne nutné.** Zkoušející může otázku **zúžit** („zaměřte se na…“) — v historii se to děje často (viz „Zúžení/Zaměření“ v tabulkách níže) — ale nemusí.
- **Křížové dotazy jsou vzácné.** Teoreticky se může doptat i na věc z jiné otázky, prakticky je to ale neobvyklé. **Spoléhám na to, že řeším jen své dvě přiřazené otázky** a nepřipravuju se na „nesouvisející“ doptávání napříč tématy.

**Co z toho plyne pro prioritizaci:**

- **Společná (BI-SPOL) otázka přijde skoro jistě z gesce komise.** Komise nezadá předmět, který nikdo z nich neučí → reálně se vybírá ze **SAP** (Daňhel), **PST** (Dedecius/Petr), **matematiky** (Petr: LA1, MA1, MA2, DML, KAB-9) a **DBS** (Hunka). V celé historii (40 záznamů) se nikdo z komise nedotkl **AAG, AG1, OSY, PA1/2, PSI** → ty můžu **prakticky vypustit** (viz níže).
- **Specializační (BI-UI) otázka je celá v gesci komise.** LA2 = Petr; ML1/ML2 = Holeňa + Dedecius; ZUM = Holeňa. Cokoli z 1–26 zadá doménový expert → **celou specializaci musím umět plošně**, tady vypouštět nelze.
- **Závěr:** příprava se zužuje na **(1) celé BI-UI** + **(2) BI-SPOL jen z předmětů komise** (SAP, PST, matematika, DBS, příp. DML/KAB-9). Zbytek BI-SPOL je u téhle komise krajně nepravděpodobný.

---

## TL;DR — priorita kurzů podle komise

| Priorita | Kurz | Otázky | Kdo z komise | Proč |
|---|---|---|---|---|
| 🔴 **NEJVYŠŠÍ** | **SAP** | 28, 29, 30 | **Daňhel** (výhradně) | Jeho jediná doména, zkouší ji **pořád** a do hloubky — jistá zóna tvrdého doptávání |
| 🔴 **NEJVYŠŠÍ** | **PST** | 26, 27 | **Dedecius** (místopředseda) + **Petr** | Dedeciova srdcovka, nejčastější otázka v historii; ptají se dva členové |
| 🟠 Vysoká | **LA1 / LA2 / MA2** | 11,12 / UI 1–7 / 15,16 | **Petr** (všechny matematické) | Vlastní čísla, diagonalizace, funkce více proměnných, integrály — opakovaně |
| 🟠 Vysoká | **ML1** | 8–14 | **Holeňa** (předseda) + **Dedecius** | Statistické ML: lin. regrese (10), logistická (12), naivní Bayes (18→ML2), k-means/DBSCAN (14) |
| 🟠 Vysoká | **ML2** | 15–20 | **Holeňa** + **Dedecius** | Holeňa doložen na SVM/jádrová regrese (15,16); Dedecius na NB/logistickou |
| 🟡 Střední | **DBS** | 5, 6 | **Hunka** | ACID, SQL dotazování, transformace ER→relační |
| 🟡 Střední | **ZUM** | 21–26 | **Holeňa** (doména AI) | Bez historie u komise, ale je to Holeňova oblast — nepodcenit |
| 🟡 Střední | **MA1 / DML / KAB-9** | 13,14 / 7,8 / 9 | **Petr** (matematik) | Petrova doména i bez silné historie: MA1/DML bez přímého záznamu; **KAB-9** (RSA / teorie čísel) **1×** (2017). *KAB-10 (symetrické šifry) nikdo* |
| ⚫ Vypustit | AAG, AG1, OSY, PA1, PA2, PSI, KAB-10 | — | nikdo | Komise je neučí a **nikdy je nezadala**; otázky přiřazuje, takže je nepřiřadí → bezpečně minimalizovat (viz níže) |

**Tři nejsilnější signály:**
1. **SAP** — Daňhel zkouší výhradně SAP, opakovaně a do hloubky → jistá oblast tvrdého doptávání.
2. **PST 26+27** — nejčastější historická otázka napříč komisí (Dedecius + Petr).
3. **Lineární regrese** (BI-UI-10) — jediná otázka, kterou doložitelně zkouší **dva různí** členové (Dedecius i Petr).

---

## Jak jsou přísní / vstřícní (podle zkušeností studentů)

> ⚠️ **Malý vzorek, anekdoty.** Komentáře jsou jen z poznámkového sloupce `question_history1.csv` (`question_history2.csv` poznámky nemá). Dedecius má 4 záznamy, ostatní 1–2, **Holeňa žádný**. Známky jsou navíc zkreslené — detailní poznámku spíš napíše ten, komu to vyšlo. Ber jako orientaci, ne jako jistotu.

| Zkoušející | Dojem | Známky (z dat) | Styl |
|---|---|---|---|
| **Hunka** | 😊 **velmi vstřícný** | B, B | „Gigachad" — návodné otázky, stačí přikyvovat, projde i málo připravený |
| **Daňhel** | 🙂 **vstřícný, ale precizní** | (bez dat) | Aktivně pomáhá a navádí (odkazuje na cvika), ale chce **přesný** mechanismus |
| **Dedecius** | 🙂 **férový, ale hodně doptává** | A, A, A | Dává áčka, zato **vrší statistické doplňující otázky** do hloubky |
| **Petr** | 😐 **precizní, jde po chybách** | A, A, A, **D** | Mostly A, ale jedna chyba v definici → vytáhne ji a může to srazit |
| **Holeňa** | ❓ **bez dat** | — | Žádná studentská poznámka; jako předseda spíš moderuje |

**Hunka — nejmírnější z komise.** Doslovný citát studentky:

> „Hunka je gigachad, popsala jsem jen půl stránky, netušila jsem skoro nic… ptal se na věci, co šly zodpovědět i bez znalostí, a pak stylem ‚tohle by mělo být takhle, že jo?' a stačilo odkývat."

Dostala **B** prakticky bez přípravy. → U DBS stačí solidní základ, navede tě.

**Daňhel — pomáhá, ale chce hloubku.** U přerušení *„chce vědět co přesně se děje, jak se skáče z paměti"*; aktivně naváděl odkazem na cvika SAP (zvyšování čítače → přerušení). → Vstřícný, ale **detail u SAP musí sedět** — nestačí to „rukama nohama".

**Dedecius — dává áčka, ale doptává jako o život.** Tři doložené **A**, zato u každé otázky série doplňujících: u k-means *„co je metrika, jestli vždy doběhne stejně, jak volit k"*; u lin. regrese *„hodně statistických otázek ohledně interceptu a epsilon a proč chceme aby střední hodnota byla 0"*. → Fér hodnotitel, ale **musíš ustát statistické pozadí**, ne jen postup.

**Petr — nejpřísnější na přesnost.** Tři **A**, ale i jedno **D**: student *„sepsal všechny definice, avšak hned tu první pokazil… pracně se ze mě snažil vydolovat to, co chtěl"* + doptal na PD/ND, co nenapsal. U jiného (A) odhalil chybu v definici RSS. → **Chyby si najde a jde po nich**; výhoda je, že nechá opravit. Piš definice **přesně**.

**Holeňa — neznámá.** V datech jediné dva věcné záznamy, **nula** poznámek k povaze. Jako **předseda** typicky vede průběh a doptává napříč AI/ML — připrav se spíš na šíři než na konkrétní „styl".

---

## 1. prof. Holeňa — předseda (všechny AI/ML kurzy)

**Doména:** veškeré AI/ML → [[8ML1-long|ML1 (8–14)]], [[15ML2-long|ML2 (15–20)]], ZUM (21–26).
**Historie:** jen 2 záznamy (málo dat), ale jako **předseda** může sáhnout kamkoli do AI/ML.

| Rok | Kurz | Otázka | → č. |
|---|---|---|---|
| LS 2021 | ADM | Jádrová regrese, bázové funkce, SVM. **Zaměřte se na SVM** | UI-15/16 |
| LS 2022 | ZNS | Základy fuzzy logiky, neurčitost, relace | mimo zadání (ZNS) |

**Závěr:** Doložený zájem o **SVM a jádrovou regresi** ([[15ML2-long|15]], [[16ML2-long|16]]). Jako předseda ale očekávej doptávání kdekoli v ML1/ML2/ZUM. Měj jistotu v principech, ne jen v receptech.

---

## 2. doc. Dedecius — místopředseda (statistika)

**Doména:** statistika → [[26PST-long|PST (26, 27)]] + statistické ML.
**Historie:** 13 záznamů — **nejaktivnější člen** a jasně zaměřený.

**Opakující se témata (seřazeno podle četnosti):**
- **PST-26** — náhodné veličiny, rozdělení, distribuční funkce, hustota, momenty *(≈4× — jeho top téma)*
- **PST-27** — statistická indukce, náhodný výběr, bodové/intervalové odhady, testování hypotéz o stř. hodnotě *(3×)*
- statistické ML: lin. regrese, logistická regrese, naivní Bayes, k-means/DBSCAN *(po 1×)*

| Rok | Kurz | Otázka (zkráceně) | → č. |
|---|---|---|---|
| 2025 LS | PST | Pravidla pravděpodobnosti, Bayes, NV, rozdělení, distr. fce, momenty, nezávislost, **CLT, zákony velkých čísel**. *Zúženo: NV, linearita, momenty* | 26 |
| 2025 LS | PST | Distribuční funkce | 26 |
| LS 2019 | PST | Náhodné veličiny, příklady rozdělení, distr. fce, hustota, momenty | 26 |
| LS 2021 | PST | Distr. fce, hustota, momenty, NV (transformace), příklady rozdělení | 26 |
| LS 2020 | PST | **Intervalové odhady** — druhy, použití, rozdíl od bodových; vazba na testování hypotéz | 27 |
| ZS 2020 | PST | Statistická indukce, náhodný výběr, bodové+intervalové odhady, testování. *Doptal: empirická distr. fce, nestrannost, konzistence odhadu* | 27 |
| LS 2021 | PST | Statistická indukce, náhodný výběr, odhady stř. hodnoty a rozptylu, testování | 27 |
| 2025 LS | (ML) | **Nesupervizované učení**, k-means, DBSCAN. *Zúženo: K-Means. Doptal: co je metrika, jestli vždy doběhne stejně, jak volit k* | UI-14 |
| 2025 LS | (ML) | **Lineární regrese** — MNČ, geom. interpretace, kolinearita. *Doptal: intercept, ε, proč E=0* | UI-10 |
| LS 2022 | VZD | **Naivní Bayesův klasifikátor** | UI-18 |
| LS 2022 | VZD | **Logistická regrese** | UI-12 |
| LS 2019 | LIN | Matice: regulární, inverzní, diagonalizace, GEM | LA1-12 |
| LS 2020 | MLO | Výroková logika — splnitelnost, ekvivalence, CNF/DNF | DML-7 |

**Závěr:** **PST 26 a 27 musím umět na jedničku** — to je jeho chleba. K tomu počítej s tím, že u statistických ML otázek (10, 12, 14, 18) bude **doptávat na statistické pozadí** (náhodný výběr, rozdělení, střední hodnota ε, nestrannost odhadů).

---

## 3. Ing. Daňhel — číslicové obvody / SAP

**Doména:** SAP → [[28SAP-long|SAP (28, 29, 30)]]. **V historii se objevuje výhradně u SAP.**
**Historie:** 9 záznamů, pokrývají **všechny tři** SAP otázky.

**Rozložení:** otázka **29** (architektura/ISA) 4×, **30** (kódy/FP) 3×, **28** (logické obvody) 2×.

| Rok | Otázka (zkráceně) | → č. |
|---|---|---|
| 2024 LS | Architektura, **von Neumann vs Harvard**, instrukční cyklus, ISA (zásobníková vs GPR), **přerušení**. *Chce přesně co se děje při přerušení (skok z paměti, čítač)* | **29** |
| LS 2020 | Architektura, instr. cyklus, ISA. *Zúženo: von Neumann vs Harvard; třídy ISA — zásobníková vs středačová, lze nakreslit* | **29** |
| LS 2020 | (totéž, jiný obor) | **29** |
| LS 2019 | Popis číslicového počítače, instr. cyklus, ISA (bez paměťové hierarchie) | **29** |
| LS 2020 | Kódy se znaménkem, aritm. operace, FP. *Zúženo: jen kódy* | **30** |
| LS 2020 | Kódy se znaménkem. *Ukažte −4 ve 4 bitech v jednotlivých reprezentacích* | **30** |
| LS 2021 | Kódy se znaménkem + FP. *−4 ve 4 bitech; vysvětlete modul a mantisu* | **30** |
| ZS 2020 | **Kombinační** logické obvody, implementace na hradlech, **minimalizace mapami** | **28** |
| LS 2019 | Kombinační **a sekvenční** (**Mealy, Moore**), hradla, minimalizace mapami | **28** |

**Závěr:** 🔴 **Nejvyšší priorita** — Daňhel zkouší pouze SAP, opakovaně a do hloubky. Konkrétně chce umět:
- ISA (zásobníková vs GPR/středačová), von Neumann × Harvard, **mechanismus přerušení** (otázka 29),
- **zápis −4 ve 4 bitech** ve všech reprezentacích + FP modul/mantisa (otázka 30),
- minimalizaci pomocí **map (Karnaugh)** a automaty Mealy/Moore (otázka 28).

---

## 4. Ing. Hunka — databázové systémy (možná PA1/2)

**Doména:** DBS → [[5DBS-long|DBS (5, 6)]]. *(Část jeho historie je softwarové inženýrství — metodiky, požadavky — což **není** v mém zadání BI-SPOL/BI-UI; ignoruj.)*
**Historie:** 5 záznamů.

| Rok | Otázka (zkráceně) | → č. |
|---|---|---|
| LS 2021 | **Transakce a jejich vlastnosti — ACID** | **6** |
| 2025 ZS | Pokročilé SQL: agregace, **vnější spojení**, **vnořené dotazy**, kvantifikace. *Doptal: kde se vnořené dotazy můžou objevit, (ne)vztažené dotazy* | **5** |
| 2025 LS | **Transformace konceptuálního na relační** model, příp. do DDL; ukázat na 1:1, 1:N s kardinalitami | 5 (ER→rel.) |
| 2025 LS | Analýza a správa požadavků, UC/scénáře (na příkladu) | mimo zadání (SI) |
| 2025 LS | Klasické vs agilní metodiky, UP, SCRUM | mimo zadání (SI) |

**Závěr:** Pro mě relevantní jsou **DBS 5 a 6**: **ACID**, **SQL** (vnější spojení, vnořené/(ne)vztažené dotazy, agregace) a **převod ER → relační schéma** (1:1, 1:N kardinality). Z poznámek vychází jako benevolentní, ale doptává se na praktické detaily. PA1/2 v jeho historii nedoloženo.

---

## 5. Ing. Petr — všechny matematické kurzy

**Doména:** matematika → [[11LA1-long|LA1 (11, 12)]], [[13MA1-long|MA1 (13, 14)]], [[15MA2-long|MA2 (15, 16)]], [[1LA2-long|LA2 (UI 1–7)]], [[7DML-long|DML (7, 8)]] + přesah do statistiky a kryptografie (KAB-9).
**Historie:** 11 záznamů.

**Opakující se témata:**
- **Vlastní čísla a diagonalizace** *(2× — LA1-12 / LA2-6)*
- **Integrály / řady / Taylor** *(2× — MA2-15)*
- **Statistika** — odhady, intervaly, testování *(2× — PST-27)*

| Rok | Kurz | Otázka (zkráceně) | → č. |
|---|---|---|---|
| 2025 LS | LA1 | Matice, **vlastní čísla a diagonalizace** *(zúženo)* | **12** / UI-6 |
| LS 2015 | LIN | Vlastní čísla a vektory, diagonalizace | 12 / UI-6 |
| LS 2015 | LIN | Soustavy lin. rovnic, **Frobeniova věta**, existence a jednoznačnost řešení | **11** |
| 2025 LS | MA2 | **Funkce více proměnných** — parc. derivace, gradient, Hessova matice, lok. extrémy. *Doptal: jak určit PD/ND matice* | **16** |
| LS 2016 | ZMA | Integrální počet (primitivní fce, určitý/neurčitý integrál, geom. význam) | **15** |
| LS 2017 | ZMA | **Taylorův polynom a věta**; spočítat Taylorův polynom | 15 (MA1/MA2) |
| 2025 LS | PST | Stat. indukce, náhodný výběr, odhady, konfidenční intervaly, testování | **27** |
| LS 2016 | PST | Intervalové odhady, testování hypotéz o stř. hodnotě (s příkladem) | 27 |
| 2025 LS | (ML) | **Lineární regrese** — MNČ, geom. interpretace, kolinearita. *Doptal: pravděpodobnostní interpretace (náhodný výběr, rozdělení)* | UI-10 |
| ZS 2015 | ZDM | Homogenní rekurentní rovnice s konst. koeficienty | mimo (ZDM) |
| LS 2017 | BEZ | Symetrické/asymetrické šifry, RSA, RSA podpis | KAB-9 (staré) |

**Závěr:** Petr pokrývá celou matematickou linii. Nejjistější musím být v:
- **vlastní čísla + diagonalizace** (LA1-12, opakuje se i v LA2-6 jako mocninná/QR metoda),
- **soustavy + Frobenius** (LA1-11),
- **funkce více proměnných** (MA2-16: gradient, Hessova matice, **definitnost PD/ND**),
- **integrály a Taylor** (MA2-15).
- U **lineární regrese** i u něj počítej s **pravděpodobnostní interpretací** (stejně jako Dedecius).

Jako matematik může sáhnout i po **MA1** (limity, derivace, průběh funkce), **DML** (výroková logika, teorie čísel) a okrajově **KAB-9** (asymetrické šifry / RSA — 1× v historii, 2017). Přímá historie je u nich slabá, ale jsou v jeho gesci, takže je nepodceň.

---

## Křížové „horké" otázky (ptá se víc členů / vícenásobný signál)

| Otázka | Kdo | Pozn. |
|---|---|---|
| **BI-UI-10 Lineární regrese** | **Dedecius + Petr** | Jediná otázka doložená u **dvou** členů; navíc statistický přesah → očekávej tvrdé doptávání na pravděpodobnostní interpretaci (náhodný výběr, ε, E=0, kolinearita) |
| **PST-26 + 27** | **Dedecius + Petr** | Nejčastější téma celé komise; Dedeciova srdcovka |
| **LA1-12 / LA2-6 Vlastní čísla, diagonalizace** | **Petr** (+ Dedecius 1×) | Opakovaně; přesah LA1 → LA2 (mocninná metoda, QR) |
| **SVM / jádrová regrese (UI-15, 16)** | **Holeňa** | Jediná doložená Holeňova ML otázka |

---

## Co můžu (skoro) vypustit

Tyto společné předměty žádný člen komise neučí **a v celé historii ani jednou nezadal**. Protože komise otázky **přiřazuje** (nelosuje se), je krajně nepravděpodobné, že je dostanu:

- **AAG** (1, 2), **AG1** (3, 4, +20, 21), **OSY** (17, 18), **PA1** (19–21), **PA2** (22, 23), **PSI** (24, 25), **KAB-10** (symetrické šifry).

> ✅ Sem dej **minimum času**. Jediné reálné riziko je změna ve složení komise (nebo toho, kdo přiřazuje) — **ověř si finální komisi před zkouškou** a tehdy to případně přehodnoť.

---

## Doporučené pořadí přípravy

1. **SAP 28, 29, 30** (Daňhel) — jistá zóna tvrdého doptávání.
2. **PST 26, 27** (Dedecius + Petr) — nejčastější téma komise.
3. **LA1 11, 12 + MA2 15, 16 + LA2 1–7** (Petr) — vlastní čísla, gradient/Hessova, integrály.
4. **ML1/ML2 statistické otázky** — lin. regrese (10), logistická (12), naivní Bayes (18), k-means/DBSCAN (14), SVM/jádro (15, 16) — Dedecius + Holeňa.
5. **DBS 5, 6** (Hunka) — ACID, SQL, ER→relační.
6. **ZUM 21–26** (Holeňa, bez historie, ale jeho doména).
7. **MA1 13,14 + DML 7,8 + KAB-9** (Petr jako matematik) — limity/derivace, výroková logika + teorie čísel, RSA. Nižší priorita, ale jeho doména.
