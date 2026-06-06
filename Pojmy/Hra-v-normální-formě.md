---
aliases: [hra v normální formě, hry v normální formě, hru v normální formě, normální forma, akční profil, akčního profilu, akční profily, utilitní funkce, výplatní funkce, výplatní matice, herní matice, teorie her]
tags: [definice, kurz/ZUM]
---

# Hra v normální formě

## Definice

**Konečná hra v normální formě** pro $n$ hráčů je trojice $(\mathcal{N}, \mathcal{A}, u)$:
- $\mathcal{N} = \{N_1, \dots, N_n\}$ — konečná množina **hráčů**,
- $\mathcal{A} = A_1 \times \dots \times A_n$, kde $A_i$ je množina akcí hráče $N_i$; prvek $\mathbf{a} \in \mathcal{A}$ je **akční profil** — jedna konkrétní volba akcí provedená *nezávisle* všemi hráči,
- $u = (u_1, \dots, u_n)$, $u_i : \mathcal{A} \to \mathbb{R}$ — **utilitní (výplatní) funkce** hráče $N_i$; $u_i(\mathbf{a})$ je užitek hráče $N_i$ z profilu $\mathbf{a}$.

Pro 2 hráče se hra zapisuje **herní (výplatní) maticí**: řádek = akce $N_1$, sloupec = akce $N_2$, buňka = dvojice $(u_1, u_2)$.

Třídy: *common-payoff* ($u_1 = \dots = u_n$), *constant-sum* ($\sum_i u_i = c$), *zero-sum* ($c = 0$, např. kámen-nůžky-papír).

## Analýza akčních profilů

Z „pohledu shora" (hráči jsou rovnocenní) hledáme zajímavé profily: **[[Paretovo-optimum|Paretova optima]]** a **[[Nashovo-equilibrium|Nashova equilibria]]**. Klíčový pojem je **best response** hráče $N_i$ na akce ostatních $\mathbf{a}_{-i}$:
$$BR(\mathbf{a}_{-i}) = \arg\max_{\hat{a}_i \in A_i} u_i(a_1, \dots, \hat{a}_i, \dots, a_n).$$

## Související

- [[Nashovo-equilibrium]], [[Paretovo-optimum]]
- [[Herní-strom]] (hra v extenzivní formě — reprezentace stromem)
