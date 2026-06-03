---
aliases: [matice lineárního zobrazení, matici lineárního zobrazení, maticí zobrazení, matice zobrazení, matici zobrazení, změna báze, matice přechodu, matice přechodu mezi bázemi]
tags: [definice, kurz/LA2]
---

# Matice lineárního zobrazení

## Definice

Nechť $A \in \mathcal{L}(P,Q)$ pro prostory **konečné dimenze**, $\mathcal{X} = (x_1, \dots, x_n)$ báze $P$ a $\mathcal{Y} = (y_1, \dots, y_m)$ báze $Q$. **Matice zobrazení $A$ vzhledem k bázím $\mathcal{X}, \mathcal{Y}$** je matice ${}^{\mathcal{X}}A^{\mathcal{Y}} \in T^{m,n}$ definovaná po sloupcích předpisem
$$\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)_{:i} := (Ax_i)_{\mathcal{Y}}, \qquad i \in \hat{n},$$
tj. $i$-tý sloupec jsou souřadnice obrazu $i$-tého bázového vektoru vzhledem k $\mathcal{Y}$. Pro operátor $A \in \mathcal{L}(P)$ píšeme zkráceně ${}^{\mathcal{X}}A := {}^{\mathcal{X}}A^{\mathcal{X}}$.

## Vlastnosti

- **Obraz vektoru v souřadnicích:** pro každé $z \in P$ platí
$$(Az)_{\mathcal{Y}} = {}^{\mathcal{X}}A^{\mathcal{Y}} \cdot (z)_{\mathcal{X}}.$$
- **Hledání vzoru:** $z$ je vzor $w$ ($Az = w$) $\iff$ $(z)_{\mathcal{X}}$ řeší soustavu $\big({}^{\mathcal{X}}A^{\mathcal{Y}} \mid (w)_{\mathcal{Y}}\big)$.
- **Hodnost:** $h(A) = h\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)$ pro libovolnou volbu bází (smiřuje hodnost zobrazení a [[Hodnost-matice|hodnost matice]]).
- **Složení → součin matic:** pro $A \in \mathcal{L}(Q,V)$, $B \in \mathcal{L}(P,Q)$ a báze $\mathcal{X},\mathcal{Y},\mathcal{W}$ prostorů $P,Q,V$ platí
$$ {}^{\mathcal{X}}(AB)^{\mathcal{W}} = {}^{\mathcal{Y}}A^{\mathcal{W}} \cdot {}^{\mathcal{X}}B^{\mathcal{Y}}.$$
- **Izomorfismus → [[Regulární-matice|regulární matice]]:** je-li $A$ izomorfismus, je ${}^{\mathcal{X}}A^{\mathcal{Y}}$ regulární a $\big({}^{\mathcal{X}}A^{\mathcal{Y}}\big)^{-1} = {}^{\mathcal{Y}}(A^{-1})^{\mathcal{X}}$.

## Matice přechodu a změna báze

**Matice přechodu** od báze $\mathcal{X}$ k bázi $\mathcal{Y}$ prostoru $P$ je matice identického operátoru ${}^{\mathcal{X}}E^{\mathcal{Y}} \in T^{n,n}$; ve sloupcích obsahuje souřadnice vektorů z $\mathcal{X}$ vzhledem k $\mathcal{Y}$:
$$ {}^{\mathcal{X}}E^{\mathcal{Y}} = \big( (x_1)_{\mathcal{Y}} \ \cdots \ (x_n)_{\mathcal{Y}} \big).$$
Platí ${}^{\mathcal{X}}E^{\mathcal{Y}} \cdot (x)_{\mathcal{X}} = (x)_{\mathcal{Y}}$, je regulární s $\big({}^{\mathcal{X}}E^{\mathcal{Y}}\big)^{-1} = {}^{\mathcal{Y}}E^{\mathcal{X}}$ a skládá se ${}^{\mathcal{Y}}E^{\mathcal{Z}} \cdot {}^{\mathcal{X}}E^{\mathcal{Y}} = {}^{\mathcal{X}}E^{\mathcal{Z}}$.

**Změna bází v matici zobrazení:** pro $A \in \mathcal{L}(P,Q)$ a báze $\mathcal{X},\tilde{\mathcal{X}}$ prostoru $P$, $\mathcal{Y},\tilde{\mathcal{Y}}$ prostoru $Q$ platí
$$ {}^{\tilde{\mathcal{X}}}A^{\tilde{\mathcal{Y}}} = {}^{\mathcal{Y}}E^{\tilde{\mathcal{Y}}} \cdot {}^{\mathcal{X}}A^{\mathcal{Y}} \cdot {}^{\tilde{\mathcal{X}}}E^{\mathcal{X}}.$$

## Související

- [[Lineární-zobrazení]]
- [[Matice]]
- [[Regulární-matice]]
