---
aliases: [konečný automat, konečného automatu, konečnému automatu, konečným automatem, konečné automaty, konečných automatů, konečnými automaty, KA, DKA, NKA, deterministický konečný automat, deterministického konečného automatu, nedeterministický konečný automat, DFA, NFA]
tags: [definice, kurz/AAG]
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

## Související
- [[Regulární-jazyk]]
- [[Determinizace]]
- [[Minimalizace-DKA]]
- [[Regulární-gramatika]]
- [[Regulární-výraz]]
- [[Zásobníkový-automat]]
