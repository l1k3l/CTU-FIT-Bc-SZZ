---
tags: [otázka, kurz/MA1, otázka/13, todo]
---

# Limity a asymptotické chování

> **Otázka SZZ:** Limita posloupnosti, limita a spojitost reálné funkce jedné reálné proměnné, nástroje pro výpočet limit, asymptotické chování funkcí a posloupností (horní, dolní a těsné asymptotické meze, asymptotická ekvivalence).

Zdroje: BI-MA1 (Hrabák, Kalvoda, Petr, FIT ČVUT), kap. 2.4 (Asymptotické meze $o$, $O$), kap. 3 (Posloupnosti), kap. 4 (Limity), kap. 5 (Výpočet limit), kap. 6 (Spojitost), kap. 8.5 (L'Hospital).

Značení: $\mathbb{R}^* = \mathbb{R} \cup \{\pm\infty\}$ rozšířená osa; $U_\alpha$ okolí bodu $\alpha$ (pro $\alpha\in\mathbb{R}$ tvaru $(\alpha-\varepsilon,\alpha+\varepsilon)$, pro $+\infty$ tvaru $(c,+\infty)$); $D_f$ definiční obor; hromadný bod množiny $M$ = bod, v jehož každém okolí leží bod $M$ různý od něj.

---

## 1. Limita posloupnosti

**Definice ([[Posloupnost]]):** reálná posloupnost je zobrazení $a:\mathbb{N}\to\mathbb{R}$, $n$-tý člen $a_n$, celá posloupnost $(a_n)_{n=1}^\infty$. Je **omezená**, je-li $\exists K>0\,\forall n:|a_n|<K$; **(ostře) rostoucí/klesající** podle nerovností mezi sousedními členy.

**Definice ([[Limita-posloupnosti|limita posloupnosti]]):** $(a_n)$ má limitu $\alpha\in\mathbb{R}^*$, právě když
$$\forall U_\alpha\ \exists N\in\mathbb{N}\ \forall n\ge N:\ a_n\in U_\alpha.$$
Značíme $\lim_{n\to\infty}a_n=\alpha$ nebo $a_n\to\alpha$. Slovně: v každém okolí $\alpha$ leží **všechny členy až na konečně mnoho**. Pro $\alpha\in\mathbb{R}$ ekvivalentně $\forall\varepsilon>0\,\exists N\,\forall n\ge N:|a_n-\alpha|<\varepsilon$; pro $\alpha=+\infty$: $\forall c\,\exists N\,\forall n\ge N:a_n>c$.

**Věta (jednoznačnost).** Posloupnost má nejvýše jednu limitu.

*Důkaz (spor).* Kdyby $a_n\to b$ a $a_n\to c$, $b\neq c$, vezmeme disjunktní okolí $U_b\cap U_c=\emptyset$. Od jistého indexu by členy ležely v $U_b$ i $U_c$ současně — spor. $\square$

**Hromadný bod posloupnosti:** $\alpha$, v jehož **každém** okolí leží **nekonečně mnoho** členů. Pozor: to ke konvergenci nestačí (např. $a_n=n$ pro sudá, $\tfrac1n$ pro lichá $n$ má hromadné body $0$ i $+\infty$, ale limitu nemá).

**Konvergence (Def):** $(a_n)$ je **konvergentní**, je-li $\lim a_n\in\mathbb{R}$ (konečná), jinak **divergentní**.

### Existenční věty

**Bolzano–Weierstrassova věta.** Každá omezená posloupnost má hromadný bod v $\mathbb{R}$ (lze z ní vybrat konvergentní podposloupnost).

*Idea důkazu.* Půlením výchozího intervalu vždy vybíráme polovinu obsahující nekonečně mnoho členů; vznikne systém vnořených intervalů s délkami $\to 0$, jejich společný bod (axiom úplnosti) je hromadným bodem.

**Věta o limitě monotónní posloupnosti.** Každá monotónní posloupnost má limitu; je konečná ⟺ posloupnost je omezená. *(Postačující podmínka konvergence — stačí monotonie + omezenost.)*

**Bolzano–Cauchyova věta.** $(a_n)$ konverguje ⟺ je cauchyovská: $\forall\varepsilon>0\,\exists N\,\forall n,m>N:|a_n-a_m|<\varepsilon$. *(Kritérium konvergence bez znalosti hodnoty limity.)*

**Věta o limitě vybrané posloupnosti.** Má-li $(a_n)$ limitu $\alpha$, má ji i každá podposloupnost. ⇒ dvě podposloupnosti s různými limitami ⇒ limita neexistuje (např. $((-1)^n)$).

---

## 2. Limita a spojitost reálné funkce

**Definice ([[Limita-funkce|limita funkce]]):** $f:A\to\mathbb{R}$, $a$ hromadný bod $A$, $b\in\mathbb{R}^*$. Pak $\lim_{x\to a}f(x)=b$, právě když
$$\forall U_b\ \exists U_a\ \forall x\in(A\cap U_a)\setminus\{a\}:\ f(x)\in U_b.$$
Pro $a,b\in\mathbb{R}$ ekvivalentně **$\varepsilon$-$\delta$**: $\forall\varepsilon>0\,\exists\delta>0\,\forall x\in D_f\,(0<|x-a|<\delta\Rightarrow|f(x)-b|<\varepsilon)$. Limita posloupnosti je speciální případ ($\mathbb{N}$ má jediný hromadný bod $+\infty$).

Hodnota limity **nezávisí** na $f(a)$ — funkce v $a$ ani nemusí být definovaná (např. $\lim_{x\to0}\operatorname{sgn}(x^2)=1\neq f(0)=0$).

**Jednostranná limita:** $\lim_{x\to a^+}f := \lim_{x\to a}(f|_{A\cap(a,\infty)})$, analogicky zleva.

**Věta (vztah oboustranné a jednostranných limit).** $\lim_{x\to a}f=b$ ⟺ existují obě jednostranné limity a jsou rovny $b$.

*Důkaz.* (⇒) Z $f(x)\in U_b$ pro $x\in(U_a\cap D_f)\setminus\{a\}$ plyne totéž zvlášť pro $x>a$ a $x<a$. (⇐) Pro $U_b$ vezmeme levé okolí $U_a^-(\varepsilon_1)$ a pravé $U_a^+(\varepsilon_2)$; pro $\varepsilon=\min$ je $f(x)\in U_b$ na $U_a(\varepsilon)\setminus\{a\}$. $\square$

⇒ **Důsledek:** různé (či neexistující) jednostranné limity ⇒ oboustranná neexistuje (např. $\lim_{x\to0}\operatorname{sgn}x$).

**Heineho věta.** $\lim_{x\to a}f(x)=b$ ⟺ $a$ je hromadný bod $D_f$ a pro **každou** posloupnost $x_n\to a$, $x_n\in D_f\setminus\{a\}$, platí $f(x_n)\to b$. *(Most mezi limitou funkce a posloupnosti; nástroj k vyvracení limit.)*

*Použití (neexistence).* $\lim_{x\to+\infty}\sin x$ neexistuje: pro $x_n=2\pi n$ je $\sin x_n=0\to0$, pro $y_n=2\pi n+\tfrac\pi2$ je $\sin y_n=1\to1$.

### Spojitost

**Definice ([[Spojitost]]):** $f$ je **spojitá v bodě** $a\in D_f$, právě když
$$\lim_{x\to a}f(x)=f(a).$$
$\varepsilon$-$\delta$ tvar: $\forall\varepsilon>0\,\exists\delta>0\,\forall x:|x-a|<\delta\Rightarrow|f(x)-f(a)|<\varepsilon$. Spojitost **zprava/zleva**: $\lim_{x\to a^\pm}f=f(a)$. **Spojitá na intervalu** $J$: spojitá v každém bodě $J$.

**Věta (spojitost součtu/součinu/podílu a složení).** Jsou-li $f,g$ spojité v $a$, je spojitý jejich součet, součin a (při $g(a)\neq0$) podíl; složení spojitých funkcí je spojité. (Plyne z vět o limitách níže.) ⇒ polynomy, $\sin,\cos,\exp,\ln,\sqrt[k]{\ },|x|$ jsou spojité na $D_f$.

**Věty o spojitých funkcích na intervalu:**
- **Bolzanova (metoda půlení intervalu):** $f$ spojitá na $\langle a,b\rangle$, $f(a)f(b)<0$ ⇒ $\exists c\in(a,b):f(c)=0$. *(Konstruktivní důkaz = algoritmus hledání kořene půlením, $b_n-a_n=\tfrac{b-a}{2^{n-1}}\to0$.)*
- **O obrazu intervalu:** spojitý obraz intervalu je interval; spojitý obraz **uzavřeného** intervalu je uzavřený interval. ⇒ spojitá funkce na $\langle a,b\rangle$ nabývá globálního maxima i minima.

**Typy nespojitostí:** odstranitelná (limita existuje konečná, ale $\neq f(a)$, např. $\tfrac{\sin x}{x}$ v $0$ → dodefinuje se na $\operatorname{sinc}$); konečný skok ($\lim_{x\to a^+}\neq\lim_{x\to a^-}$, např. $\operatorname{sgn}$); nekonečná limita ($\tfrac1{x^2}$) či neexistence limity ($\sin\tfrac1x$).

---

## 3. Nástroje pro výpočet limit

**Věta o aritmetice limit (součet/součin/podíl).** Existují-li $\lim_a f$, $\lim_a g$, pak
$$\lim_a(f+g)=\lim_a f+\lim_a g,\quad \lim_a(fg)=\lim_a f\cdot\lim_a g,\quad \lim_a\tfrac fg=\frac{\lim_a f}{\lim_a g},$$
**pokud je pravá strana definována v $\mathbb{R}^*$**. (Neurčité výrazy $\infty-\infty$, $0\cdot\infty$, $\tfrac00$, $\tfrac\infty\infty$, $1^\infty$, $0^0$ věta neřeší — je třeba úprava.)

*Důkaz (součet, konečné limity).* Pro $\varepsilon>0$ ∃ $U_a$, kde $|f-c|<\tfrac\varepsilon2$ a $|g-d|<\tfrac\varepsilon2$; pak $|f+g-(c+d)|\le|f-c|+|g-d|<\varepsilon$. $\square$

**Věta o limitě sevřené funkce („dva policajti", squeeze).** Je-li $f\le g\le h$ na okolí $a$ a $\lim_a f=\lim_a h=b$, pak $\lim_a g=b$.

*Důkaz.* Pro okolí $V_b$ ∃ $V_a$, kde $f(x),h(x)\in V_b$; z $f\le g\le h$ pak i $g(x)\in V_b$. $\square$ — *Příklad:* $-\tfrac1n\le\tfrac{\sin n}{n}\le\tfrac1n\Rightarrow\lim\tfrac{\sin n}{n}=0$. Příbuzná **věta o vytlačení do nekonečna:** $f\le g$, $\lim_a f=+\infty\Rightarrow\lim_a g=+\infty$.

**Věta o limitě složené funkce.** Je-li $\lim_{x\to a}g(x)=b$, $\lim_{y\to b}f(y)=c$ a navíc buď $g(x)\neq b$ na okolí $a$, nebo $f$ je v $b$ spojitá ($f(b)=c$), pak $\lim_{x\to a}f(g(x))=c$. *(Čtvrtá podmínka je podstatná.)*

**Podílové kritérium (pro posloupnosti).** Buď $(a_n)$ s kladnými členy a $q=\lim\tfrac{a_{n+1}}{a_n}$. Pak $q<1\Rightarrow\lim a_n=0$; $q>1\Rightarrow\lim a_n=+\infty$. (Pro $q=1$ nerozhoduje.)

*Idea.* Pro $q<r<1$ je od jistého $N$ $a_{n+1}<r a_n$, tedy $0\le a_n\le r^{n-N-1}a_{N+1}\to0$, a věta o sevření dá $0$. *Příklad:* $\tfrac{a_{n+1}}{a_n}=\tfrac12(1+\tfrac1n)^2\to\tfrac12<1\Rightarrow\lim\tfrac{n^2}{2^n}=0$.

**L'Hospitalovo pravidlo** (kap. 8.5; důsledek Rolleovy věty). Pro typ $\tfrac00$ nebo $\tfrac\infty\infty$ (přesněji $\lim_a f=\lim_a g=0$ nebo $\lim_a|g|=+\infty$) a existuje-li $\lim_a\tfrac{f'}{g'}$, pak $\lim_a\tfrac fg=\lim_a\tfrac{f'}{g'}$. ⚠️ Nutno ověřit předpoklady (typ, existenci limity podílu derivací) — slepé použití dává chyby.

*Příklady:* $\lim_{x\to0}\tfrac{\arcsin x}{\sin x}=\lim\tfrac{1/\sqrt{1-x^2}}{\cos x}=1$; $\lim_{x\to+\infty}\tfrac{e^x}{x^2}=\lim\tfrac{e^x}{2x}=\lim\tfrac{e^x}{2}=+\infty$.

**Důležité limity (lze považovat za známé):**
$$\lim_{x\to0}\frac{\sin x}{x}=1,\quad \lim_{x\to0}\frac{e^x-1}{x}=1,\quad \lim_{x\to0}\frac{\ln(1+x)}{x}=1,\quad \lim_{x\to\pm\infty}\Big(1+\tfrac1x\Big)^x=e,$$
$$\lim_{n\to\infty}\sqrt[n]{n}=1,\quad \lim_{n\to\infty}\sqrt[n]{c}=1\ (c>0),\quad \lim_{n\to\infty}\sqrt[n]{n!}=+\infty,\quad \lim_{n\to\infty}a^n=\begin{cases}0,&|a|<1\\1,&a=1\\+\infty,&a>1\\\text{neex.},&a\le-1.\end{cases}$$
Limity tvaru $f(x)^{g(x)}$ se počítají přepisem $f^g=e^{g\ln f}$ (typy $1^\infty$, $0^0$ závisí na konkrétních $f,g$).

---

## 4. Asymptotické chování funkcí a posloupností

Nástroje pro **porovnání rychlosti růstu/poklesu** dvou funkcí, když $x\to a$ (u posloupností vždy $n\to+\infty$). Předpoklady: $a$ je hromadný bod $D_f\cap D_g$, definiční obory se na okolí $a$ shodují. Viz **[[Asymptotická-notace]]**.

### Horní meze $O$ a $o$

**Definice ($O$ — horní mez):** $f(x)=O(g(x))$ pro $x\to a$, právě když
$$\exists c>0\ \exists U_a\ \forall x\in(U_a\cap D_f\cap D_g)\setminus\{a\}:\ |f(x)|\le c\,|g(x)|.$$
Vyjadřuje „neostrou horní mez až na multiplikativní konstantu". *(„$=$" čteme jako $\in$.)*

**Definice ($o$ — striktní horní mez):** $f(x)=o(g(x))$, právě když
$$\forall c>0\ \exists U_a\ \forall x\in(U_a\cap D_f\cap D_g)\setminus\{a\}:\ |f(x)|<c\,|g(x)|.$$
Rozdíl od $O$: kvantifikátor u $c$ se mění na $\forall$ a $\le$ na $<$. „$f$ je striktně menšího řádu než $g$".

**Vlastnosti.** $O$ i $o$ jsou tranzitivní; $f=o(g)\Rightarrow f=O(g)$ (ne naopak); konstanta nemá vliv: $Kf=O(f)$. *Příklady:* $\sin x=O(1)$, $2n+1=O(n)$, $10x^2=O(x)$ pro $x\to0$; $x^2=o(x)$ pro $x\to0$, $\tfrac1{x^2}=o(\tfrac1x)$ pro $x\to+\infty$.

### Dolní a těsné meze $\Omega$, $\omega$, $\Theta$ (posloupnosti)

**Definice ($\Omega$ — dolní mez):** $a_n=\Omega(b_n)$, právě když $\exists c>0\,\exists N\,\forall n\ge N:|a_n|\ge c|b_n|$.

**Definice ($\omega$ — striktní dolní mez):** $a_n=\omega(b_n)$, právě když $\forall c>0\,\exists N\,\forall n\ge N:|a_n|>c|b_n|$.

**Definice ($\Theta$ — těsná mez):** $a_n=\Theta(b_n)$, právě když $\exists c_1,c_2>0\,\exists N\,\forall n\ge N:c_1|b_n|\le|a_n|\le c_2|b_n|$.

**Vlastnosti (přehled).** Lze je vnímat jako analogii uspořádání čísel:

| symbol | $\omega$ | $\Omega$ | $\Theta$ | $O$ | $o$ |
|---|---|---|---|---|---|
| analogie | $>$ | $\ge$ | $=$ | $\le$ | $<$ |

- $a_n=\Omega(b_n)\iff b_n=O(a_n)$; $\ a_n=\omega(b_n)\iff b_n=o(a_n)$;
- $a_n=\Theta(b_n)\iff a_n=O(b_n)\land a_n=\Omega(b_n)$; $\Theta$ je **relace ekvivalence**;
- $\omega\Rightarrow\Omega$; všechny tři jsou tranzitivní.

### Asymptotická ekvivalence $\sim$

**Definice:** $f(x)\sim g(x)$ pro $x\to a$, právě když existuje funkce $u$ s $\lim_{x\to a}u(x)=1$ a $f(x)=u(x)g(x)$ na okolí $a$.

**Vlastnosti.** $\sim$ je **relace ekvivalence** (reflexivní, symetrická, tranzitivní); je to nejpřesnější z uvedených vztahů. $f\sim g\Rightarrow f=\Theta(g)$. Má-li $f$ limitu $\alpha$ a $f\sim g$, má i $g$ limitu $\alpha$. *Příklad:* dva polynomy jsou $\sim$ v $+\infty$ ⟺ mají stejný stupeň i vedoucí koeficient.

### Vyjádření asymptotických vztahů pomocí limit

Je-li $g\neq0$ na okolí $a$:
$$\lim_{x\to a}\frac fg\in\mathbb{R}\ \Rightarrow\ f=O(g);\qquad \lim_{x\to a}\frac fg=0\ \iff\ f=o(g);\qquad \lim_{x\to a}\frac fg=1\ \iff\ f\sim g.$$
Pro posloupnosti ($b_n\neq0$): $\lim\tfrac{a_n}{b_n}>0\Rightarrow a_n=\Omega(b_n)$; $\ =+\infty\Rightarrow\omega$; $\ \in(0,+\infty)\Rightarrow\Theta$. Tím lze asymptotiku rozhodovat výpočtem limity (často přes podílové kritérium / L'Hospital) místo hledáním konstant. *Příklad:* $\lim\tfrac{n^2}{2^n}=0\Rightarrow n^2=o(2^n)$.

---

## Co je potřeba na zkoušku znát

### Definice
- Limita posloupnosti (okolí + $\varepsilon$-$N$), hromadný bod posloupnosti, konvergence/divergence.
- Limita funkce (okolí + $\varepsilon$-$\delta$), jednostranná limita, spojitost ($\lim_{x\to a}f=f(a)$).
- Asymptotické meze $O,o,\Omega,\omega,\Theta$ a ekvivalence $\sim$.

### Klíčové věty
- Jednoznačnost limity; vztah oboustranné a jednostranných limit; **Heineho věta**.
- **Bolzano–Weierstrass**, věta o limitě monotónní posloupnosti, **Bolzano–Cauchy**.
- Spojitost: **Bolzanova** (půlení intervalu), obraz uzavřeného intervalu ⇒ existence globálních extrémů.
- Aritmetika limit, věta o sevření, o složené funkci, **podílové kritérium**, **L'Hospital**.
- $\Theta=O\cap\Omega$, $\Theta$ a $\sim$ jsou ekvivalence; vyjádření $O/o/\sim$ a $\Omega/\omega/\Theta$ pomocí $\lim\tfrac fg$.

### Důležité limity
- $\frac{\sin x}{x}\to1$, $\frac{e^x-1}{x}\to1$, $\frac{\ln(1+x)}{x}\to1$, $(1+\tfrac1x)^x\to e$, $\sqrt[n]{n}\to1$, $a^n$ podle $|a|$.
