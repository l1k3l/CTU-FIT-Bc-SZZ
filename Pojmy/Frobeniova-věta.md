---
aliases: [Frobeniova věta, Frobeniovy věty, Frobeniově větě, Frobeniovu větu, Frobeniova, Frobenius, Rouché–Capelli, Rouché-Capelli, Kroneckerova-Capelliho věta]
tags: [věta, kurz/LA1]
---

# Frobeniova věta

## Znění

Nechť $A \in T^{m,n}$, $b \in T^m$. Pro soustavu $Ax = b$ platí:

1. **Řešitelnost:** soustava má řešení ($S \neq \emptyset$) **právě tehdy, když**
$$h(A) = h(A \mid b),$$
tj. [[Hodnost-matice|hodnost]] matice soustavy se rovná hodnosti rozšířené matice.
2. **Struktura:** je-li $\tilde{x}$ libovolné řešení, pak $S = \tilde{x} + S_0$, kde $S_0$ je množina řešení přidružené homogenní soustavy.
3. **Dimenze:** $S_0$ je podprostor dimenze $n - h(A)$.

(Mezinárodně Rouché–Capelliho věta.)

## Důsledky — počet řešení

Pro $n$ neznámých a $h := h(A)$:

| podmínka | počet řešení |
|---|---|
| $h(A) < h(A\mid b)$ | žádné ($S = \emptyset$) |
| $h(A) = h(A\mid b) = n$ | právě jedno ($S_0 = \{\theta\}$) |
| $h(A) = h(A\mid b) < n$ | nekonečně mnoho ($\dim S_0 = n - h > 0$) |

Počet **volných parametrů** řešení je $n - h(A)$.

## Idea důkazu (bod 1)

$Ax = b$ je řešitelná $\iff b$ leží v lineárním obalu sloupců $A$ (neboť $Ax = \sum_j x_j A_{:j}$) $\iff$ přidání sloupce $b$ nezvětší dimenzi obalu sloupců $\iff h(A) = h(A\mid b)$.

## Související

- [[Soustava-lineárních-rovnic]]
- [[Hodnost-matice]]
- [[Lineární-varieta]]
- [[Gaussova-eliminace]]
- [[Regulární-matice]]
