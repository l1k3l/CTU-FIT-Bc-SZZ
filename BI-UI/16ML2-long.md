---
studyplan: true
etapa: "4 · ML1 / ML2 — Dedecius + Holeňa"
qid: "16ML2"
examiner: "Holeňa"
topic: "Metoda podpůrných vektorů (SVM) pro klasifikaci"
readiness: nezačato
hot: true
tags: [otázka, kurz/ML2, otázka/16, todo]
---

# Metoda podpůrných vektorů (SVM)

> **Otázka SZZ:** Metoda podpůrných vektorů (SVM) pro klasifikaci.

Zdroje: BI-ML2 (FIT ČVUT), přednáška 2 — Diskriminační funkce, Princip největšího odstupu, Metoda podpůrných vektorů (lineárně separabilní i neseparabilní případ, duální formulace, jádrový trik).

Značení: binární klasifikace $Y\in\{-1,1\}$, $x\in\mathcal X$, $\varphi(x)\in\mathbb R^M$ vektor bázových funkcí, $f$ diskriminační funkce, $w,w_0$ parametry (normála a posun), $\lVert\cdot\rVert$ eukleidovská [[Norma|norma]], $\xi_i$ uvolněné proměnné, $C$ regularizační parametr, $a_i$ duální proměnné (Lagrangeovy multiplikátory), $k$ jádrová funkce.

---

## 1. Lineární diskriminační funkce

Uvažujme binární klasifikaci $Y\in\{-1,1\}$. V příznakovém prostoru $\mathbb R^M$ (s příznaky $\varphi(x)$ danými bázovými funkcemi) zaveďme **lineární diskriminační funkci**
$$f(x)=w^T\varphi(x)+w_0,\qquad \hat Y(x)=\operatorname{sgn} f(x)=\begin{cases}1 & f(x)\ge 0,\\ -1 & f(x)<0.\end{cases}$$

**Rozhodovací hranice** je dána $w^Tu+w_0=0$ — **nadrovina** v $\mathbb R^M$ (**separující nadrovina**, angl. *separating hyperplane*):

- její **normála** je vektor $w$;
- její **vzdálenost od počátku** ve směru $w$ je $d=-\dfrac{w_0}{\lVert w\rVert}$.

**Geometrie predikce.** Libovolný bod $u$ rozložíme ortogonálně na složku kolmou ($u_\perp$) a rovnoběžnou s $w$: $u=u_\perp+d\frac{w}{\lVert w\rVert}+r\frac{w}{\lVert w\rVert}$. Dosazením do $f$:
$$w^Tu+w_0=r\lVert w\rVert\quad\Longrightarrow\quad r=\frac{w^Tu+w_0}{\lVert w\rVert}.$$
Číslo $r=\dfrac{f(x)}{\lVert w\rVert}$ je **(signovaná) vzdálenost bodu $\varphi(x)$ od rozhodovací hranice** ve směru $w$. Znaménko $f(x)$ dělí prostor na dva poloprostory: kladný (ve směru $w$, predikce $1$) a záporný (predikce $-1$).

---

## 2. Princip největšího odstupu (hard margin)

Jak natrénovat $w,w_0$? Předpokládejme nejprve, že trénovací body $\varphi(x_1),\dots,\varphi(x_N)$ jsou **lineárně separabilní** — existuje nadrovina oddělující obě třídy. Pak takových nadrovin existuje nekonečně mnoho; vybereme tu s **největším odstupem** (angl. *largest margin*) = největší vzdáleností od nejbližšího bodu.

Vzdálenost $i$-tého bodu je $r_i=\frac{f(x_i)}{\lVert w\rVert}$; aby byl správně klasifikován, musí $Y_i f(x_i)>0$. Hledáme tedy
$$\max_{w,w_0}\ \min_i\ \frac{Y_i\big(w^T\varphi(x_i)+w_0\big)}{\lVert w\rVert}.$$

**Normalizace škály.** Přeškálování $w\to\kappa w$, $w_0\to\kappa w_0$ nemění vzdálenosti $r_i$. Zafixujeme škálu tak, aby pro nejbližší bod platilo $Y_j(w^T\varphi(x_j)+w_0)=1$, tj. pro všechny body
$$Y_i\big(w^T\varphi(x_i)+w_0\big)\ge 1.$$
Pak je minimální odstup $\frac1{\lVert w\rVert}$ a maximalizace $\lVert w\rVert^{-1}$ je ekvivalentní minimalizaci $\lVert w\rVert^2$.

**Geometrie pásu odstupu.** Krajní nadroviny $w^T\varphi(x)+w_0=\pm1$ leží symetricky po obou stranách hranice ve vzdálenosti $\frac1{\lVert w\rVert}$, takže **celková šířka pásu odstupu** (od jedné krajní nadroviny ke druhé) je $\dfrac{2}{\lVert w\rVert}$. Maximalizovat odstup = maximalizovat $\frac{2}{\lVert w\rVert}$ = minimalizovat $\frac12\lVert w\rVert^2$.

**Úloha trénování (hard-margin SVM):**
$$\boxed{\ \min_{w,w_0}\ \tfrac12\lVert w\rVert^2\quad\text{za podmínek}\quad Y_i\big(w^T\varphi(x_i)+w_0\big)\ge 1\ \ \forall i.\ }$$
Je to úloha **kvadratického programování** (konvexní kvadratická účelová funkce, lineární nerovnostní vazby) → jediné globální minimum.

**Podpůrné vektory.** Body, ve kterých je vazba **aktivní** ($Y_i(w^T\varphi(x_i)+w_0)=1$, tj. leží přesně na hraně pásu odstupu), se nazývají **podpůrné vektory** (angl. *support vectors*) — a **jen ony určují polohu** separující nadroviny. Odtud název **metoda podpůrných vektorů** (angl. *support vector machine, SVM*).

---

## 3. Lineárně neseparabilní případ (soft margin)

Když data nejsou lineárně separabilní, žádné $w,w_0$ nesplní všechny tvrdé vazby. Vazby proto **rozvolníme** zavedením **uvolněných proměnných** (angl. *slack variables*) $\xi_i\ge 0$:
$$Y_i f(x_i)\ge 1-\xi_i\qquad\text{(měkké podmínky, soft margin).}$$
Interpretace $\xi_i$ ($\xi_i=0$ vně pásu na správné straně; $0<\xi_i\le1$ uvnitř pásu, ale správně; $\xi_i>1$ špatně klasifikován), takže $\sum_i\xi_i$ je **horní mez počtu chyb** na trénovací množině.

**Úloha trénování (soft-margin SVM):**
$$\boxed{\ \min_{w,w_0,\xi}\ \tfrac12\lVert w\rVert^2+C\sum_{i=1}^N\xi_i\quad\text{za}\quad \xi_i\ge 0,\ \ Y_i\big(w^T\varphi(x_i)+w_0\big)\ge 1-\xi_i\ \ \forall i.\ }$$

**Parametr $C$** řídí kompromis mezi šířkou pásu a počtem chyb (tolerovaných na trénovací množině). Pozor na intuici: **čím větší $C$, tím slabší regularizace** (model se brání používat $\xi_i$ → méně chyb, riziko přeučení); malé $C$ = silná regularizace (malé $\lVert w\rVert$, více tolerovaných chyb). Volba $C=\frac{1}{\nu N}$ dává tzv. **$\nu$-SVM**, kde $0<\nu\le1$ je akceptovatelný podíl chyb.

> *Doplnění nad rámec slidů:* v optimu je $\xi_i=\max\{0,\,1-Y_i f(x_i)\}$, takže soft-margin SVM lze ekvivalentně zapsat jako **minimalizaci pantové (hinge) ztráty s regularizací**:
> $$\min_{w,w_0}\ \sum_{i=1}^N \max\{0,\,1-Y_i f(x_i)\}+\tfrac{1}{2C}\lVert w\rVert^2.$$
> Člen $\frac12\lVert w\rVert^2$ je tedy $L_2$-regularizace a hinge loss penalizuje porušení odstupu (lineárně, nulová mimo pás). To je obvyklý úhel pohledu, na který se Holeňa rád doptává.

---

## 4. Duální formulace a jádrový trik

Pomocí **Lagrangeových multiplikátorů** a **duality** lze úlohu převést na ekvivalentní **Lagrangeův duální problém** — maximalizovat vzhledem k $a_1,\dots,a_N$:
$$\tilde L(a)=\sum_{i=1}^N a_i-\frac12\sum_{i,j=1}^N a_i a_j Y_i Y_j\,k(x_i,x_j)\quad\text{za}\quad 0\le a_i\le C,\ \ \sum_{i=1}^N a_i Y_i=0,$$
kde $k(x_i,x_j)=\varphi(x_i)^T\varphi(x_j)$ je **[[Jádrová-funkce|jádrová funkce]]**.

> *Doplnění nad rámec slidů:* slidy uvádějí pouze „s využitím Lagrangeových multiplikátorů a duality lze ukázat…“. Klíčem je **KKT podmínka komplementární uvolněnosti** $a_i\big(Y_i f(x_i)-1+\xi_i\big)=0$: buď $a_i=0$, nebo je vazba aktivní. Odtud plyne **řídkost** — bod mimo pás odstupu má neaktivní vazbu, tedy $a_i=0$, a **podpůrné vektory jsou právě body s $a_i>0$**, tj. ty na hraně pásu nebo uvnitř/chybně klasifikované. KKT také vysvětlují tři režimy: $a_i=0$ (mimo pás), $0<a_i<C$ (na hraně, $\xi_i=0$), $a_i=C$ (uvnitř/chyba, $\xi_i>0$).

Klíčové: v duálu se body vyskytují **pouze ve skalárních součinech** $\varphi(x_i)^T\varphi(x_j)$ → můžeme provést **[[Jádrová-funkce|jádrový trik]]** a nahradit je jádrem $k$. Tím SVM klasifikuje **nelineárně** (např. Gaussovským/RBF jádrem) bez explicitního výpočtu $\varphi$.

Z řešení plyne $w=\sum_{j=1}^N a_j Y_j\,\varphi(x_j)$, takže diskriminační funkce je **jádrový model**:
$$f(x)=\sum_{j=1}^N a_j Y_j\,k(x,x_j)+w_0=\sum_{j=1}^N \alpha_j\,k(x,x_j)+w_0,\qquad \alpha_j=a_jY_j,$$
a predikce $\hat Y(x)=\operatorname{sgn} f(x)$.

---

## 5. Vlastnosti řešení

- Řešení je **řídké** (sparse): $a_j=0$ pro všechny správně klasifikované body **mimo** pás odstupu. Predikce tak závisí jen na podpůrných vektorech.
- **Podpůrné vektory** = body s $a_j>0$.
  - $0<a_j<C$ → leží přesně **na hraně** pásu odstupu;
  - $a_j=C$ → uvnitř pásu (správně), nebo špatně klasifikované.
- Čím větší $C$, tím **řidší** řešení (méně podpůrných vektorů).

*Příklad (XOR).* Lineárně neseparabilní data (XOR) klasifikuje SVM s **Gaussovským jádrem** správně nelineární hranicí; podpůrné vektory leží podél hranice. Větší $C$ → těsnější hranice, méně podpůrných vektorů; malé $C$ → hladší hranice, více chyb tolerováno.

---

## Co je potřeba na zkoušku znát

### Definice
- **Lineární diskriminační funkce:** $f(x)=w^T\varphi(x)+w_0$, $\hat Y=\operatorname{sgn} f(x)$; hranice = nadrovina s normálou $w$, vzdálenost bodu $r=\frac{f(x)}{\lVert w\rVert}$.
- **Odstup (margin):** vzdálenost separující nadroviny od nejbližšího bodu.
- **Podpůrné vektory:** body s aktivní vazbou / $a_j>0$ — určují polohu nadroviny.

### Věty / formulace
- **Hard-margin SVM:** $\min\tfrac12\lVert w\rVert^2$ s.t. $Y_i(w^T\varphi(x_i)+w_0)\ge1$ — kvadratické programování (konvexní → jedno globální optimum).
- **Soft-margin SVM:** $\min\tfrac12\lVert w\rVert^2+C\sum_i\xi_i$ s.t. $\xi_i\ge0$, $Y_i f(x_i)\ge1-\xi_i$; $\sum_i\xi_i$ = mez počtu chyb; velké $C$ = slabá regularizace.
- **Duál:** $\max_a\ \sum_i a_i-\tfrac12\sum_{i,j}a_ia_jY_iY_jk(x_i,x_j)$ s.t. $0\le a_i\le C$, $\sum_i a_iY_i=0$.
- **Výsledný model:** $f(x)=\sum_j a_jY_j\,k(x,x_j)+w_0$, řídký (jen podpůrné vektory).

### Idea / algoritmus
- **Princip největšího odstupu** + normalizace škály ($Y_j f(x_j)=1$ pro nejbližší) → minimalizace $\lVert w\rVert^2$.
- **Jádrový trik:** body jen ve skalárních součinech → záměna za jádro $k$ → nelineární klasifikace ([[Jádrová-funkce]]).

### Typické doplňující otázky (doptávání)
- **Holeňa (komise, předseda, LS2021):** „Bázové funkce, jádrová regrese, SVM — **zaměřte se na SVM**" (zúžil celou zkoušku jen na SVM — jeho oblíbené téma). → celá §1–§5

> *Konkrétní doptání u SVM nemáme ze zkušeností zaznamenané (jediný doložený záznam je výše uvedené zúžení).* Vzhledem k tomu, že SVM je Holeňovo téma a jako předseda ho rád zužuje, buď připraven(a) pohotově na celé jádro otázky — pravděpodobné směry: geometrie odstupu a **šířka pásu** $\tfrac{2}{\lVert w\rVert}$ (§2); **podpůrné vektory** a řídkost řešení (KKT, $a_i>0$ jen pro aktivní vazby — §4–§5); **jádrový trik** a proč je možný (body jen ve skalárních součinech v duálu — §4); role parametru $C$ a **soft margin / hinge loss** (větší $C$ = slabší regularizace — §3).
