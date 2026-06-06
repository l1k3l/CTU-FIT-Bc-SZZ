---
studyplan: true
etapa: "4 · ML1 / ML2 — Dedecius + Holeňa"
qid: "8ML1"
examiner: "Dedecius/Holeňa"
topic: "Rozhodovací stromy, náhodné lesy, AdaBoost"
readiness: nezačato
tags: [otázka, kurz/ML1, otázka/8, todo]
---

# Rozhodovací stromy, náhodné lesy, AdaBoost

> **Otázka SZZ:** Rozhodovací stromy, náhodné lesy, AdaBoost.

Zdroje: BI-ML1 (FIT ČVUT), přednáška 2 — Rozhodovací stromy (sekce 5 Klasifikace/regrese, 6 Konstrukce stromu, 7 Vyhodnocení kvality, 8 Ladění hyperparametrů, 9 Nebinární příznaky, 10 Regrese); přednáška 9 — Ensemble metody (sekce 35 Ensemble metody obecně, 36 Bagging: náhodný les, 37 Boosting: AdaBoost).

Značení: $\mathcal{X}$ prostor příznaků; $X = (X_1,\dots,X_p)^T$ náhodný vektor $p$ příznaků; $Y$ vysvětlovaná (cílová) proměnná; $N$ počet trénovacích dvojic $(x_i, Y_i)$, $i = 1,\dots,N$; $\mathcal{D}$ množina (pod)dat ve vrcholu stromu, $\#\mathcal{D}$ její velikost; $\mathcal{D}_L, \mathcal{D}_R$ levá/pravá podmnožina po rozdělení; $t_L = \#\mathcal{D}_L/\#\mathcal{D}$, $t_R = \#\mathcal{D}_R/\#\mathcal{D}$ podíly; $p_i$ relativní četnost (odhad pravděpodobnosti) $i$-té hodnoty $Y$; $T_1,\dots,T_n$ podmodely ensemble; $w_i$ váhy datových bodů.

---

## 1. Rozhodovací stromy

### 1.1 Myšlenka a problém klasifikace/regrese

V supervizovaném učení hledáme vztah mezi vysvětlovanou proměnnou $Y$ a příznaky $X_1,\dots,X_p$ tak, aby „co nejvíce platilo“
$$Y \approx f(X_1, X_2, \dots, X_p).$$
Funkce $f$ nemusí připomínat funkce z analýzy — zde jí bude **strom**. Podle počtu hodnot $Y$ rozlišujeme:

- **klasifikace** (angl. *classification*) — $Y$ nabývá jen několika málo hodnot (např. pacient má/nemá nemoc);
- **regrese** (angl. *regression*) — $Y$ nabývá tolika hodnot, že ji považujeme za *spojitou*.

**[[Rozhodovací-strom|Rozhodovací stromy]]** (angl. *decision trees*) zvládají oba typy úloh. Strom je speciální zakořeněný **[[Strom]]** (v grafovém smyslu), v jehož vnitřních vrcholech jsou **rozhodovací pravidla** nad příznaky a v listech jsou predikované hodnoty $Y$.

### 1.2 Predikce = průchod stromem

Predikci pro datový bod $x$ získáme **průchodem stromu** od kořene: v každém vnitřním vrcholu vyhodnotíme rozhodovací pravidlo (např. „pohlaví = žena?“, „$X \le d$?“) a podle výsledku pokračujeme do levého/pravého potomka. Skončíme v listu, jehož přiřazená hodnota je výsledek predikce.

*Příklad (binární klasifikace).* Pro problém určení nemoci „rýmička“ s příznaky pohlaví, horečka ($>39\,^\circ\mathrm{C}$), schopnost vstát z postele lze sestrojit strom hloubky 2 se 4 listy; každý datový bod „propadne“ jednou cestou do listu, kde je rozhodnutí ANO/NE.

Hodnota listu se určuje z trénovacích bodů, které do něj při učení dopadly:

- **klasifikace:** rozhodnutí je **majoritní třída** v listu (hlasování); při shodě se rozhodne náhodně;
- **regrese:** rozhodnutí je **průměr** hodnot $Y$ z listu (viz §1.6).

### 1.3 Budování stromu shora dolů — hladový algoritmus

Cílem je vytvořit strom dané hloubky, který co nejvíce trénovacím datům správně přiřadí $Y$. Konstrukce hrubou silou je neprůchozí — stromů hloubky 1 je $p$, hloubky 2 je $p\cdot(p-1)^2$, atd. — a hledání **optimálního** stromu je dokonce **NP-úplný problém** (Hyafil, Rivest, 1976).

Proto se používá **hladový algoritmus** s historicky vylepšovanými verzemi: **ID3** → **C4.5** → **C5** (vše John Ross Quinlan), dnes nejčastěji **CART** (Classification and Regression Trees). Princip: pro danou množinu dat vybere jeden (dosud nepoužitý) příznak, který data rozdělí na dvě části tak, aby vzniklé rozdělení **maximalizovalo zvolené dělicí kritérium**. Na obě části se pak rekurzivně aplikuje stejný postup. Postup končí, nastane-li **ukončovací (zastavovací) podmínka** (maximální hloubka stromu, příliš málo dat v množině, příliš nízký informační zisk apod.).

**Algoritmus (hladová konstrukce stromu, ID3/CART — schéma).**
```
BUILD-TREE(D, hloubka):
    if zastavovací podmínka (D, hloubka):
        return list s hodnotou:
            klasifikace -> majoritní třída v D
            regrese     -> průměr Y v D
    pro každý dosud nepoužitý příznak X:
        urči nejlepší dělení D na D_L, D_R podle X
        spočti kritérium (informační zisk / Gini / pokles MSE)
    vyber příznak (a práh) s nejlepším kritériem
    vrchol <- toto pravidlo
    vrchol.levý  <- BUILD-TREE(D_L, hloubka+1)
    vrchol.pravý <- BUILD-TREE(D_R, hloubka+1)
    return vrchol
```
Hladový postup obvykle nenajde optimální strom, ale je rychlý a v praxi dobře použitelný; *hladový ≠ optimální* (existují data, kde optimální strom hladový algoritmus nenajde, např. $Y = 1 \iff (X_2 = X_3)$).

### 1.4 Dělicí kritéria — Gini index, entropie a informační zisk

Potřebujeme **míru neuspořádanosti (nečistoty)** množiny $\mathcal{D}$ obsahující hodnoty $Y$. Označme $p_0, p_1$ poměry počtu hodnot 0 resp. 1 ($p_0 + p_1 = 1$). Rozumná míra by měla být nezáporná, nulová pro „čistou“ množinu ($p_0 = 1$), maximální pro $p_0 = p_1 = \tfrac12$, rostoucí na $[0,\tfrac12]$ a klesající na $[\tfrac12,1]$.

**Entropie.** Pro binární $Y$:
$$H(\mathcal{D}) = -p_0 \log p_0 - p_1 \log p_1 = -p_0\log p_0 - (1-p_0)\log(1-p_0),$$
obecně pro $k$ hodnot
$$H(\mathcal{D}) = -\sum_{i=0}^{k-1} p_i \log p_i.$$
S dvojkovým logaritmem je jednotkou **bit**. Pozn.: $p_i$ jsou *odhady* pravděpodobností z dat, ne skutečné pravděpodobnosti.

*Příklad.* $\mathcal{D} = \{1_0,1_1,1_2,1_3,0_4,0_5,0_6,0_7\}$ má $p_0 = \tfrac12$, tedy $H(\mathcal{D}) = -\tfrac12\log\tfrac12 - \tfrac12\log\tfrac12 = -\log\tfrac12 = 1$. Pro $\mathcal{D}_1 = \{1_0,1_1,1_3,0_7\}$ ($p_0 = \tfrac14$) je $H(\mathcal{D}_1) = -\tfrac14\log\tfrac14 - \tfrac34\log\tfrac34 \doteq 0{,}811$.

**Gini index** (angl. *Gini impurity*). Alternativa s podobnými vlastnostmi:
$$GI(\mathcal{D}) = 1 - \sum_{i=0}^{k-1} p_i^2 = \sum_{i=0}^{k-1} p_i(1-p_i).$$
Interpretace: jakási míra pravděpodobnosti, že nově přidaný prvek bude špatně klasifikován. Jinak vše funguje stejně, jen se $H(\mathcal{D})$ nahradí $GI(\mathcal{D})$.

**Informační zisk** (angl. *information gain*). Chceme příznak, který rozdělením **nejvíce sníží neuspořádanost**. Zisk = entropie $\mathcal{D}$ mínus vážený součet entropií podmnožin:
$$IG(\mathcal{D}, X_i) = H(\mathcal{D}) - t_0\, H(\mathcal{D}_0) - t_1\, H(\mathcal{D}_1),$$
kde $\mathcal{D}_0, \mathcal{D}_1$ jsou podmnožiny s $X_i = 0$ resp. $X_i = 1$ a $t_j = \#\mathcal{D}_j / \#\mathcal{D}$. Hladový algoritmus vybírá příznak s **největším** $IG$.

*Příklad (volba prvního příznaku).* Pro data výše ($H(\mathcal{D}) = 1$): příznak $X_1$ dělí na poloviny s $H = 0{,}811$, takže
$$IG(\mathcal{D}, X_1) = 1 - \tfrac12\cdot0{,}811 - \tfrac12\cdot0{,}811 = 0{,}189,$$
zatímco $X_2, X_3$ dají $H(\mathcal{D}_0) = H(\mathcal{D}_1) = 1$, tedy $IG = 0$. Vítězem je $X_1$.

### 1.5 Stromy pro spojité příznaky

Základní algoritmus uměl pravidlo $X = 0$. Spojitý příznak $X$ (např. z $[0,100]$) vyžaduje pravidla tvaru $X \le d$, kterých je nekonečně mnoho. Algoritmus proto vyzkouší všechny *smysluplné* prahy:

1. Setřiď hodnoty příznaku $X$ v právě dělené množině: $x_1 < \dots < x_\ell$.
2. Pro každé $i = 2,\dots,\ell$ vyzkoušej pravidlo $X \le (x_{i-1} + x_i)/2$ (střed mezi sousedními hodnotami) a spočítej informační zisk.
3. Jako nejlepší pravidlo vezmi to s největším informačním ziskem.

Na rozdíl od binárního příznaku má u spojitého smysl, aby se táž proměnná objevila ve stromu **vícekrát** (např. po dělení $\text{věk} \le 30$ lze „starší“ část dělit znovu $\text{věk} \le 60$). Při mnoha hodnotách se prahy zkoušejí jen po každé $k$-té hodnotě (nebo náhodně), aby se ušetřil čas. Implementace v `sklearn` se ke všem příznakům chová jako ke spojitým, takže si dobře poradí i s ordinálními. Při shodě zisku vybírá `sklearn` náhodně (nedeterminismus).

*Pozn. (nebinární kategorické příznaky).* Příznaky s několika málo hodnotami bez kvantitativního významu (**nominální**) se kódují **one-hot encoding** (dummy proměnné) — jeden příznak s $n$ hodnotami se nahradí $n$ binárními indikátory. Zvyšuje to dimenzi a může podporovat přeučení. **Ordinální** příznaky (s přirozeným uspořádáním) je lepší očíslovat a nechat zpracovat jako spojité.

### 1.6 Stromy pro spojitou vysvětlovanou proměnnou (regresní stromy)

Pro spojité $Y$ musíme vyřešit dva problémy:

**(a) Predikce listu.** Skončí-li v listu trénovací body s hodnotami např. $\{10,15,20,25,30,35\}$, predikce je jejich **průměr** (zde $22{,}5$).

**(b) Dělicí kritérium.** Entropie/Gini jsou pro spojité $Y$ nepoužitelné. Snahou je, aby hodnoty v listu byly co nejblíže střední hodnotě — mírou je **MSE = mean squared error** (téměř výběrový rozptyl):
$$\mathrm{MSE}(\mathbf{Y}) = \frac{1}{N}\sum_{j=1}^N (Y_j - \overline{Y})^2.$$
Hladový algoritmus pak místo entropie minimalizuje
$$\mathrm{MSE}(\mathcal{D}) - t_L\,\mathrm{MSE}(\mathcal{D}_L) - t_R\,\mathrm{MSE}(\mathcal{D}_R),$$
kde $t_L = \#\mathcal{D}_L/\#\mathcal{D}$, $t_R = \#\mathcal{D}_R/\#\mathcal{D}$ a $\mathrm{MSE}(\mathcal{D})$ se počítá z hodnot $Y$ všech bodů v $\mathcal{D}$. Místo MSE lze použít **MAE = mean absolute error** $\tfrac1N\sum_i |Y_i - \overline{Y}|$.

*Příklad.* $\mathrm{MSE}(\{10,15,20,25,30,35\})$ s $\overline{Y} = 22{,}5$ je $\tfrac16\big((10-22{,}5)^2 + \dots + (35-22{,}5)^2\big) = 72{,}9$.

### 1.7 Hyperparametry, přeučení, prořezávání

**Vyhodnocení kvality.** U klasifikace měříme **klasifikační přesnost** (angl. *classification accuracy*)
$$\text{accuracy} = \frac{\text{počet správně klasifikovaných dat}}{\text{počet všech dat}}.$$
Chceme ale přesnost na **všech možných datech**, ne jen na těch, která máme. Proto data dělíme na **trénovací** a **testovací** (angl. *train*/*test set*): na trénovacích model naučíme, na testovacích změříme přesnost — to dá spolehlivější odhad chování na neviděných datech. Chybovostem (= 1 − přesnost) říkáme **trénovací** a **testovací chyba**.

**Přeučení** (angl. *overfitting*). Čím hlubší strom, tím nižší trénovací chyba (až k nule), neboť strom se příliš *přizpůsobí* trénovacím datům místo aby zachytil skrytý vztah. Testovací chyba se ale s rostoucí složitostí nejdříve snižuje a od jistého bodu zase roste. Najít tento bod zlomu je úkolem celého procesu budování modelu.

**Ladění hyperparametrů.** Parametrům jako `max_depth`, které určují *tvar/komplexitu* modelu (a neučí se z dat), říkáme **hyperparametry**. Naivní postup „vyber `max_depth` s nejmenší testovací chybou“ vede k *příliš optimistickému* odhadu, protože model je vybrán na základě testovacích dat. Proto se data dělí na **tři** podmnožiny — trénovací, **validační** a testovací:

1. Pro různé hodnoty hyperparametru nauč strom na trénovacích datech.
2. Změř chybu (přesnost) na **validačních** datech, vyber hodnotu s nejmenší chybou.
3. Pro **finální** model změř chybu na **testovacích** datech (která dosud ležela ladem) — to je rozumný odhad skutečné chyby.

Určování hyperparametrů na validačních datech se říká **ladění** (angl. *tuning*). Dělení na podmnožiny je dobré dělat **náhodně** (typicky 20 % test, 20 % zbytku validace; lze 25 % i 30 %). Často používanou alternativou je **[[Křížová-validace|křížová validace]]** (angl. *cross-validation*). Dostupné hyperparametry stromu v `sklearn`: `criterion`, `max_depth`, `min_samples_split`, `min_samples_leaf`, `max_features`, `max_leaf_nodes`, `min_impurity_decrease`, … — část z nich realizuje **prořezávání** (omezení růstu / zjednodušení stromu jako prevence přeučení).

**Výhody a nevýhody stromů.** Výhody: nenáročnost na přípravu dat (kategorické i spojité příznaky, chybějící hodnoty), jednoduchost, rychlé učení, dobrá interpretovatelnost. Nevýhody: *nerobustnost* (drobná změna trénovacích dat může zásadně změnit strukturu stromu), většina implementací jen binární stromy, hledání optima je NP-úplné, snadné přeučení.

---

## 2. Ensemble metody a bagging — náhodný les

### 2.1 Základní myšlenka ensemble metod

**Ensemble metody** spočívají v tom, že místo jednoho modelu (např. rozhodovacího stromu) použijeme **více modelů** a jejich predikce zkombinujeme do finálního rozhodnutí. Dva nejobvyklejší přístupy:

- **bagging** (*bootstrap aggregating*) — reprezentant **náhodný les** (*Random Forest*);
- **boosting** — reprezentant **AdaBoost** (*Adaptive Boosting*).

Oba si ilustrujeme na skládání rozhodovacích stromů.

### 2.2 Bootstrap — výběr s opakováním

Ze vstupního trénovacího datasetu $\mathcal{D}$ vytvoříme $n$ datasetů $\mathcal{D}_1,\dots,\mathcal{D}_n$ (obvykle stejně velkých jako $\mathcal{D}$) pomocí metody **bootstrap**, neboli **výběru s opakováním**: opakovaně náhodně vybíráme řádek z tabulky, přičemž se řádky v jednom výběru **mohou opakovat**.

*Příklad.* Z datasetu se 4 řádky vytvoříme bootstrapem dataset velikosti pět tak, že pětkrát náhodně vybereme řádek s opakováním (např. id 1, 4, 3, 3, 1).

### 2.3 Učení podmodelů a agregace

**Náhodný les pro klasifikaci** (binární $Y \in \{0,1\}$):

1. Bootstrapem vytvoř $n$ datasetů $\mathcal{D}_1,\dots,\mathcal{D}_n$.
2. Na každém $\mathcal{D}_i$ nauč rozhodovací strom $T_i$. Pro trénování se typicky použije jen **omezená náhodně vzatá podmnožina příznaků**; stromy bývají mělké (hloubka 1–3, ale nemusí). Stromům říkáme **podmodely** (angl. *base learners*).
3. Při predikci bod $x$ proženeme všemi stromy a uložíme predikce $\hat{Y}_1,\dots,\hat{Y}_n$.
4. Stromy tvoří **náhodný les**; finální rozhodnutí je **většinové hlasování** (majority vote): je-li v $\{\hat{Y}_1,\dots,\hat{Y}_n\}$ více jedniček než nul, je predikce $\hat{Y} = 1$.

**Algoritmus (náhodný les — schéma).**
```
NÁHODNÝ-LES(D, n):
    for i = 1, ..., n:
        D_i <- bootstrap(D)               # výběr s opakováním
        F_i <- náhodná podmnožina příznaků (velikost ~ sqrt(p))
        T_i <- BUILD-TREE na D_i jen s příznaky F_i
    return {T_1, ..., T_n}

PREDIKCE(x):
    klasifikace: většinové hlasování predikcí T_1,...,T_n  (majority vote)
    regrese:     průměr predikcí  Ŷ = (1/n) Σ Ŷ_i
```

**Regrese.** Pro spojité $Y$ se predikce lesa bere jako **průměr** predikcí jednotlivých stromů:
$$\hat{Y} = \frac{1}{n}\sum_{i=1}^n \hat{Y}_i.$$
Implementace `RandomForestClassifier` ve `scikit-learn` navíc průměruje *pravděpodobnosti* tříd: označíme-li $\hat{p}_i = \hat{P}(Y=1 \mid T_i, X = x)$, je $\hat{p} = \tfrac1n\sum_i \hat{p}_i$ a $\hat{Y} = 1$ pro $\hat{p} > 0{,}5$, jinak $0$.

### 2.4 Hyperparametry

- `n_estimators` — počet stromů v lese;
- `max_depth` — maximální hloubka stromů (typicky spíše nízká);
- `max_features` — počet náhodně vybraných příznaků, ze kterých hladový algoritmus vybírá dělicí příznak; defaultně $\sqrt{p}$;
- lze nastavit i ostatní obvyklé hyperparametry stromů (jakožto podmodelů).

### 2.5 Proč to funguje — snížení rozptylu

U baggingu je vhodné, aby podmodely **nebyly stejné**, ale naopak co nejpestřejší. Toho se dosáhne **randomizací**: u náhodných lesů je daná (a) bootstrapem generujícím odlišné trénovací datasety a (b) hodnotou `max_features`. Jelikož rozhodovací stromy jsou velmi citlivé na změny v trénovacích datech (**mají velký rozptyl**), stačí odlišnost datasetů daná bootstrapem k získání velmi odlišných stromů. Průměrováním (resp. hlasováním) predikcí těchto rozdílných podmodelů se snažíme **redukovat rozptyl** (a povětšinou se to úspěšně daří). Přestože jednotlivé stromy mohou být slabé modely (*weak learners*), jejich kolektivní rozhodování dává překvapivě dobré výsledky. Náhodné lesy jsou na rozdíl od jednoho stromu **robustní a odolné vůči přeučení** — cenou je ztráta jednoduchosti a snadné interpretovatelnosti.

---

## 3. Boosting — AdaBoost

### 3.1 Základní myšlenka boostingu

Stejně jako u baggingu konstruujeme více podmodelů (opět rozhodovací stromy, i když AdaBoost umí i jiné modely) a finální rozhodnutí je **(vážená) kompozice** rozhodnutí jednotlivých modelů. Na rozdíl od baggingu ale podmodely **nejsou nezávislé** — jsou **seřazené** a každý další je ovlivněn předchozími. Vliv je realizován pomocí **vah datových bodů**: při konstrukci $n$-tého stromu je **zvýšena váha** těm bodům, které předchozí $(n-1)$-tý strom **klasifikoval špatně**. Tak se další model soustředí na body, se kterými si předchozí modely neporadily. Konkrétní implementací je **AdaBoost** (Freund, Schapire 1997).

### 3.2 Váhy datových bodů a `sample_weight`

Pro $N$ trénovacích bodů máme pole nezáporných vah $w_1,\dots,w_N$ (`sample_weight`), které určují, jak je který bod „důležitý“ (default $w_i = 1$). Při učení stromu se váhy projeví ve výpočtu informačního zisku $H(\mathcal{D}) - t_L H(\mathcal{D}_L) - t_R H(\mathcal{D}_R)$: entropie i podíly $t_L, t_R$ se počítají **váženě**. Např. odhad pravděpodobnosti třídy 1 v $\mathcal{D}_L$ je součet vah bodů třídy 1 v $\mathcal{D}_L$ dělený sumou vah všech bodů v $\mathcal{D}_L$; podíl $t_L$ je suma vah bodů v $\mathcal{D}_L$ dělená sumou vah všech bodů v $\mathcal{D}$. Strom se pak učí tak, aby správně predikoval zejména body s **vyšší vahou**.

### 3.3 Algoritmus AdaBoost

Na začátku máme dataset $\mathcal{D}$ s $N$ body; uvažujeme binární klasifikaci. Počet stromů je zadán hyperparametrem `n_estimators`.

**Algoritmus (AdaBoost — učení).**
```
ADABOOST(D, n_estimators, learning_rate):
    1. w_i <- 1/N pro všechna i;  m <- 1          # rovnoměrné váhy
    2. while m <= n_estimators:
    3.     nauč strom T^(m) na D s vahami w_i
    4.     e^(m) <- součet vah bodů špatně klasifikovaných stromem T^(m)
    5.     if e^(m) == 0: konec                    # vše klasifikováno správně
    6.     α^(m) <- learning_rate · log( (1 - e^(m)) / e^(m) )
    7.     pro body špatně klasifikované T^(m):  w_i <- w_i · exp(α^(m))
    8.     znormalizuj váhy w_i tak, aby Σ w_i = 1
    9.     m <- m + 1
    return stromy T^(1), T^(2), ...  s vahami α^(1), α^(2), ...
```

- **Chyba modelu** $e^{(m)}$ = součet vah špatně klasifikovaných bodů.
- **Příspěvek (váha) modelu** $\alpha^{(m)} = \texttt{learning\_rate} \cdot \log\dfrac{1 - e^{(m)}}{e^{(m)}}$: čím menší chyba $e^{(m)}$, tím větší $\alpha^{(m)}$, tedy tím větší vliv stromu na finální rozhodnutí.
- **Aktualizace vah:** špatně klasifikovaným bodům váha *roste* ($w_i \leftarrow w_i \exp(\alpha^{(m)})$), poté se váhy normalizují na součet 1. Příště se model víc soustředí na dosud problematické body.
- `learning_rate` je hyperparametr (default obvykle u boostingu): nižší hodnota zpomalí trénování a brání přeučení — jde o **regularizaci**; cenou je obvykle nutnost zvýšit `n_estimators`.

**Finální vážené hlasování.** Rozhodnutí pro bod $x$:

1. Každému stromu $T^{(m)}$ přiřaď váhu $\alpha^{(m)}$ z kroku 6.
2. Sečti váhy $\alpha^{(m)}$ všech stromů, které pro $x$ predikují $Y = 1$, a zvlášť těch, které predikují $Y = 0$.
3. Rozhodni se pro tu možnost, pro kterou je součet vah vyšší.

*Poznámky.* Vícetřídní verze je **AdaBoost-SAMME** (Zhu et al. 2006), regresní **AdaBoost.R2** (Drucker 1997). AdaBoost může použít jakýkoli model s `sample_weight`; ve `sklearn` jsou výchozí stromy hloubky 3 (`base_estimator`). Podmodely jsou typicky **slabé modely** (mělké stromy); boosting postupně koriguje chyby předchozích modelů, čímž **redukuje vychýlení (bias)** (na rozdíl od baggingu, který redukuje rozptyl).

### 3.4 Rozdíl bagging vs. boosting

| | **Bagging (náhodný les)** | **Boosting (AdaBoost)** |
|---|---|---|
| podmodely | **nezávislé**, učené paralelně | **závislé**, učené **sekvenčně** |
| trénovací data | bootstrap (výběr s opakováním) | celé $\mathcal{D}$ s **měnícími se vahami** bodů |
| diverzita | bootstrap + náhodné příznaky | zvyšování vah špatně klasifikovaných bodů |
| agregace | majority vote / průměr (rovné váhy) | **vážené** hlasování (váhy $\alpha^{(m)}$) |
| co redukuje | **rozptyl** (variance) | **vychýlení** (bias) |
| podmodely bývají | mělké, ale „pestré“ | slabé (*weak learners*) |

---

## Co je potřeba na zkoušku znát

### Definice
- **Rozhodovací strom:** zakořeněný strom, ve vnitřních vrcholech rozhodovací pravidla nad příznaky, v listech predikce $Y$ (majoritní třída / průměr). Predikce = průchod od kořene do listu.
- **Entropie** $H(\mathcal{D}) = -\sum_i p_i \log p_i$; **Gini index** $GI(\mathcal{D}) = 1 - \sum_i p_i^2$.
- **Informační zisk** $IG(\mathcal{D}, X_i) = H(\mathcal{D}) - t_0 H(\mathcal{D}_0) - t_1 H(\mathcal{D}_1)$.
- **MSE** $\tfrac1N\sum_j (Y_j - \overline{Y})^2$ — dělicí kritérium pro regresní stromy.
- **Bootstrap:** výběr řádků s opakováním. **Náhodný les:** ensemble stromů na bootstrap datasetech + náhodných příznacích, agregace hlasováním/průměrem.
- **AdaBoost:** sekvenční ensemble s vahami bodů a vahami $\alpha^{(m)}$ modelů.

### Věty / fakta
- Hledání **optimálního** stromu je **NP-úplný** problém → hladové algoritmy (ID3, C4.5, CART), *hladový ≠ optimální*.
- Hlubší strom → nižší trénovací chyba, ale **přeučení**; testovací chyba má minimum → ladění hyperparametrů na **validačních** datech.
- **Bagging** redukuje **rozptyl** (využívá velkého rozptylu stromů + randomizace); **boosting** redukuje **vychýlení**.
- AdaBoost: $\alpha^{(m)} = \texttt{lr}\cdot\log\frac{1-e^{(m)}}{e^{(m)}}$ — menší chyba ⇒ větší příspěvek; špatně klasifikovaným bodům roste váha.

### Algoritmy
- **Hladová konstrukce stromu** (ID3/CART): rekurzivně vyber příznak (a práh) maximalizující kritérium, dokud nenastane zastavovací podmínka.
- **Spojité příznaky:** setřiď hodnoty, zkoušej prahy $X \le (x_{i-1}+x_i)/2$, vyber dle informačního zisku.
- **Náhodný les:** $n$× bootstrap + strom na náhodné podmnožině příznaků; agregace majority vote / průměr; hyperparametr `n_estimators`, `max_features` $=\sqrt{p}$.
- **AdaBoost:** rovnoměrné váhy → opakuj (nauč strom s vahami, spočti $e^{(m)}$, $\alpha^{(m)}$, zvyš váhy chybných bodů, normalizuj) → finální vážené hlasování.
