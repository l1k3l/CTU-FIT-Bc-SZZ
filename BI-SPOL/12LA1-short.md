---
tags: [otázka, kurz/LA1, otázka/12, todo]
---

# 12 — Matice (zkrácená verze)

## 1. Matice a součin

[[Matice]] $A = (a_{ij}) \in T^{m,n}$. Transpozice $(A^T)_{ji} = a_{ij}$. Sčítání a $\times$ skalárem po složkách.

**Součin** ($A \in T^{m,n}$, $B \in T^{n,p}$, sloupce $A$ = řádky $B$):
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj} \in T^{m,p}.$$
Vlastnosti: asociativní, distributivní, $(AB)^T = B^TA^T$, $AE = A = EA$. **Nekomutativní** ($AB \neq BA$).

## 2. Regulární matice

$A \in T^{n,n}$ **[[Regulární-matice|regulární]]** $\iff$ existuje inverze ($AB = BA = E$). Ekvivalentně:
$$\text{reg.} \iff h(A) = n \iff A \sim E \iff \det A \neq 0 \iff Ax=\theta \text{ jen } x=\theta \iff \text{řádky/sloupce LN}.$$
Jinak **singulární**. Jednostranná inverze stačí ($AB=E$ nebo $BA=E$ ⇒ reg., $B=A^{-1}$).

## 3. Inverzní matice

**[[Inverzní-matice]]** $A^{-1}$: $AA^{-1} = A^{-1}A = E$, **jednoznačná**.
Vlastnosti: $(A^{-1})^{-1}=A$, $(AB)^{-1} = B^{-1}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$, $\det A^{-1} = (\det A)^{-1}$.

**Výpočet (Gauss–Jordan):** $(A \mid E) \sim (E \mid A^{-1})$. Nulový řádek vlevo ⇒ singulární. $O(n^3)$.

## 4. Vlastní čísla

**[[Vlastní-číslo]]:** $\lambda \in \mathbb{C}$, $\exists x \neq \theta$: $Ax = \lambda x$. Spektrum $\sigma(A)$. Vlastní podprostor $\ker(A - \lambda E)$.

**Charakteristický polynom** $p_A(\lambda) = \det(A - \lambda E)$, stupně $n$:
$$\lambda \in \sigma(A) \iff p_A(\lambda) = 0.$$
Nad $\mathbb{C}$ vždy $\exists$ vlastní číslo, $\sum \nu_a = n$.

**Násobnosti:** $\nu_a$ = násobnost kořene $p_A$; $\nu_g = \dim\ker(A-\lambda E) = n - h(A-\lambda E)$; vždy $1 \le \nu_g \le \nu_a \le n$.

**Výpočet:** kořeny $p_A$ = vlastní čísla; vlastní vektory = řešení $(A - \lambda E)x = \theta$.

**Podobnost:** $A = P^{-1}BP$ ⇒ stejný $p_A$, spektrum, násobnosti, $\det$.

## 5. Diagonalizace

**[[Diagonalizace|Diagonalizovatelná]]:** $A = PDP^{-1}$, $D$ diagonální. Ekvivalentně:
$$\iff \text{báze z vlastních vektorů} \iff \textstyle\sum_\lambda \nu_g(\lambda) = n \iff \nu_g(\lambda) = \nu_a(\lambda)\ \forall\lambda.$$
$n$ **různých** vlastních čísel ⇒ diagonalizovatelná (vl. vektory k různým $\lambda$ jsou LN).

**Konstrukce:** $P = (x_1 \mid \cdots \mid x_n)$ vlastní vektory, $D = \operatorname{diag}(\lambda_1,\dots,\lambda_n)$ ve stejném pořadí.

**Mocnina:** $A^k = P D^k P^{-1}$, $D^k = \operatorname{diag}(\lambda_i^k)$.

---

## Co odpovědět rychle

- **Součin** $(AB)_{ij} = \sum_k a_{ik}b_{kj}$; asociativní, $(AB)^T = B^TA^T$, **nekomutativní**.
- **Regulární** $\iff h(A)=n \iff \det A \neq 0 \iff A^{-1}$ existuje.
- **Inverze:** $(A\mid E) \sim (E \mid A^{-1})$; $(AB)^{-1}=B^{-1}A^{-1}$.
- **Vlastní číslo:** $Ax=\lambda x$, $x\neq\theta$; $\lambda \iff \det(A-\lambda E)=0$. $\nu_g \le \nu_a$.
- **Diagonalizace:** $A=PDP^{-1}$, $P$ = vl. vektory, $D$ = vl. čísla; $\iff \nu_g=\nu_a\ \forall\lambda$; $A^k = PD^kP^{-1}$.
