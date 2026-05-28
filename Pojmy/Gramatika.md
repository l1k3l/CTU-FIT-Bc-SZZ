---
aliases: [gramatika, gramatiky, gramatice, gramatikou, gramatik, gramatikám, gramatikami, generativní gramatika]
tags: [definice, kurz/AAG]
---

# Gramatika

## Definice

**Gramatika** (generativní, frázová) je čtveřice
$$G = (N, \Sigma, P, S),$$
kde
- $N$ — konečná množina **neterminálních symbolů** (neterminálů),
- $\Sigma$ — konečná množina **terminálních symbolů**, $N \cap \Sigma = \emptyset$,
- $P$ — konečná množina **přepisovacích pravidel** $(\alpha, \beta)$, často psaných $\alpha \to \beta$, $\alpha \in (N \cup \Sigma)^+$, $\beta \in (N \cup \Sigma)^*$,
- $S \in N$ — **počáteční (startovací) neterminál**.

**Přímá derivace:** $\gamma \alpha \delta \Rightarrow \gamma \beta \delta$, je-li $\alpha \to \beta \in P$.

**Větná forma:** $\alpha$ taková, že $S \Rightarrow^* \alpha$. **Věta:** větná forma bez neterminálů.

**Jazyk gramatiky:** $L(G) = \{w \in \Sigma^* : S \Rightarrow^* w\}$.

## Chomského hierarchie

| Typ | Název | Pravidla | Akceptor |
|---|---|---|---|
| 0 | neomezená | $\alpha \to \beta$, $\alpha \in (N\cup\Sigma)^+$ | Turingův stroj |
| 1 | kontextová | $\gamma A \delta \to \gamma \alpha \delta$, $\alpha \neq \varepsilon$ | lineárně omezený automat |
| 2 | [[Bezkontextová-gramatika\|bezkontextová]] | $A \to \alpha$, $A \in N$ | [[Zásobníkový-automat\|zásobníkový automat]] |
| 3 | [[Regulární-gramatika\|regulární]] | $A \to aB$ nebo $A \to a$ | [[Konečný-automat\|konečný automat]] |

Hierarchie je striktní: typ 3 ⊊ typ 2 ⊊ typ 1 ⊊ typ 0.

## Související
- [[Regulární-gramatika]]
- [[Bezkontextová-gramatika]]
- [[Derivační-strom]]
