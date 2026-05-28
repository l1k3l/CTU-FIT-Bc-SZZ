---
tags: [otázka, kurz/AAG, otázka/1, hotovo]
---

# Regulární jazyky

> **Otázka SZZ:** Regulární jazyky: Deterministické a nedeterministické konečné automaty. Determinizace konečného automatu. Minimalizace deterministického konečného automatu. Operace s konečnými automaty. Regulární gramatiky, regulární výrazy, regulární rovnice.

Zdroje: BI-AAG přednášky 1–6 (Holub, FIT ČVUT) — základní pojmy, konečné automaty, operace s automaty, regulární výrazy, převody RG–RV–KA, vlastnosti RJ.

---

## 1. Základní pojmy

**Abeceda** $\Sigma$ je konečná neprázdná množina symbolů. **Řetězec (slovo)** nad $\Sigma$ je konečná posloupnost symbolů; prázdný řetězec značíme $\varepsilon$. $\Sigma^*$ je množina všech řetězců, $\Sigma^+ = \Sigma^* \setminus \{\varepsilon\}$.

- **Zřetězení** $\cdot$ je asociativní, ne komutativní; $\varepsilon$ je neutrální prvek.
- **Délka** $|x| \ge 0$, $|\varepsilon| = 0$.
- **Formální jazyk** $L$ nad $\Sigma$: $L \subseteq \Sigma^*$.

**Operace nad jazyky:**
- množinové (sjednocení $\cup$, průnik $\cap$, rozdíl);
- **doplněk** $\bar L = \Sigma^* \setminus L$;
- **součin (zřetězení)** $L_1 \cdot L_2 = \{xy : x \in L_1, y \in L_2\}$;
- **mocnina** $L^n = L \cdot L^{n-1}$, $L^0 = \{\varepsilon\}$;
- **[[Iterace-jazyka|iterace (Kleeneho hvězdice)]]** $L^* = \bigcup_{n \ge 0} L^n$;
- **pozitivní iterace** $L^+ = \bigcup_{n \ge 1} L^n$.

**[[Regulární-jazyk|Regulární jazyk]]** je jazyk, který lze vyjádřit některým z následujících ekvivalentních způsobů:
1. množinou přijímanou konečným automatem (deterministickým či nedeterministickým),
2. regulárním výrazem,
3. regulární gramatikou.

Ekvivalenci těchto tří charakterizací zaručuje **Kleeneho věta** (viz §7.4).

---

## 2. Deterministický konečný automat (DKA)

### 2.1 Definice
**[[Konečný-automat|Deterministický konečný automat (DKA)]]** je pětice
$$M = (Q, \Sigma, \delta, q_0, F),$$
kde
- $Q$ — konečná neprázdná množina vnitřních **stavů**,
- $\Sigma$ — konečná **vstupní abeceda**,
- $\delta : Q \times \Sigma \to Q$ — **přechodová funkce**,
- $q_0 \in Q$ — **počáteční stav**,
- $F \subseteq Q$ — množina **koncových (přijímajících) stavů**.

DKA je **úplně určený**, jestliže $\delta(q,a)$ je definováno pro každé $q \in Q$ a $a \in \Sigma$. Parciální DKA lze doplnit přidáním „odpadního" stavu $q_\emptyset$ a směrováním všech nedefinovaných přechodů do něj.

### 2.2 Konfigurace, přechod, jazyk
**Konfigurace** DKA je dvojice $(q, w) \in Q \times \Sigma^*$. Počáteční konfigurace je $(q_0, w)$, přijímající $(q, \varepsilon)$ pro $q \in F$.

**Přechod** $\vdash_M$:
$$(q, aw') \vdash_M (p, w') \iff \delta(q,a) = p.$$
$\vdash^*_M$ je tranzitivně-reflexivní uzávěr.

**Jazyk přijímaný automatem $M$:**
$$L(M) = \{w \in \Sigma^* : \exists\, q \in F,\ (q_0, w) \vdash^*_M (q, \varepsilon)\}.$$

### 2.3 Dosažitelné a užitečné stavy
- Stav $q$ je **dosažitelný**, pokud $\exists w: (q_0, w) \vdash^* (q, \varepsilon)$. Nedosažitelné stavy odstraníme BFS od $q_0$.
- Stav $q$ je **užitečný**, pokud z něj lze dosáhnout koncového stavu: $\exists p \in F, w: (q, w) \vdash^* (p, \varepsilon)$. Zbytečné stavy odstraníme BFS pozpátku z $F$.

---

## 3. Nedeterministický konečný automat (NKA)

### 3.1 Definice
**[[Konečný-automat|Nedeterministický konečný automat (NKA)]]** je pětice $(Q, \Sigma, \delta, q_0, F)$, kde
$$\delta : Q \times \Sigma \to 2^Q.$$
Přechod: $(q, aw') \vdash_M (p, w') \iff p \in \delta(q, a)$.

**Jazyk:** $L(M) = \{w : \exists q \in F, (q_0, w) \vdash^* (q, \varepsilon)\}$. Stačí existence jedné akceptující výpočetní větve.

### 3.2 NKA s $\varepsilon$-přechody (NKA-$\varepsilon$)
Rozšíření: $\delta : Q \times (\Sigma \cup \{\varepsilon\}) \to 2^Q$. $\varepsilon$-přechody nečtou žádný symbol vstupu.

**$\varepsilon$-uzávěr stavu $q$:**
$$\varepsilon\text{-Closure}(q) = \{p \in Q : (q, \varepsilon) \vdash^* (p, \varepsilon)\}.$$

**Odstranění $\varepsilon$-přechodů** (NKA-$\varepsilon \to$ NKA):
```
1: δ'(q, a) ← ⋃_{p ∈ ε-Closure(q)} δ(p, a),  ∀a ∈ Σ
2: F' ← {q : ε-Closure(q) ∩ F ≠ ∅}
```

### 3.3 NKA s více počátečními stavy
Lze povolit $I \subseteq Q$ místo jediného $q_0$. Převod na NKA s jedním počátečním stavem: přidáme nový $q_0$ a definujeme $\delta'(q_0, a) = \bigcup_{q \in I} \delta(q, a)$.

---

## 4. Determinizace konečného automatu (NKA → DKA)

**Věta:** Ke každému NKA $M$ existuje **ekvivalentní** DKA $M'$ (tj. $L(M) = L(M')$).

Důkaz tvoří podmnožinová konstrukce (subset construction).

### 4.1 Algoritmus — podmnožinová konstrukce
```
Vstup:  NKA M = (Q, Σ, δ, q₀, F)
Výstup: DKA M' s L(M) = L(M')
(1)  Q' ← {{q₀}}                          // stavy DKA = podmnožiny Q
(2)  q'₀ ← {q₀}
(3)  Dokud existuje q' ∈ Q', které nebylo zpracováno:
(4)      Pro každé a ∈ Σ:
(5)          δ'(q', a) ← ⋃_{p ∈ q'} δ(p, a)
(6)          Q' ← Q' ∪ {δ'(q', a)}
(7)  F' ← {q' ∈ Q' : q' ∩ F ≠ ∅}
(8)  Vrať M' = (Q', Σ, δ', q'₀, F')
```

Pro NKA-$\varepsilon$ je třeba buď nejprve odstranit $\varepsilon$-přechody, nebo přímo pracovat s $\varepsilon$-uzávěry: $q'_0 \leftarrow \varepsilon\text{-Closure}(q_0)$, $\delta'(q', a) \leftarrow \varepsilon\text{-Closure}\bigl(\bigcup_{p \in q'} \delta(p, a)\bigr)$.

### 4.2 Korektnost (skica)
Indukcí podle délky vstupu $w$ se ukáže
$$\hat\delta'(q'_0, w) = \{p \in Q : (q_0, w) \vdash^*_{\text{NKA}} (p, \varepsilon)\}.$$
Tedy $w \in L(M_{\text{DKA}}) \iff \hat\delta'(q'_0, w) \cap F \neq \emptyset \iff$ existuje akceptující výpočet NKA $\iff w \in L(M_{\text{NKA}})$.

### 4.3 Stavová exploze
V nejhorším případě $|Q'| = 2^{|Q|}$. Typicky se však vytvoří jen zlomek podmnožin (vždy vznikají jen **dosažitelné** podmnožiny). Příklad: NKA na slova obsahující podřetězec „ab" se 2 stavy dává DKA se 3 dosažitelnými stavy.

---

## 5. Minimalizace deterministického konečného automatu

### 5.1 Definice
DKA $M$ je **stavově minimální**, pokud neexistuje DKA $M'$ s $L(M') = L(M)$ a $|Q(M')| < |Q(M)|$.

Dva stavy $p, q \in Q$ jsou **(jazykově) ekvivalentní** $p \sim q$, pokud
$$\forall w \in \Sigma^*: \hat\delta(p, w) \in F \iff \hat\delta(q, w) \in F.$$
Tj. z $p$ a $q$ je přijímán tentýž jazyk.

### 5.2 Věta o jednoznačnosti
**Věta:** Minimální DKA daného regulárního jazyka je **jednoznačně určen až na izomorfismus** (pojmenování stavů). Jeho stavy odpovídají třídám ekvivalence $\sim$.

(Hlubší důvod plyne z **Myhill–Nerodovy věty**: počet stavů minimálního DKA = počet tříd Myhill–Nerodovy ekvivalence $\equiv_L$ pravých kongruencí.)

### 5.3 Algoritmus — rozkladová tabulka
Před spuštěním je třeba mít DKA bez nedosažitelných a zbytečných stavů, **úplně určený**.

```
Vstup:  DKA M = (Q, Σ, δ, q₀, F)
Výstup: Minimální DKA Mₘ s L(Mₘ) = L(M)
(1)  Q_I ← Q \ F;  Q_II ← F                   // počáteční rozklad
(2)  Opakuj:
(3)      Vytvoř tabulku: řádek = stav, sloupec = symbol Σ;
         v buňce zapiš ID podmnožiny, ve které leží δ(q, a).
(4)      Pokud existuje podmnožina, jejíž řádky nejsou všechny stejné,
         rozděl ji na maximální skupiny se shodnými řádky.
(5)  Dokud nedochází k dalšímu dělení.
(6)  Q_m ← výsledné třídy.
(7)  δ_m([q], a) := [δ(q, a)]      // korektně definováno
(8)  q_{0m} := [q₀];  F_m := { [q] : q ∈ F }
```

**Idea:** Začneme nejhrubším možným rozkladem, který respektuje $F$ vs. $Q \setminus F$ (vstup $\varepsilon$ je rozlišuje). Iterativně rozkládáme každou třídu podle toho, kam přechody vedou (s respektováním aktuálního rozkladu). Když se rozklad přestane měnit, je to **nejhrubší shoda** $\sim$.

**Složitost:** naivně $O(|Q|^2 \cdot |\Sigma|)$; Hopcroftova varianta $O(|Q| \cdot |\Sigma| \cdot \log |Q|)$.

### 5.4 Důsledek
Z dvou DKA pro tentýž jazyk dostáváme po minimalizaci automaty izomorfní → minimalizace dává **kanonický tvar** a hodí se k testu ekvivalence dvou DKA.

---

## 6. Operace s konečnými automaty

**Věta (uzavřenost regulárních jazyků):** Třída regulárních jazyků je uzavřena na **sjednocení, průnik, doplněk, zřetězení a iteraci**. Důkazy dávají následující konstrukce.

### 6.1 Sjednocení
**(a) Přes nový počáteční stav s $\varepsilon$-přechody** — NKA-$\varepsilon$:
```
Q := Q₁ ∪ Q₂ ∪ {q₀},   q₀ ∉ Q₁ ∪ Q₂
δ(q₀, ε) := {q₀₁, q₀₂}
δ(q, a) := δᵢ(q, a)    pro q ∈ Qᵢ
F := F₁ ∪ F₂
```

**(b) Produktový automat** (pro DKA, sjednocení):
$M = (Q_1 \times Q_2, \Sigma, \delta, (q_{01}, q_{02}), F)$, kde
$$\delta((q_1, q_2), a) = (\delta_1(q_1, a), \delta_2(q_2, a)), \qquad F = (F_1 \times Q_2) \cup (Q_1 \times F_2).$$

### 6.2 Průnik — produktový automat
Stejná konstrukce, ale $F = F_1 \times F_2$ (oba musí přijímat). Lze konstruovat jen dosažitelné stavy (BFS od $(q_{01}, q_{02})$).

### 6.3 Doplněk
Předpoklad: $M$ je **deterministický a úplně určený**. Pak
$$\overline M = (Q, \Sigma, \delta, q_0, Q \setminus F).$$
Pro nedeterministický automat tato konstrukce **nefunguje** — je třeba nejprve determinizovat.

### 6.4 Zřetězení (součin)
NKA-$\varepsilon$, $Q_1 \cap Q_2 = \emptyset$:
$$M = (Q_1 \cup Q_2, \Sigma, \delta, q_{01}, F_2),$$
$\delta(q, a) = \delta_i(q, a)$ pro $q \in Q_i$, a navíc $\delta(q, \varepsilon) = \{q_{02}\}$ pro každý $q \in F_1$.

### 6.5 Iterace (Kleeneho hvězdice)
Přidá se nový počáteční stav $q'_0$ s $\varepsilon$-přechodem do $q_0$, z každého koncového stavu se přidá $\varepsilon$-přechod zpět do $q_0$. $F' = F \cup \{q'_0\}$ (aby $M^*$ přijímal $\varepsilon$).

### 6.6 Rozdíl a symetrická diference
$L_1 \setminus L_2 = L_1 \cap \overline{L_2}$. Z uzavřenosti na $\cap$ a $\neg$ plyne i uzavřenost na $\setminus$ a $\triangle$.

---

## 7. Regulární gramatiky, regulární výrazy

### 7.1 Regulární gramatika
Obecně **[[Gramatika|gramatika]]** je čtveřice $G = (N, \Sigma, P, S)$:
- $N$ — neterminály, $\Sigma$ — terminály, $N \cap \Sigma = \emptyset$,
- $P$ — pravidla, $S \in N$ — počáteční neterminál.

**[[Regulární-gramatika|Regulární gramatika]]** (typ 3 Chomského hierarchie) — každé pravidlo má **pravolineární** tvar
$$A \to aB \quad \text{nebo} \quad A \to a, \qquad A, B \in N,\ a \in \Sigma,$$
plus výjimečně $S \to \varepsilon$ za podmínky, že $S$ se nevyskytuje na pravé straně žádného pravidla. (Alternativně lze definovat **levolineární** tvar $A \to Ba \mid a$ — generuje tutéž třídu.) **Pozor:** levo- a pravolineární pravidla v jedné gramatice mohou generovat ne-regulární jazyky.

**Jazyk gramatiky:** $L(G) = \{w \in \Sigma^* : S \Rightarrow^* w\}$.

### 7.2 Regulární výraz (RV)
**Syntaxe** (induktivně):
1. $\emptyset$, $\varepsilon$, $a$ pro každé $a \in \Sigma$ jsou regulární výrazy.
2. Jsou-li $x, y$ regulární výrazy, pak také $(x + y)$, $(x \cdot y)$ a $(x)^*$.

**Sémantika** — jazyk přiřazený regulárnímu výrazu:
- $L(\emptyset) = \emptyset$, $L(\varepsilon) = \{\varepsilon\}$, $L(a) = \{a\}$,
- $L(x + y) = L(x) \cup L(y)$,
- $L(x \cdot y) = L(x) \cdot L(y)$,
- $L(x^*) = (L(x))^*$.

Priorita: $\,^* > \cdot > +$. Závorky a tečky se vynechávají, pokud nedojde k nejednoznačnosti.

### 7.3 Ekvivalence a identity
Dva regulární výrazy jsou **ekvivalentní** ($x = y$), pokud $L(x) = L(y)$. Základní identity:
$$
\begin{aligned}
& x + x = x, \quad x + y = y + x, \quad (x+y)+z = x+(y+z), \\
& x + \emptyset = x, \quad x \cdot \emptyset = \emptyset \cdot x = \emptyset, \quad x \cdot \varepsilon = \varepsilon \cdot x = x.
\end{aligned}
$$
Užitečné věty:
- $\emptyset^* = \varepsilon$, $(x^*)^* = x^*$, $(x+y)^* = (x^* y^*)^*$,
- $x^* = \varepsilon + x \cdot x^*$,
- $(xy)^*x = x(yx)^*$.

### 7.4 Kleeneho věta
**Věta (Kleene):** Jazyk $L$ je regulární *právě tehdy*, když je přijímaný nějakým konečným automatem, *právě tehdy*, když ho generuje nějaká regulární gramatika, *právě tehdy*, když ho popisuje nějaký regulární výraz.

Důkaz dávají vzájemné převody, viz §8.

---

## 8. Převody mezi RG, RV a KA

```
        Regulární výrazy
              ↕
   Reg. gramatiky ⇄ Konečné automaty
```

### 8.1 RG → NKA
```
Q := N ∪ {A},  A ∉ N            // A = nový koncový stav
δ(B, a) := {C : (B → aC) ∈ P}  ∪  {A : (B → a) ∈ P}     ∀a, ∀B
q₀ := S
F := {A} ∪ ({S} pokud S → ε ∈ P)
```

### 8.2 NKA → RG
```
N := Q,  S := q₀
P := {B → aC : C ∈ δ(B, a)}
   ∪ {B → a  : ∃C ∈ δ(B, a) ∩ F}
   ∪ ({S → ε} pokud q₀ ∈ F)
```

### 8.3 RV → NKA (Glushkov, metoda sousedů)
1. Očísluj výskyty terminálů ve výrazu $V \mapsto V'$.
2. Spočti množinu **počátečních** symbolů $Z$ (mohou stát na začátku), **koncových** $K$ (mohou stát na konci) a **sousedů** $P = \{ab : a, b\ \text{mohou stát vedle sebe}\}$.
3. $Q := \{q_0\} \cup \{a_i \in V'\}$; $\delta(q_0, a) := \{a_i \in Z\}$, $\delta(a_i, b) := \{b_j : a_i b_j \in P\}$.
4. $F := K \cup (\{q_0\}\ \text{pokud}\ \varepsilon \in L(V))$.

Alternativy: **Thompsonova** (induktivní konstrukce z $\varepsilon$-NFA), **Brzozowského derivace**.

### 8.4 KA → RV (metoda regulárních rovnic)
Z automatu sestavíme soustavu, kterou vyřešíme **Ardenovým lemmatem** (viz §9).

```
Pro každý q ∈ Q sestav rovnici:
   X_q = ∑_{a ∈ Σ, p ∈ δ(q, a)} a · X_p     ( + ε, pokud q ∈ F )
Vyřeš soustavu pravých regulárních rovnic.
Výsledný regulární výraz V := X_{q₀}.
```

Alternativa: **eliminace stavů** — postupně odstraňujeme stavy z grafu a hrany nahrazujeme regulárními výrazy popisujícími všechny cesty přes odstraněný stav.

### 8.5 RV → RG
Postupná induktivní konstrukce podle struktury výrazu: pro každý atomický výraz $a$ triviální gramatika $G_a = (\{A\}, \{a\}, \{A \to a\}, A)$, a operace $+, \cdot, ^*$ kombinují gramatiky standardními algoritmy.

### 8.6 RG → RV
Pro každý neterminál sestavíme regulární rovnici a vyřešíme soustavu (viz §9).

---

## 9. Regulární rovnice a Ardenovo lemma

### 9.1 Ardenovo lemma
**Věta (Arden):** Nechť $\alpha, \beta$ jsou regulární výrazy a $\varepsilon \notin L(\alpha)$. Pak rovnice
$$X = \alpha X + \beta \qquad\text{má jediné řešení}\qquad X = \alpha^* \beta.$$
(Levou variantou $X = X\alpha + \beta$ je řešení $X = \beta \alpha^*$.)

*Důkaz (skica):* Dosazením: $\alpha^* \beta = \beta + \alpha\alpha^*\beta = \beta + \alpha(\alpha^*\beta)$ — vyhovuje. Naopak iterativním rozvíjením $X = \beta + \alpha X = \beta + \alpha\beta + \alpha^2\beta + \dots = \alpha^* \beta$. Pokud $\varepsilon \in L(\alpha)$, řešení už není jednoznačné.

### 9.2 Standardní soustava regulárních rovnic
$$X_i = \alpha_{i0} + \alpha_{i1} X_1 + \alpha_{i2} X_2 + \dots + \alpha_{in} X_n, \qquad 1 \le i \le n,$$
kde $\alpha_{ij}$ jsou regulární výrazy nad $\Sigma$ neobsahující neznámé.

**Postup řešení (eliminace):**
1. Vyber nějakou rovnici $X_k = \dots + \alpha_{kk} X_k + \dots$ a aplikuj Arden: $X_k = \alpha_{kk}^* (\text{zbytek pravé strany})$.
2. Dosaď výsledek do ostatních rovnic.
3. Opakuj, dokud nezůstane jediná rovnice — vyřeš Ardenem.

### 9.3 Příklad
$$\begin{cases} A = 1A + 1B \\ B = 0A + 0B + 0 \end{cases}$$
- $A = 1^* \cdot 1B = 1^+ B$ (Arden zleva).
- Dosadíme: $B = 0 \cdot 1^+ B + 0B + 0 = (01^+ + 0) B + 0 = (01^*) B + 0$.
- Arden: $B = (01^*)^* \cdot 0$.
- $A = 1^+ \cdot (01^*)^* \cdot 0$.

### 9.4 Použití
- **KA → RV** (§8.4).
- **RG → RV** (§8.6).
- Analýza struktury automatu, dokazování ekvivalence regulárních výrazů.

---

## 10. Co je potřeba na zkoušku znát

### Definice
DKA (pětice + úplnost), NKA, NKA-$\varepsilon$, $\varepsilon$-uzávěr, konfigurace, přechod, $L(M)$; dosažitelný/užitečný stav; ekvivalence automatů; regulární gramatika (pravolineární tvar); regulární výraz (syntaxe + sémantika); regulární jazyk; Kleeneova hvězdice.

### Věty (s důkazovou skicou)
- **Determinizace:** ke každému NKA existuje ekvivalentní DKA (důkaz podmnožinovou konstrukcí).
- **Jednoznačnost minimálního DKA** (až na izomorfismus); Myhill–Nerodova věta jako pozadí.
- **Uzavřenost regulárních jazyků** na $\cup, \cap, \neg, \cdot, ^*$ (důkaz konstrukcemi).
- **Kleeneova věta:** regulární $\iff$ KA $\iff$ RG $\iff$ RV.
- **Ardenovo lemma:** $X = \alpha X + \beta \Rightarrow X = \alpha^* \beta$ při $\varepsilon \notin L(\alpha)$.

### Algoritmy
- Odstranění $\varepsilon$-přechodů (NKA-$\varepsilon \to$ NKA).
- Odstranění nedosažitelných / zbytečných stavů.
- Podmnožinová konstrukce (NKA → DKA).
- Minimalizace DKA (rozkladová tabulka).
- Produktový automat pro sjednocení a průnik.
- Konstrukce automatu pro doplněk (deterministický + úplně určený, prohození F).
- Zřetězení a Kleeneho hvězdice přes NKA-$\varepsilon$.
- Převody RG ↔ NKA; Glushkov/Thompson (RV → NKA); regulární rovnice (KA/RG → RV).

### Datové struktury / složitosti
- Velikost podmnožinové konstrukce až $2^{|Q|}$.
- Minimalizace $O(|Q|^2 |\Sigma|)$ naivně, $O(|Q| |\Sigma| \log |Q|)$ Hopcroft.
- Produktový automat $|Q_1| \cdot |Q_2|$ stavů.
