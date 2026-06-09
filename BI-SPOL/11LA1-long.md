---
studyplan: true
etapa: "3 · LA1 / MA2 / LA2 — Petr"
qid: "11LA1"
examiner: "Petr"
topic: "Soustavy lin. rovnic, Frobeniova věta, Gaussova eliminace"
readiness: in progress
tags: [otázka, kurz/LA1, otázka/11, todo]
---

# Soustavy lineárních rovnic

> **Otázka SZZ:** Soustavy lineárních rovnic: Frobeniova věta a související pojmy, vlastnosti a popis množiny řešení, Gaussova eliminační metoda.

Zdroje: BI-LA1 (Dombek, Kalvoda, Kleprlík, Klouda, FIT ČVUT), kap. 1 (Soustavy lineárních rovnic), kap. 3 (Hodnost a regularita matice), kap. 4 (Frobeniova věta a kompletní řešení SLR).

Značení: $T$ je těleso ($\mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{Z}_p$), $A \in T^{m,n}$ matice, $\theta$ nulový vektor, $E$ jednotková matice, $h(A)$ hodnost matice.

---

## 1. Soustavy lineárních rovnic

### 1.1 Definice

**Definice ([[Soustava-lineárních-rovnic|soustava lineárních rovnic]], SLR):** Nechť $m, n \in \mathbb{N}$, $a_{ij}, b_i \in T$. **Soustavou $m$ lineárních rovnic o $n$ neznámých** $x_1, \dots, x_n$ nazýváme
$$\begin{aligned} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\ &\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m \end{aligned}$$
Číslo $a_{ij}$ je $j$-tý koeficient $i$-té rovnice. **Řešením** je $n$-tice $(x_1, \dots, x_n) \in T^n$ splňující všechny rovnice; množinu všech řešení značíme $S$ (rovná se průniku množin řešení jednotlivých rovnic).

- **Homogenní** soustava: $b_1 = \cdots = b_m = 0$; jinak **nehomogenní**.
- Homogenní soustava má vždy aspoň triviální řešení $(0, \dots, 0)$; to naopak nikdy neřeší nehomogenní soustavu.

### 1.2 Maticový zápis

S [[Matice|maticí]] soustavy $A \in T^{m,n}$, vektorem neznámých $x = (x_1, \dots, x_n)^T$ a vektorem pravých stran $b = (b_1, \dots, b_m)^T$ zapíšeme soustavu kompaktně jako
$$A x = b, \qquad \text{kde } (Ax)_i = \sum_{j=1}^n a_{ij} x_j.$$
**Rozšířená matice soustavy** je $(A \mid b) \in T^{m,n+1}$ (svislá čára je jen grafická). Soustava $Ax = \theta$ se nazývá **přidružená homogenní soustava** k $Ax = b$; její množinu řešení značíme $S_0$.

---

## 2. Hodnost matice a Frobeniova věta

### 2.1 Hodnost matice

**Definice ([[Hodnost-matice|hodnost matice]]):** Hodnost matice $A \in T^{m,n}$, značená $h(A)$, je dimenze lineárního obalu jejích řádků (chápaných jako vektory z $T^n$):
$$h(A) := \dim \big\langle (A_{1:})^T, \dots, (A_{m:})^T \big\rangle.$$

**Vlastnosti:** $0 \le h(A) \le \min(m,n)$; $h(A) = h(A^T)$ (hodnost řádků = hodnost sloupců); elementární úpravy GEM hodnost nemění; pro matici v horním stupňovitém tvaru je $h(A)$ rovna počtu nenulových řádků (pivotů). Hodnost je nástroj pro rozhodnutí o řešitelnosti soustavy.

### 2.2 Frobeniova věta

**Věta ([[Frobeniova-věta]]):** Nechť $A \in T^{m,n}$, $b \in T^m$. Pro soustavu $Ax = b$ platí:

1. soustava je **řešitelná** ($S \neq \emptyset$) **právě tehdy, když** $h(A) = h(A \mid b)$;
2. je-li $\tilde{x}$ libovolné řešení, pak $S = \tilde{x} + S_0$;
3. $S_0$ je podprostor dimenze $n - h(A)$.

**Důkaz bodu 1 (idea).** Označme sloupce $A_{:1}, \dots, A_{:n}$. Platí $Ax = \sum_{j=1}^n x_j A_{:j}$, takže $x$ je řešením $\iff b$ je lineární kombinací sloupců $A$, tj. $b \in \langle A_{:1}, \dots, A_{:n} \rangle$. To nastane právě tehdy, když přidání $b$ nezvětší dimenzi obalu sloupců, tedy když $h(A) = h(A \mid b)$ (využíváme $h(X) = h(X^T)$). $\square$

**Důkaz bodu 3 (idea).** Pro $h(A) = n$ jsou sloupce lineárně nezávislé, takže $Ax = \theta$ má jen triviální řešení a $\dim S_0 = 0$. Obecně se z báze $S_0$ a vybrané báze sloupcového prostoru sestaví báze celého $T^n$, odkud $\dim S_0 + h(A) = n$. $\square$

### 2.3 Důsledek — počet řešení

Pro $n$ neznámých a $h := h(A)$:

| podmínka | počet řešení |
|---|---|
| $h(A) < h(A \mid b)$ | žádné ($S = \emptyset$) |
| $h(A) = h(A \mid b) = n$ | právě jedno ($S_0 = \{\theta\}$) |
| $h(A) = h(A \mid b) < n$ | nekonečně mnoho (nad nekonečným tělesem) |

Počet **volných parametrů** řešení je $n - h(A) = \dim S_0$.

**Speciální případ — regulární matice.** Je-li $A$ čtvercová a **[[Regulární-matice|regulární]]** ($h(A) = n$), má $Ax = b$ pro každé $b$ právě jedno řešení $x = A^{-1}b$.

---

## 3. Vlastnosti a popis množiny řešení

### 3.1 Struktura řešení

**Věta (o vlastnostech SLR).** Pro $Ax = b$ s množinami řešení $S$ (soustavy) a $S_0$ (přidružené homogenní) platí:

1. $\theta \in S_0$;
2. $x \in S_0,\ \alpha \in T \Rightarrow \alpha x \in S_0$;
3. $x, y \in S_0 \Rightarrow x + y \in S_0$ — tedy **$S_0$ je podprostor** $T^n$;
4. $x, y \in S \Rightarrow x - y \in S_0$;
5. je-li $\tilde{x} \in S$, pak pro každé $y \in S$ existuje $z \in S_0$ s $y = \tilde{x} + z$;
6. je-li $\tilde{x} \in S$ a $z \in S_0$, pak $\tilde{x} + z \in S$.

**Důkaz (bod 3, 4, 6).** Pro $x, y \in S_0$: $A(x+y) = Ax + Ay = \theta + \theta = \theta$ (distributivita), tedy $x + y \in S_0$. Pro $x, y \in S$: $A(x-y) = Ax - Ay = b - b = \theta$, tedy $x - y \in S_0$. Pro $\tilde{x} \in S$, $z \in S_0$: $A(\tilde{x} + z) = A\tilde{x} + Az = b + \theta = b$, tedy $\tilde{x} + z \in S$. $\square$

**Věta (o struktuře řešení SLR).** Je-li $\tilde{x}$ libovolné (partikulární) řešení $Ax = b$, pak
$$\boxed{\,S = \tilde{x} + S_0\,}$$
(body 5 a 6 dávají obě inkluze). **Klíčový princip:** k popisu celé množiny řešení stačí najít **jedno** řešení $\tilde{x}$ a popsat $S_0$ přidružené homogenní soustavy.

**Důsledek (počet řešení nad $\mathbb{Q}, \mathbb{R}, \mathbb{C}$).** Má-li soustava aspoň dvě řešení, má jich nekonečně mnoho. (Jsou-li $x \neq y$ řešení, je $z = x - y \neq \theta$ v $S_0$, a pak $x + \alpha z \in S$ pro nekonečně mnoho $\alpha$.)

### 3.2 Homogenní soustava

$S_0$ je vždy neprázdný podprostor dimenze $n - h(A)$. Bázi $S_0$ tvoří $n - h$ vektorů: za volné proměnné (odpovídající vedlejším sloupcům) postupně dosadíme bázové vektory $T^{n-h}$ (např. $e_1, \dots, e_{n-h}$) a dopočítáme vázané proměnné. Neexistuje-li volná proměnná, je $S_0 = \{\theta\}$.

### 3.3 Nehomogenní soustava

Množina řešení je buď **prázdná** (když $h(A) < h(A \mid b)$), nebo
$$S = \tilde{x} + S_0,$$
kde $\tilde{x}$ je libovolné partikulární řešení a $S_0$ se počítá z **přidružené homogenní** soustavy (tj. s pravou stranou $\theta$, nikoli $b$ — častá chyba).

### 3.4 Geometrický popis — lineární varieta

**Definice ([[Lineární-varieta|lineární varieta]]):** Množina $W \subseteq T^n$ je lineární varieta, existuje-li $a \in T^n$ a podprostor $P$ s $W = a + P$. Podprostor $P$ je **zaměření** $Z(W)$, $\dim W := \dim Z(W)$.

Množina řešení **řešitelné** soustavy je tedy lineární varieta $S = \tilde{x} + S_0$ se zaměřením $Z(S) = S_0$ a dimenzí
$$\dim S = \dim S_0 = n - h(A).$$
Zaměření je určeno jednoznačně, takže dimenze řešení nezávisí na volbě $\tilde{x}$ ani na postupu výpočtu.

**Pozor na typ objektu a operaci** (časté doptávání). Zápis $S = \tilde{x} + S_0$ je **vektor $+$ podprostor**, kde
$$\tilde{x} + S_0 := \{\, \tilde{x} + z : z \in S_0 \,\}.$$
Partikulární řešení $\tilde{x}$ tedy **posune** (zde: přičte se ke **každému** vektoru) celý podprostor $S_0$ od počátku. Výsledek **není** podprostor (pokud $\tilde{x} \notin S_0$, neobsahuje $\theta$), nýbrž **lineární varieta**. Vektor posunutí $\tilde{x}$ je sám prvkem variety ($\tilde{x} = \tilde{x} + \theta \in S$).

---

## 4. Gaussova eliminační metoda

### 4.1 Elementární úpravy

**Definice ([[Gaussova-eliminace|operace GEM]]):** Na řádcích matice provádíme

- **(G1)** prohození dvou řádků;
- **(G2)** vynásobení řádku nenulovým $\alpha \in T \setminus \{0\}$;
- **(G3)** přičtení $\alpha$-násobku jednoho řádku k jinému.

**Věta (vliv GEM na řešení).** Převedeme-li rozšířenou matici soustavy operacemi (G1)–(G3) na jinou, mají obě soustavy **stejnou množinu řešení** (úpravy odpovídají ekvivalentním úpravám rovnic a jsou vratné).

*Důkaz (idea).* (G1) nemění $S$ z definice. (G2) plyne z distributivity a z toho, že pro $\alpha \neq 0$ je $\alpha y = \alpha z \iff y = z$. (G3) využívá platnost druhé rovnice: přičtením jejího násobku se množina řešení nezmění. $\square$

**Maticový pohled (oblíbené doptávání).** Každá jednotlivá úprava (G1)–(G3) na matici $A$ se realizuje jako **vynásobení zleva regulární maticí** (tzv. elementární maticí) $P_i$. Celá GEM je tedy $PA$, kde $P = P_k \cdots P_1$ je regulární (součin regulárních). Protože násobení regulární maticí **nemění hodnost** ani řešitelnost a je vratné ($Ax=b \iff PAx = Pb$), množina řešení se zachová — to je nejčistší důkaz, **proč GEM nemění množinu řešení**.

### 4.2 Horní stupňovitý tvar (HST)

**Definice.** Matice je v **HST**, jsou-li nulové řádky až dole a indexy $j_1, \dots, j_k$ prvních nenulových prvků (**pivotů**) jednotlivých nenulových řádků striktně rostou:
$$j_1 < j_2 < \cdots < j_k.$$
Sloupce s pivotem jsou **hlavní** (jim odpovídají vázané proměnné), ostatní **vedlejší** (volné proměnné). Pro matici v HST je $h(A) = k$ (počet pivotů).

### 4.3 Algoritmus

**Postup (GEM).** Položíme pivotní řádek $k=1$, sloupec $\ell=1$. Opakujeme:
1. je-li sloupec $\ell$ od $k$-tého řádku dolů nulový, zvyš $\ell$ a opakuj;
2. je-li $b_{k\ell} = 0$ a níže existuje nenulový prvek, prohoď řádky (G1);
3. máme pivot $b_{k\ell} \neq 0$ — úpravami (G3) vynuluj všechny prvky **pod** ním; pak $k \leftarrow k+1$, $\ell \leftarrow \ell+1$.

Po skončení je matice v HST. **Složitost** $O(n^3)$ pro čtvercovou soustavu. Vhodná volba pořadí úprav (a (G2)) může výpočet zjednodušit (vyhnout se zlomkům).

**Gaussova–Jordanova eliminace** pokračuje za HST: znormuje pivoty na $1$ a vynuluje i prvky **nad** nimi → **redukovaný HST (rHST)**, ze kterého se řešení odečte přímo.

### 4.4 Řešitelnost a popis řešení z HST

Po převodu $(A \mid b)$ do HST rozhodneme:

1. **poslední sloupec $(A\mid b)$ je hlavní** (existuje řádek $(0 \cdots 0 \mid c)$ s $c \neq 0$, tj. rovnice $0 = c$) $\Rightarrow$ **bez řešení**;
2. **poslední sloupec je jediný vedlejší** $\Rightarrow$ **právě jedno řešení** (zpětný chod / dosazování zdola nahoru);
3. **poslední sloupec vedlejší a existuje další vedlejší sloupec** $\Rightarrow$ **více řešení** (nad nekonečným tělesem nekonečně mnoho).

(Toto je výpočetní podoba Frobeniovy věty: poslední sloupec hlavní $\iff h(A) < h(A\mid b)$.)

**Popis množiny řešení.**
1. převeď $(A \mid b)$ do HST (případně rHST);
2. **partikulární řešení $\tilde{x}$:** za volné proměnné dosaď libovolně (oblíbeně $0$) a dopočítej vázané proměnné ze soustavy $(A \mid b)$;
3. **báze $S_0$:** ve **homogenní** soustavě $(A \mid \theta)$ dej postupně jednu volnou proměnnou rovnu $1$ a ostatní $0$, dopočítej vázané proměnné — dostaneš $n - h$ lineárně nezávislých vektorů;
4. výsledek $S = \tilde{x} + \langle z_1, \dots, z_{n-h} \rangle$.

### 4.6 Jiné metody řešení (regulární $A$)

Je-li $A$ **regulární** ($n \times n$, $h(A) = n$), má $Ax = b$ jediné řešení a lze ho najít i bez GEM:

- **přes inverzní matici:** $x = A^{-1}b$;
- **Cramerovo pravidlo (Věta 5.45):** pro každé $i$ je
$$x_i = \frac{\det A_i}{\det A}, \qquad A_i = (A_{:1} \mid \cdots \mid \underset{i\text{-tý sloupec}}{b} \mid \cdots \mid A_{:n}),$$
kde $A_i$ vznikne z $A$ nahrazením $i$-tého sloupce vektorem $b$. Vyžaduje $\det A \neq 0$ (tj. regularitu). Výpočetně je ale **nevýhodné** ($n+1$ determinantů) — GEM je v praxi rychlejší.

### 4.5 Příklad

Soustava nad $\mathbb{R}$ s rozšířenou maticí již v HST:
$$\left(\begin{array}{ccccc|c} 1 & 2 & 1 & 3 & 0 & 3 \\ 0 & 0 & -2 & -6 & 0 & -5 \\ 0 & 0 & 0 & 1 & 1 & 1 \end{array}\right).$$
$h(A) = h(A\mid b) = 3 < 5 = n$, tedy nekonečně mnoho řešení s $5 - 3 = 2$ volnými parametry (vedlejší sloupce $2$ a $5$, tj. $x_2, x_5$). Volbou $x_2 = x_5 = 0$ vyjde partikulární $\tilde{x} = (\tfrac12, 0, -\tfrac12, 1, 0)$; bázový vektor $S_0$ (volba $x_2 = 1, x_5 = 0$ v homogenní soustavě) je $(-2, 1, 0, 0, 0)$. Pak $S = \tilde{x} + \langle (-2,1,0,0,0),\ z_2 \rangle$.

---

## Co je potřeba na zkoušku znát

### Definice
- Soustava lineárních rovnic ($Ax = b$), homogenní / nehomogenní, množina řešení $S$, $S_0$, rozšířená matice $(A \mid b)$.
- Hodnost matice $h(A) = \dim \langle \text{řádky} \rangle$; $h(A) = h(A^T)$.
- Horní stupňovitý tvar, pivot, hlavní / vedlejší sloupec, vázaná / volná proměnná.
- Lineární varieta $W = a + P$, zaměření, dimenze.

### Klíčové věty
- **Frobeniova věta:** $Ax=b$ řešitelná $\iff h(A) = h(A\mid b)$; $S = \tilde{x} + S_0$; $\dim S_0 = n - h(A)$.
- **Struktura řešení:** $S_0$ je podprostor; $S = \tilde{x} + S_0$ (partikulární řešení + řešení homogenní soustavy).
- **Počet řešení:** $0$ / $1$ / $\infty$ podle $h(A)$ vs. $h(A\mid b)$ vs. $n$.
- **GEM nemění množinu řešení** (ani hodnost).
- **Regulární $A$:** jediné řešení $x = A^{-1}b$.

### Algoritmy
- **GEM** — převod na HST: pivot, nulování pod pivotem, $O(n^3)$.
- **Rozhodnutí o řešitelnosti** z HST (poslední sloupec hlavní / vedlejší).
- **Popis řešení:** partikulární $\tilde{x}$ + báze $S_0$ ($n - h$ vektorů); pozor na pravou stranu $\theta$ při výpočtu $S_0$.
- **Cramerovo pravidlo / $x = A^{-1}b$** — pro regulární $A$ jako alternativa ke GEM.

### Související pojmy (které je nutné umět definovat)

Zkoušející téměř vždy chtějí **definice všech pojmů použitých ve Frobeniově větě**. Měj připravené (řetězí se): **lineární kombinace** → **lineárně (ne)závislý soubor** → **lineární obal / generátory** → **báze** → **dimenze podprostoru** → **hodnost matice** (přes bázi řádkového prostoru). Dále **podprostor**, **horní stupňovitý tvar** a **lineární varieta**.

### Typické doplňující otázky (doptávání)

- **Petr (Ivo Petr):** "Soustavy lin. rovnic, metody řešení a věta o existenci a jednoznačnosti řešení" — zaměřuje na Frobenia jako větu o existenci/jednoznačnosti → §2.2, §2.3.
- **Kalvoda:** chce Frobeniovu větu **přesně** a definici **všech** použitých pojmů (hodnost, dimenze, lin. nezávislost); zúžení často jen na GEM + popis množiny řešení → §2.2, "Související pojmy", §4.
- **Starý:** "Co je to za objekt $S = \tilde{x} + S_0$? Co je to za operaci? Vektor $+$ podprostor" → odpověz **lineární varieta**, partikulární řešení posouvá $S_0$ (přičítá se ke každému vektoru) → §3.4.
- **Pernecká / Černý:** definuj **bázi** a přes ni **hodnost matice**; "jak se z geometrického hlediska nazývá množina řešení?" → lineární varieta, §3.4.
- **Zhouf:** "Jak jinak než GEMem řešíš soustavu?" → přes inverzní matici $x=A^{-1}b$, pak Cramerovo pravidlo → §4.6. Také "jak GEM mění determinant" (viz otázka 12).
- **Legerský:** rozeber **dimenzi** podle případů $0$ / $n$ / nekonečno a **kvantifikátory**; ilustruj příkladem → §2.3.
- **Olšák:** "Vysvětli, proč úpravy GEM nemění množinu řešení" → realizace násobením regulární maticí zleva → §4.1.
