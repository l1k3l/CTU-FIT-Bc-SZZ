---
aliases: [regulární matice, regulární matici, regulární maticí, regulárních matic, regulární, regularita, regularitu, regularity, singulární matice, singulární, invertibilní matice]
tags: [definice, kurz/LA1]
---

# Regulární matice

## Definice

Čtvercová matice $A \in T^{n,n}$ je **regulární**, pokud k ní existuje [[Inverzní-matice|inverzní matice]], tj. matice $B \in T^{n,n}$ s
$$AB = BA = E.$$
Není-li $A$ regulární, je **singulární**. (Pojem je definován jen pro čtvercové matice.)

## Ekvivalentní charakterizace

Pro $A \in T^{n,n}$ jsou ekvivalentní:

1. $A$ je regulární (existuje $A^{-1}$);
2. $h(A) = n$ ([[Hodnost-matice|hodnost]] je plná);
3. $A \sim E$ (lze [[Gaussova-eliminace|GEM]] převést na jednotkovou matici);
4. řádky $A$ jsou lineárně nezávislé; rovněž sloupce $A$ jsou lineárně nezávislé;
5. $\det A \neq 0$ ([[Determinant]]);
6. homogenní soustava $Ax = \theta$ má jen triviální řešení;
7. pro každé $b$ má $Ax = b$ právě jedno řešení, a to $x = A^{-1}b$.

## Vlastnosti

- **Jednostranná inverze stačí:** existuje-li $B$ s $AB = E$ **nebo** $BA = E$, je $A$ regulární a $B = A^{-1}$.
- Součin regulárních matic je regulární: $(AB)^{-1} = B^{-1}A^{-1}$.
- $A^T$ je regulární a $(A^T)^{-1} = (A^{-1})^T$.
- Násobení regulární maticí nemění [[Hodnost-matice|hodnost]].

## Související

- [[Inverzní-matice]]
- [[Hodnost-matice]]
- [[Determinant]]
- [[Gaussova-eliminace]]
- [[Matice]]
- [[Soustava-lineárních-rovnic]]
