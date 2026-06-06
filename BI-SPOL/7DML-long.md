---
studyplan: true
etapa: 7 · MA1 / DML / KAB — Petr
qid: 7DML
examiner: Petr
topic: "Výroková logika: splnitelnost, ekvivalence, CNF/DNF, úplné normální tvary"
readiness: in progress
tags:
  - otázka
  - kurz/DML
  - otázka/7
  - todo
---

# Výroková logika

> **Otázka SZZ:** Výroková logika: splnitelnost formulí, logická ekvivalence a důsledek, universální systém logických spojek, disjunktivní a konjunktivní normální tvary, úplné normální tvary.

Zdroje: BI-DML, kapitola 2 (Výroková logika), Bohdal a kol., FIT ČVUT.

---

## 1. Jazyk výrokové logiky (kontext)

**Výroková formule** se buduje induktivně z **prvotních formulí** (atomů, značíme $A, B, C, \dots$) pomocí logických spojek $\neg, \land, \lor, \Rightarrow, \Leftrightarrow$ a závorek.

**Ohodnocení** $v$ je zobrazení, které každé prvotní formuli přiřadí pravdivostní hodnotu $0$ nebo $1$. Ohodnocení se rozšiřuje na složené formule podle pravdivostních tabulek spojek.

Symboly $\top$ a $\bot$ označují formule, které mají pro každé ohodnocení hodnotu $1$, resp. $0$.

---

## 2. Splnitelnost formulí

### 2.1 Tautologie, splnitelná formule, kontradikce

**Definice (Tautologie, splnitelnost, kontradikce):** Buď $F$ výroková formule.

- $F$ je **[[Tautologie|tautologie]]**, právě když pro každé ohodnocení $v$ platí $v(F) = 1$.
- $F$ je **splnitelná**, jestliže existuje ohodnocení $v$ takové, že $v(F) = 1$.
- $F$ je **kontradikce**, právě když pro každé ohodnocení $v$ platí $v(F) = 0$.

Píšeme též $F = \top$ pro tautologii a $F = \bot$ pro kontradikci.

### 2.2 Vzájemné vztahy

**Tvrzení (Základní vztahy):**
1. Negace tautologie je kontradikce.
2. Negace kontradikce je tautologie.
3. Každá tautologie je splnitelná.
4. Žádná splnitelná formule (a tedy ani tautologie) není kontradikce.
5. Žádná kontradikce není splnitelná.

**Důkaz.** Přímo z definice — pro každé $v$ máme $v(\neg F) = 1 - v(F)$, a stačí postupně rozepsat.

### 2.3 Příklady
- $A \lor \neg A$ — tautologie (zákon vyloučeného třetího).
- $A \land \neg A$ — kontradikce (zákon vyloučení sporu).
- $A \Leftrightarrow B$ — splnitelná, ale ne tautologie.
- $(A \Rightarrow B) \Leftrightarrow (\neg B \Rightarrow \neg A)$ — tautologie (kontrapozice).

### 2.4 SAT problém

Úlohou **SAT** (Boolean satisfiability problem) je rozhodnout, zda zadaná formule je splnitelná. Pro $n$ prvotních formulí má pravdivostní tabulka $2^n$ řádků — naivní algoritmus je exponenciální. Široká škála rozhodovacích a optimalizačních problémů se na SAT redukuje.

---

## 3. Logická ekvivalence a logický důsledek

### 3.1 Definice

**Definice (Logická ekvivalence a důsledek):** Buďte $E, F$ výrokové formule.

- $E$ a $F$ jsou **logicky ekvivalentní**, právě když pro každé ohodnocení $v$ platí $v(E) = v(F)$. Píšeme $E \equiv F$ (skripta používají $E = F$).
- $F$ je **logickým důsledkem** $E$, právě když pro každé ohodnocení $v$, pro které $v(E) = 1$, je i $v(F) = 1$. Píšeme $E \models F$ (skripta používají $E \Rightarrow\!\!\Rightarrow F$).

### 3.2 Charakterizace pomocí tautologie/kontradikce

**Věta (Ekvivalence a důsledek pomocí tautologie):** Pro libovolné výrokové formule $E, F$ platí:

1. $E \equiv F$ právě tehdy, když $E \Leftrightarrow F$ je tautologie.
2. $E \models F$ právě tehdy, když $E \Rightarrow F$ je tautologie.
3. $E \models F$ právě tehdy, když $E \land \neg F$ je kontradikce.

**Důkaz.**
1. Z definice: $E \equiv F \iff (\forall v)\,v(E) = v(F) \iff (\forall v)\,v(E \Leftrightarrow F) = 1$.
2. Z definice: $E \models F \iff (\forall v)\,(v(E) = 1 \Rightarrow v(F) = 1) \iff (\forall v)\,v(E \Rightarrow F) = 1$.
3. Stačí použít bod 2 a fakt, že $E \Rightarrow F$ je tautologie $\iff E \land \neg F$ je kontradikce (z $\neg(E \Rightarrow F) \equiv E \land \neg F$).

### 3.3 Vlastnosti ekvivalence a důsledku

Logická ekvivalence je **reflexivní, symetrická a tranzitivní** (jde tedy o relaci ekvivalence).
Logický důsledek je **reflexivní a tranzitivní**.

**Náhrada podformule (Věta o substituci):** Je-li $G$ podformule $F$ a $G \equiv G'$, pak $F \equiv F'$, kde $F'$ vznikne z $F$ nahrazením $G$ za $G'$. Tato věta legitimizuje úpravy formulí „po částech".

### 3.4 Klíčové logické zákony

| Typ | Zákon |
|---|---|
| Vyloučení sporu | $A \land \neg A \equiv \bot$ |
| Vyloučeného třetího | $A \lor \neg A \equiv \top$ |
| Dvojí negace | $\neg\neg A \equiv A$ |
| Idempotence | $A \land A \equiv A$, $A \lor A \equiv A$ |
| Komutativita | $A \land B \equiv B \land A$, $A \lor B \equiv B \lor A$ |
| Asociativita | $(A \land B) \land C \equiv A \land (B \land C)$ atd. |
| Distributivita | $A \land (B \lor C) \equiv (A \land B) \lor (A \land C)$ a duál |
| Absorpce | $A \land (A \lor B) \equiv A$, $A \lor (A \land B) \equiv A$ |
| De Morgan | $\neg(A \land B) \equiv \neg A \lor \neg B$, $\neg(A \lor B) \equiv \neg A \land \neg B$ |
| Kontrapozice | $A \Rightarrow B \equiv \neg B \Rightarrow \neg A$ |
| Implikace ↔ disjunkce | $A \Rightarrow B \equiv \neg A \lor B$ |
| Negace implikace | $\neg(A \Rightarrow B) \equiv A \land \neg B$ |
| Ekvivalence ↔ konjunkce implikací | $A \Leftrightarrow B \equiv (A \Rightarrow B) \land (B \Rightarrow A)$ |

### 3.5 Klasické důsledky (dedukce)

| Pravidlo | Tvar |
|---|---|
| Modus ponens | $(A \Rightarrow B) \land A \models B$ |
| Modus tollens (disj.) | $(A \lor B) \land \neg A \models B$ |
| Reductio ad absurdum | $(A \Rightarrow B) \land \neg B \models \neg A$ |
| Hypotetický sylogismus | $(A \Rightarrow B) \land (B \Rightarrow C) \models A \Rightarrow C$ |
| Konstruktivní dilema | $(A \Rightarrow B) \land (C \Rightarrow D) \land (A \lor C) \models B \lor D$ |
| Destruktivní dilema | $(A \Rightarrow B) \land (C \Rightarrow D) \land (\neg B \lor \neg D) \models \neg A \lor \neg C$ |

---

## 4. Universální systém logických spojek

### 4.1 Definice

**Definice (Universální systém spojek, USS):** Množina logických spojek tvoří **universální systém**, právě když ke každé výrokové formuli existuje logicky ekvivalentní formule, která obsahuje pouze spojky z této množiny.

### 4.2 Triviální (přímo z předchozího)

Universálními systémy jsou:
1. $\{\neg, \land, \lor, \Rightarrow, \Leftrightarrow\}$,
2. $\{\neg, \land, \lor, \Rightarrow\}$ (díky $A \Leftrightarrow B \equiv (A \Rightarrow B) \land (B \Rightarrow A)$),
3. $\{\neg, \land, \lor\}$ (díky $A \Rightarrow B \equiv \neg A \lor B$).

### 4.3 Dvouprvkové USS

**Věta:** Universálními systémy jsou
1. $\{\neg, \lor\}$,
2. $\{\neg, \land\}$,
3. $\{\neg, \Rightarrow\}$.

**Důkaz (pro $\{\neg, \lor\}$, strukturální indukcí):** Stačí ukázat, že ostatní spojky lze vyjádřit pomocí $\neg, \lor$.
- $E \Rightarrow F \equiv \neg E \lor F$.
- $E \land F \equiv \neg(\neg E \lor \neg F)$ (De Morgan + dvojí negace).
- $E \Leftrightarrow F \equiv (E \Rightarrow F) \land (F \Rightarrow E) \equiv \neg(\neg(\neg E \lor F) \lor \neg(E \lor \neg F))$.

### 4.4 Jednoprvkové USS — NAND a NOR

**Definice (NAND, NOR):**
- **Shefferův symbol** (NAND): $A \uparrow B := \neg(A \land B)$.
- **Peirceova šipka** (NOR): $A \downarrow B := \neg(A \lor B)$.

**Věta (Jednoprvkové USS):** $\{\uparrow\}$ i $\{\downarrow\}$ tvoří USS.

**Důkaz pro $\uparrow$:** Stačí vyjádřit $\neg, \land, \lor$ pomocí $\uparrow$:
- $\neg E \equiv \neg(E \land E) \equiv E \uparrow E$,
- $E \land F \equiv \neg\neg(E \land F) \equiv (E \uparrow F) \uparrow (E \uparrow F)$,
- $E \lor F \equiv \neg(\neg E \land \neg F) \equiv (E \uparrow E) \uparrow (F \uparrow F)$ (De Morgan).

Implikaci a ekvivalenci pak skládáme z předchozích.

**Věta:** $\uparrow$ a $\downarrow$ jsou **jediné** binární logické spojky tvořící jednoprvkový USS.

**Idea důkazu:** Spojka $?$ musí být schopná vyrobit negaci jako $A?A$, tedy z pravdy dělá lež a opačně. Z 16 binárních spojek nad dvěma prvotními formulemi tuto podmínku splňují pouze $\neg A$, $\neg B$, $\uparrow$ a $\downarrow$. První dvě nejsou skutečně binární. Zůstávají $\uparrow$ a $\downarrow$.

**Použití:** $\uparrow, \downarrow$ jsou základem elektronického návrhu (jediné hradlo stačí pro libovolnou kombinační logiku); NAND/NOR flash paměti.

---

## 5. Disjunktivní a konjunktivní normální tvary

### 5.1 Literál, klausule, implikant

**Definice (Literál):** Výroková formule je **literál**, je-li prvotní formulí ($A$) nebo negací prvotní formule ($\neg A$).

**Definice (Disjunktivní normální tvar, DNT):**
- **Implikant** = literál nebo konjunkce několika literálů, např. $A \land \neg B \land C$.
- Formule je v **DNT** (anglicky DNF), je-li implikantem nebo disjunkcí implikantů, např. $(A \land \neg B) \lor (\neg A \land C) \lor \neg C$.

**Definice (Konjunktivní normální tvar, KNT):**
- **Klausule** = literál nebo disjunkce několika literálů, např. $A \lor \neg B \lor C$.
- Formule je v **KNT** (anglicky CNF), je-li klausulí nebo konjunkcí klausulí, např. $(A \lor \neg B) \land (\neg A \lor C) \land \neg C$.

**Proč implikant/klausule?** Aby formule v DNT byla pravdivá, **stačí** být splněn jediný implikant — každý implikant implikuje pravdivost celku. Aby formule v KNT byla pravdivá, **musí** být splněna každá klausule — každá je nutnou podmínkou.

### 5.2 Převod do DNT/KNT

**Postup:**
1. Eliminujeme $\Leftrightarrow$ pomocí $A \Leftrightarrow B \equiv (A \Rightarrow B) \land (B \Rightarrow A)$.
2. Eliminujeme $\Rightarrow$ pomocí $A \Rightarrow B \equiv \neg A \lor B$.
3. Vtáhneme negace dovnitř pomocí De Morganových zákonů, použijeme dvojí negaci.
4. Roznásobíme distributivními zákony: $\land$ přes $\lor$ pro DNT, $\lor$ přes $\land$ pro KNT.
5. Implikanty/klausule, které jsou kontradikcí/tautologií, vyloučíme. Použijeme absorpci.

**Mezi DNT a KNT** se přechází opakovanou aplikací distributivních zákonů.

**Z DNT do KNT negace:** Pokud $F$ je v DNT, $\neg F$ získáme De Morganem v KNT.

**Věta (Každou formuli lze převést do DNT i KNT):** Ke každé výrokové formuli existuje logicky ekvivalentní formule v DNT a logicky ekvivalentní formule v KNT. (Dokáže se strukturální indukcí.)

### 5.3 Příklady

**$A \Rightarrow (\neg B \land C)$:**

$$A \Rightarrow (\neg B \land C) \equiv \neg A \lor (\neg B \land C) \quad \text{(DNT)}$$
$$\equiv (\neg A \lor \neg B) \land (\neg A \lor C) \quad \text{(KNT)}.$$

**$A \Leftrightarrow B$:**

$$A \Leftrightarrow B \equiv (A \Rightarrow B) \land (B \Rightarrow A) \equiv (\neg A \lor B) \land (\neg B \lor A) \quad \text{(KNT)}$$
$$\equiv (A \land B) \lor (\neg A \land \neg B) \quad \text{(DNT)}.$$

### 5.4 Jednoznačnost

**Pozn.** DNT ani KNT **nejsou jednoznačné**. Například $A \equiv A \lor (A \land B) \equiv A \land (A \lor B)$ — v DNT i KNT tu existují různé tvary.

---

## 6. Úplné normální tvary

### 6.1 Minterm, maxterm

**Definice (Minterm, ÚDNT):** Buď $F$ výroková formule s prvotními formulemi $P_1, \dots, P_n$.
- **Minterm** formule $F$ je implikant, který obsahuje **všechny prvotní formule** $P_1, \dots, P_n$ (každou právě jednou, případně znegovanou).
- Formule je v **úplném DNT (ÚDNT)**, je-li mintermem nebo disjunkcí různých (logicky neekvivalentních) mintermů.

**Definice (Maxterm, ÚKNT):**
- **Maxterm** formule $F$ je klausule, která obsahuje všechny prvotní formule $P_1, \dots, P_n$ právě jednou.
- Formule je v **úplném KNT (ÚKNT)**, je-li maxtermem nebo konjunkcí různých maxtermů.

**Konvence pro krajní případy:** $\bot$ považujeme za ÚDNT kontradikce (prázdná disjunkce mintermů), $\top$ za ÚKNT tautologie.

### 6.2 Existence a jednoznačnost

**Věta (Každou formuli lze převést do ÚDNT i ÚKNT):** Ke každé výrokové formuli existuje formule logicky ekvivalentní v ÚDNT a formule logicky ekvivalentní v ÚKNT.

**Idea důkazu (pro ÚDNT):**
1. Převedeme $F$ do DNT (Věta 2.11).
2. Implikanty, které jsou kontradikcemi, vyloučíme. Zbylé implikanty doplníme o chybějící prvotní formule pomocí
   $$A \equiv A \land \top \equiv A \land (B \lor \neg B) \equiv (A \land B) \lor (A \land \neg B),$$
   opakujeme pro všechny chybějící $B$.
3. Duplicitní mintermy odstraníme.

Pro ÚKNT analogicky s $A \equiv A \lor \bot \equiv A \lor (B \land \neg B) \equiv (A \lor B) \land (A \lor \neg B)$.

**Důsledek (Jednoznačnost):** Úplné DNT a úplný KNT formule $F$ jsou určeny **jednoznačně**, a to až na pořadí mintermů (maxtermů) a pořadí literálů v nich.

### 6.3 Vztah k pravdivostní tabulce

**Pozorování (ÚDNT vs. pravdivostní tabulka):** Buď $F$ formule v ÚDNT s $n$ prvotními formulemi.
- Každý minterm odpovídá **jednomu řádku** tabulky, ve kterém je $F$ pravdivá — pro různá ohodnocení jsou pravdivé různé mintermy.
- Formule je pravdivá pro tolik ohodnocení, kolik má mintermů.

**Pozorování (ÚKNT vs. tabulka):** Každý maxterm v ÚKNT odpovídá jednomu řádku, kde $F = 0$. Počet maxtermů = počet ohodnocení, pro která $F = 0$.

**Důsledek:** Pro $F$ s $n$ prvotními formulemi platí
$$|\text{mintermy ÚDNT}| + |\text{maxtermy ÚKNT}| = 2^n.$$

**Jak číst ÚDNT z tabulky:** Pro každý řádek s $F = 1$ vytvoříme minterm — kde proměnná = 1, vezmeme ji bez negace; kde = 0, vezmeme znegovanou. Disjunkce všech mintermů dá ÚDNT.

**Jak číst ÚKNT z tabulky:** Pro každý řádek s $F = 0$ vytvoříme maxterm — kde proměnná = 0, vezmeme ji bez negace; kde = 1, vezmeme znegovanou. Konjunkce všech maxtermů dá ÚKNT.

### 6.4 Charakterizace ekvivalence a důsledku přes úplné NT

**Věta (Ekvivalence pomocí ÚNT):** Buďte $A, B$ výrokové formule se stejnými prvotními formulemi. Pak
1. $A \equiv B$ právě tehdy, když jejich ÚDNT obsahují stejné mintermy.
2. $A \equiv B$ právě tehdy, když jejich ÚKNT obsahují stejné maxtermy.

**Věta (Důsledek pomocí ÚNT):** Při stejných prvotních formulích platí:
1. $A \models B$ právě tehdy, když všechny mintermy ÚDNT $A$ jsou obsaženy v ÚDNT $B$.
2. $A \models B$ právě tehdy, když všechny maxtermy ÚKNT $B$ jsou obsaženy v ÚKNT $A$.

**Důkaz:** Plyne z jednoznačnosti ÚNT a z toho, že množina ohodnocení, pro která $A = 1$ ($\subseteq$ pro důsledek), je popsána právě mintermy ÚDNT.

### 6.5 Příklad — důsledek pomocí ÚKNT

Mějme $F_1 = A \Rightarrow (B \Rightarrow C)$, $F_3 = (A \land B) \Rightarrow C$.

$$F_1 \equiv \neg A \lor \neg B \lor C \quad (\text{ÚKNT, jediný maxterm}),$$
$$F_3 \equiv \neg(A \land B) \lor C \equiv \neg A \lor \neg B \lor C \quad (\text{stejný ÚKNT}).$$

Stejné ÚKNT $\Rightarrow F_1 \equiv F_3$.

### 6.6 Minimalizace normálních tvarů

Úplné tvary jsou užitečné, ale často zbytečně dlouhé. Lze je zjednodušit aplikací logických zákonů, typicky hledáním dvojic mintermů lišících se jedním literálem:
$$(F \land A) \lor (F \land \neg A) \equiv F \land (A \lor \neg A) \equiv F.$$

V praxi se k minimalizaci používají algoritmy jako Karnaughovy mapy nebo Quine–McCluskey.

---

## 7. Co je potřeba na zkoušku znát

### Definice
- Výroková formule, ohodnocení, $\top$, $\bot$.
- Tautologie, splnitelná formule, kontradikce.
- Logická ekvivalence ($\equiv$) a logický důsledek ($\models$).
- Universální systém spojek (USS).
- Shefferův symbol $\uparrow$ (NAND), Peirceova šipka $\downarrow$ (NOR).
- Literál, implikant, klausule.
- DNT, KNT.
- Minterm, maxterm, ÚDNT, ÚKNT.

### Klíčové věty
- $E \equiv F \iff E \Leftrightarrow F$ je tautologie.
- $E \models F \iff E \Rightarrow F$ je tautologie $\iff E \land \neg F$ je kontradikce.
- $\{\neg, \lor\}$, $\{\neg, \land\}$, $\{\neg, \Rightarrow\}$ jsou (dvouprvkové) USS.
- $\uparrow$ a $\downarrow$ tvoří jednoprvkové USS a jsou jediné takové binární spojky.
- Každou formuli lze převést do DNT i do KNT.
- Každou formuli lze převést do ÚDNT i ÚKNT, **jednoznačně** (až na pořadí).
- $A \equiv B \iff$ stejné mintermy ÚDNT (resp. maxtermy ÚKNT).
- $A \models B \iff$ mintermy $A$ $\subseteq$ mintermy $B$ (resp. maxtermy $B$ $\subseteq$ maxtermy $A$).
- Počet mintermů ÚDNT + počet maxtermů ÚKNT = $2^n$.

### Klíčové zákony
- Vyloučení sporu/třetího, dvojí negace.
- Komutativní, asociativní, distributivní zákony.
- De Morganovy zákony.
- Kontrapozice, implikace jako disjunkce.
- Modus ponens, modus tollens, hypotetický sylogismus.

### Algoritmy a postupy
- Převod do DNT/KNT: eliminace $\Leftrightarrow, \Rightarrow$ → De Morgan → distributivita.
- Doplnění DNT na ÚDNT pomocí $A \equiv (A \land B) \lor (A \land \neg B)$.
- Čtení ÚDNT/ÚKNT přímo z pravdivostní tabulky.
