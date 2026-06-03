---
aliases: [svd, svd rozklad, svd rozkladu, singulární rozklad, singulárního rozkladu, singulární čísla, singulární hodnoty, singulární vektory, levé singulární vektory, pravé singulární vektory, pseudoinverze, eckartova-youngova věta]
tags: [definice, kurz/LA2]
---

# SVD

## Definice

**Singulární rozklad** (SVD, *singular value decomposition*) matice $A \in \mathbb{R}^{m,n}$ je její zápis jako součin
$$A = U \Sigma V^T,$$
kde

- $U \in \mathbb{R}^{m,m}$ je [[Ortogonální-matice|ortogonální]],
- $V \in \mathbb{R}^{n,n}$ je [[Ortogonální-matice|ortogonální]],
- $\Sigma \in \mathbb{R}^{m,n}$ je diagonální (tj. $\Sigma_{ij} = 0$ pro $i \neq j$) s nezápornou klesající diagonálou.

Na diagonále $\Sigma$ je $p := \min(m,n)$ čísel
$$\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_p \ge 0,$$
**singulárních čísel** matice $A$. Sloupce $U$ jsou **levé singulární vektory** $u_i$, sloupce $V$ jsou **pravé singulární vektory** $v_i$; platí $A v_i = \sigma_i u_i$.

**Existence:** každá matice $A \in \mathbb{R}^{m,n}$ má SVD rozklad.

## Plný vs. redukovaný tvar

- **Plný (úplný) SVD:** $U \in \mathbb{R}^{m,m}$, $V \in \mathbb{R}^{n,n}$ ortogonální, $\Sigma \in \mathbb{R}^{m,n}$.
- **Redukovaný (úsporný) SVD** pro $m \ge n$: $\hat U \in \mathbb{R}^{m,n}$ má ortonormální sloupce, $\hat\Sigma \in \mathbb{R}^{n,n}$ diagonální, $V \in \mathbb{R}^{n,n}$ ortogonální; $A = \hat U \hat\Sigma V^T$. Vznikne z plného odebráním nadbytečných sloupců $U$ a nulových řádků $\Sigma$.

## Vztah k vlastním číslům

Nenulová singulární čísla $A$ jsou odmocniny z nenulových [[Vlastní-číslo|vlastních čísel]] symetrické matice $A^T A$ (i $A A^T$):
$$\sigma_i = \sqrt{\lambda_i(A^T A)}.$$
$V$ je tvořeno ortonormální bází vlastních vektorů $A^T A$, $U$ ortonormální bází vlastních vektorů $A A^T$.

## Vlastnosti

- **Hodnost:** $h(A) = r$ = počet nenulových singulárních čísel (viz [[Hodnost-matice]]).
- **2-norma:** $\lVert A \rVert_2 = \sigma_1$; **Frobeniova norma:** $\lVert A \rVert_F = \sqrt{\sigma_1^2 + \cdots + \sigma_r^2}$ (viz [[Norma]]).
- $\langle$sloupce $A\rangle = \langle u_1, \dots, u_r\rangle$, $\ker A = \langle v_{r+1}, \dots, v_n\rangle$.

## Aproximace nízké hodnosti

$A = \sum_{j=1}^r \sigma_j u_j v_j^T$ (součet $r$ matic hodnosti 1). Ořezání na prvních $\nu$ členů,
$$A_\nu = \sum_{j=1}^\nu \sigma_j u_j v_j^T,$$
dává **nejlepší** aproximaci hodnosti $\le \nu$ v 2-normě i Frobeniově normě (**Eckartova–Youngova věta**): $\lVert A - A_\nu\rVert_2 = \sigma_{\nu+1}$.

## Pseudoinverze

Moore–Penroseova pseudoinverze $A^+ = V \Sigma^+ U^T$, kde $\Sigma^+$ vznikne invertováním nenulových singulárních čísel a transpozicí. Pro regulární $A$ je $A^+ = A^{-1} = V \Sigma^{-1} U^T$.

## Související

- [[Vlastní-číslo]]
- [[Spektrální-rozklad]]
- [[Ortogonální-matice]]
- [[Hodnost-matice]]
- [[Norma]]
- [[Metoda-nejmenších-čtverců]]
