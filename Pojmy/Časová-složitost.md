---
aliases: [časová složitost, časové složitosti, časovou složitostí, časová a paměťová složitost, paměťová složitost, prostorová složitost, paměťové složitosti, složitost algoritmu, složitosti algoritmu, time complexity, space complexity]
tags: [definice, kurz/PA1, kurz/AG1]
---

# Časová a paměťová složitost

## Výpočetní model (RAM)
**RAM** (Random Access Machine) — paměť je pole celočíselných buněk adresovatelných celými čísly; program je konečná posloupnost sekvenčně prováděných instrukcí (aritmeticko-logické a řídicí). V každém kroku se provede právě jedna instrukce.

## Definice
- **Velikost vstupu $n$** — počet paměťových buněk, které vstup zabírá.
- **Časová složitost** (v nejhorším případě) pro vstup velikosti $n$ je maximum počtu vykonaných instrukcí přes všechny přípustné vstupy velikosti nejvýše $n$.
- **Paměťová (prostorová) složitost** — analogicky maximum počtu použitých paměťových buněk.

Čas se neměří v sekundách, ale **počtem elementárních operací**; složitost nezávisí na jazyce ani hardwaru, popisuje **trend** růstu s $n$.

## Tři případy
Složitost obvykle závisí na konkrétních datech, proto se rozlišuje:
- **nejhorší** (worst case) — horní mez, nejčastěji uváděná,
- **průměrný** (average case) — přes rozdělení vstupů; bývá nejtěžší na analýzu,
- **nejlepší** (best case).

## Vztah k notaci
Pro popis trendu se používá [[Asymptotická-notace|asymptotická notace]] ($O$, $\Omega$, $\Theta$) pro $n \to +\infty$ — zanedbávají se členy nižších řádů a multiplikativní konstanty. Pro posloupnosti operací nad dynamickou strukturou viz [[Amortizovaná-složitost]].

## Související
- [[Asymptotická-notace]]
- [[Amortizovaná-složitost]]
