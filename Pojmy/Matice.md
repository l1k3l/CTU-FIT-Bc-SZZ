---
aliases: [matice, matici, maticí, matic, maticím, maticemi, maticích, matice typu, čtvercová matice, jednotková matice, nulová matice, diagonální matice, transpozice, transponovaná matice, součin matic]
tags: [definice, kurz/LA1]
---

# Matice

## Definice

Nechť $m, n \in \mathbb{N}$ a $T$ je těleso (např. $\mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{Z}_p$). **Matice typu (rozměru) $m \times n$** nad $T$ je uspořádaný soubor $mn$ prvků z $T$ zapsaný do tabulky o $m$ řádcích a $n$ sloupcích:
$$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}, \qquad a_{ij} \in T.$$
Množinu všech matic typu $m \times n$ značíme $T^{m,n}$. Prvek $a_{ij} = (A)_{ij}$ je **$ij$-tý prvek** (první index = řádek, druhý = sloupec). $j$-tý sloupec značíme $A_{:j} \in T^{m,1}$, $i$-tý řádek $A_{i:} \in T^{1,n}$. Dvě matice se rovnají, právě když jsou stejného typu a mají shodné všechny odpovídající prvky.

## Speciální matice

- **Čtvercová matice:** typu $n \times n$.
- **Nulová matice** $\Theta \in T^{m,n}$: všechny prvky jsou nuly (nulový vektor $\theta$).
- **Jednotková matice** $E_n \in T^{n,n}$ (mezinárodně $I_n$): $e_{ij} = 1$ pro $i = j$, jinak $0$.
- **Diagonální matice:** čtvercová s $a_{ij} = 0$ pro $i \neq j$. **Diagonála** je $(a_{11}, \dots, a_{nn})$.
- **Transpozice** $A^T \in T^{n,m}$: $(A^T)_{ji} = a_{ij}$ (řádky $\to$ sloupce). Platí $(A^T)^T = A$.
- **Symetrická matice:** $A = A^T$.

## Operace

Násobení skalárem a sčítání jsou **po složkách** (jen pro stejný typ): $(\alpha A)_{ij} = \alpha a_{ij}$, $(A+B)_{ij} = a_{ij} + b_{ij}$. Sčítání je komutativní a asociativní, platí distributivita $\alpha(A+B) = \alpha A + \alpha B$, $(\alpha+\beta)A = \alpha A + \beta A$.

## Součin matic

Pro $A \in T^{m,n}$, $B \in T^{n,p}$ je **součin** $AB \in T^{m,p}$ definován vztahem
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}.$$
Nutná podmínka: počet sloupců $A$ = počet řádků $B$.

**Vlastnosti:**
- **asociativita** $A(BC) = (AB)C$;
- **distributivita** $A(B+C) = AB + AC$, $(A+B)C = AC + BC$;
- $\alpha(AB) = (\alpha A)B = A(\alpha B)$;
- $(AB)^T = B^T A^T$;
- **jednotková matice je neutrální:** $AE_n = A = E_m A$;
- **NENÍ komutativní:** obecně $AB \neq BA$ (i pro čtvercové matice).

Pro čtvercovou $A$ definujeme mocninu $A^k = \underbrace{A \cdots A}_{k\times}$.

## Související

- [[Soustava-lineárních-rovnic]]
- [[Hodnost-matice]]
- [[Regulární-matice]]
- [[Inverzní-matice]]
- [[Determinant]]
- [[Vlastní-číslo]]
- [[Matice-sousednosti]]
