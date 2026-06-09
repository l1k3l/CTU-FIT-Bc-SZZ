---
studyplan: true
etapa: "4 · ML1 / ML2 — Dedecius + Holeňa"
qid: "13ML1"
examiner: "Dedecius/Holeňa"
topic: "Evaluace modelů: testovací chyba, křížová validace, metriky"
readiness: nezačato
tags: [otázka, kurz/ML1, otázka/13, todo]
---

# Evaluace modelů — testovací chyba, křížová validace, vyhodnocovací metriky

> **Otázka SZZ:** Evaluace modelů – testovací chyba a její odhad, křížová validace, vyhodnocovací metriky regrese a klasifikace.

Zdroje: BI-ML1 (FIT ČVUT), přednáška 8 — Evaluace modelů (ztrátová funkce, trénovací/validační/testovací data, hold-out, křížová validace, evaluace regrese, evaluace klasifikace); printed str. 57–66.

Značení: $Y$ vysvětlovaná proměnná, $\boldsymbol X = (X_1,\dots,X_p)^T$ vektor příznaků (vstupů), $\hat Y \equiv \hat Y(\boldsymbol X)$ predikce modelu, $\hat p = \hat{\mathrm P}(Y=1\mid\boldsymbol X)$ odhadnutá pravděpodobnost, $L(Y,\hat Y)$ ztrátová funkce, $\mathcal L$ trénovací ztráta (průměrná ztráta), $\overline{\mathrm{err}}_{\mathrm{train}}$ trénovací chyba, $\overline{\mathrm{err}}_{\mathrm{test}}$ testovací chyba, $\mathrm{Err}_{\mathcal D}$ testovací chyba podmíněná trénovacími daty, $\mathrm{Err}$ očekávaná testovací chyba, $\mathcal D = \big((Y_1,\boldsymbol x_1),\dots,(Y_N,\boldsymbol x_N)\big)$ trénovací data, $N$ počet pozorování, $k$ počet částí při křížové validaci.

---

## 1. Testovací chyba a její odhad

### 1.1 Cíl evaluace — schopnost generalizace

Jednou z hlavních výzev strojového učení je, aby natrénovaný model dobře fungoval i na **nových** vstupech, které dosud neviděl. Této schopnosti říkáme **schopnost generalizace**. V typickém scénáři máme několik kandidátů na finální model a potřebujeme mezi nimi vybrat ten nejlepší — k tomu je třeba mít **kvantitativní míru výkonnosti** modelu. Zaměřujeme se na **supervizované učení** (regrese, klasifikace).

Volba míry se může zdát přímočará (přesnost pro klasifikaci, MSE pro regresi), ale ve skutečnosti je třeba zvolit metriku odpovídající žádoucímu chování modelu. Např. u regrese můžeme chtít model, který nedělá velké chyby, ale poměrně často dělá chyby menší — anebo model, který většinou nedělá ani malé chyby, ale občas udělá hodně velkou.

### 1.2 Ztrátová funkce

Mějme vysvětlovanou proměnnou $Y$ a vektor příznaků $\boldsymbol X = (X_1,\dots,X_p)^T$. Model predikuje $\hat Y \equiv \hat Y(\boldsymbol X)$, což je funkce $\boldsymbol X$. Chybu predikce $Y$ pomocí $\hat Y$ obecně měříme tzv. **ztrátovou funkcí** (angl. *loss function*) $L$, která vhodným způsobem měří, jak dobře daný model predikuje konkrétní hodnotu.

**Regrese.** Typickou volbou je **kvadratická ztrátová funkce** měřící *kvadratickou chybu* (angl. *squared error*)
$$L(Y,\hat Y) = (Y - \hat Y)^2,$$
nebo $L_1$ ztrátová funkce měřící *absolutní chybu* (angl. *absolute error*)
$$L_1(Y,\hat Y) = |Y - \hat Y|.$$
Kvadratickou chybu využívá např. **[[Lineární-regrese|lineární regrese]]**.

**Binární klasifikace.** Model často odhaduje pravděpodobnost
$$\hat p = \hat{\mathrm P}(Y=1 \mid \boldsymbol X = \boldsymbol x).$$
(To umí např. **[[Rozhodovací-strom|rozhodovací strom]]**, který pro list, do kterého padne $\boldsymbol x$, vrátí $\hat p$ jako relativní počet reprezentantů třídy 1 z trénovací množiny v tom listu.) Finální predikce vysvětlované proměnné je potom
$$\hat Y = \begin{cases} 1 & \text{když } \hat p > 1/2, \\ 0 & \text{jinak.}\end{cases}$$
Typickou ztrátovou funkcí je **binární křížová entropie** (angl. *binary cross-entropy loss*)
$$L(Y,\hat p) = -Y\log\hat p - (1-Y)\log(1-\hat p),$$
což reálně znamená $L(1,\hat p) = -\log\hat p$ a $L(0,\hat p) = -\log(1-\hat p)$. Binární cross-entropy lze použít jen pro modely, které **odhadují pravděpodobnost** $\hat p \in (0,1)$ (typicky **[[Logistická-regrese|logistická regrese]]**, neuronové sítě, rozhodovací stromy s pravděpodobnostmi v listech), nikoli pro modely vracející jen tvrdou třídu $\hat Y\in\{0,1\}$ bez skóre.

> *Rozdíl metrika vs. ztrátová funkce (loss).* **Ztrátová funkce** se používá při **trénování** — minimalizuje se (typicky gradientním sestupem) přes parametry modelu, takže musí být (po částech) diferencovatelná a hladká. **Metrika** je míra výkonnosti, kterou až **po natrénování** vyhodnocujeme (typicky na testovacích datech) a kterou nemusíme umět optimalizovat (např. accuracy, AUC). Tytéž ztrátové funkce ale můžeme použít i jako metriku k měření **testovací chyby**, pokud pro nás dávají smysl (MSE/MAE jsou současně loss i regresní metrika; cross-entropy lze měřit i na test setu). Pojmem „**testovací chyba**" rozumíme hodnotu zvolené **metriky vyčíslenou nad TEST setem** (ne nad trénovacím).

### 1.3 Trénovací chyba a proč podhodnocuje

Při učení se snažíme minimalizovat chybu predikce měřenou pomocí **průměrné hodnoty ztrátové funkce** $L$ na trénovacích datech (trénovací množina = $N$ dvojic $(Y_i,\boldsymbol x_i)$):
$$\mathcal L = \frac{1}{N}\sum_{i=1}^N L\big(Y_i, \hat Y(\boldsymbol x_i)\big).$$
Tato průměrná hodnota se nazývá **trénovací chyba** (angl. *training error*) a značí se $\overline{\mathrm{err}}_{\mathrm{train}}$ (též *trénovací ztráta*). Pro regresi s kvadratickou ztrátou jde o *střední kvadratickou chybu*
$$\mathrm{MSE}_{\mathrm{train}} = \frac{1}{N}\sum_{i=1}^N (Y_i - \hat Y_i)^2,$$
což je ekvivalentní minimalizaci RSS v lineární regresi; pro $L_1$ ztrátu jde o *střední absolutní chybu*
$$\mathrm{MAE}_{\mathrm{train}} = \frac{1}{N}\sum_{i=1}^N |Y_i - \hat Y_i|.$$
Pro binární klasifikaci vede předchozí ztráta na minimalizaci **binární relativní entropie**
$$\mathcal L = -\frac{1}{N}\sum_{i=1}^N \Big[ Y_i\log\hat p(\boldsymbol x_i) + (1-Y_i)\log(1-\hat p(\boldsymbol x_i)) \Big].$$

> **Poznámka (vztah ke maximální věrohodnosti).** Až na mínus před sumou se jedná přesně o **logaritmus věrohodnostní funkce**, který se maximalizuje u **[[Logistická-regrese|logistické regrese]]**. S mínusem a minimalizací jde tedy o **totožnou úlohu** (minimalizace cross-entropy = maximalizace **[[Maximální-věrohodnost|věrohodnosti]]**).

Při procesu **učení modelu** se zafixovanými hyperparametry hledáme hodnoty parametrů, které minimalizují trénovací chybu. U některých modelů (např. lineární regrese) lze toto řešení najít *explicitně*; pro většinu modelů ale ne a používají se iterativní metody (typicky založené na gradientním sestupu) hledající lokální minimum. **Trénovací chyba je optimisticky vychýlený (podhodnocený) odhad chyby na nových datech**: model je laděn právě na trénovacích datech, takže se k nim přizpůsobí — v krajním případě je *přeučí* (overfitting) a na trénovacích datech vykáže nízkou chybu, která ale neodráží skutečnou schopnost generalizace.

**Detekce přeučení (overfitting).** Přeučení poznáme z **rozdílu mezi trénovací a testovací chybou**: trénovací chyba je **malá** (model si data „zapamatoval"), zatímco testovací chyba je **velká** (na nových datech selhává). Naopak malá trénovací i testovací chyba značí dobrou generalizaci. **Otestovat model „jako v produkci"** = vyčíslit zvolené metriky na **odděleném test setu**, který model při tréninku ani výběru nikdy neviděl — to simuluje příchod nových, dosud neviděných dat.

### 1.4 Testovací chyba a její odhad

Jakmile je model natrénován, zajímá nás jeho schopnost generalizace, kterou odhadujeme pomocí ztrátové funkce na *nových* datech.

**Definice (testovací chyba).** *Testovací chyba* (angl. *test error*), též *generalizační chyba* (angl. *generalization error*), je definována jako střední hodnota chyby na novém vstupu $\boldsymbol X$ **podmíněná** danými trénovacími daty:
$$\mathrm{Err}_{\mathcal D} = \mathrm E\big( L(Y,\hat Y(\boldsymbol X)) \mid \mathcal D\big),$$
kde $\mathcal D = \big((Y_1,\boldsymbol x_1),\dots,(Y_N,\boldsymbol x_N)\big)$ značí trénovací data.

**Odhad výběrovým průměrem.** Testovací chybu odhadneme výběrovým průměrem ztráty změřeným na **testovacích datech** $\big((Y_1,\boldsymbol x_1),\dots,(Y_{N_{\mathrm{test}}},\boldsymbol x_{N_{\mathrm{test}}})\big)$, která byla získána **nezávisle** na trénovacích datech $\mathcal D$:
$$\overline{\mathrm{err}}_{\mathrm{test}} = \frac{1}{N_{\mathrm{test}}}\sum_{i=1}^{N_{\mathrm{test}}} L\big(Y_i, \hat Y(\boldsymbol x_i)\big).$$
Podmíněno trénovacími daty $\mathcal D$ je $\overline{\mathrm{err}}_{\mathrm{test}}$ **nestranný odhad** $\mathrm{Err}_{\mathcal D}$, tj.
$$\mathrm E\big(\overline{\mathrm{err}}_{\mathrm{test}} \mid \mathcal D\big) = \mathrm{Err}_{\mathcal D}.$$

**Definice (očekávaná testovací chyba).** Nejobecnější mírou schopnosti modelu generalizovat je *očekávaná testovací chyba* (též *očekávaná chyba predikce*, angl. *expected test/prediction error*) definovaná jako střední hodnota testovací chyby vzhledem k náhodnému výběru trénovací množiny:
$$\mathrm{Err} = \mathrm E\big(\mathrm{Err}_{\mathcal D}\big) = \mathrm E\,L\big(Y,\hat Y(\boldsymbol X)\big).$$

### 1.5 Rozdělení dat: hold-out (trénovací / validační / testovací)

Chceme-li natrénovat model a pak odhadnout jeho testovací chybu, musíme mít k dispozici **trénovací data** a **nezávislá testovací data**. Z pohledu evaluace máme dva úkoly:

- **Výběr modelu** (*model selection*) — odhadnout výkonnost různých modelů za účelem výběru nejlepšího.
- **Ohodnocení modelu** (*model assessment*) — odhadnout testovací chybu finálního modelu.

Protože výběr modelu spadá do procesu trénování (vybíráme model, který se nejlépe přizpůsobí datům), **nesmíme použít stejná data pro výběr finálního modelu i pro jeho ohodnocení**. Když máme *dostatek dat*, rozdělíme je na tři části — způsob se nazývá **hold-out**:

| část | použití |
|---|---|
| **trénovací** | trénování konkrétních modelů se zafixovanými hyperparametry |
| **validační** | ohodnocení a porovnání modelů → výběr nejlepších hyperparametrů a nejlepšího modelu napříč třídami |
| **testovací** | až v závěrečné fázi pro odhad testovací chyby finálního, již vybraného a natrénovaného modelu |

**Časté chyby.** Validační část je správně použita k ladění hyperparametrů *v rámci jedné třídy* modelů. Pokud se ale modely s nejlepšími hyperparametry z různých tříd (např. KNN a rozhodovací strom) porovnávají *na základě testovacích dat*, je finální ohodnocení příliš optimistické (výběr nejlepšího modelu je součást trénování). **Testovací množinu musíme vždy oddělit co nejdříve** (ještě před předzpracováním) a držet ji striktně bokem pouze pro finální evaluaci.

**Rizika.** Evaluace dává rozumné výsledky jen pokud trénovací, validační i testovací data **pocházejí ze stejného rozdělení** a nejsou tam procesně vnesené odlišnosti. Tři části proto musí být **navzájem disjunktní** (žádný bod ve dvou částech) a vybrané **náhodně** (data před rozdělením náhodně permutovat, aby se nepřenesla umělá uspořádanost). **Výjimka — chronologická data:** u *nestacionárních* jevů (např. ceny na burze), kde se sledovaný systém v čase vyvíjí, data před rozdělením **nepermutujeme** a testovací (případně validační) data správně **reflektují chronologické řazení** (test = nejnovější data), aby odhad chyby reálně ukázal posun v čase. U vícekrokového modelování (doplňování chybějících hodnot, výběr příznaků) musíme validační a testovací data oddělit *již na začátku* a všechny kroky „naučené“ na trénovacích datech na ně až poté aplikovat.

---

## 2. Křížová validace

### 2.1 Motivace

Když nemáme dostatek dat, nebývá rozumné dělit je na tři části. Uvažujme scénář, kdy si testovací data dopředu oddělíme a jde nám pouze o **trénování a výběr nejlepšího modelu** — k tomu můžeme použít techniku **[[Křížová-validace|křížové validace]]** (angl. *cross-validation*). Oproti jediné validační množině křížová validace **efektivněji využívá data** (každé pozorování slouží jak k trénování, tak k validaci) a dává **méně rozptýlený odhad** chyby (průměr přes $k$ částí).

### 2.2 $k$-násobná křížová validace

Základní metodou je **$k$-násobná křížová validace** (angl. *$k$-fold cross-validation*), kde $2 \le k \le N$:

- Trénovací data $\mathcal D$ náhodně rozdělíme na $k$ *podobně* velkých částí $\mathcal D_1,\dots,\mathcal D_k$.
- Pro každé $j = 1,\dots,k$ model s danými hodnotami hyperparametrů natrénujeme na datech z množiny $\big(\bigcup_{i=1}^k \mathcal D_i\big)\setminus\mathcal D_j$ (tj. všechny části kromě $\mathcal D_j$).
- Na množině $\mathcal D_j$ odhadneme jeho chybu jako $e_j$.
- Nakonec vrátíme **průměrnou „cross-validační“ chybu**
$$\hat e = \frac{1}{k}\sum_{i=1}^k e_i.$$

Tento proces zopakujeme pro všechny zkoumané hodnoty hyperparametrů a na závěr vybereme jako **nejlepší** ty hodnoty, které vedly k **nejmenší** cross-validační chybě. Abychom pak získali finální natrénovaný model (ten v tuto chvíli nemáme), pro vybrané hodnoty hyperparametrů model **znovu natrénujeme na celé trénovací množině** $\mathcal D$.

**Algoritmus (k-fold CV pro výběr hyperparametrů).**
```
vstup: trénovací data D, mřížka hyperparametrů H, počet částí k
náhodně rozděl D na k podobně velkých částí D_1, ..., D_k
for každé nastavení hyperparametrů h v H:
    for j = 1, ..., k:
        natrénuj model s h na D \ D_j           # všechny části kromě D_j
        e_j(h) = chyba modelu na D_j             # ztráta na vynechané části
    ê(h) = (1/k) * sum_{j=1}^k e_j(h)            # průměrná CV chyba
h* = argmin_h ê(h)                               # nejlepší hyperparametry
finální model = natrénuj s h* na celé D          # přetrénuj na všech datech
return h*, finální model
```

Typické volby $k$ jsou 5 až 10.

### 2.3 Leave-one-out

V extrémním případě, kdy se $k$ rovná počtu trénovacích dat ($k = N$), mluvíme o **leave-one-out cross-validation** (LOO): trénuje se na celé trénovací množině *bez jediného bodu*, na kterém se pak měří výsledná chyba; toto se zopakuje $N$krát. LOO maximálně využívá data, ale je výpočetně velmi náročné.

### 2.4 Diskuse a dvoustupňová křížová validace

- Křížová validace může být neúnosně výpočetně náročná a nemůže tak vždy nahradit strategii s jedinou validační množinou.
- Pro *fixní* model je cross-validační chyba odhadem **očekávané testovací chyby** $\mathrm{Err}$, a nikoli testovací chyby $\mathrm{Err}_{\mathcal D}$ (což může být matoucí).
- Když máme opravdu málo dat a nechceme ani oddělovat testovací množinu, můžeme křížovou validaci použít **dvoustupňově** a současně tak vybrat nejlepší model i odhadnout jeho výkonnost: *vnitřní* křížová validace slouží na výběr nejlepšího modelu, *vnější* na odhad očekávané chyby. Výsledná vnější cross-validační chyba ale odpovídá očekávané chybě **celé procedury** pro výběr nejlepšího modelu, nikoli chybě konkrétního modelu (ten z toho ani nevypadne — pro predikci ho musíme na celých datech získat zvlášť).

### 2.5 Strategie přípravy finálního modelu

- **hold-out (s validační množinou):** dataset rozdělíme na trénovací a validační část; modely (hyperparametry) trénujeme na trénovací a validační částí vybereme nejlepší. Tento model lze ještě znovu natrénovat na celých datech.
- **hold-out s křížovou validací / dvoustupňová křížová validace:** vezmeme celý dataset, křížovou validací vybereme nejlepší model (hyperparametry) a ten pak na celých datech natrénujeme.
- Ve žádném ze scénářů si neodložíme data pro měření výkonnosti finálního modelu; jako odhad jeho výkonnosti použijeme odhad (očekávané) testovací chyby z předchozího kroku.

---

## 3. Vyhodnocovací metriky regrese

Nejobvyklejší volba kvadratické chyby jako ztrátové funkce vede na evaluaci pomocí **střední kvadratické chyby** (angl. *mean squared error*)
$$\mathrm{MSE} = \frac{1}{N}\sum_{i=1}^N (Y_i - \hat Y_i)^2.$$
Tato míra penalizuje především velké odchylky a je velmi citlivá na odlehlé hodnoty.

**Root mean squared error** — odpovídá nelineárně přeškálovanému MSE:
$$\mathrm{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^N (Y_i - \hat Y_i)^2}.$$
Má stejné vlastnosti jako MSE, akorát **jednotky jsou stejné jako jednotky vysvětlované proměnné** (snazší interpretace).

**Root mean squared logarithmic error** — pro nezáporné hodnoty vysvětlované proměnné:
$$\mathrm{RMSLE} = \sqrt{\frac{1}{N}\sum_{i=1}^N (\log Y_i - \log\hat Y_i)^2}.$$
Soustředí se na *relativní* míru odchylek — pro malé hodnoty řeší i malé odchylky, pro velké hodnoty jen velké; je méně citlivá na odlehlé hodnoty.

**Mean absolute error** — odchylky se skládají lineárně:
$$\mathrm{MAE} = \frac{1}{N}\sum_{i=1}^N |Y_i - \hat Y_i|.$$
Méně citlivá k odlehlým hodnotám než MSE.

**Koeficient determinace** $R^2$ (koeficient „R kvadrát“) — vyjadřuje, jaký podíl variability cílové proměnné model vysvětluje:
$$R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{SST}}, \qquad \mathrm{RSS} = \sum_{i=1}^N (Y_i - \hat Y_i)^2, \quad \mathrm{SST} = \sum_{i=1}^N (Y_i - \bar Y)^2,$$
kde RSS = residual sum of squares (reziduální součet čtverců), SST = total sum of squares (celkový součet čtverců).

---

## 4. Vyhodnocovací metriky klasifikace

### 4.1 Proč ne přímo ztrátová funkce

Při klasifikaci se chyba měřená pomocí ztrátové funkce pro rozumnou evaluaci příliš nehodí — typicky jde o relativní entropii, jejíž číselné hodnoty jsou těžko interpretovatelné. Nejčastěji se vyhodnocování klasifikačních modelů provádí pomocí měr odvozených z tzv. **matice záměn** (angl. *confusion matrix*). Zaměřujeme se na **binární klasifikaci**.

### 4.2 Matice záměn (confusion matrix)

Matice záměn je matice četností různých predikovaných hodnot $\hat Y_i$ proti různým skutečným hodnotám $Y_i$:

| Skutečnost \\ Predikce | $\hat Y = 1$ | $\hat Y = 0$ | $\sum$ |
|---|---|---|---|
| $Y = 1$ | **TP** | FN | $N_+ = \mathrm{TP} + \mathrm{FN}$ |
| $Y = 0$ | FP | **TN** | $N_- = \mathrm{FP} + \mathrm{TN}$ |
| $\sum$ | $\hat N_+ = \mathrm{TP} + \mathrm{FP}$ | $\hat N_- = \mathrm{FN} + \mathrm{TN}$ | $N = \mathrm{TP}+\mathrm{FP}+\mathrm{FN}+\mathrm{TN}$ |

- **TP** (*true positive*) — kolikrát model **správně** predikoval $Y=1$.
- **FP** (*false positive*) — kolikrát model **špatně** predikoval $Y=0$ (skutečnost 0, predikce 1; type I error).
- **FN** (*false negative*) — kolikrát model **špatně** predikoval $Y=1$ (skutečnost 1, predikce 0; type II error).
- **TN** (*true negative*) — kolikrát model **správně** predikoval $Y=0$.

Sloupcové součty $\hat N_+, \hat N_-$ jsou počty bodů, kde model predikoval 1, resp. 0; řádkové součty $N_+, N_-$ jsou počty bodů ve třídě 1, resp. 0. Ideální predikce vede k tomu, že FN i FP jsou rovny 0.

### 4.3 Míry odvozené z matice záměn

Následující míry odpovídají odhadům **podmíněných pravděpodobností** $\mathrm P(\hat Y = \hat y \mid Y = y)$:

| | $\hat Y = 1$ | $\hat Y = 0$ |
|---|---|---|
| $Y = 1$ | $\mathrm{TPR} = \frac{\mathrm{TP}}{N_+}$ | $\mathrm{FNR} = \frac{\mathrm{FN}}{N_+}$ |
| $Y = 0$ | $\mathrm{FPR} = \frac{\mathrm{FP}}{N_-}$ | $\mathrm{TNR} = \frac{\mathrm{TN}}{N_-}$ |

- **TPR** (*true positive rate*) — též *sensitivita*, *recall* (úplnost), *hit rate*.
- **FPR** (*false positive rate*) — též *false alarm rate*, *type I error rate*.
- **FNR** (*false negative rate*) — též *miss rate*, *type II error rate*.
- **TNR** (*true negative rate*) — též *specificita*, *selektivita*.

Někdy se používají i odhady **obrácených** pravděpodobností $\mathrm P(Y=y\mid\hat Y=\hat y)$. Především **precision** (preciznost), neboli *positive predictive value*, což je odhad $\mathrm P(Y=1\mid\hat Y=1)$:
$$\mathrm{PPV} = \frac{\mathrm{TP}}{\hat N_+}.$$

### 4.4 Přesnost a $F_1$ skóre

**Přesnost (accuracy)** — odhad $\mathrm P(\hat Y = Y)$, suverénně nejpoužívanější míra:
$$\mathrm{ACC} = \frac{\mathrm{TP} + \mathrm{TN}}{N}.$$
Přesnost **není vhodná pro nevyvážené datasety**, kde je $\mathrm P(Y=1)$ nebo $\mathrm P(Y=0)$ velmi malé — přesnost bude vysoká, jakmile model zvládne správně predikovat majoritní třídu.

**$F_1$ skóre** — harmonický průměr precision $\mathrm P(Y=1\mid\hat Y=1)$ a recall $\mathrm P(\hat Y=1\mid Y=1)$:
$$F_1 = \frac{2}{1/\mathrm{PPV} + 1/\mathrm{TPR}} = 2\,\frac{\mathrm{PPV}\cdot\mathrm{TPR}}{\mathrm{PPV} + \mathrm{TPR}}.$$
Užitečné především pro nevyvážené datasety, kde je $\mathrm P(Y=1)$ velmi malá.

### 4.5 Práh rozhodování, ROC křivka a AUC

Při klasickém přístupu (např. **[[Logistická-regrese|logistická regrese]]**) se predikce $Y$ získá porovnáním pravděpodobnosti $p(\boldsymbol X) = \mathrm P(Y=1\mid\boldsymbol X)$ s číslem $1/2$:
$$\hat Y = \mathbb 1_{\hat p(\boldsymbol X) > 0.5},$$
tj. predikujeme třídu s vyšší pravděpodobností. Toto rozhodovací pravidlo lze zobecnit zavedením **prahu** $\tau \in [0,1]$ jako nového hyperparametru:
$$\hat Y_\tau \equiv \hat Y_\tau(\boldsymbol X) = \mathbb 1_{\hat p(\boldsymbol X) > \tau}, \qquad \hat Y = \hat Y_{0.5}.$$
Pro rostoucí $\tau$ jsou TPR$_\tau$ i FPR$_\tau$ **neklesající** funkce $\tau$ (přesněji: predikce začíná na 1 pro $\tau=0$ a v nějaké hodnotě přeskočí na 0).

**ROC křivka.** Graf TPR$_\tau$ versus FPR$_\tau$ jakožto implicitní funkce $\tau$ se nazývá *receiver operating characteristic* (ROC křivka). Pro dobrý model graf strmě stoupá k levému hornímu rohu a poté pomalu do pravého horního rohu; přímka na diagonále odpovídá náhodné predikci ($\mathrm{TPR}_\tau \doteq \mathrm{FPR}_\tau$ pro každé $\tau$).

**AUC.** Kvalita modelu s ROC křivkou se obvykle vyhodnocuje jediným číslem — *plochou pod křivkou* (angl. *area under curve*), značeno **AUC**:
- náhodné predikce → AUC = 0.5,
- dokonalý model → AUC = 1,
- většina modelů má AUC mezi 0.5 a 1.

> *Doplnění nad rámec slidů (význam AUC = 1):* AUC = 1 znamená, že ROC křivka prochází levým horním rohem (TPR = 1 a FPR = 0 současně). Ekvivalentně: **existuje práh** $\tau$, pro který model **přesně klasifikuje všechny body** datasetu (žádné FP ani FN) — tj. odhadnutá pravděpodobnost $\hat p$ **dokonale odděluje** třídy 0 a 1 (všechny body třídy 1 mají vyšší $\hat p$ než kterýkoli bod třídy 0).

---

## Co je potřeba na zkoušku znát

### Definice
- **Ztrátová funkce** $L(Y,\hat Y)$: kvadratická $L=(Y-\hat Y)^2$, absolutní $L_1=|Y-\hat Y|$, binární cross-entropy $L(Y,\hat p) = -Y\log\hat p - (1-Y)\log(1-\hat p)$.
- **Trénovací chyba** $\overline{\mathrm{err}}_{\mathrm{train}} = \mathcal L = \frac1N\sum L(Y_i,\hat Y(\boldsymbol x_i))$ — optimisticky vychýlená (overfitting).
- **Testovací chyba** $\mathrm{Err}_{\mathcal D} = \mathrm E(L(Y,\hat Y(\boldsymbol X))\mid\mathcal D)$; odhad $\overline{\mathrm{err}}_{\mathrm{test}}$ na nezávislých test. datech, nestranný vůči $\mathrm{Err}_{\mathcal D}$. **Očekávaná** testovací chyba $\mathrm{Err} = \mathrm E(\mathrm{Err}_{\mathcal D})$.
- **Hold-out:** trénovací / validační / testovací; **výběr modelu** vs. **ohodnocení modelu**.
- **$k$-fold CV**, **LOO** ($k=N$).
- **Matice záměn:** TP, FP, FN, TN; **TPR/recall, FPR, TNR/specificita, PPV/precision**.
- **Metriky regrese:** MSE, RMSE, RMSLE, MAE, $R^2 = 1-\mathrm{RSS}/\mathrm{SST}$.
- **Metriky klasifikace:** ACC $=\frac{\mathrm{TP}+\mathrm{TN}}{N}$, $F_1 = 2\frac{\mathrm{PPV}\cdot\mathrm{TPR}}{\mathrm{PPV}+\mathrm{TPR}}$, ROC, AUC.

### Věty
- $\overline{\mathrm{err}}_{\mathrm{test}}$ je **nestranný odhad** $\mathrm{Err}_{\mathcal D}$: $\mathrm E(\overline{\mathrm{err}}_{\mathrm{test}}\mid\mathcal D) = \mathrm{Err}_{\mathcal D}$.
- Trénovací chyba **podhodnocuje** generalizační chybu (model laděn na trénovacích datech → overfitting).
- Cross-entropy ztráta = mínus logaritmus věrohodnostní funkce maximalizované **logistickou regresí** (minimalizace ↔ maximalizace věrohodnosti — totožná úloha).
- Pro fixní model je CV chyba odhadem **očekávané** testovací chyby $\mathrm{Err}$ (ne $\mathrm{Err}_{\mathcal D}$).
- ACC je nevhodná pro nevyvážené datasety (majoritní třída); $F_1$ vhodnější.

### Algoritmy
- **Hold-out:** odděl testovací data co nejdříve; trénovací → modely, validační → výběr hyperparametrů/modelu, testovací → finální ohodnocení.
- **$k$-fold CV:** rozděl na $k$ částí, $k$krát trénuj na $k-1$ a měř na vynechané; $\hat e = \frac1k\sum e_i$; vyber hyperparametry s min. $\hat e$ a přetrénuj na celém $\mathcal D$ ($k = 5$–$10$; LOO pro $k=N$).
- **ROC/AUC:** měň práh $\tau$, vykresli TPR$_\tau$ vs. FPR$_\tau$, vyhodnoť plochou pod křivkou.

### Typické doplňující otázky (doptávání)
- **Friedjungová (2025):** „Jaký je rozdíl mezi metrikou a ztrátovou funkcí (loss)?" (loss → trénink / gradientní sestup; metrika → vyhodnocení po tréninku) → §1.2
- **Friedjungová (2025):** „Lze tutéž loss použít i pro měření testovací chyby?" (ano, pokud pro nás dává smysl — MSE/MAE i cross-entropy) → §1.2
- **Friedjungová (2025):** „Co přesně znamená ‚testovací chyba'?" (hodnota metriky vyčíslená nad TEST setem) → §1.2, §1.4
- **Friedjungová (2025):** „Jaké podmínky musí splňovat train/test/val rozdělení?" (disjunktní, náhodně vybrané; výjimka chronologická data) → §1.5
- **Friedjungová (2025):** „Jak otestovat model tak, jak se chová v produkci?" (vyhodnotit metriky na odděleném test setu) → §1.3, §1.5
- **Friedjungová (2025):** „Jak poznáte přeučení (overfitting)?" (trénovací chyba malá, testovací velká) → §1.3
- **Friedjungová (2025):** „Načrtněte / vysvětlete křížovou validaci." (ilustrace $k$-fold) → §2.2
- **Klouda (2023):** „Pro které modely lze použít binary cross-entropy?" (modely odhadující pravděpodobnost — např. logistická regrese) → §1.2
- **Klouda (2023):** „Co znamená AUC = 1?" (existuje práh $\tau$, pro který model přesně klasifikuje všechny body datasetu) → §4.5
