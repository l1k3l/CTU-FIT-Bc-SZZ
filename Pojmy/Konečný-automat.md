---
aliases: [konečný automat, konečného automatu, konečnému automatu, konečným automatem, konečné automaty, konečných automatů, konečnými automaty, KA, DKA, NKA, deterministický konečný automat, deterministického konečného automatu, nedeterministický konečný automat, DFA, NFA, Mealyho automat, Mealy, Mealyho, Mooreův automat, Moore, Moorův automat, automat s výstupem, konečný automat s výstupem]
tags: [definice, kurz/AAG, kurz/SAP]
---

# Konečný automat

## Definice

**Deterministický konečný automat (DKA)** je pětice
$$M = (Q, \Sigma, \delta, q_0, F),$$
kde
- $Q$ — konečná neprázdná množina vnitřních **stavů**,
- $\Sigma$ — konečná **vstupní abeceda**,
- $\delta : Q \times \Sigma \to Q$ — **přechodová funkce**,
- $q_0 \in Q$ — **počáteční stav**,
- $F \subseteq Q$ — množina **koncových stavů**.

DKA je **úplně určený**, pokud $\delta(q, a)$ je definováno pro každé $q \in Q, a \in \Sigma$.

**Nedeterministický konečný automat (NKA)** má stejnou strukturu, ale $\delta : Q \times \Sigma \to 2^Q$.

**NKA s $\varepsilon$-přechody (NKA-$\varepsilon$):** $\delta : Q \times (\Sigma \cup \{\varepsilon\}) \to 2^Q$. $\varepsilon$-přechody nečtou vstup. **$\varepsilon$-uzávěr** stavu $q$ = množina stavů dosažitelných z $q$ jen po $\varepsilon$-přechodech.

## Konfigurace a jazyk

**Konfigurace:** $(q, w) \in Q \times \Sigma^*$. **Přechod** $(q, aw') \vdash (p, w')$, je-li $\delta(q, a) = p$ (resp. $p \in \delta(q, a)$).

$$L(M) = \{w \in \Sigma^* : \exists q \in F,\ (q_0, w) \vdash^* (q, \varepsilon)\}.$$

## Ekvivalence DKA a NKA

NKA i DKA přijímají právě tutéž třídu jazyků — **regulární jazyky**. Převod NKA → DKA viz [[Determinizace]] (podmnožinová konstrukce, až $2^{|Q|}$ stavů).

## Použití v SAP — Mealyho a Mooreův automat

V BI-SAP je konečný automat **matematickým modelem [[Sekvenční-obvod|sekvenčního obvodu]]**. Na rozdíl od akceptoru z AAG (který jazyk *přijímá*) jde o **automat s výstupem (převodník, *transducer*)** — má navíc výstupní abecedu a výstupní funkci, žádné koncové stavy ani přijímaný jazyk.

**Definice (5-tice):** $M = \langle X, Y, Q, \delta, \lambda\rangle$, kde
- $X$ — vstupní abeceda, $Y$ — **výstupní abeceda**, $Q$ — konečná množina vnitřních **stavů**,
- $\delta : X \times Q \to Q$ — **přechodová funkce** (následující stav),
- $\lambda$ — **výstupní funkce**.

Podle definičního oboru výstupní funkce $\lambda$ rozlišujeme dva typy:

| | výstupní funkce | výstup závisí na |
|---|---|---|
| **Mealyho automat** | $\lambda : X \times Q \to Y$ | stavu **i vstupu** |
| **Mooreův automat** | $\lambda : Q \to Y$ | **jen** na stavu |

**Rozdíly:** Mooreův automat **nemá přímou vazbu vstup→výstup** — změna vstupu se na výstupu projeví až po aktivní hraně hodin (o jeden takt později než u Mealyho, jehož výstup se mění „hned"). Mooreův automat má pro tutéž funkci **zpravidla více stavů** než ekvivalentní Mealyho. Realizace na úrovni hradel a syntéza viz [[28SAP-long]].

## Související
- [[Regulární-jazyk]]
- [[Determinizace]]
- [[Minimalizace-DKA]]
- [[Regulární-gramatika]]
- [[Regulární-výraz]]
- [[Zásobníkový-automat]]
- [[Sekvenční-obvod]]
- [[Klopný-obvod]]
- [[Čítač]]
