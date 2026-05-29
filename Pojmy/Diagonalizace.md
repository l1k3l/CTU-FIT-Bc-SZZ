---
aliases: [diagonalizace, diagonalizaci, diagonalizací, diagonalizace matice, diagonalizovatelná matice, diagonalizovatelná, diagonalizovatelnost, diagonalizovatelnosti, diagonalizovat, podobné matice, podobnost matic, podobnost]
tags: [definice, kurz/LA1]
---

# Diagonalizace

## Definice

Matice $A \in \mathbb{C}^{n,n}$ je **diagonalizovatelná**, je-li podobná diagonální matici, tj. existuje regulární $P$ a diagonální $D$ s
$$A = PDP^{-1} \qquad (D = P^{-1}AP).$$
**Podobnost matic:** $A, B$ jsou podobné, pokud $B = P^{-1}AP$ pro nějakou [[Regulární-matice|regulární]] $P$; podobné matice mají stejný charakteristický polynom, spektrum i násobnosti.

## Kritérium diagonalizovatelnosti

Pro $A \in \mathbb{C}^{n,n}$ jsou ekvivalentní:

1. $A$ je diagonalizovatelná;
2. existuje báze $\mathbb{C}^n$ tvořená [[Vlastní-číslo|vlastními vektory]] $A$;
3. součet geometrických násobností je $n$: $\sum_{\lambda \in \sigma(A)} \nu_g(\lambda) = n$;
4. pro každé vlastní číslo platí $\nu_g(\lambda) = \nu_a(\lambda)$.

**Postačující podmínka:** má-li $A$ $n$ navzájem **různých** vlastních čísel, je diagonalizovatelná (vlastní vektory k různým vlastním číslům jsou lineárně nezávislé).

## Konstrukce $P$ a $D$

Sloupce $P$ jsou vlastní vektory tvořící bázi; $D$ má na diagonále příslušná vlastní čísla **ve stejném pořadí** (každé tolikrát, kolik je jeho násobnost):
$$P = (x_1 \mid \cdots \mid x_n), \qquad D = \operatorname{diag}(\lambda_1, \dots, \lambda_n).$$

## Použití — mocniny

$$A^k = P D^k P^{-1}, \qquad D^k = \operatorname{diag}(\lambda_1^k, \dots, \lambda_n^k).$$

## Související

- [[Vlastní-číslo]]
- [[Regulární-matice]]
- [[Determinant]]
- [[Matice]]
