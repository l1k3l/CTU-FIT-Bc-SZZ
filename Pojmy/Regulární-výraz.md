---
aliases: [regulární výraz, regulárního výrazu, regulárnímu výrazu, regulárním výrazem, regulární výrazy, regulárních výrazů, regulárním výrazům, regulárními výrazy, RV, regex]
tags: [definice, kurz/AAG]
---

# Regulární výraz

## Syntaxe (induktivní definice)

Regulární výraz nad abecedou $\Sigma$:
1. $\emptyset$, $\varepsilon$ a každý symbol $a \in \Sigma$ je regulární výraz.
2. Jsou-li $x, y$ regulární výrazy, pak také $(x + y)$, $(x \cdot y)$ a $(x)^*$.

Priorita: $^* > \cdot > +$. Závorky a tečky se vynechávají, je-li to jednoznačné.

## Sémantika

Jazyk přiřazený výrazu $V$:
- $L(\emptyset) = \emptyset$, $L(\varepsilon) = \{\varepsilon\}$, $L(a) = \{a\}$;
- $L(x + y) = L(x) \cup L(y)$;
- $L(x \cdot y) = L(x) \cdot L(y)$;
- $L(x^*) = L(x)^*$.

## Ekvivalence

Dva výrazy jsou **ekvivalentní** ($x = y$), pokud $L(x) = L(y)$. Základní identity:
- $x + x = x$, $x + \emptyset = x$, $x \emptyset = \emptyset$, $x \varepsilon = x$;
- $\emptyset^* = \varepsilon$, $(x^*)^* = x^*$, $x^* = \varepsilon + x x^*$;
- $(x + y)^* = (x^* y^*)^*$, $(xy)^* x = x (yx)^*$.

## Vztah k automatům a gramatikám

**Kleeneho věta:** Jazyk je [[Regulární-jazyk|regulární]] $\iff$ je popsatelný regulárním výrazem $\iff$ je přijímán [[Konečný-automat|konečným automatem]] $\iff$ je generován [[Regulární-gramatika|regulární gramatikou]].

Převod RV → NKA: Glushkovova metoda sousedů, Thompsonova induktivní konstrukce, Brzozowského derivace. Převod KA → RV: [[Ardenovo-lemma|regulární rovnice]] nebo eliminace stavů.

## Související
- [[Regulární-jazyk]]
- [[Konečný-automat]]
- [[Regulární-gramatika]]
- [[Ardenovo-lemma]]
