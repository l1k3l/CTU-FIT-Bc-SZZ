---
studyplan: true
etapa: "3 · LA1 / MA2 / LA2 — Petr"
qid: "7LA2"
examiner: "Petr"
topic: "SVD rozklad: definice, vlastnosti, výpočet"
readiness: nezačato
tags: [otázka, kurz/LA2, otázka/7, todo]
---

# Singulární rozklad (SVD)

> **Otázka SZZ:** SVD rozklad: definice, vlastnosti, výpočet.

Zdroje: BI-LA2 (Dombek, Kalvoda, Kleprlík, Klouda, FIT ČVUT), kap. 11 (SVD rozklad) — 11.2 Geometrický význam (str. 215), 11.3 Definice (str. 217), 11.4 SVD jako změna báze (str. 222), 11.5 SVD vs. rozklad pomocí vlastních čísel (str. 222), 11.6 SVD pomocí $A^TA$ (str. 224), 11.7 Aplikace (hodnost, podprostory, normy; str. 230), 11.8 Aproximace maticemi malé hodnosti (str. 233), 11.9 Inverze a pseudoinverze (str. 235), 11.10 Výpočet (str. 237).

Značení: $A \in \mathbb{R}^{m,n}$ matice, SVD $A = U\Sigma V^T$, singulární čísla $\sigma_i$, $U, V$ [[Ortogonální-matice|ortogonální]] matice, $E$ jednotková matice, $A^T$ transpozice, $h(A)$ hodnost, $\lVert\cdot\rVert$ norma, $\theta$ nulový vektor/vektor nul.

---

## 1. Geometrický význam

Matici $A \in \mathbb{R}^{m,n}$ odpovídá lineární zobrazení $A : x \mapsto Ax$ z $\mathbb{R}^n$ do $\mathbb{R}^m$. Uvažujme jednotkovou sféru $S = \{x \in \mathbb{R}^n : \lVert x\rVert_2 = 1\}$. Jejím obrazem $AS$ je **hyperelipsa** (zobecnění elipsy).

Tuto hyperelipsu lze popsat:

- **ortonormálními směry** hlavních poloos $u_1, \dots, u_m$ (jednotkové vektory v $\mathbb{R}^m$),
- a koeficienty $\sigma_1, \dots, \sigma_m \ge 0$, které říkají, **kolikrát** se jednotková sféra v daných směrech natáhla či zmenšila.

Vektory $\sigma_1 u_1, \dots, \sigma_m u_m$ jsou pak hlavní poloosy hyperelipsy. Obvykle je řadíme podle velikosti $\sigma_1 \ge \sigma_2 \ge \cdots \ge 0$ a nazýváme **singulární čísla**.

Vzory hlavních poloos (na sféře $S$) tvoří ortonormální soubor $v_1, \dots, v_n$ (**pravé singulární vektory**); jejich obrazy mají směr $u_j$ a velikost $\sigma_j$, tedy
$$A v_j = \sigma_j u_j \quad (\forall j). \tag{11.1}$$

Maticově (pro $j = 1, \dots, n$, případ $m \ge n$): $A \big(v_1 \mid \cdots \mid v_n\big) = \big(u_1 \mid \cdots \mid u_n\big) \hat\Sigma$, tedy $AV = \hat U \hat\Sigma$, odkud vynásobením $V^T$ zprava
$$A = \hat U \hat\Sigma V^T.$$

---

## 2. Definice SVD

Pojem zavádíme přes **[[SVD|singulární rozklad]]**. Geometrie dala redukovaný tvar; doplněním na ortogonální matice vznikne plný tvar.

### 2.1 Redukovaný (úsporný) SVD

**Definice 11.1 (redukovaný / *reduced (thin)* SVD).** Redukovaným SVD rozkladem matice $A \in \mathbb{R}^{m,n}$, kde $m \ge n$, rozumíme zápis
$$A = \hat U \hat\Sigma V^T,$$
kde

- $\hat U \in \mathbb{R}^{m,n}$ má **ortonormální sloupce** (levé singulární vektory),
- $\hat\Sigma \in \mathbb{R}^{n,n}$ je diagonální s **nezápornou klesající** diagonálou,
- $V \in \mathbb{R}^{n,n}$ je **[[Ortogonální-matice|ortogonální]]** (pravé singulární vektory ve sloupcích).

Prvky $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_n \ge 0$ na diagonále $\hat\Sigma$ jsou **singulární čísla** $A$ (mohou se opakovat — vícenásobné singulární číslo).

### 2.2 Plný (úplný) SVD

**Definice 11.2 (úplný / *full* SVD).** Úplným SVD rozkladem matice $A \in \mathbb{R}^{m,n}$ je její zápis
$$\boxed{\,A = U \Sigma V^T\,},$$
kde

- $U \in \mathbb{R}^{m,m}$ je [[Ortogonální-matice|ortogonální]] matice,
- $\Sigma \in \mathbb{R}^{m,n}$ je diagonální matice (tj. $\Sigma_{ij} = 0$ pro $i \neq j$; připouštíme i nečtvercové „diagonální" matice) s nezápornou klesající diagonálou,
- $V \in \mathbb{R}^{n,n}$ je [[Ortogonální-matice|ortogonální]] matice.

Na diagonále $\Sigma$ je $p := \min(m,n)$ singulárních čísel $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_p \ge 0$.

**Vztah obou tvarů.** Pro $m = n$ tvary splývají. Je-li $m > n$, doplníme $\hat\Sigma$ o nulové řádky a $\hat U$ o sloupce tak, aby vznikla ortogonální $U$; je-li $m < n$, doplníme $\Sigma$ o nulové sloupce a $\hat V$ na ortogonální. Doplňované sloupce musí být kolmé k již spočteným (zachování ortonormality).

### 2.3 Existence

**Věta 11.1 (o existenci SVD).** Každá matice $A \in \mathbb{R}^{m,n}$ má úplný (a tedy i redukovaný) SVD rozklad.

*Důkaz (idea — indukcí přes geometrii).* Stačí $n \le m$ (jinak vezmeme rozklad $A^T$ a odtransponujeme). Postupujeme indukcí podle rozměru.

Položme $\sigma_1 := \lVert A\rVert_2$ (matice 2-[[Norma|norma]]; je nabytá, takže existuje $v_1$ s $\lVert v_1\rVert_2 = 1$ a $\lVert A v_1\rVert_2 = \sigma_1$). Zvolme $u_1$ s $\lVert u_1\rVert_2 = 1$ a $A v_1 = \sigma_1 u_1$. Doplníme $v_1$ na ortonormální bázi $\mathbb{R}^n$ (matice $V_1$) a $u_1$ na ortonormální bázi $\mathbb{R}^m$ (matice $U_1$). Pak
$$U_1^T A V_1 = \begin{pmatrix} \sigma_1 & w^T \\ \theta & B \end{pmatrix} =: S.$$
Pro $n = 1$ je hotovo. Jinak se z vlastnosti 2-normy ukáže $w = \theta$: platí
$$\lVert S\rVert_2 \left\lVert \binom{\sigma_1}{w}\right\rVert_2 \ge \left\lVert S \binom{\sigma_1}{w}\right\rVert_2 = \left\lVert \binom{\sigma_1^2 + w^T w}{Bw}\right\rVert_2 \ge \sigma_1^2 + w^T w = \sqrt{\sigma_1^2 + w^T w}\,\left\lVert\binom{\sigma_1}{w}\right\rVert_2,$$
takže $\lVert S\rVert_2 \ge \sqrt{\sigma_1^2 + w^T w}$. Protože $U_1, V_1$ ortogonální, je $\lVert S\rVert_2 = \lVert A\rVert_2 = \sigma_1$, tedy $\sigma_1 \ge \sqrt{\sigma_1^2 + w^T w}$, což jde jen pro $w = \theta$. Na zbytek $B$ aplikujeme indukční předpoklad ($B = U_2 \Sigma_2 V_2^T$) a poskládáme
$$A = U_1 \begin{pmatrix} 1 & 0 \\ 0 & U_2 \end{pmatrix} \begin{pmatrix} \sigma_1 & \theta^T \\ \theta & \Sigma_2 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & V_2 \end{pmatrix}^T V_1^T = U\Sigma V^T. \qquad \square$$

(Alternativní důkaz přes $A^T A$ je v části 5.)

---

## 3. SVD jako změna báze

SVD říká, že každou matici lze „diagonalizovat", připustíme-li **dvě různé** ortonormální báze (vlevo jinou než vpravo). Vezmeme $\mathcal{X}$ = báze $\mathbb{R}^n$ tvořenou sloupci $V$ a $\mathcal{Y}$ = báze $\mathbb{R}^m$ tvořenou sloupci $U$. Pak vzhledem k těmto bázím působí $A$ jen jako diagonální matice $\Sigma$ (škálování ve směrech). Výpočet obrazu $Ax$ proběhne ve třech krocích:

1. souřadnice ve vstupní bázi: $(x)_{\mathcal{X}} = V^T x$;
2. přeškálování složek: vynásobit $\sigma_1, \dots, \sigma_n$, tj. $\Sigma V^T x$;
3. zpět do standardní báze: vynásobit $U$, tedy $Ax = U\Sigma V^T x$.

Na rozdíl od diagonalizace pomocí jedné báze ([[Diagonalizace]]) jsou **obě** báze ortonormální.

---

## 4. SVD vs. rozklad pomocí vlastních čísel (spektrální rozklad)

Rozklad $A = U\Sigma V^T$ připomíná **[[Diagonalizace|diagonalizaci]]** / **[[Spektrální-rozklad|spektrální rozklad]]** $A = PDP^{-1}$, ale liší se:

| | spektrální rozklad | SVD |
|---|---|---|
| báze | **jedna** sada vektorů ($P$), nemusí být ortogonální | **dvě** ortonormální sady ($U$, $V$) |
| matice | jen **čtvercové** | **libovolné** $m \times n$ |
| existence | ne vždy | **vždy** |
| diagonála | vlastní čísla (mohou být záporná/komplexní) | singulární čísla $\sigma_i \ge 0$ |

### Symetrická matice — vztah obou rozkladů

**Tvrzení 11.1 (SVD symetrické matice).** Pro symetrickou $A \in \mathbb{R}^{n,n}$ jsou její singulární čísla **absolutní hodnoty** vlastních čísel; levé i pravé singulární vektory tvoří ortonormální soubory z vlastních vektorů.

*Důkaz (idea).* Ze spektrálního rozkladu symetrické matice $A = PDP^T$ ($P$ ortogonální, $D$ diagonální) přeřadíme diagonálu tak, aby $|d_{11}| \ge \cdots \ge |d_{nn}|$. Pak
$$A = P D P^T = P\,|D|\,\operatorname{sgn}(D)\,P^T,$$
což je SVD s $U = P$, $\Sigma = |D|$, $V^T = \operatorname{sgn}(D) P^T$. Znaménka lze případně přesunout do $U$. $\square$

Rozklady jsou tedy **stejné, právě když** jsou všechna vlastní čísla nezáporná.

---

## 5. SVD pomocí $A^TA$ — vztah k vlastním číslům

Singulární čísla obecné matice úzce souvisejí s **[[Vlastní-číslo|vlastními čísly]]** symetrických matic $A^T A$ a $A A^T$.

**Tvrzení 11.2 (o singulárních číslech pomocí $A^TA$).** Nenulová singulární čísla $A \in \mathbb{R}^{m,n}$ jsou rovna odmocninám z nenulových vlastních čísel matice $A^T A$ (i $A A^T$), přičemž vlastní číslo se vyskytuje tolikrát, kolik je jeho násobnost. Sloupce $V$ jsou tvořeny ortonormální bází z vlastních vektorů $A^T A$; sloupce $U$ ortonormální bází z vlastních vektorů $A A^T$.

*Důkaz.* Dosadíme $A = U\Sigma V^T$:
$$A^T A = (U\Sigma V^T)^T U\Sigma V^T = V\Sigma^T U^T U \Sigma V^T = V (\Sigma^T \Sigma) V^T. \tag{11.32}$$
To je [[Diagonalizace|diagonalizace]] matice $A^T A$ ortogonální maticí $V$: na diagonále $\Sigma^T\Sigma \in \mathbb{R}^{n,n}$ jsou $\sigma_1^2, \dots, \sigma_p^2$ a případně nuly. Vlastní čísla diagonální matice jsou přímo prvky diagonály, tedy nenulová singulární čísla jsou odmocniny z nenulových vlastních čísel $A^T A$. Pro $A A^T = U(\Sigma\Sigma^T)U^T$ analogicky. $\square$

Konkrétně pro pravé singulární vektory: $A^T A\, v_i = V(\Sigma^T\Sigma)V^T v_i = V(\Sigma^T\Sigma)e_i = \sigma_i^2 v_i$, tj. $v_i$ je vlastní vektor $A^T A$ k vlastnímu číslu $\sigma_i^2$ (pro nulová $\sigma_i$ je $A^T A v_i = \theta$).

**Důsledky tohoto tvrzení:** jednoznačnost singulárních čísel; návod na výpočet (část 8); a alternativní důkaz existence ($A^T A$ je symetrická a pozitivně semidefinitní, takže má ortonormální bázi vlastních vektorů a nezáporná vlastní čísla — odmocniny dají $\Sigma$).

---

## 6. Vlastnosti SVD

### 6.1 Hodnost

**Tvrzení 11.3 (hodnost pomocí SVD).** Je-li $r$ počet nenulových singulárních čísel $A$, pak $h(A) = r$.

*Důkaz.* Násobení [[Ortogonální-matice|ortogonální]] (regulární) maticí nemění **[[Hodnost-matice|hodnost]]**, takže $h(A) = h(U\Sigma V^T) = h(\Sigma)$. Matice $\Sigma$ je v horním stupňovitém tvaru a má právě $r$ nenulových řádků. $\square$

> **Poznámka (numerická hodnost).** Výpočet hodnosti je numericky nestabilní. Proto se zavádí $h_{\mathrm{num}}(A) := $ počet singulárních čísel větších než zafixované malé $\varepsilon > 0$. Odstranění malých $\sigma_i$ (vzniklých šumem/zaokrouhlením) dává „stabilní část" matice.

### 6.2 Podprostory — báze obrazu a jádra

**Tvrzení 11.4 (SVD a původní matice).** Pro $A \in \mathbb{R}^{m,n}$ s $r$ nenulovými singulárními čísly:

1. lineární obal sloupců $A$ = $\langle u_1, \dots, u_r\rangle$ (obor hodnot zobrazení $A$);
2. lineární obal řádků $A$ = $\langle v_1^T, \dots, v_r^T\rangle$;
3. $\ker A$ (řešení $Ax = \theta$) = $\langle v_{r+1}, \dots, v_n\rangle$;
4. $\ker A^T$ (řešení $A^T x = \theta$) = $\langle u_{r+1}, \dots, u_m\rangle$.

*Důkaz (bodů 1, 3).* Pro pravý singulární vektor $v_i$ je $V^T v_i = e_i$, tedy $\Sigma V^T v_i = \Sigma e_i = \sigma_i e_i$ (resp. $\theta$ pro $i > r$), a tak
$$A v_i = U\Sigma V^T v_i = \begin{cases} \sigma_i u_i & i \le r, \\ \theta & i > r. \end{cases}$$
Obor hodnot $A(\mathbb{R}^n) = A(\langle v_1, \dots, v_n\rangle) = \langle Av_1, \dots, Av_r\rangle = \langle u_1, \dots, u_r\rangle$ (posledních $n-r$ obrazů je nulových). Vektory $v_{r+1}, \dots, v_n$ se zobrazí na $\theta$, je jich $n - r$ a jsou lineárně nezávislé; jelikož $\dim\ker A = n - h(A) = n - r$, tvoří bázi jádra. $\square$

ON báze obrazu (= $u_1, \dots, u_r$) a jádra (= $v_{r+1}, \dots, v_n$) získáme tedy z SVD přímo.

### 6.3 Normy

**Tvrzení 11.6 (norma matice a SVD).** Pro $A$ s nenulovými singulárními čísly $\sigma_1, \dots, \sigma_r$ platí
$$\lVert A\rVert_2 = \sigma_1, \qquad \lVert A\rVert_F = \sqrt{\sigma_1^2 + \sigma_2^2 + \cdots + \sigma_r^2}.$$

*Důkaz.* Násobení ortogonální maticí nemění tyto **[[Norma|normy]]**, takže $\lVert A\rVert_2 = \lVert U\Sigma V^T\rVert_2 = \lVert\Sigma\rVert_2 = \sigma_1$ (2-norma diagonální matice je největší prvek). Pro Frobeniovu normu analogicky $\lVert A\rVert_F = \lVert\Sigma\rVert_F = \sqrt{\sum \sigma_i^2}$. $\square$

### 6.4 Jednoznačnost

**Věta 11.2 (jednoznačnost SVD).** Pro $A$ a $k = \min(m,n)$ jsou singulární čísla $\sigma_1, \dots, \sigma_k$ určena jednoznačně (jsou to vlastní čísla $A^T A$). Je-li $\sigma_i$ **jednoduché** (různé od ostatních) a nenulové, je pravý singulární vektor $v_i$ určen jednoznačně **až na znaménko**; odpovídající $u_i$ je pak určen jednoznačně.

---

## 7. Aproximace maticemi malé hodnosti (Eckartova–Youngova věta)

SVD dává **optimální** aproximaci matice maticí nižší hodnosti.

**Tvrzení 11.7 (rozklad na matice hodnosti 1).** Matici $A$ s $r$ nenulovými singulárními čísly lze zapsat jako součet $r$ matic hodnosti 1:
$$A = \sum_{j=1}^r \sigma_j u_j v_j^T. \tag{11.71}$$

*Důkaz (idea).* Rozepíšeme $\Sigma = \sum_{j=1}^r \Sigma_j$, kde $\Sigma_j = \sigma_j e_j^{(m)}(e_j^{(n)})^T$ má $\sigma_j$ jen na $j$-té pozici diagonály. Pak $U\Sigma_j V^T = \sigma_j u_j v_j^T$, takže $A = U\Sigma V^T = \sum_j \sigma_j u_j v_j^T$. $\square$

Pro $1 \le \nu \le r$ definujeme **ořezání** (ponechání $\nu$ největších singulárních čísel)
$$A_\nu := \sum_{j=1}^\nu \sigma_j u_j v_j^T = U \Sigma_\nu V^T,$$
kde $\Sigma_\nu$ má na diagonále $\sigma_1, \dots, \sigma_\nu, 0, \dots, 0$.

**Tvrzení 11.8 (Eckartova–Youngova věta — optimalita aproximace).** Pro $A_\nu$ jako výše platí
$$\lVert A - A_\nu\rVert_2 = \sigma_{\nu+1} = \inf_{\substack{B \in \mathbb{R}^{m,n} \\ h(B) \le \nu}} \lVert A - B\rVert_2,$$
kde dodefinujeme $\sigma_{\nu+1} = 0$, má-li $A$ jen $\nu$ singulárních čísel. (Analogicky pro Frobeniovu normu: $\lVert A - A_\nu\rVert_F = \sqrt{\sigma_{\nu+1}^2 + \cdots + \sigma_r^2}$.) Tedy $A_\nu$ je **nejlepší** aproximace matice $A$ maticí hodnosti $\le \nu$ v 2-normě.

*Důkaz (idea).* **První rovnost:** $A - A_\nu = U(\Sigma - \Sigma_\nu)V^T$; násobení ortogonální maticí nemění 2-normu, $\Sigma - \Sigma_\nu$ je diagonální s největším prvkem $\sigma_{\nu+1}$, tedy $\lVert A - A_\nu\rVert_2 = \sigma_{\nu+1}$. **Optimalita (sporem):** kdyby existovala $B$, $h(B) \le \nu$, s $\lVert A - B\rVert_2 < \sigma_{\nu+1}$, je $\ker B$ podprostor $W$ dimenze $\ge n - \nu$, na němž $\lVert Aw\rVert_2 = \lVert(A-B)w\rVert_2 < \sigma_{\nu+1}\lVert w\rVert_2$. Naopak na podprostoru $V_0 = \langle v_1, \dots, v_{\nu+1}\rangle$ (dimenze $\nu+1$) platí $\lVert Av\rVert_2 \ge \sigma_{\nu+1}\lVert v\rVert_2$. Součet dimenzí $W$ a $V_0$ je $> n$, takže existuje nenulový $z \in W \cap V_0$, pro nějž současně $\sigma_{\nu+1}\lVert z\rVert_2 \le \lVert Az\rVert_2 < \sigma_{\nu+1}\lVert z\rVert_2$ — spor. $\square$

**Využití:** komprese dat (obrazy, signály), potlačení šumu, redukce dimenze, doporučovací systémy — patří mezi základní nástroje numerické matematiky a strojového učení.

---

## 8. Inverze a pseudoinverze

### 8.1 Inverze regulární matice

Pro regulární $A \in \mathbb{R}^{n,n}$ s SVD $A = U\Sigma V^T$ je $\Sigma$ regulární diagonální a
$$A^{-1} = V \Sigma^{-1} U^T, \qquad \Sigma^{-1} = \operatorname{diag}(\sigma_1^{-1}, \dots, \sigma_n^{-1}). \tag{11.86}$$
(Toto **ještě není** SVD rozklad $A^{-1}$ — diagonála $\Sigma^{-1}$ je rostoucí.) Největší singulární číslo $A^{-1}$ je $\sigma_n^{-1}$, odkud **číslo podmíněnosti** $\kappa(A) = \sigma_1/\sigma_n$; $\kappa(A) = 1$ v 2-normě právě tehdy, když je $A$ násobkem ortogonální matice.

### 8.2 Moore–Penroseova pseudoinverze

Invertováním pouze **nenulových** singulárních čísel získáme pro $A \in \mathbb{R}^{m,n}$ s $r$ nenulovými $\sigma$ **pseudoinverzi**
$$A^+ = V \Sigma^+ U^T = \sum_{j=1}^r \sigma_j^{-1} v_j u_j^T,$$
kde $\Sigma^+ \in \mathbb{R}^{n,m}$ má na diagonále $\sigma_1^{-1}, \dots, \sigma_r^{-1}, 0, \dots$. Je to zobecnění inverze i pro singulární / nečtvercové matice.

**Tvrzení 11.10 (vlastnosti pseudoinverze).** $A A^+ A = A$; $A^+ A A^+ = A^+$; $(A A^+)^T = A A^+$; $(A^+ A)^T = A^+ A$. (Tyto čtyři Penroseovy podmínky $A^+$ jednoznačně určují.)

Pseudoinverze řeší úlohu **[[Metoda-nejmenších-čtverců|nejmenších čtverců]]** $\min_x \lVert Ax - b\rVert_2$: řešení s nejmenší normou je $x = A^+ b$.

---

## 9. Výpočet SVD rozkladu

### 9.1 Ruční výpočet (malé matice) — přes $A^TA$

Pro malé matice se podle Tvrzení 11.2 počítá z diagonalizace symetrické matice $A^T A$ (nebo $A A^T$ — vybíráme tu menší).

**Postup 11.1 (výpočet úplného SVD pomocí $A^TA$).** Pro $A \in \mathbb{R}^{m,n}$:

1. cílem je rovnost $A^T A = V(\Sigma^T\Sigma)V^T$ (vhodná diagonalizace $A^T A$);
2. spočítej $A^T A$;
3. spočítej její [[Vlastní-číslo|vlastní čísla]] (každé tolikrát, kolik je násobnost), seřaď je sestupně; nenulová singulární čísla jsou jejich odmocniny — vlož je na diagonálu $\Sigma \in \mathbb{R}^{m,n}$, zbytek nuly;
4. spočítej **ortonormální** báze vlastních podprostorů pro jednotlivá vlastní čísla — tyto vektory tvoří sloupce $V$ (pravé singulární vektory $v_1, \dots, v_n$);
5. levé singulární vektory pro nenulová $\sigma_j$ dopočítej z $AV = U\Sigma$, tj. $A v_j = \sigma_j u_j \Rightarrow u_j = \tfrac{1}{\sigma_j} A v_j$;
6. chybějící sloupce $U$ (k nulovým $\sigma$) doplň na ortonormální bázi — libovolná ON báze ortogonálního doplňku již spočtených $u_j$.

(Symetricky lze počítat přes $A A^T$ — Postup 11.2 — a sloupce $V$ dopočítat z $U^T A = \Sigma V^T$, tj. $v_j = \tfrac{1}{\sigma_j} A^T u_j$. Volíme tu z matic $A^T A$ / $A A^T$, která je menší.)

> **Pozor:** vlastní vektory ke stejnému vlastnímu číslu (násobnému) nebo k nule nemusí vyjít navzájem ortogonální — je třeba spočítat **ortonormální bázi** podprostoru (např. Gram–Schmidtem), ne jen znormalizovat.

**Příklad (z učebnice).** Pro $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \\ -1 & -2 \\ 1 & 2 \end{pmatrix}$ je $A^T A = \begin{pmatrix} 7 & 14 \\ 14 & 28\end{pmatrix}$ s vlastními čísly $35$ a $0$. Singulární čísla jsou $\sqrt{35}$ a $0$; $v_1 = \tfrac{1}{\sqrt5}(1,2)$, $v_2 = \tfrac{1}{\sqrt5}(2,-1)$; $u_1 = \tfrac{1}{\sqrt{35}} A v_1 = \tfrac{1}{\sqrt7}(1,2,-1,1)$, zbylé sloupce $U$ se doplní na ON bázi.

### 9.2 Numerický výpočet (velké matice)

Výpočet přes $A^T A$ je numericky nepřesný (umocnění zvětší chybu u nejmenších $\sigma$). Pro větší matice se SVD počítá podobně jako vlastní čísla, ve **dvou fázích**:

1. **Bidiagonalizace (přímá fáze).** Matici převedeme na bidiagonální tvar **Golubovou–Kahanovou bidiagonalizací** — zleva i zprava násobíme [[Ortogonální-matice|ortogonálními]] (Householderovými) maticemi $A = Q B \tilde Q$. Podle **Tvrzení 11.11** násobení ortogonálními maticemi zachovává singulární čísla (z SVD $B = \tilde U\Sigma\tilde V^T$ plyne $A = Q\tilde U\,\Sigma\,\tilde V^T\tilde Q$, což je SVD $A$).
2. **Iterační fáze.** Bidiagonální matici převedeme na diagonální iteračním algoritmem — varianta **QR algoritmu** nebo **divide-and-conquer**.

---

## Co je potřeba na zkoušku znát

### Definice
- **SVD:** $A = U\Sigma V^T$, $A \in \mathbb{R}^{m,n}$; $U \in \mathbb{R}^{m,m}$, $V \in \mathbb{R}^{n,n}$ ortogonální, $\Sigma \in \mathbb{R}^{m,n}$ diagonální s $\sigma_1 \ge \cdots \ge \sigma_p \ge 0$ ($p = \min(m,n)$).
- Singulární čísla $\sigma_i$; levé ($u_i$, sloupce $U$) a pravé ($v_i$, sloupce $V$) singulární vektory; $A v_i = \sigma_i u_i$.
- Plný vs. redukovaný (úsporný) tvar.

### Klíčové věty a vlastnosti
- **Existence:** každá $A$ má SVD (důkaz indukcí přes 2-normu, nebo přes $A^T A$).
- **Vztah k vlastním číslům:** $\sigma_i = \sqrt{\lambda_i(A^T A)}$; $V$ z vl. vektorů $A^T A$, $U$ z vl. vektorů $A A^T$.
- **Hodnost** $h(A) = r$ = počet nenulových $\sigma_i$.
- **Normy:** $\lVert A\rVert_2 = \sigma_1$, $\lVert A\rVert_F = \sqrt{\sum \sigma_i^2}$.
- Báze: $\operatorname{Im} A = \langle u_1,\dots,u_r\rangle$, $\ker A = \langle v_{r+1},\dots,v_n\rangle$.
- **Eckart–Young:** $A_\nu = \sum_{j\le\nu}\sigma_j u_j v_j^T$ je nejlepší aproximace hodnosti $\le\nu$ v 2-normě, $\lVert A - A_\nu\rVert_2 = \sigma_{\nu+1}$.
- **Pseudoinverze** $A^+ = V\Sigma^+ U^T$; pro regulární $A$ je $A^{-1} = V\Sigma^{-1}U^T$, $\kappa(A) = \sigma_1/\sigma_n$.

### Výpočet
- **Ručně:** diagonalizuj $A^T A$ (či $A A^T$, tu menší) → $\sigma_i = \sqrt{\lambda_i}$, $V$ z ON bází vl. podprostorů, $u_j = \tfrac{1}{\sigma_j}Av_j$, zbytek $U$ doplnit na ON bázi.
- **Numericky:** Golubova–Kahanova bidiagonalizace + iterační (QR / divide-and-conquer); přes $A^T A$ se pro velké matice nepočítá (chyba).
