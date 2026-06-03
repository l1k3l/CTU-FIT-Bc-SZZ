---
aliases: [lineární zobrazení, lineárního zobrazení, lineárnímu zobrazení, lineárním zobrazením, lineárních zobrazení, jádro, jádra, jádru, obraz, obrazu, obraz zobrazení, defekt, defektu, hodnost zobrazení, injektivní, surjektivní, izomorfismus, homomorfismus, lineární operátor, lineární funkcionál]
tags: [definice, kurz/LA2]
---

# Lineární zobrazení

## Definice

Nechť $P$ a $Q$ jsou vektorové prostory nad **stejným** tělesem $T$. Zobrazení $A : P \to Q$ je **lineární** (značíme $A \in \mathcal{L}(P,Q)$), právě když současně platí:

1. **aditivita:** $(\forall x, y \in P)\big(A(x+y) = Ax + Ay\big)$;
2. **homogenita:** $(\forall \alpha \in T)(\forall x \in P)\big(A(\alpha x) = \alpha Ax\big)$.

Ekvivalentně jednou podmínkou: $(\forall \alpha \in T)(\forall x, y \in P)\big(A(\alpha x + y) = \alpha Ax + Ay\big)$. (Pro obraz vektoru píšeme zkráceně $Ax$ místo $A(x)$.)

**Speciální případy:**
- **lineární operátor (transformace):** $A \in \mathcal{L}(P,P)$, značíme $\mathcal{L}(P)$;
- **lineární funkcionál:** lineární zobrazení $P \to T$;
- **izomorfismus:** lineární zobrazení, které je bijekce.

## Jádro, obraz, hodnost a defekt

Nechť $A \in \mathcal{L}(P,Q)$, $\theta_P, \theta_Q$ nulové vektory v $P$, $Q$.

- **Hodnost zobrazení:** $h(A) := \dim A(P)$, kde $A(P)$ je **obor hodnot (obraz)** $\operatorname{Im} A = A(P)$.
- **Jádro:** $\ker A := \{x \in P \mid Ax = \theta_Q\} = A^{-1}(\theta_Q)$.
- **Defekt:** $d(A) := \dim \ker A$.

$A(P)$ i $\ker A$ jsou **podprostory** ($A(P) \subset\subset Q$, $\ker A \subset\subset P$), takže mají dimenzi. *Pozor:* hodnost zobrazení $h(A)$ je odlišný pojem od [[Hodnost-matice|hodnosti matice]].

## Vlastnosti

Pro $A \in \mathcal{L}(P,Q)$:
- $A\theta_P = \theta_Q$ (obraz nulového vektoru je nulový vektor);
- $A(\langle M \rangle) = \langle A(M) \rangle$ — obraz lineárního obalu je lineární obal obrazů; tedy z báze $(x_1,\dots,x_n)$ prostoru $P$ je $A(P) = \langle Ax_1, \dots, Ax_n \rangle$;
- obraz LZ souboru je LZ; „předobraz“ LN souboru je LN;
- lineární zobrazení je jednoznačně určeno obrazy prvků libovolné **báze** $P$ (pro každý soubor obrazů existuje právě jedno takové $A$);
- složení i inverze (existuje-li) lineárních zobrazení jsou opět lineární: $A \in \mathcal{L}(P,Q)$, $B \in \mathcal{L}(Q,R) \Rightarrow BA \in \mathcal{L}(P,R)$.

## Věta o dimenzi (rank-nullity)

**2. věta o dimenzi:** pro $A \in \mathcal{L}(P,Q)$ platí
$$h(A) + d(A) = \dim P.$$

## Injektivita, surjektivita, izomorfismus

Pro $A \in \mathcal{L}(P,Q)$ s $\dim P, \dim Q < \infty$:

- **injektivita:** $A$ je prosté $\iff \ker A = \{\theta_P\} \iff d(A) = 0 \iff h(A) = \dim P$. Prosté zobrazení zachovává LN soubory.
- **surjektivita:** $A$ je na $\iff A(P) = Q \iff h(A) = \dim Q$.
- **izomorfismus** = injektivní + surjektivní. Je-li $\dim P = \dim Q < \infty$, pak je $A$ prosté právě tehdy, když je na.

## Související

- [[Matice-lineárního-zobrazení]]
- [[Hodnost-matice]]
- [[Matice]]
- [[Soustava-lineárních-rovnic]]
