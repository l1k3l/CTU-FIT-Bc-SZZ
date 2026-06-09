---
tags: [otázka, kurz/MA1, otázka/13, todo]
---

# 13 — Limity a asymptotické chování (zkrácená verze)

## 1. Limita posloupnosti

[[Posloupnost]] $a:\mathbb{N}\to\mathbb{R}$. **[[Limita-posloupnosti|Limita]]** $\lim a_n=\alpha\in\mathbb{R}^*$:
$$\forall U_\alpha\,\exists N\,\forall n\ge N:\ a_n\in U_\alpha,\quad\text{tj. }\forall\varepsilon>0\,\exists N\,\forall n\ge N:|a_n-\alpha|<\varepsilon.$$
V každém okolí $\alpha$ leží všechny členy až na konečně mnoho. **Jednoznačná.** **Konvergentní** ⟺ $\lim\in\mathbb{R}$.

**Hromadný bod** $(a_n)$: v každém okolí nekonečně mnoho členů (ke konvergenci nestačí).

- **Bolzano–Weierstrass:** omezená posloupnost má hromadný bod (lze vybrat konvergentní podposloupnost).
- **Monotónní posl.** má limitu; konečnou ⟺ omezená.
- **Bolzano–Cauchy:** konverguje ⟺ $\forall\varepsilon\,\exists N\,\forall n,m>N:|a_n-a_m|<\varepsilon$.
- Limita ⇒ každá podposloupnost má touž limitu (2 různé ⇒ neexistuje).

## 2. Limita a spojitost funkce

**[[Limita-funkce|Limita funkce]]** $\lim_{x\to a}f=b$ ($a$ hrom. bod $D_f$):
$$\forall U_b\,\exists U_a\,\forall x\in(D_f\cap U_a)\setminus\{a\}:f(x)\in U_b,\quad \varepsilon\text{-}\delta:\ 0<|x-a|<\delta\Rightarrow|f(x)-b|<\varepsilon.$$
Nezávisí na $f(a)$. **Jednostranná:** $\lim_{x\to a^\pm}$. Platí $\lim_{x\to a}f=b\iff\lim_{x\to a^+}f=\lim_{x\to a^-}f=b$.

**Heine:** $\lim_{x\to a}f=b\iff$ pro každou $x_n\to a$, $x_n\neq a$, je $f(x_n)\to b$ (vyvracení limit).

**[[Spojitost]] v $a$:** $\lim_{x\to a}f(x)=f(a)$ ($a\in D_f$). Součet/součin/podíl/složení spojitých je spojité.
- **Bolzano (půlení):** $f$ spojitá na $\langle a,b\rangle$, $f(a)f(b)<0\Rightarrow\exists c:f(c)=0$.
- Spojitý obraz uzavřeného intervalu je uzavřený interval ⇒ existence glob. max/min.
- **Nespojitosti:** odstranitelná / konečný skok / nekonečná / neexistence limity.

## 3. Nástroje pro výpočet limit

- **Aritmetika limit:** $\lim(f\pm g)=\lim f\pm\lim g$, $\lim(fg)=\lim f\lim g$, $\lim\tfrac fg=\tfrac{\lim f}{\lim g}$ (je-li pravá strana def.).
- **Sevření (2 policajti):** $f\le g\le h$, $\lim f=\lim h=b\Rightarrow\lim g=b$.
- **Složená funkce:** $\lim_a g=b$, $\lim_b f=c$ (+ podmínka $g\neq b$ na okolí, nebo $f$ spojitá v $b$) $\Rightarrow\lim_a f\circ g=c$.
- **Podílové kritérium** (posl., $a_n>0$): $q=\lim\tfrac{a_{n+1}}{a_n}$; $q<1\Rightarrow\lim a_n=0$, $q>1\Rightarrow+\infty$.
- **L'Hospital** (typ $\tfrac00$, $\tfrac\infty\infty$): $\lim\tfrac fg=\lim\tfrac{f'}{g'}$, existuje-li pravá (ověř předpoklady!). Past: $\tfrac{2x+\sin x}{x+\sin x}$ — $\lim\tfrac{f'}{g'}$ neexistuje (≠ závěr), správně $=2$ úpravou $/x$; „bludný kruh" $\tfrac{e^x+e^{-x}}{e^x-e^{-x}}$ se cyklí.

**Známé limity:** $\frac{\sin x}{x}\to1$, $\frac{e^x-1}{x}\to1$, $\frac{\ln(1+x)}{x}\to1$, $(1+\tfrac1x)^x\to e$, $\sqrt[n]{n}\to1$, $\sqrt[n]{c}\to1$, $\sqrt[n]{n!}\to+\infty$, $a^n\to\{0/1/+\infty/\text{neex.}\}$ dle $|a|$. Tvar $f^g=e^{g\ln f}$.

## 4. Asymptotické chování ([[Asymptotická-notace]])

Porovnání pro $x\to a$ (posl. $n\to+\infty$). Na okolí $a$, $x\neq a$:

| | def. | analogie | limitní podmínka ($g\neq0$) |
|---|---|---|---|
| $f=O(g)$ | $\exists c>0:\lvert f\rvert\le c\lvert g\rvert$ | $\le$ | $\lim\tfrac fg\in\mathbb{R}\Rightarrow O$ |
| $f=o(g)$ | $\forall c>0\,\exists U_a:\lvert f\rvert<c\lvert g\rvert$ | $<$ | $\lim\tfrac fg=0\iff o$ |
| $a_n=\Omega(b_n)$ | $\exists c>0,N:\lvert a_n\rvert\ge c\lvert b_n\rvert$ | $\ge$ | $\lim\tfrac{a_n}{b_n}>0\Rightarrow\Omega$ |
| $a_n=\omega(b_n)$ | $\forall c>0\,\exists N:\lvert a_n\rvert>c\lvert b_n\rvert$ | $>$ | $\lim=+\infty\Rightarrow\omega$ |
| $a_n=\Theta(b_n)$ | $\exists c_1,c_2,N:c_1\lvert b_n\rvert\le\lvert a_n\rvert\le c_2\lvert b_n\rvert$ | $=$ | $\lim\in(0,+\infty)\Rightarrow\Theta$ |

- $\Omega(b)\iff b=O(a)$; $\omega(b)\iff b=o(a)$; $\Theta=O\cap\Omega$ (**ekvivalence**); $o\Rightarrow O$, $\omega\Rightarrow\Omega$; vše tranzitivní.
- **Asympt. ekvivalence** $f\sim g$: $\exists u$, $\lim u=1$, $f=u\,g$ na okolí $a$. **Ekvivalence**, nejpřesnější; $f\sim g\Rightarrow f=\Theta(g)$; $\lim\tfrac fg=1\iff f\sim g$.

---

## Co odpovědět rychle

- **Lim. posl.:** $\forall\varepsilon\,\exists N\,\forall n\ge N:|a_n-\alpha|<\varepsilon$. Konverg. ⟺ $\lim\in\mathbb{R}$. B–W, monotónní+omezená, B–C.
- **Lim. funkce / spojitost:** $\varepsilon$-$\delta$; spojitá ⟺ $\lim_{x\to a}f=f(a)$; Heine; Bolzano (kořen).
- **Nástroje:** aritmetika, sevření, složená, podílové kritérium, L'Hospital + známé limity.
- **Asymptotika:** $O\le$, $o<$, $\Omega\ge$, $\omega>$, $\Theta=$; $\sim$ nejpřesnější; přes $\lim\tfrac fg$.
