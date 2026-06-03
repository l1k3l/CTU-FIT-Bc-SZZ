---
aliases: [neuronová síť, neuronové sítě, neuronovou sítí, neuronových sítí, umělá neuronová síť, dopředná neuronová síť, feedforward, vícevrstvá síť, hluboká neuronová síť, deep learning, zpětné šíření chyby, backpropagation, dávková normalizace, dropout]
tags: [definice, kurz/ML2]
---

# Neuronová síť

## Definice

(Dopředná, *feedforward*) **neuronová síť** je model složený z vrstev neuronů, kde výstupy jedné vrstvy tvoří vstupy další. Každý neuron počítá $g(w^Tx+w_0)$ s [[Aktivační-funkce|aktivační funkcí]] $g$. Síť je **složení** vrstev
$$f=f^{(l)}\circ f^{(l-1)}\circ\dots\circ f^{(1)},$$
vrstvy kromě výstupní jsou **skryté**, počet vrstev je **hloubka**. Klasifikační dopředná síť = **vícevrstvý [[Perceptron|perceptron]] (MLP)**.

**Skryté vrstvy** fungují jako **naučené příznaky** (na rozdíl od ručně volených bázových/jádrových funkcí). **Věta o univerzální aproximaci:** už síť s jednou skrytou vrstvou aproximuje libovolnou spojitou funkci (v praxi se však dává přednost hlubším sítím).

## Trénování

Minimalizace účelové funkce $J(w)=\frac1N\sum_i L(Y_i,f(x_i;w))$ (ztráty: MSE, cross-entropy) **[[Gradient|gradientním]] sestupem**. Gradient se počítá **zpětným šířením chyby** (back-propagation): dopředný chod spočte výstup a $J$, zpětný chod propaguje derivace řetězovým pravidlem od výstupu ke vstupu (výpočetní graf).

- **Optimalizace:** stochastický gradientní sestup na dávkách (epocha = průchod dat), momentum, AdaGrad, RMSProp, **Adam**.
- **Regularizace:** L1/L2 penalizace vah, předčasné zastavení (early stopping), dropout, dávková normalizace.

## Související

- [[Perceptron]]
- [[Aktivační-funkce]]
- [[Gradient]]
- [[Maximální-věrohodnost]]
