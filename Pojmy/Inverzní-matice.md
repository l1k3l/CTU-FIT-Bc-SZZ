---
aliases: [inverzní matice, inverzní matici, inverzní maticí, inverzní matic, inverze matice, inverze, maticová inverze, inverzní]
tags: [definice, kurz/LA1]
---

# Inverzní matice

## Definice

K čtvercové matici $A \in T^{n,n}$ je **inverzní maticí** matice $B \in T^{n,n}$ splňující
$$AB = BA = E.$$
Značíme $B = A^{-1}$. Matice, k níž inverze existuje, je [[Regulární-matice|regulární]].

**Jednoznačnost:** je-li $A$ regulární, je $A^{-1}$ určena jednoznačně (kdyby $B_1, B_2$ obě byly inverzní, pak $B_1 = B_1 E = B_1(AB_2) = (B_1 A)B_2 = E B_2 = B_2$).

## Vlastnosti

- $(A^{-1})^{-1} = A$;
- $(AB)^{-1} = B^{-1}A^{-1}$ (pozor na pořadí);
- $(A^T)^{-1} = (A^{-1})^T$;
- $\det(A^{-1}) = (\det A)^{-1}$.

## Výpočet — Gaussovou eliminací

K matici $A$ připíšeme jednotkovou matici a [[Gaussova-eliminace|GEM]] (Gaussovou–Jordanovou eliminací) převedeme levý blok na $E$:
$$(A \mid E) \;\sim\; (E \mid A^{-1}).$$
Pravý blok je hledaná $A^{-1}$. **Vznikne-li v levém bloku nulový řádek** (nelze dosáhnout $E$), je $A$ singulární a inverze neexistuje. Funguje, protože každou posloupnost úprav GEM realizuje regulární matice $P$ (zleva): z $PA = E$ plyne $P = A^{-1}$, a tytéž úpravy převedou $E$ na $PE = A^{-1}$.

Řešení soustavy s regulární maticí: $x = A^{-1}b$.

## Související

- [[Regulární-matice]]
- [[Gaussova-eliminace]]
- [[Determinant]]
- [[Matice]]
