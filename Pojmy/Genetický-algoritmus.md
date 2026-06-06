---
aliases: [genetický algoritmus, genetického algoritmu, genetickým algoritmem, genetické algoritmy, GA, evoluční algoritmus, evoluční algoritmy, evolučního algoritmu, evolučním algoritmem, genetický operátor, genetické operátory]
tags: [algoritmus, kurz/ZUM]
---

# Genetický algoritmus

## Princip

**Evoluční algoritmus** (stochastická populační iterativní optimalizace; J. Holland) inspirovaný přírodním výběrem („přežití silnějšího"). „Šlechtí" **populaci** $\mu$ kandidátů (**jedinců**); kvalitní jedinci jsou **selekcí** vybráni k reprodukci (**křížení** + **mutace**), čímž vzniká nová **generace** (operátor **náhrady**). Klasický GA optimalizuje binární řetězce (**chromozomy**) délky $n$:
$$\max_{\mathbf{x} \in \{0,1\}^n} f(\mathbf{x}),$$
kde $f$ je **fitness** (kriteriální funkce). Pojmy: **genotyp** (reprezentace řešení) vs. **fenotyp** (jeho význam/sémantika).

## Schéma

Inicializace populace → opakuj { **selekce** rodičů → **křížení** → **mutace** → **náhrada** } dokud není splněna ukončovací podmínka.

## Genetické operátory

- **Selekce** (výběr rodičů dle fitness): *ruletová* (proporcionální, $P_i = f_i / \sum_j f_j$), *turnajová* (vyber nejlepšího z $k$ náhodně vylosovaných — necitlivá na konkrétní hodnoty fitness).
- **Křížení (rekombinace):** výměna informace mezi dvěma rodiči — *jednobodové*, *dvoubodové*, *n-bodové*, *uniformní* (po bitech). Lze i vynechat.
- **Mutace:** drobná náhodná změna genotypu — *bit-flip* (invertuj každý bit s malou pravděpodobností $p_m \approx 10^{-2}$).

Selekce (+ křížení) zajišťuje **exploataci**, mutace (+ křížení) **exploraci**; poměr řídí selekční tlak a míra mutace. Hlavní hrozba: **předčasná konvergence** (populace zestejní = uvíznutí v lokálním optimu); zmírnění tzv. *niching*.

## Související

- [[Hill-climbing]], [[Simulované-žíhání]] (jednokandidátové metody), [[Normální-rozdělení]] (gaussovská mutace u evolučních strategií), [[Konečný-automat]] (evoluční programování), [[Strom]] (genetické programování)
