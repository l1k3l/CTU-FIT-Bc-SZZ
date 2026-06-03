---
aliases: [spektrální rozklad, spektrálního rozkladu, spektrální věta, spektrum symetrické matice, ortogonální diagonalizace, ortogonálně diagonalizovatelná, pozitivně definitní, pozitivní definitnost, pozitivně definitní matice, pozitivně semidefinitní, pozitivně semidefinitní matice, normální matice]
tags: [definice, kurz/LA2]
---

# Spektrální rozklad

## Definice

**Spektrální rozklad** je [[Diagonalizace|diagonalizace]] reálné **symetrické** matice $S \in \mathbb{R}^{n,n}$ ($S^T = S$) pomocí [[Ortogonální-matice|ortogonální]] matice. Spektrální věta (Věta o symetrických maticích) říká:

1. všechna [[Vlastní-číslo|vlastní čísla]] symetrické matice jsou **reálná**;
2. existuje ortogonální matice $Q$ a diagonální $\Lambda$ tak, že
$$S = Q \Lambda Q^T,$$
přičemž sloupce $Q$ tvoří **ortonormální bázi** $\mathbb{R}^n$ z vlastních vektorů a $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ obsahuje příslušná vlastní čísla.

Obráceně: každá matice tvaru $Q\Lambda Q^T$ (s ortogonální $Q$, diagonální $\Lambda$) je symetrická, neboť $(Q\Lambda Q^T)^T = Q\Lambda Q^T$.

## Idea důkazu

- **Reálnost:** pro vlastní pár $(\lambda, x)$ vychází $\overline{x}^T S x = \lambda\|x\|_2^2$ i $= \overline{\lambda}\|x\|_2^2$, tedy $\lambda = \overline{\lambda}$, takže $\lambda \in \mathbb{R}$.
- **Existence rozkladu:** indukcí podle $n$ pomocí částečné diagonalizace — vlastní vektor lze volit reálný a jednotkový, doplnit na ortonormální bázi a redukovat na blok o rozměr menší.

## Vztah k diagonalizaci a normálním maticím

Spektrální rozklad je speciální (ortogonální) případ diagonalizace $A = PDP^{-1}$, kde navíc $P = Q$ je ortogonální, takže $Q^{-1} = Q^T$. Ortonormální báze z vlastních vektorů existuje obecněji pro **normální** matice ($A^T A = A A^T$); pro komplexní normální matice je $A = U D \overline{U}^T$ s unitární $U$.

## Pozitivní (semi)definitnost

Symetrická $S$ je **pozitivně definitní**, pokud $x^T S x > 0$ pro všechna $x \neq \theta$; **pozitivně semidefinitní**, pokud $x^T S x \ge 0$ pro všechna $x$. Charakterizace přes spektrum:

- $S$ je pozitivně semidefinitní $\iff$ všechna vlastní čísla jsou **nezáporná** ($\lambda_i \ge 0$);
- $S$ je pozitivně definitní $\iff$ všechna vlastní čísla jsou **kladná** ($\lambda_i > 0$).

(Plyne dosazením $y = Q^T x$ do $x^T S x = y^T \Lambda y = \sum_i \lambda_i y_i^2$.)

## Související

- [[Vlastní-číslo]]
- [[Diagonalizace]]
- [[Ortogonální-matice]]
- [[SVD]]
