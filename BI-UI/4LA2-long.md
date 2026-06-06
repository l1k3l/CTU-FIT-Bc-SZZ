---
studyplan: true
etapa: "3 · LA1 / MA2 / LA2 — Petr"
qid: "4LA2"
examiner: "Petr"
topic: "LU rozklad, řešení soustav pomocí LU"
readiness: nezačato
tags: [otázka, kurz/LA2, otázka/4, todo]
---

# LU rozklad a řešení soustav

> **Otázka SZZ:** LU rozklad matic, řešení soustavy lineárních rovnic pomocí LU rozkladu.

Zdroje: BI-LA2 (Klouda a kol., FIT ČVUT), kap. 8 (LU rozklad) — 8.2 Definice LU rozkladu, 8.3 Výpočet LU rozkladu, 8.4 Řešení soustavy rovnic pomocí LU rozkladu, 8.5 LU rozklad s pivotací, 8.6 LU stabilita, 8.7 Částečná pivotace (str. 148–162).

Značení: $A \in T^{n,n}$ čtvercová [[Matice|matice]] nad tělesem $T$ (v textu $\mathbb{R}$), $E$ jednotková matice, $\theta$ nulový vektor, $A^T$ transpozice, vektory píšeme kurzívou. Pojem **rozklad (faktorizace)** matice znamená její přepsání do tvaru součinu $A = BC$ matic se speciálními vlastnostmi (trojúhelníkové, diagonální, …).

---

## 1. Definice LU rozkladu

**Gaussova eliminační metoda** převádí matici $A$ na matici v horním stupňovitém tvaru; je-li $A$ čtvercová, jde zároveň o **horní trojúhelníkovou** matici, kterou značíme $U$ (z angl. *upper triangular*).

**Definice (LU rozklad).** Mějme matici $A \in T^{n,n}$. Pokud existují **dolní trojúhelníková matice $L \in T^{n,n}$ s jedničkami na diagonále** (z angl. *lower triangular*) a **horní trojúhelníková matice $U \in T^{n,n}$** tak, že
$$A = LU,$$
nazýváme tento součin **[[LU-rozklad|LU rozkladem]]** (LU faktorizací) matice $A$. Matice $L$ a $U$ nazýváme **faktory**. Schématicky
$$L = \begin{pmatrix} 1 & 0 & \cdots & 0 \\ * & 1 & \cdots & 0 \\ \vdots & & \ddots & \vdots \\ * & * & \cdots & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} * & * & \cdots & * \\ 0 & * & \cdots & * \\ \vdots & & \ddots & \vdots \\ 0 & 0 & \cdots & * \end{pmatrix},$$
kde $*$ zastupuje libovolné hodnoty (na vynechaných místech jsou nuly).

### 1.1 Kdy LU rozklad existuje

LU rozklad **neexistuje pro každou matici**. Například
$$A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$$
nemá LU rozklad: rovnice $\left(\begin{smallmatrix} 0 & 1 \\ 1 & 1 \end{smallmatrix}\right) = \left(\begin{smallmatrix} 1 & 0 \\ x & 1 \end{smallmatrix}\right)\left(\begin{smallmatrix} y & z \\ 0 & w \end{smallmatrix}\right)$ nemá řešení (z levého horního rohu vyjde $y = 0$, ale pak $1 = xy = 0$).

**Věta (o existenci LU rozkladu).** Matice má LU rozklad **právě tehdy, když ji lze převést do horního stupňovitého tvaru pouze úpravami „(G3) směrem dolů“** — tj. přičítáním násobku řádku k řádku s **vyšším** indexem, bez prohazování řádků (G1).

Související postačující podmínka přes hlavní minory: je-li $A$ **silně regulární** — tj. všechny vedoucí hlavní podmatice $A_{1:1,1:1}, A_{1:2,1:2}, \dots, A_{1:n,1:n}$ jsou [[Regulární-matice|regulární]] (mají nenulový [[Determinant|determinant]]) — pak eliminace nikdy nenarazí na nulový pivot a LU rozklad existuje. Naopak regulární matice má LU rozklad právě tehdy, když je silně regulární.

### 1.2 Jednoznačnost

**Poznámka (o jednoznačnosti).** Je-li matice **regulární** a má-li LU rozklad, pak je tento rozklad **jednoznačný**.

*Náznak důkazu.* Nechť $\widehat{L}\widehat{U} = A = LU$ jsou dva rozklady. Protože $A$ je regulární, jsou regulární i všechny faktory. Pak
$$L^{-1}\widehat{L} = U \widehat{U}^{-1}.$$
Levá strana je dolní trojúhelníková s jedničkami na diagonále (inverze i součin takových matic mají tutéž vlastnost), pravá strana je horní trojúhelníková. Matice, která je zároveň horní i dolní trojúhelníková s jedničkami na diagonále, je jednotková matice $E$:
$$L^{-1}\widehat{L} = U\widehat{U}^{-1} = E \implies L = \widehat{L},\ U = \widehat{U}. \qquad \square$$
(Pro **singulární** matici jednoznačnost neplatí — existují singulární matice s více různými LU rozklady.)

---

## 2. Výpočet LU rozkladu

LU rozklad je v podstatě **„záznam“ Gaussovy eliminace**: v matici $U$ je výsledný horní stupňovitý tvar, v matici $L$ je uloženo, jaké operace (G3) byly při eliminaci použity.

### 2.1 Eliminační matice

Každý krok GEM „směrem dolů“ odpovídá vynásobení $A$ zleva dolní trojúhelníkovou maticí. Označme $x_k$ $k$-tý sloupec matice $X_{k-1}$ vzniklé z $A$ po $k-1$ krocích. V $k$-tém kroku vynulujeme prvky pod diagonálním prvkem $x_{kk}$ tak, že od $j$-tého řádku ($k < j \le n$) odečteme $\ell_{jk}$-násobek $k$-tého řádku, kde **multiplikátor**
$$\ell_{jk} = \frac{x_{jk}}{x_{kk}} \qquad (k < j \le n).$$
Tomuto kroku odpovídá matice $L_k = E - \ell_k e_k^T$, kde $\ell_k = (0,\dots,0,\ell_{k+1,k},\dots,\ell_{nk})^T$ a $e_k$ je $k$-tý vektor standardní báze. Po $n-1$ krocích
$$\underbrace{L_{n-1}\cdots L_2 L_1}_{L^{-1}} A = U, \qquad A = LU, \quad L = L_1^{-1}\cdots L_{n-1}^{-1}.$$

Pokud $x_{kk} = 0$: buď jsou všechny prvky pod ním nulové (pak $\ell_{jk} = 0$ a krok netřeba), nebo je některý nenulový — pak požadovaný krok GEM nelze provést a **matice nemá LU rozklad** (řeší se pivotací, viz §4).

### 2.2 Tvar faktoru $L$ (proč se multiplikátory přímo zapisují)

Dva pomocné výsledky činí výpočet $L$ triviálním:

**Tvrzení (inverze jedné eliminační matice).** $L_k = E - \ell_k e_k^T \implies L_k^{-1} = E + \ell_k e_k^T$.

*Důkaz.* Z identity $e_k^T \ell_k = 0$ (k-tá složka $\ell_k$ je nula) plyne
$$(E - \ell_k e_k^T)(E + \ell_k e_k^T) = E + \ell_k e_k^T - \ell_k e_k^T - \ell_k \underbrace{(e_k^T \ell_k)}_{0} e_k^T = E. \qquad \square$$

**Tvrzení (tvar součinu inverzí).** $L = L_1^{-1} L_2^{-1} \cdots L_{n-1}^{-1} = E + \ell_1 e_1^T + \cdots + \ell_{n-1} e_{n-1}^T$.

*Idea důkazu.* Neúplnou indukcí; při roznásobení mizí všechny smíšené členy díky $e_j^T \ell_k = 0$ pro $j \le k-1$. $\square$

**Důsledek (o faktoru $L$).** Faktor $L$ se dá během Gaussovy eliminace určit jednoduše tak, že na pozici $(j,k)$ **přímo zapíšeme multiplikátor $\ell_{jk}$** použitý k vynulování prvku na téže pozici:
$$L = \begin{pmatrix} 1 & & & \\ \ell_{21} & 1 & & \\ \ell_{31} & \ell_{32} & 1 & \\ \vdots & & \ddots & \\ \ell_{n1} & \ell_{n2} & \cdots & 1 \end{pmatrix}.$$

### 2.3 Algoritmus a složitost

```
Algoritmus (LU rozklad bez pivotace)
vstup:  A ∈ T^{n,n}
výstup: L (dolní troj., jedničky na diag.), U (horní troj.), A = LU

U ← A;  L ← E
for k = 1, …, n-1 do
    if u_kk = 0 then
        if ∃ j ∈ {k+1,…,n}: u_jk ≠ 0 then
            STOP  (matice nemá LU rozklad)
        else
            for j = k+1, …, n do  ℓ_jk ← 0
    else
        for j = k+1, …, n do
            ℓ_jk      ← u_jk / u_kk          # multiplikátor → do L
            u_{j,k:n} ← u_{j,k:n} − ℓ_jk · u_{k,k:n}   # eliminace řádku
```

**Složitost.** Aktualizace prvků odpovídá objemu „jehlanu“ o základně $n$, tedy $\sim \tfrac{1}{3}n^3$ aktualizovaných prvků, každá za 2 aritmetické operace — celkem $\sim \tfrac{2}{3}n^3$ operací, tj. $O(n^3)$. Faktorizace je výpočetně stejně náročná jako jeden běh GEM.

---

## 3. Řešení soustavy $Ax = b$ pomocí LU rozkladu

Hlavní využití LU rozkladu je řešení **[[Soustava-lineárních-rovnic|soustav lineárních rovnic]]**. Řešme soustavu $n$ rovnic o $n$ neznámých s **regulární** maticí $A \in T^{n,n}$ a pravou stranou $b$:
$$Ax = b \iff LUx = b.$$
Označíme $y = Ux$ a soustavu rozdělíme na dvě snadno řešitelné **trojúhelníkové** soustavy:
$$\boxed{\;Ly = b \quad(\text{dopředná substituce}), \qquad Ux = y \quad(\text{zpětná substituce}).\;}$$

### 3.1 Dopředná substituce ($Ly = b$)

$L$ je dolní trojúhelníková s jedničkami na diagonále, řešíme **shora dolů** (od prvního řádku k poslednímu):
$$y_i = b_i - \sum_{j=1}^{i-1} \ell_{ij}\, y_j, \qquad i = 1, \dots, n.$$

### 3.2 Zpětná substituce ($Ux = y$)

$U$ je horní trojúhelníková, řešíme **zdola nahoru** (od posledního řádku k prvnímu):
$$x_i = \frac{1}{u_{ii}}\Bigl(y_i - \sum_{j=i+1}^{n} u_{ij}\, x_j\Bigr), \qquad i = n, n-1, \dots, 1.$$
(Zpětnou substituci znáte z GEM — jde o řešení soustavy s trojúhelníkovou maticí postupným dosazováním.)

### 3.3 Příklad

Pro $A = \left(\begin{smallmatrix} 3 & 1 & 1 & 1 \\ 6 & 4 & 4 & 3 \\ 15 & 9 & 10 & 7 \\ 9 & 7 & 5 & 7 \end{smallmatrix}\right)$ vyjde GEM (jen G3 dolů)
$$L = \begin{pmatrix} 1 & & & \\ 2 & 1 & & \\ 5 & 2 & 1 & \\ 3 & 2 & -2 & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} 3 & 1 & 1 & 1 \\ 0 & 2 & 2 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 2 \end{pmatrix}.$$
Pro $b = (2,7,15,16)^T$: dopředně $Ly = b \Rightarrow y = (2,3,-1,2)^T$, zpětně $Ux = y \Rightarrow x = (0,2,-1,1)^T$.

### 3.4 Složitost a hlavní výhoda

Každá substituce stojí $\sim n^2$ operací, tedy $O(n^2)$; obě dohromady stále $O(n^2)$.

**Výhoda pro více pravých stran.** Faktorizaci $A = LU$ spočítáme **jen jednou** za $O(n^3)$. Pro každou další pravou stranu $b$ (častá úloha v aplikacích) už stačí jen dvě substituce za $O(n^2)$. Naproti tomu opakovaný běh GEM pro každou novou $b$ by stál pokaždé $O(n^3)$. (Faktory $L, U$ závisí jen na $A$, nikoli na $b$.)

---

## 4. LU rozklad s pivotací $PA = LU$

U řešení soustavy **nezáleží na pořadí rovnic**, takže můžeme přeházet pořadí řádků (a adekvátně i pravé strany), aby matice už LU rozklad měla. Výměnu řádků reprezentuje **permutační matice**.

**Definice (permutační matice).** Je-li $\pi$ permutace na $\{1,\dots,n\}$, je $P$ daná $P_{ij} = 1$ pro $\pi(i) = j$ a $0$ jinak. Násobení $PA$ zleva přeházejí pořadí řádků $A$; $P$ má v každém řádku i sloupci právě jednu jedničku.

**Definice (LU rozklad s řádkovou pivotací).** Zápis
$$PA = LU,$$
kde $P$ je permutační matice, $L$ dolní trojúhelníková s jedničkami na diagonále a $U$ horní trojúhelníková, nazýváme **LU rozkladem s řádkovou pivotací**. **Každá** čtvercová matice takový rozklad má (kvůli volbě $P$ nemusí být jednoznačný).

### 4.1 Motivace — nulový pivot a numerická stabilita

- **Nulový pivot.** Matice $\left(\begin{smallmatrix} 0 & 1 \\ 1 & 1 \end{smallmatrix}\right)$ nemá LU rozklad, ale po prohození řádků (permutaci) už ano.
- **Numerická stabilita (LU stabilita).** I když rozklad existuje, dělení **malým** pivotem $x_{kk}$ v multiplikátoru $\ell_{jk} = x_{jk}/x_{kk}$ vede k velkým prvkům a ztrátě přesnosti. Příklad: pro $A = \left(\begin{smallmatrix} 10^{-20} & 1 \\ 1 & 1 \end{smallmatrix}\right)$ má LU rozklad bez pivotace relativní zpětnou chybu $\tfrac{1}{2}$ — **není zpětně stabilní** — a spočtené řešení soustavy je úplně chybné.

### 4.2 Částečná pivotace

**Definice (částečná pivotace).** LU rozklad s řádkovou pivotací $PA = LU$ je **s částečnou pivotací**, pokud $|\ell_{ij}| \le 1$ pro všechna $i \ge j$. Toho dosáhneme tím, že v $k$-tém kroku GEM přepermutujeme řádky tak, aby na pozici $x_{kk}$ byl v absolutní hodnotě **největší prvek zpracovávaného sloupce**:
$$|x_{kk}| = \max_{i \ge k} |x_{ik}| \implies \ell_{ik} = \frac{x_{ik}}{x_{kk}}, \quad |\ell_{ik}| \le 1.$$
Tím se vyhneme dělení malým pivotem. Při prohození řádků se prohazují i už zapsané části faktoru $L$ a aktualizuje se $P$.

```
Algoritmus (LU s částečnou pivotací)
U ← A;  L ← E;  P ← E
for k = 1, …, n-1 do
    zvol i ≥ k tak, aby |u_ik| bylo maximální
    if u_ik = 0 then  for j=k+1..n: ℓ_jk ← 0          # sloupec pod diag. nulový
    else
        prohoď řádky:  u_{k,k:n} ↔ u_{i,k:n};  ℓ_{k,1:k-1} ↔ ℓ_{i,1:k-1};  p_{k,:} ↔ p_{i,:}
        for j = k+1, …, n do
            ℓ_jk      ← u_jk / u_kk
            u_{j,k:n} ← u_{j,k:n} − ℓ_jk · u_{k,k:n}
```

Řešení soustavy s $PA = LU$: z $Ax = b$ je $PAx = Pb$, tedy $LUx = Pb$ — nejdřív přeházíme pravou stranu na $Pb$, pak dopředná $Ly = Pb$ a zpětná $Ux = y$.

**Úplná pivotace** navíc permutuje i sloupce ($PAQ = LU$, $Q$ permutuje neznámé) tak, aby pivot byl největší v celé nezpracované části; její přínos obvykle nepřeváží vyšší cenu, proto se v praxi používá částečná pivotace.

---

## 5. Poznámka k determinantu

Z $A = LU$ a vlastnosti $\det(AB) = \det A \cdot \det B$ plyne, že [[Determinant|determinant]] se z LU rozkladu spočte snadno: determinant trojúhelníkové matice je součin diagonálních prvků, a protože $\det L = 1$ (jedničky na diagonále), je
$$\det A = \det L \cdot \det U = \prod_{i=1}^{n} u_{ii}.$$
S pivotací $PA = LU$ navíc $\det A = \det(P^{-1})\prod_i u_{ii} = \pm\prod_i u_{ii}$, kde znaménko je $(-1)$ na počet prohození řádků:
$$\boxed{\;\det A = \pm \prod_{i=1}^{n} u_{ii}.\;}$$

---

## Co je potřeba na zkoušku znát

### Definice
- **LU rozklad:** $A = LU$, $L$ dolní trojúhelníková s **jedničkami na diagonále**, $U$ horní trojúhelníková.
- **LU rozklad s (řádkovou / částečnou) pivotací:** $PA = LU$, $P$ permutační matice; částečná pivotace $\Rightarrow |\ell_{ij}| \le 1$.
- Multiplikátor $\ell_{jk} = x_{jk}/x_{kk}$; permutační matice.

### Věty
- **Existence:** LU rozklad existuje $\iff$ matici lze do HST převést jen úpravami (G3) dolů; silně regulární matice ho má.
- **Jednoznačnost:** regulární matice s LU rozkladem ho má jednoznačný (náznak: $L^{-1}\widehat L = U\widehat U^{-1} = E$).
- **Pivotace:** každá čtvercová matice má rozklad $PA = LU$.
- **Determinant:** $\det A = \pm\prod_i u_{ii}$.

### Algoritmy
- **Výpočet LU** přes GEM (G3 dolů): $U$ = HST, multiplikátory $\ell_{jk}$ zapisujeme přímo do $L$; složitost $\sim\tfrac{2}{3}n^3 = O(n^3)$.
- **Řešení $Ax = b$:** dopředná substituce $Ly = b$ (shora dolů) + zpětná substituce $Ux = y$ (zdola nahoru), každá $O(n^2)$.
- **Výhoda LU vs. opakovaná GEM:** faktorizace jednou $O(n^3)$, pak každá další pravá strana jen $O(n^2)$.
- **Pivotace** ($|\ell_{ij}|\le 1$): kvůli nulovému pivotu a numerické stabilitě (dělení malým pivotem).
