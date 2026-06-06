---
aliases: [hill climbing, hill-climbing, horolezecký algoritmus, šplhání do kopce, steepest ascent, nejstrmější stoupání, lokální prohledávání, lokálního prohledávání, iterativní optimalizace]
tags: [algoritmus, kurz/ZUM]
---

# Hill climbing

## Princip

Metoda **lokálního prohledávání** / iterativní optimalizace pro úlohy, kde je důležitý jen cílový stav, ne cesta k němu. Pracuje s jediným kandidátem $x$, generuje body v jeho **okolí** (sousedství) a přejde k sousedovi, je-li lepší podle kriteriální funkce $f$. Analogie: šplhání do kopce — „rozhlížíme se a jdeme nahoru".

Generování souseda: vektor z $\mathbb{R}^n$ ve vzdálenosti $\le \varepsilon$; binární vektor lišící se v $\le k$ bitech; u problému $N$ dam konfigurace lišící se pozicí jedné dámy; obecně sousední uzel ve [[Stavový-prostor|stavovém prostoru]].

## Varianty

- **základní (first-choice / stochastic):** vygeneruje 1 náhodného souseda a přijme ho, je-li lepší;
- **steepest ascent (nejstrmější stoupání):** vygeneruje $k$ sousedů a vybere nejlepšího;
- **s restarty:** algoritmus se spouští opakovaně (např. 1000×) z náhodných počátečních stavů.

## Problém lokálního optima

Uvázne v **[[Lokální-extrém|lokálním optimu]]**, na **plošině** nebo **hřbetu** — k dalšímu zlepšení by byl nutný *dočasně zhoršující krok*, který hill climbing nedělá. Navíc **prokletí dimenzionality**: ve vysokých dimenzích nelze dostatečně hustě navzorkovat okolí (objem roste exponenciálně). Zmírnění: [[Simulované-žíhání]], [[Tabu-prohledávání]], restarty, populační metody.

## Související

- [[Simulované-žíhání]], [[Tabu-prohledávání]], [[Lokální-extrém]], [[Genetický-algoritmus]], [[Stavový-prostor]]
