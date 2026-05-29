---
aliases: [vlastní číslo, vlastního čísla, vlastním číslem, vlastní čísla, vlastních čísel, vlastní vektor, vlastního vektoru, vlastní vektory, vlastních vektorů, spektrum, spektra, vlastní podprostor, charakteristický polynom, charakteristického polynomu, eigenvalue, eigenvector]
tags: [definice, kurz/LA1]
---

# Vlastní číslo

## Definice

Číslo $\lambda \in \mathbb{C}$ je **vlastní číslo** matice $A \in \mathbb{C}^{n,n}$, právě když existuje **nenulový** vektor $x \in \mathbb{C}^n$ s
$$A x = \lambda x.$$
Takový $x$ je **vlastní vektor** příslušející $\lambda$. (Nenulovost $x$ je nutná — jinak by každé $\lambda$ vyhovovalo.) Množina všech vlastních čísel je **spektrum** $\sigma(A)$.

**Vlastní podprostor** příslušející $\lambda$ je podprostor řešení homogenní soustavy
$$(A - \lambda E)x = \theta, \qquad \text{tj. } \ker(A - \lambda E).$$

## Charakteristický polynom

$$p_A(\lambda) := \det(A - \lambda E)$$
je polynom stupně $n$. Platí
$$\lambda \in \sigma(A) \iff p_A(\lambda) = 0,$$
neboť $A - \lambda E$ musí být singulární (jinak by $(A-\lambda E)x = \theta$ mělo jen nulové řešení). Každá komplexní matice má aspoň jedno vlastní číslo (základní věta algebry); součet algebraických násobností je $n$.

## Násobnosti

- **Algebraická násobnost** $\nu_a(\lambda)$ = násobnost $\lambda$ jako kořene $p_A$;
- **geometrická násobnost** $\nu_g(\lambda)$ = dimenze vlastního podprostoru ($= n - h(A - \lambda E)$);
- vždy $1 \le \nu_g(\lambda) \le \nu_a(\lambda) \le n$.

## Výpočet

1. sestav $p_A(\lambda) = \det(A - \lambda E)$;
2. kořeny $p_A$ jsou vlastní čísla (jejich násobnost = $\nu_a$);
3. pro každé $\lambda$ vyřeš $(A - \lambda E)x = \theta$ — nenulová řešení jsou vlastní vektory, $\nu_g = $ dimenze řešení.

## Související

- [[Diagonalizace]]
- [[Determinant]]
- [[Soustava-lineárních-rovnic]]
- [[Matice]]
