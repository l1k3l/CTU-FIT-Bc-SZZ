---
tags: [otázka, kurz/LA2, otázka/1, todo]
---

# Lineární zobrazení a jeho matice

> **Otázka SZZ:** Lineární zobrazení: definice a vlastnosti (hodnost, jádro, defekt, injektivita, surjektivita), matice lineárního zobrazení.

Zdroje: BI-LA2 (učebnice, FIT ČVUT), kap. 3 (Lineární zobrazení — 3.2 Základní pojmy, 3.3 Definice lin. zobrazení, 3.5 Základní vlastnosti, 3.6 Hodnost, jádro, defekt, 3.7 Injektivita, 3.8 Vztah hodnosti a defektu, 3.9 O rovnicích $Ax=b$, str. 43–62), kap. 4 (Matice lineárního zobrazení — 4.3 Zavedení, 4.5 Vlastnosti, 4.6 Změna báze, str. 66–85).

Značení: $T$ těleso, $P, Q, V$ vektorové prostory (VP) nad **stejným** $T$, $\theta_P, \theta_Q$ nulové vektory, $A \in T^{m,n}$ matice, $E$ jednotková matice / identický operátor, $h(\cdot)$ hodnost, $d(\cdot)$ defekt, $\langle \cdots \rangle$ lineární obal, $P \subset\subset Q$ „$P$ je podprostor $Q$". Obraz vektoru píšeme zkráceně $Ax$ místo $A(x)$.

---

## 1. Definice lineárního zobrazení

Připomeňme nejprve obecné pojmy o zobrazeních. Pro zobrazení $f : M \to N$:
- $f(K) := \{f(x) \mid x \in K\}$ je **obraz množiny** $K \subseteq M$;
- $f^{-1}(L) := \{x \in M \mid f(x) \in L\}$ je **vzor množiny** $L \subseteq N$ (značíme $f^{-1}(a) := f^{-1}(\{a\})$);
- $f$ je **injektivní (prosté):** $(\forall x,y)(f(x)=f(y) \Rightarrow x=y)$;
- $f$ je **surjektivní (na):** $(\forall y \in N)(\exists x \in M)(f(x)=y)$, tj. $f(M)=N$;
- $f$ je **bijektivní**, je-li současně injektivní i surjektivní;
- složené zobrazení $(f \circ g)(x) := f(g(x))$; **identické zobrazení** $E_M(x) := x$; **inverzní zobrazení** $f^{-1}$ splňuje $f \circ f^{-1} = E_N$, $f^{-1} \circ f = E_M$ a existuje právě tehdy, když $f$ je bijekce.

**Definice (lineární zobrazení).** Buďte $P, Q$ vektorové prostory nad **stejným** tělesem $T$. Zobrazení $A : P \to Q$ nazveme **lineární**, právě když současně platí:

1. **(aditivita)** $(\forall x, y \in P)\big(A(x+y) = Ax + Ay\big)$;
2. **(homogenita)** $(\forall \alpha \in T)(\forall x \in P)\big(A(\alpha x) = \alpha Ax\big)$.

Množinu všech lineárních zobrazení z $P$ do $Q$ značíme $\mathcal{L}(P,Q)$. Toto je definice pojmu **[[Lineární-zobrazení]]**.

> Na levé straně rovností sčítáme/násobíme operacemi prostoru $P$, na pravé straně operacemi prostoru $Q$.

**Speciální případy se samostatným jménem (Definice 3.2):**
- **lineární operátor (transformace)** na $P$: lineární zobrazení z $P$ do **téhož** $P$; značíme $\mathcal{L}(P) := \mathcal{L}(P,P)$;
- **lineární funkcionál** na $P$: lineární zobrazení z $P$ do tělesa $T$;
- **izomorfismus**: lineární zobrazení, které je bijekce.

**Tvrzení (alternativní vyjádření linearity).** Pro $A : P \to Q$ jsou ekvivalentní:
1. $A \in \mathcal{L}(P,Q)$;
2. $(\forall \alpha \in T)(\forall x,y \in P)\big(A(\alpha x + y) = \alpha Ax + Ay\big)$;
3. $(\forall n)(\forall \alpha_1,\dots,\alpha_n \in T)(\forall x_1,\dots,x_n \in P)\Big(A\big(\sum_{i=1}^n \alpha_i x_i\big) = \sum_{i=1}^n \alpha_i Ax_i\Big)$.

Bod 3 (linearita „přenáší" celé lineární kombinace) se dokazuje indukcí podle $n$ z bodu 2.

**Příklady.** Lineární jsou např.: $A : \mathbb{R}\to\mathbb{R}$, $Ax := a\cdot x$ pro pevné $a$; násobení vektoru maticí $A(x) := \mathbf{A}\cdot x$ pro $\mathbf{A}\in T^{m,n}$ (zobrazení $T^n \to T^m$); identický operátor $Ex = x$; derivování polynomů; **souřadnicový izomorfismus** $(\cdot)_{\mathcal{B}} : V \to T^n$. Naopak afinní funkce $f(x) = ax + b$ s $b \neq 0$ lineární **není** (porušuje homogenitu: $f(0\cdot 0) = b \neq 0 = 0\cdot f(0)$).

**Souřadnicový izomorfismus.** Je-li $\mathcal{B} = (x_1,\dots,x_n)$ báze VP $V$ nad $T$, je přiřazení souřadnic $(\cdot)_{\mathcal{B}} : V \to T^n$, $x \mapsto (x)_{\mathcal{B}}$, izomorfismus (Věta 3.1). Důsledek: každý VP dimenze $d$ nad $T$ má stejnou mohutnost jako $T^d$.

---

## 2. Vlastnosti lineárního zobrazení

**Věta (základní vlastnosti, Věta 3.2).** Nechť $A \in \mathcal{L}(P,Q)$. Potom:

1. **Obraz nulového vektoru je nulový vektor:** $A\theta_P = \theta_Q$.
2. **Obraz lineárního obalu je lineární obal obrazů:** pro $M \subseteq P$ je $A(\langle M \rangle) = \langle A(M)\rangle$; speciálně pro soubor $(x_1,\dots,x_n)$
$$A\big(\langle x_1,\dots,x_n\rangle\big) = \langle Ax_1,\dots,Ax_n\rangle.$$
3. **Obraz podprostoru je podprostor:** $\tilde P \subset\subset P \Rightarrow A(\tilde P) \subset\subset Q$.
4. **Vzor podprostoru je podprostor:** $\tilde Q \subset\subset Q \Rightarrow A^{-1}(\tilde Q) \subset\subset P$.
5. **Obraz LZ souboru je LZ:** $(x_1,\dots,x_n)$ LZ $\Rightarrow (Ax_1,\dots,Ax_n)$ LZ.
6. **„Předobraz" LN souboru je LN:** $(Ax_1,\dots,Ax_n)$ LN $\Rightarrow (x_1,\dots,x_n)$ LN.

**Důkaz (vybrané body).**
- *Bod 1.* $A\theta_P = A(0\cdot\theta_P) = 0\cdot A\theta_P = \theta_Q$ (homogenita).
- *Bod 2, inkluze $\langle A(M)\rangle \supseteq A(\langle M\rangle)$.* Je-li $y \in A(\langle M\rangle)$, existuje $x \in \langle M\rangle$ s $Ax = y$, tj. $x = \sum_i \alpha_i x_i$ pro $x_i \in M$. Z linearity $y = Ax = A\big(\sum_i \alpha_i x_i\big) = \sum_i \alpha_i Ax_i \in \langle A(M)\rangle$. Opačná inkluze obdobně.
- *Bod 5.* Je-li $(x_1,\dots,x_n)$ LZ, existují $\alpha_1,\dots,\alpha_n$ ne všechny nulové s $\sum_i \alpha_i x_i = \theta_P$. Pak $\sum_i \alpha_i Ax_i = A\big(\sum_i \alpha_i x_i\big) = A\theta_P = \theta_Q$ je netriviální LK dávající nulový vektor, tedy $(Ax_1,\dots,Ax_n)$ je LZ.
- *Bod 6* je obměna bodu 5. $\square$

**Věta (o určení lin. zobrazení obrazy báze, Věta 3.3).** Nechť $P,Q$ jsou VP nad $T$, $(x_1,\dots,x_n)$ báze $P$ a $(y_1,\dots,y_n)$ libovolný soubor vektorů z $Q$. Potom existuje **právě jedno** $A \in \mathcal{L}(P,Q)$ s
$$(\forall i \in \hat n)(Ax_i = y_i).$$

*Idea důkazu.* Každé $z \in P$ se jednoznačně píše $z = \sum_i \alpha_i x_i$. Má-li $A$ být lineární a splňovat $Ax_i = y_i$, musí nutně $Az = \sum_i \alpha_i y_i$ — tím je $A$ jednoznačně určeno. Naopak takto definované $A$ je dobře definované, lineární a splňuje zadání (linearita se ověří přes souřadnicový izomorfismus). $\square$

> **Klíčové.** Lineární zobrazení je plně určeno obrazy vektorů libovolné báze. To je základ pojmu matice zobrazení (kap. 5).

**Tvrzení (o složení a inverzi, Tvrzení 3.2).** Pro VP $P,Q,R$ nad stejným $T$:
1. $A \in \mathcal{L}(P,Q)$, $B \in \mathcal{L}(Q,R) \Rightarrow$ složené $BA \in \mathcal{L}(P,R)$;
2. je-li $A \in \mathcal{L}(P,Q)$ izomorfismus, je i $A^{-1} \in \mathcal{L}(Q,P)$ (inverze izomorfismu je izomorfismus).

---

## 3. Jádro, obraz, hodnost a defekt

**Definice (hodnost, jádro, defekt, Definice 3.4).** Nechť $A \in \mathcal{L}(P,Q)$.

- **Obor hodnot (obraz)** je $A(P) = \operatorname{Im} A$; **hodnost zobrazení**
$$h(A) := \dim A(P).$$
- **Jádro** zobrazení je množina
$$\ker A := \{x \in P \mid Ax = \theta_Q\} = A^{-1}(\theta_Q).$$
- **Defekt** je $d(A) := \dim \ker A$.

Z bodů 3 a 4 Věty 3.2 plyne, že $A(P) \subset\subset Q$ a $\ker A = A^{-1}(\theta_Q) \subset\subset P$ jsou podprostory, takže má smysl mluvit o jejich dimenzích.

> **Pozor.** Hodnost *zobrazení* $h(A)$ je principiálně **odlišný pojem** od **[[Hodnost-matice|hodnosti matice]]** — souvislost teprve dokážeme (Věta 4.3). Geometricky: $\ker A$ je „co se zhroutí do $\theta_Q$", $A(P)$ je „obsazená část" cílového prostoru.

**Výpočet (Příklad 3.4).**
- *Jádro:* řešíme homogenní soustavu $Ax = \theta$ (za $x$ obecný vektor) → její řešení popisují $\ker A$.
- *Obor hodnot:* je-li $(x_1,\dots,x_n)$ báze $P$, pak $A(P) = \langle Ax_1,\dots,Ax_n\rangle$ (bod 2 Věty 3.2); z tohoto generujícího souboru vybereme bázi.

**Příklad.** $B : \mathbb{C}^3\to\mathbb{C}^2$, $B(x,y,z) = (x+2y-z,\ x-2y-3z)$. Rovnice $B(x,y,z) = \theta$ vede na soustavu s řešením $\langle(4,-1,2)\rangle$, tedy $\ker B = \langle(4,-1,2)\rangle$ (defekt $1$). Obor hodnot $B(\mathbb{C}^3) = \langle Be_1, Be_2, Be_3\rangle = \langle(1,1),(2,-2)\rangle = \mathbb{C}^2$ (hodnost $2$).

---

## 4. Injektivita, surjektivita, izomorfismus

### 4.1 Charakterizace injektivity jádrem

**Věta (o jádru prostého zobrazení, Věta 3.4).** Nechť $A \in \mathcal{L}(P,Q)$. Potom
$$A \text{ je prosté} \iff \ker A = \{\theta_P\}.$$

**Důkaz.**
- „$\Rightarrow$": je-li $A$ prosté, pak rovnici $Ax = \theta_Q$ řeší nejvýše jeden prvek; protože $A\theta_P = \theta_Q$ (bod 1 Věty 3.2), je $\ker A = A^{-1}(\theta_Q) = \{\theta_P\}$.
- „$\Leftarrow$": nechť $x,y \in P$ splňují $Ax = Ay$. Z linearity $A(x-y) = Ax - Ay = \theta_Q$, tedy $x - y \in \ker A = \{\theta_P\}$, takže $x - y = \theta_P$, neboli $x = y$. $\square$

**Věta (LN/LZ soubor a prosté zobrazení, Věta 3.5) a Důsledek 3.1.** Je-li $A \in \mathcal{L}(P,Q)$ **prosté**, pak obraz LN souboru je LN a vzor LZ souboru je LZ; dohromady s bodem 5 Věty 3.2:
$$(x_1,\dots,x_n) \text{ LN} \iff (Ax_1,\dots,Ax_n) \text{ LN}.$$
Prosté lineární zobrazení tedy **zachovává lineární nezávislost**.

### 4.2 Zachování dimenze a vztahy in/sur-jektivity

**Věta (zachování dimenze, Věta 3.6).** Pro $A \in \mathcal{L}(P,Q)$ a podprostor $M \subset\subset P$:
1. $\dim A(M) \le \dim M$;
2. je-li $A$ prosté, pak $\dim A(M) = \dim M$;
3. $h(A) \le \min\{\dim P, \dim Q\}$.

**Pozorování (vztah in/sur-jektivity a defektu/hodnosti, Pozorování 3.1).** Nechť $A \in \mathcal{L}(P,Q)$ a $\dim P, \dim Q < \infty$. Potom:
$$A \text{ je injektivní} \iff \ker A = \{\theta_P\} \iff d(A) = 0 \iff h(A) = \dim P,$$
$$A \text{ je surjektivní} \iff A(P) = Q \iff h(A) = \dim Q.$$

**Důsledek (izomorfismus mezi VP stejné dimenze, Důsledek 3.2).** Je-li $\dim P = \dim Q < \infty$ a $A \in \mathcal{L}(P,Q)$, pak je $A$ **injektivní právě tehdy, když je surjektivní** (a tedy je-li jedno z toho, je rovnou izomorfismus).

*Důkaz.* $A$ prosté $\iff d(A)=0 \overset{(*)}{\iff} h(A) = \dim P \overset{(**)}{\iff} A(P) = Q \iff A$ je na, kde $(*)$ je 2. věta o dimenzi a $(**)$ plyne z $\dim A(P) = h(A) = \dim P = \dim Q < \infty$ (podprostor téže konečné dimenze jako celek je celkem). $\square$

---

## 5. Vztah hodnosti a defektu (2. věta o dimenzi)

**Věta (2. věta o dimenzi / rank-nullity theorem, Věta 3.7).** Nechť $A \in \mathcal{L}(P,Q)$. Potom
$$\boxed{\,h(A) + d(A) = \dim P\,}.$$

**Důkaz.** Nekonečné případy: je-li $d(A) = \infty$, pak $\dim\ker A = \infty \le \dim P$, takže $\dim P = \infty$ a rovnost platí; obdobně je-li $h(A) = \infty = \dim A(P) \le \dim P$. Předpokládejme tedy obojí konečné. Okrajově: je-li $d(A)=0$, je $A$ prosté a z bodu 2 Věty 3.6 je $h(A) = \dim A(P) = \dim P$, tj. $h(A)+0=\dim P$; je-li $h(A)=0$, je $A(P)=\{\theta_Q\}$, tedy $\ker A = P$ a $0 + d(A) = \dim P$.

Hlavní případ $0 < d(A) < \infty$. Nechť $k := d(A)$ a $(x_1,\dots,x_k)$ báze $\ker A$, $(y_1,\dots,y_\ell)$ báze $A(P)$ (kde $\ell := h(A)$). Protože $y_i \in A(P)$, existují $z_1,\dots,z_\ell \in P$ s $Az_i = y_i$. Tvrdíme, že $(x_1,\dots,x_k,z_1,\dots,z_\ell)$ je báze $P$.

*LN.* Mějme LK dávající nulu:
$$\theta_P = \alpha_1 x_1 + \cdots + \alpha_k x_k + \beta_1 z_1 + \cdots + \beta_\ell z_\ell. \tag{$\ast$}$$
Aplikujeme $A$ a využijeme $Ax_i = \theta_Q$:
$$\theta_Q = A(\theta_P) = \beta_1 Az_1 + \cdots + \beta_\ell Az_\ell = \beta_1 y_1 + \cdots + \beta_\ell y_\ell.$$
Protože $(y_1,\dots,y_\ell)$ je LN, je $\beta_1 = \cdots = \beta_\ell = 0$. Vztah $(\ast)$ se redukuje na $\theta_P = \sum_i \alpha_i x_i$, a protože $(x_1,\dots,x_k)$ je LN, je i $\alpha_1 = \cdots = \alpha_k = 0$. Soubor je tedy LN.

*Generuje $P$.* Vezmi $v \in P$. Pak $Av \in A(P)$, tedy $Av = \sum_i \beta_i y_i$ pro nějaké $\beta_i$. Položme $u := v - (\beta_1 z_1 + \cdots + \beta_\ell z_\ell)$. Pak
$$Au = Av - \textstyle\sum_i \beta_i Az_i = Av - \sum_i \beta_i y_i = \theta_Q,$$
takže $u \in \ker A$, tedy $u = \sum_i \alpha_i x_i$. Celkem $v = u + (v-u) = \sum_i \alpha_i x_i + \sum_i \beta_i z_i$, takže soubor generuje $P$.

Soubor délky $k + \ell$ je báze $P$, proto $\dim P = k + \ell = d(A) + h(A)$. $\square$

---

## 6. Rovnice typu $Ax = b$ (most ke SLR)

**Věta (o řešení rovnice $Ax=b$, Věta 3.8).** Nechť $A \in \mathcal{L}(P,Q)$, $b \in Q$. Existuje-li $\tilde x \in P$ s $A\tilde x = b$ (partikulární řešení), pak množina všech řešení je
$$A^{-1}(b) = \tilde x + \ker A.$$

*Idea důkazu.* $x \in A^{-1}(b) \iff Ax = b = A\tilde x \iff A(x-\tilde x) = \theta_Q \iff x - \tilde x \in \ker A \iff x \in \tilde x + \ker A$. $\square$

Množina řešení je tedy buď prázdná, nebo **lineární varieta** „vektor plus podprostor" v $P$ — přirozené zobecnění množiny řešení **[[Soustava-lineárních-rovnic|soustavy lineárních rovnic]]** (SLR).

**Soustavy lineárních rovnic jako speciální případ.** Pro $\mathbf{A} \in T^{m,n}$, $b \in T^m$ definuje předpis $Ax := \mathbf{A}\cdot x$ lineární zobrazení $A \in \mathcal{L}(T^n, T^m)$. Potom množina řešení soustavy $\mathbf{A}x = b$ je $S = A^{-1}(b) = \tilde x + S_0$, kde $S_0 = \ker A$ je množina řešení přidružené homogenní soustavy. Navíc $h(A) = h(\mathbf{A})$ (obor hodnot je obal sloupců $\mathbf{A}$), takže **2. věta o dimenzi** dává třetí část Frobeniovy věty (Věta 3.9):
$$\dim S_0 = d(A) = n - h(A) = n - h(\mathbf{A}).$$

---

## 7. Matice lineárního zobrazení

### 7.1 Motivace a zavedení

Chtěli bychom ke každému $A$ najít matici $\mathbf{A}$ tak, aby $A(x) = \mathbf{A}\cdot x$. To obecně nelze (např. pro $x$ polynom součin matice $\times$ polynom nedává smysl). Řešení: pro VP **konečné dimenze** nahradíme vektory jejich **souřadnicemi vzhledem k bázím** (to jsou prvky $T^n$, s nimiž umíme počítat). Hledáme tedy matici $\mathbf{A}$ s
$$\mathbf{A}\cdot (z)_{\mathcal{X}} = (Az)_{\mathcal{Y}}.$$

**Souřadnice vzhledem k bázi.** Je-li $\mathcal{X} = (x_1,\dots,x_n)$ báze $V$ a $z = \sum_i \alpha_i x_i$, jsou $(z)_{\mathcal{X}} := (\alpha_1,\dots,\alpha_n) \in T^n$ (ztotožňujeme $T^n \cong T^{n,1}$, tj. souřadnice píšeme do sloupce). Pro bázový vektor platí $(x_i)_{\mathcal{X}} = e_i$ (Pozorování 4.2).

**Definice (matice zobrazení vzhledem k bázím, Definice 4.1).** Nechť $A \in \mathcal{L}(P,Q)$, $\mathcal{X} = (x_1,\dots,x_n)$ báze $P$, $\mathcal{Y} = (y_1,\dots,y_m)$ báze $Q$. **Matici zobrazení $A$ vzhledem k bázím $\mathcal{X},\mathcal{Y}$** definujeme po sloupcích jako
$$\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)_{:i} := (Ax_i)_{\mathcal{Y}}, \qquad i \in \hat n,$$
tedy schematicky
$$ {}^{\mathcal{X}}A^{\mathcal{Y}} = \big( (Ax_1)_{\mathcal{Y}} \ \ (Ax_2)_{\mathcal{Y}} \ \ \cdots \ \ (Ax_n)_{\mathcal{Y}} \big) \in T^{m,n}.$$
$i$-tý sloupec jsou **souřadnice obrazu $i$-tého bázového vektoru** vzhledem k cílové bázi. Pro operátor $A \in \mathcal{L}(P)$ píšeme zkráceně ${}^{\mathcal{X}}A := {}^{\mathcal{X}}A^{\mathcal{X}}$. Toto je pojem **[[Matice-lineárního-zobrazení]]**. Je-li $\mathcal{E}$ standardní báze, používá se zkrácené značení (např. ${}^{\mathcal{X}}A^{\mathcal{E}}$).

### 7.2 Vlastnosti matice zobrazení

**Věta (matice zobrazení funguje správně, Věta 4.1).** Pro $A \in \mathcal{L}(P,Q)$, báze $\mathcal{X},\mathcal{Y}$ a každé $z \in P$ platí
$$(Az)_{\mathcal{Y}} = {}^{\mathcal{X}}A^{\mathcal{Y}} \cdot (z)_{\mathcal{X}}.$$

*Idea důkazu.* Píšeme $(z)_{\mathcal{X}} = (\alpha_1,\dots,\alpha_n)$, tedy $z = \sum_k \alpha_k x_k$. Z definice násobení matice sloupcem a z linearity přiřazení souřadnic:
$${}^{\mathcal{X}}A^{\mathcal{Y}}\cdot(z)_{\mathcal{X}} = \sum_k \alpha_k \big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)_{:k} = \sum_k \alpha_k (Ax_k)_{\mathcal{Y}} = \Big(\sum_k \alpha_k Ax_k\Big)_{\mathcal{Y}} = (Az)_{\mathcal{Y}}. \qquad \square$$

**Důsledek (hledání vzoru, Důsledek 4.1).** Pro $w \in Q$ je $z$ vzorem $w$ (tj. $Az = w$) **právě tehdy, když** $(z)_{\mathcal{X}}$ řeší soustavu s rozšířenou maticí
$$\big({}^{\mathcal{X}}A^{\mathcal{Y}} \mid (w)_{\mathcal{Y}}\big).$$
Hledání vzoru se tedy převádí na řešení SLR. Speciálně $\ker A$ najdeme řešením $\big({}^{\mathcal{X}}A^{\mathcal{Y}} \mid \theta\big)$ (řešení jsou souřadnice vektorů z jádra vzhledem k $\mathcal{X}$).

**Praktická pravidla.**
- *Matici zobrazení* spočteme tak, že najdeme obrazy báze $\mathcal{X}$ a jejich souřadnice vzhledem k $\mathcal{Y}$ (sloupce matice).
- *Obraz vektoru:* vynásobíme matici zobrazení sloupcem souřadnic vektoru.
- *Vzor vektoru:* řešíme SLR (matice zobrazení | sloupec souřadnic) — výsledek je třeba interpretovat jako souřadnice vzhledem k $\mathcal{X}$.

**Věta (matice složeného zobrazení, Věta 4.2).** Nechť $A \in \mathcal{L}(Q,V)$, $B \in \mathcal{L}(P,Q)$ a $\mathcal{X},\mathcal{Y},\mathcal{W}$ jsou postupně báze $P,Q,V$ (konečné dimenze). Potom **složení odpovídá součinu matic**:
$$ {}^{\mathcal{X}}(AB)^{\mathcal{W}} = {}^{\mathcal{Y}}A^{\mathcal{W}} \cdot {}^{\mathcal{X}}B^{\mathcal{Y}}.$$

**Důsledek (matice izomorfismu, Důsledek 4.2).** Je-li $A \in \mathcal{L}(P,Q)$ izomorfismus a $\dim P, \dim Q < \infty$, pak je ${}^{\mathcal{X}}A^{\mathcal{Y}}$ **[[Matice|čtvercová]] regulární matice** a
$$\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)^{-1} = {}^{\mathcal{Y}}(A^{-1})^{\mathcal{X}}.$$
(Plyne z Věty 4.2 použité na $A\circ A^{-1}$, kde matice identického operátoru vychází $E$.)

**Věta (souvislost hodnosti zobrazení a hodnosti matice, Věta 4.3).** Nechť $A \in \mathcal{L}(P,Q)$, $\dim P, \dim Q < \infty$, $\mathcal{X}$ báze $P$, $\mathcal{Y}$ báze $Q$. Potom
$$h(A) = h\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big).$$

*Idea důkazu.* $h(A) = \dim A(P) = \dim\langle Ax_1,\dots,Ax_n\rangle$. Souřadnicový izomorfismus $(\cdot)_{\mathcal{Y}}$ zachovává dimenzi obalu, takže $= \dim\langle (Ax_1)_{\mathcal{Y}},\dots,(Ax_n)_{\mathcal{Y}}\rangle$. Tyto souřadnice jsou ale přesně sloupce matice ${}^{\mathcal{X}}A^{\mathcal{Y}}$, takže $= h({}^{\mathcal{X}}A^{\mathcal{Y}})$ (hodnost = dimenze obalu sloupců). $\square$

> Tím se smiřuje dvojí význam slova „hodnost": hodnost *zobrazení* se rovná hodnosti jeho *matice* v libovolných bázích. Defekt pak dopočítáme z 2. věty o dimenzi: $d(A) = \dim P - h(A)$.

### 7.3 Změna báze a matice přechodu

**Definice (matice přechodu, Definice 4.2).** Nechť $\mathcal{X} = (x_1,\dots,x_n)$ a $\mathcal{Y}$ jsou báze $P$. Matici **identického operátoru** ${}^{\mathcal{X}}E^{\mathcal{Y}} \in T^{n,n}$ nazýváme **maticí přechodu** od báze $\mathcal{X}$ k bázi $\mathcal{Y}$. Jelikož $Ex = x$, platí
$$ {}^{\mathcal{X}}E^{\mathcal{Y}} = \big( (x_1)_{\mathcal{Y}} \ \ (x_2)_{\mathcal{Y}} \ \ \cdots \ \ (x_n)_{\mathcal{Y}} \big),$$
tj. ve sloupcích souřadnice vektorů z $\mathcal{X}$ vzhledem k $\mathcal{Y}$.

**Věta (vlastnosti matice přechodu, Věta 4.4).** Nechť $\mathcal{X},\mathcal{Y},\mathcal{Z}$ jsou báze $P$, $\dim P < \infty$. Potom:
1. $(\forall x \in P)\ {}^{\mathcal{X}}E^{\mathcal{Y}}\cdot (x)_{\mathcal{X}} = (x)_{\mathcal{Y}}$ (přepočet souřadnic mezi bázemi);
2. ${}^{\mathcal{X}}E^{\mathcal{Y}}$ je regulární a $\big({}^{\mathcal{X}}E^{\mathcal{Y}}\big)^{-1} = {}^{\mathcal{Y}}E^{\mathcal{X}}$;
3. ${}^{\mathcal{Y}}E^{\mathcal{Z}}\cdot {}^{\mathcal{X}}E^{\mathcal{Y}} = {}^{\mathcal{X}}E^{\mathcal{Z}}$.

(Vše plyne z Věty 4.1 a 4.2 použitých na identický operátor a z $E\circ E = E$, $E^{-1}=E$.) Pro přechod **do standardní báze** je matice triviální: ${}^{\mathcal{X}}E^{\mathcal{E}_n} = (x_1\ \cdots\ x_n)$ (vektory $\mathcal{X}$ jako sloupce).

**Věta (změna bází v matici zobrazení, Věta 4.5).** Nechť $A \in \mathcal{L}(P,Q)$, $\dim P, \dim Q < \infty$, $\mathcal{X},\tilde{\mathcal{X}}$ báze $P$, $\mathcal{Y},\tilde{\mathcal{Y}}$ báze $Q$. Potom
$$\boxed{\,{}^{\tilde{\mathcal{X}}}A^{\tilde{\mathcal{Y}}} = {}^{\mathcal{Y}}E^{\tilde{\mathcal{Y}}} \cdot {}^{\mathcal{X}}A^{\mathcal{Y}} \cdot {}^{\tilde{\mathcal{X}}}E^{\mathcal{X}}\,}.$$
Je to přímý důsledek Věty 4.2 (matice složeného zobrazení) aplikované na $A = E_Q \circ A \circ E_P$.

*Speciální případ — operátor a podobnost.* Pro $A \in \mathcal{L}(P)$ a dvě báze $\mathcal{X},\tilde{\mathcal{X}}$ je ${}^{\tilde{\mathcal{X}}}A = R^{-1}\,{}^{\mathcal{X}}A\,R$, kde $R = {}^{\tilde{\mathcal{X}}}E^{\mathcal{X}}$ — matice téhož operátoru v různých bázích jsou **podobné**. Je-li $\mathcal{X}$ tvořena vlastními vektory, vyjde ${}^{\mathcal{X}}A$ diagonální (diagonalizace).

**Příklad.** $A \in \mathcal{L}(\mathbb{Z}_5^3, \mathbb{Z}_5^2)$, $A(a,b,c) = (a+2b,\ b+3c)$. Vzhledem ke standardní bázi: $Ae_1 = (1,0)$, $Ae_2 = (2,1)$, $Ae_3 = (0,3)$, tedy
$${}^{\mathcal{E}_3}A^{\mathcal{E}_2} = \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 3 \end{pmatrix}.$$
Obraz $z = (1,2,4)$: $Az = {}^{\mathcal{E}_3}A^{\mathcal{E}_2}\cdot(1,2,4)^T = (0,4)$. Vzor $(1,3)$ řeší soustavu $\big(\,{}^{\mathcal{E}_3}A^{\mathcal{E}_2}\mid(1,3)^T\big)$, řešení $A^{-1}(1,3) = (1,0,1)+\langle(2,1,1)\rangle$.

---

## Co je potřeba na zkoušku znát

### Definice
- **Lineární zobrazení** $A\in\mathcal{L}(P,Q)$: aditivita + homogenita (nad stejným tělesem). Operátor, funkcionál, izomorfismus.
- **Obor hodnot** $A(P)$, **hodnost** $h(A)=\dim A(P)$; **jádro** $\ker A = A^{-1}(\theta_Q)$, **defekt** $d(A)=\dim\ker A$.
- **Injektivita / surjektivita / bijekce**; izomorfismus = lineární bijekce.
- **Matice zobrazení** ${}^{\mathcal{X}}A^{\mathcal{Y}}$: $i$-tý sloupec $=(Ax_i)_{\mathcal{Y}}$. **Matice přechodu** ${}^{\mathcal{X}}E^{\mathcal{Y}}$.

### Věty s důkazy
- **2. věta o dimenzi (rank-nullity):** $h(A)+d(A)=\dim P$ — důkaz sestavením báze $P$ z báze jádra a vzorů báze oboru hodnot.
- **O jádru prostého zobrazení:** $A$ prosté $\iff \ker A=\{\theta_P\}$.
- **Vztah in/sur-jektivity:** $A$ prosté $\iff d(A)=0 \iff h(A)=\dim P$; $A$ na $\iff h(A)=\dim Q$. Při $\dim P=\dim Q<\infty$: prosté $\iff$ na.
- **Matice zobrazení funguje:** $(Az)_{\mathcal{Y}}={}^{\mathcal{X}}A^{\mathcal{Y}}\cdot(z)_{\mathcal{X}}$.
- **Hodnost:** $h(A)=h({}^{\mathcal{X}}A^{\mathcal{Y}})$; **složení = součin matic**; **změna báze** ${}^{\tilde{\mathcal{X}}}A^{\tilde{\mathcal{Y}}}={}^{\mathcal{Y}}E^{\tilde{\mathcal{Y}}}\,{}^{\mathcal{X}}A^{\mathcal{Y}}\,{}^{\tilde{\mathcal{X}}}E^{\mathcal{X}}$.

### Algoritmy
- **Jádro:** vyřeš homogenní soustavu $Ax=\theta$ (resp. $({}^{\mathcal{X}}A^{\mathcal{Y}}\mid\theta)$); řešení jsou souřadnice vektorů jádra.
- **Obor hodnot:** $A(P)=\langle Ax_1,\dots,Ax_n\rangle$, vyber bázi.
- **Matice zobrazení:** spočti obrazy báze $\mathcal{X}$ a jejich souřadnice v $\mathcal{Y}$ → sloupce.
- **Obraz / vzor:** $\mathbf{A}\cdot(z)_{\mathcal{X}}$ / řeš SLR $(\mathbf{A}\mid(w)_{\mathcal{Y}})$.
- **Matice přechodu mezi nestandardními bázemi:** přes standardní bázi, ${}^{\mathcal{X}}E^{\mathcal{Y}}=({}^{\mathcal{Y}}E^{\mathcal{E}})^{-1}\,{}^{\mathcal{X}}E^{\mathcal{E}}$, počítá se GEM na dvojbloku.
