---
studyplan: true
etapa: 1 · SAP — Daňhel
qid: 28SAP
examiner: Daňhel
topic: Kombinační a sekvenční obvody (Mealy/Moore), hradla, minimalizace mapami
readiness: in progress
tags:
  - otázka
  - kurz/SAP
  - otázka/28
  - hotovo
---

# Kombinační a sekvenční logické obvody, minimalizace map

> **Otázka SZZ:** Kombinační a sekvenční logické obvody (Mealy, Moore), popis a možnosti implementace na úrovni hradel. Minimalizace vyjádření logické funkce s využitím map.

Zdroje: BI-SAP, `kombinacni_obvody.pdf`, `sekvencni_obvody.pdf`, `sap-6-typical.pdf` (H. Kubátová, KČN FIT ČVUT).

---

## 1. Kombinační logické obvody

### 1.1 Definice
**[[Kombinační-obvod|Kombinační logický obvod]]** je obvod, ve kterém je každý výstup $out_i$ určen **pouze okamžitou kombinací** hodnot vstupů $in_1,\dots,in_p$ — nezávisí na historii. Obvod **nemá paměť**. (Kontrast se sekvenčním obvodem, jehož výstup závisí i na *posloupnosti* vstupů, viz §4.)

Výstupy popisujeme logickými funkcemi $f:\{0,1\}^n\to\{0,1\}$ prostředky **[[Booleova-algebra|Booleovy algebry]]**.

### 1.2 Booleova algebra
**[[Booleova-algebra|Booleova algebra]]** je struktura $\langle B,+,\cdot,\neg,0,1\rangle$ s axiomy (pro všechna $a,b,c\in B$):

| | zákon | duální tvar | název |
|---|---|---|---|
| 1 | $a+b=b+a$ | $a\cdot b=b\cdot a$ | komutativita |
| 2 | $a+(b+c)=(a+b)+c$ | $a(bc)=(ab)c$ | asociativita |
| 3 | $a+bc=(a+b)(a+c)$ | $a(b+c)=ab+ac$ | distributivita |
| 4 | $a+0=a$ | $a\cdot 1=a$ | neutralita 0, 1 |
| 5 | $a+\overline a=1$ | $a\cdot\overline a=0$ | vlastnosti negace |

Zde $+$ = logický součet (OR), $\cdot$ = logický součin (AND, vynechává se), $\neg$ = negace; obě binární operace mají **stejnou prioritu**. Z axiomů se odvodí: idempotence ($a+a=a$), agresivita 0/1 ($a+1=1$, $a\cdot 0=0$), dvojí negace, **absorbce** $a+ab=a$, **absorbce negace** $a+\overline a b=a+b$, **de Morgan** $\overline{a+b}=\overline a\,\overline b$, **consensus** $ab+\overline a c+bc=ab+\overline a c$.

*Příklad důkazu (absorbce):* $a+ab\overset{(4)}{=}a\cdot1+ab\overset{(3)}{=}a(1+b)\overset{\text{agr.}}{=}a\cdot1\overset{(4)}{=}a.$

**Princip duality:** záměnou $+\leftrightarrow\cdot$ a $0\leftrightarrow1$ z platného tvrzení vznikne opět platné.

### 1.3 Logické funkce, literál, term
- **Proměnná** $x\in B$; **literál** = proměnná v přímém ($x$) nebo negovaném ($\overline x$) tvaru.
- **P-term (součinový)** = součin literálů ($a\overline b c$); **S-term (součtový)** = součet literálů ($\overline a+b$).
- **Minterm** = P-term obsahující *všechny* nezávislé proměnné (je 1 pro jedinou kombinaci). **Maxterm** = S-term se všemi proměnnými (je 0 pro jedinou kombinaci).
- **Stavový index** $s$ = dekadická hodnota kombinace hodnot proměnných.
- Funkcí $n$ proměnných je $2^{2^n}$. Pro $n=2$ existuje 16 funkcí: kromě AND, OR, NOT mj. **XOR** ($a\oplus b=a\overline b+\overline a b$, nonekvivalence), **NAND** ($\overline{ab}$), **NOR** ($\overline{a+b}$), ekvivalence, implikace.

### 1.4 Kanonické tvary
Každou funkci lze zapsat jako:
- **ÚNDF** (úplná normální disjunktivní forma) = **součet mintermů** (kanonický SOP),
- **ÚNKF** (úplná normální konjunktivní forma) = **součin maxtermů** (kanonický POS).

*Příklad* $f(a,b,c)$ s jedničkami v indexech 1, 2, 4, 6 (a = nejnižší řád):
$$f=\overline c\,\overline b a+\overline c b\overline a+c\overline b\,\overline a+cb\overline a \quad(\text{ÚNDF})$$
$$f=(c+b+a)(c+\overline b+\overline a)(\overline c+b+\overline a)(\overline c+\overline b+\overline a)\quad(\text{ÚNKF})$$
Zkrácený zápis: $f=\sum(1,2,4,6)=\prod(0,3,5,7)$ ($\sum$ = indexy, kde $f=1$; $\prod$ = kde $f=0$).

---

## 2. Minimalizace vyjádření logické funkce s využitím map

Cílem je najít **MNDF** (minimální normální disjunktní forma — minimální počet co nejkratších P-termů) resp. **MNKF**. Menší výraz = méně hradel = menší plocha a zpoždění.

### 2.1 Karnaughova mapa
**[[Karnaughova-mapa|Karnaughova mapa]]** je obdélník o $2^n$ polích, do nichž zapisujeme hodnoty funkce. Pole jsou uspořádána **Grayovým kódem** tak, že **sousední pole se liší v hodnotě právě jedné proměnné** (sousední stavy). Sousednost je **cyklická** — krajní sloupce i řádky spolu sousedí.

Příklad rozložení 4 proměnných (řádky $dc$, sloupce $ba$ v Grayově pořadí 00, 01, 11, 10):

```
          ba=00  01  11  10
   dc=00 |  0    1    3    2 |
      01 |  4    5    7    6 |
      11 | 12   13   15   14 |
      10 |  8    9   11   10 |
```

(Existuje i **Svobodova mapa** s lineárně řazenými indexy; pro minimalizaci se používá Karnaughova.)

### 2.2 Implikanty
- **Implikant** = krychle (P-term) ležící celá v onsetu (množině jedniček) funkce.
- **Prvoimplikant (přímá krychle)** = implikant, který už nelze zvětšit (žádný literál nelze odebrat).
- **Podstatný (esenciální) implikant** = prvoimplikant pokrývající jedničku, kterou nepokrývá žádný jiný prvoimplikant.

### 2.3 Algoritmus minimalizace (SOP)
1. Najdi **maximální skupiny (smyčky)** sousedních jedniček o velikosti mocniny 2 → všechny **prvoimplikanty**.
2. Vyber všechny **podstatné** implikanty.
3. Zbývající jedničky pokryj dalšími prvoimplikanty (co nejmenším počtem).

Skupinu popisují jen ty proměnné, které se v ní **nemění**.

*Příklad:* $f(a,b,c,d)=\sum(1,4,5,6,9,10,12,13,14)\Rightarrow f=a\overline b+\overline a c+\overline a bd$ (jedna ze čtveřic je redundantní).

### 2.4 Neurčené stavy (*don't care*)
Kombinace, které nemohou nastat, značíme **×** a smíme je libovolně využít (0/1) k zvětšení skupin. Zápis $\sum_{(1)}(\dots)+\sum_{(\times)}(\dots)$. *Příklad:* $\sum_{(1)}(0,1,2,3,4,5,11)+\sum_{(\times)}(7,10,14)=\overline b\,\overline d+b\overline c$.

### 2.5 Algebraická minimalizace
Postupné aplikování zákonů (zejména **absorbce**, **absorbce negace**, **consensus**). Užitečná je **Shannonova expanze** $F=a\,F(1,\dots)+\overline a\,F(0,\dots)$.

### 2.6 Quine–McCluskeyho metoda
Pro mnoho proměnných (mapa nepřehledná). Tabulkově: minterm­y se zapíší binárně, sdružují se po dvojicích lišících se v 1 bitu (→ čtveřice…) → neslučitelné = **prvoimplikanty**; pak **tabulka pokrytí** určí podstatné implikanty a doplní zbytek. Programovatelné; pro velmi mnoho proměnných **heuristiky**.

---

## 3. Možnosti implementace na úrovni hradel

### 3.1 Hradla a úplný systém
Základní hradla: **AND, OR, NOT, NAND, NOR, XOR** (značky ANSI i IEC, kde XOR = `=1`, NAND = AND s kroužkem, NOR = OR s kroužkem na výstupu). **Úplný systém** funkcí je $\{+,\cdot,\neg\}$; úplný je i **samotný NAND**, resp. **samotný NOR** — proto se v ASIC realizuje právě jimi (nejméně tranzistorů, nejmenší plocha).

> **Proč se XOR používá tak často?** XOR ($a\oplus b$) je **detektor nerovnosti / parity** — výstup 1 právě když je počet jedniček lichý. Proto je jádrem (1) **sčítačky** (součtový bit $s=a\oplus b\oplus p$, §3.3), (2) **řízeného invertoru** ve sčítačce/odčítačce (XOR operandu s řídicím signálem *Odčítej*), (3) **komparátoru** (rovnost = NOR všech XORů po bitech), (4) **generátoru a kontroly parity** a obecně **detekce/oprava chyb**. Bez XOR by tyto obvody potřebovaly více hradel.

### 3.2 Dvojúrovňová realizace
- **AND-OR** přímo z MNDF (1. úroveň AND vytvoří P-termy, 2. úroveň OR je sečte).
- **NAND-NAND** — funkci v MNDF dvojitě znegujeme a podle de Morgana převedeme na samé NAND:
$$f=a+\overline b\,\overline c+c\overline d=\overline{\;\overline a\cdot\overline{\overline b\,\overline c}\cdot\overline{c\overline d}\;}$$
Pravidlo: pro $+$ i $\cdot$ použijeme NAND; proměnné vstupující přímo do hradla na **liché úrovni od konce** musí být negované.

### 3.3 Příklad — jednobitová úplná [[Sčítačka|sčítačka]]
3 vstupy ($a, b$, přenos $p$), 2 výstupy (součet $s$, přenos $q$):
$$s=a\oplus b\oplus p,\qquad q=ab+ap+bp=M_3(a,b,p)\ \text{(majorita)}.$$
Součet $s$ nelze v mapě zjednodušit (žádné dvě jedničky nesousedí) → realizace přes XOR; přenos $q$ se minimalizuje na 3 dvojice. Z **dvou polovičních sčítaček** ($s=a\oplus b$, $q=ab$) + hradla OR vznikne úplná sčítačka.

### 3.4 Hazardy
**Hazard** vzniká, šíří-li se signál na výstup různými cestami s různým zpožděním → na výstupu se může krátce objevit nesprávná hodnota (zákmit). Typy: **statický** (1/0), **dynamický**. **Kritérium z mapy:** sousedí-li dvě jedničky patřící do **různých krychlí**, hrozí statický hazard v jedničce; odstraní se přidáním **redundantní krychle** přemosťující obě skupiny.

---

## 4. Sekvenční logické obvody

### 4.1 Definice a model
**[[Sekvenční-obvod|Sekvenční obvod (SO)]]** je obvod, jehož výstupy závisí nejen na okamžité kombinaci vstupů, ale i na **posloupnosti** předchozích vstupů — musí si pamatovat **vnitřní stav**. Paměť je realizována **zpětnou vazbou**. Matematickým modelem SO je **[[Konečný-automat|konečný automat]]** (Mealy/Moore, §5).

**Huffmanův model:** kombinační část (počítá výstupy a následující stav) + **paměťová část** (registr stavu z [[Klopný-obvod|klopných obvodů]]), uzavřená zpětnou vazbou, řízená hodinami **CLK**.

### 4.2 Klopné obvody
**[[Klopný-obvod|Klopný obvod]]** = jednobitová bistabilní paměť. Typy: **D** ($Q^{t+1}=D$), **RS**, **JK** ($J\overline Q+\overline K Q$), **T** ($T\oplus Q$). V BI-SAP se používá výhradně **D klopný obvod**: hodnota na vstupu D se hodinovým pulzem překlopí na výstup, takže **budicí funkce = funkce následujícího stavu**.

### 4.3 Synchronní vs asynchronní
- **Asynchronní:** stav se může měnit kdykoli (paměť = vodiče se zpětnou vazbou); obtížné časování.
- **Synchronní (SSO):** stav se mění jen v okamžicích **hodinového signálu**; frekvence se volí tak, aby kombinační část stihla ustálit signály.

### 4.4 Kódování stavů
Pro $n$ vnitřních stavů je potřeba $m$ stavových proměnných, $2^{m-1}<n\le 2^m$ (tedy $m=\lceil\log_2 n\rceil$). Volba kódu ovlivňuje složitost kombinační části (u čítačů se kód volí rovný požadovanému výstupu).

---

## 5. Konečné automaty: Mealyho a Mooreův

### 5.1 Definice
Konečný automat (model SO) je **automat s výstupem (převodník)** — pětice
$$M=\langle X, Y, Q, \delta, \lambda\rangle,$$
kde $X$ = vstupní abeceda, $Y$ = **výstupní abeceda**, $Q$ = stavy, $\delta:X\times Q\to Q$ = **přechodová funkce**, $\lambda$ = **výstupní funkce**. (Pozor: jde o jiný objekt než akceptor z AAG — má výstup, nikoli koncové stavy a přijímaný jazyk.)

| | výstupní funkce | výstup závisí na |
|---|---|---|
| **Mealyho automat** | $\lambda:X\times Q\to Y$ | stavu **i vstupu** |
| **Mooreův automat** | $\lambda:Q\to Y$ | **jen** na stavu |

### 5.2 Rozdíl Mealy × Moore
- **Mooreův automat nemá přímou vazbu vstup→výstup.** Změna vstupu se na jeho výstupu projeví až **po aktivní hraně hodin** (o jeden takt později než u Mealyho, jehož výstup se mění „hned"). Z hlediska reakce na vstup je tedy Moore o takt **zpožděn**.
- Mooreův automat má pro tutéž funkci **zpravidla více stavů** (v nejlepším případě stejně).
- **V realizaci:** u Mealyho se výstup odebírá ze **vstupu** klopného obvodu (kombinačně, mění se hned), u Moora z **výstupu** klopného obvodu (až po hraně CLK). Pro řadič procesoru je vhodný Mooreův automat (snazší synchronizace).

### 5.3 Popis automatu
- **Graf přechodů (stavový diagram):** orientovaný graf, uzly = stavy. U Mealyho jsou hrany značeny *vstup/výstup*, u Moora je výstup zapsán **u stavu**.
- **Tabulka přechodů** ($\delta$): pro každý stav a vstup následující stav. **Tabulka výstupů** ($\lambda$): u Mealyho stejně velká jako tabulka přechodů, u Moora **jen jeden sloupec** (výstup závisí na stavu).

### 5.4 Postup syntézy (7 kroků)
1. Vytvoř **graf přechodů**.
2. Vyplň tabulky pro $\delta$ a $\lambda$.
3. **Zakóduj** stavy (a vstupy/výstupy) → kódované tabulky.
4. Zapiš funkce do **map**.
5. Najdi **minimální výrazy** pro budicí funkce klopných obvodů (D) a pro výstupy.
6. **Realizuj** obvod (D klopné obvody + kombinační logika).
7. Spočítej **maximální hodinovou frekvenci** $f_{max}=1/W$, kde $W$ je nejdelší cesta (zpoždění hradel + Clock-to-Q klopného obvodu + předstih/setup).

### 5.5 Příklad — čítač M4 (Mealy vs Moore)
**[[Čítač|Čítač]] je sekvenční obvod** (ne jen „speciální registr" — má vnitřní stav a zpětnou vazbu), takže se navrhuje právě tímto 7krokovým postupem. Týž postup dává libovolný **modulo-$N$** čítač (komise často chce **netriviální** příklad, např. **M5 s povolovacím vstupem $E$**) — jen se změní počet stavů a kódovací tabulka.

Modulo-4 čítač s povolovacím vstupem $E$ (při $E=0$ nečítá), výstup = binární kód 0…3, dva D klopné obvody (stavové proměnné $q_1q_0$). Stavový kód volíme rovný výstupu.

Budicí (= následující stav) a výstupní funkce:
$$D_{q_0}=q_0\overline E+\overline{q_0}E=q_0\oplus E,\qquad D_{q_1}=\overline{q_0}q_1+q_1\overline E+q_0\overline{q_1}E=E q_0\oplus q_1$$
$$Y_0=q_0,\quad Y_1=q_1.$$
Každý stupeň je vlastně **poloviční sčítačka** ($q_0\oplus E$ + přenos $E\cdot q_0$). U **Moora** se výstup bere z výstupů klopných obvodů (objeví se až po hraně CLK), u **Mealyho** z jejich vstupů (objeví se zároveň s následujícím stavem).

### 5.6 Převod Mealy → Moore
1. Uzel, do něhož všechny vstupní hrany nesou **stejný** výstupní symbol, **ponecháme**.
2. Uzel s různými výstupy na vstupních hranách **rozštěpíme** na tolik uzlů, kolik je různých výstupních symbolů.
3. Doplníme hrany a stavům přiřadíme odpovídající **výstupní symboly** (Moore: výstup u stavu). Výsledný Mooreův automat má aspoň tolik stavů jako původní Mealyho.

---

## 6. Co je potřeba na zkoušku znát

### Definice
Kombinační vs sekvenční obvod; Booleova algebra (axiomy 1–5); literál, P-/S-term, minterm, maxterm; ÚNDF/ÚNKF, MNDF/MNKF; (prvo)implikant, podstatný implikant; Karnaughova mapa, sousední stavy, don't-care; hradlo, úplný systém (NAND/NOR); klopný obvod (D); konečný automat (5-tice), Mealy vs Moore.

### Postupy
- Minimalizace mapou: prvoimplikanty → podstatné → pokrytí; využití don't-care; cyklická sousednost.
- Algebraická minimalizace (absorbce, consensus); Quine–McCluskey (princip).
- Realizace na hradlech: AND-OR a NAND-NAND (pravidlo lichých úrovní); detekce hazardů z mapy + redundantní krychle.
- 7 kroků syntézy SSO; výpočet $f_{max}$.
- Převod Mealy → Moore (štěpení stavů).

### Vzorce
- Úplná sčítačka: $s=a\oplus b\oplus p$, $q=ab+ap+bp$.
- Počet stavových proměnných: $2^{m-1}<n\le2^m$.
- Charakteristické rovnice KO: D, RS, JK, T.

### Typické doplňující otázky (doptávání)
> Z reálných zkušeností (Kohlík, Daňhel, Kubátová, Dobiáš…).
- **Proč se XOR tak často používá?** → §3.1 (detektor nerovnosti/parity: sčítačka, řízený invertor, komparátor, parita).
- **Jmenujte kombinační obvod důležitý v počítači** → **sčítačka / ALU** (§3.3).
- **Je čítač kombinační, nebo sekvenční obvod?** → **sekvenční** (má stav + zpětnou vazbu), §5.5.
- **Navrhněte netriviální sekvenční obvod**, např. **M5 čítač s povolovacím vstupem $E$** → 7 kroků syntézy, §5.4–5.5.
- **Rozdíl Mealy × Moore i v realizaci** (odkud se bere výstup) a **převod Mealy→Moore** → §5.2, §5.6.
- **Rozlište značky hradel** NAND × NOR (kroužek na výstupu) → §3.1.
- **Jak vyjádříte logickou funkci?** (z mapy SOP/POS, ÚNDF/ÚNKF) → §1.4, §2.
