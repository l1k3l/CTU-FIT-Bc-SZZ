---
studyplan: true
etapa: "6 · ZUM — Holeňa"
qid: "25ZUM"
examiner: "Holeňa"
topic: "Hry v normální formě, Paretovo optimum, Nashovo equilibrium"
readiness: nezačato
tags: [otázka, kurz/ZUM, otázka/25, todo]
---

# Hry v normální formě

> **Otázka SZZ:** Hry v normální formě. Analýza akčních profilů: Paretovo optimum, Nashovo equilibrium.

Zdroje: BI-ZUM (FIT ČVUT), přednáška 7 — *Multiagentní systémy, Teorie her*.

Značení: hráči $\mathcal{N}$, akce $\mathcal{A} = A_1 \times \dots \times A_n$, akční profil $\mathbf{a}$, utilitní funkce $u_i$, redukovaný profil $\mathbf{a}_{-i}$.

---

## 1. Kontext: multiagentní systémy a teorie her

**Multiagentní systém** = kolekce nezávislých agentů ve sdíleném prostředí; každý vnímá, jedná za svým cílem a interaguje s ostatními. **Self-interested** agent maximalizuje svůj **užitek (utilitu)** $u : S \to \mathbb{R}$. **Teorie her** studuje situace, kde jsou utilitní funkce agentů ve vzájemné interakci. Reprezentace hry: **normální forma** (maticí — tato otázka) vs. **extenzivní forma** (stromem — viz [[26ZUM-long|ot. 26]]).

---

## 2. Hra v normální formě

**[[Hra-v-normální-formě|Konečná hra v normální formě]]** pro $n$ hráčů je trojice $(\mathcal{N}, \mathcal{A}, u)$:
- $\mathcal{N} = \{N_1, \dots, N_n\}$ — konečná množina **hráčů**,
- $\mathcal{A} = A_1 \times \dots \times A_n$, kde $A_i$ je množina akcí hráče $N_i$; prvek $\mathbf{a} \in \mathcal{A}$ je **akční profil** — jedna konkrétní volba akcí provedená *nezávisle* všemi hráči,
- $u = (u_1, \dots, u_n)$, $u_i : \mathcal{A} \to \mathbb{R}$ — **utilitní (výplatní) funkce**; $u_i(\mathbf{a})$ je užitek hráče $N_i$ z profilu $\mathbf{a}$.

Pro 2 hráče se hra zapisuje **herní (výplatní) maticí**: řádek = akce $N_1$, sloupec = akce $N_2$, buňka = dvojice $(u_1, u_2)$.

**Třídy her:** *common-payoff* ($u_1 = \dots = u_n$, čistá koordinace) · *constant-sum* ($\sum_i u_i = c$) · *zero-sum* ($c = 0$).

**Příklad (kámen–nůžky–papír, zero-sum):**

| $N_1 \backslash N_2$ | K | N | P |
|---|---|---|---|
| **K** | 0, 0 | 1, −1 | −1, 1 |
| **N** | −1, 1 | 0, 0 | 1, −1 |
| **P** | 1, −1 | −1, 1 | 0, 0 |

---

## 3. Analýza akčních profilů

Hru v normální formě analyzujeme „z pohledu shora" — hráči jsou rovnocenní (nebereme optiku jednoho hráče). Hledáme „zajímavé" profily: **Paretova optima** a **Nashova equilibria**.

### Paretovo optimum
Profil $\mathbf{a}'$ **paretovsky dominuje** profil $\mathbf{a}$, jestliže
1. $\forall i : u_i(\mathbf{a}') \ge u_i(\mathbf{a})$, a
2. $\exists i : u_i(\mathbf{a}') > u_i(\mathbf{a})$

(nikdo si nepohorší, aspoň jeden si polepší). Profil $\mathbf{a}^*$ je **[[Paretovo-optimum|paretovsky optimální]]**, neexistuje-li profil, který jej paretovsky dominuje. Jde o pojem z multikriteriální optimalizace (kompromis mezi protichůdnými kritérii); optimálních profilů bývá více.

### Best response a Nashovo equilibrium
**Best response** hráče $N_i$ na akce ostatních $\mathbf{a}_{-i} = (a_1, \dots, a_{i-1}, a_{i+1}, \dots, a_n)$:
$$BR(\mathbf{a}_{-i}) = \arg\max_{\hat{a}_i \in A_i} u_i(a_1, \dots, \hat{a}_i, \dots, a_n).$$
Profil $\mathbf{a}$ je **[[Nashovo-equilibrium|Nashovo equilibrium]]**, jestliže
$$\forall i : a_i \in BR(\mathbf{a}_{-i}),$$
tj. akce každého hráče je nejlepší odpovědí na akce ostatních. Je to **stabilní** profil — žádný hráč si nemůže *jednostrannou* změnou polepšit (ani svého rozhodnutí litovat).

---

## 4. Worked example — vězňovo dilema

Dva vězni se nezávisle rozhodují: **C** = mlčet (spolupracovat), **D** = udat komplice (zradit). Vyšší číslo = lepší (např. méně let):

| $N_1 \backslash N_2$ | C | D |
|---|---|---|
| **C** | 3, 3 | 0, 5 |
| **D** | 5, 0 | 1, 1 |

**Nashovo equilibrium:** pro $N_1$ proti C dává D zisk $5 > 3$, proti D dává D zisk $1 > 0$ → **D je dominantní**. Symetricky pro $N_2$. Jediné Nashovo equilibrium je tedy **(D, D) = (1, 1)**.

**Paretovo optimum:** profil (D, D) je paretovsky **dominován** profilem (C, C) = (3, 3) (oba si polepší). Paretovsky optimální jsou **(C, C), (C, D), (D, C)** — profil (D, D) optimální *není*.

> **Pointa:** racionální (Nash) chování zde vede ke **kolektivně horšímu** výsledku — Nashovo equilibrium nemusí být paretovsky optimální. To je jádro „dilematu".

---

## Co je potřeba na zkoušku znát

### Definice
- **Hra v normální formě** $(\mathcal{N}, \mathcal{A}, u)$; **akční profil** $\mathbf{a}$; **utilitní funkce** $u_i : \mathcal{A} \to \mathbb{R}$; herní matice.
- **Paretovská dominance:** $\forall i\, u_i(\mathbf{a}') \ge u_i(\mathbf{a})$ a $\exists i\, u_i(\mathbf{a}') > u_i(\mathbf{a})$; **Paretovo optimum** = nedominovaný profil.
- **Best response** $BR(\mathbf{a}_{-i}) = \arg\max_{\hat a_i} u_i(\dots)$; **Nashovo equilibrium** = $\forall i: a_i \in BR(\mathbf{a}_{-i})$ (stabilní profil).

### Klíčové
- Umět v dané matici **najít Nashova equilibria** (každý hráč hraje best response) a **Paretovsky optimální profily** (nedominované).
- **Vězňovo dilema:** (D, D) je jediné Nash, ale je paretovsky dominováno (C, C) → Nash ≠ Pareto.
- Třídy: zero-sum / constant-sum / common-payoff.
