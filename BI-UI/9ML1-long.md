---
tags: [otázka, kurz/ML1, otázka/9, todo]
---

# Metrika, metoda nejbližších sousedů a aglomerativní hierarchické shlukování

> **Otázka SZZ:** Metrika - definice a příklady. Metoda nejbližších sousedů pro klasifikaci i regresi. Aglomerativní hierarchické shlukování.

Zdroje: BI-ML1 (FIT ČVUT), přednáška 3 — *kNN a metriky* (sekce 11 kNN: popis metody, Definice 11.1 metrika; sekce 12 normalizace dat a nominální příznaky; sekce 13 prokletí dimenzionality); přednáška 11 — *nesupervizované učení* (sekce 42 shluková analýza, Definice 42.1 metrika; sekce 43 hierarchické shlukování). Z přednášky 11 zde čerpáme **pouze** aglomerativní hierarchické shlukování; k-means a obecné principy nesupervizovaného učení patří k otázce 14.

Značení: $\mathcal{X}$ množina (prostor možných hodnot příznaků, typicky $\mathbb{R}^p$), $p$ počet příznaků, $\boldsymbol{x} = (x_1,\dots,x_p)^T$ vektor příznaků (jedna realizace náhodného vektoru $\boldsymbol{X}$), $Y$ vysvětlovaná proměnná, $N$ počet trénovacích dvojic $(\boldsymbol{x}_i, Y_i)$, $d(\cdot,\cdot)$ metrika (vzdálenost dvou bodů), $D(\cdot,\cdot)$ vzdálenost dvou shluků, $k$ počet sousedů resp. shluků, $\hat{y}$ predikce.

---

## 1. Metrika — definice a příklady

### 1.1 Definice

Klíčovým pojmem celé otázky je **vzdálenost** mezi dvěma datovými body. Formálně se zavádí jako **[[Metrika|metrika]]** (tutéž definici uvádějí Definice 11.1 i Definice 42.1).

**Definice (metrika).** *Vzdálenost* (též *metrika*) na množině $\mathcal{X}$ je funkce
$$d : \mathcal{X} \times \mathcal{X} \to [0, +\infty)$$
taková, že pro každé $x, y, z \in \mathcal{X}$ platí
1. $d(x,y) \ge 0$, a $d(x,y) = 0$ právě tehdy, když $x = y$ — **pozitivní definitnost**,
2. $d(x,y) = d(y,x)$ — **symetrie**,
3. $d(x,y) \le d(x,z) + d(z,y)$ — **trojúhelníková nerovnost**.

Dvojice $(\mathcal{X}, d)$ se nazývá **metrický prostor**.

**Slovní výklad axiomů.**
1. Vzdálenost různých bodů je vždy kladná; nulová je jen pro shodné body.
2. Vzdálenost bodu $x$ od $y$ je stejná jako vzdálenost $y$ od $x$.
3. Přímá vzdálenost mezi dvěma body je vždy menší nebo rovna vzdálenosti vedoucí přes nějaký třetí bod.

> Pozor: tato metrika je pojem *metrického prostoru* (vzdálenostní funkce na množině), a je **odlišná** od grafové vzdálenosti (délka nejkratší cesty) z předmětu AG1.

### 1.2 Příklady metrik

Často používané vzdálenosti na $\mathbb{R}^p$ pro body $\boldsymbol{x} = (x_1,\dots,x_p)$ a $\boldsymbol{y} = (y_1,\dots,y_p)$:

**Eukleidovská vzdálenost** (též $L_2$ vzdálenost) — nejběžnější volba, odpovídá eukleidovské **[[Norma|normě]]** rozdílu:
$$d_2(\boldsymbol{x}, \boldsymbol{y}) = \|\boldsymbol{x} - \boldsymbol{y}\|_2 = \sqrt{\sum_{i=1}^p (x_i - y_i)^2}.$$

**Manhattanská vzdálenost** (též $L_1$ vzdálenost):
$$d_1(\boldsymbol{x}, \boldsymbol{y}) = \|\boldsymbol{x} - \boldsymbol{y}\|_1 = \sum_{i=1}^p |x_i - y_i|.$$

**Čebyševova vzdálenost** (též $L_\infty$ vzdálenost):
$$d_\infty(\boldsymbol{x}, \boldsymbol{y}) = \|\boldsymbol{x} - \boldsymbol{y}\|_\infty = \max_i |x_i - y_i|.$$

Všechny tři jsou speciálními případy **$L_q$ metriky** (Minkowského $q$-metrika, $q$-norma) pro $q = 1, 2, \dots$:
$$d_q(\boldsymbol{x}, \boldsymbol{y}) = \|\boldsymbol{x} - \boldsymbol{y}\|_q = \sqrt[q]{\sum_{i=1}^p |x_i - y_i|^q}.$$
Eukleidovská vzdálenost je $q = 2$, manhattanská $q = 1$, Čebyševova je limitní případ $q \to \infty$. Tyto metriky jsou přímo podporovány v `scikit-learn`.

**Hammingova / „shodná–různá" vzdálenost.** Pro nominální (kategoriální) příznak nemá smysl měřit číselný rozdíl. Lze metriku modifikovat tak, aby pro daný příznak vracela $0$ při shodné hodnotě a $1$ při různé hodnotě (rozlišuje jen dva stavy). Podobný efekt dává one-hot encoding s dummy příznaky.

**Levenštejnova vzdálenost.** Příkladem metriky na množině **řetězců** je Levenštejnova (editační) vzdálenost — minimální počet jednoznakových operací (vkládání, mazání, nahrazení), které převedou jeden řetězec na druhý.

**Kosinová vzdálenost.** Na podmnožinu příznaků lze použít míru založenou na **[[Skalární-součin|skalárním součinu]]**, která porovnává směr (úhel) dvou vektorů:
$$\frac{\boldsymbol{x} \cdot \boldsymbol{y}}{\|\boldsymbol{x}\|_2 \, \|\boldsymbol{y}\|_2}.$$

**Vlastní vzdálenosti.** Vzdálenost lze definovat v podstatě libovolně — jediný požadavek je, aby vracela jednoznačně určené číslo pro dva datové body (dva vektory příznaků). Lze definovat i vzdálenosti chovající se v každé dimenzi jinak (např. spojitý příznak přispěje absolutní hodnotou rozdílu, jméno se porovná Levenštejnovou vzdáleností). Volba sofistikované míry ale může z jednoduchého modelu udělat model složitý (a třeba i méně přesný), neboť přibývají hyperparametry určující váhu jednotlivých složek.

---

## 2. Metoda nejbližších sousedů (kNN)

### 2.1 Základní myšlenka

**Metoda nejbližších sousedů** (*K Nearest Neighbors*, kNN) řeší úlohu **supervizovaného učení**: na základě $p$ příznaků $X_1,\dots,X_p$ chceme predikovat hodnotu vysvětlované proměnné $Y$. Příznaky skládáme do vektoru $\boldsymbol{X} = (X_1,\dots,X_p)^T$ chápaného jako náhodný vektor, jeho konkrétní realizaci značíme $\boldsymbol{x} \in \mathcal{X}$ (typicky $\mathcal{X} = \mathbb{R}^p$). K dispozici máme **trénovací množinu** $N$ dvojic $(\boldsymbol{x}_1, Y_1),\dots,(\boldsymbol{x}_N, Y_N)$.

Základní (a velice jednoduchá) myšlenka kNN: chceme-li predikovat hodnotu pro nový bod $\boldsymbol{x}$,
1. v trénovacích datech najdeme $k$ bodů ($k$ je zadaný hyperparametr), které mají od $\boldsymbol{x}$ **nejmenší vzdálenost**;
2. predikci založíme na známých hodnotách $Y$ pro těchto $k$ bodů.

### 2.2 Klasifikace a regrese

**Klasifikace** (diskrétní $Y$) — **většinové hlasování**: predikujeme nejčastější hodnotu (třídu) mezi $k$ nejbližšími sousedy.

**Regrese** (spojité $Y$) — **průměr**: predikujeme průměr hodnot $y_1,\dots,y_k$ příslušných $k$ nejbližším sousedům,
$$\hat{y} = \frac{1}{k}\sum_{i=1}^k y_i.$$

Často se v regresi volí **vážený průměr**, kde $w_i \ge 0$ jsou váhy jednotlivých sousedů:
$$\hat{y} = \frac{\sum_{i=1}^k w_i y_i}{\sum_{i=1}^k w_i}.$$
Váhy se obvykle volí tak, aby **klesaly se vzdáleností**; v `scikit-learn` lze nastavit `weights=distance`, které zvolí
$$w_i = \frac{1}{d(\boldsymbol{x}, \boldsymbol{x}_i)}.$$

**Pseudokód predikce kNN:**
```
vstup: trénovací data {(x_i, Y_i)}_{i=1..N}, dotazovaný bod x, k, metrika d, váhy
1. pro i = 1..N spočti d_i = d(x, x_i)
2. setřiď body podle d_i vzestupně, vyber prvních k → sousedé x_(1),...,x_(k)
3. klasifikace: ŷ = nejčastější hodnota mezi Y_(1),...,Y_(k)   # většinové hlasování
   regrese:    ŷ = (Σ w_i Y_(i)) / (Σ w_i)                      # (vážený) průměr
```

### 2.3 Hyperparametry

Pro regresi i klasifikaci jsou smysluplné tři hyperparametry (přímo dostupné ve `scikit-learn` třídách `KNeighborsClassifier` / `KNeighborsRegressor`):
- **$k$** — počet hledaných nejbližších sousedů (`n_neighbors`);
- **metrika** — použitá vzdálenost, obecně funkce vracející dvěma bodům číslo (`metric`);
- **váhy** sousedů — určují „sílu jejich hlasu" při predikci (`weights`).

### 2.4 Učení vs. predikce (líné učení)

U většiny metod supervizovaného učení je výpočetně náročná **fáze učení** modelu, kdežto predikce je rychlá (např. u **[[Rozhodovací-strom|rozhodovacích stromů]]** stačí průchod nehlubokým stromem).

U kNN je tomu **naopak** — jde o tzv. **líné učení** (*lazy learning*): učení vlastně neprobíhá, **trénovací data jsou sama o sobě naučeným modelem**. Výpočetně náročná je naopak **predikce**: hledání nejbližších sousedů vyžaduje průchod všemi trénovacími daty a změření vzdálenosti od každého trénovacího bodu. (To je opak *eager* přístupu rozhodovacích stromů či regrese.)

Predikci lze zrychlit **indexací dat** do vyhledávacího stromu (např. k-d strom); situace se pak „znormalizuje" — predikce se zrychlí na úkor učení, tj. tvorby indexu.

### 2.5 Normalizace dat

Na rozdíl od rozhodovacích stromů je kNN **náročná na přípravu dat** a citlivá na typy a měřítka jednotlivých příznaků.

**Problém různého měřítka.** Mějme dva příznaky — rozměry půdorysu bazénu, kde $x_1$ je v centimetrech a $x_2$ v metrech. Pro domy s bazény o straně 5 a 6 m je příspěvek do eukleidovské vzdálenosti
$$(500 - 600)^2 + (5 - 6)^2 = 100^2 + 1 = 10001,$$
takže ačkoli se oba příznaky liší o „stejnou" velikost, změna v $x_2$ je proti $x_1$ zcela zanedbatelná — příznak s větším měřítkem dominuje vzdálenosti. Proto se data **normalizují**.

**Min-max normalizace** do intervalu $[0,1]$ — pro daný příznak najdeme jeho minimum a maximum v trénovacích datech a hodnotu $x_i$ nahradíme:
$$x_i \leftarrow \frac{x_i - \min_x}{\max_x - \min_x}.$$
Změny v jednotlivých příznacích se pak porovnávají s maximálním možným rozdílem hodnot, čímž se dosáhne omezené souměřitelnosti.

**Standardizace** — pomocí výběrového průměru $\bar{x}$ a výběrového rozptylu $s_x^2$:
$$x_i \leftarrow \frac{x_i - \bar{x}}{\sqrt{s_x^2}}, \qquad \bar{x} = \tfrac{1}{n}\sum_i x_i, \quad s_x^2 = \tfrac{1}{n-1}\sum_i (x_i - \bar{x})^2.$$

**Pozor:** normalizace po příznacích není univerzální. Např. u MNIST (obrázky $28\times28 = 784$ pixelů, hodnoty 0–255) jsou všechny příznaky souměřitelné (stejné měřítko i význam), normalizace po jednotlivých příznacích by tu spíše uškodila (pixely vždy nulové či jen někde šedé). Lze normalizovat do $[0,1]$, ale globálně (přes všechny sloupce), tj. $\min_X = 0$, $\max_X = 255$. Normalizace dat je obecně velké a složité téma bez univerzálně správného přístupu.

### 2.6 Prokletí dimenzionality

**Prokletí dimenzionality** (*the curse of dimensionality*) označuje problémy objevující se při vysokém počtu příznaků, kdy jsou datové body prvky mnohadimenzionálního prostoru. S kNN jsou spojeny zejména dva efekty:
- **Data se zvyšováním dimenze řídnou** a navzájem se vzdalují. Pro zachování stejné hustoty by bylo nutné řádově navýšit počet datových bodů, což obvykle není možné.
- **S rostoucí dimenzí** se pro klasické metriky **zmenšují rozdíly** mezi vzdáleným a blízkým bodem — pojem „nejbližší soused" ztrácí rozlišovací sílu.

*Příklad řídnutí.* Mějme $d$-dimenzionální jednotkovou krychli $[0,1]^d$ a v ní rovnoměrně rozhozeno 1000 bodů. Jak velkou podkrychli o hraně $a$ potřebujeme, aby obsahovala v průměru 10 bodů (pokrývala $\tfrac{1}{100}$ objemu)? Z $a^d = \tfrac{1}{100}$ plyne $a = \sqrt[d]{1/100}$: pro $d=1$ je $a=0{,}01$, pro $d=3$ je $a\approx0{,}215$, pro $d=10$ je $a\approx0{,}63$ a pro $d=50$ dokonce $a\approx0{,}91$. „Lokální" okolí tak ve vysoké dimenzi pokrývá téměř celý rozsah každého příznaku — body jsou od sebe velmi vzdálené.

### 2.7 Vliv $k$ na přeučení

Většinu modelů lze **přeučit** (*overfitting*) — např. u rozhodovacích stromů stačilo vytvořit příliš hluboký strom s mnoha listy. U kNN přeučení odpovídá malému $k$:
- **$k = 1$** — model kopíruje každý trénovací bod, rozhodovací hranice je velmi členitá (přeučení).
- **velké $k$** — predikce se zprůměruje přes více sousedů, rozhodovací hranice se vyhladí.

Přeučení tedy zabraňujeme **zvýšením počtu sousedů $k$**. (Příliš velké $k$ ovšem vede k podučení — v limitě $k = N$ predikuje kNN konstantu: globální většinovou třídu, resp. globální průměr.)

---

## 3. Aglomerativní hierarchické shlukování

Shlukování (clustering) je metoda **[[Nesupervizované-učení|nesupervizovaného učení]]** (učení bez učitele): data nejsou nijak označena a cílem je porozumět jejich vnitřní struktuře. **[[Shluková-analýza|Shluková analýza]]** roztřídí data do skupin (shluků) tak, aby *blízké body byly ve stejném shluku* a *vzdálené body v různých shlucích*. (Obecné principy nesupervizovaného učení a algoritmus k-means patří k otázce 14.)

### 3.1 Vstupy a výstupy

**Vstupy:**
- metrický prostor $\mathcal{X}$ se vzdáleností $d$,
- množina dat $\mathcal{D} \subset \mathcal{X}$,
- obvykle také požadovaný počet shluků $k$.

**Výstup** — *rozklad* množiny dat na shluky. Je to $C = (C_1,\dots,C_k)$, kde $C_i \subset \mathcal{D}$ pro každé $i$, $C_i \cap C_j = \emptyset$ pro $i \neq j$ a
$$\mathcal{D} = \bigcup_{i=1}^k C_i.$$
Bod $x \in \mathcal{D}$ je v $i$-tém shluku, jestliže $x \in C_i$. U hierarchického shlukování může být finálním výstupem **dendrogram** — grafické znázornění hierarchické struktury shlukování.

### 3.2 Algoritmus (hladový aglomerativní přístup)

Aglomerativní (zdola-nahoru) přístup. Označme $N$ počet prvků množiny dat $\mathcal{D}$.
- Na začátku považujeme **každý bod za samostatný shluk** — máme tedy právě $N$ shluků.
- Opakovaně provádíme:
  1. najdeme dva shluky, které jsou k sobě **nejblíže**,
  2. tyto dva shluky **spojíme** do nového shluku.
- Po $N-1$ opakováních skončíme s **jediným velkým shlukem** obsahujícím všechny body.

K provedení postupu je třeba stanovit **způsob měření vzdálenosti dvou shluků** (§3.3). Má-li být výstupem konkrétní shlukování (a ne celý dendrogram), je třeba určit **zastavovací kritérium** (§3.5) — nejčastěji počet shluků $k$, případně limitní hodnotu vzdálenosti, nad kterou už shluky nespojujeme. (Vzdálenost spojovaných shluků v každém kroku neklesá.)

**Pseudokód:**
```
vstup: data D = {x_1,...,x_N}, vzdálenost bodů d, kritérium spojování (linkage) D(·,·)
1. inicializuj N shluků, každý {x_i} je samostatný shluk
2. opakuj (N-1)-krát (resp. dokud není splněno zastavovací kritérium):
       najdi dvojici shluků (A, B) s nejmenším D(A, B)
       spoj A a B do nového shluku A ∪ B; ulož výšku spojení = D(A, B)
3. výstup: dendrogram (posloupnost spojení); rozklad získáš jeho rozříznutím
```

### 3.3 Kritéria spojování shluků (linkage)

Vstupem do shlukování je vzdálenost dvojice bodů $d(x,y)$. Z ní odvodíme vzdálenost dvou shluků $D(A,B)$ jedním z těchto způsobů:

**Metoda nejbližšího souseda** (*single linkage*) — generuje dlouhé řetězce:
$$D(A,B) = \min_{x \in A,\, y \in B} d(x,y).$$

**Metoda nejvzdálenějšího souseda** (*complete linkage*) — generuje kompaktní shluky:
$$D(A,B) = \max_{x \in A,\, y \in B} d(x,y).$$

**Párová vzdálenost** (*average linkage*) — kompromis předchozích dvou:
$$D(A,B) = \frac{1}{|A|\,|B|} \sum_{x \in A,\, y \in B} d(x,y).$$

**Wardova metoda** (na $\mathbb{R}^p$) — velmi účinná, minimalizuje nárůst vnitřního rozptylu při spojení:
$$D(A,B) = \sum_{\boldsymbol{x} \in A \cup B} \|\boldsymbol{x} - \bar{\boldsymbol{x}}_{A\cup B}\|^2 - \sum_{\boldsymbol{x} \in A} \|\boldsymbol{x} - \bar{\boldsymbol{x}}_A\|^2 - \sum_{\boldsymbol{x} \in B} \|\boldsymbol{x} - \bar{\boldsymbol{x}}_B\|^2,$$
kde $\bar{\boldsymbol{x}}_A = \tfrac{1}{|A|}\sum_{\boldsymbol{x}\in A}\boldsymbol{x}$ je geometrický střed množiny $A$ a $\bar{\boldsymbol{x}}_B, \bar{\boldsymbol{x}}_{A\cup B}$ analogicky.

### 3.4 Dendrogram

Celý proces aglomerativního shlukování lze reprezentovat a graficky znázornit pomocí **dendrogramu**:
- Jde o **strom**, jehož vrcholy představují shluky, které při běhu vznikly.
- V **listech** jsou počáteční jednoprvkové shluky, **kořen** reprezentuje finální shluk všech bodů.
- Strom je nakreslen tak, že všechny listy jsou ve výšce $0$ a **výška ostatních vrcholů odpovídá vzdálenosti** podřazených shluků, které se v tomto vrcholu spojily.

### 3.5 Volba počtu shluků

Z dendrogramu lze získat konkrétní shlukování několika způsoby:
- Známe-li požadovaný počet $k$ shluků, **rozřízneme** dendrogram mezi $k$-tým a $(k-1)$-ním nejvyšším vrcholem; hrany procházející řezem odpovídají výsledným shlukům.
- Nebo stanovíme **limitní hranici vzdálenosti** a dendrogram rozřízneme v dané výšce.
- Případně určíme místo rozříznutí (a tím počet shluků) pomocí **největšího rozdílu výšek** sousedních vrcholů.

### 3.6 Vlastnosti, složitost a poznámky

- **Výhoda:** hierarchické shlukování dává ucelený pohled pomocí dendrogramu a teprve na jeho základě lze vybírat vhodný počet shluků (na rozdíl od k-means, kde se $k$ stanovuje předem).
- **Hierarchická struktura:** při zvýšení počtu shluků o jeden dojde pouze k rozdělení některého ze stávajících, ostatní se nemění.
- **Kvalita** dendrogramu (z pohledu zachování párových vzdáleností originálních dat) se měří např. pomocí *cophenetic correlation*.
- Existuje i **divizní** hierarchické shlukování (shora-dolů): vychází z jednoho shluku a opakovaně dělí.
- **Složitost.** V jednom kroku aglomerativního algoritmu je třeba provést $\tfrac{m(m-1)}{2}$ porovnání, kde $m$ je aktuální počet shluků — celkem $\mathcal{O}(N^3)$. Pro single nebo complete linkage lze dosáhnout $\mathcal{O}(N^2)$. (Pro srovnání: divizní algoritmus dělá v kroku $2^{m-1}$ porovnání, tedy $\mathcal{O}(2^N)$.) Hierarchické shlukování se proto **příliš nehodí pro velké datové soubory**.

---

## Co je potřeba na zkoušku znát

### Definice
- **Metrika** $d : \mathcal{X}\times\mathcal{X} \to [0,+\infty)$: (1) pozitivní definitnost ($d(x,y)\ge0$, $=0 \iff x=y$), (2) symetrie, (3) trojúhelníková nerovnost. $(\mathcal{X},d)$ = metrický prostor.
- **Příklady metrik:** $L_2$ (eukleidovská) $\sqrt{\sum(x_i-y_i)^2}$, $L_1$ (manhattanská) $\sum|x_i-y_i|$, $L_\infty$ (Čebyševova) $\max_i|x_i-y_i|$; obecně $L_q = \sqrt[q]{\sum|x_i-y_i|^q}$. Na řetězcích Levenštejnova; kosinová $\tfrac{\boldsymbol{x}\cdot\boldsymbol{y}}{\|\boldsymbol{x}\|\|\boldsymbol{y}\|}$.
- **kNN:** najdi $k$ nejbližších trénovacích bodů; klasifikace = většinové hlasování, regrese = (vážený) průměr $\hat{y} = \tfrac{1}{k}\sum y_i$.
- **Linkage:** single $\min d$, complete $\max d$, average $\tfrac{1}{|A||B|}\sum d$, Ward (nárůst vnitřního rozptylu).
- **Rozklad shlukování:** disjunktní $C_1,\dots,C_k$ s $\bigcup C_i = \mathcal{D}$.

### Věty
- (Žádná netriviální věta s důkazem; klíčové jsou definice a algoritmy.)
- Vlastnostní fakta k zapamatování: malé $k$ → přeučení, velké $k$ → vyhlazení/podučení; prokletí dimenzionality (data řídnou a vzdalují se, rozdíly vzdáleností mizí); vzdálenost spojovaných shluků v dendrogramu neklesá.

### Algoritmy
- **kNN predikce:** spočti vzdálenosti k všem $N$ bodům, vyber $k$ nejbližších, hlasuj/průměruj. Líné učení (data = model), náročná predikce, zrychlení indexací. Hyperparametry $k$, metrika, váhy. Data nutno normalizovat (min-max, standardizace).
- **Aglomerativní hierarchické shlukování:** $N$ jednoprvkových shluků → opakovaně spoj dva nejbližší (dle linkage) → po $N-1$ krocích jeden shluk. Výstup dendrogram, rozříznutí dle $k$ / výšky. Složitost $\mathcal{O}(N^3)$, pro single/complete $\mathcal{O}(N^2)$.
