---
tags: [otázka, kurz/ZUM, otázka/25, todo]
---

# 25 — Hry v normální formě (zkrácená verze)

## Definice
[[Hra-v-normální-formě|Hra v normální formě]] = trojice $(\mathcal{N},\mathcal{A},u)$:
- $\mathcal{N}$ = hráči, $\mathcal{A}=A_1\times\dots\times A_n$, prvek $\mathbf{a}$ = **akční profil** (volba akcí všemi hráči nezávisle),
- $u_i:\mathcal{A}\to\mathbb{R}$ = **utilitní (výplatní) funkce**.

2 hráči → **herní matice**, buňka $(u_1,u_2)$. Třídy: zero-sum / constant-sum / common-payoff.

## Analýza profilů
**[[Paretovo-optimum|Paretovo optimum]]:** $\mathbf{a}'$ paretovsky dominuje $\mathbf{a}$, když $\forall i\,u_i(\mathbf{a}')\ge u_i(\mathbf{a})$ a $\exists i\,u_i(\mathbf{a}')>u_i(\mathbf{a})$. Profil je paretovsky optimální = není dominován.

**Best response:** $BR(\mathbf{a}_{-i})=\arg\max_{\hat a_i}u_i(\dots,\hat a_i,\dots)$.
**[[Nashovo-equilibrium|Nashovo equilibrium]]:** profil $\mathbf{a}$ s $\forall i:a_i\in BR(\mathbf{a}_{-i})$ — každý hraje nejlepší odpověď; **stabilní** (nikdo si jednostranně nepolepší).

## Vězňovo dilema

| | C | D |
|---|---|---|
| **C** | 3, 3 | 0, 5 |
| **D** | 5, 0 | 1, 1 |

D dominantní pro oba → jediné **Nash = (D,D)=(1,1)**. Ale (D,D) je paretovsky dominováno **(C,C)=(3,3)**. ⇒ **Nash ≠ Pareto** (racionalita vede ke kolektivně horšímu).

---

## Co odpovědět rychle
- $(\mathcal{N},\mathcal{A},u)$, akční profil, herní matice.
- **Pareto:** nikdo si nepohorší + aspoň jeden si polepší; optimum = nedominovaný.
- **Nash:** každý hraje best response, stabilní profil.
- **Vězňovo dilema:** (D,D) jediné Nash, dominováno (C,C).
