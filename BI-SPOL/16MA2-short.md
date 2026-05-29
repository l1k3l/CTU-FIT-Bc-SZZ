# 16 — Diferenciální počet více proměnných a extrémy (zkrácená verze)

## 1. Okolí, limita, spojitost v $\mathbb{R}^n$

Norma $\lVert x\rVert=\sqrt{\sum x_j^2}$, vzdálenost $d(x,y)=\lVert x-y\rVert$. **Okolí** $U_a(\varepsilon)=\{x:d(x,a)<\varepsilon\}$ (koule). Hromadný bod, otevřená množina.

**[[Limita-funkce|Limita]]** $\lim_{x\to a}F(x)=b$: $\forall U_b\,\exists U_a\,\forall x\in(U_a\cap D_F)\setminus\{a\}:F(x)\in U_b$. **Po složkách:** $\iff\lim F_j=b_j\ \forall j$. **[[Spojitost]]:** $\lim_{x\to a}F=F(a)$.

## 2. Parciální derivace, gradient

**[[Parciální-derivace]]:** $\frac{\partial f}{\partial x_j}(a)=\lim_{h\to0}\frac{f(a+he_j)-f(a)}{h}$ (derivace ve směru osy, ostatní proměnné konst.). Smíšené: pořadí obecně nelze zaměnit; spojité $\Rightarrow$ lze (**Schwarz–Clairaut**).

**[[Gradient]]** (řádkový): $\nabla f(a)=(\frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n})(a)$. Derivace ve směru $\partial_v f(a)=\langle\nabla f(a)^T\mid v\rangle$; **gradient = směr největšího růstu**.

## 3. Derivace a Hessova matice

**Derivace** $DF(a)\in\mathbb{R}^{m,n}$: $\lim_{x\to a}\frac{\lVert F(x)-F(a)-DF(a)(x-a)\rVert}{\lVert x-a\rVert}=0$ (nejlepší lin. aproximace). Pak $DF(a)_{ij}=\frac{\partial F_i}{\partial x_j}(a)$ (Jacobi, jednoznačná). Pro $m=1$: $Df(a)=\nabla f(a)$. Tečná rovina $z=f(a)+\nabla f(a)(x-a)$.
- existence $Df$ ⇒ existují parc. derivace (ne naopak; stačí spojité parc. derivace).

**[[Hessova-matice]]** $\nabla^2 f(a)=(\frac{\partial^2 f}{\partial x_i\partial x_j}(a))_{i,j}\in\mathbb{R}^{n,n}$; symetrická, jsou-li 2. parc. derivace spojité.

## 4. Kvadratické formy a definitnost ([[Kvadratická-forma]])

$q(x)=x^T M x$, $M$ symetrická, $q(\theta)=0$.

| typ | podmínka |
|---|---|
| PD | $q(x)>0$, $x\neq\theta$ |
| PSD | $q(x)\ge0$ |
| ID | $\exists x,y:q(x)>0,q(y)<0$ |
| NSD | $q(x)\le0$ |
| ND | $q(x)<0$, $x\neq\theta$ |

**Určení:**
- **[[Vlastní-číslo|Vlastní čísla]]** $M$ (symetrická → reálná): kladná→PD, nezáporná→PSD, obě znam.→ID, nekladná→NSD, záporná→ND.
- **Sylvester** (rohové minory): PD ⟺ $\det M_k>0\ \forall k$; ND ⟺ $(-1)^k\det M_k>0\ \forall k$. (PSD/NSD: neostré minory NESTAČÍ.)
- **Úprava na čtverce** $q=\sum\alpha_j(\cdot)^2$: $n$ kladných→PD, $<n$ kladných→PSD, smíšená→ID. Různá znam. na diagonále→ID.

## 5. Lokální extrémy (bez omezení) ([[Lokální-extrém]])

**Def.:** ostré lok. min. v $a$: $\exists U_a$, $f(x)>f(a)$ na $U_a\setminus\{a\}$ (max: $<$; neostré: $\ge,\le$).

**Body:** $\nabla f(a)=\theta^T$ → **stacionární**; + neexist. gradient → **kritický**; stac. bez extrému → **sedlo**.

- **Nutná I:** extrém ⇒ $\nabla f(a)=\theta^T$ (nebo parc. der. neexistuje). *(Jen nutná: $x^2-y^2$ sedlo.)*
- **Nutná II:** lok. min/max + spojité 2. parc. der. ⇒ $\nabla^2 f(a)$ PSD/NSD. *(Jen nutná: $x^2-y^4$.)*
- **Postačující:** $\nabla f(a)=\theta^T$ a $\nabla^2 f(a)$ **PD** ⇒ ostré min, **ND** ⇒ ostré max, **ID** ⇒ sedlo. **PSD/NSD nerozhoduje** (rozbor z definice). *(Důkaz: Taylor do 2. řádu.)*

**Algoritmus:** $D_f,\nabla f$ → řeš $\nabla f=\theta$ → $\nabla^2 f$ v stac. bodech → definitnost → typ; PSD/NSD řeš z definice.

---

## Co odpovědět rychle

- **Parc. derivace** = derivace v jedné proměnné; **gradient** $\nabla f$ řádkový = směr růstu; **Hessova matice** = 2. parc. derivace (symetrická při spojitosti).
- **Definitnost** přes vlastní čísla / Sylvester ($\det M_k>0$ PD) / čtverce.
- **Extrém:** nutná $\nabla f=\theta^T$; postačující Hessián PD→min, ND→max, ID→sedlo; PSD/NSD nerozhoduje.
