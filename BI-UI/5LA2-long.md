---
tags: [otázka, kurz/LA2, otázka/5, todo]
---

# QR rozklad a metoda nejmenších čtverců

> **Otázka SZZ:** QR rozklad: výpočet a využití při výpočtu odhadu metodou nejmenších čtverců.

Zdroje: BI-LA2 (FIT ČVUT), kap. 9 (QR rozklad) — sekce 9.2 Ortogonální matice, 9.3 Vlastnosti OG matic, 9.4 Definice QR rozkladu, 9.5 Existence a jednoznačnost, 9.6 Triangularizace, 9.7 Householderova triangularizace, 9.8 Givensova triangularizace; kap. 12 (Metoda nejmenších čtverců) — sekce 12.2 Motivace, 12.4–12.6 přeurčená soustava a normální rovnice, 12.7 řešení pomocí QR; printed str. 163–190 a 239–253.

Značení: $A \in \mathbb{R}^{m,n}$ matice, $E_n$ jednotková matice, $A^T$ transpozice, $Q$ ortogonální matice, $R$ horní trojúhelníková matice, $\|\cdot\|$ (resp. $\|\cdot\|_2$) eukleidovská norma, $h(A)$ hodnost, $\theta$ nulový vektor, $\varphi, \theta$ úhly, vektory plain italikou ($x, b, v, q$).

---

## 1. Ortogonální matice a jejich vlastnosti

### 1.1 Matice s ortonormálními sloupci

**Definice (matice s ortonormálními sloupci).** Matici $Q \in \mathbb{R}^{m,n}$, $m \ge n$, nazýváme **maticí s ortonormálními sloupci**, pokud
$$Q^T Q = E_n.$$
Rozepsáno přes sloupce: $Q_{:i}^T Q_{:j} = \langle Q_{:i} \mid Q_{:j}\rangle = \begin{cases} 0 & i \neq j, \\ 1 & i = j, \end{cases}$ tedy soubor sloupců $(Q_{:1},\dots,Q_{:n})$ je **ortonormální** vzhledem ke standardnímu **[[Skalární-součin|skalárnímu součinu]]**.

### 1.2 Ortogonální matice

**Definice ([[Ortogonální-matice|ortogonální matice]]).** Čtvercovou matici $Q \in \mathbb{R}^{n,n}$ nazýváme **ortogonální** (OG) maticí, pokud
$$Q^T = Q^{-1}, \qquad \text{tj.} \qquad Q^T Q = Q Q^T = E_n.$$
Transpozice OG matice je tedy zároveň její inverzí — užitečné, neboť obecně je inverze numericky drahá. Každá OG matice je triviálně maticí s ortonormálními sloupci; naopak každá **čtvercová** matice s ON sloupci je nutně ortogonální (postačitelnost inverze z jedné strany). Sloupce ortogonální matice tvoří ortonormální bázi $\mathbb{R}^n$ (viz **[[Ortogonální-báze]]**).

### 1.3 Vlastnosti ortogonálních matic

**Tvrzení (transpozice a součin).** Je-li $Q$ ortogonální, je $Q^T$ ortogonální. Jsou-li $Q_1, Q_2 \in \mathbb{R}^{n,n}$ ortogonální, je jejich součin ortogonální.

*Důkaz.* Pro transpozici: z $E = QQ^T = (Q^T)^TQ^T$ a $E = Q^TQ = Q^T(Q^T)^T$ plyne $(Q^T)^{-1} = (Q^T)^T$. Pro součin: $Q_1Q_2$ je součin regulárních matic, tedy regulární, a $(Q_1Q_2)^{-1} = Q_2^{-1}Q_1^{-1} = Q_2^TQ_1^T = (Q_1Q_2)^T$. $\square$

(Tvrzení o součinu je klíčové pro triangularizace — viz §3.)

**Tvrzení (zachování skalárního součinu).** Je-li $Q \in \mathbb{R}^{n,n}$ ortogonální, pak pro všechna $x, y \in \mathbb{R}^n$ platí
$$(Qx)^T(Qy) = x^T y.$$

*Důkaz.* $(Qx)^T(Qy) = x^T Q^T Q y = x^T E y = x^T y.$ $\square$

Odtud plyne, že ortogonální matice **zachovává ortogonalitu**: $x \perp y \Rightarrow Qx \perp Qy$. (Totéž platí i pro matici s ortonormálními sloupci — důkaz potřebuje jen $Q^TQ = E_n$. Naopak pro matici s pouze **ortogonálními** (neznormovanými) sloupci to neplatí — protipříklad $R = \begin{psmallmatrix}2&2\\-1&4\end{psmallmatrix}$ má kolmé sloupce, ale kolmé vektory $(1,-1),(1,1)$ zobrazí na nekolmé.)

**Tvrzení (zachování eukleidovské [[Norma|normy]]).** Je-li $Q$ ortogonální, pak $\|Qx\|_2 = \|x\|_2$ pro každé $x$.

*Důkaz.* $\|Qx\|_2^2 = (Qx)^T(Qx) = x^TQ^TQx = x^Tx = \|x\|_2^2.$ $\square$

Tato izometrie je důvodem velkého využití OG matic v numerické lineární algebře: násobení OG maticí **nezvětší** zaokrouhlovací chyby. Formálně: **číslo podmíněnosti** $\kappa_2(Q) = \|Q\|_2\,\|Q^{-1}\|_2 = 1$, a maticové normy $\|\cdot\|_2, \|\cdot\|_F$ jsou **invariantní** vůči násobení OG maticí: $\|QA\|_2 = \|A\|_2 = \|AR\|_2$, totéž pro $\|\cdot\|_F$.

**Tvrzení (determinant).** Pro ortogonální $Q$ je $\det Q = \pm 1$.

*Důkaz.* Aplikací determinantu na $Q^TQ = E$: $\det(Q^T)\det(Q) = (\det Q)^2 = \det E = 1$, tedy $\det Q = \pm 1$. $\square$

Geometricky: $\det Q = +1$ odpovídá **rotaci**, $\det Q = -1$ **zrcadlení** (reflexi). Obě budou stavebními kameny triangularizací.

**Tvrzení (vlastní čísla).** Pro každé vlastní číslo $\lambda$ ortogonální matice platí $|\lambda| = 1$.

*Důkaz.* Z $Qx = \lambda x$ pro vlastní vektor $x \neq \theta$ je $\|x\|_2 = \|Qx\|_2 = |\lambda|\,\|x\|_2$, tedy $|\lambda| = 1$. $\square$

(Pozor: vlastní čísla mohou být komplexní — např. $\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$ má $\pm i$. Neplatí tedy $\lambda \in \{-1,1\}$.)

---

## 2. QR rozklad

### 2.1 Definice

**Definice (redukovaný [[QR-rozklad|QR rozklad]]).** Mějme $m \ge n$ a $A \in \mathbb{R}^{m,n}$. Zápis
$$A = \hat{Q}\hat{R},$$
kde $\hat{Q} \in \mathbb{R}^{m,n}$ je matice s ortonormálními sloupci ($\hat{Q}^T\hat{Q} = E_n$) a $\hat{R} \in \mathbb{R}^{n,n}$ je horní trojúhelníková, nazýváme **redukovaný QR rozklad**.

**Definice (úplný QR rozklad).** Zápis
$$A = QR,$$
kde $Q \in \mathbb{R}^{m,m}$ je ortogonální a $R \in \mathbb{R}^{m,n}$ je „horní trojúhelníková“ ($R_{ij} = 0$ pro $i > j$; pro $m>n$ jde o tzv. horní lichoběžníkovou matici), nazýváme **úplný (kompletní) QR rozklad**.

Schématicky pro $m > n$: v úplném rozkladu má $R$ posledních $m-n$ řádků nulových, takže posledních $m-n$ sloupců $Q$ při násobení nehraje roli. Označíme-li $\hat{Q} = Q_{:,1:n}$ a $\hat{R}$ horních $n$ řádků $R$, dostaneme redukovaný rozklad. Naopak z redukovaného získáme úplný doplněním sloupců $\hat{Q}$ o libovolnou ON bázi ortogonálního doplňku $\langle q_1,\dots,q_n\rangle^\perp$ a $\hat{R}$ o nulové řádky. Pro $m = n$ oba pojmy splývají.

### 2.2 Existence a jednoznačnost

**Věta (o existenci).** Pro $m \ge n$ má každá matice $A \in \mathbb{R}^{m,n}$ redukovaný i úplný QR rozklad.

*Důkaz (idea).* Stačí najít redukovaný (úplný se z něj doplní). Pokud jsou sloupce $A$ LN, sestrojíme rozklad Gramovou–Schmidtovou ortogonalizací (§3.1). Selže-li ortogonalizace v $k$-tém kroku ($a_k \in \langle q_1,\dots,q_{k-1}\rangle$, tj. $z_k = \theta$), zvolíme $q_k$ jako libovolný jednotkový vektor kolmý na $\langle q_1,\dots,q_{k-1}\rangle$ a položíme $r_{kk} = 0$. Tím rovnost $a_k = r_{1k}q_1 + \dots + r_{k-1,k}q_{k-1} + 0\cdot q_k$ stále platí a po $n$ krocích máme redukovaný rozklad. $\square$

**Věta (o jednoznačnosti).** Mějme $m \ge n$ a $A \in \mathbb{R}^{m,n}$ s hodností $n$. Potom existuje **právě jeden** redukovaný QR rozklad $A = \hat{Q}\hat{R}$ s $r_{jj} > 0$ pro všechna $j$.

*Náznak důkazu.* Existence: rozklad z klasického Gramova–Schmidtova algoritmu má všechny diagonální členy $\hat{R}$ kladné. Jednoznačnost: mějme dva takové rozklady $\hat{Q}\hat{R} = A = \tilde{Q}\tilde{R}$. Protože $h(A)=n$, jsou $\hat{R},\tilde{R}$ regulární a $\tilde{R}\hat{R}^{-1} = \tilde{Q}^T\hat{Q} =: D$. Levá strana je horní trojúhelníková s kladnou diagonálou, $(\tilde{Q}^T\hat{Q})^T = \hat{Q}^T\tilde{Q} = \hat{R}\tilde{R}^{-1}$ je rovněž horní trojúhelníková — tedy $D$ je zároveň dolní i horní trojúhelníková, čili diagonální s kladnými prvky. Z $D^TD = E$ plyne $D^2 = E$, tedy $D = E$. Odtud $\hat{R} = \tilde{R}$ a $\hat{Q} = \tilde{Q}$. $\square$

Bez podmínky $r_{jj} > 0$ jednoznačnost neplatí (lze měnit znaménka sloupců $\hat{Q}$ a řádků $\hat{R}$); při LZ sloupcích neplatí ani s ní (volnost ve volbě „doplňkového“ $q_k$).

**Poznámka (hodnost z QR).** Platí $h(A) = h(\hat{R})$ (z odhadu hodnosti součinu: $h(A) \le h(\hat{R})$ z $A = \hat{Q}\hat{R}$ a $h(\hat{R}) \le h(A)$ z $\hat{R} = \hat{Q}^TA$).

---

## 3. Výpočet QR rozkladu

### 3.1 Gramova–Schmidtova ortogonalizace

QR rozklad úzce souvisí s **[[Gram-Schmidtův-algoritmus|Gramovou–Schmidtovou ortogonalizací]]** sloupců $a_1,\dots,a_n$ matice $A$. Rozepsání $A = \hat{Q}\hat{R}$ po sloupcích dává
$$a_1 = r_{11}q_1, \quad a_2 = r_{12}q_1 + r_{22}q_2, \quad \dots, \quad a_n = r_{1n}q_1 + \dots + r_{nn}q_n,$$
což je přesně Gramova–Schmidtova ortogonalizace s průběžnou normalizací, kde pro $i < j$:
$$r_{ij} = q_i^T a_j, \qquad r_{jj} = \|a_j - r_{1j}q_1 - \dots - r_{j-1,j}q_{j-1}\|_2.$$

**Algoritmus (klasický Gramův–Schmidt pro QR).**
```
for j = 1, ..., n:
    z_j = a_j
    for i = 1, ..., j-1:
        r_ij = q_i^T a_j        # projekční koeficient
        z_j  = z_j - r_ij q_i   # odečtení projekcí
    r_jj = ||z_j||_2
    q_j  = z_j / r_jj           # normalizace
```
Pro matici s LZ sloupci se přidá větvení: je-li $r_{jj} = 0$, zvolí se $q_j$ jako libovolný jednotkový vektor kolmý na dosud nalezené $q_i$ a $r_{jj}$ zůstane $0$.

**Složitost:** $\sim 2mn^2$ aritmetických operací (každý ze $\approx \tfrac12 mn^2 + \dots$ aktualizovaných prvků = 4 operace). **Numerická poznámka:** klasický GS **není zpětně stabilní** (ztráta ortogonality vlivem zaokrouhlení). Opravou je **modifikovaný Gramův–Schmidt**, který odečítá projekce postupně z již aktualizovaného vektoru — je stabilní při stejné asymptotické složitosti.

### 3.2 Triangularizace — princip

Máme-li $A = QR$, platí $Q^T A = R$: matice $R$ vznikne z $A$ vynásobením ortogonální maticí $Q^T$, která **vynuluje** všechny prvky pod diagonálou. Najít $Q^T$ přímo je stejně těžké jako najít QR rozklad. Proto hledáme jednoduché OG matice $Q_1, Q_2, \dots, Q_k$, z nichž každá zvětší počet nul pod diagonálou:
$$Q_k \cdots Q_2 Q_1 A = R \quad(\text{horní trojúhelníková}), \qquad Q^T = Q_k\cdots Q_1.$$
Protože součin OG matic je OG matice, je $Q = (Q_k\cdots Q_1)^T$ ortogonální a $A = QR$. Stavebními kameny jsou **rotace** ($\det Q_i = 1$) a **zrcadlení** podle nadroviny ($\det Q_i = -1$).

### 3.3 Householderova triangularizace (zrcadlení)

**Idea:** jednou ortogonální maticí (Householderovým reflektorem) zrcadlit první sloupec zpracovávané podmatice na násobek $e_1$, čímž se vynuluje **celý sloupec** pod diagonálou najednou.

**Householderův reflektor.** Pro nenulový $v \in \mathbb{R}^n$ je matice
$$F = E - \frac{2}{\|v\|_2^2}\,v v^T$$
ortogonální (zrcadlení podle nadroviny $H$ kolmé na $v$). Plyne z $\operatorname{proj}_v x = \tfrac{x^Tv}{v^Tv}v$ a faktu, že zrcadlení = identita minus dvojnásobek projekce na $v$.

**Volba normály.** Chceme $Fx = \blacksquare\, e_1$, kde $|\blacksquare| = \|x\|_2$ (zachování normy). Normála zrcadlící nadroviny je $v = \pm\|x\|_2 e_1 - x$. Z numerických důvodů volíme tu z možností, která dá **delší** vektor $v$ (vyhneme se odečtení blízkých čísel):
$$v = \operatorname{sgn}(x_1)\,\|x\|_2\, e_1 + x.$$

**Věta (ortogonalita reflektoru).** Pro nenulové $v$ je $E - \tfrac{2}{\|v\|_2^2}vv^T$ ortogonální. *(Důkaz přímým ověřením $F^TF = E$, neboť $F$ je symetrická a involutorní: $F^2 = E$.)*

V $k$-tém kroku triangularizace má matice tvar $\begin{psmallmatrix} B & C \\ \Theta & X \end{psmallmatrix}$ (prvních $k-1$ sloupců hotových); reflektor aplikujeme pouze na podmatici $X$ a sestavíme $Q_k = \begin{psmallmatrix} E_{k-1} & \\ & F \end{psmallmatrix}$.

**Algoritmus (Householderův QR — spočítá $R = Q^TA$).**
```
for k = 1, ..., n:
    x   = A[k:m, k]                      # zbytek k-tého sloupce
    v_k = sgn(x_1) ||x||_2 e_1 + x
    v_k = v_k / ||v_k||_2                # normalizace
    A[k:m, k:n] = A[k:m, k:n] - 2 v_k (v_k^T A[k:m, k:n])
```
Matici $Q$ **nekonstruujeme explicitně** — ukládáme vektory $v_k$. Násobení $Q^T b = Q_n\cdots Q_1 b$ a $Qx = Q_1\cdots Q_n x$ provádíme přímo přes reflektory (rychlejší než maticové násobení). Případné $Q = QE = (Qe_1,\dots,Qe_m)$.

**Složitost:** zásadní operace $A_{k:m,j} - 2v_k(v_k^T A_{k:m,j})$ je $4\ell$ operací na sloupec délky $\ell$. Celkem
$$2mn^2 - \tfrac{2}{3}n^3.$$

### 3.4 Givensova triangularizace (rotace)

**Idea:** rotací v rovině dvou souřadnic vynulovat **jeden** prvek pod diagonálou.

**Givensova rotace v $\mathbb{R}^2$.** Rotace zobrazující $x = (x_1,x_2)$ na $(\|x\|_2, 0)$:
$$G = \begin{pmatrix} c & s \\ -s & c \end{pmatrix}, \qquad c = \frac{x_1}{\|x\|_2}, \quad s = \frac{x_2}{\|x\|_2}.$$
(Ověření $Gx = (\|x\|_2, 0)^T$ a ortogonality $c^2+s^2=1$ je přímočaré.)

**Rotace v $\mathbb{R}^m$** $G(a_{ii}, a_{ji})$ je jednotková matice, do níž na pozicích $(i,i),(i,j),(j,i),(j,j)$ vložíme $c, s, -s, c$ (s $c = \tfrac{x_i}{\sqrt{x_i^2+x_j^2}}$, $s = \tfrac{x_j}{\sqrt{x_i^2+x_j^2}}$). Je ortogonální, mění **pouze řádky $i$ a $j$** a vytvoří nulu na pozici $(j,i)$.

**Algoritmus (Givensova triangularizace — $R = Q^TA$).**
```
for i = 1, ..., n:
    for j = i+1, ..., m:
        spočti G(a_ii, a_ji)                       # z aktuálního sloupce i
        A[{i,j}, i:n] = G(a_ii, a_ji) A[{i,j}, i:n]  # ovlivní jen řádky i, j
```

**Složitost:** na vynulování jednoho prvku 6 operací (4 násobení + 2 sčítání); celkem
$$\sim 3mn^2 - n^3,$$
tj. **o ~50 % více** než Householder.

### 3.5 Srovnání metod

- **Householderův reflektor** vynuluje celý sloupec v jedné operaci — výhodný pro **plné** matice (nejméně operací).
- **Givensova rotace** pracuje vždy se dvěma řádky a vynuluje jeden prvek — výhodná pro **řídké** matice (selektivní eliminace) a **paralelizaci** (lze vynulovat více pozic najednou).
- **Gramův–Schmidt** dává přímo $\hat{Q}$ (ON sloupce); klasický je nestabilní, modifikovaný stabilní.
- Existují i blokové verze (kombinace reflektorů uvnitř bloků a rotací mezi bloky).

---

## 4. Metoda nejmenších čtverců

### 4.1 Motivace a přeurčená soustava

V úlohách typu **lineární regrese** (statistika, strojové učení) hledáme parametry modelu $Y \approx w^T x$ z $N$ datových bodů. Vznikne soustava $Xw = Y$ s maticí příznaků $X \in \mathbb{R}^{N,p+1}$, kde $N \gg p+1$ — soustava je **přeurčená** a typicky **nemá řešení** ($Y \notin \operatorname{Im}X$). Rezignujeme na přesné řešení a hledáme $w$ minimalizující **součet kvadrátů reziduí** (RSS):
$$\operatorname{RSS}(w) = \sum_{i=1}^N (Y_i - w^T x_i)^2 = \|Y - Xw\|_2^2.$$

### 4.2 Řešení ve smyslu nejmenších čtverců

**Definice ([[Metoda-nejmenších-čtverců|řešení ve smyslu nejmenších čtverců]]).** Mějme $A \in \mathbb{R}^{m,n}$, $b \in \mathbb{R}^m$. Vektor $x \in \mathbb{R}^n$ nazveme **řešením soustavy $Ax = b$ ve smyslu nejmenších čtverců**, pokud
$$\|b - Ax\|_2 = \min_{y \in \mathbb{R}^n}\|b - Ay\|_2.$$
Je-li $x$ klasickým řešením soustavy, je $\|b-Ax\| = 0$ a nerovnost je splněna automaticky — proto pro řešitelnou soustavu množina řešení MNČ splývá s klasickou množinou řešení.

### 4.3 Geometrická interpretace — ortogonální projekce

Minimalizovat $\|b - Ax\|$ znamená najít v podprostoru $\operatorname{Im}A = \langle A_{:1},\dots,A_{:n}\rangle$ (lineární obal sloupců, sloupcový prostor) **nejbližší vektor k $b$**. Tím je **ortogonální projekce** $b$ na $\operatorname{Im}A$ (úloha o vzdálenosti bodu od podprostoru):

**Tvrzení (řešení a projekce).** $x$ je řešením $Ax = b$ ve smyslu nejmenších čtverců **právě tehdy, když**
$$Ax = \operatorname{proj}_{\operatorname{Im}A} b.$$

Tato soustava je **vždy řešitelná** (projekce leží v $\operatorname{Im}A$), takže řešení MNČ vždy existuje.

**Důsledek (jednoznačnost).** Řešení existuje **právě jedno** $\iff h(A) = n$ (sloupce LN). Je-li $h(A) < n$, je řešení nekonečně mnoho (dimenze $n - h(A)$).

### 4.4 Normální rovnice

**Věta (normální rovnice).** Mějme $A \in \mathbb{R}^{m,n}$, $b \in \mathbb{R}^m$. Pak $x$ je řešením $Ax = b$ ve smyslu nejmenších čtverců, právě když splňuje **normální rovnice**
$$A^T A\, x = A^T b.$$
Je-li navíc $h(A) = n$, lze řešení vyjádřit jako $x = (A^TA)^{-1}A^Tb$.

*Důkaz.* Označme $P = \operatorname{Im}A$. „$\Rightarrow$“ Je-li $x$ řešení MNČ, pak $Ax = \operatorname{proj}_P b$, takže reziduum
$$b - Ax = b - \operatorname{proj}_P b = \operatorname{proj}_{P^\perp} b$$
je **kolmé na každý sloupec** $A$. Proto $A^T(b - Ax) = \theta$ (řádek po řádku $A_{:i}\cdot(b-Ax) = 0$), odkud roznásobením $A^TAx = A^Tb$.
„$\Leftarrow$“ Platí-li $A^TAx = A^Tb$, pak $A^T(b-Ax) = \theta$, tedy $b - Ax \in P^\perp$. Pro libovolné $y$ pak z Pythagorovy věty $\|b - Ay\|^2 = \|b - Ax\|^2 + \|Ax - Ay\|^2 \ge \|b-Ax\|^2$, takže $x$ minimalizuje. Pro $h(A)=n$ je $h(A^TA)=n$, $A^TA$ regulární, odkud $x = (A^TA)^{-1}A^Tb$. $\square$

V regresním zápisu: $X^TX\,\hat{w}^{(\mathrm{OLS})} = X^TY$, resp. $\hat{w}^{(\mathrm{OLS})} = (X^TX)^{-1}X^TY$.

---

## 5. Řešení MNČ pomocí QR rozkladu

### 5.1 Vzorec $\hat{R}x = \hat{Q}^Tb$

Hlavní trik: jelikož $\hat{Q}$ obsahuje ve sloupcích ON bázi $\operatorname{Im}A$, platí pro ortogonální projekci
$$\operatorname{proj}_{\operatorname{Im}A} b = \hat{Q}\hat{Q}^T b.$$
Dosazením do podmínky $Ax = \operatorname{proj}_{\operatorname{Im}A}b$ s $A = \hat{Q}\hat{R}$:
$$\hat{Q}\hat{R}x = \hat{Q}\hat{Q}^T b.$$
Vynásobením $\hat{Q}^T$ zleva (a využitím $\hat{Q}^T\hat{Q} = E$) dostaneme **trojúhelníkovou soustavu**

$$\boxed{\;\hat{R}\,x = \hat{Q}^T b\;}$$

kterou vyřešíme **zpětnou substitucí**.

**Věta (řešení MNČ pomocí QR).** Mějme $A \in \mathbb{R}^{m,n}$, $b \in \mathbb{R}^m$, $h(A) = n$, a $A = QR = \hat{Q}\hat{R}$. Pak $x$ je řešení MNČ $\iff \hat{R}x = \hat{Q}^Tb$, a navíc pro minimální reziduum platí $\|b - Ax\| = \|Q'^Tb\|$, kde $Q = (\hat{Q}\ \ Q')$.

*Důkaz (idea druhé části).* Násobení OG maticí $Q^T$ nemění normu: $\|Ax - b\|^2 = \|Q^T(QRx - b)\|^2 = \|Rx - Q^Tb\|^2$. Blokovým zápisem $R = \begin{psmallmatrix}\hat{R}\\ \Theta\end{psmallmatrix}$, $Q^Tb = \begin{psmallmatrix}\hat{Q}^Tb \\ Q'^Tb\end{psmallmatrix}$ a Pythagorovou větou
$$\left\|\begin{psmallmatrix}\hat{R}x\\ \theta\end{psmallmatrix} - \begin{psmallmatrix}\hat{Q}^Tb\\ Q'^Tb\end{psmallmatrix}\right\|^2 = \|\hat{R}x - \hat{Q}^Tb\|^2 + \|Q'^Tb\|^2.$$
První člen minimalizujeme volbou $\hat{R}x = \hat{Q}^Tb$ (je nulový), druhý člen je konstantní = minimální reziduum. $\square$

Pro regresi: $\hat{R}\,\hat{w}^{(\mathrm{OLS})} = \hat{Q}^TY$ a $\min_w \operatorname{RSS}(w) = \|Q'^TY\|^2$.

### 5.2 Proč je QR stabilnější než normální rovnice

Sestavení a vyřešení normálních rovnic $A^TAx = A^Tb$ je rychlé, ale matice $A^TA$ má **číslo podmíněnosti rovné druhé mocnině** podmíněnosti $A$ ($\kappa(A^TA) = \kappa(A)^2$). Pro špatně podmíněné $A$ tak dochází k velké ztrátě přesnosti a výpočet $(A^TA)^{-1}$ je nestabilní. Cesta přes QR:

- nepoužívá $A^TA$ ani inverzi — pracuje jen s **ortogonálními** transformacemi, které normu (a tím zaokrouhlovací chyby) **nezvětšují** ($\kappa_2(Q) = 1$);
- soustava $\hat{R}x = \hat{Q}^Tb$ je trojúhelníková, řeší se zpětnou substitucí;
- podmíněnost úlohy zůstává $\kappa(A)$, nikoli $\kappa(A)^2$.

Proto je QR **standardní numericky stabilní metodou** pro výpočet odhadu metodou nejmenších čtverců (pro nejhůře podmíněné úlohy lze sáhnout po [[SVD]]). Cenou je ~2× více operací než normální rovnice — to je pro stabilitu přijatelné.

---

## Co je potřeba na zkoušku znát

### Definice
- **Ortogonální matice:** $Q^TQ = QQ^T = E$, tj. $Q^{-1} = Q^T$; matice s ON sloupci $Q^TQ = E_n$.
- **Redukovaný / úplný QR rozklad:** $A = \hat{Q}\hat{R}$ ($\hat{Q}$ ON sloupce, $\hat{R}$ horní trojúhelníková) / $A = QR$ ($Q$ ortogonální).
- **Householderův reflektor** $F = E - \tfrac{2}{\|v\|^2}vv^T$; **Givensova rotace** $G = \begin{psmallmatrix}c&s\\-s&c\end{psmallmatrix}$, $c = x_1/\|x\|$, $s = x_2/\|x\|$.
- **Řešení ve smyslu nejmenších čtverců:** minimalizuje $\|b - Ax\|_2$.

### Věty
- OG matice **zachovává skalární součin i normu**, $\det Q = \pm 1$, $|\lambda| = 1$, $\kappa_2(Q)=1$; součin OG matic je OG.
- **Existence** QR (každá $A$, $m\ge n$); **jednoznačnost** redukovaného při $h(A)=n$ a $r_{jj}>0$.
- **Normální rovnice:** $x$ řeší MNČ $\iff A^TAx = A^Tb$; geometricky $Ax = \operatorname{proj}_{\operatorname{Im}A}b$, reziduum $b - Ax \perp \operatorname{Im}A$.
- **Řešení MNČ pomocí QR:** $\hat{R}x = \hat{Q}^Tb$; minimální reziduum $\|Q'^Tb\|$; numericky stabilnější než $A^TA$.

### Algoritmy
- **Gramův–Schmidt** (klasický nestabilní / modifikovaný stabilní), $\sim 2mn^2$.
- **Householderova triangularizace** — vynulování celého sloupce zrcadlením, $2mn^2 - \tfrac{2}{3}n^3$, vhodná pro plné matice.
- **Givensova triangularizace** — vynulování jednoho prvku rotací, $\sim 3mn^2 - n^3$, vhodná pro řídké matice a paralelizaci.
- **Výpočet odhadu MNČ:** $A = QR \to \hat{R}x = \hat{Q}^Tb \to$ zpětná substituce.
