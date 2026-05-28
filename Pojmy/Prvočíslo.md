---
aliases: [prvočíslo, prvočísla, prvočísel, prvočíslu, prvočíslem, prvočíslech, prvočíselný, prvočíselná, prvočíselné, prvočíselnou, složené číslo, složeného čísla]
tags: [definice, kurz/DML]
---

# Prvočíslo

## Definice

Přirozená čísla $\mathbb{N}$ se podle počtu dělitelů dělí do tří tříd:

1. **Číslo 1** — má právě jednoho dělitele (sebe).
2. **Prvočísla** — mají právě dva dělitele: sebe a číslo 1.
3. **Složená čísla** — mají více než dva dělitele.

## Nekonečnost prvočísel

**Věta (Eukleides):** Existuje nekonečně mnoho prvočísel.

**Důkaz sporem.** Předpokládejme konečnou množinu $\{p_1, \dots, p_k\}$ všech prvočísel. Položme $P = p_1 p_2 \cdots p_k + 1$. Pak $P > 1$, a tedy:
- Buď je $P$ prvočíslo — spor (chybí v seznamu).
- Nebo je $P$ složené a dělí jej některé $p_j$. Ale z $P = p_1 \cdots p_k + 1$ plyne $p_j \mid 1$, což je spor.

## Eukleidovo lemma

**Lemma:** Buď $p$ prvočíslo.
1. $p \mid (ab) \land p \nmid a \Rightarrow p \mid b$.
2. $p \mid (a_1 \cdots a_k) \Rightarrow \exists j: p \mid a_j$.

## Základní věta aritmetiky

**Věta:** Každé $n \in \mathbb{N}$, $n \geq 2$, se dá **jednoznačně** vyjádřit jako součin
$$n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k},$$
kde $p_1 < p_2 < \cdots < p_k$ jsou prvočísla a $\alpha_i \in \mathbb{N}$. Tento zápis = **kanonický (prvočíselný) rozklad** / **faktorizace** $n$.

## Související

- [[Dělitelnost]]
- [[Eukleidův-algoritmus]]
- [[Kongruence]]
- [[Eulerova-funkce]]
