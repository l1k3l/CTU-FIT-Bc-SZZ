---
tags: [otázka, kurz/DML, otázka/8, todo]
---

# Základy teorie čísel

> **Otázka SZZ:** Základy teorie čísel: dělitelnost, REA a diofantické rovnice, prvočísla, modulární aritmetika, Malá Fermatova a Eulerova věta, lineární kongruence, Čínská věta o zbytcích.

Zdroje: BI-DML, kapitola 6 (Základy teorie čísel), Bohdal a kol., FIT ČVUT.

---

## 1. Dělitelnost

### 1.1 Definice

**Definice ([[Dělitelnost]]):** Buďte $a, b \in \mathbb{Z}$. Říkáme, že $a$ **dělí** $b$, značíme $a \mid b$, jestliže existuje $k \in \mathbb{Z}$ takové, že $a \cdot k = b$. Mluvíme o $a$ jako o **děliteli** $b$ a $b$ jako o **násobku** $a$. Pokud $a$ nedělí $b$, píšeme $a \nmid b$.

### 1.2 Vlastnosti dělitelnosti

**Tvrzení:** Pro všechna $a, b, c \in \mathbb{Z}$ platí:
1. $1 \mid n$ a $n \mid 0$ pro každé $n \in \mathbb{Z}$.
2. $a \mid b \iff |a| \mid |b|$.
3. Pokud $a \mid b$ a $b \neq 0$, pak $|a| \leq |b|$.
4. Pokud $a \mid b$ a $a \mid c$, pak $a \mid (b + c)$.
5. Pokud $a \mid b$, pak $a \mid nb$ pro všechna $n \in \mathbb{Z}$.
6. **Lineární kombinace:** $a \mid b \land a \mid c \iff a \mid (mb + nc)$ pro všechna $m, n \in \mathbb{Z}$.

**Důkaz bodu 6** ($\Rightarrow$): Z $b = ka$, $c = \ell a$ plyne $mb + nc = (mk + n\ell)a$, tedy $a \mid (mb + nc)$. ($\Leftarrow$): volbou $(m,n) = (1,0)$ a $(0,1)$.

### 1.3 Dělení se zbytkem

**Věta (O dělení se zbytkem):** Nechť $a \in \mathbb{Z}$, $d \in \mathbb{N}$. Pak existují **jednoznačně určená** $q, r \in \mathbb{Z}$ taková, že
$$a = qd + r \quad \land \quad 0 \leq r < d.$$

**Důkaz (idea):** Existence indukcí podle $|a|$ (pro $a \geq 0$ standardní indukční krok; pro $a < 0$ převod přes $|a|$). Jednoznačnost: kdyby $q_1 d + r_1 = q_2 d + r_2$, pak $(q_1 - q_2)d = r_2 - r_1$ s $|r_2 - r_1| < d$ ⇒ $r_1 = r_2$, $q_1 = q_2$.

**Definice:** $q$ je **celočíselný podíl**, $r = a \bmod d$ je **zbytek po dělení**.

### 1.4 GCD a LCM

**Definice (gcd, lcm, nesoudělnost):** Pro $a, b \in \mathbb{Z}$:
- **Společný dělitel** $n \in \mathbb{N}_0$: $n \mid a \land n \mid b$.
- **Největší společný dělitel** $\gcd(a, b)$ = společný dělitel, který je navíc násobkem každého dalšího společného dělitele:
$$n \mid a \land n \mid b \land \big(\forall d \in \mathbb{N}_0 : (d \mid a \land d \mid b) \Rightarrow d \mid n\big).$$
- $a, b$ jsou **nesoudělná**, je-li $\gcd(a, b) = 1$.
- **Nejmenší společný násobek** $\operatorname{lcm}(a, b)$ analogicky duálně.

**Mezní hodnoty:** $\gcd(a, 0) = a$ pro $a \neq 0$, $\gcd(0,0) = 0$, $\operatorname{lcm}(a, 0) = 0$.

---

## 2. [[Eukleidův-algoritmus|Eukleidův algoritmus]] a Bézoutova rovnost

### 2.1 Lemma — invariant pro EA

**Lemma (Příprava pro EA):** Pro $a, b, c \in \mathbb{Z}$:
1. $\gcd(a, b) = \gcd(b, a) = \gcd(|a|, |b|)$.
2. $\gcd(a + cb, b) = \gcd(a, b)$ pro libovolné $c \in \mathbb{Z}$.

**Důkaz bodu 2:** Pokud $e \mid a \land e \mid b$, pak $e \mid (a + cb)$. Obráceně, pokud $e \mid (a + cb) \land e \mid b$, pak $e \mid (a + cb - cb) = a$. Společní dělitelé jsou stejné množiny ⇒ stejné gcd.

### 2.2 Eukleidův algoritmus

**Věta (EA):** Pro $a \geq b > 0$ definujeme rekurentně $r_1 = a$, $r_2 = b$, $r_n = r_{n-2} \bmod r_{n-1}$ pro $n \geq 3$. Posloupnost $(r_n)$ je striktně klesající a nezáporná ⇒ existuje nejmenší $k$ s $r_{k+1} = 0$, a pak $r_k = \gcd(a, b)$.

**Důkaz korektnosti:** Opakovanou aplikací lemmatu výše:
$$\gcd(a, b) = \gcd(r_1, r_2) = \gcd(r_2, r_3) = \dots = \gcd(r_k, 0) = r_k.$$

### 2.3 Bézoutova rovnost

**Věta (Bézoutova rovnost):** Pro každá $a, b \in \mathbb{Z}$ existují $m, n \in \mathbb{Z}$ taková, že
$$\gcd(a, b) = m \cdot a + n \cdot b.$$
Dvojici $(m, n)$ nazýváme **Bézoutovy koeficienty** (nejsou jednoznačné).

**Síla tvrzení:** $\gcd(a, b)$ je dokonce **nejmenší kladné** celé číslo vyjádřitelné jako $ma + nb$ s $m, n \in \mathbb{Z}$.

**Důkaz minimality:** Pokud $d = m_0 a + n_0 b > 0$, pak $\gcd(a, b) \mid a \land \gcd(a, b) \mid b \Rightarrow \gcd(a, b) \mid d$, tedy $\gcd(a, b) \leq d$.

### 2.4 Rozšířený Eukleidův algoritmus (REA / EEA)

**Věta (REA):** REA udržuje vedle $r_n$ ještě koeficienty $\alpha_n, \beta_n$ splňující $r_n = \alpha_n a + \beta_n b$:

$$\alpha_1 = 1,\ \beta_1 = 0,\quad \alpha_2 = 0,\ \beta_2 = 1,$$
$$q_{n-1} = \left\lfloor \frac{r_{n-2}}{r_{n-1}} \right\rfloor,$$
$$r_n = r_{n-2} - q_{n-1} r_{n-1},$$
$$\alpha_n = \alpha_{n-2} - q_{n-1} \alpha_{n-1},\quad \beta_n = \beta_{n-2} - q_{n-1} \beta_{n-1}.$$

V kroku $k$, kdy $r_k = \gcd(a, b)$, máme $\gcd(a, b) = \alpha_k \cdot a + \beta_k \cdot b$.

**Důkaz** silnou indukcí podle $n$. ZK: $r_1 = 1 \cdot a + 0 \cdot b$, $r_2 = 0 \cdot a + 1 \cdot b$. IK:
$$r_n = r_{n-2} - q_{n-1} r_{n-1} = (\alpha_{n-2} - q_{n-1}\alpha_{n-1})a + (\beta_{n-2} - q_{n-1}\beta_{n-1})b.$$

**Zápis tabulkou** (sloupce $r_i, \alpha_i, \beta_i, q_i$). Příklad pro $\gcd(254, 158)$:

| $r_i$ | $\alpha_i$ | $\beta_i$ | $q_i$ |
|---:|---:|---:|---:|
| 254 | 1 | 0 | — |
| 158 | 0 | 1 | 1 |
| 96 | 1 | $-1$ | 1 |
| 62 | $-1$ | 2 | 1 |
| 34 | 2 | $-3$ | 1 |
| 28 | $-3$ | 5 | 1 |
| 6 | 5 | $-8$ | 4 |
| 4 | $-23$ | 37 | 1 |
| **2** | **28** | **$-45$** | 2 |
| 0 |  |  |  |

Výsledek: $\gcd(254, 158) = 2 = 28 \cdot 254 + (-45) \cdot 158$.

### 2.5 Lineární diofantické rovnice

**Definice (LDR):** **Lineární diofantická rovnice** o dvou neznámých je rovnice
$$ax + by = c, \quad a, b, c \in \mathbb{Z},$$
jejíž řešení hledáme v $\mathbb{Z}^2$.

**Věta (Řešitelnost LDR):** LDR $ax + by = c$ má řešení **právě tehdy, když $\gcd(a, b) \mid c$**.

**Důkaz.** ($\Rightarrow$): Pokud $ax + by = c$, pak $\gcd(a, b) \mid (ax + by) = c$. ($\Leftarrow$): Z Bézoutovy rovnosti $\gcd(a, b) = \alpha a + \beta b$ a $c = k \cdot \gcd(a, b)$ získáme řešení $x = k\alpha$, $y = k\beta$.

**Postup nalezení řešení:**
1. Pomocí REA spočti $\gcd(a, b)$ a Bézoutovy koeficienty $\alpha, \beta$.
2. Pokud $\gcd(a, b) \nmid c$, řešení neexistuje.
3. Jinak partikulární řešení: $x_0 = \alpha \cdot \frac{c}{\gcd(a, b)}$, $y_0 = \beta \cdot \frac{c}{\gcd(a, b)}$.

**Věta (Všechna řešení LDR):** Pokud $(x_0, y_0)$ řeší $ax + by = c$ (a $a, b \neq 0$), pak množina všech řešení je
$$\left\{ \left(x_0 + \frac{b}{\gcd(a, b)} k,\ y_0 - \frac{a}{\gcd(a, b)} k\right) \ \middle|\ k \in \mathbb{Z} \right\}.$$

**Důkaz (idea):** Z $ax + by = ax_0 + by_0$ plyne $\frac{a}{d}(x - x_0) = \frac{b}{d}(y_0 - y)$, kde $d = \gcd(a, b)$. Lemma 6.2 dává $\gcd(a/d, b/d) = 1$, takže $\frac{a}{d} \mid (y_0 - y)$ a $\frac{b}{d} \mid (x - x_0)$, čímž dostaneme předpis.

**Pohled lineární algebry:** Obecné řešení = partikulární řešení + řešení přidružené homogenní LDR $ax + by = 0$, jejíž všechna řešení jsou $k \cdot (b/d, -a/d)$.

---

## 3. Prvočísla

### 3.1 Definice

**Definice:** Přirozená čísla $\mathbb{N}$ se dělí na:
1. Číslo $1$ (jediný dělitel = sebe).
2. **[[Prvočíslo|Prvočísla]]** — přesně dva dělitele ($1$ a $p$).
3. **Složená čísla** — více než dva dělitele.

### 3.2 Nekonečnost prvočísel

**Věta (Eukleides):** Existuje nekonečně mnoho prvočísel.

**Důkaz sporem.** Předpokládejme $p_1, \dots, p_k$ jsou všechna prvočísla. Vezměme $P = p_1 p_2 \cdots p_k + 1$. Pak $P > 1$:
- Pokud je $P$ prvočíslo, spor (není v seznamu).
- Pokud je $P$ složené, dělí ho nějaké $p_j$. Ale pak $p_j \mid (P - p_1 \cdots p_k) = 1$, což je spor.

### 3.3 Eukleidovo lemma a základní věta aritmetiky

**Lemma (Eukleidovo):** Buď $p$ prvočíslo.
1. Pokud $p \mid (ab)$ a $p \nmid a$, pak $p \mid b$.
2. Pokud $p \mid (a_1 a_2 \cdots a_k)$, pak existuje $j$ takové, že $p \mid a_j$.

**Důkaz bodu 1:** Pokud $p \nmid a$, pak (jelikož $p$ je prvočíslo) $\gcd(a, p) = 1$. Z Lemmatu o LDR (pokud $a \mid bc \land \gcd(a, b) = 1$, pak $a \mid c$) plyne $p \mid b$. Bod 2 indukcí podle $k$.

**Věta (Základní věta aritmetiky):** Každé $n \in \mathbb{N}$, $n \geq 2$, lze **jednoznačně** vyjádřit ve tvaru
$$n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k} = \prod_{i=1}^{k} p_i^{\alpha_i},$$
kde $p_1 < p_2 < \dots < p_k$ jsou prvočísla a $\alpha_i \in \mathbb{N}$. Tento zápis = **kanonický (prvočíselný) rozklad** $n$.

**Důkaz (idea):** Existence indukcí (každé složené $n$ lze rozdělit na $n = ab$ s $a, b < n$, pak rekurze). Jednoznačnost sporem — nejmenší protipříklad $n = p_1 \cdots p_k = q_1 \cdots q_\ell$, pak $p_1 \mid q_1 \cdots q_\ell$ ⇒ (Eukl. lemma) $p_1 = q_i$ pro nějaké $i$, zkrátíme, dostaneme menší protipříklad — spor.

### 3.4 Vztah gcd a lcm

**Pozorování:** Pro $a = \prod p_i^{\alpha_i}$, $b = \prod p_i^{\beta_i}$ (společný seznam prvočísel) platí
$$\gcd(a, b) = \prod p_i^{\min(\alpha_i, \beta_i)}, \quad \operatorname{lcm}(a, b) = \prod p_i^{\max(\alpha_i, \beta_i)}.$$

**Tvrzení:** $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |a| \cdot |b|$.

**Důkaz:** Použijeme $\min + \max = \alpha + \beta$ pro každé prvočíslo z rozkladu. Důsledek: $\operatorname{lcm}(a, b) = \frac{|a| \cdot |b|}{\gcd(a, b)}$ — lze počítat bez faktorizace, rychle přes EA.

---

## 4. Modulární aritmetika

### 4.1 Kongruence modulo $m$

**Definice ([[Kongruence]]):** Pro $a, b \in \mathbb{Z}$, $m \in \mathbb{N}$ ($m \geq 2$) říkáme, že $a$ je **kongruentní s $b$ modulo $m$**, značíme $a \equiv b \pmod m$, právě když $m \mid (a - b)$.

**Tvrzení (Ekvivalentní vyjádření):** Následující jsou ekvivalentní:
1. $a \equiv b \pmod m$.
2. $\exists k \in \mathbb{Z}:\ a = b + km$.
3. $a \bmod m = b \bmod m$ (stejné zbytky po dělení).

**Vlastnosti $\equiv$:** Reflexivní, symetrická, tranzitivní ⇒ relace ekvivalence.

### 4.2 Zachovávání operací

**Tvrzení:** Nechť $a \equiv b \pmod m$ a $c \equiv d \pmod m$. Pak:
1. $a + c \equiv b + d \pmod m$.
2. $a - c \equiv b - d \pmod m$.
3. $a c \equiv b d \pmod m$.
4. $a^k \equiv b^k \pmod m$ pro $k \in \mathbb{N}$.

**Důkaz bodu 3:** Z $a = b + km$, $c = d + \ell m$:
$$ac = (b + km)(d + \ell m) = bd + \underbrace{(b\ell + dk)m + k\ell m^2}_{\text{násobek } m} \equiv bd \pmod m.$$

### 4.3 Množina $\mathbb{Z}_m$

**Definice:** $\mathbb{Z}_m := \{0, 1, \dots, m-1\}$. Definujeme operace
$$a +_m b := (a + b) \bmod m, \qquad a \cdot_m b := (a \cdot b) \bmod m.$$

**Věta (Algebraické vlastnosti $\mathbb{Z}_m$):** $(\mathbb{Z}_m, +_m, \cdot_m)$ splňuje uzavřenost, komutativitu, asociativitu, distributivitu, existenci neutrálních prvků ($0, 1$) a existenci **aditivního** inverzního prvku pro každý prvek (pro $a \neq 0$ je to $m - a$).

### 4.4 Multiplikativní inverze

**Definice:** $x \in \mathbb{Z}_m$ je **multiplikativní inverzí** $a$, značíme $a^{-1}$, právě když $a \cdot_m x = 1$.

**Věta (O existenci):** $a \in \mathbb{Z}_m$ má multiplikativní inverzi **právě tehdy, když $\gcd(a, m) = 1$**. Pokud existuje, je jediná.

**Důkaz:** Existence inverze $\iff$ řešitelnost $ax \equiv 1 \pmod m$ $\iff$ řešitelnost LDR $ax + my = 1$ $\iff$ $\gcd(a, m) \mid 1 \iff \gcd(a, m) = 1$.

**Inverze se počítá REA** aplikovaným na $ax + my = 1$.

**Důsledek:** Pokud $m$ je prvočíslo, **každý nenulový prvek** $\mathbb{Z}_m$ má inverzi ⇒ $(\mathbb{Z}_m, +_m, \cdot_m)$ je **konečné těleso** (jako v BI-LA1).

---

## 5. Malá Fermatova a Eulerova věta

### 5.1 Krácení v modulu

**Věta (O krácení):** Pro $a, b, c \in \mathbb{Z}$, $m \geq 2$, $d = \gcd(m, c)$:
$$ac \equiv bc \pmod m \iff a \equiv b \pmod{m/d}.$$

Speciálně **lze krátit** beze změny modula, právě když $\gcd(m, c) = 1$.

**Důkaz (idea):** $ac \equiv bc \pmod m$ je $m \mid c(a - b)$. Po dělení obou stran $d = \gcd(m, c)$ dostaneme $(m/d) \mid (c/d)(a - b)$, a jelikož $\gcd(m/d, c/d) = 1$, plyne $(m/d) \mid (a - b)$.

### 5.2 Malá Fermatova věta

**Věta (**[[Malá-Fermatova-věta|Malá Fermatova]]**, MFV):** Buď $p$ prvočíslo a $a \in \mathbb{N}$ není násobkem $p$ (tj. $\gcd(a, p) = 1$). Pak
$$a^{p-1} \equiv 1 \pmod p.$$

**Důkaz.** Uvažme čísla $a, 2a, 3a, \dots, (p-1)a$.
- Žádné z nich není dělitelné $p$ (jelikož $p \nmid a$ a $p \nmid j$ pro $j < p$).
- Žádná dvě nejsou kongruentní modulo $p$: kdyby $ja \equiv ka \pmod p$ s $j < k < p$, pak (z krácení, $\gcd(a, p) = 1$) $j \equiv k \pmod p$ — spor s $j < k < p$.
- Tedy zbytky $\{a, 2a, \dots, (p-1)a\} \pmod p$ tvoří permutaci $\{1, 2, \dots, p-1\}$.

Z toho:
$$a \cdot 2a \cdots (p-1)a \equiv 1 \cdot 2 \cdots (p-1) \pmod p,$$
$$a^{p-1} (p-1)! \equiv (p-1)! \pmod p,$$
$$a^{p-1} \equiv 1 \pmod p \quad (\text{zkrácení, } \gcd((p-1)!, p) = 1).$$

**Důsledek (Inverze pomocí MFV):** Pokud $p$ je prvočíslo a $a \in \mathbb{Z}_p \setminus \{0\}$, pak $a^{p-2}$ je multiplikativní inverzí $a$ modulo $p$, protože $a \cdot a^{p-2} = a^{p-1} \equiv 1$.

### 5.3 Eulerova funkce

**Definice ([[Eulerova-funkce|Eulerova funkce $\varphi$]]):**
$$\varphi(n) := \big|\{k \in \mathbb{N} : k \leq n \land \gcd(k, n) = 1\}\big|.$$
Tedy počet přirozených čísel $\leq n$ nesoudělných s $n$.

**Hodnoty:** $\varphi(1)=1$, $\varphi(2)=1$, $\varphi(3)=2$, $\varphi(4)=2$, $\varphi(5)=4$, $\varphi(6)=2$, $\varphi(7)=6$, $\varphi(8)=4$, $\varphi(9)=6$, $\varphi(10)=4$.

**Tvrzení (Na prvočíslech):** $p$ je prvočíslo $\iff \varphi(p) = p - 1$.

**Tvrzení (Na mocninách prvočísel):** Pro prvočíslo $p$ a $\alpha \in \mathbb{N}$:
$$\varphi(p^\alpha) = p^\alpha - p^{\alpha-1}.$$

**Důkaz:** Soudělná s $p^\alpha$ jsou právě násobky $p$. Mezi čísly $1, \dots, p^\alpha$ je jich $p^{\alpha-1}$ ⇒ nesoudělných je $p^\alpha - p^{\alpha-1}$.

**Tvrzení (Multiplikativita $\varphi$):** Je-li $\gcd(m, n) = 1$, pak $\varphi(mn) = \varphi(m) \varphi(n)$.

**Věta (Výpočet $\varphi$ z faktorizace):** Pro $m = p_1^{\alpha_1} \cdots p_k^{\alpha_k}$:
$$\varphi(m) = m \left(1 - \frac{1}{p_1}\right) \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right).$$

**Příklad:** $\varphi(100) = \varphi(2^2 \cdot 5^2) = 100 \cdot \frac{1}{2} \cdot \frac{4}{5} = 40$.

### 5.4 Eulerova věta

**Věta (Eulerova, EV):** Nechť $m \in \mathbb{N}$, $m \geq 2$, a $a$ je nesoudělné s $m$. Pak
$$a^{\varphi(m)} \equiv 1 \pmod m.$$

**Vztah:** Eulerova věta je **zobecněním** MFV — pro prvočíselné $m$ máme $\varphi(m) = m - 1$ a obě věty říkají totéž.

**Důsledek (Inverze pomocí EV):** Pokud $\gcd(a, m) = 1$, pak $a^{\varphi(m) - 1}$ je multiplikativní inverzí $a$ modulo $m$.

**Příklad:** $2^{268} \bmod 9$. Máme $\gcd(9, 2) = 1$, $\varphi(9) = 6$, $268 = 44 \cdot 6 + 4$:
$$2^{268} = (2^6)^{44} \cdot 2^4 \equiv 1 \cdot 16 \equiv 7 \pmod 9.$$

### 5.5 Binární mocnění (square & multiply)

Pro výpočet $b^N \bmod m$, když nelze použít MFV/EV (např. $\gcd(b, m) \neq 1$):
1. Vyjádři $N$ binárně: $N = (a_k a_{k-1} \dots a_0)_2$.
2. Spočti zbytky $b, b^2, b^4, \dots, b^{2^k}$ modulo $m$ postupným umocňováním.
3. Vynásob ty $b^{2^j}$, kde $a_j = 1$, v každém kroku redukuj modulo $m$.

Složitost $O(\log N)$ multiplikací.

---

## 6. Lineární kongruence

### 6.1 Jednoduchá lineární kongruence

**Definice:** **Lineární kongruence** je úloha najít všechna $x \in \mathbb{Z}$ splňující
$$ax \equiv b \pmod m, \quad a, b, m \in \mathbb{Z},\ m \geq 2.$$

**Věta (Řešení lineární kongruence):** $ax \equiv b \pmod m$ má řešení **právě tehdy, když $\gcd(a, m) \mid b$**.

Pokud $(x_0, y_0)$ je řešením přidružené LDR $ax + my = b$, pak všechna řešení v $\mathbb{Z}$ jsou
$$x \equiv x_0 + k \cdot \frac{m}{\gcd(a, m)} \pmod m, \quad k \in \mathbb{Z}.$$

**Důkaz:** $ax \equiv b \pmod m$ $\iff$ $\exists y: ax + my = b$, což je LDR. Aplikujeme předchozí věty o LDR a vezmeme jen složku $x$.

**Věta (Počet řešení v $\mathbb{Z}_m$):** Pokud $\gcd(a, m) \mid b$, pak v $\mathbb{Z}_m$ existuje právě $\gcd(a, m)$ různých řešení; množina:
$$\left\{ \left(x_0 + k \cdot \frac{m}{\gcd(a, m)}\right) \bmod m \ \middle|\ k = 0, 1, \dots, \gcd(a, m) - 1 \right\}.$$

### 6.2 Přes multiplikativní inverzi

Pokud $\gcd(a, m) = 1$, má $a$ inverzi $a^{-1} \bmod m$ a kongruence se řeší jako
$$ax \equiv b \pmod m \iff x \equiv a^{-1} b \pmod m,$$
což je analogie pravidla $x = b/a$ pro lineární rovnice. (Pro prvočíselné $m$ jde dokonce o rovnici v tělese $\mathbb{Z}_m$.)

### 6.3 Příklad

**Vyřeš $9x \equiv 12 \pmod{15}$.**

$\gcd(9, 15) = 3$, $3 \mid 12$ ⇒ řešení existuje, $3$ řešení v $\mathbb{Z}_{15}$. REA dá $9 \cdot 2 + 15 \cdot (-1) = 3$, vynásobíme $4$: $9 \cdot 8 + 15 \cdot (-4) = 12$. Tedy $x_0 = 8$, všechna:
$$x \equiv 8 + 5k \pmod{15}, \quad k = 0, 1, 2 \Rightarrow x \in \{3, 8, 13\}.$$

---

## 7. Čínská věta o zbytcích

### 7.1 Soustavy lineárních kongruencí

Mějme soustavu
$$x \equiv a_1 \pmod{m_1},\ \dots,\ x \equiv a_N \pmod{m_N}.$$

### 7.2 ČVOZ — moduly po dvou nesoudělné

**Věta (Čínská věta o zbytcích, ČVOZ / CRT):** Nechť $m_1, \dots, m_N \geq 2$ jsou **po dvou nesoudělné** ($\gcd(m_i, m_j) = 1$ pro $i \neq j$). Pak soustava má řešení a je **jednoznačně určeno modulo $M = \prod_i m_i$**.

**Konstruktivní důkaz a algoritmus řešení:**
1. Pro každé $i$ polož $M_i = M / m_i$ (součin všech kromě $m_i$).
2. $\gcd(M_i, m_i) = 1$ (jelikož všechna $m_j$ pro $j \neq i$ jsou nesoudělná s $m_i$) ⇒ existuje $X_i$ řešící $M_i X_i \equiv 1 \pmod{m_i}$ (najdeme REA).
3. Pak řešení je
$$x \equiv \sum_{i=1}^{N} a_i M_i X_i \pmod M.$$

**Ověření:** Pro libovolné $j$: v součtu má pouze sčítanec $a_j M_j X_j$ nenulový zbytek modulo $m_j$ (neboť pro $i \neq j$ je $m_j \mid M_i$ ⇒ $M_i X_i \equiv 0 \pmod{m_j}$). Tedy $x \equiv a_j M_j X_j \equiv a_j \pmod{m_j}$.

**Jednoznačnost modulo $M$:** Pokud $x, y$ obě řeší, pak $m_j \mid (x - y)$ pro každé $j$, takže $M = \prod m_j \mid (x - y)$ (díky nesoudělnosti) ⇒ $x \equiv y \pmod M$.

### 7.3 Příklad

**Vyřeš:** $x \equiv 1 \pmod 2$, $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$.

$M = 30$, $M_1 = 15$, $M_2 = 10$, $M_3 = 6$.
- $15 X_1 \equiv 1 \pmod 2 \Rightarrow X_1 = 1$.
- $10 X_2 \equiv 1 \pmod 3 \Rightarrow X_2 = 1$.
- $6 X_3 \equiv 1 \pmod 5 \Rightarrow X_3 = 1$.

$x \equiv 1 \cdot 15 \cdot 1 + 2 \cdot 10 \cdot 1 + 3 \cdot 6 \cdot 1 = 53 \equiv 23 \pmod{30}$.

### 7.4 Zobecněná ČVOZ — bez nesoudělnosti

**Věta (ZČVOZ):** Soustava
$$x \equiv a_i \pmod{m_i}, \quad i = 1, \dots, N$$
má řešení **právě tehdy, když $\gcd(m_i, m_j) \mid (a_i - a_j)$ pro všechna $i \neq j$**. Pokud řešení existuje, je jednoznačné modulo $\operatorname{lcm}(m_1, \dots, m_N)$.

### 7.5 Dosazovací metoda

Univerzální postup, použitelný i pro ZČVOZ:
1. Vyřeš první kongruenci: $x = a_1 + m_1 t$ ($t \in \mathbb{Z}$).
2. Dosaď do druhé: $a_1 + m_1 t \equiv a_2 \pmod{m_2}$, vyřeš pro $t$.
3. Dostaneš $t = t_0 + m'_1 u$, dosaď zpět: $x = a_1 + m_1 (t_0 + m'_1 u)$ — to splňuje první dvě kongruence.
4. Iteruj přes zbylé kongruence.

### 7.6 Aplikace ČVOZ

- **Paralelní výpočty s velkými čísly:** rozdělíš modulo $m_1, \dots, m_r$ (prvočíselné), počítáš na $r$ procesorech v menších modulech, výsledek sklížíš přes ČVOZ.
- **RSA:** rozklad výpočtu modulo $n = pq$ na modulo $p$ a modulo $q$ urychluje dešifrování.

---

## 8. Co je potřeba na zkoušku znát

### Definice
- Dělitelnost, dělení se zbytkem ($a = qd + r$, $0 \leq r < d$).
- $\gcd$, $\operatorname{lcm}$, nesoudělnost.
- Bézoutovy koeficienty.
- Lineární diofantická rovnice (LDR).
- Prvočíslo, složené číslo, prvočíselný rozklad.
- Kongruence $a \equiv b \pmod m$, $\mathbb{Z}_m$, $+_m$, $\cdot_m$.
- Aditivní a multiplikativní inverze v $\mathbb{Z}_m$.
- Eulerova funkce $\varphi(n)$.
- Lineární kongruence, soustava lineárních kongruencí.

### Klíčové věty
- **O dělení se zbytkem** — existence a jednoznačnost $q, r$.
- **Eukleidův algoritmus** — $\gcd(a, b) = r_k$ (poslední nenulový zbytek).
- **Bézoutova rovnost** — $\gcd(a, b) = ma + nb$ pro nějaká $m, n \in \mathbb{Z}$; navíc je to nejmenší kladná lineární kombinace.
- **Řešitelnost LDR** $ax + by = c$: $\gcd(a, b) \mid c$.
- **Všechna řešení LDR:** $(x_0, y_0) + k(b/d, -a/d)$.
- **Nekonečnost prvočísel** (Eukleidův důkaz sporem).
- **Eukleidovo lemma** — $p \mid ab \land p \nmid a \Rightarrow p \mid b$.
- **Základní věta aritmetiky** — jednoznačná prvočíselná faktorizace.
- $\gcd \cdot \operatorname{lcm} = |a| \cdot |b|$.
- **Existence multiplikativní inverze v $\mathbb{Z}_m$** $\iff \gcd(a, m) = 1$.
- **Malá Fermatova věta:** $\gcd(a, p) = 1 \Rightarrow a^{p-1} \equiv 1 \pmod p$.
- **Eulerova věta:** $\gcd(a, m) = 1 \Rightarrow a^{\varphi(m)} \equiv 1 \pmod m$.
- **Krácení v modulu:** $ac \equiv bc \pmod m \iff a \equiv b \pmod{m/\gcd(m, c)}$.
- **Řešitelnost lineární kongruence** $ax \equiv b \pmod m$: $\gcd(a, m) \mid b$; pak $\gcd(a, m)$ řešení v $\mathbb{Z}_m$.
- **Čínská věta o zbytcích** (po dvou nesoudělná modula) — existence a jednoznačnost modulo $M = \prod m_i$.
- **Zobecněná ČVOZ** — podmínka $\gcd(m_i, m_j) \mid (a_i - a_j)$, jednoznačnost modulo $\operatorname{lcm}$.

### Algoritmy
- **EA** — $\gcd(a, b)$ posloupností zbytků.
- **REA / EEA** — gcd + Bézoutovy koeficienty; tabulkový nebo maticový zápis.
- **Řešení LDR** — REA + úprava partikulárního řešení.
- **Výpočet $\varphi(m)$** z faktorizace.
- **Inverze v $\mathbb{Z}_m$** přes REA nebo Eulerovu/MFV ($a^{p-2}$, $a^{\varphi(m)-1}$).
- **Binární mocnění** (square & multiply) — $b^N \bmod m$ v $O(\log N)$.
- **Řešení soustavy ČVOZ** — vzorec $x = \sum a_i M_i X_i$ nebo dosazovací metoda.
