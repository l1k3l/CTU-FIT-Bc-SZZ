---
tags: [otázka, kurz/LA2, otázka/1, todo]
---

# 1 — Lineární zobrazení a jeho matice (zkrácená verze)

## 1. Definice

$P, Q$ VP nad **stejným** tělesem $T$. Zobrazení $A:P\to Q$ je **[[Lineární-zobrazení|lineární]]** ($A\in\mathcal{L}(P,Q)$), právě když:
$$\text{(adit.) } A(x+y)=Ax+Ay, \qquad \text{(homog.) } A(\alpha x)=\alpha Ax.$$
Ekvivalentně $A(\alpha x+y)=\alpha Ax+Ay$, obecně $A\big(\sum_i\alpha_i x_i\big)=\sum_i\alpha_i Ax_i$.

**Speciální:** operátor $\mathcal{L}(P)=\mathcal{L}(P,P)$; funkcionál $P\to T$; **izomorfismus** = lineární bijekce.

## 2. Vlastnosti

Pro $A\in\mathcal{L}(P,Q)$:
- $A\theta_P=\theta_Q$;
- $A(\langle x_1,\dots,x_n\rangle)=\langle Ax_1,\dots,Ax_n\rangle$ (obraz obalu = obal obrazů);
- obraz podprostoru i vzor podprostoru je podprostor;
- obraz LZ souboru je LZ; vzor LN souboru (předobraz) je LN;
- $A$ je **jednoznačně určeno obrazy báze** $P$;
- složení i inverze (existuje-li) lin. zobrazení jsou lineární.

## 3. Jádro, obraz, hodnost, defekt

| pojem | definice |
|---|---|
| obor hodnot | $A(P)=\operatorname{Im}A \subset\subset Q$ |
| hodnost zobr. | $h(A)=\dim A(P)$ |
| jádro | $\ker A=\{x\mid Ax=\theta_Q\}=A^{-1}(\theta_Q)\subset\subset P$ |
| defekt | $d(A)=\dim\ker A$ |

*Pozor:* $h(A)$ (zobrazení) $\neq$ [[Hodnost-matice|hodnost matice]] — ale viz §6. Výpočet: jádro řešením $Ax=\theta$; obor hodnot $=\langle$obrazy báze$\rangle$.

## 4. Injektivita, surjektivita, izomorfismus

Pro $\dim P,\dim Q<\infty$:
$$A \text{ prosté} \iff \ker A=\{\theta_P\} \iff d(A)=0 \iff h(A)=\dim P,$$
$$A \text{ na} \iff A(P)=Q \iff h(A)=\dim Q.$$
Prosté zobrazení zachovává LN: $(x_i)$ LN $\iff (Ax_i)$ LN.

**Důsledek:** je-li $\dim P=\dim Q<\infty$, pak $A$ prosté $\iff$ $A$ na ($\iff$ izomorfismus).

## 5. Věta o dimenzi (rank-nullity)

$$\boxed{\,h(A)+d(A)=\dim P\,}$$

*Idea:* báze $P$ se složí z báze jádra ($k$ vektorů) a ze vzorů $z_i$ báze oboru hodnot ($\ell$ vektorů); soubor je LN a generuje $P$, tedy $\dim P=k+\ell=d(A)+h(A)$.

**Rovnice $Ax=b$:** existuje-li partikulární $\tilde x$, je $A^{-1}(b)=\tilde x+\ker A$ (lineární varieta). Pro $A x:=\mathbf{A}x$ je $S=\tilde x+S_0$, $S_0=\ker A$ → [[Soustava-lineárních-rovnic|SLR]], $\dim S_0=n-h(\mathbf{A})$.

## 6. Matice lineárního zobrazení

$\mathcal{X}=(x_1,\dots,x_n)$ báze $P$, $\mathcal{Y}$ báze $Q$ (konečná dim.). **[[Matice-lineárního-zobrazení|Matice zobrazení]]** ${}^{\mathcal{X}}A^{\mathcal{Y}}\in T^{m,n}$ po sloupcích:
$$\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)_{:i}=(Ax_i)_{\mathcal{Y}} \quad (i\text{-tý sloupec = souřadnice obrazu }i\text{-tého báz. vektoru}).$$

**Funguje:** $(Az)_{\mathcal{Y}}={}^{\mathcal{X}}A^{\mathcal{Y}}\cdot(z)_{\mathcal{X}}$. Vzor: $z$ vzor $w$ $\iff$ $(z)_{\mathcal{X}}$ řeší $\big({}^{\mathcal{X}}A^{\mathcal{Y}}\mid(w)_{\mathcal{Y}}\big)$; jádro = řešení $({}^{\mathcal{X}}A^{\mathcal{Y}}\mid\theta)$.

**Klíčové vztahy:**
- **hodnost:** $h(A)=h\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)$ (smiřuje oba pojmy hodnosti); $d(A)=\dim P-h$;
- **složení = součin:** ${}^{\mathcal{X}}(AB)^{\mathcal{W}}={}^{\mathcal{Y}}A^{\mathcal{W}}\cdot{}^{\mathcal{X}}B^{\mathcal{Y}}$;
- **izomorfismus:** ${}^{\mathcal{X}}A^{\mathcal{Y}}$ regulární, $\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)^{-1}={}^{\mathcal{Y}}(A^{-1})^{\mathcal{X}}$.

**Matice přechodu** ${}^{\mathcal{X}}E^{\mathcal{Y}}$ (matice identity): sloupce $=(x_i)_{\mathcal{Y}}$; ${}^{\mathcal{X}}E^{\mathcal{Y}}(x)_{\mathcal{X}}=(x)_{\mathcal{Y}}$, $\big({}^{\mathcal{X}}E^{\mathcal{Y}}\big)^{-1}={}^{\mathcal{Y}}E^{\mathcal{X}}$, ${}^{\mathcal{Y}}E^{\mathcal{Z}}\,{}^{\mathcal{X}}E^{\mathcal{Y}}={}^{\mathcal{X}}E^{\mathcal{Z}}$.

**Změna báze:** ${}^{\tilde{\mathcal{X}}}A^{\tilde{\mathcal{Y}}}={}^{\mathcal{Y}}E^{\tilde{\mathcal{Y}}}\cdot{}^{\mathcal{X}}A^{\mathcal{Y}}\cdot{}^{\tilde{\mathcal{X}}}E^{\mathcal{X}}$. (Operátor: matice v různých bázích jsou podobné.)

---

## Co odpovědět rychle

- **Linearita:** $A(\alpha x+\beta y)=\alpha Ax+\beta Ay$; $A\theta_P=\theta_Q$.
- **Jádro/defekt/hodnost:** $\ker A=A^{-1}(\theta_Q)$, $d(A)=\dim\ker A$, $h(A)=\dim A(P)$.
- **Rank-nullity:** $h(A)+d(A)=\dim P$.
- **Injektivita** $\iff \ker A=\{\theta_P\} \iff d(A)=0 \iff h(A)=\dim P$; **surjektivita** $\iff h(A)=\dim Q$.
- **Stejná dimenze:** prosté $\iff$ na $\iff$ izomorfismus.
- **Matice:** sloupce $=(Ax_i)_{\mathcal{Y}}$; $(Az)_{\mathcal{Y}}={}^{\mathcal{X}}A^{\mathcal{Y}}(z)_{\mathcal{X}}$; $h(A)=h({}^{\mathcal{X}}A^{\mathcal{Y}})$; složení = součin; změna báze přes matice přechodu.
