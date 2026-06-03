---
aliases: [metoda nejmenších čtverců, metodou nejmenších čtverců, metody nejmenších čtverců, nejmenší čtverce, MNČ, OLS, normální rovnice, ortogonální projekce]
tags: [definice, kurz/LA2]
---

# Metoda nejmenších čtverců

## Definice

Pro **přeurčenou** soustavu $Ax = b$ s $A \in \mathbb{R}^{m,n}$, $b \in \mathbb{R}^m$ (typicky $m > n$, soustava nemá řešení) hledáme vektor $x \in \mathbb{R}^n$, který minimalizuje **eukleidovskou [[Norma|normu]] rezidua**:
$$x \text{ je řešení ve smyslu nejmenších čtverců} \iff \|b - Ax\|_2 = \min_{y \in \mathbb{R}^n} \|b - Ay\|_2.$$
Tedy $Ax$ je nejblíže $b$, jak jen to jde. Anglicky **ordinary least squares (OLS)**; v statistice/ML jde o **lineární regresi**.

## Normální rovnice

$x$ je řešením ve smyslu nejmenších čtverců **právě tehdy, když** splňuje **normální rovnice**
$$A^T A\, x = A^T b.$$
Soustava (12.34) $Ax = \operatorname{proj}_{\operatorname{Im}A} b$ je vždy řešitelná, takže řešení MNČ vždy existuje. Je-li $h(A) = n$ (sloupce LN), je $A^TA$ regulární a řešení je **jediné**:
$$x = (A^T A)^{-1} A^T b.$$

## Geometrická interpretace

Minimalizace $\|b - Ax\|$ znamená hledat v podprostoru $\operatorname{Im}A = \langle A_{:1},\dots,A_{:n}\rangle$ (sloupcový prostor) vektor nejbližší $b$ — to je **ortogonální projekce** $b$ na $\operatorname{Im}A$:
$$Ax = \operatorname{proj}_{\operatorname{Im}A} b.$$
**Reziduum** $b - Ax = \operatorname{proj}_{(\operatorname{Im}A)^\perp} b$ je tedy **kolmé na každý sloupec** $A$, tj. $A^T(b - Ax) = \theta$ — odtud přímo plynou normální rovnice.

## Řešení pomocí QR

Inverze $(A^TA)^{-1}$ je numericky nestabilní (číslo podmíněnosti $A^TA$ je druhou mocninou podmíněnosti $A$). Místo toho použijeme **[[QR-rozklad]]** $A = \hat{Q}\hat{R}$:
$$\hat{R}\,x = \hat{Q}^T b \quad \text{(zpětná substituce)}.$$
Plyne z $\operatorname{proj}_{\operatorname{Im}A}b = \hat{Q}\hat{Q}^T b$ a $Ax = \hat{Q}\hat{R}x$. Tato cesta je výrazně **numericky stabilnější** než normální rovnice. (Pro nejhůře podmíněné úlohy lze použít [[SVD]].)

## Související

- [[Lineární-regrese]] (statistické/ML použití MNČ)
- [[QR-rozklad]]
- [[Soustava-lineárních-rovnic]]
- [[Ortogonální-báze]]
- [[SVD]]
