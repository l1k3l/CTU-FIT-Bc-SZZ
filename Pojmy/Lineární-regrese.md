---
aliases: [lineární regrese, lineární regresi, lineární regresí, lineárního regresního modelu, lineárního modelu, model lineární regrese, lineární regresní model]
tags: [definice, kurz/ML1]
---

# Lineární regrese

## Definice

**Lineární regrese** je (diskriminativní) model supervizovaného učení, který předpokládá **lineární závislost** vysvětlované (cílové) proměnné $Y$ na příznacích $X_1,\dots,X_p$ s aditivní náhodnou chybou:
$$Y = w_0 + w_1 x_1 + \dots + w_p x_p + \varepsilon, \qquad \mathrm{E}\,\varepsilon = 0.$$
Po zavedení umělého příznaku $x_0 = 1$ a vektoru vah $w = (w_0,\dots,w_p)^T$ stručně $Y = w^T x + \varepsilon$; pro $N$ trénovacích bodů maticově $Y = \mathbf{X}w + \varepsilon$. Koeficient $w_0$ je **intercept** (očekávaná hodnota $Y$ při nulových příznacích).

## Odhad parametrů (OLS)

Váhy se odhadují **[[Metoda-nejmenších-čtverců|metodou nejmenších čtverců]]** — minimalizací reziduálního součtu čtverců $\mathrm{RSS}(w) = \|Y - \mathbf{X}w\|^2$. Řešením **normální rovnice** $\mathbf{X}^T\mathbf{X}\,w = \mathbf{X}^T Y$; je-li $\mathbf{X}^T\mathbf{X}$ regulární (sloupce $\mathbf{X}$ LN), má jediné řešení
$$\hat w_{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T Y.$$
Účelová funkce je konvexní ([[Hessova-matice|Hessova matice]] $2\mathbf{X}^T\mathbf{X}$ je PSD), takže každé řešení normální rovnice je globálním minimem.

## Predikce

$\hat Y = x^T \hat w$ — jde o bodový odhad podmíněné střední hodnoty $\mathrm{E}(Y \mid X = x)$.

## Rozšíření

- **Hřebenová regrese** (ridge) — $L_2$-regularizace $+\lambda\|w\|^2$ proti kolinearitě a přeučení (otázka 11).
- **[[Logistická-regrese|Logistická regrese]]** — analogie pro klasifikaci (binární $Y$), trénovaná [[Maximální-věrohodnost|maximální věrohodností]] (otázka 12).
- **Lineární model bázových funkcí** — nahrazení příznaků jejich nelineárními transformacemi (model zůstává lineární v $w$).

## Související

- [[Metoda-nejmenších-čtverců]]
- [[Konvexní-funkce]]
- [[Logistická-regrese]]
