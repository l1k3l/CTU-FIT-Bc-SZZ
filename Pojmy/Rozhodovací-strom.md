---
aliases: [rozhodovací strom, rozhodovacího stromu, rozhodovacímu stromu, rozhodovací stromy, rozhodovacích stromů, rozhodovacím stromům, rozhodovacím stromem, rozhodovacích stromech, decision tree]
tags: [definice, kurz/ML1]
---

# Rozhodovací strom

## Definice

**Rozhodovací strom** (angl. *decision tree*) je model supervizovaného učení v podobě zakořeněného [[Strom|stromu]], jehož vnitřní vrcholy obsahují **rozhodovací pravidla** nad příznaky (např. $X = 0$ pro binární, $X \le d$ pro spojitý příznak) a jehož **listy** nesou predikovanou hodnotu vysvětlované proměnné $Y$. Predikce datového bodu odpovídá průchodu od kořene k listu podle splnění pravidel.

- **Klasifikační strom** přiřazuje v listu majoritní třídu; dělení volí maximalizací **informačního zisku** (pokles **entropie**, příp. **Gini indexu**).
- **Regresní strom** přiřazuje v listu průměr hodnot $Y$; dělení volí minimalizací rozptylu / MSE.

Strom se buduje shora dolů **hladovým** algoritmem (ID3, C4.5, CART) — nalezení optimálního stromu je NP-úplný problém. Hloubku/velikost (a tím přeučení) řídíme hyperparametry a prořezáváním, laděnými přes [[Křížová-validace|křížovou validaci]].

## Vlastnosti

- Zvládá klasifikaci i regresi, spojité i kategoriální příznaky, je snadno interpretovatelný.
- Predikce je rychlá (průchod stromem), učení dražší.
- Náchylný k přeučení → základ **ensemble** metod (náhodný les, boosting / AdaBoost — otázka 8).

## Související

- [[Strom]]
- [[Křížová-validace]]
- [[Lineární-regrese]]
