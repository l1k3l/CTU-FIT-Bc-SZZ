---
tags: [otázka, kurz/MA2, otázka/16, todo]
---

# Diferenciální počet funkcí více proměnných a extrémy

> **Otázka SZZ:** Funkce více proměnných: diferenciální počet funkcí více proměnných (limita, parciální derivace, derivace, gradient, Hessova matice), kvadratické formy a jejich definitnosti, analytická metoda hledání lokálních extrémů funkcí více proměnných (bez omezení).

Zdroje: BI-MA2 (Kalvoda, Pernecká, Petr, FIT ČVUT), kap. 7 (Funkce více proměnných), kap. 8 (Kvadratické formy), kap. 9.1–9.3 (Extrémy funkcí více proměnných).

Značení: $x=(x_1,\dots,x_n)^T\in\mathbb{R}^n$ (sloupcový vektor), $\theta$ nulový vektor, $\hat n=\{1,\dots,n\}$, $e_j$ $j$-tý vektor standardní báze, $\langle x\mid y\rangle=x^T y$ standardní skalární součin.

---

## 1. Okolí, limita a spojitost v $\mathbb{R}^n$

**Euklidovská norma a vzdálenost:** $\lVert x\rVert=\sqrt{\sum_{j=1}^n x_j^2}=\sqrt{\langle x\mid x\rangle}$, $\ d(x,y)=\lVert x-y\rVert$. *(Schwarz: $|\langle x\mid y\rangle|\le\lVert x\rVert\lVert y\rVert$; trojúhelníková: $\lVert x+y\rVert\le\lVert x\rVert+\lVert y\rVert$.)*

**Definice (okolí).** $U_a(\varepsilon)=\{x\in\mathbb{R}^n\mid d(x,a)<\varepsilon\}$ — otevřená koule (v $\mathbb{R}^1$ interval, v $\mathbb{R}^2$ kruh bez kružnice). **Hromadný bod** $M$: v každém okolí leží bod $M$ různý od $a$. **Vnitřní bod / otevřená množina** (každý bod vnitřní), **hraniční bod**.

**Vektorová posloupnost** $(x_k)_{k=1}^\infty$, $x_k\in\mathbb{R}^n$: $\lim_k x_k=a\iff\lim_k\lVert x_k-a\rVert=0\iff$ konverguje **po složkách** ($\lim_k(x_k)_j=a_j\ \forall j$). Vyvrácení: stačí divergence jedné složky.

**Definice ([[Limita-funkce|limita]] funkce více proměnných).** $F:D_F\to\mathbb{R}^m$, $D_F\subset\mathbb{R}^n$, $a$ hromadný bod $D_F$. Pak $\lim_{x\to a}F(x)=b\in\mathbb{R}^m$ právě když
$$\forall U_b\ \exists U_a\ \forall x\in(U_a\cap D_F)\setminus\{a\}:\ F(x)\in U_b.$$
**Po složkách:** $\lim_{x\to a}F(x)=b\iff\lim_{x\to a}F_j(x)=b_j$ pro každé $j\in\hat m$. Platí věty o limitě součtu, násobku, součinu a podílu (jako v BI-MA1).

**Definice ([[Spojitost]]).** $F$ je spojitá v $a\in D_F$ (hromadném bodě), právě když $\lim_{x\to a}F(x)=F(a)$. Součet/násobek/součin/podíl ($G(a)\neq0$) i složení spojitých funkcí jsou spojité; elementární funkce zadané po složkách (např. $\sin x+\cos y$, $\ln(xy)$) jsou spojité na svých definičních oborech.

---

## 2. Parciální derivace a gradient

**Definice ([[Parciální-derivace]]).** $f:D_f\to\mathbb{R}$, $D_f\subset\mathbb{R}^n$, definovaná na okolí $a$, $j\in\hat n$. Existuje-li limita
$$\frac{\partial f}{\partial x_j}(a)=\lim_{h\to0}\frac{f(a+h e_j)-f(a)}{h},$$
je to **parciální derivace** $f$ v $a$ podle $j$-té proměnné. Je to obyčejná [[Derivace|derivace]] funkce $g(t)=f(a+t e_j)$ v $0$.

- **Výpočet:** derivujeme podle $x_j$, ostatní proměnné bereme jako konstanty (platí běžná pravidla).
- **Geometrický význam:** míra růstu $f$ v bodě $a$ ve směru $j$-té souřadné osy.
- **Vyšší/smíšené:** $\tfrac{\partial^2 f}{\partial x_k\partial x_j}=\tfrac{\partial}{\partial x_k}\big(\tfrac{\partial f}{\partial x_j}\big)$; pořadí obecně **nelze** zaměnit (protipříklad $f(x,y)=xy\tfrac{x^2-y^2}{x^2+y^2}$ v $\theta$: $\tfrac{\partial^2 f}{\partial x\partial y}(\theta)=1\neq-1=\tfrac{\partial^2 f}{\partial y\partial x}(\theta)$).

*Příklad.* $f(x,y)=x+xy+y$: $\tfrac{\partial f}{\partial x}=1+y$, $\tfrac{\partial f}{\partial y}=x+1$.

**Definice ([[Gradient]]).** Má-li $f$ v $a$ všechny parciální derivace konečné, je **gradient** řádkový vektor
$$\nabla f(a)=\operatorname{grad}f(a)=\Big(\tfrac{\partial f}{\partial x_1}(a),\dots,\tfrac{\partial f}{\partial x_n}(a)\Big)\in\mathbb{R}^{1,n}.$$

**Derivace ve směru** (jednotkový $v$): $\partial_v f(a)=\lim_{h\to0}\tfrac{f(a+hv)-f(a)}{h}=\langle\nabla f(a)^T\mid v\rangle$. **Gradient je směr největšího růstu** — maximum $\partial_v f(a)$ je pro $v=\nabla f(a)^T/\lVert\nabla f(a)\rVert$ (ze Schwarzovy nerovnosti).

---

## 3. Derivace funkce a Hessova matice

**Motivace.** V BI-MA1 byla $f'(a)$ směrnicí tečny: $f(x)\approx f(a)+f'(a)(x-a)$ (nejlepší lineární aproximace). Zobecnění: lineární člen popíše matice.

**Definice (derivace zobrazení).** $F:D_F\to\mathbb{R}^m$, $D_F\subset\mathbb{R}^n$, definované na okolí $a$. **Derivací** $F$ v $a$ je matice $DF(a)\in\mathbb{R}^{m,n}$ splňující
$$\lim_{x\to a}\frac{\lVert F(x)-F(a)-DF(a)(x-a)\rVert}{\lVert x-a\rVert}=0,$$
tj. $F(x)\approx F(a)+DF(a)(x-a)$ a chyba je menší než lineární.

**Věta (složky a jednoznačnost).** Má-li $F$ derivaci $DF(a)$, pak je dána jednoznačně a
$$DF(a)_{i,j}=\frac{\partial F_i}{\partial x_j}(a)\qquad(\text{Jacobiho matice}).$$
*Důkaz (idea).* Z definice po zúžení na přímku $x=a+he_j$ ($h\to0$) vyjde právě parciální derivace $\partial_{x_j}F_i(a)$. $\square$

**Důsledky.** Pro $f:\mathbb{R}^n\to\mathbb{R}$ ($m=1$) je $Df(a)=\nabla f(a)$ (proto je gradient řádkový). **Tečná rovina** ke grafu $z=f(x)$ v $a$: $\ z=f(a)+\nabla f(a)(x-a)$. Vztah parciální ↔ totální derivace:
- existuje-li $Df(a)$, pak existují všechny parciální derivace (ukázáno);
- **obráceně neplatí** — samotná existence parciálních derivací nestačí. Stačí ale **spojitost** všech prvních parciálních derivací na okolí $a$.

**Derivace složeného zobrazení (řetězové pravidlo):** $D(F\circ G)(a)=DF(G(a))\cdot DG(a)$.

**Definice ([[Hessova-matice]]).** Derivace gradientu chápaného jako zobrazení $\mathbb{R}^n\to\mathbb{R}^n$ — matice druhých parciálních derivací
$$\nabla^2 f(a)=\Big(\tfrac{\partial^2 f}{\partial x_i\partial x_j}(a)\Big)_{i,j=1}^n\in\mathbb{R}^{n,n}.$$
*(„Hessián" v české terminologii často značí $\det\nabla^2 f$.)*

**Symetrie (Schwarzova–Clairautova věta).** Jsou-li všechny druhé parciální derivace spojité na okolí $a$, je $\nabla^2 f(a)$ **symetrická** (typický případ). Symetrickou matici lze chápat jako kvadratickou formu — to je most k části 4 a 5.

---

## 4. Kvadratické formy a jejich definitnosti

**Motivace.** Taylor v 1D: $f(x)=f(a)+f'(a)(x-a)+\tfrac{f''(a)}2(x-a)^2+\dots$ — o extrému rozhodoval znaménko $f''$. Ve více proměnných je analogem kvadratického členu kvadratická forma s maticí $\nabla^2 f(a)$.

**Definice ([[Kvadratická-forma]]).** $q:\mathbb{R}^n\to\mathbb{R}$ je kvadratická forma, existuje-li symetrická [[Matice|matice]] $M\in\mathbb{R}^{n,n}$ s
$$q(x)=\sum_{j,k=1}^n M_{j,k}x_j x_k = x^T M x = \langle x\mid Mx\rangle.$$
Vždy $q(\theta)=0$. (Symetrie není omezující: $x^T A x=x^T\tfrac12(A+A^T)x$.)

**Definice (definitnost).** Kvadratická forma (resp. její symetrická matice) je
- **pozitivně definitní (PD):** $q(x)>0$ pro každé $x\neq\theta$;
- **pozitivně semidefinitní (PSD):** $q(x)\ge0$ pro každé $x$;
- **indefinitní (ID):** $\exists x,y:\ q(x)>0$ a $q(y)<0$;
- **negativně semidefinitní (NSD):** $q(x)\le0$ pro každé $x$;
- **negativně definitní (ND):** $q(x)<0$ pro každé $x\neq\theta$.

*(Konvence kurzu: každá PD je i PSD; jediná forma současně PSD i NSD je nulová. V 1D je $q(x)=\alpha x^2$ a ID neexistuje.)*

### Určování definitnosti

**Vztah k vlastním číslům.** Symetrická reálná matice je **diagonalizovatelná** s reálnými [[Vlastní-číslo|vlastními čísly]] a ortonormální bází vlastních vektorů ($M=PDP^T$, $P^{-1}=P^T$).

**Věta (definitnost a vlastní čísla).** $q(x)=x^T M x$ je PD / PSD / ID / NSD / ND právě tehdy, když vlastní čísla $M$ jsou **všechna kladná / nezáporná / s oběma znaménky / nekladná / záporná**.

*Důkaz (idea).* $q(x)=x^T PDP^T x=\sum_j\lambda_j (P^T x)_j^2$; podle znamének $\lambda_j$ a volbou $x=Pe_j$ plynou ekvivalence. $\square$

**Úprava na čtverce.** Postupně doplníme členy s $x_k^2$ na čtverec a vyjádříme $q(x)=\sum_{j=1}^k\alpha_j(\dots)^2$ ($k$ nezávislých čtverců, $\alpha_j\neq0$). Pak: $k=n$, všechna $\alpha_j>0\Rightarrow$ PD; $k=n$, $\alpha_j<0\Rightarrow$ ND; $k<n$, $\alpha_j>0\Rightarrow$ PSD (ne PD); smíšená znaménka $\Rightarrow$ ID. (Pro čistě smíšené členy: $xy=\tfrac14(x+y)^2-\tfrac14(x-y)^2$.) *Příklad:* $x^2+2xy+2y^2=(x+y)^2+y^2$ PD; $x^2+4xy+y^2=(x+2y)^2-3y^2$ ID.

**Sylvesterovo kritérium** (rohové minory $M_k=(M_{ij})_{i,j=1}^k$):
$$M\ \text{PD}\iff\det M_k>0\ \forall k\in\hat n;\qquad M\ \text{ND}\iff(-1)^k\det M_k>0\ \forall k\in\hat n.$$
⚠️ Pro PSD/NSD **nestačí** neostré nerovnosti rohových minorů (nutno všechny hlavní minory; např. $M=\operatorname{diag}\text{-like}$ s $\det M_k\ge0$ může být ID). **Indefinitnost rychle:** různá znaménka na diagonále $M$ $\Rightarrow$ ID.

---

## 5. Analytická metoda hledání lokálních extrémů (bez omezení)

**Definice ([[Lokální-extrém]]).** $f:D_f\to\mathbb{R}$, $D_f\subset\mathbb{R}^n$, $a\in D_f$. $f$ má v $a$ **ostré lokální minimum** (resp. **maximum**), existuje-li okolí $U_a$ s $f(x)>f(a)$ (resp. $<$) pro $x\in(U_a\cap D_f)\setminus\{a\}$; **(neostré) lokální min./max.** s $\ge$ (resp. $\le$) pro $x\in U_a\cap D_f$.

### Nutné podmínky

**Věta (nutná podmínka I — gradient).** Má-li $f$ v $a$ lokální extrém, pak každá parciální derivace v $a$ je $0$ nebo neexistuje. Existují-li všechny parciální derivace, je $\nabla f(a)=\theta^T$.

*Důkaz.* Funkce $g(t)=f(a+t e_j)$ má v $0$ lokální extrém, tedy $g'(0)$ je $0$ nebo neexistuje; ale $g'(0)=\partial_{x_j}f(a)$ (1D nutná podmínka z BI-MA1). $\square$

**Terminologie ([[Lokální-extrém|Def.]]).** $\nabla f(a)=\theta^T$ → **stacionární bod**; $\nabla f(a)=\theta^T$ nebo gradient neexistuje → **kritický bod** (jen tam může být extrém); stacionární bod bez extrému → **sedlový bod**.

⚠️ Nutná, ne postačující: $f(x,y)=x^2-y^2$ má $\nabla f(\theta)=\theta^T$, ale v $\theta$ je sedlo ($f(t,0)>0>f(0,t)$). Extrém může být i v bodě s neexistujícím gradientem: $f(x,y)=\sqrt{x^2+y^2}$ (kužel) má v $\theta$ ostré minimum.

**Věta (nutná podmínka II — Hessova matice).** Má-li $f$ spojité všechny druhé parciální derivace na okolí $a$ a v $a$ lokální **minimum** (resp. **maximum**), je $\nabla^2 f(a)$ **PSD** (resp. **NSD**).

*Důkaz (idea).* Pro $x\neq\theta$ uvaž $g(h)=f(a+hx)$; z 1D Taylora a $g'(0)=0$ plyne $0\le g(h)-g(0)=\tfrac12 g''(\xi_h)h^2$ s $g''(0)=x^T\nabla^2 f(a)x$; limitou $x^T\nabla^2 f(a)x\ge0$. $\square$

⚠️ Také jen nutná: $f(x,y)=x^2-y^4$ má $\nabla f(\theta)=\theta^T$ a PSD Hessovu matici, ale v $\theta$ extrém nemá.

### Postačující podmínka

**Věta (postačující podmínka).** $f$ má spojité třetí parciální derivace na okolí $a$ a platí
1. $\nabla f(a)=\theta^T$ (stacionární bod),
2. $\nabla^2 f(a)$ je **PD** (resp. **ND**).

Pak má $f$ v $a$ **ostré lokální minimum** (resp. **maximum**). Je-li $\nabla^2 f(a)$ **ID**, je $a$ **sedlový bod** (extrém nenastává).

*Důkaz (idea).* Taylorova věta do kvadratických členů: $f(x)-f(a)=\tfrac12(x-a)^T\nabla^2 f(a)(x-a)+R_2$, $|R_2|\le M\lVert x-a\rVert^3$. Pro PD je $(x-a)^T\nabla^2 f(a)(x-a)\ge\lambda_*\lVert x-a\rVert^2$ ($\lambda_*$ = nejmenší vl. číslo $>0$); pro dost malé okolí kvadratický člen převáží zbytek, takže $f(x)>f(a)$. ND přes $-f$; ID přes existenci směrů s opačnými znaménky $x^T\nabla^2 f(a)x$. $\square$

⚠️ Vyjde-li $\nabla^2 f(a)$ **PSD** nebo **NSD** (a ne definitní), věta **nerozhoduje** — nutno zkoumat $f$ na okolí přímo z definice (např. $f=x^2+y^3$ má v $\theta$ PSD Hessián, ale extrém nemá).

### Algoritmus (vyšetření lokálních extrémů)

1. urči $D_f$ a $\nabla f$;
2. vyřeš $\nabla f(x)=\theta^T$ → **stacionární body** (+ body, kde gradient neexistuje);
3. sestav $\nabla^2 f$ a v každém stac. bodě urči její **definitnost** (vlastní čísla / Sylvester / čtverce);
4. PD → ostré min., ND → ostré max., ID → sedlo; PSD/NSD → rozhodni z definice.

*Příklad.* $f(x,y)=x^4+y^4-x^2-2xy-y^2$. $\nabla f=(4x^3-2x-2y,\,4y^3-2x-2y)$; stacionární body $a=(-1,-1)$, $b=(0,0)$, $c=(1,1)$. $\nabla^2 f=\left(\begin{smallmatrix}12x^2-2&-2\\-2&12y^2-2\end{smallmatrix}\right)$. V $a,c$: $\left(\begin{smallmatrix}10&-2\\-2&10\end{smallmatrix}\right)$ PD ($10>0$, $\det=96>0$) → ostrá lokální minima. V $b$: $\left(\begin{smallmatrix}-2&-2\\-2&-2\end{smallmatrix}\right)$ NSD ($=-2(x+y)^2$) → nerozhodne; rozbor $f(t,-t)=2t^4>0$, $f(t,0)=t^4-t^2<0$ → **sedlo**.

*(Aplikace: metoda nejmenších čtverců — minimalizace $\lVert y-Ac\rVert^2$ vede na $\nabla F=-2A^T y+2A^T Ac=\theta$, řešení $c=(A^T A)^{-1}A^T y$; Hessián $2A^T A$ je PD.)*

---

## Co je potřeba na zkoušku znát

### Definice
- Okolí v $\mathbb{R}^n$, hromadný bod; limita a spojitost funkce více proměnných (přes okolí, po složkách).
- Parciální derivace, gradient (řádkový), derivace = matice nejlepší lineární aproximace, Hessova matice.
- Kvadratická forma a pět typů definitnosti; lokální/sedlový/stacionární/kritický bod.

### Klíčové věty
- $DF(a)_{ij}=\partial_{x_j}F_i(a)$ (Jacobiho matice), pro $m=1$ je $Df=\nabla f$; existence derivace ⇒ parciální derivace (ne naopak; stačí spojité parciální derivace).
- **Schwarzova–Clairautova** věta (symetrie Hessovy matice).
- **Definitnost ⟺ znaménka vlastních čísel**; **Sylvesterovo kritérium** (PD: $\det M_k>0$; ND: $(-1)^k\det M_k>0$); úprava na čtverce.
- **Nutná I:** extrém ⇒ $\nabla f(a)=\theta^T$. **Nutná II:** min/max ⇒ Hessián PSD/NSD.
- **Postačující:** $\nabla f(a)=\theta^T$ + Hessián PD/ND ⇒ ostré min/max; ID ⇒ sedlo; PSD/NSD nerozhoduje.

### Pozor
- Všechny podmínky přes gradient/Hessián jsou jen nutné, resp. postačující — protipříklady $x^2-y^2$ (sedlo), $x^2-y^4$ (PSD bez extrému), $\sqrt{x^2+y^2}$ (extrém bez gradientu).
