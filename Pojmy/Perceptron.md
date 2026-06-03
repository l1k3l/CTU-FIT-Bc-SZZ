---
aliases: [perceptron, perceptronu, perceptronem, jednovrstvý perceptron, vícevrstvý perceptron, MLP, multilayer perceptron, perceptron algoritmus, umělý neuron]
tags: [definice, kurz/ML2]
---

# Perceptron

## Definice

**Perceptron** (Rosenblatt, 1957) je matematický model jednoho umělého neuronu pro binární klasifikaci. Spočte **vnitřní potenciál** jako váženou sumu vstupů
$$\xi=w_0+\sum_{i=1}^p w_ix_i=w^Tx+w_0$$
a aplikuje **skokovou aktivační funkci** $g(\xi)=\mathbb 1[\xi\ge0]$. Výstup $\hat Y=g(w^Tx+w_0)$; hodnota $-w_0$ je **práh**. Rozhodovací hranice $w^Tx+w_0=0$ je **nadrovina** → perceptron je **lineární klasifikátor**.

## Trénování (perceptron algoritmus)

On-line učení: pro chybně klasifikovaný bod inkrementálně upraví váhy
$$w_i\leftarrow w_i+(Y-\hat Y)x_i,\qquad w_0\leftarrow w_0+(Y-\hat Y).$$
**Věta o konvergenci:** jsou-li data lineárně separabilní s odstupem $\gamma>0$ ($\lVert\tilde w^*\rVert=1$) a $\lVert\tilde x_i\rVert\le R$, počet kroků s chybou je nejvýše $R^2/\gamma^2$.

## Omezení a rozšíření

Perceptron umí jen **lineárně separabilní** úlohy (neumí XOR — Minsky, Papert 1969). Skládáním neuronů vzniká **vícevrstvý perceptron (MLP)** = [[Neuronová-síť|dopředná neuronová síť]], trénovaná gradientním sestupem a zpětným šířením chyby.

## Související

- [[Neuronová-síť]]
- [[Aktivační-funkce]]
- [[Logistická-regrese]]
- [[Gradient]]
