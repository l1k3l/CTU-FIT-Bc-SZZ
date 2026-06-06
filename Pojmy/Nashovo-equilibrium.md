---
aliases: [Nashovo equilibrium, Nashova equilibria, Nashova rovnováha, Nashovým equilibriem, Nash equilibrium, best response, nejlepší odpověď]
tags: [definice, kurz/ZUM]
---

# Nashovo equilibrium

## Definice

V [[Hra-v-normální-formě|hře v normální formě]] je **best response** hráče $N_i$ na akce ostatních $\mathbf{a}_{-i} = (a_1, \dots, a_{i-1}, a_{i+1}, \dots, a_n)$ množina
$$BR(\mathbf{a}_{-i}) = \arg\max_{\hat{a}_i \in A_i} u_i(a_1, \dots, \hat{a}_i, \dots, a_n).$$

Akční profil $\mathbf{a}$ je **Nashovo equilibrium**, jestliže
$$\forall i \in \{1, \dots, n\} : a_i \in BR(\mathbf{a}_{-i}),$$
tj. akce každého hráče je nejlepší odpovědí na akce ostatních. Je to **stabilní** profil — žádný hráč si nemůže *jednostrannou* změnou své akce polepšit (ani svého rozhodnutí litovat).

## Vztah k Paretu

Nashovo equilibrium **nemusí** být [[Paretovo-optimum|paretovsky optimální]]. Klasicky ve **vězňovu dilematu** je profil *(zradit, zradit)* jediné Nashovo equilibrium, ale je paretovsky dominován profilem *(mlčet, mlčet)* — racionální individuální chování vede ke kolektivně horšímu výsledku.

## Související

- [[Paretovo-optimum]], [[Hra-v-normální-formě]]
