---
tags: [otázka, kurz/LA2, otázka/4, todo]
---

# 4 — LU rozklad a řešení soustav (zkrácená verze)

## 1. Definice

**[[LU-rozklad|LU rozklad]]** matice $A \in T^{n,n}$:
$$A = LU,$$
$L$ = dolní trojúhelníková **s jedničkami na diagonále**, $U$ = horní trojúhelníková.

**S pivotací:** $PA = LU$, $P$ permutační matice (prohazuje řádky). **Částečná pivotace:** $P$ volena tak, že $|\ell_{ij}| \le 1$.

**Existence:** LU rozklad existuje $\iff$ matici lze do HST převést jen úpravami (G3) „dolů“ (bez prohazování řádků). Silně regulární matice ho má. Regulární matice s LU rozkladem $\Rightarrow$ rozklad **jednoznačný**. Rozklad $PA = LU$ má **každá** čtvercová matice.

## 2. Výpočet (idea)

LU rozklad = „záznam“ [[Gaussova-eliminace|GEM]]. Matici převedeme GEM (jen G3 dolů) na HST $\to U$. **Multiplikátory** $\ell_{jk} = x_{jk}/x_{kk}$ (čím vynulujeme prvek pod diagonálou) zapisujeme **přímo na pozici $(j,k)$ do $L$**.

$$L = \begin{pmatrix} 1 & & \\ \ell_{21} & 1 & \\ \vdots & \ddots & \\ \ell_{n1} & \cdots & 1 \end{pmatrix}, \qquad \det A = \pm\prod_i u_{ii}.$$

**Složitost:** $\sim \tfrac{2}{3}n^3 = O(n^3)$ (jako jeden běh GEM).

## 3. Řešení $Ax = b$

$$Ax = b \iff LUx = b, \quad y := Ux \implies \begin{cases} Ly = b & \text{dopředná substituce (shora dolů)} \\ Ux = y & \text{zpětná substituce (zdola nahoru)} \end{cases}$$

Obě soustavy jsou trojúhelníkové, řeší se postupným dosazováním, každá $O(n^2)$.

**Výhoda:** faktorizaci $A=LU$ spočtu **jen jednou** ($O(n^3)$); pro každou další pravou stranu $b$ stačí 2 substituce v $O(n^2)$ (faktory na $b$ nezávisí). Opakovaná GEM by stála pokaždé $O(n^3)$.

S pivotací: $PAx = Pb \Rightarrow Ly = Pb$, $Ux = y$.

## 4. Proč pivotace

- **Nulový pivot:** $\left(\begin{smallmatrix} 0&1\\1&1 \end{smallmatrix}\right)$ nemá LU rozklad; po prohození řádků ano.
- **Numerická stabilita:** dělení **malým** pivotem $x_{kk}$ v $\ell_{jk}=x_{jk}/x_{kk}$ ztrácí přesnost (LU bez pivotace není zpětně stabilní). Částečná pivotace dá na diagonálu v abs. hodnotě největší prvek sloupce $\Rightarrow |\ell_{ij}| \le 1$.

---

## Co odpovědět rychle

- **Definice:** $A = LU$ ($L$ dolní s jedničkami na diag., $U$ horní); s pivotací $PA = LU$.
- **Výpočet:** GEM dolů, multiplikátory $\ell_{jk}=x_{jk}/x_{kk}$ do $L$; $O(n^3)$.
- **Řešení:** $Ly=b$ (dopředná) + $Ux=y$ (zpětná), každá $O(n^2)$.
- **Hlavní výhoda:** více pravých stran — faktorizace jednou, pak jen $O(n^2)$ na každé $b$.
- **Pivotace:** kvůli nulovému pivotu a stabilitě; $\det A = \pm\prod_i u_{ii}$.
