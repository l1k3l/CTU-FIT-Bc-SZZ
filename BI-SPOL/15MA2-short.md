# 15 — Integrální počet, řady, asymptotika součtů (zkrácená verze)

## 1. Neurčitý integrál ([[Primitivní-funkce]])

**Primitivní fce:** $F$ na $(a,b)$ s $F'=f$. **Jednoznačná až na $C$**: $\int f\,dx=F+C$ (množina všech prim. fcí). Spojitá $f\Rightarrow$ prim. fce existuje. **Linearita.**

Tabulka: $\int x^n=\tfrac{x^{n+1}}{n+1}$ ($n\neq-1$), $\int\tfrac1x=\ln|x|$, $\int e^x=e^x$, $\int\tfrac{1}{1+x^2}=\arctan x$, $\int\tfrac{1}{\sqrt{1-x^2}}=\arcsin x$.

## 2. Per partes a substituce

- **Per partes:** $\int fg=fG-\int f'G$ (z derivace součinu). Pro polynom·exp/sin.
- **Substituce I:** $\int f(\varphi(x))\varphi'(x)\,dx=F(\varphi(x))+C$ (subst. $y=\varphi(x)$); speciálně $\int\tfrac{\varphi'}{\varphi}=\ln|\varphi|$.
- **Substituce II:** $x=\varphi(t)$ bijekce, $\varphi'\neq0$ $\Rightarrow\int f(x)dx=G(\varphi^{-1}(x))+C$ (odmocniny).
- Racionální fce: dělení + parciální zlomky $\to\ln$, $\arctan$.

## 3. Riemannův určitý integrál ([[Riemannův-integrál]])

**Dělení** $\sigma$, **dolní/horní součet** $s=\sum\Delta_i\inf f$, $S=\sum\Delta_i\sup f$; **dolní/horní integrál** $\sup_\sigma s$, $\inf_\sigma S$.
$$\int_a^b f := \underline{\int}f=\overline{\int}f\in\mathbb{R}\ (\text{shoda}).$$
**Spojitá $f\Rightarrow$ existuje** $=\lim_n\mathcal{J}(\sigma_n,f)$ (normální posl. dělení). Neexistuje: Dirichletova fce.

**Vlastnosti:** linearita; aditivita v mezích $\int_a^b=\int_a^c+\int_c^b$; **monotonie** $f\le g\Rightarrow\int f\le\int g$.

**Newtonova formule:** $f$ spojitá, $F$ prim. $\Rightarrow\int_a^b f=F(b)-F(a)$ (důkaz: Lagrange na dělení). Per partes/substituce i pro $\int_a^b$.

**Geom. význam:** obsah mezi grafem a osou $x$ **se znaménkem** ($\int_0^\pi\sin=2$, $\int_\pi^{2\pi}\sin=-2$). Plocha mezi grafy: $\int_a^b(f-g)$ ($f\ge g$). **Nevlastní integrál:** $\int_a^\infty f=\lim_{c\to\infty}\int_a^c f$ (např. $\int_1^\infty\tfrac1{x^2}=1$); konv. ⟺ konečná limita.

## 4. Číselné řady ([[Číselná-řada]])

$\sum a_k$, částečný součet $s_n=\sum_{k=0}^n a_k$. **Konverguje** ⟺ $(s_n)$ konverg.; součet $=\lim s_n$. Geometrická $\sum q^k=\tfrac1{1-q}$ ($|q|<1$). **Abs. konv.** ($\sum|a_k|$ konv.) $\Rightarrow$ konv.

**Kritéria:**
| kritérium | tvrzení |
|---|---|
| nutná podmínka | konv. $\Rightarrow a_k\to0$ (nestačí! $\sum\tfrac1k$ div.) |
| Bolzano–Cauchy | konv. ⟺ $\forall\varepsilon\exists n_0:|a_n+\dots+a_{n+p}|<\varepsilon$ |
| srovnávací | $0\le|a_k|\le b_k$, $\sum b_k$ konv. $\Rightarrow\sum a_k$ abs. konv. |
| d'Alembert (podíl) | $a_k>0$: $\lim\tfrac{a_{k+1}}{a_k}<1$ konv., $>1$ div. |
| Leibniz | $(a_k)\searrow0$ $\Rightarrow\sum(-1)^k a_k$ konv. |
| integrální | $f$ spoj. monot., $f(n)=a_n>0$: $\sum a_n$ ⟺ $\int_1^\infty f$ |

## 5. Asymptotika součtů integrálem

**Věta:** $f$ spojitá na $\langle1,\infty)$,
$$f\searrow:\ f(n)+\int_1^n f\le\sum_{k=1}^n f(k)\le f(1)+\int_1^n f;\qquad f\nearrow:\ f(1)+\int_1^n f\le\sum\le f(n)+\int_1^n f.$$
(Důkaz: $f(k\!+\!1)\le\int_k^{k+1}f\le f(k)$, sečíst.) Z ní **integrální kritérium**.

**Výsledky:** $\sum_{k=1}^n\tfrac1k\sim\ln n$ (rozdíl $\to\gamma\approx0{,}577$); $\ln n!\approx n\ln n-n$ (Stirling $n!\sim\sqrt{2\pi n}\,(n/e)^n$); $\sum_{k=1}^n k^2\sim\tfrac13 n^3$. $\sum k^\alpha$ konv. ⟺ $\alpha<-1$.

---

## Co odpovědět rychle

- **Prim. fce** $F'=f$, jednoznačná až na $C$; **per partes** $\int fg=fG-\int f'G$, **substituce** $\int f(\varphi)\varphi'=F(\varphi)$.
- **Riemann:** dolní=horní integrál; spojitá $\Rightarrow$ existuje; **Newton** $\int_a^b f=F(b)-F(a)$.
- **Řady:** nutná $a_k\to0$; srovnávací / d'Alembert / Leibniz / integrální kritérium; abs.⇒konv.
- **Asymptotika:** $\sum f(k)$ sevři mezi $\int_1^n f$ + krajní člen; $\sum\tfrac1k\sim\ln n$, $\sum k^\alpha$ konv. ⟺ $\alpha<-1$.
