---
aliases: [křížová validace, křížové validace, křížovou validací, křížovou validaci, křížové validaci, cross-validation, cross validation, k-fold, k-násobná křížová validace, leave-one-out, LOO]
tags: [definice, kurz/ML1]
---

# Křížová validace

## Definice

**Křížová validace** (angl. *cross-validation*) je technika odhadu generalizační (testovací) chyby modelu, která opakovaně využívá tatáž data k trénování i validaci. Slouží zejména pro **výběr hyperparametrů** a **výběr modelu** (model selection), když není dostatek dat na samostatnou validační množinu.

**$k$-násobná křížová validace** ($k$-fold, $2 \le k \le N$): trénovací data $\mathcal{D}$ se náhodně rozdělí na $k$ podobně velkých částí $\mathcal{D}_1,\dots,\mathcal{D}_k$. Pro každé $j = 1,\dots,k$ se model natrénuje na $\mathcal{D} \setminus \mathcal{D}_j$ a změří se chyba $e_j$ na vynechané části $\mathcal{D}_j$. Výsledná **cross-validační chyba** je průměr
$$\hat e = \frac{1}{k}\sum_{j=1}^k e_j.$$
Vyberou se hyperparametry s nejmenší $\hat e$ a finální model se přetrénuje na celém $\mathcal{D}$. Typicky $k = 5$–$10$.

**Leave-one-out (LOO):** extrémní případ $k = N$ — trénuje se na všech datech kromě jednoho bodu, na němž se měří chyba; opakuje se $N$krát.

## Vlastnosti

- Méně rozptýlený odhad chyby a efektivnější využití dat než jediná validační množina.
- Pro fixní model je CV chyba odhadem **očekávané** testovací chyby $\mathrm{Err}$, nikoli chyby konkrétního modelu $\mathrm{Err}_{\mathcal{D}}$.
- Cena: $k$-násobné (resp. $N$-násobné) trénování.

## Související

- [[Lineární-regrese]]
- [[Logistická-regrese]]
- [[Rozhodovací-strom]]
