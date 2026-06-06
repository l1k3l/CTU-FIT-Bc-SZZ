---
aliases: [tabu prohledávání, tabu prohledávání, tabu search, tabu list, tabu seznam, tabu prohledáváním]
tags: [algoritmus, kurz/ZUM]
---

# Tabu prohledávání

## Princip

Rozšíření [[Hill-climbing|hill climbingu]], které brání **oscilaci** a nutí algoritmus opustit **[[Lokální-extrém|lokální optimum]]**. Zavádí **tabu list** — popis částí prostoru, kam se kandidující řešení nesmí vrátit. Vyšplhá-li algoritmus na vrchol, je nucen „dobytý vrchol" opustit a zahájit **vynucený sestup**; navštívené oblasti se postupně zakazují (tabu list roste a vede prohledávání do neprozkoumaných oblastí).

Podoba tabu listu závisí na problému, většinou vychází z **podobnosti / metriky** na množině stavů: euklidovská či cosinová vzdálenost ($\mathbb{R}^n$), Hammingova vzdálenost ($\{0,1\}^n$), strukturální podobnost (grafy, stromy).

## Související

- [[Hill-climbing]], [[Simulované-žíhání]], [[Lokální-extrém]]
