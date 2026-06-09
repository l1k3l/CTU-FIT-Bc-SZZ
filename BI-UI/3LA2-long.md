---
studyplan: true
etapa: "3 · LA1 / MA2 / LA2 — Petr"
qid: "3LA2"
examiner: "Petr"
topic: "Ortogonalita a ortogonální báze"
readiness: nezačato
tags: [otázka, kurz/LA2, otázka/3, todo]
---

# Ortogonalita a ortogonální báze

> **Otázka SZZ:** Ortogonalita a ortogonální báze: definice, vlastnosti, využití při počítání vzdáleností lineárních variet.

Zdroje: BI-LA2 (FIT ČVUT), kap. 5 (Skalární součin), sekce 5.6 (Ortogonalita), 5.7 (Vlastnosti OG/ON báze), 5.8 (Ortogonalizace); pro připomenutí 5.1–5.4 (skalární součin a norma); kap. 6 (Geometrie $\mathbb{R}^n$), sekce 6.2 (Vzdálenost), 6.3 (Vzdálenost bodu od podprostoru), 6.4 (vzdálenost pomocí OG báze), 6.5 (pomocí báze $P^\perp$), 6.6 (od nadroviny), 6.7 (Vzdálenost variet). Tištěné strany 102–110 a 114–124.

Značení: $\mathcal{H} = (V, \langle \cdot \mid \cdot \rangle)$ je **prehilbertův prostor** (vektorový prostor se skalárním součinem nad $T = \mathbb{R}$ nebo $\mathbb{C}$), $\langle x \mid y \rangle$ je skalární součin, $\|x\| = \sqrt{\langle x \mid x \rangle}$ je norma indukovaná skalárním součinem, $\theta$ nulový vektor, $\hat{n} = \{1, \dots, n\}$. Vektory píšeme tučně/italikou.

Připomenutí: **[[Skalární-součin]]** je zobrazení $\langle \cdot \mid \cdot \rangle : V \times V \to T$, lineární v druhém argumentu, s hermitovskou symetrií $\langle x \mid y \rangle = \overline{\langle y \mid x \rangle}$ a pozitivně definitní ($\langle x \mid x \rangle \ge 0$, rovnost $\iff x = \theta$). **[[Norma]]** indukovaná skalárním součinem je $\|x\| := \sqrt{\langle x \mid x \rangle}$.

---

## 1. Ortogonalita

Pojem ortogonality (kolmosti) zobecňuje klasickou geometrickou kolmost z $\mathbb{R}^2$ (vektory $x, y$ jsou kolmé $\iff x \cdot y = 0$) na libovolný prostor se skalárním součinem.

### 1.1 Ortogonální vektory

**Definice (ortogonalita / kolmost).** Nechť $\mathcal{H}$ je prostor se skalárním součinem a $x, y \in \mathcal{H}$. Vektor $x$ nazýváme **ortogonální na** (též **kolmý na**) vektor $y$, právě když
$$\langle x \mid y \rangle = 0.$$
Pro kolmé vektory píšeme též $x \perp y$.

Díky hermitovské symetrii je $\langle x \mid y \rangle = 0 \iff \langle y \mid x \rangle = 0$, takže relace kolmosti je symetrická. Nulový vektor $\theta$ je kolmý na každý vektor, neboť $\langle \theta \mid y \rangle = 0$.

### 1.2 Ortogonální a ortonormální soubory

**Definice (ortogonální soubor, OG).** Soubor vektorů $(x_1, \dots, x_n)$ z $\mathcal{H}$ nazveme **ortogonální (OG)**, právě když je každý vektor souboru kolmý na všechny ostatní, tj. pro každé $i, j \in \hat{n}$, $i \neq j$, platí
$$\langle x_i \mid x_j \rangle = 0.$$

**Definice (ortonormální soubor, ON).** Soubor $(x_1, \dots, x_n)$ z $\mathcal{H}$ nazveme **ortonormální (ON)**, právě když je ortogonální a každý vektor má velikost 1. Neboli pro každé $i, j \in \hat{n}$ platí
$$\langle x_i \mid x_j \rangle = \delta_{ij} = \begin{cases} 0 & \text{pro } i \neq j, \\ 1 & \text{pro } i = j. \end{cases}$$
(Podmínka $\langle x_i \mid x_i \rangle = 1$ je ekvivalentní $\|x_i\| = 1$.) ON soubor je tedy OG soubor jednotkových vektorů.

### 1.3 Ortogonální doplněk

**Definice (ortogonální doplněk).** Nechť $W \subseteq \mathcal{H}$. **Ortogonálním doplňkem** $W$ rozumíme množinu všech vektorů kolmých na celé $W$:
$$W^\perp := \{\, x \in \mathcal{H} \mid \langle x \mid w \rangle = 0 \text{ pro všechna } w \in W \,\}.$$
$W^\perp$ je vždy podprostor $\mathcal{H}$ (kolmost na pevné $w$ je zachována při sčítání a násobení skalárem). Pro konečnědimenzionální podprostor $W$ platí $\mathcal{H} = W \oplus W^\perp$, tedy $\dim W + \dim W^\perp = \dim \mathcal{H}$, a $(W^\perp)^\perp = W$.

> *Pozn.:* Skripta BI-LA2 ortogonální doplněk v sekci 5.6 explicitně nedefinují; výše uvedené je standardní formulace.

---

## 2. Ortogonální a ortonormální báze

OG/ON soubor (nenulových vektorů) je vždy lineárně nezávislý (Věta v sekci 3.1), je tedy bází podprostoru, který generuje.

**Definice (ortogonální báze, OG báze).** **[[Ortogonální-báze|Ortogonální báze]]** podprostoru $P \subseteq \mathcal{H}$ je báze $P$, která je zároveň ortogonálním souborem (vzájemně kolmé nenulové vektory).

**Definice (ortonormální báze, ON báze).** **Ortonormální báze** podprostoru $P$ je báze $P$, která je zároveň ortonormálním souborem (vzájemně kolmé jednotkové vektory).

Standardní báze $(e_1, \dots, e_n)$ prostoru $T^n$ se standardním skalárním součinem je příkladem ON báze.

---

## 3. Vlastnosti OG/ON báze

### 3.1 Lineární nezávislost OG souboru

Vlastnost být ortogonální je „silnější" než být lineárně nezávislý:

**Věta (o lineární nezávislosti OG souboru).** Ortogonální soubor **nenulových** vektorů je lineárně nezávislý. Speciálně každý ortonormální soubor vektorů je LN.

**Důkaz.** Buď $(x_1, \dots, x_n)$ OG soubor nenulových vektorů. Uvažujme lineární kombinaci dávající nulový vektor
$$\sum_{j=1}^n \alpha_j x_j = \theta.$$
Pro libovolné $i \in \hat{n}$ pak platí
$$0 = \langle x_i \mid \theta \rangle = \Big\langle x_i \,\Big|\, \sum_{j=1}^n \alpha_j x_j \Big\rangle = \sum_{j=1}^n \alpha_j \langle x_i \mid x_j \rangle = \alpha_i \|x_i\|^2,$$
kde poslední rovnost plyne z toho, že $\langle x_i \mid x_j \rangle = 0$ pro $i \neq j$. Podle předpokladu je $x_i \neq \theta$, tudíž $\|x_i\| \neq 0$, a proto nutně $\alpha_i = 0$ pro všechna $i \in \hat{n}$. Soubor je tedy LN. $\square$

(Předpoklad nenulovosti je nutný: $\theta$ je kolmý na vše, takže soubor obsahující $\theta$ je OG, ale není LN.)

### 3.2 Fourierovy koeficienty — souřadnice vůči ON/OG bázi

Hlavní výhoda ON báze: souřadnice vektoru se počítají pouhými skalárními součiny, není třeba řešit soustavu rovnic.

**Věta (Fourierovy koeficienty vůči ON bázi).** Nechť $\mathcal{X} = (x_1, \dots, x_n)$ je ON báze prehilbertova prostoru $\mathcal{H}$. Potom pro každé $z \in \mathcal{H}$ platí
$$z = \sum_{i=1}^n \langle x_i \mid z \rangle\, x_i, \qquad \text{neboli} \qquad (z)_\mathcal{X} = \big( \langle x_1 \mid z \rangle, \langle x_2 \mid z \rangle, \dots, \langle x_n \mid z \rangle \big).$$

**Důkaz.** Jelikož je $\mathcal{X}$ báze, lze každý $z \in \mathcal{H}$ psát jako $z = \sum_{j=1}^n \alpha_j x_j$. S využitím linearity skalárního součinu a ortonormality dostáváme pro každé $i \in \hat{n}$
$$\langle x_i \mid z \rangle = \Big\langle x_i \,\Big|\, \sum_{j=1}^n \alpha_j x_j \Big\rangle = \sum_{j=1}^n \alpha_j \langle x_i \mid x_j \rangle = \alpha_i,$$
neboť $\langle x_i \mid x_j \rangle = 0$ pro $i \neq j$ a $\langle x_i \mid x_i \rangle = 1$. Souřadnice jsou tedy přímo $\alpha_i = \langle x_i \mid z \rangle$. $\square$

**Poznámka (OG báze).** Pro pouze ortogonální (nenormovanou) bázi se vzorec lehce zesložití — ve jmenovateli zůstane skalární součin bázového vektoru sám se sebou, tj. $\|x_i\|^2$:
$$\alpha_i = \frac{\langle x_i \mid z \rangle}{\langle x_i \mid x_i \rangle} = \frac{\langle x_i \mid z \rangle}{\|x_i\|^2}, \qquad z = \sum_{i=1}^n \frac{\langle x_i \mid z \rangle}{\langle x_i \mid x_i \rangle}\, x_i.$$
Čísla $\dfrac{\langle x_i \mid z \rangle}{\langle x_i \mid x_i \rangle}$ se nazývají **Fourierovy koeficienty**; jsou to souřadnice $z$ vzhledem k OG bázi.

**Geometrický význam — ortogonální projekce na přímku.** Pro $v \neq \theta$ je zobrazení
$$\operatorname{proj}_v(z) := \frac{\langle v \mid z \rangle}{\langle v \mid v \rangle}\, v$$
**ortogonální projekce** $z$ na přímku $\langle v \rangle$. Rozklad vektoru do ON/OG báze lze tedy psát jako součet projekcí do jednotlivých směrů:
$$z = \sum_{i=1}^n \operatorname{proj}_{x_i}(z).$$

### 3.3 Pythagorova věta

**Věta (Pythagorova věta).** Nechť $x, y \in \mathcal{H}$ a $x$ je kolmý na $y$. Potom pro normu indukovanou skalárním součinem platí
$$\|x + y\|^2 = \|x\|^2 + \|y\|^2.$$
Obecněji: je-li $(x_1, \dots, x_n)$ ortogonální soubor, pak
$$\|x_1 + \dots + x_n\|^2 = \|x_1\|^2 + \dots + \|x_n\|^2.$$

**Důkaz.** Přímo z definice normy indukované skalárním součinem:
$$\|x + y\|^2 = \langle x + y \mid x + y \rangle = \|x\|^2 + \langle x \mid y \rangle + \langle y \mid x \rangle + \|y\|^2.$$
Z předpokladu kolmosti je $\langle x \mid y \rangle = \langle y \mid x \rangle = 0$, takže $\|x+y\|^2 = \|x\|^2 + \|y\|^2$. Obecnou verzi pro $n$ vektorů dokážeme z této indukcí. $\square$

### 3.4 Parsevalova (Besselova) rovnost

Známe-li souřadnice vůči ON bázi, snadno spočteme normu vektoru.

**Věta (Parsevalova rovnost).** Nechť $\mathcal{X} = (x_1, \dots, x_n)$ je ON báze prehilbertova prostoru $\mathcal{H}$ a $z \in \mathcal{H}$. Potom platí
$$\|z\| = \big\| (z)_\mathcal{X} \big\|_2,$$
tj. norma vektoru se rovná eukleidovské 2-normě jeho souřadnicového vektoru.

**Důkaz.** Je-li $z = \alpha_1 x_1 + \dots + \alpha_n x_n$, tedy $(z)_\mathcal{X} = (\alpha_1, \dots, \alpha_n)$, pak pomocí Pythagorovy věty (vektory $\alpha_i x_i$ jsou navzájem kolmé) a homogenity normy:
$$\|z\|^2 = \|\alpha_1 x_1 + \dots + \alpha_n x_n\|^2 = \|\alpha_1 x_1\|^2 + \dots + \|\alpha_n x_n\|^2 = |\alpha_1|^2 \|x_1\|^2 + \dots + |\alpha_n|^2 \|x_n\|^2 = |\alpha_1|^2 + \dots + |\alpha_n|^2 = \big\|(z)_\mathcal{X}\big\|_2^2,$$
kde jsme využili $\|x_i\| = 1$. Odmocněním získáme tvrzení. $\square$

---

## 4. Ortogonalizace — Gram–Schmidtův algoritmus

Počítání souřadnic v ON bázi je mnohem jednodušší než v obecné bázi (stačí skalární součiny místo řešení soustavy). **[[Gram-Schmidtův-algoritmus|Gram–Schmidtův proces]]** umožňuje z libovolné báze vyrobit OG, resp. ON bázi téhož prostoru — díky čemuž má každý konečnědimenzionální (pod)prostor ON bázi.

### 4.1 Myšlenka (odvození vzorce)

Máme dva nenulové vektory $u, v$ a chceme nahradit $v$ vektorem $z = v - \alpha u$ tak, aby $z$ bylo kolmé na $u$, přičemž zůstane zachován lineární obal ($\langle u, v \rangle = \langle u, z \rangle$). Protože
$$\langle u \mid z \rangle = \langle u \mid v - \alpha u \rangle = \langle u \mid v \rangle - \alpha \langle u \mid u \rangle,$$
volbou
$$\alpha = \frac{\langle u \mid v \rangle}{\langle u \mid u \rangle}$$
dostaneme $\langle u \mid z \rangle = 0$. Vektor $\frac{\langle u \mid v \rangle}{\langle u \mid u \rangle} u = \operatorname{proj}_u(v)$ je „část" $v$ rovnoběžná s $u$; odečteme-li ji, zbude kolmá složka. Pro tři vektory $(u, v, w)$ s již ortogonálním $(u, v)$ odečteme od $w$ projekce do obou směrů: $z = w - \frac{\langle u \mid w \rangle}{\langle u \mid u \rangle} u - \frac{\langle v \mid w \rangle}{\langle v \mid v \rangle} v$.

### 4.2 Věta a algoritmus

**Věta (Gramova–Schmidtova ortogonalizace).** Nechť $\mathcal{X} = (x_1, \dots, x_n) \subseteq \mathcal{H}$ je LN soubor vektorů. Potom existuje ON soubor $\mathcal{Y} = (y_1, \dots, y_n)$ vektorů z $\mathcal{H}$ takový, že pro každé $k \in \hat{n}$ platí
$$\langle x_1, \dots, x_k \rangle = \langle y_1, \dots, y_k \rangle.$$

**Postup (Gram–Schmidt).** Z LN souboru $(x_1, \dots, x_n)$ vyrobíme nejprve OG soubor $(z_1, \dots, z_n)$:
$$\begin{aligned}
z_1 &= x_1, \\
z_2 &= x_2 - \frac{\langle z_1 \mid x_2 \rangle}{\langle z_1 \mid z_1 \rangle} z_1, \\
z_3 &= x_3 - \frac{\langle z_1 \mid x_3 \rangle}{\langle z_1 \mid z_1 \rangle} z_1 - \frac{\langle z_2 \mid x_3 \rangle}{\langle z_2 \mid z_2 \rangle} z_2, \\
&\ \vdots \\
z_k &= x_k - \sum_{i=1}^{k-1} \frac{\langle z_i \mid x_k \rangle}{\langle z_i \mid z_i \rangle} z_i.
\end{aligned}$$
Kompaktně pomocí projekcí: $z_k = x_k - \sum_{i=1}^{k-1} \operatorname{proj}_{z_i}(x_k)$. **Normalizací** pak získáme ON soubor:
$$y_i = \frac{1}{\|z_i\|}\, z_i.$$

**Důkaz (idea, indukcí přes $k$).** Ukážeme, že $(z_1, \dots, z_k)$ je OG soubor nenulových vektorů s $\langle x_1, \dots, x_k \rangle = \langle z_1, \dots, z_k \rangle$.

- *Báze $k = 1$:* $z_1 = x_1 \neq \theta$ a $\langle z_1 \rangle = \langle x_1 \rangle$.
- *Krok $k-1 \Rightarrow k$:* $z_k \neq \theta$ — kdyby $z_k = \theta$, plynulo by ze vzorce $x_k \in \langle z_1, \dots, z_{k-1} \rangle = \langle x_1, \dots, x_{k-1} \rangle$, spor s LN souboru $\mathcal{X}$. Ortogonalita: pro $i \in \widehat{k-1}$ je (s využitím indukčního předpokladu $\langle z_i \mid z_j \rangle = 0$ pro $i \neq j$)
$$\langle z_i \mid z_k \rangle = \langle z_i \mid x_k \rangle - \frac{\langle z_i \mid x_k \rangle}{\langle z_i \mid z_i \rangle} \langle z_i \mid z_i \rangle = 0.$$
Rovnost obalů: $z_k \in \langle x_1, \dots, x_k \rangle$ a naopak $x_k = z_k + \sum_{i<k} (\dots) z_i \in \langle z_1, \dots, z_k \rangle$, takže $\langle z_1, \dots, z_k \rangle = \langle x_1, \dots, x_k \rangle$ (oba mají dimenzi $k$, neboť OG soubor nenulových vektorů je LN).

Přeškálování $y_i = \frac{1}{\|z_i\|} z_i$ dá vektory s normou 1 a neovlivní ortogonalitu ani lineární obaly. $\square$

### 4.3 Příklad

V $\mathbb{R}^4$ se standardním skalárním součinem najdeme ON bázi podprostoru $P = \langle x_1, x_2, x_3 \rangle$ pro $x_1 = (1,2,2,-1)$, $x_2 = (1,1,-5,3)$, $x_3 = (3,2,8,-7)$:
$$\begin{aligned}
z_1 &= (1,2,2,-1), \\
z_2 &= x_2 - \frac{\langle z_1 \mid x_2 \rangle}{\langle z_1 \mid z_1 \rangle} z_1 = (1,1,-5,3) - \frac{-10}{10}(1,2,2,-1) = (2,3,-3,2), \\
z_3 &= x_3 - \frac{\langle z_1 \mid x_3 \rangle}{\langle z_1 \mid z_1 \rangle} z_1 - \frac{\langle z_2 \mid x_3 \rangle}{\langle z_2 \mid z_2 \rangle} z_2 = (3,2,8,-7) - \frac{30}{10}(1,2,2,-1) - \frac{-26}{26}(2,3,-3,2) = (2,-1,-1,-2).
\end{aligned}$$
Normalizací: $y_1 = \frac{1}{\sqrt{10}}(1,2,2,-1)$, $y_2 = \frac{1}{\sqrt{26}}(2,3,-3,2)$, $y_3 = \frac{1}{\sqrt{10}}(2,-1,-1,-2)$. Soubor $(y_1, y_2, y_3)$ je ON báze $P$.

---

## 5. Využití ortogonality při počítání vzdáleností lineárních variet

Toto je hlavní aplikace ortogonální projekce, kterou exam-otázka explicitně zmiňuje. Postup je vždy převedení obecné úlohy na úlohu, kterou už umíme: **vzdálenost vektoru od podprostoru** = délka ortogonální projekce do ortogonálního doplňku.

Pracujeme v $\mathbb{R}^n$ se standardním skalárním součinem (norma = eukleidovská).

### 5.1 Vzdálenost množin

**Definice (vzdálenost množin).** Pro dvě množiny $M, N \subseteq \mathbb{R}^n$ definujeme
$$d(M, N) := \inf\{\, \|x - y\| \mid x \in M, \ y \in N \,\}.$$
(Pro jednoprvkovou množinu $M = \{v\}$ píšeme zkráceně $d(v, N)$.) V lineární algebře bychom vystačili s minimem, ale infimum je obecně bezpečnější.

### 5.2 Vzdálenost bodu od podprostoru — klíčová věta

**Tvrzení (o vlivu posunutí).** Posunutí o pevný vektor $v$ vzdálenost nemění:
$$d(M, N) = d(v + M, v + N).$$
Speciálně pro varietu $a + P$ a vektor $z$ platí $d(z, a + P) = d(z - a, P)$. **Důsledek:** úlohu „vzdálenost bodu od variety" převedeme posunutím o $-a$ na úlohu „vzdálenost bodu od podprostoru".

**Věta (o vzdálenosti a kolmici).** Buď $x \in \mathbb{R}^n$ a $P$ podprostor. Existují-li $v \in P$ a $w \in P^\perp$ s rozkladem $x = v + w$, potom
$$d(x, P) = \|w\|.$$

**Důkaz.** $\|x - v\| = \|w\|$, takže $\|w\|$ je v množině $\{\|x-y\| \mid y \in P\}$. Pro libovolné $y \in P$ je $x - y = (x-v) - (y-v) = w + (v - y)$, kde $w \in P^\perp$ a $v - y \in P$ jsou kolmé, takže podle Pythagorovy věty
$$\|x - y\|^2 = \|w\|^2 + \|v - y\|^2 \ge \|w\|^2.$$
Minima je dosaženo pro $y = v$. $\square$

Rozklad $x = v + w$ s $v \in P$, $w \in P^\perp$ existuje a je jednoznačný, neboť $\mathbb{R}^n = P \oplus P^\perp$ (viz §1.3). Vektor $v$ je **ortogonální projekce** $x$ na $P$, vektor $w = x - v$ se nazývá **ortogonální rejekce**.

### 5.3 Výpočet 1 — pomocí OG/ON báze podprostoru

**Definice (ortogonální projekce na podprostor).** Je-li $(y_1, \dots, y_k)$ **OG** báze podprostoru $P$, pak
$$\operatorname{proj}_P(z) := \operatorname{proj}_{y_1}(z) + \dots + \operatorname{proj}_{y_k}(z) = \sum_{i=1}^k \frac{\langle y_i \mid z \rangle}{\langle y_i \mid y_i \rangle} y_i.$$
(Ortogonalita báze je zde **klíčová** — pro neortogonální soubor součet projekcí na jednotlivé směry nedává projekci na podprostor.) Pak $v = \operatorname{proj}_P(z) \in P$, $w = z - \operatorname{proj}_P(z) \in P^\perp$ a vzdálenost je $d(z, P) = \|z - \operatorname{proj}_P(z)\|$.

Postup: nemáme-li OG bázi $P$, vyrobíme ji Gram–Schmidtem (§4) — proto se vše opírá o ortogonalizaci.

**Maticový zápis (ON báze).** Je-li $(y_1, \dots, y_k)$ **ON** báze $P$ a $B = (y_1 \mid \dots \mid y_k)$ matice s těmito vektory ve sloupcích, pak
$$\operatorname{proj}_P(z) = B B^T z.$$

### 5.4 Výpočet 2 — pomocí báze ortogonálního doplňku $P^\perp$

Hledání OG báze je pracné (počet operací roste kvadraticky s $\dim P$). Pro podprostory větší dimenze je výhodnější najít bázi $P^\perp$.

**Pozorování.** Je-li $(y_1, \dots, y_k)$ báze $P$, pak $x \in P^\perp \iff x$ je kolmé na všechny $y_i$. Hledání báze $P^\perp$ je tedy **řešení homogenní soustavy** $\sum$ s maticí, jejíž řádky jsou $y_i^T$:
$$\begin{pmatrix} y_1^T \\ \vdots \\ y_k^T \end{pmatrix} x = 0.$$

**Důsledek (dimenze).** $\dim P^\perp = n - \dim P$.

Máme-li bázi $(z_1, \dots, z_\ell)$ doplňku $P^\perp$ (s $\ell = n - k$), spojený soubor $(y_1, \dots, y_k, z_1, \dots, z_\ell)$ je bází $\mathbb{R}^n$. Souřadnice vektoru $z$ v této bázi dají přímo rozklad $z = \underbrace{\sum \alpha_i y_i}_{v \in P} + \underbrace{\sum \beta_j z_j}_{w \in P^\perp}$ a vzdálenost je $\|w\|$ (koeficienty $\alpha_i$ nás přitom ani nezajímají).

### 5.5 Vzdálenost od nadroviny — normálový vektor

**Nadrovina** je varieta dimenze $n-1$, popsatelná jednou neparametrickou rovnicí $a_1 x_1 + \dots + a_n x_n = b$. Vektor $n_W := a = (a_1, \dots, a_n)$ je **normálový vektor** — tvoří bázi $P^\perp$ zaměření $P$ (tj. $P^\perp = \langle n_W \rangle$), je určen jednoznačně až na nenulový násobek.

Pro podprostor $P$ dimenze $n-1$ s normálou $n_P$ se vzdálenost počítá jedním zlomkem:
$$d(x, P) = \|\operatorname{proj}_{n_P}(x)\| = \frac{|\langle n_P \mid x \rangle|}{\|n_P\|}.$$
(Obecnou nadrovinu, která není podprostorem, nejdřív posuneme dle Tvrzení o posunutí.)

### 5.6 Vzdálenost dvou variet — redukce na bod a podprostor

**Věta (o vzdálenosti variet).** Pro variety $M = a + \langle x_1, \dots, x_k \rangle$ a $N = b + \langle y_1, \dots, y_\ell \rangle$ platí
$$d(M, N) = d\big(\, a - b,\ \langle x_1, \dots, x_k, y_1, \dots, y_\ell \rangle \,\big).$$

**Důkaz.** $d(M,N) = \inf\{\|a + u - (b + v)\| \mid u \in \langle x_i \rangle, v \in \langle y_j \rangle\}$. Úpravou $\|(a-b) - (v - u)\|$ a položením $w = v - u \in \langle x_1,\dots,x_k,y_1,\dots,y_\ell\rangle$ dostaneme $\inf\{\|(a-b) - w\|\} = d(a-b, \langle x_1,\dots,x_k,y_1,\dots,y_\ell\rangle)$. $\square$

**Geometrie:** vzdálenost dvou přímek v $\mathbb{R}^3$ tak spočteme jako vzdálenost vektoru $a-b$ od roviny generované oběma směry (viz vzdálenost bodu od nadroviny). Vzdálenost dvou variet se tedy vždy redukuje na §5.2.

### 5.7 Vzájemné polohy a úhel (doplnění)

**Polohy variet** $W, U$ se zaměřeními $Z(W), Z(U)$: **rovnoběžné** ($Z(W) \subseteq Z(U)$ nebo naopak), **různoběžné** (nerovnoběžné a $W \cap U \neq \emptyset$), **mimoběžné** (nerovnoběžné a $W \cap U = \emptyset$).

**Úhel dvou vektorů:** $\arccos \dfrac{\langle x \mid y \rangle}{\|x\|\,\|y\|}$ — korektní díky Schwarzově nerovnosti $-1 \le \frac{\langle x \mid y \rangle}{\|x\|\|y\|} \le 1$; výsledek je z $\langle 0, \pi \rangle$. Pro přímky/nadroviny se počítá z $|\langle u \mid v\rangle|$ (resp. normálových vektorů), výsledek je z $\langle 0, \pi/2 \rangle$.

---

## Co je potřeba na zkoušku znát

### Definice
- **Ortogonalita:** $x \perp y \iff \langle x \mid y \rangle = 0$.
- **OG soubor:** vzájemně kolmé vektory ($\langle x_i \mid x_j \rangle = 0$ pro $i \neq j$). **ON soubor:** navíc $\|x_i\| = 1$, tj. $\langle x_i \mid x_j \rangle = \delta_{ij}$.
- **OG / ON báze:** báze, která je OG / ON souborem.
- **Ortogonální doplněk** $W^\perp = \{x \mid \langle x \mid w \rangle = 0\ \forall w \in W\}$.

### Klíčové věty
- **Lineární nezávislost:** OG soubor **nenulových** vektorů je LN (důkaz: $0 = \langle x_i \mid \sum \alpha_j x_j \rangle = \alpha_i \|x_i\|^2$).
- **Fourierovy koeficienty:** vůči ON bázi $z = \sum_i \langle x_i \mid z \rangle x_i$; vůči OG bázi $\alpha_i = \frac{\langle x_i \mid z \rangle}{\langle x_i \mid x_i \rangle}$.
- **Pythagorova věta:** $x \perp y \Rightarrow \|x+y\|^2 = \|x\|^2 + \|y\|^2$.
- **Parsevalova rovnost:** vůči ON bázi $\|z\| = \|(z)_\mathcal{X}\|_2$.

### Algoritmus
- **Gram–Schmidt:** $z_k = x_k - \sum_{i<k} \frac{\langle z_i \mid x_k \rangle}{\langle z_i \mid z_i \rangle} z_i$ (odečtení projekcí do již vytvořených směrů) → OG báze; normalizace $y_i = \frac{1}{\|z_i\|} z_i$ → ON báze. Zachovává lineární obaly $\langle x_1,\dots,x_k\rangle = \langle z_1,\dots,z_k\rangle$. Důsledek: každý konečnědimenzionální prostor má ON bázi.

### Vzdálenosti variet (aplikace ortogonality — chce ji Dombek!)
- **Vzdálenost bodu od podprostoru:** $x = v + w$, $v \in P$, $w \in P^\perp$ ⟹ $d(x, P) = \|w\|$ (délka kolmice = norma projekce do $P^\perp$).
- **Projekce na $P$ (z OG báze):** $\operatorname{proj}_P(z) = \sum_i \frac{\langle y_i \mid z\rangle}{\langle y_i \mid y_i\rangle} y_i$; ON báze maticově $\operatorname{proj}_P(z) = BB^T z$. **Ortogonalita báze je nutná.**
- **Přes $P^\perp$:** bázi $P^\perp$ najdu jako řešení homogenní soustavy s řádky $y_i^T$; $\dim P^\perp = n - \dim P$.
- **Posunutí nemění vzdálenost:** $d(z, a+P) = d(z-a, P)$ — tak se bod-od-variety převede na bod-od-podprostoru.
- **Nadrovina:** normálový vektor $n_W$ (báze $P^\perp$), $d(x, P) = \frac{|\langle n_P \mid x\rangle|}{\|n_P\|}$.
- **Vzdálenost dvou variet** $M = a + \langle x_i\rangle$, $N = b + \langle y_j\rangle$: $d(M,N) = d(a-b, \langle x_1,\dots,x_k, y_1,\dots,y_\ell\rangle)$ — redukce na bod–podprostor.

### Typické doplňující otázky (doptávání)
- **Dombek:** "Jak definuješ vzdálenost dvou množin / dvou variet?" → §5.1, §5.6 (řada studentů se na definici vzdálenosti množin zasekla).
- **Dombek:** chce i **definici skalárního součinu** (i když není v zadání) a **souřadnice vůči ON/OG bázi přes skalární součin** (Fourierovy koeficienty) → připomenutí nahoře + §3.2.
- **Dombek:** "Co je ortogonální matice, uveď dvě vlastnosti?" (stačí: zachovává ortogonalitu a normu) → viz [[5LA2-long#QR rozklad|ortogonální matice]].
- **Dombek / Knop:** "Jak se hledá ortogonální báze / proč ortogonalizaci děláme?" a **rozdíl OG vs ON souboru** → §1.2, §4.
- **Obecně Dombek:** chce ověřit, že student **chápe princip**, ne jen papouškuje definice — u každé definice umět říct, co znamená a k čemu je.
