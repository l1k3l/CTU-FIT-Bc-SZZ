---
tags: [otázka, kurz/AAG, otázka/1, hotovo]
---

# 1 — Regulární jazyky (zkrácená verze)

## 1. Základní pojmy

- **Abeceda** $\Sigma$ konečná, **slovo** $w \in \Sigma^*$, **jazyk** $L \subseteq \Sigma^*$.
- Operace: $\cup, \cap, \setminus, \overline{\cdot}, \cdot$ (zřetězení), $L^n$, $L^* = \bigcup_{n \ge 0} L^n$, $L^+ = LL^*$.
- **[[Regulární-jazyk|Regulární jazyk]]** = jazyk přijímaný KA = popsaný RV = generovaný RG (Kleeneova věta).

---

## 2. [[Konečný-automat|Konečné automaty]]

**DKA:** pětice $M = (Q, \Sigma, \delta, q_0, F)$, $\delta: Q \times \Sigma \to Q$. Úplně určený, pokud $\delta$ je definováno všude.

**NKA:** $\delta: Q \times \Sigma \to 2^Q$. Přijímá, existuje-li akceptující výpočet.

**NKA-$\varepsilon$:** $\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to 2^Q$. **$\varepsilon$-uzávěr** $\varepsilon\text{-Cl}(q)$ = stavy dosažitelné z $q$ jen $\varepsilon$-přechody.

**Konfigurace** $(q, w)$. **Přechod** $(q, aw) \vdash (p, w) \iff \delta(q,a) \ni p$.

**Jazyk:** $L(M) = \{w : (q_0, w) \vdash^* (q, \varepsilon),\ q \in F\}$.

---

## 3. [[Determinizace|Determinizace]] (NKA → DKA)

**Věta:** Ke každému NKA existuje ekvivalentní DKA.

**Podmnožinová konstrukce:** stavy DKA = podmnožiny $Q$. $q'_0 = \{q_0\}$, $\delta'(q', a) = \bigcup_{p \in q'} \delta(p, a)$, $F' = \{q' : q' \cap F \neq \emptyset\}$. Pro NKA-$\varepsilon$ pracujeme s $\varepsilon$-uzávěry.

**Velikost:** v nejhorším případě $2^{|Q|}$ stavů; typicky výrazně méně (jen dosažitelné podmnožiny).

---

## 4. [[Minimalizace-DKA|Minimalizace DKA]]

**Předpoklady:** úplně určený DKA bez nedosažitelných a zbytečných stavů.

**Ekvivalence stavů:** $p \sim q \iff \forall w: \hat\delta(p,w) \in F \Leftrightarrow \hat\delta(q,w) \in F$.

**Algoritmus (rozkladová tabulka):**
1. Počáteční rozklad $\{F, Q \setminus F\}$.
2. Sestav tabulku přechodů, řádky stavů ohodnoceny ID podmnožin, do kterých vedou.
3. Rozděl podmnožiny tak, aby každá obsahovala stavy se shodnými řádky.
4. Opakuj do stabilizace; stavy minimálního DKA = výsledné třídy.

**Věta (jednoznačnost):** Minimální DKA daného jazyka je jednoznačný **až na izomorfismus** (důsledek Myhill–Nerodovy věty).

**Složitost:** $O(|Q|^2 |\Sigma|)$ naivně; Hopcroft $O(|Q| |\Sigma| \log |Q|)$.

---

## 5. Operace s KA (uzavřenost RJ)

| Operace | Konstrukce |
|---|---|
| $\cup$ | nový $q_0$ s $\varepsilon$-přechody do $q_{01}, q_{02}$; **nebo** produkt s $F = (F_1 \times Q_2) \cup (Q_1 \times F_2)$ |
| $\cap$ | produkt s $F = F_1 \times F_2$ |
| $\neg$ | **úplně určený DKA**: prohoď $F \leftrightarrow Q \setminus F$ |
| $\cdot$ | $\varepsilon$-přechody z $F_1$ do $q_{02}$; $F = F_2$ |
| $^*$ | nový $q'_0 \to q_0$ ($\varepsilon$), z $F$ zpět do $q_0$, $F' = F \cup \{q'_0\}$ |
| $\setminus, \triangle$ | $L_1 \setminus L_2 = L_1 \cap \overline{L_2}$ |

**Pozor:** doplněk vyžaduje deterministický **a úplně určený** automat.

---

## 6. [[Regulární-gramatika|Regulární gramatika]] (typ 3)

$G = (N, \Sigma, P, S)$, pravidla **pravolineárně**: $A \to aB$ nebo $A \to a$ (eventuelně $S \to \varepsilon$, pokud $S$ není napravo).

**RG → NKA:** stavy = neterminály + nový koncový $A$; $\delta(B, a) = \{C : B \to aC\} \cup \{A : B \to a\}$.

**NKA → RG:** $N := Q$, $S := q_0$, $P := \{B \to aC : C \in \delta(B,a)\} \cup \{B \to a : \exists C \in \delta(B,a) \cap F\}$.

---

## 7. [[Regulární-výraz|Regulární výraz]] (RV)

**Syntaxe:** $\emptyset, \varepsilon, a$; $(x+y), (xy), (x)^*$. Priorita: $^* > \cdot > +$.

**Sémantika:** $L(\emptyset) = \emptyset$, $L(\varepsilon) = \{\varepsilon\}$, $L(a) = \{a\}$, $L(x+y) = L(x) \cup L(y)$, $L(xy) = L(x) L(y)$, $L(x^*) = L(x)^*$.

**Identity:** $x+x=x$; $x+\emptyset=x$; $x\emptyset = \emptyset$; $x\varepsilon=x$; $\emptyset^* = \varepsilon$; $(x^*)^*=x^*$; $x^* = \varepsilon + xx^*$; $(x+y)^* = (x^*y^*)^*$.

**Kleeneho věta:** RJ $\iff$ KA $\iff$ RG $\iff$ RV.

**RV → NKA:** Glushkov (sousedé), Thompson (induktivně $\varepsilon$-NFA), Brzozowski (derivace).

---

## 8. [[Ardenovo-lemma|Regulární rovnice]] a Ardenovo lemma

**Arden:** Je-li $\varepsilon \notin L(\alpha)$, pak $X = \alpha X + \beta$ má jediné řešení $X = \alpha^* \beta$. (Levá varianta: $X = X\alpha + \beta \Rightarrow X = \beta \alpha^*$.)

**Soustava:** $X_i = \alpha_{i0} + \sum_j \alpha_{ij} X_j$, $1 \le i \le n$. Řešíme **eliminací**: aplikuj Arden na rovnici s rekurzí $X_k = \dots + \alpha_{kk} X_k + \dots$, dosaď do ostatních, opakuj.

**KA → RV:** sestav pro každý $q$ rovnici $X_q = \sum_{a, p \in \delta(q,a)} a X_p\ (+\varepsilon\ \text{pokud}\ q \in F)$; vyřeš pravé soustavy; $V := X_{q_0}$.

**Alternativa KA → RV:** eliminace stavů — odstraňuj postupně stavy, hrany nahrazuj regulárními výrazy popisujícími cesty přes odstraněný stav.

---

## Co odpovědět rychle

- **Determinizace:** podmnožinová konstrukce; $|Q'| \le 2^{|Q|}$.
- **Minimalizace:** rozkladová tabulka, jednoznačně až na izomorfismus.
- **Operace:** $\cup, \cap$ = produkt; $\neg$ = prohoď F (nutně det. + úplně určený); $\cdot, ^*$ = $\varepsilon$-NFA konstrukce.
- **Kleeneova věta:** RJ $\iff$ KA $\iff$ RG $\iff$ RV.
- **Arden:** $X = \alpha X + \beta \Rightarrow X = \alpha^* \beta$.
- **Převody:** RG ↔ NKA triviálně; KA → RV regulární rovnice; RV → KA Glushkov/Thompson.
