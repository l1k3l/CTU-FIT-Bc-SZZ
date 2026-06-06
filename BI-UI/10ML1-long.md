---
studyplan: true
etapa: "4 · ML1 / ML2 — Dedecius + Holeňa"
qid: "10ML1"
examiner: "Dedecius + Petr"
topic: "Lineární regrese: MNČ, geometrická interpretace, kolinearita"
readiness: nezačato
hot: true
tags: [otázka, kurz/ML1, otázka/10, todo]
---

# Lineární regrese — metoda nejmenších čtverců, geometrická interpretace, kolinearita

> **Otázka SZZ:** Lineární regrese – metoda nejmenších čtverců, geometrická interpretace, problém kolinearity.

Zdroje: BI-ML1 (FIT ČVUT), přednáška 4 (Základy lineární regrese, sekce 14; Extrémy funkce více proměnných, sekce 15; Metoda nejmenších čtverců, sekce 16) — printed str. 32–38; přednáška 5 (Geometrická interpretace MNČ, sekce 18; Regularita versus lineární nezávislost, sekce 19; Problém kolinearity, sekce 20) — printed str. 39–43.

Značení: $Y$ vysvětlovaná (cílová) náhodná veličina, $X_1,\dots,X_p$ příznaky, $w = (w_0,w_1,\dots,w_p)^T$ vektor vah (parametrů), $w_0$ intercept, $\varepsilon$ náhodná chyba, $\mathrm{E}\,\varepsilon = 0$. Po zavedení umělého příznaku $X_0 = x_0 = 1$ píšeme $x = (x_0,x_1,\dots,x_p)^T$ a $Y = w^Tx + \varepsilon$. Trénovací data: $N$ párů $(Y_i, x_i)$, $\mathbf{X} \in \mathbb{R}^{N,p+1}$ matice příznaků (řádky $x_i^T$, první sloupec samé jedničky), $\mathbf{Y} = (Y_1,\dots,Y_N)^T$, $\varepsilon = (\varepsilon_1,\dots,\varepsilon_N)^T$. Odhad vah $\hat w$, konkrétně $\hat w_{\mathrm{OLS}}$ (ordinary least squares). Predikce $\hat Y$. $\|\cdot\|$ eukleidovská [[Norma|norma]].

---

## 1. Model lineární regrese

### 1.1 Formalizace úlohy

Na základě $p$ příznaků $X_1,\dots,X_p$ chceme predikovat hodnotu **vysvětlované proměnné** $Y$. V modelu **[[Lineární-regrese|lineární regrese]]** předpokládáme **lineární závislost** $Y$ na hodnotách příznaků. Protože nevěříme, že je tato závislost dokonalá (pro stejné hodnoty příznaků nedostaneme vždy stejné $Y$), modelujeme ji s **náhodnou chybou** $\varepsilon$:
$$Y = w_1 x_1 + \dots + w_p x_p + \varepsilon,$$
kde $w_1,\dots,w_p$ jsou neznámé koeficienty a $\varepsilon$ je náhodná veličina shrnující část $Y$, kterou příznaky nevysvětlí (vlivy, které neznáme nebo do modelu cíleně nezahrnujeme, plus chyby a nekonzistence dat).

### 1.2 Model lineární regrese (intercept)

Obvykle ještě oddělujeme střední hodnotu náhodných vlivů, čímž dostaneme **model lineární regrese**: hodnota vysvětlované proměnné $Y$ v bodě $(x_1,\dots,x_p)^T$ je
$$Y = w_0 + w_1 x_1 + \dots + w_p x_p + \varepsilon, \qquad \mathrm{E}\,\varepsilon = 0.$$

- Koeficient $w_0$ se nazývá **intercept** a odpovídá (očekávané) výchozí hodnotě $Y$ při nulových příznacích.
- Předpoklad $\mathrm{E}\,\varepsilon = 0$ zajišťuje, že chyba je v průměru vystředěná (žádná systematická odchylka).

### 1.3 Vektorový a maticový zápis

Zavedeme-li **umělý konstantní příznak** $X_0 = x_0 = 1$ a vektorové značení
$$x = (x_0, x_1, \dots, x_p)^T, \qquad w = (w_0, w_1, \dots, w_p)^T,$$
můžeme model zkráceně psát jako
$$Y = w^T x + \varepsilon.$$
Vektor $w$ koeficientů nazýváme **vektor vah**.

Trénovací data považujeme za náhodný výběr z modelu provedený v různých bodech $x_1,\dots,x_N$. Máme $N$ párů $(Y_i, x_i)$, kde $Y_i = w^T x_i + \varepsilon_i$. Body $x_1,\dots,x_N$ zapíšeme po řádcích do **matice příznaků** $\mathbf{X} \in \mathbb{R}^{N,p+1}$:
$$\mathbf{X} = \begin{pmatrix} x_1^T \\ \vdots \\ x_N^T \end{pmatrix} = \begin{pmatrix} 1 & x_{1;1} & x_{1;2} & \cdots & x_{1;p} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{N;1} & x_{N;2} & \cdots & x_{N;p} \end{pmatrix}.$$
Naměřené hodnoty příznaků $X_1,\dots,X_p$ spolu s přidaným umělým příznakem $X_0 = 1$ tedy tvoří sloupce matice $\mathbf{X}$. Celkový model trénovací množiny zapíšeme maticově jako
$$\boxed{\;\mathbf{Y} = \mathbf{X}w + \varepsilon\;}, \qquad \mathrm{E}\,\varepsilon = (\mathrm{E}\,\varepsilon_1,\dots,\mathrm{E}\,\varepsilon_N)^T = 0.$$

### 1.4 Predikce v modelu

Máme-li odhad $\hat w$ vektoru vah, hodnotu $Y$ v konkrétním bodě $x$ predikujeme vztahem
$$\hat Y = \hat w^T x = x^T \hat w = \hat w_0 + \hat w_1 x_1 + \dots + \hat w_p x_p.$$
Skutečná hodnota je $Y = w^T x + \varepsilon$ (náhodná veličina). Z $\mathrm{E}\,\varepsilon = 0$ plyne $\mathrm{E}\,Y = w^T x$, takže $\hat Y$ je **bodovým odhadem střední hodnoty** $\mathrm{E}\,Y$ v bodě $x$. (Lineární regrese je tak příkladem diskriminativní metody, kdy přímo odhadujeme $\mathrm{E}(Y \mid X = x)$.)

---

## 2. Metoda nejmenších čtverců

### 2.1 Ztrátová funkce a reziduální součet čtverců

Cílem je najít takovou hodnotu $w$, aby chyba modelu byla co nejmenší; tu pak použijeme jako odhad $\hat w$. Chybu měříme nezápornou **ztrátovou funkcí** $L$ aplikovanou na skutečnou hodnotu $Y$ a predikci $\hat Y$. Pro spojitou vysvětlovanou veličinu se obvykle volí **kvadratická ztrátová funkce**
$$L(Y, \hat Y) = (Y - \hat Y)^2.$$
Abychom co nejvíce využili trénovací data, minimalizujeme součet chyb přes všechny dvojice $(x_i, Y_i)$, tzv. **reziduální součet čtverců** (residual sum of squares):
$$\mathrm{RSS}(w) = \sum_{i=1}^{N} L(Y_i, w^T x_i) = \sum_{i=1}^{N}(Y_i - w^T x_i)^2 = \|\mathbf{Y} - \mathbf{X}w\|^2.$$
Minimalizací tohoto výrazu vzhledem k $w$ získáme odhad $\hat w$. Tento postup se nazývá **[[Metoda-nejmenších-čtverců|metoda nejmenších čtverců]]** (MNČ, the method of least squares). Trénování modelu je tedy úloha optimalizace — hledání extrému (minima) funkce $\mathrm{RSS}(w)$ proměnné $w \in \mathbb{R}^{p+1}$.

### 2.2 Připomenutí: extrémy funkce více proměnných

Protože $w$ je vektor, minimalizace $\mathrm{RSS}(w)$ spadá do problematiky hledání extrémů **funkce více proměnných**; postupuje se analogicky jako u funkce jedné proměnné.

**Definice ([[Parciální-derivace|parciální derivace]]).** Pro $f:\mathbb{R}^d \to \mathbb{R}$ je parciální derivace $\partial_{x_i} f(a)$ podle $x_i$ v bodě $a = (a_1,\dots,a_d)$ derivací funkce jedné proměnné $g(x_i) = f(a_1,\dots,x_i,\dots,a_d)$ v bodě $a_i$ (ostatní proměnné bereme jako konstanty).

**Definice ([[Gradient]]).** Má-li $f$ v bodě $a$ konečné všechny parciální derivace, je gradient
$$\nabla f(a) = \Big(\tfrac{\partial f}{\partial x_1}(a), \dots, \tfrac{\partial f}{\partial x_d}(a)\Big).$$
Gradient ukazuje **směr maximálního růstu** funkce a je vždy kolmý na vrstevnici. Má-li $f$ v bodě lokální extrém a gradient zde existuje, musí být nulový.

**Definice ([[Hessova-matice|Hessova matice]]).** Hessova matice $\mathbf{H}_f(a)$ je matice druhých parciálních derivací $\big(\tfrac{\partial^2 f}{\partial x_i \partial x_j}(a)\big)_{i,j}$.

**Věta (postačující podmínka pro [[Lokální-extrém|lokální extrém]]).** Nechť $f:\mathbb{R}^d \to \mathbb{R}$ má spojité druhé parciální derivace na okolí bodu $x^*$ a $\nabla f(x^*) = 0$. Pak:
- je-li $s^T \mathbf{H}_f(x^*) s > 0$ pro každé $s \neq 0$ ($\mathbf{H}_f$ **pozitivně definitní**), má $f$ v $x^*$ **ostré lokální minimum**;
- platí-li $s^T \mathbf{H}_f(x) s \ge 0$ pro každé $s$ a všechna $x$ z nějakého okolí ($\mathbf{H}_f$ **pozitivně semidefinitní**), má $f$ v $x^*$ **neostré lokální minimum**.

### 2.3 Gradient RSS a normální rovnice

Aplikujeme teorii na $\mathrm{RSS}(w) = \sum_{i=1}^N (Y_i - w^T x_i)^2$. Parciální derivace podle $w_j$:
$$\frac{\partial\,\mathrm{RSS}}{\partial w_j} = \sum_{i=1}^{N} 2(Y_i - w^T x_i)(-x_{i;j}).$$
Sestavením složek do vektoru dostaneme gradient
$$\nabla\,\mathrm{RSS} = -\sum_{i=1}^{N} 2(Y_i - w^T x_i)\, x_i = -2\,\mathbf{X}^T(\mathbf{Y} - \mathbf{X}w).$$
Položíme-li $\nabla\,\mathrm{RSS} = 0$, dostaneme **normální rovnici** (normal equation)
$$\mathbf{X}^T \mathbf{Y} - \mathbf{X}^T \mathbf{X} w = 0 \qquad\Longleftrightarrow\qquad \boxed{\;\mathbf{X}^T \mathbf{X}\, w = \mathbf{X}^T \mathbf{Y}\;}.$$

### 2.4 Hessova matice RSS — konvexita a globální minimum

Druhé parciální derivace: $\tfrac{\partial^2 \mathrm{RSS}}{\partial w_k \partial w_j} = \sum_{i=1}^N 2(-x_{i;k})(-x_{i;j})$, takže Hessova matice je
$$\mathbf{H}_{\mathrm{RSS}}(w) = 2\,\mathbf{X}^T \mathbf{X}$$
**bez ohledu** na konkrétní hodnotu $w$ (RSS je kvadratická funkce). Pro každé $s \in \mathbb{R}^{p+1}$ platí
$$s^T(\mathbf{X}^T \mathbf{X})s = (\mathbf{X}s)^T(\mathbf{X}s) = \|\mathbf{X}s\|^2 \ge 0,$$
takže $\mathbf{H}_{\mathrm{RSS}}$ je vždy **pozitivně semidefinitní** ⇒ $\mathrm{RSS}$ je **[[Konvexní-funkce|konvexní funkce]]**. Podle postačující podmínky proto nastává (neostré) lokální minimum v **jakémkoli** bodě $w$ řešícím normální rovnici. Díky konvexitě je každé takové lokální minimum zároveň **globálním minimem** (geometrický důkaz globálnosti viz §3).

### 2.5 OLS odhad při regularitě

Předpokládejme, že je matice $\mathbf{X}^T \mathbf{X}$ **[[Regulární-matice|regulární]]**. Pak má normální rovnice **jednoznačné řešení**
$$\hat w_{\mathrm{OLS}} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y},$$
kde značení vychází z anglického ordinary least squares solution.

Pozitivní definitnost (a tím ostrost minima) je v tomto případě zaručena: pro matici $\mathbf{X}$ a libovolné $s \in \mathbb{R}^{p+1}$ platí řetěz implikací
$$\mathbf{X}s = 0 \;\Rightarrow\; \mathbf{X}^T\mathbf{X}s = 0 \;\Rightarrow\; s^T\mathbf{X}^T\mathbf{X}s = 0 \;\Rightarrow\; \|\mathbf{X}s\|^2 = 0 \;\Rightarrow\; \mathbf{X}s = 0.$$
Z regularity $\mathbf{X}^T\mathbf{X}$ tedy plyne, že pro nenulové $s$ nikdy neplatí $s^T(\mathbf{X}^T\mathbf{X})s = 0$ — Hessova matice je pozitivně definitní, a $\hat w_{\mathrm{OLS}}$ je bodem **ostrého** (a tedy jediného) globálního minima. Predikce v bodě $x$ je pak
$$\hat Y = \hat w_{\mathrm{OLS}}^T x = x^T (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}.$$

> Tutéž normální rovnici a vzorec lze odvodit i čistě lineárně-algebraicky jako řešení přeurčené soustavy ve smyslu nejmenších čtverců — srov.
>
> ![[Metoda-nejmenších-čtverců#Normální rovnice]]

---

## 3. Geometrická interpretace

### 3.1 RSS jako vzdálenost a sloupcový prostor

Minimalizace $\mathrm{RSS}(w) = \|\mathbf{Y} - \mathbf{X}w\|^2$ je ekvivalentní minimalizaci $\|\mathbf{Y} - \mathbf{X}w\|$. To znamená, že pro optimální $w$ je **eukleidovská vzdálenost** bodů $\mathbf{Y}$ a $\mathbf{X}w$ v prostoru $\mathbb{R}^N$ nejmenší možná.

Označíme-li $i$-tý sloupec matice $\mathbf{X}$ jako $\mathbf{X}_{\bullet i}$, pak
$$\mathbf{X}w = w_0 \mathbf{X}_{\bullet 0} + w_1 \mathbf{X}_{\bullet 1} + \dots + w_p \mathbf{X}_{\bullet p}$$
je **lineární kombinací sloupců** $\mathbf{X}$. Vektor $\mathbf{X}w$ tedy leží v lineárním podprostoru $\mathbb{R}^N$, který je lineárním obalem $p+1$ sloupců (**sloupcovém prostoru**); pro různá $w$ tento podprostor celý pokrývá:
$$\langle \mathbf{X}_{\bullet 0}, \dots, \mathbf{X}_{\bullet p}\rangle = \{\mathbf{X}w \mid w \in \mathbb{R}^{p+1}\}.$$

### 3.2 Nejbližší bod = ortogonální projekce

Chceme-li minimalizovat vzdálenost $\mathbf{Y}$ od $\mathbf{X}w$, hledáme v podprostoru sloupců bod $\mathbf{X}w$ nejbližší k $\mathbf{Y}$. Bod $\mathbf{X}w$ je k $\mathbf{Y}$ nejblíže, právě když je **reziduum** (chybový vektor) $\mathbf{Y} - \mathbf{X}w$ na tento podprostor **kolmé**. Vektor $\mathbf{X}w$ je tedy **ortogonální projekcí** $\mathbf{Y}$ na sloupcový prostor:
$$\mathbf{X}\hat w = \operatorname{proj}_{\langle \mathbf{X}_{\bullet 0},\dots,\mathbf{X}_{\bullet p}\rangle} \mathbf{Y}.$$

Schematicky: $\mathbf{Y}$ trčí z roviny sloupcového prostoru, $\mathbf{X}w$ je jeho „stín“ (pata kolmice) a $\mathbf{Y} - \mathbf{X}w$ je svislá kolmice mezi nimi — nejkratší možná spojnice bodu s podprostorem.

### 3.3 Kolmost rezidua → normální rovnice

Je-li reziduum $\mathbf{Y} - \mathbf{X}w$ kolmé na podprostor, je kolmé na **všechny** generující sloupce:
$$(\mathbf{X}_{\bullet i})^T(\mathbf{Y} - \mathbf{X}w) = 0 \qquad \text{pro všechna } i = 0,\dots,p.$$
Sloučením těchto $p+1$ rovnic do maticového zápisu (řádky $\mathbf{X}^T$ jsou právě sloupce $\mathbf{X}$):
$$\mathbf{X}^T(\mathbf{Y} - \mathbf{X}w) = 0 \qquad\Longleftrightarrow\qquad \mathbf{X}^T\mathbf{Y} - \mathbf{X}^T\mathbf{X}w = 0.$$
Získali jsme tedy znovu **normální rovnici** z §2.3 — tentokrát čistě geometrickou úvahou, beze derivací. Algebraická (gradient = 0) a geometrická (reziduum ⊥ sloupce) cesta vedou k téže rovnici.

> Tato kolmost rezidua na sloupcový prostor a z ní plynoucí normální rovnice je tatáž geometrie, jaká se v lineární algebře používá pro řešení přeurčených soustav:
>
> ![[Metoda-nejmenších-čtverců#Geometrická interpretace]]

### 3.4 Každé řešení dává globální minimum

Z geometrické úvahy navíc plyne, že **pro jakékoli** řešení $w$ normální rovnice je $\|\mathbf{Y} - \mathbf{X}w\|$ (a tedy i $\mathrm{RSS}(w)$) nejmenší možné — projekce je jediný bod podprostoru minimalizující vzdálenost. Každé řešení normální rovnice proto dává **globální minimum** RSS (potvrzuje konvexitu z §2.4). Pythagorova úvaha: pro libovolné $y$ a řešení $\hat w$ platí $\|\mathbf{Y} - \mathbf{X}y\|^2 = \|\mathbf{Y} - \mathbf{X}\hat w\|^2 + \|\mathbf{X}\hat w - \mathbf{X}y\|^2 \ge \|\mathbf{Y} - \mathbf{X}\hat w\|^2$.

---

## 4. Problém kolinearity

### 4.1 Regularita versus lineární nezávislost sloupců

Normální rovnice má jednoznačné řešení, právě když je $\mathbf{X}^T\mathbf{X}$ **regulární**. Pomocí výše uvedeného řetězu implikací ($\mathbf{X}s = 0 \Leftrightarrow \mathbf{X}^T\mathbf{X}s = 0$) platí:

**Tvrzení.** Matice $\mathbf{X}^T\mathbf{X}$ je regulární **právě tehdy, když jsou sloupce $\mathbf{X}$ lineárně nezávislé** (tj. $\mathbf{X}s = 0$ pouze pro $s = 0$, neboli $h(\mathbf{X}) = p+1$ — viz [[Hodnost-matice|hodnost matice]]).

Kdy sloupce **nemohou** být lineárně nezávislé:
- **$N < p+1$** (málo dat, mnoho příznaků): v $N$-rozměrném prostoru $\mathbb{R}^N$ nemůže existovat $p+1$ lineárně nezávislých vektorů, takže $p+1$ sloupců $\mathbf{X}$ nutně závisí. Tady nepomůže žádný vzorec — soustava je podurčená.
- **$N \ge p+1$**, ale příznaky jsou samy lineárně závislé (jeden je lineární kombinací ostatních). Pak ani libovolně velké $N$ nepomůže a sloupce $\mathbf{X}$ budou závislé vždy.

### 4.2 Singulární $\mathbf{X}^T\mathbf{X}$ — neexistence jednoznačného řešení

Normální rovnice $\mathbf{X}^T\mathbf{Y} - \mathbf{X}^T\mathbf{X}w = 0$ je soustava $p+1$ lineárních rovnic o $p+1$ neznámých (viz [[Soustava-lineárních-rovnic|soustava lineárních rovnic]]) a má **vždy alespoň jedno řešení**.

- **Sloupce LN ⇒** $\mathbf{X}^T\mathbf{X}$ regulární ⇒ právě jedno řešení $\hat w_{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ (viz [[Inverzní-matice|inverzní matice]]).
- **Sloupce LZ ⇒** $\mathbf{X}^T\mathbf{X}$ singulární ⇒ **nekonečně mnoho řešení**. Pro každé dvě řešení $w, w'$ platí $\mathbf{X}^T\mathbf{X}(w - w') = 0$, odkud $\mathbf{X}(w - w') = 0$, a tudíž
$$\mathrm{RSS}(w) = \|\mathbf{Y} - \mathbf{X}w'\|^2 = \mathrm{RSS}(w').$$
Všechna řešení tedy odpovídají téže (globální, ovšem neostré) minimální hodnotě RSS. Jednoznačný odhad vah $\hat w$ neexistuje — predikce je sice jednoznačná, ale interpretace jednotlivých vah ztrácí smysl.

Řešení lze v singulárním případě zapsat pomocí Moorovy–Penroseovy pseudoinverze $\hat w = (\mathbf{X}^T\mathbf{X})^+\mathbf{X}^T\mathbf{Y}$, které mezi všemi řešeními vybírá to s **nejmenší normou** $\|\hat w\|$ (knihovní funkce typu `LinearRegression` v `scikit-learn` to dělají automaticky).

### 4.3 „Skoro“ závislé sloupce — kolinearita

Problémem nejsou jen přesně lineárně závislé sloupce, ale stačí **„skoro“ lineárně závislé** (např. silně korelované příznaky). V obou případech mluvíme o **problému kolinearity** (collinearity): existují lineární kombinace sloupců dávající téměř nulové vektory, zatímco jiné vrací mnohem větší vektory, tj.
$$\|\mathbf{X}u\| \gg \|\mathbf{X}v\| \doteq 0 \qquad\text{pro nějaké } \|u\| = \|v\| = 1.$$
Inverze $\mathbf{X}^T\mathbf{X}$ pak sice teoreticky existuje, ale její výpočet je **numericky problematický** — matice je **špatně podmíněná**. Mírou je **číslo podmíněnosti** $\kappa(\mathbf{X}^T\mathbf{X})$ (poměr největšího a nejmenšího vlastního čísla); pro kolineární data je obrovské. (Numericky proto bývá lepší řešit MNČ přes [[QR-rozklad|QR rozklad]] než přes normální rovnice — $\kappa(\mathbf{X}^T\mathbf{X}) = \kappa(\mathbf{X})^2$.)

### 4.4 Důsledky kolinearity

- **Jádro problému:** odhad $\hat w_{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ je velmi **citlivý** na malé nevhodné změny $\mathbf{Y}$ nebo $\mathbf{X}$. Kdybychom náhodný výběr trénovací množiny zopakovali, hodnota $\hat w_{\mathrm{OLS}}$ se může **radikálně změnit**.
- Z pravděpodobnostního pohledu má $\hat w_{\mathrm{OLS}}$ v jistých směrech **velký rozptyl** (vysoká variance odhadu).
- To se přenáší i na predikce $\hat Y$, které v některých bodech mají velký rozptyl — predikcím proto **nemůžeme příliš důvěřovat**.
- Důsledkem bývá **přeučení** (overfitting): model se příliš přizpůsobí trénovací množině a špatně predikuje nové body.

### 4.5 Náznak řešení

Narazíme-li na problém kolinearity, máme v zásadě tři možnosti:
1. **Přidat data nebo odebrat problematické body** — nepomůže, jsou-li příznaky samy (skoro) lineárně závislé.
2. **Snížit počet příznaků** — vyhodit některé, případně je nahradit menším počtem nových, již nezávislých (metody redukce dimenze).
3. **Změnit minimalizovanou funkci** přidáním **regularizačního členu** k RSS — tzv. regularizace. Typickým zástupcem je **hřebenová regrese** (ridge regression), která ke ztrátě přidá $\lambda\|w\|^2$; tím se $\mathbf{X}^T\mathbf{X}$ nahradí $\mathbf{X}^T\mathbf{X} + \lambda E$ (regulární i pro kolineární data) a řešení se stabilizuje. Viz hřebenová regrese v [[Lineární-regrese]] (podrobně otázka 11).

---

## Co je potřeba na zkoušku znát

### Definice
- **Model lineární regrese:** $Y = w_0 + w_1 x_1 + \dots + w_p x_p + \varepsilon$, $\mathrm{E}\,\varepsilon = 0$; vektorově $Y = w^T x + \varepsilon$ (s $x_0 = 1$); maticově trénovací data $\mathbf{Y} = \mathbf{X}w + \varepsilon$. Intercept $w_0$. Predikce $\hat Y = x^T\hat w$.
- **RSS (reziduální součet čtverců):** $\mathrm{RSS}(w) = \sum_i (Y_i - w^T x_i)^2 = \|\mathbf{Y} - \mathbf{X}w\|^2$ (kvadratická ztráta).
- **MNČ:** odhad $\hat w$ minimalizuje $\mathrm{RSS}(w)$.
- **Kolinearita:** sloupce $\mathbf{X}$ (skoro) lineárně závislé, $\|\mathbf{X}u\| \gg \|\mathbf{X}v\| \doteq 0$.

### Věty
- **Normální rovnice:** $\nabla\,\mathrm{RSS} = -2\mathbf{X}^T(\mathbf{Y} - \mathbf{X}w) = 0 \iff \mathbf{X}^T\mathbf{X}w = \mathbf{X}^T\mathbf{Y}$.
- **Hessova matice** $\mathbf{H}_{\mathrm{RSS}} = 2\mathbf{X}^T\mathbf{X}$ je PSD ($s^T\mathbf{X}^T\mathbf{X}s = \|\mathbf{X}s\|^2 \ge 0$) ⇒ RSS konvexní ⇒ řešení je **globální minimum**.
- **OLS:** při regulární $\mathbf{X}^T\mathbf{X}$ je $\hat w_{\mathrm{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$ jediné (ostré) minimum.
- **Geometrie:** $\mathbf{X}\hat w = \operatorname{proj}_{\langle\text{sloupce }\mathbf{X}\rangle}\mathbf{Y}$; reziduum $\mathbf{Y} - \mathbf{X}\hat w \perp$ sloupce ⇒ $\mathbf{X}^T(\mathbf{Y} - \mathbf{X}\hat w) = 0$ = normální rovnice.
- **Regularita ⇔ LN sloupce:** $\mathbf{X}^T\mathbf{X}$ regulární $\iff$ sloupce $\mathbf{X}$ LN; jinak nekonečně mnoho řešení se stejnou (neostrou) globální hodnotou RSS.

### Algoritmy
- **Výpočet OLS:** sestavit $\mathbf{X}, \mathbf{Y}$ → normální rovnice $\mathbf{X}^T\mathbf{X}w = \mathbf{X}^T\mathbf{Y}$ → vyřešit (přímo, numericky stabilněji přes [[QR-rozklad|QR]] / [[SVD]]).
- **Při kolinearitě:** pseudoinverze $(\mathbf{X}^T\mathbf{X})^+$ (řešení s nejmenší normou) nebo regularizace (hřebenová regrese, $\mathbf{X}^T\mathbf{X} + \lambda E$) / redukce příznaků.
