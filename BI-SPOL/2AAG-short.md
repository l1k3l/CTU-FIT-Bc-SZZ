---
tags: [otázka, kurz/AAG, otázka/2, hotovo]
---

# 2 — Bezkontextové jazyky (zkrácená verze)

## 1. [[Bezkontextová-gramatika|Bezkontextová gramatika]] (BG, typ 2)

$G = (N, \Sigma, P, S)$, pravidla **$A \to \alpha$**, $A \in N$, $\alpha \in (N \cup \Sigma)^*$.

**Derivace:** $\gamma A \delta \Rightarrow \gamma \alpha \delta$. Tranzitivní uzávěry $\Rightarrow^+, \Rightarrow^*$. **Levá / pravá** derivace přepisuje vždy nejlevější / nejpravější neterminál.

**Větná forma:** $S \Rightarrow^* \alpha$; **věta:** $w \in \Sigma^*$.

**$L(G) = \{w \in \Sigma^* : S \Rightarrow^* w\}$.**

**[[Derivační-strom|Derivační strom]]:** kořen $S$, vnitřní uzly neterminály, listy zleva doprava tvoří výsledek (yield). Bijekce: strom ↔ levá derivace ↔ pravá derivace. **Rozklad** = posloupnost čísel pravidel.

**Víceznačnost:** $\exists w \in L(G)$ se dvěma různými derivačními stromy. Příklad: dangling else. Některé jazyky jsou **inherentně víceznačné**. Ambiguita BG je **nerozhodnutelná**.

---

## 2. Úpravy BG

| Krok | Smysl |
|---|---|
| **Test prázdnosti** | $N_t := \{A : A \Rightarrow^* w \in \Sigma^*\}$; $L(G) \neq \emptyset \iff S \in N_t$ |
| **Nedostupné symboly** | $V := \{X : S \Rightarrow^* \alpha X \beta\}$; odstraň ostatní |
| **Zbytečné symboly** | nejprve neproduktivní, **pak** nedostupné (pořadí důležité!) |
| **$\varepsilon$-pravidla** | spočti $N_\varepsilon := \{A : A \Rightarrow^* \varepsilon\}$, expanduj pravidla na varianty s/bez výskytů z $N_\varepsilon$; přidej $S' \to S \mid \varepsilon$, je-li $\varepsilon \in L(G)$ |
| **Jednoduchá pravidla** | spočti $N_A := \{B : A \Rightarrow^* B\ \text{přes unit pravidla}\}$; přidej nejednoduchá pravidla z $N_A$ |

**Vlastní BG:** bez cyklů ($\neg A \Rightarrow^+ A$), bez $\varepsilon$-pravidel, bez zbytečných symbolů. **Věta:** Každý CFL má vlastní gramatiku.

---

## 3. [[Chomského-NF|Chomského normální forma]] (ChNF)

Pravidla mají tvar $A \to BC$, $A \to a$, $S \to \varepsilon$ (jen pokud $\varepsilon \in L(G)$ a $S$ není napravo).

**Věta:** Každý CFL má gramatiku v ChNF.

**Převod:** dlouhá pravidla $A \to X_1\dots X_k$ ($k > 2$) rozsekni pomocnými neterminály $Y_{X_2\dots X_k}, Y_{X_3\dots X_k}, \dots$; každý terminál ve smíšeném pravidle nahraď neterminálem $a'$ s pravidlem $a' \to a$.

---

## 4. [[Zásobníkový-automat|Zásobníkový automat]] (ZA, PDA)

**Sedmice** $R = (Q, \Sigma, G, \delta, q_0, Z_0, F)$. Přechodová funkce $\delta : Q \times (\Sigma \cup \{\varepsilon\}) \times G^* \to 2^{Q \times G^*}$ (nahrazuje řetězec na vrcholu).

**Konfigurace** $(q, w, \alpha)$. **Přechod**
$$(q, aw', \alpha\beta) \vdash (p, w', \gamma\beta) \iff (p, \gamma) \in \delta(q, a, \alpha),\ a \in \Sigma \cup \{\varepsilon\}.$$

**Dva mody přijímání:**
- **koncovým stavem** $L(R) = \{w : (q_0, w, Z_0) \vdash^* (q, \varepsilon, \gamma),\ q \in F\}$,
- **prázdným zásobníkem** $L_\varepsilon(R) = \{w : (q_0, w, Z_0) \vdash^* (q, \varepsilon, \varepsilon)\}$.

**Věta:** Mody jsou ekvivalentní — konstrukce pomocí nového dna $X_0$ a vyprazdňovacího / koncového stavu.

---

## 5. Varianty ZA

**Deterministický ZA (DZA):** $|\delta(q,a,\gamma)| \le 1$ a žádné dvě klauzule $\delta(q,a,\alpha), \delta(q,a/\varepsilon,\beta)$ nemají $\alpha, \beta$ v prefixovém vztahu.

**DCFL** = jazyky přijímané DZA koncovým stavem. **DCFL $\subsetneq$ CFL**:
- DCFL uzavřena na **doplněk** (CFL ne).
- DCFL **neuzavřena** na $\cup$ a $\cap$.
- $\{ww^R\}$ je v CFL, ale ne v DCFL.

Pro DZA: přijímání koncovým stavem $\neq$ prázdným zásobníkem.

---

## 6. BG ↔ ZA

**Věta:** $L$ je bezkontextový $\iff$ $\exists$ ZA $R: L = L_\varepsilon(R)$ (resp. $L(R)$).

**Konstrukce A (top-down, jednostavový):**
$$R = (\{q\}, \Sigma, N \cup \Sigma, \delta, q, S, \emptyset),$$
$\delta(q, \varepsilon, A) = \{(q, \alpha) : A \to \alpha \in P\}$ (expanze), $\delta(q, a, a) = \{(q, \varepsilon)\}$ (srovnání). Expanze odpovídají **levému rozkladu**.

**Konstrukce B (bottom-up, dvoustavový):**
$$R = (\{q, r\}, \Sigma, N \cup \Sigma \cup \{\#\}, \delta, q, \#, \{r\}),$$
$\delta(q, a, \varepsilon) = \{(q, a)\}$ (shift), $\delta(q, \varepsilon, \alpha) = \{(q, A) : A \to \alpha \in P\}$ (reduce), $\delta(q, \varepsilon, \#S) = \{(r, \varepsilon)\}$ (accept). Redukce v reverzním pořadí = **pravý rozklad**.

---

## 7. Modely syntaktické analýzy

**Parsing** = konstrukce derivačního stromu věty.

| Strategie | Buduje | ZA | Praxe |
|---|---|---|---|
| **top-down** | levou derivaci | top-down (§6 A) | rekurzivní sestup, LL($k$) |
| **bottom-up** | pravou derivaci | bottom-up (§6 B) | shift-reduce, LR($k$), SLR, LALR |

**Deterministické metody:**
- **LL($k$)** — top-down, $k$ symbolů lookaheadu; vyžaduje bezlevě rekurzivní BG; LL(1) ⇔ $s$-gramatika (každé pravidlo začíná unikátním terminálem).
- **LR($k$)** — bottom-up; **LR(1) přesně = DCFL** (Knuth). Praktické: SLR, LALR (Yacc/Bison).

**Obecné metody** (libovolná BG):
- **CYK** ($O(n^3)$, vyžaduje ChNF), dynamické programování zdola nahoru.
- **Earley** ($O(n^3)$ obecně, $O(n^2)$ pro jednoznačné, $O(n)$ pro LR($k$)).

### CYK
Tabulka $T[j, i]$ = neterminály derivující $x_j \dots x_{j+i-1}$.
- $T[j, 1] := \{A : A \to x_j \in P\}$,
- $T[j, i] := \{A : A \to BC \in P,\ B \in T[j, k],\ C \in T[j+k, i-k],\ 1 \le k < i\}$.
- $x \in L(G) \iff S \in T[1, n]$.

**Složitost:** $O(n^3 |G|)$.

---

## 8. Uzavřenost

**CFL uzavřena na:** $\cup, \cdot, ^*$ (konstrukce nového $S$).
**CFL NEUZAVŘENA na:** $\cap, \neg$. (Protipříklad: $\{a^n b^n c^n\}$.)

**DCFL uzavřena na:** $\neg$.
**DCFL NEUZAVŘENA na:** $\cup, \cap$.

---

## Co odpovědět rychle

- **BG** = pravidla $A \to \alpha$. **L(G)**, levá/pravá derivace, derivační strom, víceznačnost.
- **Vlastní BG:** bez cyklů, bez $\varepsilon$, bez zbytečných symbolů.
- **ChNF:** $A \to BC \mid a$. CYK $O(n^3)$.
- **ZA:** sedmice; přijetí koncovým stavem ekvivalentní s přijetím prázdným zásobníkem.
- **CFG ↔ ZA:** top-down jednostavový (expanze/srovnání) ↔ levý rozklad; bottom-up dvoustavový (shift/reduce/accept) ↔ pravý rozklad.
- **DZA, DCFL ⊊ CFL.** DCFL uzavřena na $\neg$; CFL ne.
- **Modely analýzy:** top-down (LL), bottom-up (LR); obecně CYK/Earley.
