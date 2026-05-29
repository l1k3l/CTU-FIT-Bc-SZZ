---
aliases: [limita posloupnosti, limity posloupnosti, limitu posloupnosti, limita, limity, limitě, limitou, konverguje, limit of a sequence]
tags: [definice, kurz/MA1]
---

# Limita posloupnosti

## Definice

Reálná [[Posloupnost|posloupnost]] $(a_n)_{n=1}^{\infty}$ má **limitu** $\alpha \in \mathbb{R}^*$ (rozšířená osa, tj. včetně $\pm\infty$), právě když pro **každé okolí** $U_\alpha$ bodu $\alpha$ existuje $N \in \mathbb{N}$ tak, že pro všechna $n \ge N$ platí $a_n \in U_\alpha$:
$$\forall U_\alpha\ \exists N \in \mathbb{N}\ \forall n \in \mathbb{N}\ (n \ge N \Rightarrow a_n \in U_\alpha).$$
Značíme $\lim_{n\to\infty} a_n = \alpha$ nebo $a_n \to \alpha$. Slovně: v každém okolí $\alpha$ leží **všechny členy až na konečně mnoho výjimek**.

## ε-N tvar (pro $\alpha \in \mathbb{R}$)

$$\lim_{n\to\infty} a_n = \alpha \iff \forall \varepsilon > 0\ \exists N\ \forall n \ge N: |a_n - \alpha| < \varepsilon.$$
Pro $\alpha = +\infty$: $\forall c\ \exists N\ \forall n \ge N: a_n > c$.

## Vlastnosti

- **Jednoznačnost:** posloupnost má nejvýše jednu limitu.
- **Vybraná posloupnost:** má-li $(a_n)$ limitu $\alpha$, má každá její podposloupnost také limitu $\alpha$. (Dvě vybrané posloupnosti s různými limitami ⇒ limita neexistuje.)
- **Pozor:** to, že v okolí $\alpha$ leží nekonečně mnoho členů, ke konvergenci k $\alpha$ **nestačí** (to je jen hromadný bod).

## Související

- [[Posloupnost]]
- [[Limita-funkce]]
- [[Asymptotická-notace]]
