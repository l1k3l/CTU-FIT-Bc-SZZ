---
aliases: [lineární varieta, lineární variety, lineární varietu, lineární varietě, varieta, variety, varietu, afinní podprostor, afinního podprostoru, zaměření variety, zaměření]
tags: [definice, kurz/LA1]
---

# Lineární varieta

## Definice

Množina $W \subseteq T^n$ je **lineární varieta** (afinní podprostor), pokud existuje vektor $a \in T^n$ a podprostor $P \subseteq T^n$ takové, že
$$W = a + P = \{a + p \mid p \in P\}.$$
Podprostor $P$ se nazývá **zaměření** variety, značíme $Z(W)$; $a$ je **vektor posunutí**; $\dim W := \dim Z(W)$.

## Vlastnosti

- Vektor posunutí leží ve varietě a **každý** prvek variety lze vzít za vektor posunutí: pro $b \in W$ je $W = b + Z(W)$.
- **Zaměření je jednoznačné:** $a + P = b + Q \iff P = Q \ \wedge\ b - a \in P$.
- Každý podprostor je varieta ($P = \theta + P$); obecná varieta nemusí obsahovat počátek (posunuté přímky, roviny…).

## Souvislost se soustavami rovnic

Množina řešení **řešitelné** [[Soustava-lineárních-rovnic|soustavy]] $Ax = b$ je lineární varieta
$$S = \tilde{x} + S_0$$
se zaměřením $Z(S) = S_0$ (řešení přidružené homogenní soustavy) a dimenzí $\dim S = n - h(A)$ ([[Frobeniova-věta]]).

## Související

- [[Soustava-lineárních-rovnic]]
- [[Frobeniova-věta]]
- [[Hodnost-matice]]
