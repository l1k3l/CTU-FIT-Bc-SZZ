---
aliases: [minimalizace DKA, minimalizace, minimalizaci DKA, minimalizací DKA, minimální DKA, minimálního DKA, minimální automat]
tags: [algoritmus, kurz/AAG]
---

# Minimalizace DKA

## Definice

[[Konečný-automat|DKA]] $M$ je **stavově minimální** pro jazyk $L = L(M)$, pokud neexistuje DKA $M'$ s $L(M') = L$ a $|Q(M')| < |Q(M)|$.

**Ekvivalence stavů:** $p \sim q \iff \forall w \in \Sigma^*: \hat\delta(p, w) \in F \Leftrightarrow \hat\delta(q, w) \in F$. Z $p$ a $q$ je tedy přijímán tentýž zbytek jazyka.

## Věta o jednoznačnosti

**Věta:** Minimální DKA daného regulárního jazyka je **jednoznačně určen až na izomorfismus** (přejmenování stavů). Jeho stavy odpovídají třídám ekvivalence $\sim$.

Důvod: Myhill–Nerodova věta — počet stavů minimálního DKA = počet tříd Myhill–Nerodovy pravé kongruence $\equiv_L$ na $\Sigma^*$.

## Algoritmus (rozkladová tabulka)

**Vstup:** DKA bez nedosažitelných a zbytečných stavů, **úplně určený**.

1. Počáteční rozklad $\{Q \setminus F, F\}$ (vstup $\varepsilon$ rozliší koncové od nekoncových).
2. Sestav tabulku přechodů: každý stav v tabulce s symboly $\Sigma$ jako sloupci; v buňce uvádíme **identifikátor podmnožiny**, ve které leží cíl přechodu.
3. Najdi podmnožinu, jejíž řádky nejsou všechny stejné — rozděl ji na maximální skupiny stavů se shodnými řádky.
4. Opakuj do stabilizace; třídy výsledného rozkladu = stavy minimálního DKA.

**Složitost:** $O(|Q|^2 |\Sigma|)$ naivně; **Hopcroftův** algoritmus $O(|Q| |\Sigma| \log |Q|)$.

## Použití
- Kanonický tvar pro testování ekvivalence dvou DKA (minimalizuj oba a porovnej).
- Optimalizace velikosti automatu před implementací.

## Související
- [[Konečný-automat]]
- [[Determinizace]]
- [[Regulární-jazyk]]
