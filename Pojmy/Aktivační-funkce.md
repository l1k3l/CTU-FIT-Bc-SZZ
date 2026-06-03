---
aliases: [aktivační funkce, aktivační funkce, aktivační funkcí, aktivačních funkcí, ReLU, RELU, Leaky ReLU, SELU, sigmoida, softmax, tanh, skoková aktivační funkce]
tags: [definice, kurz/ML2]
---

# Aktivační funkce

## Definice

**Aktivační funkce** $g$ je nelineární funkce aplikovaná na vnitřní potenciál neuronu $\xi=w^Tx+w_0$; výstup neuronu je $g(\xi)$. Nelinearita je nutná — bez ní by se složení vrstev [[Neuronová-síť|neuronové sítě]] redukovalo na jediné lineární zobrazení. Pro trénování gradientním sestupem musí být $g$ (skoro všude) **diferencovatelná**.

## Aktivační funkce skrytých vrstev

- **ReLU** $g(z)=\max(0,z)$ — nejpoužívanější; rychlá, ale nulová derivace pro $z<0$ („umírající ReLU“);
- **Leaky ReLU** $g(z)=z$ pro $z\ge0$, jinak $0{,}01z$ — nenulový gradient i pro $z<0$;
- **SELU** — samonormalizující varianta (zachovává průměr a rozptyl mezi vrstvami);
- **tanh** $g(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}$ — používaná před nástupem ReLU;
- **skoková** $g(z)=\mathbb 1[z\ge0]$ — původní [[Perceptron|perceptron]] (nediferencovatelná → nevhodná pro backprop).

## Výstupní aktivační funkce (podle úlohy)

- **regrese:** identita $g(z)=z$;
- **binární klasifikace:** **sigmoida** $\sigma(z)=\frac1{1+e^{-z}}$ → pravděpodobnost třídy 1;
- **klasifikace do $c$ tříd:** **softmax** $\operatorname{softmax}_i(z)=\frac{e^{z_i}}{\sum_j e^{z_j}}$ → vektor pravděpodobností (diferencovatelná aproximace argmax).

## Související

- [[Neuronová-síť]]
- [[Perceptron]]
- [[Logistická-regrese]]
