---
aliases: [LU rozklad, LU rozkladu, LU rozkladem, LU faktorizace, LU dekompozice, PLU rozklad, trojúhelníkový rozklad, dolní trojúhelníková matice, horní trojúhelníková matice]
tags: [definice, kurz/LA2]
---

# LU rozklad

## Definice

**LU rozklad** (LU faktorizace) matice $A \in T^{n,n}$ je její zapsání jako součin
$$A = LU,$$
kde $L \in T^{n,n}$ je **dolní trojúhelníková matice s jedničkami na diagonále** (z angl. *lower triangular*) a $U \in T^{n,n}$ je **horní trojúhelníková matice** (z angl. *upper triangular*). Matice $L$ a $U$ nazýváme **faktory**.

$$L = \begin{pmatrix} 1 & & & \\ \ell_{21} & 1 & & \\ \vdots & & \ddots & \\ \ell_{n1} & \ell_{n2} & \cdots & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} * & * & \cdots & * \\ & * & \cdots & * \\ & & \ddots & \vdots \\ & & & * \end{pmatrix}.$$

## Existence a jednoznačnost

- LU rozklad **neexistuje vždy** — např. $\left(\begin{smallmatrix} 0 & 1 \\ 1 & 1 \end{smallmatrix}\right)$ jej nemá.
- Matice má LU rozklad **právě tehdy, když ji lze převést do horního stupňovitého tvaru pouze úpravami (G3) „směrem dolů“** (přičtení násobku řádku k řádku s vyšším indexem) — tj. bez prohození řádků.
- Je-li matice [[Regulární-matice|regulární]] a má LU rozklad, pak je tento rozklad **jednoznačný**.

## LU rozklad s pivotací (PLU)

Aby šel rozklad spočítat i tehdy, kdy je nutné prohazovat řádky (nulový pivot, numerická nestabilita), zavádí se
$$PA = LU,$$
kde $P$ je **permutační matice** (prohazuje pořadí řádků). Každá čtvercová matice má rozklad $PA = LU$ s vhodným $P$. U **částečné pivotace** se navíc volí $P$ tak, aby $|\ell_{ij}| \le 1$ (v každém kroku se na diagonálu dostane v absolutní hodnotě největší prvek sloupce).

## Výpočet

LU rozklad je v podstatě „záznam“ [[Gaussova-eliminace|Gaussovy eliminace]]: matici $A$ převedeme GEM (jen úpravy G3 dolů) do horního stupňovitého tvaru $U$; **multiplikátory** $\ell_{jk} = x_{jk}/x_{kk}$ použité při vynulování prvků pod diagonálou se ukládají přímo na příslušná místa do $L$. Faktorizace stojí $\sim \tfrac{2}{3}n^3$ aritmetických operací, tedy $O(n^3)$.

## Použití — řešení soustav

Hlavní využití je řešení [[Soustava-lineárních-rovnic|soustavy lineárních rovnic]] $Ax = b$: z $LUx = b$ označíme $y = Ux$ a řešíme dvě snadné trojúhelníkové soustavy
$$Ly = b \ (\text{dopředná substituce}), \qquad Ux = y \ (\text{zpětná substituce}),$$
každou v $O(n^2)$. Výhoda: faktorizaci $O(n^3)$ spočítáme jen **jednou** a pro každou další pravou stranu $b$ stačí už jen dvě substituce v $O(n^2)$.

## Determinant

Z $A = LU$ (resp. $PA = LU$) a $\det L = 1$ plyne
$$\det A = \pm \prod_{i=1}^{n} u_{ii},$$
kde znaménko je $\det P^{-1} = (-1)^{\#\text{prohození řádků}}$ (bez pivotace $+$). Viz [[Determinant]].

## Související

- [[Gaussova-eliminace]]
- [[Soustava-lineárních-rovnic]]
- [[Determinant]]
- [[Regulární-matice]]
- [[Matice]]
