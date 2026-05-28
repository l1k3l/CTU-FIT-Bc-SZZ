---
aliases: [determinizace, determinizaci, determinizací, podmnožinová konstrukce, podmnožinové konstrukce, subset construction]
tags: [algoritmus, kurz/AAG]
---

# Determinizace

## Definice

**Determinizace** je převod nedeterministického [[Konečný-automat|konečného automatu]] (NKA) na ekvivalentní deterministický (DKA).

**Věta:** Ke každému NKA $M = (Q, \Sigma, \delta, q_0, F)$ existuje ekvivalentní DKA $M'$ takový, že $L(M) = L(M')$.

## Podmnožinová konstrukce

Stavy DKA jsou **podmnožinami** $Q$:
- $q'_0 := \{q_0\}$ (resp. $\varepsilon\text{-Closure}(q_0)$ pro NKA-$\varepsilon$),
- $\delta'(q', a) := \bigcup_{p \in q'} \delta(p, a)$,
- $F' := \{q' \in Q' : q' \cap F \neq \emptyset\}$.

Generujeme pouze **dosažitelné** podmnožiny (BFS od $q'_0$).

## Složitost

V nejhorším případě $|Q'| = 2^{|Q|}$. Typicky vznikne výrazně méně dosažitelných podmnožin. Existují příklady jazyků (např. „$n$-tý znak od konce je 1"), kde exponenciální nárůst nelze obejít.

## Korektnost (skica)

Indukcí podle délky vstupu $w$ se ukáže
$$\hat\delta'(q'_0, w) = \{p \in Q : (q_0, w) \vdash^*_{\text{NKA}} (p, \varepsilon)\},$$
takže $w$ je DKA přijato $\iff$ existuje akceptující výpočet NKA.

## Související
- [[Konečný-automat]]
- [[Minimalizace-DKA]]
- [[Regulární-jazyk]]
