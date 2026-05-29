---
aliases: [soustava lineárních rovnic, soustavy lineárních rovnic, soustavu lineárních rovnic, soustavě lineárních rovnic, soustav lineárních rovnic, SLR, soustava rovnic, homogenní soustava, nehomogenní soustava, rozšířená matice soustavy]
tags: [definice, kurz/LA1]
---

# Soustava lineárních rovnic

## Definice

Nechť $T$ je těleso, $m, n \in \mathbb{N}$, $a_{ij}, b_i \in T$. **Soustava $m$ lineárních rovnic o $n$ neznámých** $x_1, \dots, x_n$ je
$$\begin{aligned} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\ &\ \,\vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n &= b_m \end{aligned}$$
**Řešením** je $n$-tice $(x_1, \dots, x_n) \in T^n$ splňující všechny rovnice; množinu všech řešení značíme $S$.

## Maticový zápis

S maticí soustavy $A \in T^{m,n}$, vektorem neznámých $x$ a vektorem pravých stran $b \in T^m$ lze soustavu zapsat jako
$$Ax = b.$$
**Rozšířená matice soustavy** je $(A \mid b) \in T^{m,n+1}$.

- **Homogenní soustava:** $b = \theta$, tj. $Ax = \theta$. Vždy má aspoň triviální řešení $\theta$.
- **Nehomogenní soustava:** $b \neq \theta$.
- K soustavě $Ax = b$ je **přidružená homogenní soustava** $Ax = \theta$ s množinou řešení $S_0$.

## Struktura množiny řešení

$S_0$ je **podprostor** $T^n$ (uzavřený na součet a násobek). Pro řešitelnou soustavu a libovolné (partikulární) řešení $\tilde{x}$ platí
$$S = \tilde{x} + S_0,$$
tedy množina řešení je [[Lineární-varieta|lineární varieta]] se zaměřením $S_0$. Nad nekonečným tělesem má soustava buď $0$, $1$, nebo nekonečně mnoho řešení (má-li aspoň dvě, má jich nekonečně).

Řešitelnost a počet řešení popisuje [[Frobeniova-věta]]; řešení se hledá [[Gaussova-eliminace|Gaussovou eliminací]].

## Související

- [[Frobeniova-věta]]
- [[Gaussova-eliminace]]
- [[Hodnost-matice]]
- [[Lineární-varieta]]
- [[Matice]]
- [[Regulární-matice]]
