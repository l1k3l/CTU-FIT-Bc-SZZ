---
studyplan: true
etapa: "4 · ML1 / ML2 — Dedecius + Holeňa"
qid: "14ML1"
examiner: "Dedecius"
topic: "Nesupervizované učení: k-means, DBSCAN"
readiness: nezačato
tags: [otázka, kurz/ML1, otázka/14, todo]
---

# Nesupervizované učení, k-means a DBSCAN

> **Otázka SZZ:** Nesupervizované učení – základní prinicipy, algoritmus k-means, DBSCAN.

Zdroje: BI-ML1 (FIT ČVUT), přednáška 11 — sekce 41 Úvod do nesupervizovaného učení, 42 Shluková analýza, 44 Algoritmus k-means; přednáška 12 — sekce 45 Shlukování pomocí hustoty, 46 DBSCAN, 47 Silhouette skóre. (Hierarchické aglomerativní shlukování ze sekce 43 patří k otázce 9 — zde jen zmíníme.)

Značení: $\mathcal{X}$ prostor příznaků (možných hodnot), $X = (X_1,\dots,X_p)^T$ náhodný vektor pozorovaných příznaků, $f_X$ jeho hustota pravděpodobnosti, $\mathcal{D} \subset \mathcal{X}$ dataset (množina dat) o $N$ bodech, $d$ metrika (vzdálenost) na $\mathcal{X}$, $\|\cdot\|$ eukleidovská norma, $k$ počet shluků, $C = (C_1,\dots,C_k)$ rozklad na shluky, $\mu_i$ centroid (geometrický střed) $i$-tého shluku, $\varepsilon > 0$ a $\text{MinPts} \in \mathbb{N}^+$ parametry DBSCAN.

---

## 1. Nesupervizované učení — základní principy

### 1.1 Vymezení

**[[Nesupervizované-učení|Nesupervizované učení]]** (angl. *unsupervised learning*, též **učení bez učitele**) nastává v situaci, kdy data **nemáme nikterak označená** — neexistuje žádná vysvětlovaná veličina (cílová proměnná), kterou bychom u trénovacích dat znali a snažili se ji naučit predikovat. To je zásadní rozdíl oproti supervizovanému učení (klasifikace, regrese), kde každý trénovací bod nese označení.

**Cílem** nesupervizovaného učení je **porozumět vnitřní struktuře dat** pouze na základě dat samotných, tj. bez vnějšího vodítka. Porozuměním zde typicky myslíme nalezení co „nejmenších" oblastí v prostoru příznaků $\mathcal{X}$, kde se data vyskytují nejčastěji.

Motivace: naměřená data se obvykle **nevyskytují v celém prostoru stejně pravděpodobně**, ale bývají více či méně **lokalizována** — tvoří shluky, vyskytují se v méně-dimenzionálních oblastech apod. Porozumění této lokalizaci přináší důležitou informaci o vnitřní struktuře dat.

> *Doplnění nad rámec slidů (zkoušející se ptal na zařazení mezi paradigmata):* tři základní paradigmata strojového učení se liší tím, jaké vodítko (zpětnou vazbu) má model k dispozici:
> - **supervizované učení** — každý trénovací bod nese **označení** (cílovou proměnnou); učíme se predikovat (klasifikace, regrese);
> - **nesupervizované učení** — data **bez označení**; učíme se vnitřní strukturu (shlukování, redukce dimenzionality, odhad hustoty);
> - **posílené učení** (angl. *reinforcement learning*) — není pevný dataset s odpověďmi; agent **interaguje s prostředím**, koná akce a dostává **odměnu** (zpožděnou, řídkou) a učí se strategii (politiku) maximalizující kumulativní odměnu.

### 1.2 Pravděpodobnostní pohled — odhad hustoty

Z pohledu teorie pravděpodobnosti a statistiky (viz BI-PST) chápeme pozorovaná data jako **realizace [[Náhodný-vektor|náhodného vektoru]]** $X = (X_1,\dots,X_p)^T$. Označme $\mathcal{X}$ prostor možných výsledků (volba $\mathcal{X}$ je součástí volby modelu):

- pro $p$ binárních příznaků volíme $\mathcal{X} = \{0,1\}^p$;
- pro $p$ spojitých příznaků typicky $\mathcal{X} = \mathbb{R}^p$.

Porozumět vnitřní struktuře dat pak znamená **porozumět rozdělení** $X$, tj. získat odhad pravděpodobnosti $\mathrm{P}(X \in O)$ pro každou rozumnou podmnožinu $O \subset \mathcal{X}$. Ekvivalentně:

- pro spojité příznaky odhadnout sdruženou **hustotu pravděpodobnosti** $f_X(x) \equiv f_X(x_1,\dots,x_p)$;
- pro diskrétní příznaky odhadnout sdruženou **pravděpodobnostní funkci** $p_X(x) \equiv \mathrm{P}(X_1 = x_1,\dots,X_p = x_p)$.

Soustředíme se přitom zejména na nalezení oblastí v $\mathcal{X}$, které mají velkou pravděpodobnost a jsou přitom „co nejmenší". Tyto oblasti vysoké hustoty odpovídají shlukům — to je společný motiv shlukovacích algoritmů a hustotních metod (DBSCAN, sekce 3).

### 1.3 Problém vyhodnocení úspěšnosti

Obecným problémem nesupervizovaného učení je, že **vůbec není jasné, jak vyhodnocovat úspěšnost** získaného porozumění. To je velký rozdíl oproti supervizovanému učení, kde lze kvalitu modelu hodnotit mnoha více méně rovnocennými způsoby (např. přesností u klasifikace, kde máme správné odpovědi). Absence jednoznačného hodnotícího kritéria vede k tomu, že existuje více způsobů formalizace úlohy a mnoho různých algoritmů, které na stejných datech mohou dávat **velmi rozdílné výsledky**.

### 1.4 Vztah k redukci dimenzionality

Druhým velkým proudem nesupervizovaného učení (vedle shlukování a odhadu hustoty) je **redukce dimenzionality**. Příklad: leží-li body v $\mathbb{R}^3$ na kouli, lze jejich polohu popsat dvěma sférickými souřadnicemi a získat ekvivalentní reprezentaci pomocí dvou spojitých příznaků místo tří. Tím se zachová podstatná informace o struktuře dat při nižším počtu příznaků. (Detailněji není předmětem této otázky.)

---

## 2. Shluková analýza a algoritmus k-means

### 2.1 Shluková analýza — cíl a vstupy/výstupy

Jednou ze základních metod nesupervizovaného učení je **[[Shluková-analýza|shlukování]]** (angl. *clustering*). Cílem je roztřídit data do skupin (**shluků**) tak, aby platily dva přirozené (a obecně **nekompatibilní**) požadavky:

- blízké body budou ve stejném shluku;
- vzdálené body budou v různých shlucích.

Tento popis je vágní a požadavky nelze obecně splnit současně; spolu s neexistencí hodnotícího kritéria kvality to vede k existenci mnoha různých formalizací a algoritmů.

Klíčovým pojmem, na němž shlukování stojí, je vzdálenost. Pracujeme v **[[Metrika|metrickém prostoru]]** $(\mathcal{X}, d)$, kde $d: \mathcal{X} \times \mathcal{X} \to [0,+\infty)$ je **metrika** (vzdálenost) splňující pro všechna $x,y,z \in \mathcal{X}$:

1. $d(x,y) \ge 0$, a $d(x,y) = 0 \iff x = y$ (pozitivní definitnost);
2. $d(x,y) = d(y,x)$ (symetrie);
3. $d(x,y) \le d(x,z) + d(z,y)$ (trojúhelníková nerovnost).

Na $\mathbb{R}^p$ se nejčastěji používá eukleidovská ($L_2$) vzdálenost $d_2(x,y) = \sqrt{\sum_{i=1}^p (x_i - y_i)^2}$, dále manhattanská ($L_1$) $d_1(x,y) = \sum_i |x_i - y_i|$ a Čebyševova ($L_\infty$) $d_\infty(x,y) = \max_i |x_i - y_i|$. (Metrika je hlavním tématem **otázky 9** — tam i příklady $L_q$, Levenštejnova vzdálenost a aglomerativní hierarchické shlukování.)

**Vstupy** shlukování: metrický prostor $\mathcal{X}$ se vzdáleností $d$, množina dat $\mathcal{D} \subset \mathcal{X}$, obvykle požadovaný počet shluků $k$.

**Výstup** shlukování: rozklad množiny dat na shluky $C = (C_1,\dots,C_k)$, kde $C_i \subset \mathcal{D}$ pro každé $i$ a $C_i \cap C_j = \emptyset$ pro $i \ne j$, přičemž
$$\mathcal{D} = \bigcup_{i=1}^k C_i.$$
Bod $x \in \mathcal{D}$ je v $i$-tém shluku, jestliže $x \in C_i$.

> **Vztah k jiným metodám.** Vedle nehierarchického k-means a hustotního DBSCAN existuje i **hierarchické aglomerativní shlukování** (dendrogram, single/complete/average/Ward linkage) — to je předmětem otázky 9.

### 2.2 Formulace shlukování jako optimalizační úlohy (WCSS)

Oblíbeným přístupem ke shlukování je formulace ve tvaru **optimalizační úlohy**: definujeme **účelovou funkci** (angl. *objective function*) ohodnocující daný rozklad a hledáme rozklad, který ji minimalizuje.

Pro dané $k$ hledáme rozklad $C = (C_1,\dots,C_k)$ na $\mathcal{X} = \mathbb{R}^p$ s eukleidovskou vzdáleností, který minimalizuje účelovou funkci
$$G(C) = \sum_{i=1}^k \frac{1}{2|C_i|} \sum_{x,y \in C_i} \|x - y\|^2.$$
V účelové funkci se pro každý shluk sečtou průměrné kvadráty vzdáleností všech dvojic bodů daného shluku. Tuto funkci lze elegantně vyjádřit pomocí součtů kvadrátů vzdáleností od geometrických středů (těžišť) shluků — to je **vnitroshlukový součet čtverců** (WCSS, *within-cluster sum of squares*).

**Tvrzení (souvislost s geometrickým středem).** Pro konečnou množinu bodů $A \subset \mathbb{R}^p$ platí
$$\frac{1}{2|A|}\sum_{x,y \in A} \|x - y\|^2 = \sum_{x \in A} \|x - \bar{x}\|^2 = \min_{\mu \in \mathbb{R}^p} \sum_{x \in A} \|x - \mu\|^2,$$
kde $\bar{x} = \frac{1}{|A|}\sum_{x \in A} x$ je geometrický střed (centroid) množiny $A$.

*Důkaz.* Pro každé $a,b \in \mathbb{R}^p$ platí $\|a - b\|^2 = (a-b)^T(a-b) = \|a\|^2 - 2a^Tb + \|b\|^2$ (neboť $b^Ta = a^Tb$). Pro $a = x - \mu$, $b = y - \mu$ z toho plyne
$$\frac{1}{2|A|}\sum_{x,y\in A}\|x-y\|^2 = \frac{1}{2|A|}\sum_{x,y}\|x-\mu\|^2 + \frac{1}{2|A|}\sum_{x,y}\|y-\mu\|^2 - \frac{1}{|A|}\sum_{x,y}(x-\mu)^T(y-\mu).$$
První dva členy dají dohromady $\sum_{x \in A}\|x - \mu\|^2$. Poslední člen upravíme:
$$\frac{1}{|A|}\sum_{x,y}(x-\mu)^T(y-\mu) = \frac{1}{|A|}\Big(\sum_x (x-\mu)\Big)^T\Big(\sum_y (y-\mu)\Big) = \frac{1}{|A|}\Big\|\sum_{x\in A}(x-\mu)\Big\|^2.$$
Tento člen je vždy nezáporný a roven nule právě tehdy, když $\mu = \bar{x}$ (z definice $\bar{x}$). Proto
$$\frac{1}{2|A|}\sum_{x,y\in A}\|x-y\|^2 \le \sum_{x\in A}\|x-\mu\|^2,\quad\text{s rovností pouze pro }\mu = \bar{x}. \qquad\square$$

Důsledkem je vyjádření účelové funkce přes centroidy:
$$G(C) = \sum_{i=1}^k \sum_{x \in C_i} \|x - \bar{x}_i\|^2, \qquad \bar{x}_i = \frac{1}{|C_i|}\sum_{x \in C_i} x.$$
Nalezení **globálního** minima této funkce je výpočetně obtížné (NP-těžké). Algoritmus k-means je heuristický iterativní postup konvergující k **lokálnímu** minimu.

### 2.3 Algoritmus k-means (Lloydův algoritmus)

**Slovní popis.** Nejprve zvolíme $k$ středových bodů (centroidů). Iterativně opakujeme:

1. **Přiřazení:** vytvoříme shluky odpovídající středovým bodům — pro každý bod $x$ najdeme nejbližší středový bod a podle něj $x$ zařadíme do příslušného shluku.
2. **Přepočet:** spočítáme nové středové body jako geometrické středy těchto shluků.

**Algoritmus (k-means).**
```
vstup: data D, počet shluků k, metrika (eukleidovská)
inicializace: počáteční rozmístění k středových bodů μ_1, ..., μ_k
opakuj:
    # 1. přiřazení bodů k nejbližšímu centroidu
    for i = 1, ..., k:
        C_i = { x ∈ D | i = argmin_j ||x - μ_j|| }
    # 2. přepočet centroidů
    for i = 1, ..., k:
        μ_i = (1 / |C_i|) Σ_{x ∈ C_i} x
dokud změna účelové funkce mezi iteracemi není dostatečně malá
výstup: rozklad C = (C_1, ..., C_k)
```

**Důkaz konvergence k lokálnímu minimu.** V každé iteraci účelová funkce **neroste**:

- *Krok přiřazení.* Zafixujme centroidy $\mu_i = \bar{x}_i$ z minulé iterace a přesuňme každý bod $x$ do shluku $\tilde{C}_i$ s nejmenší vzdáleností $\|x - \mu_i\|$. Tím se jistě nezvětší součet kvadrátů vzdáleností od (zafixovaných) středů:
$$\sum_{i=1}^k \sum_{x \in \tilde{C}_i} \|x - \mu_i\|^2 \le \sum_{i=1}^k \sum_{x \in C_i} \|x - \mu_i\|^2 = G(C).$$
- *Krok přepočtu.* Z tvrzení 2.2 (minimum přes $\mu$ se nabývá v centroidu) plyne pro nové centroidy $\bar{x}_i'$ shluků $\tilde{C}_i$:
$$G(\tilde{C}) = \sum_{i=1}^k \sum_{x \in \tilde{C}_i} \|x - \bar{x}_i'\|^2 \le \sum_{i=1}^k \sum_{x \in \tilde{C}_i} \|x - \mu_i\|^2.$$

Dohromady $G(\tilde{C}) \le G(C)$. Posloupnost hodnot $G$ je nerostoucí a zdola omezená, navíc rozkladů je konečně mnoho — algoritmus tedy konverguje k **lokálnímu** minimu. $\square$

**Zastavení.** Běh zastavíme, jakmile je změna hodnoty účelové funkce mezi iteracemi dostatečně malá (ekvivalentně se přiřazení bodů přestane měnit).

### 2.4 Citlivost na inicializaci a k-means++

Výsledek významně závisí na inicializační části. Obvykle se počáteční středy generují náhodně (např. náhodným výběrem $k$ bodů z dat); existují i „chytřejší" metody jako **k-means++** (David, Vassilvitskii, 2007), které volí počáteční centroidy rozprostřeně. Protože algoritmus dává jen lokální minimum, **spouští se opakovaně** s různou inicializací a jako finální se bere běh s **nejnižší** hodnotou účelové funkce.

### 2.5 Volba počtu shluků $k$

Na rozdíl od hierarchického shlukování (kde počet shluků určíme až z dendrogramu) je u k-means nutné **stanovit $k$ dopředu**. Univerzální automatický způsob neexistuje; používané heuristiky:

- **Metoda lokte (elbow).** Vykreslíme hodnotu účelové funkce (WCSS) v závislosti na $k$. Je-li $k^\*$ optimální počet, pro $k < k^\*$ funkce klesá prudce, pro $k \ge k^\*$ se pokles výrazně zmírní. Optimální $k$ detekujeme jako „loket" (zlom) v grafu. Je to subjektivní a pro některá data prakticky nepoužitelné (slidy ukazují příklad, kde loket dá $k=2$, ač data vznikla jako směs **tří** normálních rozdělení).
- **Silhouette skóre** (viz sekce 3.7) — robustnější kvantitativní kritérium: $k$ volíme tak, aby průměrné $s$ bylo maximální.
- Někdy je $k$ **dáno typem úlohy / předem známé** (víme, kolik shluků očekáváme — např. počet tříd, segmentů), pak jej nemusíme odhadovat z dat.

### 2.6 Vlastnosti a omezení k-means

- **Časová složitost** jedné iterace je $\mathcal{O}(Nkp)$ (každý z $N$ bodů se porovná s $k$ centroidy v $p$-rozměrném prostoru); celkem krát počet iterací. Algoritmus je rychlý a dobře škáluje na velká data.
- **Sférické shluky.** Účelová funkce minimalizuje rozptyl kolem centroidů — k-means proto preferuje přibližně **sférické (kulové), podobně velké** shluky a selhává na protáhlých či nekonvexních tvarech.
- **Nutnost zadat $k$** dopředu.
- **Citlivost na inicializaci** (jen lokální minimum) a na **odlehlé hodnoty** (centroid táhnou k sobě; k-means neumí body označit jako šum).

---

## 3. DBSCAN

### 3.1 Shlukování pomocí hustoty — motivace

**DBSCAN** (angl. *density-based spatial clustering of applications with noise*, Ester et al. 1996) je jeden z nejpoužívanějších algoritmů shlukování, implicitně založený na principu **odhadu hustoty** rozdělení dat na prostoru $\mathcal{X}$. Myšlenka: máme-li (úměrný) odhad hustoty $f_X$, získáme shluky jako **souvislé oblasti, kde hustota překročí zvolenou hranici**, a body mimo tyto oblasti označíme jako **šum**. DBSCAN tuto myšlenku realizuje lokálně přes počítání bodů v okolí.

Pracujeme v **metrickém prostoru** $\mathcal{X}$ s metrikou $d(x,y)$, z něhož pochází dataset $\mathcal{D}$, a se dvěma parametry $\varepsilon > 0$ a $\text{MinPts} \in \mathbb{N}^+$.

### 3.2 Základní pojmy

**Definice ($\varepsilon$-okolí).** $\varepsilon$-okolí bodu $x$ v $\mathcal{D}$ (angl. *$\varepsilon$-neighborhood*) je množina
$$N_\varepsilon(x) = \{ y \in \mathcal{D} \mid d(x,y) \le \varepsilon \}.$$

**Definice (klíčový bod).** Bod $x \in \mathcal{D}$ je **klíčový bod** (angl. *core point*), jestliže jeho $\varepsilon$-okolí obsahuje alespoň $\text{MinPts}$ bodů,
$$|N_\varepsilon(x)| \ge \text{MinPts}.$$

**Definice (okrajový bod).** **Okrajový bod** (angl. *border point*) je bod, který **není klíčový**, ale je přímo dosažitelný z nějakého klíčového bodu.

**Šum** (angl. *noise*) jsou body, které nejsou ani klíčové, ani okrajové (neleží v žádném shluku) — viz definice níže.

### 3.3 Dosažitelnost a spojenost

**Definice (přímá dosažitelnost).** Bod $y \in \mathcal{D}$ je **přímo dosažitelný** (angl. *directly density-reachable*) z bodu $x \in \mathcal{D}$, jestliže $x$ je klíčový bod a $y \in N_\varepsilon(x)$.

Relace přímé dosažitelnosti je **symetrická pro dvojici klíčových bodů**, ale **nesymetrická** pro okrajový bod (okrajový bod může být přímo dosažitelný z klíčového, ale ne naopak — okrajový bod není klíčový, takže z něj nelze přímo dosáhnout nic).

**Definice (dosažitelnost).** Bod $y \in \mathcal{D}$ je **dosažitelný** (angl. *density-reachable*) z bodu $x \in \mathcal{D}$, pokud existuje posloupnost bodů $x_1, x_2, \dots, x_n \in \mathcal{D}$ taková, že $x_1 = x$, $x_n = y$ a pro každé $i = 1,\dots,n-1$ je $x_{i+1}$ přímo dosažitelný z $x_i$.

Z toho plyne, že všechny body po cestě **kromě posledního** ($y$) musí být klíčové body.

**Definice (spojenost).** Bod $y \in \mathcal{D}$ je **spojený** (angl. *density-connected*) s bodem $x \in \mathcal{D}$, jestliže existuje (klíčový) bod $p \in \mathcal{D}$ takový, že $x$ i $y$ jsou dosažitelné z bodu $p$.

Relace spojenosti je zjevně **symetrická**; pro klíčové body je také **tranzitivní**. Jsou-li dva body spojené a jeden z nich je klíčový, pak ten druhý je z toho prvního dosažitelný.

### 3.4 Shluk a šum

**Definice (shluk).** **Shluk** (angl. *cluster*) $C$ je podmnožina $\mathcal{D}$ obsahující alespoň jeden klíčový bod taková, že:

- **(maximalita)** pro každé $x,y \in \mathcal{D}$ platí: je-li $x \in C$ a $y$ je dosažitelný z $x$, pak $y \in C$;
- **(souvislost)** pro každé $x,y \in C$ je $x$ spojený s $y$.

Tedy **shluk = maximální množina vzájemně spojených bodů**. Označme $C_1,\dots,C_k$ množinu všech shluků v $\mathcal{D}$ (vzhledem k $\varepsilon$ a $\text{MinPts}$). Množinu $N$ bodů z $\mathcal{D}$, které nejsou v žádném shluku, nazýváme **šumem**:
$$N = \mathcal{D} \setminus \bigcup_{i=1}^k C_i.$$

**Poznámky k definici.** Každý shluk $C$ obsahuje klíčový bod $p \in C$, z něhož jsou dosažitelné všechny body v jeho $\varepsilon$-okolí (kterých je alespoň $\text{MinPts}$), takže **každý shluk obsahuje alespoň $\text{MinPts}$ bodů**. Každý bod ve shluku je spojený se všemi klíčovými body v $C$, a tedy z libovolného klíčového bodu dosažitelný. To dává návod na algoritmus: najdeme klíčový bod a vytvoříme k němu shluk jako množinu všech z něj dosažitelných bodů (které ještě nejsou v jiném shluku).

### 3.5 Algoritmus

**Abstraktní popis (DBSCAN).**
```
vstup: dataset D, metrika d, parametry ε, MinPts
# 1. nalezení klíčových bodů
spočítej ε-okolí každého bodu a označ klíčové body (|N_ε(x)| ≥ MinPts)
# 2. vytvoření zárodků shluků
spoj sousední (přímo dosažitelné) klíčové body do shluků
# 3. zařazení neklíčových bodů
for každý bod x, který není klíčový:
    pokud má ve svém ε-okolí klíčový bod:
        přidej x do shluku podle (prvního) klíčového bodu v okolí
    jinak:
        přidej x mezi šum
výstup: shluky C_1, ..., C_k a šum N
```
**Poznámka.** Okrajový bod, který má ve svém $\varepsilon$-okolí klíčové body z různých (zárodků) shluků, spadne do **prvního** z nich, ke kterému jej algoritmus dostane. Výsledné shluky proto v takovém případě **nesplňují podmínku maximality** z definice (okrajový bod je jen v jednom shluku, nikoliv ve všech, kam by podle maximality patřil) — to je drobná nekonzistence implementace oproti formální definici.

**Časová složitost.** V nejhorším případě $\mathcal{O}(N^2)$ (počítání okolí všech dvojic). S vhodnou prostorovou indexovou strukturou (např. R-strom) se v mnoha reálných situacích lze dostat na $\mathcal{O}(N \log N)$ (Schubert et al. 2017).

### 3.6 Výhody, omezení a volba parametrů

**Výhody:**

- **shluky libovolného (nekonvexního) tvaru** — DBSCAN nepředpokládá sférické shluky, najde i protáhlé/zatočené **nelineární struktury** (na rozdíl od k-means). Protože pracuje pouze s **hustotou bodů** (počty v $\varepsilon$-okolí), spojí body i podél zakřivené nadplochy — typický „učebnicový" příklad je tzv. **švýcarská rolka** (angl. *Swiss roll*), tj. spirálovitě stočená 2D plocha v $\mathbb{R}^3$, kterou k-means rozseká, kdežto hustotní metoda ji vrátí jako jeden shluk;
- **detekce šumu** — snížená citlivost na odlehlé hodnoty, ty jsou označeny jako šum;
- **nevyžaduje zadat počet shluků** $k$ dopředu — počet shluků vyplyne z dat.

**Omezení (volba parametrů):**

- **MinPts** je mnohem méně důležitý než $\varepsilon$. Obvykle dobrá volba je $4$–$6$ (někdy se doporučuje $2\dots p$, kde $p$ je počet příznaků).
- **$\varepsilon$** se doporučuje volit co nejmenší; lze např. brát průměrnou vzdálenost bodů k jejich $(2\cdot p - 1)$-tému nejbližšímu sousedovi.
- **Velikost šumu** by obvykle měla být mezi 1 % a 30 % dat. **Velikost největšího shluku** by neměla překročit 50 % datasetu — pak je vhodné zmenšit $\varepsilon$, případně použít pokročilejší algoritmus (HDBSCAN).
- DBSCAN má potíže s daty, kde se výrazně **liší hustota** mezi shluky (jediné $\varepsilon$ pak nestačí).

### 3.7 Silhouette skóre (evaluace shlukování)

Pro evaluaci shlukování (a hledání optimálního počtu shluků) slouží **Silhouette skóre** (Rousseeuw, 1987). Uvažujme shlukování $\mathcal{D} = C_1 \cup \dots \cup C_k$ a pro bod $x \in \mathcal{D}$ označme $j(x)$ index jeho shluku.

- **Vnitřní rozdílnost** $a(x)$ — průměrná vzdálenost $x$ od ostatních bodů ve stejném shluku:
$$a(x) = \frac{1}{|C_{j(x)}| - 1} \sum_{y \in C_{j(x)},\, y \ne x} d(x,y).$$
- **Sousední rozdílnost** $b(x)$ — minimum z průměrných vzdáleností $x$ od bodů ostatních shluků:
$$b(x) = \min_{i \ne j(x)} d(x, C_i), \qquad d(x, C_i) = \frac{1}{|C_i|}\sum_{y \in C_i} d(x,y).$$
- **Silhouette skóre bodu:**
$$s(x) = \frac{b(x) - a(x)}{\max\{a(x), b(x)\}} \in [-1, 1].$$
(Při jediném shluku klademe $s(x) = 0$.) Hodnota blízká $1$: $x$ je dobře zatříděn ($a \ll b$); kolem $0$: $x$ je na hranici dvou shluků; blízko $-1$: $x$ je špatně přiřazen (patřil by spíše do sousedního shluku).

Průměr přes celé shlukování $s = \frac{1}{|\mathcal{D}|}\sum_{x \in \mathcal{D}} s(x)$ udává kvalitu — čím vyšší, tím lepší. Porovnáním $s$ pro různé počty shluků lze nalézt **vhodný počet shluků** jako ten, pro který je $s$ maximální.

---

## Co je potřeba na zkoušku znát

### Definice
- **Nesupervizované učení:** učení bez učitele z neoznačených dat; cíl = porozumět vnitřní struktuře (rozdělení $X$), tj. odhad hustoty $f_X$, shlukování, redukce dimenzionality.
- **Metrika** $d$: nezápornost + identita, symetrie, trojúhelníková nerovnost; $(\mathcal{X},d)$ metrický prostor.
- **Shluk (rozklad):** $C = (C_1,\dots,C_k)$, $C_i$ disjunktní, $\bigcup C_i = \mathcal{D}$.
- **Účelová funkce k-means (WCSS):** $G(C) = \sum_i \frac{1}{2|C_i|}\sum_{x,y \in C_i}\|x-y\|^2 = \sum_i \sum_{x \in C_i}\|x - \bar{x}_i\|^2$.
- **DBSCAN:** $\varepsilon$-okolí $N_\varepsilon(x) = \{y \mid d(x,y) \le \varepsilon\}$; **klíčový bod** $|N_\varepsilon(x)| \ge \text{MinPts}$; **okrajový bod** (neklíčový, přímo dosažitelný z klíčového); **šum** (nikam nepatří).
- **Přímá dosažitelnost** ($x$ klíčový, $y \in N_\varepsilon(x)$); **dosažitelnost** (řetězec přímých dosažitelností, všechny kromě posledního klíčové); **spojenost** ($\exists p$: $x,y$ dosažitelné z $p$).
- **Shluk DBSCAN:** maximální množina vzájemně spojených bodů (maximalita + souvislost), obsahuje $\ge \text{MinPts}$ bodů.
- **Silhouette:** $s(x) = \frac{b(x)-a(x)}{\max\{a(x),b(x)\}} \in [-1,1]$.

### Věty
- **Tvrzení o centroidu:** $\frac{1}{2|A|}\sum_{x,y}\|x-y\|^2 = \sum_x \|x-\bar{x}\|^2 = \min_\mu \sum_x \|x-\mu\|^2$ (minimum v geometrickém středu) → přepis WCSS přes centroidy.
- **Konvergence k-means:** v každé iteraci $G$ neroste (krok přiřazení i přepočtu), konverguje k lokálnímu minimu; globální minimum je NP-těžké.
- Relace u DBSCAN: přímá dosažitelnost symetrická jen pro dvojice klíčových bodů; spojenost symetrická, pro klíčové body tranzitivní.

### Algoritmy
- **k-means (Lloyd):** inicializace $k$ centroidů → přiřazení bodů nejbližšímu centroidu → přepočet centroidů → opakuj do konvergence. Lokální minimum, citlivost na inicializaci (k-means++), volba $k$ (loket/silhouette). Iterace $\mathcal{O}(Nkp)$. Sférické shluky, nutno zadat $k$.
- **DBSCAN:** najdi klíčové body → spoj přímo dosažitelné klíčové do zárodků → zařaď okrajové k sousednímu klíčovému, ostatní = šum. $\mathcal{O}(N^2)$ (až $\mathcal{O}(N\log N)$ s indexem). Libovolný tvar shluků, detekce šumu, nezadává se $k$; citlivý na $\varepsilon$.

### Typické doplňující otázky (doptávání)
- **Friedjungová (2025):** „Jak se volí $k$ u k-means?" (metoda lokte / elbow nad WCSS; nebo silhouette; nebo $k$ dáno typem úlohy / předem známé) → §2.5
- **Friedjungová (2025):** „Co k-means optimalizuje?" (účelovou funkci = vnitroshlukový součet kvadrátů vzdáleností od centroidů, WCSS; iterativně, $G$ neroste → konverguje k lokálnímu minimu; zastavení, když se $G$ téměř nemění) → §2.2, §2.3
- **Friedjungová (2025):** „Jaký je rozdíl mezi supervizovaným, nesupervizovaným a posíleným učením?" (označená data / bez označení / interakce s prostředím + odměna) → §1.1
- **Friedjungová (2025):** „Na čem pracuje DBSCAN a jaké struktury odhalí?" (na hustotě bodů; odhalí nelineární / nekonvexní struktury — „švýcarská rolka") → §3.1, §3.6
- **Friedjungová (2025):** „Vyjmenujte pojmy DBSCAN." (klíčový/core bod, $\varepsilon$-okolí, šum, dosažitelný, spojený) → §3.2, §3.3
- **Friedjungová (2025):** „Proč je těžké nastavit parametry DBSCAN?" ($\varepsilon$ a MinPts se ladí těžko, zvláště při různé hustotě shluků — jediné $\varepsilon$ nestačí) → §3.6
