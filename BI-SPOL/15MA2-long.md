---
studyplan: true
etapa: "3 · LA1 / MA2 / LA2 — Petr"
qid: "15MA2"
examiner: "Petr"
topic: "Integrální počet, číselné řady a kritéria konvergence"
readiness: nezačato
tags: [otázka, kurz/MA2, otázka/15, todo]
---

# Integrální počet, číselné řady a asymptotika součtů

> **Otázka SZZ:** Integrální počet funkce jedné proměnné (neurčitý integrál a Riemannův určitý integrál, metody integrace pomocí substituce a per partes), číselné řady a kritéria jejich konvergence, asymptotické odhady chování posloupností částečných součtů řad pomocí integrálu.

Zdroje: BI-MA2 (Kalvoda, Pernecká, Petr, FIT ČVUT), kap. 2 (Primitivní funkce a neurčitý integrál), kap. 3 (Riemannův určitý integrál), kap. 4.1–4.3 (Číselné řady, kritéria konvergence, odhadování součtů).

Značení: $\int f$ neurčitý integrál, $\int_a^b f$ Riemannův integrál; $\mathbb{R}^*=\mathbb{R}\cup\{\pm\infty\}$.

---

## 1. Neurčitý integrál (primitivní funkce)

**Definice ([[Primitivní-funkce]]):** $f$ definovaná na intervalu $(a,b)$. Funkce $F$ s
$$F'(x)=f(x)\quad\forall x\in(a,b)$$
je **primitivní funkcí** k $f$ na $(a,b)$. Taková $F$ je diferencovatelná, a tedy [[Spojitost|spojitá]] na $(a,b)$. Integrace je „inverzní" k [[Derivace|derivaci]].

**Věta (jednoznačnost až na konstantu).** Je-li $F$ primitivní k $f$ na $(a,b)$, pak $G$ je primitivní k $f$ $\iff$ $\exists C\in\mathbb{R}:\ G(x)=F(x)+C$.

*Důkaz.* $(F-G)'=f-f=0$ na $(a,b)$, tedy $F-G$ je konstantní (věta o vztahu derivace a monotonie). Naopak $(F+C)'=F'=f$. $\square$

**Definice (neurčitý integrál):** množina všech primitivních funkcí k $f$ na $(a,b)$,
$$\int f(x)\,dx = F(x)+C.$$
$f$ = integrand, $x$ = integrační proměnná, $C$ = integrační konstanta. Platí $\big(\int f\big)'=f$ a $\int g'\,dx=g+C$.

**Věta (postačující podmínka existence).** Je-li $f$ spojitá na $(a,b)$, má na $(a,b)$ primitivní funkci. *(Bez důkazu.)*

**Věta (linearita).** $\int(f+g)=\int f+\int g$, $\ \int(\alpha f)=\alpha\int f$. *(Z linearity derivace.)*

**Tabulkové integrály** (z derivací elementárních funkcí): $\int x^n dx=\tfrac{x^{n+1}}{n+1}+C$ ($n\neq-1$), $\int\tfrac1x dx=\ln|x|+C$, $\int e^x dx=e^x+C$, $\int a^x dx=\tfrac{a^x}{\ln a}+C$, $\int\sin x\,dx=-\cos x+C$, $\int\cos x\,dx=\sin x+C$, $\int\tfrac{1}{\cos^2 x}dx=\operatorname{tg}x+C$, $\int\tfrac{1}{\sqrt{1-x^2}}dx=\arcsin x+C$, $\int\tfrac{1}{1+x^2}dx=\arctan x+C$.

Ne každá elementární funkce má elementární primitivní funkci ($\int e^{-x^2}dx$, $\int\tfrac{\sin x}x dx$, $\int\tfrac{1}{\ln x}dx$ — existují, ale nelze je vyjádřit konečně mnoha operacemi z elementárních funkcí).

---

## 2. Metody integrace: per partes a substituce

### Per partes (po částech)

**Věta (per partes — neurčitý integrál).** $f$ diferencovatelná na $(a,b)$, $G$ primitivní k $g$, existuje-li primitivní funkce k $f'G$, pak existuje i k $fg$ a
$$\int f g = fG - \int f'G.$$
*(Často $\int u v' = uv-\int u'v$.)*

*Důkaz.* Derivací: $(fG-\int f'G)' = (fG)'-f'G = f'G+fG'-f'G=fG'=fg$ (Leibnizovo pravidlo). $\square$

Vhodné pro součin, kde jeden činitel derivováním „mizí" (polynom) nebo se cyklicky vrací (exp·sin).

*Příklady.*
- $\int x\sin x\,dx = -x\cos x+\int\cos x\,dx = -x\cos x+\sin x+C$.
- $\int x^2 e^x dx = x^2 e^x - 2\int x e^x dx = (x^2-2x+2)e^x+C$ (per partes dvakrát).
- $\int\arctan x\,dx = x\arctan x-\int\tfrac{x}{1+x^2}dx = x\arctan x-\tfrac12\ln(1+x^2)+C$ (trik $1\cdot\arctan x$).

### Substituce

**Věta (o substituci I).** Má-li $f$ primitivní funkci $F$ na $(a,b)$, je $\varphi$ diferencovatelná na $(\alpha,\beta)$ a $\varphi((\alpha,\beta))\subset(a,b)$, pak
$$\int f(\varphi(x))\,\varphi'(x)\,dx = F(\varphi(x))+C.$$
*Důkaz.* $(F\circ\varphi)'(x)=F'(\varphi(x))\varphi'(x)=f(\varphi(x))\varphi'(x)$ (derivace složené funkce). $\square$ — Použití: v integrandu „odhalíme" $\varphi'$, položíme $y=\varphi(x)$. Speciálně $\int\tfrac{\varphi'(x)}{\varphi(x)}dx=\ln|\varphi(x)|+C$.

**Věta (o substituci II).** Je-li $\varphi$ bijekce $(\alpha,\beta)\to(a,b)$ s nenulovou konečnou derivací a $\int f(\varphi(t))\varphi'(t)\,dt=G(t)+C$, pak $\int f(x)\,dx = G(\varphi^{-1}(x))+C$. *(Volíme $x=\varphi(t)$; opírá se o derivaci inverzní funkce — užitečné na odstranění odmocnin, např. $x=\sin t$, $x=\sinh t$.)*

*Příklady.* $\int\tfrac{1}{x^2}\sin\tfrac1x dx = -\cos\tfrac1x+C$ (subst. $y=\tfrac1x$); $\int\tfrac{1}{\sqrt{1-x^2}}dx=\arcsin x+C$ (subst. $x=\sin t$).

**Integrace racionálních funkcí** $\int\tfrac{p(x)}{q(x)}dx$: dělení polynomů + **rozklad na parciální zlomky** ($\tfrac{ax+b}{(x-c)(x-d)}=\tfrac{A}{x-c}+\tfrac{B}{x-d}$) → integrály typu $\ln|x-a|$, $\tfrac{1}{x-a}$, resp. doplnění na čtverec → $\arctan$.

---

## 3. Riemannův určitý integrál

**Konstrukce (Darbouxova).** Buď $f$ omezená na $J=\langle a,b\rangle$ a $\sigma=\{a=x_0<\dots<x_n=b\}$ **dělení** ($\Delta_i=x_i-x_{i-1}$, norma $\nu(\sigma)=\max_i\Delta_i$). **Dolní** a **horní součet:**
$$s(\sigma,f)=\sum_{i=1}^n\Delta_i\!\!\inf_{\langle x_{i-1},x_i\rangle}\!\!f,\qquad S(\sigma,f)=\sum_{i=1}^n\Delta_i\!\!\sup_{\langle x_{i-1},x_i\rangle}\!\!f$$
(obsah obdélníků pod, resp. nad grafem). **Dolní/horní integrál:** $\underline{\int_a^b}f=\sup_\sigma s(\sigma,f)$, $\overline{\int_a^b}f=\inf_\sigma S(\sigma,f)$.

**Definice ([[Riemannův-integrál]]).** Pokud $\underline{\int_a^b}f=\overline{\int_a^b}f\in\mathbb{R}$, nazýváme společnou hodnotu **Riemannovým integrálem** $\int_a^b f(x)\,dx$. Geometricky obsah plochy mezi grafem a osou $x$ (se znaménkem).

**Věta (postačující podmínka existence).** $f$ **spojitá** na $\langle a,b\rangle$ $\Rightarrow$ $\int_a^b f$ existuje; navíc pro libovolnou **normální** posloupnost dělení ($\nu(\sigma_n)\to0$) je
$$\int_a^b f = \lim_n s(\sigma_n,f)=\lim_n S(\sigma_n,f) = \lim_n \mathcal{J}(\sigma_n,f),$$
kde $\mathcal{J}(\sigma,f)=\sum_i f(\alpha_i)\Delta_i$, $\alpha_i\in\langle x_{i-1},x_i\rangle$, je **integrální součet** (stačí $s\le\mathcal{J}\le S$).

*Příklad neexistence:* Dirichletova funkce ($1$ na $\mathbb{Q}$, jinak $0$) má na $\langle0,1\rangle$ horní integrál $1$, dolní $0$.

### Vlastnosti

- **Linearita:** $\int_a^b(f+g)=\int_a^b f+\int_a^b g$, $\ \int_a^b cf=c\int_a^b f$.
- **Aditivita v mezích:** $\int_a^b f=\int_a^c f+\int_c^b f$.
- **Monotonie:** $f\le g$ na $\langle a,b\rangle\Rightarrow\int_a^b f\le\int_a^b g$. *(Klíčové pro odhady v části 5.)*

### Newtonova–Leibnizova formule

**Věta (Newtonova formule).** $f$ spojitá na $\langle a,b\rangle$ s primitivní funkcí $F$. Pak
$$\int_a^b f(x)\,dx = F(b)-F(a) = \big[F(x)\big]_a^b.$$

*Důkaz.* Pro dělení $\sigma$ aplikuj **Lagrangeovu větu o přírůstku** na $F$ na každém $\langle x_{i-1},x_i\rangle$: $\exists\alpha_i$ s $F(x_i)-F(x_{i-1})=F'(\alpha_i)\Delta_i=f(\alpha_i)\Delta_i$. Sečtením (teleskopicky) $F(b)-F(a)=\sum_i f(\alpha_i)\Delta_i=\mathcal{J}(\sigma,f)$. Limitou přes normální posloupnost dělení $F(b)-F(a)=\int_a^b f$. $\square$

Propojuje geometrickou konstrukci s primitivní funkcí — umožňuje počítat $\int_a^b f$ bez limit.

**Per partes a substituce pro určitý integrál** (z Newtonovy formule):
$$\int_a^b fg = \big[fG\big]_a^b - \int_a^b f'G,\qquad \int_a^b f(\varphi(t))\varphi'(t)\,dt = \int_{\varphi(a)}^{\varphi(b)} f(x)\,dx.$$

*Příklady.* $\int_0^1 x\,dx=[\tfrac{x^2}2]_0^1=\tfrac12$; $\int_0^\pi\sin x\,dx=[-\cos x]_0^\pi=2$; $\int_0^1\ln(1+x)\,dx=2\ln2-1$ (per partes).

---

## 4. Číselné řady a kritéria konvergence

**Definice ([[Číselná-řada]]).** Pro [[Posloupnost|posloupnost]] $(a_k)_{k=0}^\infty$ je $\sum_{k=0}^\infty a_k$ číselná řada; **posloupnost částečných součtů** $s_n=\sum_{k=0}^n a_k$. Řada **konverguje**, je-li $(s_n)$ [[Limita-posloupnosti|konvergentní]], a její **součet** je $\lim_n s_n$; jinak **diverguje**. Konvergence se nezmění změnou konečně mnoha členů.

**Geometrická řada:** $\sum_{k=0}^\infty q^k=\tfrac{1}{1-q}$ pro $|q|<1$ (jinak diverguje). *(Z $s_n=\tfrac{1-q^{n+1}}{1-q}$.)*

**Linearita:** konvergují-li $\sum a_k=S_a$, $\sum b_k=S_b$, pak $\sum(a_k+b_k)=S_a+S_b$ a $\sum(c\,a_k)=c\,S_a$.

### Kritéria

**Věta (nutná podmínka).** $\sum a_k$ konverguje $\Rightarrow\lim_{k}a_k=0$.

*Důkaz.* $S=\lim s_n$; $|a_n|=|s_n-s_{n-1}|\le|s_n-S|+|S-s_{n-1}|\to0$. $\square$

⚠️ Jen **nutná**: $\sum\tfrac1k$ (harmonická) i $\sum\tfrac1{\sqrt k}$ mají $a_k\to0$, přesto **divergují** ($s_n\ge\tfrac{n}{\sqrt n}=\sqrt n\to\infty$). **Důsledek:** $a_k\not\to0$ (či limita neexistuje) $\Rightarrow$ řada diverguje.

**Věta (Bolzano–Cauchy).** $\sum a_k$ konverguje $\iff\forall\varepsilon>0\,\exists n_0\,\forall n\ge n_0\,\forall p\in\mathbb{N}:\ |a_n+\dots+a_{n+p}|<\varepsilon$. *(B–C kritérium pro posloupnost $(s_n)$.)*

**Definice (absolutní konvergence):** $\sum a_k$ je **absolutně konvergentní**, konverguje-li $\sum|a_k|$.

**Věta.** Absolutní konvergence $\Rightarrow$ konvergence. *(Z B–C: $|a_n+\dots+a_{n+p}|\le|a_n|+\dots+|a_{n+p}|<\varepsilon$.)* Naopak neplatí ($\sum\tfrac{(-1)^k}{k}$). U neabsolutně konvergentních záleží na pořadí sčítání.

**Věta (srovnávací kritérium).**
- (a) $0\le|a_k|\le b_k$ od jistého $k_0$ a $\sum b_k$ konverguje $\Rightarrow\sum a_k$ absolutně konverguje;
- (b) $0\le a_k\le b_k$ a $\sum a_k$ diverguje $\Rightarrow\sum b_k$ diverguje.

*Důkaz (a).* B–C: $\sum_{k=n}^{n+p}|a_k|\le\sum_{k=n}^{n+p}b_k<\varepsilon$. $\square$

**Věta (d'Alembertovo / podílové kritérium).** $a_k>0$. Je-li $\lim_k\tfrac{a_{k+1}}{a_k}<1\Rightarrow\sum a_k$ konverguje; $>1\Rightarrow$ diverguje. *(Pro $=1$ nerozhoduje, např. $\sum\tfrac1k$.)*

*Idea.* Pro $\tilde q=\lim<q<1$ je od $k_0$ $a_k\le q^{k-k_0}a_{k_0}$, srovnání s geometrickou řadou. *Příklad:* $\sum\tfrac{k^{1000}}{2^k}$ konverguje, neboť $\tfrac{a_{k+1}}{a_k}\to\tfrac12<1$.

**Věta (Leibnizovo kritérium).** Je-li $(a_k)$ monotónní a $\lim_k a_k=0$, pak $\sum(-1)^k a_k$ konverguje („řada se střídavými znaménky").

*Idea.* Vybrané součty $(s_{2n+1})$ rostou a jsou shora omezené ($\in\langle0,a_0\rangle$) $\Rightarrow$ mají limitu; $s_{2n}=s_{2n+1}+a_{2n+1}\to$ táž limita. Monotonie je podstatná. *Příklad:* $\sum\tfrac{(-1)^k}{k}$ konverguje (ale ne absolutně).

---

## 5. Asymptotické odhady součtů pomocí integrálu

Některé částečné součty $s_n=\sum_{k=1}^n a_k$ nelze sečíst explicitně (např. $\sum\tfrac1k$). Lze je ale **geometricky srovnat s plochou pod křivkou**, kterou počítá [[Riemannův-integrál|integrál]] (součet $\sum a_k$ = obsah obdélníků šířky $1$).

**Věta 4.7 (odhad částečných součtů integrálem).** Buď $f$ spojitá na $\langle1,+\infty)$, $n\in\mathbb{N}$.
- $f$ **klesající**: $\displaystyle f(n)+\int_1^n f \le \sum_{k=1}^n f(k) \le f(1)+\int_1^n f.$
- $f$ **rostoucí**: $\displaystyle f(1)+\int_1^n f \le \sum_{k=1}^n f(k) \le f(n)+\int_1^n f.$

*Důkaz (klesající).* Pro $x\in\langle k,k+1\rangle$ je $f(k+1)\le f(x)\le f(k)$; z monotonie integrálu $f(k+1)\le\int_k^{k+1}f\le f(k)$. Sečtením přes $k$ a úpravou plynou obě nerovnosti. $\square$

**Důsledky (rychlost růstu).**
- $\sum_{k=1}^n k^2$: $f(x)=x^2$ rostoucí, $\int_1^n x^2=\tfrac{n^3-1}3$ $\Rightarrow$ $\tfrac13 n^3+\tfrac23\le s_n\le\tfrac13 n^3+n^2-\tfrac13$, tedy $s_n\sim\tfrac13 n^3$ ($\lim\tfrac{s_n}{n^3/3}=1$).
- $\ln n!=\sum_{k=1}^n\ln k$: $f(x)=\ln x$ rostoucí, $F(x)=x\ln x-x$ $\Rightarrow$ $n\ln n-n+1\le\ln n!\le\ln n+n\ln n-n+1$, odlogaritmováním $e\cdot\tfrac{n^n}{e^n}\le n!\le e n\cdot\tfrac{n^n}{e^n}$ (slabší než **Stirling** $n!\sim\sqrt{2\pi n}\,\tfrac{n^n}{e^n}$).
- **Harmonická čísla:** $f(x)=\tfrac1x$ klesající, $\int_1^n\tfrac1x=\ln n$ $\Rightarrow$ $\tfrac1n+\ln n\le\sum_{k=1}^n\tfrac1k\le1+\ln n$, tedy $\sum_{k=1}^n\tfrac1k\sim\ln n$ a $\sum_{k=1}^n\tfrac1k-\ln n\to\gamma$ (**Eulerova–Mascheroniova konstanta** $\approx0{,}5772$).

**Věta 4.8 (integrální kritérium).** Buď $\sum a_n$ s kladnými členy a $f$ spojitá, monotónní na $\langle1,+\infty)$ s $f(n)=a_n$. Pak
$$\sum_{n=1}^\infty a_n \text{ konverguje} \iff \int_1^\infty f(x)\,dx \text{ konverguje}.$$
*(Přímý důsledek Věty 4.7.)*

*Příklad.* $\sum k^\alpha$ konverguje $\iff\alpha<-1$: $\int_1^\infty x^\alpha dx$ konverguje pro $\alpha<-1$ a diverguje pro $\alpha\ge-1$. Speciálně $\sum\tfrac1k$ ($\alpha=-1$) i $\sum\tfrac1{\sqrt[3]{k}}$ ($\alpha=-\tfrac13$) divergují.

---

## Co je potřeba na zkoušku znát

### Definice
- Primitivní funkce ($F'=f$) a neurčitý integrál; Riemannův integrál (dolní/horní součet a integrál, shoda).
- Číselná řada, částečný součet, konvergence/součet, absolutní konvergence.

### Klíčové věty
- Jednoznačnost primitivní funkce (až na $C$); existence pro spojité $f$; linearita.
- **Per partes** $\int fg=fG-\int f'G$ a obě věty o **substituci** (+ verze pro určitý integrál).
- Existence Riemannova integrálu pro spojitou funkci; vlastnosti (linearita, aditivita v mezích, **monotonie**).
- **Newtonova formule** $\int_a^b f=F(b)-F(a)$ (důkaz přes Lagrange).
- **Nutná podmínka** $a_k\to0$; **srovnávací**, **d'Alembertovo**, **Leibnizovo**, **integrální** kritérium; absolutní ⇒ obyčejná konvergence.
- **Věta 4.7** (odhad $\sum f(k)$ integrálem) a důkaz pro klesající $f$; integrální kritérium.

### Typické výsledky
- Geometrická řada $\tfrac{1}{1-q}$; $\sum k^\alpha$ konv. $\iff\alpha<-1$; harmonická řada diverguje.
- $\sum_{k=1}^n\tfrac1k\sim\ln n$ (+ konstanta $\gamma$); $\ln n!\approx n\ln n-n$; $\sum k^2\sim\tfrac13 n^3$.
