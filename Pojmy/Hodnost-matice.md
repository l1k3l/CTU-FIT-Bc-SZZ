---
aliases: [hodnost matice, hodnosti matice, hodnost, hodnosti, hodností, rank]
tags: [definice, kurz/LA1]
---

# Hodnost matice

## Definice

**Hodnost matice** $A \in T^{m,n}$, značená $h(A)$ (mezinárodně $\operatorname{rank} A$), je dimenze lineárního obalu souboru jejích řádků (chápaných jako vektory z $T^n$):
$$h(A) := \dim \big\langle (A_{1:})^T, \dots, (A_{m:})^T \big\rangle.$$

## Vlastnosti

- $0 \le h(A) \le \min(m, n)$.
- **Hodnost řádků = hodnost sloupců:** $h(A) = h(A^T)$.
- [[Gaussova-eliminace|GEM]] hodnost **nemění**: je-li $A \sim B$, pak $h(A) = h(B)$.
- Pro matici v **horním stupňovitém tvaru** je $h(A)$ = počet nenulových řádků = počet pivotů.
- $h(AB) \le \min\{h(A), h(B)\}$.
- Násobení **regulární** maticí hodnost nezmění: $h(PA) = h(A) = h(AQ)$ pro regulární $P, Q$.

## Výpočet

Matici převedeme GEM do HST; hodnost = počet nenulových řádků.

## Použití

- kritérium řešitelnosti soustav ([[Frobeniova-věta]]): $Ax=b$ řešitelná $\iff h(A) = h(A\mid b)$;
- charakterizace [[Regulární-matice|regularity]]: $A \in T^{n,n}$ regulární $\iff h(A) = n$;
- dimenze lineárního obalu vektorů, test příslušnosti vektoru do obalu.

## Související

- [[Gaussova-eliminace]]
- [[Frobeniova-věta]]
- [[Regulární-matice]]
- [[Matice]]
