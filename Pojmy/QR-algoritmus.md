---
aliases: [qr algoritmus, qr algoritmu, qr algoritmem, qr iterace, schurova forma, schurův rozklad, hessenbergův tvar, hessenbergova tvaru, tridiagonální matice]
tags: [definice, kurz/LA2]
---

# QR algoritmus

## Definice

**QR algoritmus** je iterační, numericky stabilní metoda pro výpočet **všech** [[Vlastní-číslo|vlastních čísel]] čtvercové matice $A \in \mathbb{R}^{n,n}$. V každém kroku spočte [[QR-rozklad]] aktuální matice a vynásobí faktory v opačném pořadí:
$$A^{(0)} = A, \qquad A^{(k-1)} = Q^{(k)} R^{(k)}, \qquad A^{(k)} = R^{(k)} Q^{(k)}.$$
Tedy „spočti $A = QR$, vrať $RQ$".

## Zachování spektra

Každá $A^{(k)}$ je **podobná** $A$, tedy má stejná vlastní čísla. Pro jeden krok platí $R^{(k)} = (Q^{(k)})^T A^{(k-1)}$, takže
$$A^{(k)} = R^{(k)} Q^{(k)} = (Q^{(k)})^T A^{(k-1)} Q^{(k)} = (Q^{(k)})^{-1} A^{(k-1)} Q^{(k)},$$
což je transformace podobnosti ([[Ortogonální-matice|ortogonální]] $Q$, tedy $Q^{-1} = Q^T$).

## Konvergence

Za vhodných předpokladů (vlastní čísla jednoduchá v absolutní hodnotě $|\lambda_1| > |\lambda_2| > \dots$) posloupnost $A^{(k)}$ konverguje:

- **symetrická matice** → diagonální matice; vlastní čísla pak leží na diagonále;
- **nesymetrická matice** → (blokově) horní trojúhelníková matice, tzv. **Schurova forma** $A = QRQ^T$ ($Q$ ortogonální, $R$ horní trojúhelníková); vlastní čísla jsou na diagonále.

Limitní matice $B$ je podobná $A$, takže její diagonální prvky jsou vlastní čísla $A$.

## Příprava matice (Hessenbergův / třídiagonální tvar)

V základní podobě je QR algoritmus drahý ($O(n^3)$ na iteraci). Matici proto nejprve převedeme **podobností** (ortogonálními Householderovými reflexemi aplikovanými oboustranně, $B = QAQ^T$) na **Hessenbergův tvar** (nuly pod poddiagonálou: $j+1 < i \Rightarrow a_{ij} = 0$). Pro symetrické matice vznikne **třídiagonální** matice ($|i-j|>1 \Rightarrow a_{ij}=0$). Na tomto tvaru je každá QR iterace výrazně levnější a tvar se zachovává.

## Související

- [[QR-rozklad]]
- [[Vlastní-číslo]]
- [[Mocninná-metoda]]
- [[Spektrální-rozklad]]
- [[Ortogonální-matice]]
