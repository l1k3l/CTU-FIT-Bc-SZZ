---
tags: [otázka, kurz/LA1, otázka/11, todo]
---

# 11 — Soustavy lineárních rovnic (zkrácená verze)

## 1. Soustava lineárních rovnic

$$Ax = b, \quad A \in T^{m,n},\ x \in T^n,\ b \in T^m, \qquad (Ax)_i = \sum_j a_{ij}x_j.$$

Rozšířená matice $(A \mid b)$. **Homogenní:** $b = \theta$ (přidružená homogenní soustava $Ax = \theta$, řešení $S_0$). Množina řešení soustavy $S$.

## 2. Hodnost matice + Frobeniova věta

**Hodnost** $h(A) = \dim \langle \text{řádky } A \rangle$ = počet pivotů v HST. Platí $h(A) = h(A^T)$, $h(A) \le \min(m,n)$.

**[[Frobeniova-věta]]:** $Ax=b$ řešitelná $\iff h(A) = h(A\mid b)$. Pak $S = \tilde{x} + S_0$ a $\dim S_0 = n - h(A)$.

**Počet řešení** ($n$ neznámých):

| | |
|---|---|
| $h(A) < h(A\mid b)$ | žádné |
| $h(A) = h(A\mid b) = n$ | jedno |
| $h(A) = h(A\mid b) < n$ | $\infty$ (nad $\mathbb{R}$); $n-h$ parametrů |

Regulární $A$ ($h=n$): jediné řešení $x = A^{-1}b$.

## 3. Popis množiny řešení

$S_0$ je **podprostor** $T^n$ ($\theta \in S_0$, uzavřený na $+$ a násobek), $\dim S_0 = n - h(A)$.

**Struktura:** $S = \tilde{x} + S_0$ — partikulární řešení $+$ řešení homogenní soustavy. (Stačí jedno $\tilde{x}$ a báze $S_0$.) Nad $\mathbb{R}$: aspoň 2 řešení $\Rightarrow$ nekonečně.

**[[Lineární-varieta]]:** $S = \tilde{x} + S_0$ je varieta se zaměřením $S_0$, $\dim S = n - h(A)$. Operace = **vektor $+$ podprostor**: $\tilde{x}+S_0 = \{\tilde{x}+z : z\in S_0\}$ ($\tilde{x}$ posune $S_0$; není to podprostor).

## 4. Gaussova eliminace (GEM)

**Úpravy** (nemění $S$ ani $h$): (G1) prohození řádků, (G2) $\times$ nenulové číslo, (G3) přičtení násobku řádku.

**HST** (horní stupňovitý tvar): nulové řádky dole, indexy pivotů rostou $j_1 < \cdots < j_k$. Hlavní sloupce (vázané prom.) / vedlejší (volné prom.).

**Algoritmus:** zleva najdi pivot, prohozením dej nahoru, (G3) vynuluj pod pivotem, opakuj. $O(n^3)$. (Gauss–Jordan navíc nuluje nad pivoty → rHST.)

Každá úprava = **násobení regulární maticí zleva** ($PA$, $P$ reg.) → proto nemění hodnost ani $S$.

**Čtení řešitelnosti z HST $(A\mid b)$:** poslední sloupec hlavní → bez řešení; jediný vedlejší → jedno; více vedlejších → $\infty$.

**Popis řešení:**
1. partikulární $\tilde{x}$: volné prom. $= 0$, dopočti vázané z $(A\mid b)$;
2. báze $S_0$: v $(A\mid \theta)$ dej jednu volnou prom. $=1$, ostatní $0$, dopočti → $n-h$ vektorů;
3. $S = \tilde{x} + \langle z_1,\dots,z_{n-h}\rangle$. (Pozor: $S_0$ z pravé strany $\theta$!)

---

## Co odpovědět rychle

- **Frobenius:** řešitelná $\iff h(A) = h(A\mid b)$; pak $\dim S_0 = n - h(A)$.
- **Struktura:** $S = \tilde{x} + S_0$ (partikulární + homogenní), $S_0$ podprostor.
- **Počet řešení:** $0$ / $1$ / $\infty$ podle $h(A)$, $h(A\mid b)$, $n$.
- **GEM:** úpravy (G1)–(G3) nemění množinu řešení ani hodnost; převod na HST, $O(n^3)$.
- **Geometrie:** množina řešení = lineární varieta dimenze $n - h(A)$ (vektor $+$ podprostor).
- **Jinak než GEM** (regulární $A$): $x = A^{-1}b$; **Cramer** $x_i = \det A_i / \det A$ ($A_i$ = $A$ s $i$-tým sloupcem nahrazeným $b$).
- **Související pojmy** (umět definovat): lin. kombinace → lin. (ne)závislost → báze → dimenze → hodnost; podprostor, HST, varieta.
