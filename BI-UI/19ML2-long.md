---
tags: [otázka, kurz/ML2, otázka/19, todo]
---

# Neuronové sítě

> **Otázka SZZ:** Neuronové sítě – perceptron, aktivační funkce, trénování hlubokých neuronových sítí.

Zdroje: BI-ML2 (FIT ČVUT), přednášky 7–9 — Perceptron a jeho trénování, Vícevrstvé sítě a univerzální aproximace, Aktivační funkce, Ztrátové/účelové funkce, Zpětné šíření chyby, Dávkové učení, Optimalizační metody, Regularizace.

Značení: $x\in\mathbb R^p$ vstup, $w$ váhy, $w_0$ intercept (bias), $\xi=w^Tx+w_0$ vnitřní potenciál, $g$ aktivační funkce, $f(x;w)$ výstup sítě, $L$ ztrátová funkce, $J(w)$ účelová funkce, $\epsilon$ učící parametr (learning rate).

---

## 1. Perceptron

**Model.** **[[Perceptron]]** (Rosenblatt, 1957) je model jednoho umělého neuronu. Spočte **vnitřní potenciál** $\xi=w_0+\sum_{i=1}^p w_ix_i=w^Tx+w_0$ a aplikuje **skokovou aktivační funkci**:
$$\hat Y=g(\xi),\qquad g(\xi)=\begin{cases}1 & \xi\ge 0,\\ 0 & \xi<0.\end{cases}$$
Neuron je „aktivován“ ($g=1$), když $\sum_i w_ix_i\ge -w_0$; hodnota $-w_0$ je **práh**. **Rozhodovací hranice** $w^Tx+w_0=0$ je **nadrovina**, která dělí $\mathbb R^p$ na dva lineárně separované poloprostory → perceptron je **lineární klasifikátor**.

**Algoritmus trénování (perceptron algorithm).** On-line učení: opakovaně procházíme body, pro chybně klasifikovaný bod inkrementálně upravíme váhy. S $\tilde x_i=(1,x_{i;1},\dots,x_{i;p})^T$, $\tilde w=(w_0,\dots,w_p)^T$, predikce $\hat Y_i=g(\tilde x_i^T\tilde w)$ je správná, když $(2Y_i-1)\tilde x_i^T\tilde w>0$. Začneme $\tilde w^0=0$ a iterujeme:
$$\tilde w^{k+1}=\begin{cases}\tilde w^k+(2Y_{i(k)}-1)\tilde x_{i(k)} & \text{predikce chybná},\\ \tilde w^k & \text{jinak}.\end{cases}$$
(Ekvivalentně $\text{error}=Y-\hat Y$, $w_i\leftarrow w_i+\text{error}\cdot x_i$, $w_0\leftarrow w_0+\text{error}$.) Ukončíme, když posledních $N$ kroků nezměnilo váhy.

**Věta (konvergence perceptronu).** Jsou-li data lineárně separabilní — existuje $\tilde w^*$, $\lVert\tilde w^*\rVert=1$ a $\gamma>0$ tak, že $(2Y_i-1)\tilde x_i^T\tilde w^*>\gamma$ pro všechna $i$ — a platí $\lVert\tilde x_i\rVert\le R$, pak počet kroků s chybou je **nejvýše $\dfrac{R^2}{\gamma^2}$**.

*Idea důkazu.* Při $n$-té chybě roste průmět $(\tilde w^{k_n+1})^T\tilde w^*\ge n\gamma$ (každá oprava přidá $\ge\gamma$), takže ze Schwarzovy nerovnosti $\lVert\tilde w^{k_n+1}\rVert\ge n\gamma$. Současně norma roste pomalu: $\lVert\tilde w^{k_n+1}\rVert^2\le nR^2$ (protože při chybě je $(2Y-1)\tilde x^T\tilde w^k<0$). Dohromady $n^2\gamma^2\le nR^2$, tedy $n\le R^2/\gamma^2$. $\blacksquare$

**Problém XOR.** Perceptron umí jen **lineárně separabilní** úlohy; **XOR** neumí (Minsky, Papert 1969 → „AI winter“). XOR řeší až **vícevrstvá síť** (kombinace neuronů), ale algoritmus trénování jednoho perceptronu nelze snadno rozšířit — řešením byl až **gradientní sestup** + **zpětné šíření chyby** (80. léta).

---

## 2. Vícevrstvé neuronové sítě (MLP)

**Dopředná (feedforward) síť**, klasifikačně **vícevrstvý perceptron (MLP)**: vrstvy neuronů, výstupy jedné vrstvy jsou vstupy další; obvykle **plně propojené** (fully connected). Vrstvy kromě výstupní jsou **skryté**; počet vrstev = **hloubka**. Každý neuron počítá $g(w^Tx+w_0)$; $i$-tá vrstva je funkce $f^{(i)}:\mathbb R^{n_{i-1}}\to\mathbb R^{n_i}$ a celá síť je **složení**
$$f=f^{(l)}\circ f^{(l-1)}\circ\dots\circ f^{(1)}.$$

**Role skrytých vrstev.** Skryté vrstvy fungují jako **naučené příznaky** pro další vrstvy (výstupní vrstva je pak lineární model nad nimi) — podobně jako bázové funkce u **[[Jádrová-funkce|jádrových metod]]**, ale zde se příznaky **učí z dat**, nejsou pevně dané. To dává velkou obecnost.

**Věta o univerzální aproximaci** (Hornik 1989): síť s **jednou** skrytou vrstvou (nelineární aktivace, lineární agregace) umí aproximovat libovolnou spojitou funkci s omezeným nosičem s libovolnou přesností. V praxi to ale vyžaduje obrovský počet neuronů a zvyšuje přeučení — výhodnější jsou **hlubší** sítě (sofistikovanější příznaky), za cenu obtížnějšího učení. Učení příznaků **ztrácí konvexitu** úlohy.

---

## 3. Aktivační funkce

### 3.1 Skryté vrstvy (nelineární, skoro všude diferencovatelné)
- **ReLU** $g(z)=\max(0,z)$ — nejpoužívanější; rychlá, kladná derivace pro $z>0$; nevýhoda: nulová derivace pro $z<0$ („umírající ReLU“).
- **Leaky ReLU** $g(z)=z$ pro $z\ge0$, $0{,}01z$ jinak — nenulový gradient i pro $z<0$.
- **SELU** $g(z)=\lambda z$ resp. $\lambda\alpha(e^z-1)$ — samonormalizující (zachovává průměr/rozptyl mezi vrstvami).
- **tanh** $g(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}$ — používaná před ReLU.

(Nelinearita je nutná — jinak by složení lineárních vrstev bylo opět lineární.)

### 3.2 Výstupní vrstva (podle typu úlohy)
- **Regrese:** identita $g(z)=z$, $\hat Y=w^Th+w_0$.
- **Binární klasifikace:** **sigmoida** $\sigma(z)=\frac1{1+e^{-z}}$, $\hat{\mathrm P}(Y=1\mid x)=\sigma(w^Th+w_0)$, $\hat Y=\mathbb 1[\hat p>0{,}5]$.
- **Klasifikace do $c$ tříd:** **softmax** $\operatorname{softmax}_i(z)=\dfrac{e^{z_i}}{\sum_j e^{z_j}}$, $\hat{\mathrm P}(Y=i\mid x)=\operatorname{softmax}_i$, $\hat Y=\arg\max_i$ (diferencovatelná aproximace argmax / one-hot).

---

## 4. Ztrátové a účelové funkce

**Ztrátová funkce** $L(Y,\hat Y)$ měří chybu v jednom bodě; **účelová funkce** je její průměr: $J(w)=\frac1N\sum_{i=1}^N L(Y_i,f(x_i;w))$.

| Úloha | Ztrátová funkce | Účelová funkce |
|---|---|---|
| regrese | kvadratická $(Y-\hat Y)^2$ / L1 $\lvert Y-\hat Y\rvert$ | **MSE** / MAE |
| binární klasifikace | $-Y\log\hat p-(1-Y)\log(1-\hat p)$ | **binární cross-entropy** |
| $c$ tříd | $-\sum_j\mathbb 1_{Y=j}\log\hat p_j=-\log\hat p_Y$ | **kategorická cross-entropy** |

(Cross-entropy odpovídá **[[Maximální-věrohodnost|maximálně věrohodnému]]** odhadu, MSE je analogie **[[Metoda-nejmenších-čtverců|nejmenších čtverců]]**.)

---

## 5. Zpětné šíření chyby (back-propagation)

Účelovou funkci minimalizujeme **[[Gradient|gradientním]] sestupem**, gradient $\nabla_w J(w)$ se počítá **řetězovým pravidlem**. Pro složení vícehodnotové $g:\mathbb R^m\to\mathbb R^n$ s $f:\mathbb R^n\to\mathbb R$:
$$\frac{\partial(f\circ g)}{\partial x_j}(x)=\sum_{i=1}^n\frac{\partial f}{\partial g_i}(g(x))\,\frac{\partial g_i}{\partial x_j}(x).$$

Síť je složení vrstev → gradient podle parametru $w_j$ se počítá postupným násobením a sčítáním parciálních derivací vrstev **od výstupu ke vstupu**. Dva chody:

- **Dopředný chod (forward pass):** spočte výstup $f(x;w)$ a hodnotu $J(w)$.
- **Zpětný chod (backward pass):** propaguje derivace zpět vrstvami — odtud **zpětné šíření chyby**. Násobí derivaci ztráty podle vstupu s derivací sítě podle parametrů.

Výpočet se efektivně reprezentuje **výpočetním grafem** (vrcholy = proměnné, hrany = elementární operace), který umožňuje automatické derivování.

---

## 6. Trénování hlubokých sítí

### 6.1 Dávkové (minibatch) učení
- **Deterministické metody** počítají gradient přes **celou** trénovací množinu — pro velká data paměťově/výpočetně náročné.
- **Stochastické (dávkové) metody** počítají gradient na **dávce** (batch) velikosti $m$ jako odhad $\tilde\nabla_w J(w)$. Velikost typicky mocnina 2 (32, 64, 128); $m=1$ = online učení.
- **Epocha** = jeden průchod celé trénovací množiny ($N/m$ kroků). Před každou epochou body **zamícháme**. Na konci epochy vyhodnotíme validační výkon. Trénink ukončíme po daném počtu epoch / dosažení cíle.

### 6.2 Optimalizační metody (update vah)
- **SGD:** $w\leftarrow w-\epsilon\,\tilde\nabla_w J(w)$. Učící parametr $\epsilon$ kritický: velké → oscilace/divergence, malé → pomalá konvergence (uvíznutí). Inicializace vah náhodná (Xavier/Glorot). $\epsilon$ se často nechává klesat.
- **Momentum (hybnost):** $v\leftarrow\mu v-\epsilon\tilde\nabla J$, $w\leftarrow w+v$ — tlumí oscilace (analogie tělesa v poli). Varianta Nesterov.
- **AdaGrad:** adaptuje $\epsilon$ pro každou váhu zvlášť dělením $\sqrt{\sum\text{(historické gradienty)}^2}$.
- **RMSProp:** jako AdaGrad, ale s **exponenciálně klesajícím** průměrem kvadrátů gradientů (potlačí dávnou historii).
- **Adam** („adaptive moments“): RMSProp + momentum + korekce v počátečních iteracích — v současnosti nejpoužívanější (resp. AdamW při L2). Existují i metody 2. řádu (Newton, BFGS) využívající **[[Hessova-matice|Hessovu matici]]**, ale jsou drahé.

### 6.3 Problémy gradientu v hlubokých sítích
- Gradientní sestup míří do bodů s nulovým gradientem; u hlubokých sítí lze uvíznout v **lokálním minimu** nebo **sedlovém bodě**. Pro sítě s mnoha parametry to obvykle není velký problém (jsou řídké a hodnoty blízké globálnímu minimu).
- **Mizející/explodující gradient:** změna parametrů v hlubších vrstvách mění vstupy mělčích → obtížná volba $\epsilon$ (relativní změny výstupu velmi nelineární v $w$).
- **Dávková normalizace (batch norm):** standardizuje vnitřní potenciály neuronů přes dávku ($h'_{i,j}=\frac{h_{i,j}-\hat\mu_j}{\sqrt{\delta+\hat\sigma_j^2}}$) a volitelně lineárně transformuje $\gamma_j h'_{i,j}+\beta_j$. Stabilizuje učení (střední hodnota/rozptyl řízeny přímo $\gamma,\beta$). Při predikci se používají klouzavé průměry $\mu_j,\sigma_j^2$.

### 6.4 Regularizace (proti přeučení)
- **Penalizace norem vah** (po vrstvách): $J'(w)=J(w)+\lambda\Omega(w)$; **L2** $\Omega=\lVert w^{(i)}\rVert_2^2$ (jako hřebenová regrese), **L1** $\Omega=\lVert w^{(i)}\rVert_1$ (jako Lasso — řídké váhy).
- **Předčasné zastavení (early stopping):** sleduj validační chybu po epochách, ulož nejlepší váhy, ukonči po $\ell$ epochách bez zlepšení. Nejpoužívanější.
- **Dropout:** ve fázi trénování náhodně nuluje vstupy vrstvy (každý nezávisle s prav. $p$), pro každou dávku znovu; nevynulované škáluje $\frac1{1-p}$ (inverzní dropout). Analogie **baggingu** (průměrování podsítí), nutí příznaky být užitečné v různých kontextech → lepší generalizace. Levné, univerzální.

---

## Co je potřeba na zkoušku znát

### Definice
- **Perceptron:** $\hat Y=g(w^Tx+w_0)$, $g$ skoková; lineární klasifikátor, hranice = nadrovina.
- **MLP:** složení vrstev $f=f^{(l)}\circ\dots\circ f^{(1)}$, skryté vrstvy = naučené příznaky; hloubka = počet vrstev.
- **Aktivační funkce:** skryté ReLU/Leaky ReLU/SELU/tanh; výstupní identita (regrese) / sigmoid (binár.) / softmax ($c$ tříd).
- **Ztráty:** MSE/MAE, binární a kategorická cross-entropy.

### Věty
- **Konvergence perceptronu:** lineárně separabilní + odstup $\gamma$, $\lVert\tilde x_i\rVert\le R$ → max. $R^2/\gamma^2$ chyb.
- **Univerzální aproximace:** 1 skrytá vrstva aproximuje libovolnou spojitou funkci (ale neefektivně → raději hlubší sítě).
- Perceptron neumí **XOR** (lineární separabilita).

### Algoritmy
- **Perceptron algoritmus:** při chybě $w\leftarrow w+(Y-\hat Y)x$, on-line.
- **Backpropagation:** forward pass → $J$; backward pass = řetězové pravidlo od výstupu ke vstupu (výpočetní graf).
- **Optimalizace:** SGD (+ momentum), AdaGrad, RMSProp, **Adam**; dávkové učení (batch, epocha, shuffle), learning rate.
- **Regularizace:** L1/L2, early stopping, dropout, batch normalization.
