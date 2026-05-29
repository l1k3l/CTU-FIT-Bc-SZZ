---
tags: [otázka, kurz/MA1, otázka/14, todo]
---

# 14 — Diferenciální počet (zkrácená verze)

## 1. Derivace a geometrický význam

**[[Derivace]] v bodě:**
$$f'(a)=\lim_{x\to a}\frac{f(x)-f(a)}{x-a}=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}\in\mathbb{R}^*.$$
**Diferencovatelná** ⟺ $f'(a)\in\mathbb{R}$. Geometricky $f'(a)=\operatorname{tg}\alpha$ = **směrnice tečny**.

**Tečna:** $y=f(a)+f'(a)(x-a)$ (pro $f'(a)\in\mathbb{R}$); svislá $x=a$ (pro $f$ spojitou, $f'(a)=\pm\infty$).

**Diferencovatelnost ⇒ [[Spojitost|spojitost]]** (ne naopak: $|x|$ v $0$).

**Pravidla:** $(f+g)'=f'+g'$, $(fg)'=f'g+fg'$, $(\tfrac fg)'=\tfrac{f'g-fg'}{g^2}$, $(f\circ g)'=f'(g)\,g'$, $(f^{-1})'(f(c))=\tfrac1{f'(c)}$.
Základní: $(x^n)'=nx^{n-1}$, $(e^x)'=e^x$, $(\ln x)'=\tfrac1x$, $(\sin)'=\cos$, $(\cos)'=-\sin$, $(\operatorname{tg})'=\tfrac1{\cos^2}$, $(\arctan)'=\tfrac1{1+x^2}$.

## 2. Věty o střední hodnotě + monotonie

- **Rolle:** $f$ spojitá $\langle a,b\rangle$, derivace na $(a,b)$, $f(a)=f(b)\Rightarrow\exists c:f'(c)=0$.
- **Lagrange (přírůstek):** $\exists c\in(a,b):f'(c)=\tfrac{f(b)-f(a)}{b-a}$.

**Monotonie (na $J$, $f$ spojitá, $f'$ na $J^\circ$):**
$$f'\ge0\Rightarrow\text{rostoucí},\ f'>0\Rightarrow\text{ostře rost.},\ f'<0\Rightarrow\text{ostře kles.},\ f'=0\Rightarrow\text{konst.}$$
(Důkaz: Lagrange.) **Znaménko $f'$ rozhoduje o monotonii.**

## 3. Konvexita/konkavita

**[[Konvexní-funkce|Ryze konvexní]] v $a$:** body grafu **nad** tečnou, $f(x)>f(a)+f'(a)(x-a)$ na okolí; **konkávní** = pod. ($-f$ konvexní ⟺ $f$ konkávní.)

**Kritérium:** $f''\ge0$ na $J^\circ\iff f$ konvexní; $f''>0\Rightarrow$ ryze konvexní (neobrátitelné: $x^4$). Konkávně opačně. **Znaménko $f''$ rozhoduje o konvexitě.**

**Inflexní bod:** mění se konvexita↔konkavita; kandidáti $f''(c)=0$.

## 4. Lokální extrémy a hledání

**[[Lokální-extrém]]:** $\exists U_a:f(x)\le f(a)$ (max) / $\ge$ (min); ostré s $<,>$ na $U_a\setminus\{a\}$.

**Nutná podmínka (Fermat):** extrém ⇒ $f'(a)=0$ (**stacionární bod**) **nebo** $f'$ neexistuje. Jen nutná! ($x^3$ v $0$: $f'=0$, ale bez extrému.)

**Postačující:**
- **Změna znaménka $f'$** (a $f$ spojitá v $a$): $+\to-$ ⇒ ostré max, $-\to+$ ⇒ ostré min.
- **2. derivace:** $f'(c)=0$ a $f''(c)>0\Rightarrow$ ostré min; $f''(c)<0\Rightarrow$ ostré max.

**Globální extrém na $\langle a,b\rangle$ (spojitá):** existuje; nabývá se v krajních bodech, nebo kde $f'=0$/neexistuje ⇒ porovnej funkční hodnoty. (Uzavřenost podstatná.)

## 5. Asymptoty

**[[Asymptota]]:**
- **Svislá** $x=a$: $\lim_{x\to a^\pm}f=\pm\infty$.
- **Se směrnicí** $y=kx+q$ v $\pm\infty$: $\lim(f(x)-kx-q)=0$, kde
$$k=\lim_{x\to\pm\infty}\frac{f(x)}{x},\qquad q=\lim_{x\to\pm\infty}(f(x)-kx).$$
$k=0$ ⇒ vodorovná. (Asymptota ≠ tečna.)

**L'Hospital** (pro limity): typ $\tfrac00$, $\tfrac\infty\infty$ ⇒ $\lim\tfrac fg=\lim\tfrac{f'}{g'}$ (ověř předpoklady).

**Vyšetřování průběhu:** $D_f$ + symetrie → spojitost + asymptoty + limity v krajích → $f'$ (monotonie, extrémy) → $f''$ (konvexita, inflexe) → graf.

---

## Co odpovědět rychle

- **Derivace** = $\lim\tfrac{f(x)-f(a)}{x-a}=\operatorname{tg}\alpha$ (směrnice tečny). Diferenc. ⇒ spojitá.
- **Monotonie** ↔ znaménko $f'$; **konvexita** ↔ znaménko $f''$ (přes Lagrange).
- **Extrém:** nutná $f'=0$/neex.; postačující změna znaménka $f'$ nebo $f''(c)\gtrless0$.
- **Asymptota:** $k=\lim\tfrac fx$, $q=\lim(f-kx)$; svislá kde $\lim=\pm\infty$.
