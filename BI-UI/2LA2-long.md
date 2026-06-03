---
tags: [otázka, kurz/LA2, otázka/2, todo]
---

# Skalární součin a norma vektoru

> **Otázka SZZ:** Skalární součin a norma vektoru: definice, vlastnosti a příklady.

Zdroje: BI-LA2 (FIT ČVUT), kap. 5 (Skalární součin), sekce 5.2 (Skalární součin), 5.3 (Příklady skalárních součinů), 5.4 (Norma), 5.5 (Příklady norem); printed str. 93–101.

Značení: $V$ je vektorový prostor nad tělesem $T = \mathbb{R}$ nebo $T = \mathbb{C}$ (skalární součin lze rozumně zavést **jen** nad těmito dvěma tělesy). $\theta$ je nulový vektor; $\overline{z} = a - bi$ je číslo komplexně sdružené k $z = a + bi$; pro reálné $a$ je $\overline{a} = a$. Skalární součin značíme $\langle x \mid y \rangle$, normu $\|x\|$. Dvojici $(V, \langle\,\cdot\mid\cdot\,\rangle)$ značíme $\mathcal{H}$.

---

## 1. Skalární součin — definice a axiomy

**Definice (skalární součin).** Buď $V$ vektorový prostor nad $T = \mathbb{R}$ nebo $\mathbb{C}$. Zobrazení
$$\langle\,\cdot\mid\cdot\,\rangle : V \times V \to T$$
nazýváme (obecný) **[[Skalární-součin|skalární součin]]**, platí-li pro všechny vektory $x, y, z \in V$ a každý skalár $\alpha \in T$ následující axiomy:

1. **Linearita v druhém argumentu:**
$$\langle x \mid y + z \rangle = \langle x \mid y \rangle + \langle x \mid z \rangle \qquad \text{a} \qquad \langle x \mid \alpha y \rangle = \alpha \langle x \mid y \rangle .$$

2. **Hermitovská symetrie** (konjugovaná symetrie):
$$\langle x \mid y \rangle = \overline{\langle y \mid x \rangle} .$$

3. **Pozitivní definitnost:**
$$\langle x \mid x \rangle \ge 0 \qquad \text{a zároveň} \qquad \big( \langle x \mid x \rangle = 0 \iff x = \theta \big).$$

Dvojici $(V, \langle\,\cdot\mid\cdot\,\rangle)$ nazýváme **(vektorovým) prostorem se skalárním součinem**, zkráceně **prehilbertův prostor**, a značíme $\mathcal{H}$.

**Reálný vs. komplexní případ.**
- Pro $T = \mathbb{C}$ je 2. axiom (komplexní sdružení) nezbytný: z 2. axiomu plyne $\langle x \mid x \rangle = \overline{\langle x \mid x \rangle}$, tedy $\langle x \mid x \rangle$ je **reálné číslo**, a teprve pak má smysl nerovnost $\langle x \mid x \rangle \ge 0$ ve 3. axiomu (na $\mathbb{C}$ neexistuje rozumné uspořádání).
- Pro $T = \mathbb{R}$ je sdružení reálného čísla zbytečné ($\overline{a} = a$). Druhý axiom se proto zjednoduší na **běžnou symetrii**:
$$\langle x \mid y \rangle = \langle y \mid x \rangle .$$

**Varování (volba linearity).** Některé materiály požadují linearitu v **první** složce a sdruženou linearitu ve druhé. Zde (dle textbooku BI-LA2) je linearita ve **druhé** složce.

---

## 2. Vlastnosti skalárního součinu

**Pozorování (základní vlastnosti).** Pro libovolné $x, y, z \in \mathcal{H}$ a $\alpha \in T$ platí (dokazuje se přímo z definice):

1. **Sdružená (konjugovaná) linearita v prvním argumentu:**
$$\langle x + y \mid z \rangle = \langle x \mid z \rangle + \langle y \mid z \rangle \qquad \text{a} \qquad \langle \alpha x \mid z \rangle = \overline{\alpha}\,\langle x \mid z \rangle .$$
(Pro $T = \mathbb{R}$ odpadá pruh a dostáváme přímo linearitu i v prvním argumentu.)

2. **Skalární součin s nulovým vektorem je nula:**
$$\langle x \mid \theta \rangle = 0 = \langle \theta \mid x \rangle .$$

**Důkaz bodu 1 (aditivita v 1. argumentu).** Přímým výpočtem:
$$\langle x + y \mid z \rangle \overset{\text{ax.2}}{=} \overline{\langle z \mid x + y \rangle} \overset{\text{ax.1}}{=} \overline{\langle z \mid x \rangle + \langle z \mid y \rangle} = \overline{\langle z \mid x \rangle} + \overline{\langle z \mid y \rangle} \overset{\text{ax.2}}{=} \langle x \mid z \rangle + \langle y \mid z \rangle .$$
Pro homogenitu:
$$\langle \alpha x \mid z \rangle \overset{\text{ax.2}}{=} \overline{\langle z \mid \alpha x \rangle} \overset{\text{ax.1}}{=} \overline{\alpha \langle z \mid x \rangle} = \overline{\alpha}\,\overline{\langle z \mid x \rangle} \overset{\text{ax.2}}{=} \overline{\alpha}\,\langle x \mid z \rangle . \qquad \square$$

**Důkaz bodu 2.** Z aditivity a $\theta = 0 \cdot \theta$:
$$\overline{\langle \theta \mid x \rangle} \overset{\text{ax.2}}{=} \langle x \mid \theta \rangle = \langle x \mid 0\cdot\theta \rangle \overset{\text{ax.1}}{=} 0 \cdot \langle x \mid \theta \rangle = 0 .$$
Odtud $\langle x \mid \theta \rangle = 0$ i $\langle \theta \mid x \rangle = 0$. $\square$

---

## 3. Příklady skalárních součinů

**Standardní (eukleidovský) skalární součin na $T^n$.** Pro $x = (x_1, \dots, x_n)$, $y = (y_1, \dots, y_n) \in T^n$ klademe
$$x \bullet y := \sum_{j=1}^{n} \overline{x_j}\, y_j .$$
Tento součin se nazývá **standardní skalární součin** (na $\mathbb{R}^n$ též eukleidovský). Vektory pak píšeme tučně a značíme $x \bullet y$, abychom jej odlišili od součinu čísel. Pomocí komplexně sdruženého vektoru $\overline{x} = (\overline{x_1}, \dots, \overline{x_n})$ lze psát maticově (ztotožníme-li matici $1\times 1$ s číslem):
$$x \bullet y = \overline{x}^T y, \qquad \text{a na } \mathbb{R}^n \text{ pak } x \bullet y = x^T y .$$

**Frobeniův skalární součin na prostoru matic $T^{m,n}$.** Pro [[Matice|matice]] $A = (a_{ij})$, $B = (b_{ij})$ klademe
$$\langle A \mid B \rangle := \sum_{i=1}^{m} \sum_{j=1}^{n} \overline{a_{ij}}\, b_{ij} .$$
Je to zobecnění standardního součinu na vektorový prostor matic.

**Vážený (nestandardní) součin na $\mathbb{R}^n$.** Skalární součin na $T^n$ nemusí být standardní; např. na $\mathbb{R}^2$ pro $x = (x_1, x_2)$, $y = (y_1, y_2)$:
$$\langle x \mid y \rangle := x^T \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} y = 2 x_1 y_1 + x_1 y_2 + x_2 y_1 + x_2 y_2 .$$
Obecně výraz $x^T A y$ odpovídá skalárnímu součinu na $\mathbb{R}^n$ **právě tehdy, když** matice $A$ je symetrická a pozitivně definitní.

**Integrální skalární součin na prostoru funkcí.** Buď $\mathcal{C}\big(\langle 0,1\rangle\big)$ množina všech reálných spojitých funkcí na intervalu $\langle 0,1\rangle$. Pro $f, g \in \mathcal{C}\big(\langle 0,1\rangle\big)$ definujeme
$$\langle f \mid g \rangle := \int_0^1 f(x)\, g(x)\, dx .$$
Tento součin je klíčový např. ve Fourierově analýze a při řešení diferenciálních rovnic.

---

## 4. Norma — definice a axiomy

**Definice (norma).** Buď $V$ vektorový prostor nad $T = \mathbb{R}$ nebo $\mathbb{C}$. Zobrazení
$$\|\cdot\| : V \to \mathbb{R}$$
nazýváme **[[Norma|norma]]**, pokud pro libovolné $x, y \in V$ a $\alpha \in T$ platí:

1. **Nezápornost:** $\|x\| \ge 0$.
2. **Definitnost** (jen nulový vektor má nulovou normu): $\|x\| = 0 \iff x = \theta$.
3. **Homogenita v absolutní hodnotě:** $\|\alpha x\| = |\alpha| \cdot \|x\|$.
4. **Trojúhelníková nerovnost:** $\|x + y\| \le \|x\| + \|y\|$.

Číslo $\|x\|$ nazýváme **velikostí vektoru** $x$. Číslo $d(x,y) := \|x - y\|$ nazýváme **vzdáleností** vektorů $x$ a $y$. Trojúhelníková nerovnost odpovídá pravidlu, že cesta z bodu $A$ do bodu $C$ přes bod $B$ nemůže být kratší než přímá cesta z $A$ do $C$.

---

## 5. Norma indukovaná skalárním součinem

**Definice (norma indukovaná skalárním součinem).** V prehilbertově prostoru $\mathcal{H}$ se skalárním součinem $\langle\,\cdot\mid\cdot\,\rangle$ definujeme zobrazení $\|\cdot\| : \mathcal{H} \to \mathbb{R}$ předpisem
$$\boxed{\ \|x\| := \sqrt{\langle x \mid x \rangle}\ } .$$
Toto zobrazení nazýváme **normou indukovanou skalárním součinem**.

**Věta (o korektnosti indukované normy).** Zobrazení $\|x\| = \sqrt{\langle x \mid x \rangle}$ je skutečně norma (splňuje axiomy 1–4 z Definice normy).

**Důkaz axiomů 1–3.**
- *Korektnost a 1. axiom.* Dle 3. axiomu skalárního součinu je $\langle x \mid x \rangle \ge 0$ pro každé $x$, takže odmocnina je korektně definovaná a $\|x\| \ge 0$.
- *2. axiom.* Z 3. axiomu skalárního součinu: $\|x\| = 0 \iff \sqrt{\langle x \mid x \rangle} = 0 \iff \langle x \mid x \rangle = 0 \iff x = \theta$.
- *3. axiom.* Z homogenity skalárního součinu (1. axiom def. a 1. bod Pozorování) a z toho, že $|\alpha|^2 = \alpha\overline{\alpha}$:
$$\|\alpha x\| = \sqrt{\langle \alpha x \mid \alpha x \rangle} = \sqrt{\alpha\overline{\alpha}\,\langle x \mid x \rangle} = \sqrt{|\alpha|^2 \langle x \mid x \rangle} = |\alpha|\sqrt{\langle x \mid x \rangle} = |\alpha|\,\|x\| .$$

Splnění 4. axiomu (trojúhelníkové nerovnosti) je důsledkem Schwarzovy nerovnosti — viz sekce 7. $\square$

---

## 6. Příklady norem

**Eukleidovská norma.** Norma indukovaná standardním skalárním součinem se nazývá **eukleidovská norma**. Pro $x = (x_1, \dots, x_n) \in T^n$:
$$\|x\| = \sqrt{\overline{x_1} x_1 + \cdots + \overline{x_n} x_n} = \sqrt{|x_1|^2 + \cdots + |x_n|^2} .$$
Tuto normu lze zahrnout do škály tzv. $p$-norem.

**$p$-norma.** Na $T^n$ definujeme pro $p \in \langle 1, \infty \rangle$ tzv. **$p$-normu** předpisem: pro $x = (x_1, \dots, x_n)$
$$\|x\|_p = \begin{cases} \big( |x_1|^p + \cdots + |x_n|^p \big)^{\frac{1}{p}} & \text{pro } p < \infty , \\[1mm] \max\{ |x_1|, \dots, |x_n| \} & \text{pro } p = \infty . \end{cases}$$
Dá se ukázat, že $p$-norma je skutečně norma. Speciální případy:

| norma | předpis | geometrický význam |
|---|---|---|
| **1-norma** (manhattanská, součtová) | $\|x\|_1 = \sum_{j=1}^n \lvert x_j\rvert$ | součet absolutních hodnot složek; délka cesty po mřížce |
| **2-norma** (eukleidovská) | $\|x\|_2 = \big(\sum_{j=1}^n \lvert x_j\rvert^2\big)^{1/2}$ | přímá vzdálenost z počátku do $x$; norma indukovaná standardním součinem |
| **$\infty$-norma** (maximová) | $\|x\|_\infty = \max_j \lvert x_j\rvert$ | největší složka (v absolutní hodnotě) |

Pro $x = (5,4)$ je např. $\|x\|_1 = 9$. Množiny vektorů s velikostí $1$ tvoří v $\mathbb{R}^2$: kosočtverec (pro 1-normu), kružnici (2-norma), čtverec (∞-norma).

---

## 7. Cauchyho–Schwarzova a trojúhelníková nerovnost

**Věta (Schwarzova / Cauchyho–Schwarzova nerovnost).** Pro každé $x, y \in \mathcal{H}$ platí
$$\boxed{\ \big| \langle x \mid y \rangle \big| \le \|x\| \cdot \|y\|\ } \tag{5.24}$$
kde $\|\cdot\|$ je norma indukovaná skalárním součinem.

*(Pozn.: textbook ji označuje jako Schwarzovu nerovnost; po jejích objevitelích se obecně nazývá Cauchyho–Schwarzova, příp. Cauchyho–Bunjakovského–Schwarzova.)*

**Důkaz.** Pro $y = \theta$ platí rovnost ve tvaru $0 = 0$ (oba členy nulové). Uvažujme tedy $y \neq \theta$. Z linearity skalárního součinu nejdříve rozepíšeme normu součtu vektorů: pro libovolné $x, y \in \mathcal{H}$
$$\langle x + y \mid x + y \rangle = \langle x \mid x \rangle + \langle x \mid y \rangle + \langle y \mid x \rangle + \langle y \mid y \rangle = \|x\|^2 + 2\,\mathrm{Re}\langle x \mid y \rangle + \|y\|^2 . \tag{5.27}$$
Položme
$$\lambda := \frac{\langle y \mid x \rangle}{\|y\|^2}$$
a aplikujme vztah analogický (5.27) na vektory $x$ a $-\lambda y$. Z 3. axiomu (pozitivní definitnost) je $\langle x - \lambda y \mid x - \lambda y \rangle \ge 0$, tedy
$$0 \le \langle x - \lambda y \mid x - \lambda y \rangle = \|x\|^2 + |\lambda|^2 \|y\|^2 - 2\,\mathrm{Re}\big( \lambda \cdot \langle x \mid y \rangle \big) . \tag{5.29}$$
Dosazením zvoleného $\lambda$ a využitím $\langle x \mid y \rangle = \overline{\langle y \mid x \rangle}$ (tedy $|\langle y \mid x \rangle| = |\langle x \mid y \rangle|$ a $\langle y \mid x \rangle \langle x \mid y \rangle = |\langle x \mid y \rangle|^2$) se pravá strana zjednoduší na
$$\|x\|^2 - \frac{|\langle x \mid y \rangle|^2}{\|y\|^2} \ \ge 0 .$$
Odtud $|\langle x \mid y \rangle|^2 \le \|x\|^2 \|y\|^2$ a po odmocnění $|\langle x \mid y \rangle| \le \|x\|\,\|y\|$. $\square$

**Pozorování (rovnost v Schwarzově nerovnosti).** Rovnost $|\langle x \mid y \rangle| = \|x\|\,\|y\|$ nastává **právě tehdy, když je soubor $(x, y)$ lineárně závislý.**

*Důkaz (idea).* „$\Rightarrow$": Pro $y = \theta$ triviální. Pro $y \neq \theta$ z předchozího výpočtu při rovnosti vyjde $\langle x - \lambda y \mid x - \lambda y \rangle = 0$, odkud z pozitivní definitnosti $x - \lambda y = \theta$, tedy $(x,y)$ je LZ. „$\Leftarrow$": Je-li $(x,y)$ LZ, pak $x = \alpha y$ (či naopak), a dosazením vyjde $|\langle x \mid y \rangle| = |\alpha|\,\|y\|^2 = \|x\|\,\|y\|$. $\square$

**Věta (trojúhelníková nerovnost).** Pro každé $x, y \in \mathcal{H}$ a indukovanou normu platí
$$\|x + y\| \le \|x\| + \|y\| .$$

**Důkaz.** Pro libovolné komplexní číslo $z$ platí $\mathrm{Re}\, z \le |z|$. Z toho a Schwarzovy nerovnosti
$$\mathrm{Re}\langle x \mid y \rangle \le |\langle x \mid y \rangle| \le \|x\|\,\|y\| .$$
Dosazením do (5.27):
$$\|x + y\|^2 = \langle x + y \mid x + y \rangle = \|x\|^2 + 2\,\mathrm{Re}\langle x \mid y \rangle + \|y\|^2 \le \|x\|^2 + 2\|x\|\|y\| + \|y\|^2 = \big(\|x\| + \|y\|\big)^2 .$$
Po odmocnění obou (nezáporných) stran dostáváme $\|x + y\| \le \|x\| + \|y\|$. $\square$

**Důsledek (odhad skalárního součinu).** Schwarzova nerovnost říká, že skalární součin dvou vektorů může být v absolutní hodnotě nejvýše roven součinu jejich velikostí.

---

## Co je potřeba na zkoušku znát

### Definice
- **Skalární součin** $\langle\,\cdot\mid\cdot\,\rangle : V \times V \to T$ ($T = \mathbb{R}$ nebo $\mathbb{C}$): 3 axiomy — linearita ve 2. argumentu, hermitovská symetrie $\langle x\mid y\rangle = \overline{\langle y\mid x\rangle}$ (na $\mathbb{R}$ jen symetrie), pozitivní definitnost.
- Prehilbertův prostor $\mathcal{H} = (V, \langle\,\cdot\mid\cdot\,\rangle)$.
- **Norma** $\|\cdot\| : V \to \mathbb{R}$: 4 axiomy — nezápornost, definitnost, homogenita $\|\alpha x\| = |\alpha|\|x\|$, trojúhelníková nerovnost.
- **Norma indukovaná skalárním součinem** $\|x\| = \sqrt{\langle x\mid x\rangle}$.
- Standardní (eukleidovský) součin $x\bullet y = \sum \overline{x_j} y_j$; eukleidovská norma; $p$-normy (1-, 2-, ∞-).

### Věty s důkazy
- **Konjugovaná linearita v 1. argumentu** a $\langle x\mid\theta\rangle = 0$ (přímý výpočet z axiomů).
- **Korektnost indukované normy** (axiomy 1–3 plynou z axiomů skalárního součinu).
- **Schwarzova (Cauchyho–Schwarzova) nerovnost** $|\langle x\mid y\rangle| \le \|x\|\|y\|$ — důkaz volbou $\lambda = \langle y\mid x\rangle/\|y\|^2$ a pozitivní definitností; rovnost $\iff (x,y)$ LZ.
- **Trojúhelníková nerovnost** $\|x+y\| \le \|x\| + \|y\|$ — z rozpisu $\|x+y\|^2$ a Schwarzovy nerovnosti.
