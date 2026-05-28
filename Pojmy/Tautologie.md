---
aliases: [tautologie, tautologii, tautologií, tautologiím, tautologiemi, tautologiích, splnitelná, splnitelné, splnitelnou, splnitelnost, splnitelnosti, kontradikce, kontradikci, kontradikcí, kontradikcemi]
tags: [definice, kurz/DML]
---

# Tautologie

Pojem popisující, do jaké míry je výroková formule pravdivá: zda platí vždy (**tautologie**), někdy (**splnitelná**), nebo nikdy (**kontradikce**).

## Definice

Buď $F$ výroková formule. Říkáme, že $F$ je
- **tautologie**, právě když pro každé ohodnocení $v$ platí $v(F) = 1$. Píšeme $F = \top$.
- **splnitelná**, jestliže existuje ohodnocení $v$ takové, že $v(F) = 1$.
- **kontradikce**, právě když pro každé ohodnocení $v$ platí $v(F) = 0$. Píšeme $F = \bot$.

Symboly $\top, \bot$ označují konstantní formule s těmito hodnotami.

## Vzájemné vztahy

1. Negace tautologie je kontradikce, a opačně.
2. Každá tautologie je splnitelná.
3. Žádná splnitelná formule (a tedy ani tautologie) není kontradikce.
4. Žádná kontradikce není splnitelná.

## Příklady

- $A \lor \neg A$ — tautologie (zákon vyloučeného třetího).
- $A \land \neg A$ — kontradikce (zákon vyloučení sporu).
- $A$ — splnitelná, ale ne tautologie.
- $(A \Rightarrow B) \Leftrightarrow (\neg B \Rightarrow \neg A)$ — tautologie (kontrapozice).
- $\neg(A \Rightarrow B) \Leftrightarrow (A \land \neg B)$ — tautologie (negace implikace).

## Charakterizace logické ekvivalence a důsledku

Pro výrokové formule $E, F$ platí:
- $E \equiv F$ (logicky ekvivalentní) $\iff$ $E \Leftrightarrow F$ je tautologie.
- $E \models F$ ($F$ je důsledkem $E$) $\iff$ $E \Rightarrow F$ je tautologie $\iff$ $E \land \neg F$ je kontradikce.

## SAT problém

**SAT** (Boolean satisfiability problem) = rozhodnout, zda zadaná výroková formule je splnitelná. NP-úplný; je-li $n$ prvotních formulí, naivní algoritmus přes pravdivostní tabulku má složitost $\Theta(2^n)$.

## Související

- Související pojmy v rámci VL: literál, klausule, implikant, DNT, KNT, ÚDNT, ÚKNT.
