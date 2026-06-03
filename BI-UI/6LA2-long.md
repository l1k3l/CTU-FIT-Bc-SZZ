---
tags: [otázka, kurz/LA2, otázka/6, todo]
---

# Výpočet vlastních čísel: mocninná metoda a QR algoritmus

> **Otázka SZZ:** Výpočet vlastních čísel, mocninná metoda, QR algoritmus.

Zdroje: BI-LA2 (textbook FIT ČVUT), kap. 10 (Spektrum matic) — 10.2 Připomenutí BI-LA1, 10.3 Spektrální rozklad symetrických matic, 10.4 Pozitivní (semi)definitnost, 10.5 Výpočet vlastních čísel, 10.6–10.8 Mocninná metoda, 10.9–10.10 QR algoritmus, 10.11 Příprava matice pro QR algoritmus (printed 191–210).

Značení: $\lambda$ vlastní číslo, $\sigma(A)$ spektrum, $A \in \mathbb{R}^{n,n}$ (vlastní čísla mohou být i komplexní), $Q$ ortogonální matice, $\Lambda$ (resp. $D$) diagonální matice, $E$ jednotková matice, $A^T$ transpozice, $\theta$ nulový vektor, $\|\cdot\|_2$ eukleidovská norma, $x$ vektory.

---

## 1. Připomenutí vlastních čísel a spektrální rozklad symetrických matic

### 1.1 Vlastní čísla, vektory, diagonalizace (BI-LA1)

**Definice ([[Vlastní-číslo|vlastní číslo]]):** Číslo $\lambda \in \mathbb{C}$ je vlastní číslo matice $A \in \mathbb{R}^{n,n}$, právě když existuje **nenulový** vektor $x \in \mathbb{C}^n$ s
$$A x = \lambda x.$$
Vektor $x$ je příslušný **vlastní vektor**. Množina všech vlastních čísel je **spektrum** $\sigma(A)$.

**[[Diagonalizace]]** (též **spektrální rozklad**) čtvercové matice je rozklad
$$A = P D P^{-1},$$
kde $D$ je diagonální (vlastní čísla na diagonále, každé tolikrát, kolik je jeho geometrická násobnost) a $P$ je regulární, ve sloupcích vlastní vektory v odpovídajícím pořadí. Z $AP = PD$ je vidět, že $j$-tý sloupec dává $A x_j = \lambda_j x_j$.

**Věta 10.1 (o diagonalizovatelnosti).** Pro $A \in \mathbb{R}^{n,n}$ jsou ekvivalentní:
1. $A$ je diagonalizovatelná;
2. součet geometrických násobností všech vlastních čísel je $n$;
3. existuje báze $\mathbb{C}^n$ složená z vlastních vektorů $A$.

### 1.2 Spektrální rozklad symetrických matic

Reálné symetrické matice ($A^T = A$) mají mimořádně příjemnou strukturu spektra (Hessovy matice v BI-MA2, korelační/kovarianční matice, matice neorientovaných grafů).

**Věta 10.2 (o symetrických maticích) — [[Spektrální-rozklad|spektrální rozklad]].** Buď $S \in \mathbb{R}^{n,n}$ symetrická. Potom:
1. **všechna vlastní čísla $S$ jsou reálná**;
2. $S$ je „reálně" diagonalizovatelná a vlastní vektory lze volit reálné a tvořící **ortonormální bázi**: existuje [[Ortogonální-matice|ortogonální]] matice $Q \in \mathbb{R}^{n,n}$ a diagonální $D \in \mathbb{R}^{n,n}$ s
$$\boxed{\,S = Q D Q^T\,}.$$

**Důkaz reálnosti (část 1).** Buď $(\lambda, x)$ vlastní pár, $x \in \mathbb{C}^n$. S komplexním skalárním součinem počítáme dvěma způsoby:
$$\overline{x}^T S x = \overline{x}^T (\lambda x) = \lambda \overline{x}^T x = \lambda \|x\|_2^2,$$
$$\overline{x}^T S x = (S^T \overline{x})^T x = (\overline{S x})^T x = (\overline{\lambda x})^T x = \overline{\lambda}\, \overline{x}^T x = \overline{\lambda}\|x\|_2^2,$$
kde jsme využili symetrie ($S^T = S$), vlastnosti transpozice součinu a komplexního sdružení ($\overline{S} = S$, neboť $S$ je reálná). Porovnáním $\lambda\|x\|_2^2 = \overline{\lambda}\|x\|_2^2$ a $x \neq \theta$ plyne $\lambda = \overline{\lambda}$, tedy $\lambda \in \mathbb{R}$. $\square$

**Náznak důkazu existence rozkladu (část 2).** Indukcí podle $n$. Pro $n=1$ triviální. Pro krok $n \to n+1$: každá matice má (komplexní, zde reálné) vlastní číslo $\lambda_1$; vlastní vektor je nenulové řešení reálné soustavy $(S - \lambda_1 E)x = \theta$, lze ho volit reálný a jednotkový — $x_1$. Doplníme ho na ortonormální bázi (Gram–Schmidt) a sestavíme ortogonální $P$ se sloupci této báze. Částečná diagonalizace dá
$$B = P^T S P = \begin{pmatrix} \lambda_1 & 0 \\ 0 & C \end{pmatrix},$$
kde $B$ je opět symetrická ($B^T = P^T S^T P = B$), proto má nulový i první řádek a $C \in \mathbb{R}^{n,n}$ je symetrická. Z indukčního předpokladu $C = \tilde Q \tilde D \tilde Q^T$. Složením ortogonálních matic dostaneme $S = QDQ^T$ s ortogonální $Q$. $\square$

**Poznámka (normální matice).** Ortonormální báze z vlastních vektorů existuje pro širší třídu — **normální** matice ($A^T A = A A^T$): kromě symetrických i antisymetrické, ortogonální a cirkulantní. Pro komplexní normální matice platí $A = U D \overline{U}^T$ s **unitární** $U$ ($\overline{U}^T U = E$).

### 1.3 Pozitivní (semi)definitnost a spektrum

**Definice ([[Spektrální-rozklad|pozitivní definitnost]]).** Symetrická $S \in \mathbb{R}^{n,n}$ je
- **pozitivně definitní**, pokud $x^T S x > 0$ pro všechna $x \neq \theta$;
- **pozitivně semidefinitní**, pokud $x^T S x \ge 0$ pro všechna $x$.

(Každá pozitivně definitní je i semidefinitní; obráceně ne.)

**Věta 10.3 (o definitnosti a vlastních číslech).** Pro symetrickou $S$:
1. $S$ je pozitivně semidefinitní $\iff$ všechna vlastní čísla jsou **nezáporná**;
2. $S$ je pozitivně definitní $\iff$ všechna vlastní čísla jsou **kladná**.

**Důkaz.** „$\Rightarrow$": pro vlastní pár $(\lambda, x)$, $x$ reálný nenulový, je $0 \le x^T S x = x^T(\lambda x) = \lambda\|x\|_2^2$, tedy $\lambda \ge 0$ (resp. $>0$). „$\Leftarrow$": z $S = QDQ^T$ položíme $y = Q^T x$ (násobení ortogonální maticí nemění normu, tedy $y \neq \theta \iff x \neq \theta$):
$$x^T S x = (Q^T x)^T D (Q^T x) = y^T D y = \sum_{i=1}^n d_i y_i^2 \ge 0,$$
neboť $d_i \ge 0$; je-li dokonce $d_i > 0$, je suma $>0$ pro $y \neq \theta$. $\square$

**Gramovy matice.** Pro libovolnou $X \in \mathbb{R}^{m,n}$ jsou $X^T X$ a $X X^T$ symetrické, pozitivně **semidefinitní**, mají hodnost $h(X)$; $X^T X$ je pozitivně definitní $\iff h(X) = n$ (využití u [[SVD]]).

---

## 2. Výpočet vlastních čísel obecně

V BI-LA1 se vlastní čísla matic $2\times2$ a $3\times3$ hledala jako kořeny **charakteristického polynomu** $p_A(\lambda) = \det(A - \lambda E)$. Pro větší matice je to prakticky nepoužitelné:

- pro $n \ge 5$ má $p_A$ stupeň $n \ge 5$, a podle **Abelovy–Ruffiniho věty** kořeny obecného polynomu stupně $\ge 5$ **nelze vyjádřit v uzavřeném tvaru** (radikály) — neexistuje analogie vzorce pro kvadratickou rovnici;
- numerické hledání kořenů polynomu je navíc **velmi špatně podmíněná** úloha (malá změna koeficientů → velká změna kořenů).

**Pozorování 10.1 (o hledání vlastních čísel).** Algoritmus pro hledání vlastních čísel matic řádu $5 \times 5$ a více **musí být iterační**.

Dvě základní iterační metody: **mocninná metoda** (jedno / několik vlastních čísel) a **QR algoritmus** (všechna vlastní čísla).

---

## 3. Mocninná metoda

### 3.1 Idea

**[[Mocninná-metoda|Mocninná metoda]]** (power iteration) iteruje posloupnost znormovaných vektorů
$$\frac{x}{\|x\|_2},\ \frac{Ax}{\|Ax\|_2},\ \frac{A^2 x}{\|A^2 x\|_2},\ \frac{A^3 x}{\|A^3 x\|_2}, \dots$$
V každém kroku: **(1)** vynásob maticí $A$, **(2)** znormuj výsledek, **(3)** opakuj. Rekurzivně
$$v^{(k)} := \frac{A^k x}{\|A^k x\|_2} = \frac{A v^{(k-1)}}{\|A v^{(k-1)}\|_2}.$$
Za vhodných předpokladů posloupnost konverguje k vlastnímu vektoru příslušnému **dominantnímu** vlastnímu číslu (v absolutní hodnotě největšímu).

### 3.2 Odvození konvergence (symetrický případ)

Buď $A \in \mathbb{R}^{n,n}$ symetrická s ortonormální bází vlastních vektorů $(q_1, \dots, q_n)$ a vlastními čísly seřazenými
$$|\lambda_1| > |\lambda_2| \ge |\lambda_3| \ge \dots \ge |\lambda_n|.$$
(Ostrá nerovnost $|\lambda_1| > |\lambda_2|$ je požadavek na **jednoduchost** dominantního vlastního čísla.) Startovní vektor $x$ volíme tak, aby nebyl kolmý na $q_1$, tj. $q_1^T x \neq 0$, neboli $x \notin q_1^\perp = \langle q_2, \dots, q_n\rangle$. Rozložme $x = \alpha_1 q_1 + \dots + \alpha_n q_n$; pak $\alpha_1 \neq 0$.

Vektor $v^{(k)}$ je násobek $A^k x$ (díky normalizaci), tedy s $c_k = \|A^k x\|_2^{-1}$:
$$v^{(k)} = c_k A^k x = c_k\big(\alpha_1 A^k q_1 + \dots + \alpha_n A^k q_n\big) = c_k\big(\alpha_1 \lambda_1^k q_1 + \dots + \alpha_n \lambda_n^k q_n\big)$$
$$= c_k \lambda_1^k\Big(\alpha_1 q_1 + \alpha_2\Big(\tfrac{\lambda_2}{\lambda_1}\Big)^k q_2 + \dots + \alpha_n\Big(\tfrac{\lambda_n}{\lambda_1}\Big)^k q_n\Big).$$
Protože $\left|\tfrac{\lambda_i}{\lambda_1}\right| < 1$ pro $i \ge 2$, je $\left(\tfrac{\lambda_i}{\lambda_1}\right)^k \to 0$ a se zvyšujícím se $k$ se prosadí $q_1$. Po zapracování normalizačního faktoru
$$v^{(k)} = \frac{\lambda_1^k}{|\lambda_1|^k}\,\frac{\alpha_1}{|\alpha_1|}\,\frac{1}{\sqrt{1 + o(1)}}\big(q_1 + o(1)\big).$$
- Pro $\lambda_1 > 0$: $v^{(k)} \to \operatorname{sgn}(\alpha_1) q_1$.
- Pro $\lambda_1 < 0$: znaménko střídá, $v^{(2k)} \to \operatorname{sgn}(\alpha_1)q_1$, $v^{(2k+1)} \to -\operatorname{sgn}(\alpha_1)q_1$ — což nevadí, $q_1$ i $-q_1$ jsou přípustné vlastní vektory.

**Věta 10.6 (o mocninné metodě pro symetrické matice).** Buď $A$ symetrická s dominantním $\lambda_1 \neq 0$ geometrické násobnosti 1 a vlastním vektorem $q_1$. Není-li $x$ kolmý na $q_1$, pak
$$\frac{A^k x}{\|A^k x\|_2} \to q_1 \quad \text{nebo}\quad \to -q_1.$$

**Rychlost konvergence** je dána poměrem $\left|\dfrac{\lambda_2}{\lambda_1}\right|$ (lineární konvergence vlastního vektoru; chyba vlastního vektoru $\sim |\lambda_2/\lambda_1|^k$, chyba vlastního čísla $\sim |\lambda_2/\lambda_1|^{2k}$).

**Poznámka — nutnost jednoduchosti.** Není-li dominantní vlastní číslo jednoduché v absolutní hodnotě, metoda nekonverguje. Příklad: $A = \operatorname{diag}(1, -1)$, $x = (\alpha, \beta)$ s $\alpha, \beta \neq 0$ dává $A^k x = (\alpha, (-1)^k \beta)$ — vektor osciluje a nikdy se nepřiblíží žádnému vlastnímu vektoru.

### 3.3 Rayleighův podíl — odhad vlastního čísla

Mocninná metoda dává vlastní **vektor**; vlastní **číslo** odhadneme:
- jednoduše: pro index $i$ s největší složkou aproximace platí $\lambda_1 \approx \dfrac{(A v^{(k)})_i}{(v^{(k)})_i}$;
- lépe (zejména symetrické matice) **Rayleighovým podílem**.

**Definice 10.4 (Rayleighův podíl).** Pro $A \in \mathbb{R}^{n,n}$ a $y \neq \theta$
$$r(y) = \frac{y^T A y}{y^T y}.$$

**Tvrzení 10.1.** Je-li $x$ vlastní vektor příslušný $\lambda$, pak $r(x) = \lambda$.

**Důkaz.** $r(x) = \dfrac{x^T A x}{x^T x} = \dfrac{x^T(\lambda x)}{x^T x} = \lambda\dfrac{x^T x}{x^T x} = \lambda.$ $\square$

Pro $v^{(k)} \to q_1$ tedy $\lambda^{(k)} := r(v^{(k)}) \to \lambda_1$, a to **rychleji** (řád $|\lambda_2/\lambda_1|^{2k}$ místo $|\lambda_2/\lambda_1|^{k}$) — to je hlavní důvod jeho použití.

### 3.4 Pseudokód

```
Algoritmus: Mocninná metoda (symetrická varianta s Rayleighovým podílem)
  v⁽⁰⁾ ← libovolný vektor s ‖v⁽⁰⁾‖₂ = 1   (nekolmý na q₁)
  for k = 1, 2, … do
      w ← A · v⁽ᵏ⁻¹⁾                       # 1 násobení maticí–vektorem
      v⁽ᵏ⁾ ← w / ‖w‖₂                       # normalizace
      λ⁽ᵏ⁾ ← (v⁽ᵏ⁾)ᵀ A v⁽ᵏ⁾                 # Rayleighův podíl (odhad λ₁)
  end for                                   # stop: λ⁽ᵏ⁾ se mezi kroky mění minimálně
```
(Nesymetrická varianta: místo Rayleighova podílu $\lambda^{(k)} = (w)_i / (v^{(k-1)})_i$ pro $i$ s největší složkou.) Náklad na iteraci je dominantně jedno násobení matice–vektor $O(n^2)$ (pro řídké matice méně).

### 3.5 Varianty a využití (poznámky 10.4)

- **Konvergence vlastního čísla je kvadratická** oproti lineární konvergenci vlastního vektoru.
- Funguje i pro **nesymetrické** matice (opět nutná jednoduchost dominantního vlastního čísla).
- Vhodná pro **řídké** matice nebo matice zadané jen implicitně (umíme spočítat $Av$, ne samotnou $A$).
- Aplikace: **PageRank** (ohodnocení relevance webových stránek).
- **Deflace prostoru:** pro druhé vlastní číslo symetrické matice iterujeme v ortogonálním doplňku $q_1$, pro $k$-té v $\langle q_1, \dots, q_{k-1}\rangle^\perp$.
- **Inverzní iterace:** mocninná metoda na $A^{-1}$ najde **nejmenší** vlastní číslo v absolutní hodnotě.
- **Posunutá (inverzní) iterace:** máme-li odhad $\mu$ hledaného vlastního čísla, aplikujeme metodu na $(A - \mu E)^{-1}$ — najde vlastní číslo nejbližší $\mu$. (Iterace Rayleighova podílu volí $\mu$ adaptivně.)

---

## 4. QR algoritmus

Mocninná metoda dává jen jedno (či několik) vlastních čísel. Pro **všechna** vlastní čísla slouží **[[QR-algoritmus|QR algoritmus]]** — numericky stabilní iterace nad [[QR-rozklad|QR rozklady]] matic $A, A^2, \dots$

### 4.1 Iterace

$$A^{(0)} = A, \qquad A^{(k-1)} = Q^{(k)} R^{(k)}\ \text{(QR rozklad)}, \qquad A^{(k)} = R^{(k)} Q^{(k)}.$$
Slovy: v každém kroku **(1)** spočti QR rozklad aktuální matice ($A = QR$), **(2)** vrať součin v opačném pořadí ($RQ$), **(3)** opakuj.

```
Algoritmus: QR algoritmus
  A⁽⁰⁾ ← A
  for k = 1, 2, … do
      Q⁽ᵏ⁾ R⁽ᵏ⁾ ← A⁽ᵏ⁻¹⁾     # QR rozklad
      A⁽ᵏ⁾ ← R⁽ᵏ⁾ Q⁽ᵏ⁾         # součin v opačném pořadí
  end for                       # stop: prvky pod diagonálou (resp. mimo) ≈ 0
```

### 4.2 Zachování spektra podobností

**Tvrzení 10.2 (o vlivu QR algoritmu na vlastní čísla).** Matice $A^{(k)}$ konstruované QR algoritmem mají stejná vlastní čísla jako $A$.

**Důkaz.** Z $A^{(k-1)} = Q^{(k)} R^{(k)}$ a ortogonality $Q^{(k)}$ ($(Q^{(k)})^{-1} = (Q^{(k)})^T$) je $R^{(k)} = (Q^{(k)})^T A^{(k-1)}$. Dosazením do kroku 4:
$$A^{(k)} = R^{(k)} Q^{(k)} = (Q^{(k)})^T A^{(k-1)} Q^{(k)} = (Q^{(k)})^{-1} A^{(k-1)} Q^{(k)}.$$
To je transformace **podobnosti**, tedy $A^{(k)}$ je podobná $A^{(k-1)}$. Indukcí je $A^{(k)}$ podobná $A^{(0)} = A$, a podobné matice mají stejná vlastní čísla. $\square$

### 4.3 Konvergence k Schurově / trojúhelníkové formě

Posloupnost $A^{(k)}$ za vhodných předpokladů (vlastní čísla jednoduchá v absolutní hodnotě, $|\lambda_1| > |\lambda_2| > \dots$) konverguje k matici $B$, která je podobná $A$ (má tedy stejná vlastní čísla na diagonále):

- **symetrická matice** $A$ → posloupnost často konverguje k **diagonální** matici; vlastní čísla jsou pak prvky diagonály;
- **nesymetrická matice** $A$ → posloupnost často konverguje k **horní trojúhelníkové** matici; vlastní čísla jsou na diagonále.

Pro nesymetrické matice tak obecně dostáváme podobnost k horní trojúhelníkové matici s **ortogonální** maticí podobnosti — to je **Schurův rozklad**
$$A = Q R Q^T, \qquad Q \text{ ortogonální},\ R \text{ horní trojúhelníková}.$$

Rychlost konvergence dominantního prvku je řízena poměry sousedních vlastních čísel; čím blíže jsou dvě vlastní čísla, tím pomalejší konvergence příslušného prvku. **Selhání:** ortogonální matice $Q$ má rozklad $QE = Q$, takže QR iterace se zacyklí ($A^{(k)} = Q$) — vlastní čísla nejsou jednoduchá, všechna mají velikost 1.

### 4.4 Příprava matice: Hessenbergův / třídiagonální tvar

V základní podobě je QR algoritmus **drahý**: každá iterace je QR rozklad $n\times n$ + součin, $O(n^3)$, a iterací je mnoho. Šetříme tak, že matici nejprve převedeme **podobností** na tvar s mnoha nulami, na němž je každá iterace levná.

Použijeme **ortogonální** transformace (Householderovy reflexe) aplikované **oboustranně** — to zachová podobnost (a tedy spektrum) a u ortogonálních matic se snadno počítá inverze:
$$B = Q A Q^T = Q A Q^{-1}.$$

**„Špatný nápad".** Householderův reflektor $Q_1$ nulující celý první sloupec pod $\alpha$ při oboustranné aplikaci $Q_1 A Q_1$ matici **opět zaplní** (násobení zprava pokazí vynulované prvky).

**„Dobrý nápad".** Vynulujeme jen prvky **pod poddiagonálou** — reflektor ve tvaru $Q_1 = \begin{pmatrix}1 & \\ & F\end{pmatrix}$ zachová první prvek sloupce. Postupně $Q_2, \dots, Q_{n-2}$ dospějeme k matici v **Hessenbergově tvaru** (nuly pod poddiagonálou).

**Definice 10.5 (Hessenbergův tvar).** $A \in \mathbb{R}^{n,n}$ je v Hessenbergově tvaru, platí-li pro $i, j$:
$$j + 1 < i \implies a_{ij} = 0.$$

**Poznámka 10.6 — symetrický případ.** Je-li $A$ symetrická, je i výsledná matice symetrická, takže má nuly pod poddiagonálou **i nad naddiagonálou** → **třídiagonální** matice.

**Definice 10.6 (třídiagonální matice).** $A$ je třídiagonální, platí-li $|i - j| > 1 \implies a_{ij} = 0$.

Celkově $Q = Q_1 Q_2 \cdots Q_{n-2}$ dává faktorizaci
$$Q^T A Q = H, \qquad A = Q H Q^T,$$
takže $A$ a $H$ jsou podobné (stejné spektrum včetně násobností). Hessenbergův / třídiagonální tvar se v QR iteracích **zachovává**, takže výpočet je výrazně levnější.

```
Algoritmus: Householderova redukce do Hessenbergova tvaru
  for k = 1, …, n-2 do
      x  ← A[k+1:n, k]                          # podsloupec pod diagonálou
      vₖ ← sgn(x₁)·‖x‖₂·e₁ + x                  # Householderův vektor
      vₖ ← vₖ / ‖vₖ‖₂
      A[k+1:n, k:n] ← A[k+1:n, k:n] − 2 vₖ (vₖᵀ A[k+1:n, k:n])   # zleva
      A[1:n, k+1:n] ← A[1:n, k+1:n] − 2 (A[1:n, k+1:n] vₖ) vₖᵀ   # zprava
  end for
```

---

## Co je potřeba na zkoušku znát

### Definice
- Vlastní číslo / vlastní vektor, spektrum $\sigma(A)$; diagonalizace $A = PDP^{-1}$.
- Spektrální rozklad symetrické matice $S = QDQ^T$ ($Q$ ortogonální, $D$ diagonální reálná).
- Pozitivní (semi)definitnost $x^T S x > 0$ ($\ge 0$); Rayleighův podíl $r(y) = \frac{y^T A y}{y^T y}$.
- Hessenbergův tvar ($j+1<i \Rightarrow a_{ij}=0$), třídiagonální tvar ($|i-j|>1 \Rightarrow a_{ij}=0$), Schurův rozklad $A=QRQ^T$.

### Klíčové věty
- **Symetrická matice:** reálná vlastní čísla + ON báze vlastních vektorů, $S = QDQ^T$ (umět důkaz reálnosti).
- **Definitnost vs. spektrum:** pozitivně (semi)definitní $\iff$ vlastní čísla kladná (nezáporná).
- **Proč ne charakteristický polynom:** Abelova–Ruffiniho věta (žádné radikály pro $n\ge5$) + špatná podmíněnost → iterační metody nutné.
- **Mocninná metoda:** $\frac{A^k x}{\|A^k x\|_2} \to q_1$ za předpokladu jednoduchého dominantního $\lambda_1$ a $q_1^T x \neq 0$; rychlost $|\lambda_2/\lambda_1|$; Rayleighův podíl $\to \lambda_1$. Umět odvození přes rozklad do báze vlastních vektorů.
- **QR algoritmus:** $A^{(k)}$ je podobná $A$ (ortogonální transformace $A^{(k)} = (Q^{(k)})^T A^{(k-1)} Q^{(k)}$), tedy stejné spektrum; konverguje k (blokově) trojúhelníkové / diagonální formě (vlastní čísla na diagonále).

### Algoritmy a složitost
- Mocninná metoda: násob $A$ + normuj; iterace $O(n^2)$ (méně pro řídké). Varianty: inverzní, posunutá iterace, deflace.
- QR algoritmus: $A = QR \to RQ$; bez přípravy $O(n^3)$ na iteraci.
- Příprava: oboustranné Householderovy reflexe → Hessenberg (obecně) / třídiagonální (symetrické), zachovává spektrum, zlevní iterace.
