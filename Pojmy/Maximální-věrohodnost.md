---
aliases: [maximální věrohodnost, maximálně věrohodný odhad, maximálně věrohodného odhadu, metoda maximální věrohodnosti, MLE, věrohodnostní funkce, věrohodnost, věrohodnosti, log-věrohodnost, logaritmická věrohodnost]
tags: [definice, kurz/ML1, kurz/PST]
---

# Maximální věrohodnost

## Definice

**Metoda maximální věrohodnosti** (angl. *maximum likelihood estimation*, **MLE**) je metoda konstrukce [[Bodový-odhad|bodového odhadu]] neznámého parametru $\theta$. Pro pozorování $x_1,\dots,x_n$ zavedeme **věrohodnostní funkci** jako pravděpodobnost (resp. hustotu) dat v závislosti na parametru; za předpokladu [[Nezávislost-náhodných-veličin|nezávislosti]] pozorování je to součin
$$L(\theta) = \prod_{i=1}^n f_\theta(x_i).$$
**MLE odhad** $\hat\theta_{\mathrm{MLE}} = \arg\max_\theta L(\theta)$ je hodnota parametru, při níž jsou pozorovaná data **nejpravděpodobnější**. V praxi se maximalizuje **log-věrohodnost** $\ell(\theta) = \ln L(\theta)$ (stejné maximum, ze součinu se stane součet, snazší derivace).

## Použití v ML1

Trénování [[Logistická-regrese|logistické regrese]] je MLE odhad koeficientů $w$: maximalizace log-věrohodnosti je ekvivalentní minimalizaci **binární křížové entropie** (binary cross-entropy). Účelová funkce je konvexní, ale nemá uzavřené řešení — řeší se numericky (gradientní metoda, Newton / IRLS).

## Související

- [[Bodový-odhad]]
- [[Logistická-regrese]]
- [[Nezávislost-náhodných-veličin]]
