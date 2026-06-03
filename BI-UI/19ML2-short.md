---
tags: [otázka, kurz/ML2, otázka/19, todo]
---

# 19 — Neuronové sítě (zkrácená verze)

## 1. Perceptron

[[Perceptron]] = jeden neuron. Vnitřní potenciál $\xi=w^Tx+w_0$, skoková aktivace:
$$\hat Y=g(\xi),\quad g(\xi)=\mathbb 1[\xi\ge0].$$
Hranice $w^Tx+w_0=0$ = nadrovina → **lineární klasifikátor** ($-w_0$ = práh).

**Trénování (on-line):** při chybě $w_i\leftarrow w_i+(Y-\hat Y)x_i$, $w_0\leftarrow w_0+(Y-\hat Y)$.

**Věta o konvergenci:** lineárně separabilní data s odstupem $\gamma$ ($\lVert\tilde w^*\rVert=1$) a $\lVert\tilde x_i\rVert\le R$ → nejvýše $R^2/\gamma^2$ chyb.

Perceptron **neumí XOR** → potřeba vícevrstvé sítě.

## 2. Vícevrstvá síť (MLP)

Dopředná síť = složení vrstev $f=f^{(l)}\circ\dots\circ f^{(1)}$, neuron $g(w^Tx+w_0)$. Skryté vrstvy = **naučené příznaky**; hloubka = počet vrstev.

**Univerzální aproximace:** 1 skrytá vrstva aproximuje libovolnou spojitou funkci (ale neefektivně → raději hlubší sítě; učení příznaků = ztráta konvexity).

## 3. Aktivační funkce

**Skryté** (nelineární, sk. všude diferenc.): **ReLU** $\max(0,z)$ (nejpoužívanější), Leaky ReLU ($0{,}01z$ pro $z<0$), SELU, tanh.

**Výstupní:**
- regrese → identita $g(z)=z$;
- binární → **sigmoida** $\sigma(z)=\frac1{1+e^{-z}}$, $\hat p=\sigma(w^Th+w_0)$;
- $c$ tříd → **softmax** $\frac{e^{z_i}}{\sum_j e^{z_j}}$, $\hat Y=\arg\max_i$.

## 4. Ztrátové / účelové funkce

$J(w)=\frac1N\sum_i L(Y_i,f(x_i;w))$.
- regrese: $(Y-\hat Y)^2$ → MSE (resp. L1 → MAE);
- binární: $-Y\log\hat p-(1-Y)\log(1-\hat p)$ (cross-entropy);
- $c$ tříd: $-\log\hat p_Y$ (kategorická cross-entropy).

(Cross-entropy ≈ [[Maximální-věrohodnost|MLE]].)

## 5. Zpětné šíření chyby

Min. $J$ [[Gradient|gradientním]] sestupem. **Řetězové pravidlo** $\frac{\partial(f\circ g)}{\partial x_j}=\sum_i\frac{\partial f}{\partial g_i}\frac{\partial g_i}{\partial x_j}$.
- **Forward pass:** spočti $f(x;w)$, $J$.
- **Backward pass:** derivace zpět vrstvami (od výstupu ke vstupu) = **backprop**; reprezentace **výpočetním grafem**.

## 6. Trénování hlubokých sítí

**Dávkové učení:** gradient na dávce velikosti $m$ (odhad), **epocha** = průchod dat ($N/m$ kroků), shuffle. $m=1$ = online.

**Optimalizace:**
- **SGD:** $w\leftarrow w-\epsilon\tilde\nabla J$; $\epsilon$ (learning rate) kritický.
- **+ momentum:** $v\leftarrow\mu v-\epsilon\tilde\nabla J$, $w\leftarrow w+v$.
- **AdaGrad / RMSProp / Adam** — adaptivní $\epsilon$ per váha (Adam nejpoužívanější).

**Problémy:** lokální minima / sedlové body; mizející/explodující gradient → **batch normalization** (standardizace potenciálů přes dávku $+\gamma h'+\beta$).

**Regularizace** (proti přeučení):
- **L2/L1** penalizace vah ($\lambda\Omega(w)$; L1 → řídké);
- **early stopping** (nejlepší validační chyba);
- **dropout** (náhodné nulování vstupů s prav. $p$, škálování $\frac1{1-p}$; ≈ bagging).

---

## Co odpovědět rychle
- **Perceptron:** $\hat Y=g(w^Tx+w_0)$ skoková, lineární klasifikátor; konvergence $\le R^2/\gamma^2$; neumí XOR.
- **MLP:** složení vrstev, skryté = naučené příznaky; univerzální aproximace.
- **Aktivace:** ReLU (skryté), sigmoid/softmax/identita (výstup).
- **Ztráty:** MSE / cross-entropy.
- **Backprop:** forward + backward (řetězové pravidlo).
- **Trénink:** dávkové SGD/Adam + epochy; regularizace L2/early stopping/dropout/batch norm.
