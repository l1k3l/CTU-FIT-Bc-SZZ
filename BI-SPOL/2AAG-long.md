---
tags: [otázka, kurz/AAG, otázka/2, hotovo]
---

# Bezkontextové jazyky

> **Otázka SZZ:** Bezkontextové jazyky: Bezkontextové gramatiky, zásobníkové automaty a jejich varianty. Modely syntaktické analýzy bezkontextových jazyků.

Zdroje: BI-AAG přednášky 1, 7, 8 (Holub, FIT ČVUT) — základní pojmy a Chomského hierarchie, bezkontextové gramatiky a jejich úpravy, zásobníkové automaty a modely syntaktické analýzy.

---

## 1. Bezkontextová gramatika (BG, CFG)

### 1.1 Definice
**[[Gramatika|Gramatika]]** je čtveřice $G = (N, \Sigma, P, S)$:
- $N$ — konečná množina **neterminálů**,
- $\Sigma$ — konečná množina **terminálů**, $N \cap \Sigma = \emptyset$,
- $P$ — konečná množina **přepisovacích pravidel**,
- $S \in N$ — **počáteční (startovací) neterminál**.

**[[Bezkontextová-gramatika|Bezkontextová gramatika]]** (typ 2 Chomského hierarchie) má každé pravidlo tvaru
$$A \to \alpha, \qquad A \in N,\ \alpha \in (N \cup \Sigma)^*.$$
Na pravé straně může být cokoli (včetně $\varepsilon$); levá strana je jeden neterminál — odtud „bezkontextová".

### 1.2 Derivace
**Přímá derivace** $\gamma A \delta \Rightarrow \gamma \alpha \delta$, je-li $(A \to \alpha) \in P$. Označení: $\Rightarrow^k$ ($k$ kroků), $\Rightarrow^+$ (tranzitivní uzávěr), $\Rightarrow^*$ (tranzitivně-reflexivní uzávěr).

- **Větná forma:** $\alpha \in (N \cup \Sigma)^*$ taková, že $S \Rightarrow^* \alpha$.
- **Věta:** větná forma bez neterminálů, $w \in \Sigma^*$.
- **Jazyk:** $L(G) = \{w \in \Sigma^* : S \Rightarrow^* w\}$.

**Levá / pravá derivace:** derivace, ve které je v každém kroku přepisován vždy nejlevější (resp. nejpravější) neterminál.

### 1.3 [[Derivační-strom|Derivační strom]]
Strom, ve kterém
1. kořen je ohodnocen $S$,
2. vnitřní uzly jsou ohodnoceny neterminály, listy terminály nebo $\varepsilon$,
3. pro každý vnitřní uzel ohodnocený $A$ s následovníky zleva doprava $A_1, \dots, A_k$ existuje pravidlo $A \to A_1 \dots A_k \in P$,
4. **výsledek (yield)** stromu = řetězec listů zleva doprava — odpovídá nějaké větné formě.

**Bijekce:** derivační strom $\longleftrightarrow$ levá derivace $\longleftrightarrow$ pravá derivace (jednoznačně). Rozklad věty = posloupnost čísel pravidel použitých při derivaci; **levý rozklad** = pořadí pravidel levé derivace, **pravý rozklad** = obrácené pořadí pravidel pravé derivace.

### 1.4 Víceznačnost (ambiguita)
BG $G$ je **nejednoznačná**, pokud existuje věta $w \in L(G)$, k níž lze sestavit alespoň dva různé derivační stromy. Jinak je **jednoznačná**.

**Příklad „dangling else":** $S \to \mathtt{if}\ b\ \mathtt{then}\ S\ \mathtt{else}\ S \mid \mathtt{if}\ b\ \mathtt{then}\ S \mid a$. Větu `if b then if b then a else a` lze rozklíčovat dvěma způsoby — jednoznačně se odstraní rozdělením $S$ na $S_1$ (může mít `else`) a $S_2$ (nesmí).

**Vlastnosti:**
- Některé jazyky jsou **inherentně nejednoznačné** — neexistuje pro ně žádná jednoznačná BG (např. $\{a^i b^j c^k : i = j \lor j = k\}$).
- **Nerozhodnutelnost:** neexistuje algoritmus rozhodující, zda daná BG je nejednoznačná (redukce z PCP).

---

## 2. Úpravy bezkontextových gramatik

Cílem je převést libovolnou BG na ekvivalentní gramatiku v „pěkném" tvaru, např. **vlastní** nebo v některé **normální formě**.

### 2.1 Test prázdnosti $L(G)$
Spočti množinu $N_t$ neterminálů, ze kterých lze derivovat terminální řetězec:
```
N₀ := ∅
opakuj  Nᵢ := {A : (A → α) ∈ P, α ∈ (Nᵢ₋₁ ∪ Σ)*} ∪ Nᵢ₋₁
dokud   Nᵢ = Nᵢ₋₁
L(G) ≠ ∅  ⟺  S ∈ N_t.
```

### 2.2 Nedostupné symboly
$X \in N \cup \Sigma$ je **nedostupný**, neexistuje-li $S \Rightarrow^* \alpha X \beta$.
```
V₀ := {S}
opakuj  Vᵢ := {X : (A → αXβ) ∈ P, A ∈ Vᵢ₋₁} ∪ Vᵢ₋₁
dokud   Vᵢ = Vᵢ₋₁
N' := Vᵢ ∩ N,  Σ' := Vᵢ ∩ Σ.
```

### 2.3 Zbytečné symboly
$X$ je **zbytečný**, pokud neexistuje $S \Rightarrow^* w X y \Rightarrow^* wxy$ s $w, x, y \in \Sigma^*$. Odstraníme:
1. nejprve neproduktivní (z §2.1 — ponecháme jen $N_t$),
2. poté nedostupné (§2.2).

**Pozor na pořadí** — opačně by mohly zůstat symboly nedosažené po odstranění neproduktivních.

**Definice:** $G$ je **redukovaná**, pokud neobsahuje zbytečné symboly.

### 2.4 $\varepsilon$-pravidla
$G$ je **bez $\varepsilon$-pravidel**, jestliže $P$ neobsahuje žádné pravidlo $A \to \varepsilon$, **nebo** obsahuje jediné $S \to \varepsilon$ a $S$ se nevyskytuje na pravé straně.

```
N_ε := nejmenší množina splňující: A ∈ N_ε, pokud (A → α) ∈ P a α ∈ N_ε*.
Pro každé pravidlo A → X₁…Xₙ vygeneruj všechny varianty
  vzniklé vynecháváním libovolných Xᵢ ∈ N_ε; vylučme prázdnou pravou stranu.
Je-li S ∈ N_ε, přidej nový S' s pravidly S' → S | ε.
```

### 2.5 Jednoduchá pravidla
**Jednoduché pravidlo** $A \to B$, $A, B \in N$.
```
Pro každý A spočti N_A := nejmenší množinu obsahující A
   uzavřenou na: jestliže B ∈ N_A a (B → C) ∈ P, pak C ∈ N_A.
Nová pravidla: pro každý A a každý B ∈ N_A převezmi nejednoduchá pravidla
   {A → α : (B → α) ∈ P, α ∉ N}.
```

### 2.6 Vlastní gramatika
**Definice:** $G$ je **vlastní**, pokud je bez cyklů ($\neg \exists A \Rightarrow^+ A$), bez $\varepsilon$-pravidel a bez zbytečných symbolů.

**Věta:** Jestliže $G$ je bez $\varepsilon$-pravidel a bez jednoduchých pravidel, pak je bez cyklů.

**Věta:** Každý bezkontextový jazyk $L$ lze generovat nějakou vlastní gramatikou.

### 2.7 Věta o dosazování
**Věta:** Nechť $(A \to \alpha B \beta) \in P$, $A \neq B$, a nechť $B \to \gamma_1 \mid \dots \mid \gamma_k$ jsou všechna pravidla s $B$ vlevo. Položíme-li
$$P' = (P \setminus \{A \to \alpha B \beta\}) \cup \{A \to \alpha \gamma_i \beta : 1 \le i \le k\},$$
pak $L(G) = L(G')$. (Užitečné technické lemma pro důkazy úprav.)

---

## 3. Chomského normální forma

### 3.1 Definice
BG $G$ je v **Chomského normální formě (ChNF)**, jestliže každé pravidlo má jeden ze tří tvarů:
1. $A \to BC$, $A, B, C \in N$,
2. $A \to a$, $A \in N$, $a \in \Sigma$,
3. $S \to \varepsilon$ — výjimečně, pokud $\varepsilon \in L(G)$, a $S$ se nevyskytuje napravo.

### 3.2 Věta o existenci
**Věta:** Každý bezkontextový jazyk $L$ lze generovat gramatikou v Chomského normální formě.

### 3.3 Algoritmus převodu
Předpoklad: vlastní BG bez jednoduchých pravidel.
```
1. Pravidla A → BC a A → a zachovej; zachovej S → ε, pokud existuje.
2. Pro každé pravidlo A → X₁ X₂ … Xₖ s k > 2:
     zaveď pomocné neterminály Y_{X₂…Xₖ}, Y_{X₃…Xₖ}, …
     a přidej A → X'₁ Y_{X₂…Xₖ}, Y_{X₂…Xₖ} → X'₂ Y_{X₃…Xₖ}, …,
     Y_{Xₖ₋₁ Xₖ} → X'ₖ₋₁ X'ₖ.
3. Každý terminál a ve smíšeném pravidle nahraď novým neterminálem a'
     a přidej pravidlo a' → a.
```

### 3.4 Příklad
$S \to aAB \mid BA$, $A \to BBB \mid a$, $B \to AS \mid b$ se převede na ChNF:
$$\{ S \to a'Y_{AB} \mid BA,\ A \to BY_{BB} \mid a,\ B \to AS \mid b,\ Y_{AB} \to AB,\ Y_{BB} \to BB,\ a' \to a \}.$$

---

## 4. Zásobníkový automat (ZA, PDA)

### 4.1 Definice
**[[Zásobníkový-automat|Zásobníkový automat]]** je sedmice
$$R = (Q, \Sigma, G, \delta, q_0, Z_0, F),$$
kde
- $Q$ — konečná množina vnitřních stavů,
- $\Sigma$ — vstupní abeceda,
- $G$ — zásobníková abeceda (značíme $G$ podle přednášky, jindy též $\Gamma$),
- $\delta$ — zobrazení z konečné podmnožiny $Q \times (\Sigma \cup \{\varepsilon\}) \times G^*$ do konečných podmnožin $Q \times G^*$,
- $q_0 \in Q$ — počáteční stav,
- $Z_0 \in G$ — počáteční symbol v zásobníku,
- $F \subseteq Q$ — množina koncových stavů.

Přechodová funkce dovoluje **nahradit celý řetězec na vrcholu zásobníku**:
$$\delta(q, a, \alpha) \ni (p, \gamma)$$
říká, že ve stavu $q$ přečteme symbol $a \in \Sigma \cup \{\varepsilon\}$, na vrcholu zásobníku máme $\alpha$, přejdeme do stavu $p$ a vrchol nahradíme řetězcem $\gamma$.

### 4.2 Konfigurace a přechod
**Konfigurace:** $(q, w, \alpha) \in Q \times \Sigma^* \times G^*$.

**Počáteční konfigurace:** $(q_0, w, Z_0)$.

**Přechod** $\vdash_R$ je definován vztahem
$$(q, aw', \alpha\beta) \vdash_R (p, w', \gamma\beta) \iff (p, \gamma) \in \delta(q, a, \alpha),\ a \in \Sigma \cup \{\varepsilon\}.$$
$\vdash^*$ je tranzitivně-reflexivní uzávěr.

**Důležitá vlastnost (zásobníková lokálnost):** Pokud $(q, w, A) \vdash^n (q', \varepsilon, \varepsilon)$, pak také $(q, w, A\alpha) \vdash^n (q', \varepsilon, \alpha)$ pro libovolné $\alpha$. Obsah pod aktuálním vrcholem výpočet neovlivňuje.

### 4.3 Přijímané jazyky
ZA definuje **dva** jazyky:

1. **Přijetí koncovým stavem** (acceptance by final state):
$$L(R) = \{w : (q_0, w, Z_0) \vdash^* (q, \varepsilon, \gamma),\ q \in F\}.$$

2. **Přijetí prázdným zásobníkem** (acceptance by empty stack):
$$L_\varepsilon(R) = \{w : (q_0, w, Z_0) \vdash^* (q, \varepsilon, \varepsilon)\}.$$

V druhém případě je $F$ obvykle $\emptyset$ (nehraje roli).

### 4.4 Ekvivalence obou modů přijímání
**Věta:** Jazyk $L$ je přijímán nějakým ZA s koncovým stavem $\iff$ je přijímán nějakým ZA s prázdným zásobníkem.

**Konstrukce $L(P_f) = L_\varepsilon(P_\varepsilon)$:** přidá se nový start $q'_0$ s $\varepsilon$-přechodem, který vloží $Z_0$ nad nové dno $X_0 \notin G$; ze všech koncových stavů $q \in F$ pak vede $\varepsilon$-přechod do nového vyprazdňovacího stavu $q_\varepsilon$, který $\varepsilon$-přechody zlikviduje obsah zásobníku.

**Konstrukce $L_\varepsilon(P_\varepsilon) = L(P_f)$:** opět dno $X_0$, ze stavů, ve kterých původní automat měl vyprázdněný zásobník (tj. $X_0$ na vrcholu), přejdi $\varepsilon$-přechodem do nového koncového stavu $q_f$.

---

## 5. Varianty ZA

### 5.1 Deterministický ZA (DZA)
**Definice:** $R$ je **deterministický**, jestliže:
1. $|\delta(q, a, \gamma)| \le 1$ pro každé $(q, a, \gamma)$.
2. Pokud $\delta(q, a, \alpha) \neq \emptyset$ a $\delta(q, a, \beta) \neq \emptyset$ pro různá $\alpha, \beta \in G^*$, pak ani jeden z $\alpha, \beta$ není **prefixem** druhého.
3. Pokud $\delta(q, a, \alpha) \neq \emptyset$ a $\delta(q, \varepsilon, \beta) \neq \emptyset$, pak opět $\alpha, \beta$ nesmí být prefix jeden druhého.

Podmínky 2, 3 jsou nutné kvůli tomu, že $\delta$ pracuje s celými řetězci na vrcholu zásobníku — jinak by se mohly použít dva přechody současně.

### 5.2 Deterministické bezkontextové jazyky (DCFL)
Třída jazyků přijímaných DZA s koncovým stavem se nazývá **deterministická bezkontextová** (DCFL).

**Vlastnosti:**
- $\text{DCFL} \subsetneq \text{CFL}$ — vlastní podtřída. Klasický příklad CFL mimo DCFL: $\{w w^R : w \in \{a,b\}^*\}$ (palindromy bez explicitního středu).
- DCFL je uzavřena na **doplněk** (na rozdíl od obecných CFL!).
- DCFL **není** uzavřena na sjednocení a průnik.
- Pro DZA se rozlišuje přijímání koncovým stavem vs. prázdným zásobníkem — nejsou ekvivalentní (s prázdným zásobníkem deterministický automat nepřijme žádný řetězec, jehož vlastní prefix je také přijímán).

### 5.3 Rozšířený ZA, jednostavový ZA
Drobné varianty:
- **Jednostavový ZA** ($|Q| = 1$) — postačuje pro CFG → ZA (top-down konstrukce, §6.2).
- **Dvoustavový ZA** — používá konstrukce bottom-up (§6.3).
- **Rozšířený ZA** — vrchol zásobníku je obecný řetězec; standardní v Holubovo definici.

---

## 6. Vztah BG ↔ ZA

**Věta:** Pro každou BG $G$ existuje ZA $R$ takový, že $L_\varepsilon(R) = L(G)$. (A naopak: jazyk přijímaný libovolným ZA je bezkontextový.)

**Důsledek:** Třída CFL = jazyky generované BG = jazyky přijímané ZA.

Přednáška BI-AAG ukazuje **dvě konstrukce** BG $\to$ ZA odpovídající dvěma modelům syntaktické analýzy.

### 6.1 Konstrukce A: top-down (syntaktická analýza shora dolů)
$$R = (\{q\}, \Sigma, N \cup \Sigma, \delta, q, S, \emptyset),$$
kde
- $\delta(q, \varepsilon, A) := \{(q, \alpha) : (A \to \alpha) \in P\}$ pro každý $A \in N$ — **expanze**,
- $\delta(q, a, a) := \{(q, \varepsilon)\}$ pro každý $a \in \Sigma$ — **srovnání**.

Vrchol zásobníku se kreslí **vlevo**. ZA má jediný stav, na začátku je v zásobníku $S$. Posloupnost expanzí použitých během akceptujícího výpočtu odpovídá přesně **levému rozkladu** věty.

**Příklad** — aritmetické výrazy:
$E \to E+T \mid T$, $T \to T*F \mid F$, $F \to (E) \mid a$. Pravidla očíslujeme $1..6$. Akceptující výpočet na vstupu `a+a*a`:
```
(q, a+a*a, E)  ⊢ (q, a+a*a, E+T)   pravidlo 1
               ⊢ (q, a+a*a, T+T)   pravidlo 2
               ⊢ (q, a+a*a, F+T)   pravidlo 4
               ⊢ (q, a+a*a, a+T)   pravidlo 6
               ⊢ (q,  +a*a,  +T)   srovnání
               ⊢ (q,   a*a,   T)   srovnání
               ⊢ … ⊢ (q, ε, ε).
```
Levý rozklad: $1, 2, 4, 6, 3, 4, 6, 6$.

### 6.2 Konstrukce B: bottom-up (syntaktická analýza zdola nahoru)
$$R = (\{q, r\}, \Sigma, N \cup \Sigma \cup \{\#\}, \delta, q, \#, \{r\}),$$
kde
- $\delta(q, a, \varepsilon) := \{(q, a)\}$ pro $a \in \Sigma$ — **přesun (shift)**,
- $\delta(q, \varepsilon, \alpha) := \{(q, A) : (A \to \alpha) \in P\}$ — **redukce (reduce)**,
- $\delta(q, \varepsilon, \#S) := \{(r, \varepsilon)\}$ — **přijetí (accept)**.

Tento ZA přijímá **koncovým stavem** $r$. Symbol $\#$ slouží jako dno zásobníku. Posloupnost redukcí v opačném pořadí odpovídá **pravému rozkladu** věty.

Pro stejnou aritmetickou gramatiku platí: na vstupu `a+a*a` proběhne sled shift–reduce, výsledkem je pravá derivace s reverzním rozkladem $6,4,2,6,4,6,3,1$.

### 6.3 Náznak opačného směru (ZA → CFG)
Klasická konstrukce (mimo BI-AAG) zavádí pro každou trojici $[q, A, p]$ neterminál reprezentující „od stavu $q$ s $A$ na vrcholu se přejde do stavu $p$ a $A$ je z vrcholu odebráno". Pravidla simulují přechody ZA. Důsledek: každý jazyk přijímaný NZA je bezkontextový — uzavírá ekvivalenci.

---

## 7. Modely syntaktické analýzy

**Syntaktická analýza (parsing) = konstrukce derivačního stromu vstupní věty $w$** v zadané gramatice (tedy ověření $w \in L(G)$ a získání struktury).

### 7.1 Dvě hlavní strategie
| Strategie | Co staví | Použitý ZA | Praktické varianty |
|---|---|---|---|
| **Shora dolů (top-down)** | levou derivaci | top-down ZA (§6.1) | rekurzivní sestup, LL($k$) |
| **Zdola nahoru (bottom-up)** | pravou derivaci | bottom-up ZA (§6.2) | shift-reduce, LR($k$), SLR, LALR |

### 7.2 Deterministická analýza
Pro praktické překladače chceme **deterministický** ZA — pak rozklad běží v lineárním čase. Toho lze dosáhnout pro vlastní podtřídu CFL = **DCFL**.

- **LL($k$) gramatiky:** lze deterministicky analyzovat shora dolů s $k$ symboly lookaheadu. Vyžadují **bezlevě rekurzivní** gramatiky. Příkladem speciální podtřídy je **$s$-gramatika** (každé pravidlo začíná unikátním terminálem) — odpovídá LL(1).
- **LR($k$) gramatiky:** deterministická analýza zdola nahoru. LR(1) přesně pokrývá celou DCFL (Knuth). Praktické podtřídy: **SLR**, **LALR** (Yacc/Bison), **LR(1)**.

Podrobně se LL/LR analyzuje v BI-PJP (top-down) a NI-SYP (bottom-up).

### 7.3 Obecné metody (libovolná BG)
Pokud gramatika není deterministická, lze stále analyzovat v polynomiálním čase:

- **CYK (Cocke–Younger–Kasami)** — dynamické programování zdola nahoru. Vyžaduje BG v **ChNF**. Složitost $O(n^3 |G|)$, kde $n = |w|$.
- **Earleyho algoritmus** — top-down s lookaheadem, pracuje na libovolné BG. $O(n^3)$ obecně, $O(n^2)$ pro jednoznačné, $O(n)$ pro LR($k$).
- **GLR (zobecněné LR)** — paralelní udržování všech možných stavů zásobníku.

### 7.4 Algoritmus CYK

**Vstup:** BG $G = (N, \Sigma, P, S)$ v ChNF; vstupní řetězec $x = x_1 x_2 \dots x_n$.

**Výstup:** rozhodnutí, zda $x \in L(G)$.

**Idea:** Tabulka $T[j, i]$ obsahuje **množinu neterminálů**, ze kterých lze vyderivovat podřetězec $x_j x_{j+1} \dots x_{j+i-1}$ délky $i$ začínající na pozici $j$.

```
1: T[j, 1] := {A : (A → x_j) ∈ P}                   ∀j
2: pro i := 2, …, n:                                // délka podřetězce
3:    pro j := 1, …, n − i + 1:                     // pozice
4:        T[j, i] := ∅
5:        pro k := 1, …, i − 1:                     // místo zlomu
6:            T[j, i] := T[j, i]
                ∪ {A : (A → BC) ∈ P,
                     B ∈ T[j, k], C ∈ T[j + k, i − k]}
7: vrať: x ∈ L(G) ⟺ S ∈ T[1, n].
```

**Složitost:** $O(n^3 \cdot |G|)$ — tři vnořené smyčky $\times$ procházení pravidel.

**Věta:** Pro každou BG $G$ v ChNF existuje algoritmus, který v čase $O(n^3)$ rozhodne, zda dané slovo $x$ délky $n$ patří do $L(G)$.

Rozšířená verze CYK navíc dovoluje **rekonstruovat** derivační strom (uložením pro každý záznam $A \in T[j,i]$ zlomového bodu $k$ a pravidla, kterým bylo dosaženo).

---

## 8. Uzavřenost CFL

**Třída CFL je uzavřena** na:
- **sjednocení**: $G = (N_1 \cup N_2 \cup \{S\}, \Sigma, P_1 \cup P_2 \cup \{S \to S_1 \mid S_2\}, S)$,
- **zřetězení**: $S \to S_1 S_2$,
- **iteraci**: $S' \to S S' \mid \varepsilon$.

**Třída CFL NENÍ uzavřena** na:
- **průnik** (klasický protipříklad $\{a^n b^n c^n\} = \{a^n b^n c^k\} \cap \{a^k b^n c^n\}$),
- **doplněk** (vyplývá z neuzavřenosti na $\cap$, neboť $L_1 \cap L_2 = \overline{\overline{L_1} \cup \overline{L_2}}$).

Naproti tomu **DCFL** je uzavřena na doplněk, ale ne na sjednocení ani průnik.

---

## 9. Co je potřeba na zkoušku znát

### Definice
BG (čtveřice), derivace, levá/pravá derivace, větná forma, věta, $L(G)$, derivační strom, výsledek (yield), víceznačnost, rozklad; zbytečné / nedostupné / $\varepsilon$-pravidlo / jednoduché pravidlo; **vlastní gramatika**; **Chomského NF**; ZA (sedmice), konfigurace, přechod, $L(R)$ vs. $L_\varepsilon(R)$; deterministický ZA; DCFL.

### Věty (s důkazovou skicou)
- **Ekvivalence dvou modů přijímání** ZA (konstrukce s novým dnem a vyprazdňovacím stavem).
- **Věta o dosazování** (nahrazení pravidla $A \to \alpha B \beta$ všemi $A \to \alpha \gamma_i \beta$).
- **Existence vlastní gramatiky** pro každý CFL.
- **Existence Chomského NF** pro každý CFL.
- **Ekvivalence BG ↔ NZA**: jazyk je bezkontextový $\iff$ je přijímaný (nějakým) ZA. Dvě konstrukce CFG → ZA (top-down jednostavový; bottom-up dvoustavový).
- **CYK:** rozhodnutí členství v $O(n^3)$ pro ChNF.
- **Nerozhodnutelnost ambiguity.**
- DCFL $\subsetneq$ CFL; DCFL uzavřena na doplněk, CFL ne.

### Algoritmy
- Test prázdnosti $L(G)$, odstranění nedostupných / zbytečných symbolů.
- Odstranění $\varepsilon$-pravidel a jednoduchých pravidel.
- Převod BG do Chomského NF.
- CYK algoritmus syntaktické analýzy ($O(n^3)$).
- Konstrukce ZA pro BG: top-down (jednostavový, expanze + srovnání) a bottom-up (dvoustavový, shift + reduce + accept).

### Modely syntaktické analýzy
- **Top-down (shora dolů)** $\sim$ levá derivace $\sim$ LL($k$).
- **Bottom-up (zdola nahoru)** $\sim$ pravá derivace $\sim$ LR($k$), SLR, LALR.
- **Obecné metody:** CYK ($O(n^3)$, ChNF), Earley, GLR.
