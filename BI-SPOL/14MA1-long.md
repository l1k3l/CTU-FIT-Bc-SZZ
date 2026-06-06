---
studyplan: true
etapa: "7 · MA1 / DML / KAB — Petr"
qid: "14MA1"
examiner: "Petr"
topic: "Diferenciální počet: derivace, monotonie, konvexita, lok. extrémy, asymptoty"
readiness: nezačato
tags: [otázka, kurz/MA1, otázka/14, todo]
---

# Diferenciální počet funkce jedné proměnné

> **Otázka SZZ:** Diferenciální počet reálné funkce jedné reálné proměnné: derivace a její geometrický význam, vztah derivací funkce s její monotonií a konvexitou/konkavitou, lokální extrémy funkce jedné proměnné a metody jejich hledání, asymptoty funkce.

Zdroje: BI-MA1 (Hrabák, Kalvoda, Petr, FIT ČVUT), kap. 7 (Derivace), kap. 8 (Analýza průběhu funkce).

Značení: $f'(a)$ derivace v bodě, $f',f''$ první/druhá derivace, $J^\circ=(a,b)$ vnitřek intervalu $J$.

---

## 1. Derivace a její geometrický význam

**Motivace.** Průměrná rychlost mezi $t_1,t_2$ je $\tfrac{d(t_2)-d(t_1)}{t_2-t_1}$; okamžitá rychlost vznikne limitou $t_2\to t_1$. Geometricky: směrnice **sečny** grafu přejde limitně ve směrnici **tečny**.

**Definice ([[Derivace]] v bodě):** $f$ definovaná na okolí $a\in\mathbb{R}$. **Derivací** $f$ v bodě $a$ je (existuje-li) limita
$$f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}\in\mathbb{R}^*.$$
Je-li $f'(a)\in\mathbb{R}$ (konečná), je $f$ **diferencovatelná** v $a$. **Derivace** $f'$ je funkce přiřazující $x\mapsto f'(x)$ na množině bodů s konečnou derivací.

**Geometrický význam:** $f'(a)=\operatorname{tg}\alpha$ je **směrnice tečny** v $(a,f(a))$.

**Definice (tečna):** existuje-li $f'(a)$, je tečnou grafu $f$ v $a$
- přímka $y=f(a)+f'(a)(x-a)$, je-li $f'(a)\in\mathbb{R}$ (svírá s osou $x$ úhel $\alpha$, $\operatorname{tg}\alpha=f'(a)$);
- svislá přímka $x=a$, je-li $f$ spojitá v $a$ a $f'(a)=\pm\infty$.

*Příklady (z definice):* $(x^n)'=nx^{n-1}$, $(e^x)'=e^x$, $(\ln x)'=\tfrac1x$, $(\sin x)'=\cos x$, $(\cos x)'=-\sin x$.

**Věta (diferencovatelnost ⇒ spojitost).** Je-li $f$ diferencovatelná v $a$, je v $a$ [[Spojitost|spojitá]].

*Důkaz.* $\lim_{x\to a}f(x)=\lim_{x\to a}\big(\tfrac{f(x)-f(a)}{x-a}(x-a)+f(a)\big)=f'(a)\cdot0+f(a)=f(a)$. $\square$

**Obráceně neplatí:** $f(x)=|x|$ je v $0$ spojitá, ale $f'_+(0)=1\neq-1=f'_-(0)$, derivace neexistuje („zlom"). (Existují i funkce spojité na $\mathbb{R}$ bez derivace v jediném bodě.)

**Pravidla derivování (nástroje).** Pro $f,g$ diferencovatelné v $a$:
$$(f+g)'=f'+g',\quad (cf)'=cf',\quad (fg)'=f'g+fg'\ \text{(Leibniz)},\quad \Big(\tfrac fg\Big)'=\frac{f'g-fg'}{g^2}\ (g(a)\neq0).$$
**Řetízkové pravidlo:** $(f\circ g)'(a)=f'(g(a))\,g'(a)$. **Inverzní funkce:** je-li $f$ spojitá a ryze monotónní a $f^{-1}$ má konečnou nenulovou derivaci v $f(c)$, pak $f'(c)=\dfrac{1}{(f^{-1})'(f(c))}$. *(Důkazy přepisem na věty o limitách součtu/součinu/složené funkce.)* Vyšší derivace: $f^{(n)}=(f^{(n-1)})'$.

---

## 2. Věty o střední hodnotě a vztah derivace k monotonii

Tyto věty propojují **lokální** informaci (derivaci) s **globálním** chováním funkce.

**Rolleova věta.** Je-li $f$ spojitá na $\langle a,b\rangle$, má derivaci na $(a,b)$ a $f(a)=f(b)$, pak $\exists c\in(a,b):f'(c)=0$.

*Idea.* Konstantní $f$ — libovolné $c$. Jinak $f$ nabývá na $\langle a,b\rangle$ max/min (spojitost, uzavřený interval); aspoň jeden extrém je uvnitř, tam $f'=0$ (nutná podmínka extrému).

**Lagrangeova věta (o přírůstku funkce).** Je-li $f$ spojitá na $\langle a,b\rangle$ a má derivaci na $(a,b)$, pak
$$\exists c\in(a,b):\quad f'(c)=\frac{f(b)-f(a)}{b-a},\qquad\text{tj. } f(b)-f(a)=f'(c)(b-a).$$

*Důkaz.* Aplikuj Rolleovu větu na $g(x)=f(x)-\tfrac{f(b)-f(a)}{b-a}(x-a)$ (platí $g(a)=g(b)=f(a)$). $\square$

**Věta (vztah první derivace a monotonie).** Buď $f$ spojitá na $J$, $f'$ existuje na $J^\circ$. Pak na $J$:
$$f'\ge0\Rightarrow f \text{ rostoucí},\quad f'\le0\Rightarrow\text{klesající},\quad f'>0\Rightarrow\text{ostře rostoucí},\quad f'<0\Rightarrow\text{ostře klesající},\quad f'=0\Rightarrow\text{konstantní}.$$

*Důkaz (rostoucí).* Pro $x_1<x_2$ dá Lagrange $c\in(x_1,x_2)$ s $f(x_2)-f(x_1)=f'(c)(x_2-x_1)\ge0$. $\square$

⇒ **O monotonii rozhoduje znaménko derivace.**

---

## 3. Konvexita a konkavita; vztah k druhé derivaci

**Definice ([[Konvexní-funkce|konvexnost/konkávnost]] v bodě).** $f$ diferencovatelná v $a$ je **ryze konvexní** (resp. **konkávní**) v $a$, leží-li na okolí body grafu **nad** (resp. **pod**) tečnou:
$$f(x)>f(a)+f'(a)(x-a)\quad(\text{resp. }<),\qquad x\in U_a\setminus\{a\}.$$
S neostrými nerovnostmi: konvexní/konkávní. Na intervalu $J$: spojitá a (ryze) konvexní/konkávní v každém bodě $J^\circ$. ($f$ konkávní ⟺ $-f$ konvexní.)

*(Alternativně bez tečny: $(x_2,f(x_2))$ leží pod/na sečnou body $(x_1,f(x_1)),(x_3,f(x_3))$ pro $x_1<x_2<x_3$ — zahrnuje i $|x|$.)*

**Věta (kritérium konvexnosti).** Buď $f$ spojitá na $J$ s $f''$ na $J^\circ$. Pak
$$f''\ge0 \text{ na } J^\circ\iff f \text{ konvexní na } J;\qquad f''>0 \text{ na } J^\circ\Rightarrow f \text{ ryze konvexní}.$$
Pro konkávnost se nerovnosti otočí. Druhou implikaci **nelze obrátit** ($x^4$ ryze konvexní, ale $f''(0)=0$).

*Idea ⇒.* $f''\ge0$ ⇒ $f'$ rostoucí; Lagrange dá $f(x)=f(a)+f'(c)(x-a)\ge f(a)+f'(a)(x-a)$ (rozborem $x>a$, $x<a$). $\square$

⇒ **O konvexitě/konkavitě rozhoduje znaménko druhé derivace.**

**Inflexní bod:** bod $c$ (kde je $f$ spojitá), v němž se mění konvexita na konkavitu nebo naopak (ryze konvexní na jedné, ryze konkávní na druhé straně). Kandidáti: body s $f''(c)=0$.

---

## 4. Lokální extrémy a metody jejich hledání

**Definice ([[Lokální-extrém]]).** $f$ má v $a\in D_f$ **lokální maximum** (resp. **minimum**), je-li $\exists U_a\subset D_f$ s $f(x)\le f(a)$ (resp. $\ge$) pro $x\in U_a$; **ostré**, platí-li ostrá nerovnost pro $x\in U_a\setminus\{a\}$.

**Věta (nutná podmínka — Fermat).** Má-li $f$ v $a$ lokální extrém, pak **$f'(a)=0$ nebo $f'(a)$ neexistuje**.

*Důkaz.* Kdyby $f'(a)>0$, je $\tfrac{f(x)-f(a)}{x-a}>0$ na okolí, tedy $f(x)>f(a)$ vpravo a $f(x)<f(a)$ vlevo od $a$ — žádný extrém (spor). Podobně $f'(a)<0$. $\square$

⚠️ Podmínka je **jen nutná**: $f(x)=x^3$ má $f'(0)=0$, ale extrém nemá (je ostře rostoucí). Body s $f'=0$ = **stacionární**; kandidáti na extrém jsou stacionární body **a** body, kde $f'$ neexistuje (např. $|x|$ v $0$).

### Postačující kritéria

**(a) Změna monotonie / znaménka $f'$.** Je-li $f$ spojitá v $a$ a vlevo od $a$ (ostře) rostoucí, vpravo (ostře) klesající ⇒ v $a$ (ostré) lokální **maximum**; opačně **minimum**. Ekvivalentně: mění-li $f'$ v $a$ znaménko (a $f$ je v $a$ spojitá), je tam ostrý extrém. *(Spojitost podstatná: $|x|+\operatorname{sgn}x$ mění znaménko derivace, ale v $0$ extrém nemá.)*

**(b) Druhá derivace.** Je-li $f'(c)=0$ a $f$ je v $c$ ryze konvexní (typicky $f''(c)>0$) ⇒ ostré lokální **minimum**; ryze konkávní ($f''(c)<0$) ⇒ ostré lokální **maximum**.

### Globální extrémy

**Definice.** Globální maximum/minimum $f$ na $M$ je $\max_M f$ / $\min_M f$.

**Věta.** Funkce spojitá na **uzavřeném** intervalu $\langle a,b\rangle$ nabývá globálního maxima i minima, a to **jen v krajních bodech $a,b$, nebo v bodech, kde $f'=0$ nebo neexistuje**. *(Plyne z věty o obrazu uzavřeného intervalu.)* ⇒ Stačí porovnat funkční hodnoty v konečně mnoha „podezřelých" bodech. *(Uzavřenost je podstatná — $\tfrac1x+\tfrac1{x-4}$ na $(0,4)$ extrémy nemá.)*

*Příklad.* $f(x)=(x-1)(x-2)$ na $\langle0,2\rangle$: $f'=0$ v $\tfrac32$; porovnáním $f(0)=2$, $f(\tfrac32)=-\tfrac14$, $f(2)=0$ ⇒ globální max $2$ v $0$, globální min $-\tfrac14$ v $\tfrac32$.

---

## 5. Asymptoty funkce

**Definice ([[Asymptota]]).**
- **Svislá** asymptota $x=a$: alespoň jedna z jednostranných limit $\lim_{x\to a^\pm}f(x)$ je $\pm\infty$.
- **Asymptota se směrnicí** $y=kx+q$ v $+\infty$ (resp. $-\infty$): $\lim_{x\to+\infty}\big(f(x)-kx-q\big)=0$.

**Výpočet koeficientů (pro $\pm\infty$):**
$$k=\lim_{x\to+\infty}\frac{f(x)}{x},\qquad q=\lim_{x\to+\infty}\big(f(x)-kx\big),$$
musí existovat konečné obě limity. Pro $k=0$ jde o **vodorovnou** asymptotu $y=q$. Asymptoty v $+\infty$ a $-\infty$ se mohou lišit. *(Pozor: asymptota není tečna — graf ji může protnout.)*

*Příklad.* $f(x)=\sqrt[3]{3x^2-x^3}$: $k=\lim\sqrt[3]{\tfrac3x-1}=-1$, $q=\lim(\sqrt[3]{3x^2-x^3}+x)=1$ ⇒ asymptota $y=-x+1$ v $\pm\infty$.

### L'Hospitalovo pravidlo (nástroj pro limity asymptot a extrémů)

Pro typ $\tfrac00$ nebo $\tfrac\infty\infty$ a existuje-li $\lim_a\tfrac{f'}{g'}$, platí $\lim_a\tfrac fg=\lim_a\tfrac{f'}{g'}$. Je důsledkem Rolleovy věty. ⚠️ Nutno ověřit předpoklady. *Příklad:* $\lim_{x\to+\infty}\tfrac{e^x}{x^2}=\lim\tfrac{e^x}{2x}=\lim\tfrac{e^x}{2}=+\infty$ (proto $e^x$ roste rychleji než $x^2$).

---

## Shrnutí: vyšetřování průběhu funkce

1. definiční obor, průsečíky s osami, symetrie (sudost/lichost/periodicita);
2. spojitost, body nespojitosti, **asymptoty**, limity v krajních bodech $D_f$ (i $\pm\infty$);
3. $f'$: **monotonie**, lokální a globální **extrémy**;
4. $f''$: **konvexita/konkavita**, inflexní body;
5. náčrt grafu.

## Co je potřeba na zkoušku znát

### Definice
- Derivace v bodě (limita podílu), diferencovatelnost, tečna a její směrnice $f'(a)=\operatorname{tg}\alpha$.
- Lokální / globální extrém, stacionární bod; konvexní/konkávní funkce, inflexní bod; svislá a šikmá asymptota.

### Klíčové věty
- Diferencovatelnost ⇒ spojitost (ne naopak); pravidla derivování (součin, podíl, složená, inverzní).
- **Rolle** a **Lagrange** (o přírůstku) — most k monotonii a konvexitě.
- $f'>0\Rightarrow$ ostře rostoucí; $f''>0\Rightarrow$ ryze konvexní.
- **Nutná podmínka extrému** ($f'=0$ nebo neexistuje); postačující kritéria (změna znaménka $f'$; znaménko $f''$ ve stacionárním bodě).
- Existence globálních extrémů spojité funkce na uzavřeném intervalu.
- Vzorce pro asymptotu $k=\lim\tfrac{f(x)}x$, $q=\lim(f(x)-kx)$; L'Hospital.
