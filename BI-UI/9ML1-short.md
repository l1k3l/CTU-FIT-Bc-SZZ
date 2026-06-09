---
tags: [otázka, kurz/ML1, otázka/9, todo]
---

# 9 — Metrika, kNN a aglomerativní hierarchické shlukování (zkrácená verze)

## 1. Metrika

[[Metrika]] na $\mathcal{X}$ je funkce $d : \mathcal{X}\times\mathcal{X} \to [0,+\infty)$ taková, že $\forall x,y,z$:
1. $d(x,y)\ge 0$, $\ d(x,y)=0 \iff x=y$ — **pozitivní definitnost**,
2. $d(x,y)=d(y,x)$ — **symetrie**,
3. $d(x,y)\le d(x,z)+d(z,y)$ — **trojúhelníková nerovnost**.

$(\mathcal{X},d)$ = **metrický prostor**. (Pozor: druhý axiom je **symetrie**, NE asociativita; vzdálenost nikdy záporná. Jiný pojem než grafová vzdálenost z AG1.)

**Příklady** (body $\boldsymbol{x},\boldsymbol{y}\in\mathbb{R}^p$):

| metrika | vzorec | $q$ |
|---|---|---|
| eukleidovská $L_2$ | $\sqrt{\sum_i (x_i-y_i)^2}$ | $2$ |
| manhattanská $L_1$ | $\sum_i \lvert x_i-y_i\rvert$ | $1$ |
| Čebyševova $L_\infty$ | $\max_i \lvert x_i-y_i\rvert$ | $\infty$ |
| Minkowského $L_q$ | $\sqrt[q]{\sum_i \lvert x_i-y_i\rvert^q}$ | $q$ |
| Levenštejnova (řetězce) | min. počet vkládání/mazání/nahrazení | — |
| kosinová | $\dfrac{\boldsymbol{x}\cdot\boldsymbol{y}}{\|\boldsymbol{x}\|_2\|\boldsymbol{y}\|_2}$ | — |

Nominální příznak: vzdálenost $0$ (shoda) / $1$ (různé). Vzdálenost lze definovat libovolně (jen jednoznačné číslo dvěma bodům).

**Jednotková koule** ($\{d(\boldsymbol0,\boldsymbol x)=1\}$ v $\mathbb{R}^2$): $L_2$ = **kružnice/kruh**; $L_1$ = **kosočtverec** („na špičku", NE čtverec!); $L_\infty$ = **čtverec** (osově orientovaný).

## 2. Metoda nejbližších sousedů (kNN)

Supervizované učení: pro nový bod $\boldsymbol{x}$ najdi $k$ nejbližších trénovacích bodů a z jejich $Y$ predikuj.
- **klasifikace** = **většinové hlasování** (nejčastější třída mezi sousedy);
- **regrese** = **průměr** $\hat{y}=\tfrac1k\sum_{i=1}^k y_i$, příp. **vážený** $\hat{y}=\frac{\sum w_i y_i}{\sum w_i}$, $w_i = 1/d(\boldsymbol{x},\boldsymbol{x}_i)$ (váhy klesají se vzdáleností).

**Hyperparametry:** $k$ (počet sousedů), metrika, váhy sousedů.

**Líné učení** (*lazy*): učení neprobíhá — **trénovací data = model**; náročná je naopak **predikce** (průchod všemi $N$ body, vzdálenost ke každému). Zrychlení indexací (k-d strom). Opak [[Rozhodovací-strom|rozhodovacích stromů]] (drahé učení, levná predikce).

**Normalizace dat** (kNN je citlivá na měřítko — příznak s větším rozsahem dominuje vzdálenosti):
- min-max: $x_i \leftarrow \frac{x_i-\min_x}{\max_x-\min_x}$ do $[0,1]$;
- standardizace: $x_i \leftarrow \frac{x_i-\bar x}{\sqrt{s_x^2}}$.
(Po příznacích ne vždy vhodné — např. MNIST, kde jsou příznaky souměřitelné → normalizuj globálně.)

**Vliv $k$:** malé $k$ → členitá hranice, **přeučení** ($k=1$ kopíruje data); velké $k$ → vyhlazení, v limitě $k=N$ konstanta (podučení). Přeučení bráníme zvýšením $k$.

**Prokletí dimenzionality:** s rostoucí dimenzí data **řídnou a vzdalují se** a **rozdíly vzdáleností** mezi blízkým a vzdáleným bodem **mizí** → „nejbližší soused" ztrácí smysl. (Podkrychle o objemu $1/100$ má hranu $a=\sqrt[d]{1/100}$: $d{=}50 \Rightarrow a\approx0{,}91$.)

## 3. Aglomerativní hierarchické shlukování

[[Shluková-analýza|Shlukování]] = [[Nesupervizované-učení|nesupervizované učení]]: roztřiď data do shluků (blízké body spolu, vzdálené zvlášť). Rozklad $C=(C_1,\dots,C_k)$, disjunktní, $\bigcup C_i=\mathcal{D}$.

**Algoritmus (zdola-nahoru), idea:** začni s $N$ jednoprvkovými shluky; opakovaně najdi dva **nejbližší** shluky a **spoj** je; po $N-1$ krocích jeden shluk. Vstup: vzdálenost bodů + kritérium spojování (linkage). Výstup: **dendrogram**. **Složitost** $\mathcal{O}(N^3)$, pro single/complete $\mathcal{O}(N^2)$ — nevhodné pro velká data.

**Náročnost a zrychlení:** drahé = opakované **hledání nejbližší dvojice / výpočet vzdáleností** → **předpočítat matici vzdáleností** ($N\times N$). Náročnější než **k-means** ($\mathcal{O}(Nkp)$/iteraci).

**Kritéria spojování (linkage)** — vzdálenost shluků $D(A,B)$ z bodové $d$:

| linkage | $D(A,B)$ | vlastnost |
|---|---|---|
| single (nejbližší soused) | $\min_{x\in A,y\in B} d(x,y)$ | dlouhé řetězce |
| complete (nejvzdálenější soused) | $\max_{x\in A,y\in B} d(x,y)$ | kompaktní shluky |
| average (párová vzdálenost) | $\frac{1}{\lvert A\rvert\lvert B\rvert}\sum_{x\in A,y\in B} d(x,y)$ | kompromis |
| Ward | nárůst vnitřního rozptylu po spojení | účinná, $\mathbb{R}^p$ |

**Dendrogram:** strom, listy = jednoprvkové shluky (výška 0), kořen = vše; **výška vrcholu = vzdálenost** spojených shluků (neklesá).

**Volba počtu shluků $k$:** rozřízni dendrogram mezi $k$-tým a $(k-1)$-ním nejvyšším vrcholem; nebo v limitní výšce; nebo v místě největšího rozdílu výšek. Výhoda oproti k-means: $k$ volíme až z dendrogramu; hierarchická struktura (zvýšení $k$ o 1 jen rozdělí jeden shluk).

---

## Co odpovědět rychle

- **Metrika:** $d\ge0$ ($=0\iff x=y$), symetrie, trojúhelníková nerovnost. Příklady: $L_2,L_1,L_\infty$ ($L_q$), Levenštejn, kosinová.
- **kNN:** $k$ nejbližších sousedů → klasifikace = většina, regrese = (vážený) průměr. Hyperparametry $k$/metrika/váhy. Líné učení (data = model, drahá predikce). Nutná normalizace. Malé $k$ = přeučení. Prokletí dimenzionality.
- **Aglomerativní shlukování:** $N$ shluků → opakovaně spoj 2 nejbližší → dendrogram, rozříznutí dle $k$. Linkage: single (min), complete (max), average (průměr), Ward (rozptyl). Složitost $\mathcal{O}(N^3)$/$\mathcal{O}(N^2)$.
