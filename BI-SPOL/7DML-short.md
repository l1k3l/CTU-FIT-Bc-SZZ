---
tags: [otázka, kurz/DML, otázka/7, todo]
---

# 7 — Výroková logika (zkrácená verze)

## 1. Splnitelnost formulí

Pro výrokovou formuli $F$ a ohodnocení $v$ definujeme:

| Pojem | Definice |
|---|---|
| **Tautologie** | $(\forall v)\,v(F) = 1$, značíme $F = \top$ |
| **Splnitelná** | $(\exists v)\,v(F) = 1$ |
| **Kontradikce** | $(\forall v)\,v(F) = 0$, značíme $F = \bot$ |

**Vztahy:** Negace tautologie = kontradikce a opačně. Každá tautologie je splnitelná. Žádná splnitelná není kontradikce.

**Příklady:** $A \lor \neg A$ tautologie, $A \land \neg A$ kontradikce, $A \Leftrightarrow B$ splnitelná.

**SAT** = rozhodnout, zda je $F$ splnitelná. NP-úplný, redukuje se na něj řada problémů.

## 2. Logická ekvivalence a důsledek

**Definice:**
- $E \equiv F$ (ekvivalence): $(\forall v)\,v(E) = v(F)$.
- $E \models F$ (důsledek): $(\forall v)\,(v(E) = 1 \Rightarrow v(F) = 1)$.

**Charakterizace:**

| | Ekvivalentní podmínka |
|---|---|
| $E \equiv F$ | $E \Leftrightarrow F$ je tautologie |
| $E \models F$ | $E \Rightarrow F$ je tautologie |
| $E \models F$ | $E \land \neg F$ je kontradikce |

**$\equiv$** je reflexivní, symetrická, tranzitivní. **$\models$** je reflexivní a tranzitivní.

**Substituční věta:** $G \equiv G' \Rightarrow F[G] \equiv F[G']$ — lze nahrazovat podformule.

**Klíčové zákony:**

| | |
|---|---|
| Vyloučení sporu | $A \land \neg A \equiv \bot$ |
| Vyloučeného třetího | $A \lor \neg A \equiv \top$ |
| Dvojí negace | $\neg\neg A \equiv A$ |
| De Morgan | $\neg(A \land B) \equiv \neg A \lor \neg B$ |
| | $\neg(A \lor B) \equiv \neg A \land \neg B$ |
| Distributivita | $A \land (B \lor C) \equiv (A \land B) \lor (A \land C)$ |
| Kontrapozice | $A \Rightarrow B \equiv \neg B \Rightarrow \neg A$ |
| Implikace na disj. | $A \Rightarrow B \equiv \neg A \lor B$ |
| Negace implikace | $\neg(A \Rightarrow B) \equiv A \land \neg B$ |
| Ekvivalence | $A \Leftrightarrow B \equiv (A \Rightarrow B) \land (B \Rightarrow A)$ |

**Klasické důsledky:** modus ponens $(A \Rightarrow B) \land A \models B$, modus tollens $(A \Rightarrow B) \land \neg B \models \neg A$, hypotetický sylogismus $(A \Rightarrow B) \land (B \Rightarrow C) \models A \Rightarrow C$.

## 3. Universální systém spojek (USS)

**Definice:** Množina spojek tvoří USS, právě když ke každé formuli existuje logicky ekvivalentní formule používající pouze tyto spojky.

**Hierarchie:**

| Velikost | USS |
|---|---|
| 5 | $\{\neg, \land, \lor, \Rightarrow, \Leftrightarrow\}$ |
| 4 | $\{\neg, \land, \lor, \Rightarrow\}$ |
| 3 | $\{\neg, \land, \lor\}$ |
| 2 | $\{\neg, \lor\}$, $\{\neg, \land\}$, $\{\neg, \Rightarrow\}$ |
| 1 | $\{\uparrow\}$, $\{\downarrow\}$ |

**NAND, NOR:**
$$A \uparrow B := \neg(A \land B), \qquad A \downarrow B := \neg(A \lor B).$$

**Idea důkazu pro $\uparrow$:** $\neg E \equiv E \uparrow E$; $E \land F$ a $E \lor F$ se vyjádří složením (z De Morgana a dvojí negace).

**Věta:** $\uparrow$ a $\downarrow$ jsou jediné binární spojky tvořící jednoprvkový USS.

**Použití:** Stavba procesorů a flash pamětí (NAND/NOR jako jediné stačí).

## 4. DNT a KNT

**Pojmy:**
- **Literál** = $A$ nebo $\neg A$ (prvotní formule, příp. negace).
- **Implikant** = literál nebo konjunkce literálů.
- **Klausule** = literál nebo disjunkce literálů.
- **DNT** = literál / implikant / disjunkce implikantů: $\bigvee_i \bigwedge_j L_{ij}$.
- **KNT** = literál / klausule / konjunkce klausulí: $\bigwedge_i \bigvee_j L_{ij}$.

**Intuice:** V DNT stačí splnit **jeden** implikant ⇒ implikuje pravdivost celku. V KNT musí být **každá** klausule pravdivá ⇒ nutná podmínka.

**Postup převodu:**
1. Eliminuj $\Leftrightarrow$: $A \Leftrightarrow B \equiv (A \Rightarrow B) \land (B \Rightarrow A)$.
2. Eliminuj $\Rightarrow$: $A \Rightarrow B \equiv \neg A \lor B$.
3. Vtáhni negace dovnitř (De Morgan, dvojí negace).
4. Distributivně roznásob ($\land$ přes $\lor$ pro DNT, $\lor$ přes $\land$ pro KNT).
5. Vyhoď kontradikční implikanty / tautologické klausule, použij absorpci.

**Věta:** Každou formuli lze převést do DNT i KNT. Nejsou jednoznačné.

## 5. Úplné normální tvary (ÚDNT, ÚKNT)

**Pojmy:**
- **Minterm** = implikant obsahující **každou** prvotní formuli $P_1, \dots, P_n$ právě jednou (s případnou negací).
- **Maxterm** = klausule obsahující každou prvotní formuli právě jednou.
- **ÚDNT** = minterm nebo disjunkce různých mintermů. **ÚKNT** = maxterm nebo konjunkce různých maxtermů.
- Konvence: $\bot$ je ÚDNT kontradikce, $\top$ je ÚKNT tautologie.

**Věta (existence, jednoznačnost):** Ke každé formuli existuje ÚDNT a ÚKNT, **jednoznačně** (až na pořadí).

**Idea:** Implikant doplníme o chybějící prvotní formule pomocí
$$A \equiv (A \land B) \lor (A \land \neg B),$$
duplicity odstraníme. Pro ÚKNT duálně.

**Vztah k pravdivostní tabulce:**

| | mintermy ÚDNT | maxtermy ÚKNT |
|---|---|---|
| počet | # řádků s $F = 1$ | # řádků s $F = 0$ |
| součet | $|\text{min}| + |\text{max}| = 2^n$ |

**Z tabulky:** Pro $F = 1$: minterm = $\bigwedge$ proměnných (znegovaných tam, kde $= 0$). Pro $F = 0$: maxterm = $\bigvee$ proměnných (znegovaných tam, kde $= 1$).

**Ekvivalence a důsledek přes ÚNT:**

| | Podmínka |
|---|---|
| $A \equiv B$ | $A_d, B_d$ mají stejné mintermy (resp. $A_k, B_k$ stejné maxtermy) |
| $A \models B$ | mintermy $A_d$ ⊆ mintermy $B_d$ |
| $A \models B$ | maxtermy $B_k$ ⊆ maxtermy $A_k$ |

---

## Co odpovědět rychle

- **Tautologie** vždy 1, **kontradikce** vždy 0, **splnitelná** alespoň pro jedno $v$. $\neg(\text{taut}) = $ kontradikce.
- **$E \equiv F \iff (E \Leftrightarrow F) = \top$**, $E \models F \iff (E \Rightarrow F) = \top \iff (E \land \neg F) = \bot$.
- **USS** = množina spojek, jíž lze vyjádřit libovolnou formuli. $\{\neg, \lor\}, \{\neg, \land\}, \{\neg, \Rightarrow\}$ dvouprvkové; $\{\uparrow\}$ NAND a $\{\downarrow\}$ NOR jednoprvkové (jediné).
- **DNT** = disjunkce konjunkcí literálů (OR-AND), **KNT** = konjunkce disjunkcí literálů (AND-OR). Převod: zbav se $\Leftrightarrow, \Rightarrow$, vtáhni negace, roznásob distributivně.
- **ÚDNT/ÚKNT**: každý implikant/klausule obsahuje **všechny** prvotní formule. **Jednoznačné** až na pořadí.
- **Mintermy ÚDNT** ↔ řádky tabulky s $F = 1$. **Maxtermy ÚKNT** ↔ řádky s $F = 0$. Součet $= 2^n$.
- **Ekvivalence ⇔ stejné mintermy/maxtermy**, **důsledek ⇔ inkluze mintermů (resp. opačně maxtermů)**.
