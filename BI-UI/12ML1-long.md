---
studyplan: true
etapa: "4 · ML1 / ML2 — Dedecius + Holeňa"
qid: "12ML1"
examiner: "Dedecius"
topic: "Logistická regrese, binární klasifikace, trénování jako MLE"
readiness: nezačato
tags: [otázka, kurz/ML1, otázka/12, todo]
---

# Logistická regrese

> **Otázka SZZ:** Logistická regrese – sestavení modelu pro binární klasifikaci, trénování jako MLE odhad.

Zdroje: BI-ML1 (FIT ČVUT), přednáška 7 — kap. 25 Problém klasifikace, kap. 26 Základní myšlenka logistické regrese (sigmoida), kap. 27 Učení modelu (MLE), kap. 28 Závěrečné poznámky, kap. 29 Metoda gradientního vzestupu; printed str. 49–56.

Značení: $Y \in \{0,1\}$ binární vysvětlovaná proměnná, $X_1,\dots,X_p$ příznaky, $x = (x_0, x_1,\dots,x_p)^T$ vektor hodnot příznaků s **interceptem** $x_0 = 1$, $w = (w_0, w_1,\dots,w_p)^T$ vektor koeficientů (parametrů), $\sigma$ sigmoida, $\hat{p} = \mathrm{P}(Y=1 \mid x, w)$ odhad pravděpodobnosti, $N$ počet trénovacích bodů, $\mathbf{X} \in \mathbb{R}^{N, p+1}$ matice příznaků, $\boldsymbol{Y} = (Y_1,\dots,Y_N)^T$ vektor vysvětlovaných hodnot, $L$ věrohodnostní funkce, $\ell = \ln L$ log-věrohodnost.

---

## 1. Sestavení modelu pro binární klasifikaci

### 1.1 Problém klasifikace vs. regrese

Přestože se metoda **[[Logistická-regrese|logistická regrese]]** jmenuje tak, jak se jmenuje, je to metoda určená pro **klasifikaci** — nikoli pro regresi. Rozdíl mezi oběma úlohami spočívá v oboru hodnot vysvětlované proměnné $Y$:

- **regrese** — $Y$ je spojitá, hledá se závislost ve tvaru připomínajícím klasické funkce z analýzy (např. **[[Lineární-regrese|lineární regrese]]** hledá $Y \approx w_0 + w_1 x_1 + \dots + w_p x_p$);
- **klasifikace** — $Y$ nabývá jen několika málo hodnot; u funkcí, jejichž obor hodnot je konečná (zde dvouprvková) množina, je třeba použít nějaký „trik“.

**Omezení na binární klasifikaci.** Uvažujeme jen případ, kdy $Y$ nabývá hodnoty buď $0$, nebo $1$ (např. „osoba má rýmičku“ $Y=1$ vs. „nemá“ $Y=0$).

### 1.2 Cíl: predikovat pravděpodobnost místo třídy

Logistická regrese stojí na triku, který z **diskrétního** problému dělá **spojitý**: místo hodnoty $Y \in \{0,1\}$ se snažíme predikovat **pravděpodobnost**, že $Y$ má hodnotu $1$, tj. číslo z intervalu $[0,1]$. Hledáme tedy funkční předpis, který pro dané hodnoty příznaků $x$ a koeficientů $w$ vrátí číslo
$$\mathrm{P}(Y = 1 \mid x, w) \in [0,1],$$
což je odhad pravděpodobnosti, že daný datový bod patří do třídy $1$. Protože součet pravděpodobností obou tříd musí být $1$, stačí najít model pro $\mathrm{P}(Y=1 \mid x, w)$ a druhou pravděpodobnost dopočítat:
$$\mathrm{P}(Y = 0 \mid x, w) = 1 - \mathrm{P}(Y = 1 \mid x, w).$$

### 1.3 Lineární kombinace a sigmoida

Stejně jako u lineární regrese konstruujeme rozhodnutí pomocí **lineární kombinace příznaků** $w^T x = w_0 + w_1 x_1 + \dots + w_p x_p$ (s interceptem $x_0 = 1$). Tato lineární kombinace ovšem nabývá libovolných reálných hodnot, kdežto pravděpodobnost musí ležet v $[0,1]$. Proto výraz $w^T x$ **dosadíme do vhodně zvolené funkce**, jejíž obor hodnot je podmnožinou $[0,1]$. Obvyklou volbou je **sigmoida** (angl. *sigmoid function*, speciální případ logistické funkce):
$$\sigma(z) = \frac{e^z}{1 + e^z} = \frac{1}{1 + e^{-z}}.$$

**Vlastnosti sigmoidy.**

- definiční obor $\mathbb{R}$ (lze dosadit libovolné $w^T x$);
- obor hodnot **otevřený** interval $(0,1)$ — nikdy nenastane jistý jev (pravděpodobnost $1$) ani nemožný jev (pravděpodobnost $0$);
- $\sigma$ je ostře rostoucí na $\mathbb{R}$, tedy **prostá**, s inverzí $\sigma^{-1}(x) = \ln \frac{x}{1-x}$;
- $\lim_{z\to-\infty}\sigma(z) = 0$, $\lim_{z\to+\infty}\sigma(z) = 1$, $\sigma(0) = \tfrac12$, funkce $\sigma(z) - \tfrac12$ je lichá;
- pro doplňkovou třídu platí $1 - \sigma(z) = \dfrac{1}{1 + e^{z}}$.

### 1.4 Model logistické regrese

**Definice (model logistické regrese pro binární klasifikaci).** Mějme binární $Y$ s hodnotami $0,1$ a $p$ příznaků $X_1,\dots,X_p$ s konstantním $X_0 = 1$. Model pro odhad pravděpodobnosti pro dané $x = (x_0,\dots,x_p)$ a koeficienty $w = (w_0,\dots,w_p)$ má tvar
$$\boxed{\;\mathrm{P}(Y = 1 \mid x, w) = \sigma(w^T x) = \frac{e^{w^T x}}{1 + e^{w^T x}}\;}, \qquad \mathrm{P}(Y = 0 \mid x, w) = 1 - \sigma(w^T x) = \frac{1}{1 + e^{w^T x}}.$$

**Rozhodovací pravidlo (predikce).** Pro daná data $x$ se spočítá odhad $\hat{p} = \mathrm{P}(Y=1 \mid x, w)$ a rozhodne se podle prahu $\tfrac12$:
$$\hat{Y} = \mathbb{1}\!\left[\hat{p} > \tfrac12\right] = \begin{cases} 1 & \hat{p} > \tfrac12, \\ 0 & \hat{p} \le \tfrac12. \end{cases}$$

*Příklad (rýmička).* Pro $w = (0.1, -0.3, -0.2, 0.2)$ a $x = (1, 0, 35, 37.2)$ je $w^T x = 0.54$, tedy $\hat{p} = \sigma(0.54) = \tfrac{e^{0.54}}{1+e^{0.54}} \doteq 0.632 > \tfrac12$, takže model rozhodne $\hat{Y} = 1$ (osoba rýmičku pravděpodobně má).

### 1.5 Rozhodovací hranice — logit a linearita

Každý datový bod je bodem v $\mathbb{R}^p$. **Hranice rozhodnutí** mezi třídami je dána rovnicí $\hat{p} = \tfrac12$:
$$\frac{e^{w^T x}}{1 + e^{w^T x}} = \frac12.$$
Protože $\sigma(z) = \tfrac12 \iff z = 0$, řešením je
$$w^T x = w_0 + w_1 x_1 + \dots + w_p x_p = 0,$$
což je **nadrovina** (angl. *hyperplane*) v $\mathbb{R}^p$, jazykem lineární algebry afinní (lineární) varieta dimenze $p-1$. Logistická regrese má tedy **lineární rozhodovací hranici**.

Totéž lze nahlédnout přes **logit** (log-odds). Aplikací inverzní funkce $\sigma^{-1}$ na model dostaneme
$$\operatorname{logit}\hat{p} = \ln \frac{\hat{p}}{1 - \hat{p}} = w^T x,$$
tj. logaritmus poměru šancí je lineární funkcí příznaků. Práh $\hat{p} = \tfrac12$ odpovídá $\frac{\hat p}{1-\hat p} = 1$, tedy logitu $0$, tedy $w^T x = 0$ — opět nadrovina.

---

## 2. Trénování jako MLE odhad

Model víme vyhodnotit, pokud známe $w$; zatím ale nevíme, jak se $w$ určí z **trénovacích dat**, u nichž známe vedle příznaků i hodnoty $Y$. U modelů, které odhadují přímo hodnotu $Y$ (jako lineární regrese), se volí míra chyby a parametry se hledají tak, aby chybu minimalizovaly. U logistické regrese ale odhadujeme **pravděpodobnosti** hodnot $Y$, takže měřit chybu je obtížné — postupuje se jinak: parametry $w$ odhadneme metodou **MLE** (**[[Maximální-věrohodnost|maximálně věrohodný odhad]]**, angl. *maximum likelihood estimate*).

### 2.1 Myšlenka MLE (na jednoduchém příkladě házení mincí)

Mějme minci, kterou házíme; náhodná veličina $Y$ má hodnotu $1$ (hlava), nebo $0$ (orel). Mince nemusí být férová, neznámý parametr je $p = \mathrm{P}(Y=1)$. V $10$ hodech padne $7\times$ jednička a $3\times$ nula. Naučit model = odhadnout $p$.

Pro každou hodnotu $p$ umíme spočítat pravděpodobnost, s jakou by tato trénovací data padla (Bernoulliho/binomický model): pro férovou minci $p=\tfrac12$ je $\left(\tfrac12\right)^7\left(\tfrac12\right)^3 \doteq 0.00098$, pro $p = 0.6$ je $0.6^7(1-0.6)^3 \doteq 0.00179$ — vyšší, tedy $p=0.6$ je **lepší model** (data jsou pravděpodobnější).

**Myšlenka MLE:** odhad odpovídá hodnotě parametru, pro kterou jsou **trénovací data nejpravděpodobnější**. Jde o **optimalizaci** — maximalizujeme funkci, která udává pravděpodobnost trénovacích dat:
$$L(p) = p^7 (1-p)^3 \quad \text{na } [0,1].$$
Místo derivace polynomu desátého stupně funkci **zlogaritmujeme** (logaritmus je ostře rostoucí, extrémy zůstávají na stejných místech):
$$\ell(p) = \ln L(p) = 7\ln p + 3\ln(1-p), \qquad \ell'(p) = \frac{7}{p} - \frac{3}{1-p} = 0 \;\Rightarrow\; \hat{p}_{\mathrm{MLE}} = \frac{7}{10}.$$

### 2.2 Věrohodnostní funkce logistické regrese

Pro logistickou regresi je situace obdobná, jen pravděpodobnost nezávisí na jediném parametru, ale na $p+1$ parametrech $w_0,\dots,w_p$. Pro úsporu místa značíme
$$p_1(x, w) = \mathrm{P}(Y=1 \mid x, w) = \frac{e^{w^T x}}{1+e^{w^T x}}, \qquad p_0(x, w) = \mathrm{P}(Y=0 \mid x, w) = \frac{1}{1+e^{w^T x}}.$$
Mějme $N$ trénovacích bodů; $i$-tý bod sestává z hodnoty $Y_i$ a příznaků $x_i = (x_{i;0}, x_{i;1},\dots,x_{i;p})$ s $x_{i;0}=1$. Hodnoty zapíšeme do vektoru $\boldsymbol{Y} = (Y_1,\dots,Y_N)^T \in \mathbb{R}^N$ a do matice příznaků
$$\mathbf{X} = \begin{pmatrix} x_1^T \\ \vdots \\ x_N^T \end{pmatrix} = \begin{pmatrix} 1 & x_{1;1} & \cdots & x_{1;p} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{N;1} & \cdots & x_{N;p} \end{pmatrix}.$$

Pravděpodobnost jednoho bodu lze přes Bernoulliho model napsat jednotně jako
$$p_{Y_i}(x_i, w) = p_1(x_i, w)^{Y_i}\,p_0(x_i, w)^{1-Y_i} = \hat{p}_i^{\,Y_i}\,(1-\hat{p}_i)^{1-Y_i},$$
neboť pro $Y_i = 1$ dává $\hat p_i$ a pro $Y_i = 0$ dává $1-\hat p_i$.

Za (většinou oprávněného) předpokladu **[[Nezávislost-náhodných-veličin|nezávislosti]]** jednotlivých datových bodů je pravděpodobnost trénovacích dat součinem pravděpodobností bodů — to je **věrohodnostní funkce** (angl. *likelihood function*):
$$\boxed{\;L(w) = \prod_{i=1}^N p_{Y_i}(x_i, w)\;}$$
reálná funkce $p+1$ proměnných $\mathbb{R}^{p+1}\to\mathbb{R}$, vyjadřující pravděpodobnost trénovacích dat pro danou hodnotu $w$.

### 2.3 Log-věrohodnost a binární křížová entropie

Stejně jako u mince derivujeme místo součinu jeho logaritmus — **logaritmickou věrohodnost** $\ell(w) = \ln L(w)$:
$$\begin{aligned}
\ell(w) = \ln L(w) &= \sum_{i=1}^N \ln p_{Y_i}(x_i, w)\\
&= \sum_{i=1}^N \Big( Y_i \ln p_1(x_i, w) + (1-Y_i)\ln p_0(x_i, w) \Big)\\
&= \sum_{i=1}^N \left( Y_i \ln\frac{e^{w^T x_i}}{1+e^{w^T x_i}} + (1-Y_i)\ln\frac{1}{1+e^{w^T x_i}} \right)\\
&= \sum_{i=1}^N \Big( Y_i\, w^T x_i - \ln\!\big(1 + e^{w^T x_i}\big) \Big).
\end{aligned}$$
(Poslední úprava je „trocha čarování s logaritmem“ — roznásobení a sloučení obou členů.)

**Ekvivalence s křížovou entropií.** Výraz uvnitř první sumy
$$-\big(Y_i \ln \hat{p}_i + (1-Y_i)\ln(1-\hat{p}_i)\big)$$
je **binární křížová entropie** (angl. *binary cross-entropy*) jednoho bodu. Platí tedy
$$\text{binární křížová entropie} = -\,\ell(w),$$
takže **maximalizace věrohodnosti je ekvivalentní minimalizaci binární křížové entropie** — což je obvyklá účelová funkce (loss) trénování klasifikátorů.

### 2.4 Gradient log-věrohodnosti

Maximum hledáme stejně jako u lineární regrese pomocí **[[Gradient|gradientu]]** — vektoru parciálních derivací podle všech $w_0,\dots,w_p$:
$$\frac{\partial \ell}{\partial w_j}(w) = \sum_{i=1}^N x_{i;j}\big(Y_i - p_1(x_i, w)\big), \qquad j = 0, 1, \dots, p.$$
Maticovým zápisem (s vektorem predikovaných pravděpodobností $\boldsymbol{P} = (p_1(x_1,w),\dots,p_1(x_N,w))^T$):
$$\boxed{\;\nabla\ell(w) = \mathbf{X}^T\big(\boldsymbol{Y} - \boldsymbol{P}\big)\;}.$$
Reziduum $\boldsymbol{Y} - \boldsymbol{P}$ (rozdíl skutečných hodnot a predikovaných pravděpodobností) je váženo příznaky — formálně stejný tvar jako u lineární regrese, jen $\boldsymbol{P}$ skrývá sigmoidy.

### 2.5 Optimalizace — proč není uzavřené řešení

**Podmínka prvního řádu.** Maximum hledáme mezi řešeními rovnice „gradient se rovná nule“:
$$\nabla\ell(w) = \mathbf{X}^T(\boldsymbol{Y} - \boldsymbol{P}) = 0.$$
Na rozdíl od lineární regrese ale **neumíme najít explicitní (uzavřené) řešení** — neexistuje vzorec, do kterého bychom dosadili data a vypadly by koeficienty $w$ (pod $\boldsymbol{P}$ se skrývají exponenciály sigmoid, rovnice je nelineární).

**Konvexnost a jednoznačnost maxima.** Účelová funkce trénování (záporná log-věrohodnost = křížová entropie) je **[[Konvexní-funkce|konvexní]]** v $w$. Funkce $\ell(w)$ proto nemá více lokálních maxim: pokud lokální maximum existuje, je **jediné** a je to hledané **globální** maximum. (Maximum ovšem nemusí existovat vždy — neexistuje právě v případě **lineárně separabilních** tříd, kdy lze $w$ škálovat tak, že $w^T x_i > 0$ pro všechny body třídy $1$ a $w^T x_i < 0$ pro třídu $0$, a věrohodnost roste nade všechny meze.)

**Numerické metody.** Protože uzavřené řešení neexistuje, je nutné použít **numerické aproximativní metody**, které konstruují posloupnost $w^{(0)}, w^{(1)}, w^{(2)}, \dots$ konvergující k maximu:

- **vícerozměrná Newtonova metoda** (v této úloze ekvivalentní **IRLS** — iteratively reweighted least squares);
- **gradientní vzestup** (angl. *gradient ascent*).

**Algoritmus (gradientní vzestup).** Začneme počáteční hodnotou $w^{(0)}$ a iterujeme ve směru nejvyššího růstu (gradient ukazuje směrem nejvyššího růstu):
$$w^{(i+1)} = w^{(i)} + \alpha\,\nabla\ell\big(w^{(i)}\big) = w^{(i)} + \alpha\,\mathbf{X}^T\big(\boldsymbol{Y} - \boldsymbol{P}(w^{(i)})\big),$$
kde $\alpha$ je **učící parametr** (angl. *learning rate*), který může záviset na $i$ (adaptivní verze). I když globální maximum existuje, konvergence může být pomalá a pro nevhodné $\alpha$ nemusí konvergovat.

*Poznámka.* Logistická regrese je přímým použitím metod parametrické statistiky (viz BI-PST). Celá metoda stojí na předpokladu, že chování dat lze zachytit sigmoidou aplikovanou na lineární kombinaci $w^T x$; zda tato volnost (daná parametry $w$) stačí k přiblížení skutečnosti, je třeba mít na paměti. Model lze rozšířit odvozenými příznaky (mocniny, součiny příznaků apod.), čímž lze získat i nelineární rozhodovací hranice.

---

## Co je potřeba na zkoušku znát

### Definice
- **Sigmoida:** $\sigma(z) = \dfrac{e^z}{1+e^z} = \dfrac{1}{1+e^{-z}}$, obor hodnot $(0,1)$, prostá, $\sigma^{-1}(x) = \ln\frac{x}{1-x}$, $\sigma(0)=\tfrac12$.
- **Model logistické regrese:** $\mathrm{P}(Y=1\mid x,w) = \sigma(w^T x)$, $\mathrm{P}(Y=0\mid x,w) = 1-\sigma(w^T x)$; intercept $x_0=1$.
- **Rozhodovací pravidlo:** $\hat{Y} = \mathbb{1}[\hat p > \tfrac12]$; **hranice** $w^T x = 0$ (nadrovina, dim. $p-1$) → lineární klasifikátor.
- **Logit (log-odds):** $\ln\frac{\hat p}{1-\hat p} = w^T x$.
- **Věrohodnostní funkce:** $L(w) = \prod_{i=1}^N p_{Y_i}(x_i,w)$ s $p_{Y_i} = \hat p_i^{\,Y_i}(1-\hat p_i)^{1-Y_i}$; **log-věrohodnost** $\ell = \ln L$.

### Věty
- **Log-věrohodnost LR:** $\ell(w) = \sum_{i=1}^N\big(Y_i w^T x_i - \ln(1+e^{w^T x_i})\big)$.
- **Ekvivalence:** binární křížová entropie $= -\ell(w)$, tedy max. věrohodnosti $\iff$ min. cross-entropy.
- **Gradient:** $\frac{\partial\ell}{\partial w_j} = \sum_i x_{i;j}(Y_i - p_1(x_i,w))$, maticově $\nabla\ell(w) = \mathbf{X}^T(\boldsymbol{Y}-\boldsymbol{P})$.
- Účelová funkce je **konvexní** → lokální max. (pokud existuje) je jediné = globální; max. neexistuje pro lineárně separabilní třídy.
- **Není uzavřené řešení** rovnice $\nabla\ell(w)=0$ (na rozdíl od lineární regrese).

### Algoritmy
- **MLE odhad** $\hat w$: maximalizuj věrohodnost = data nejpravděpodobnější (myšlenka: minci $\hat p_{\mathrm{MLE}}=\tfrac{7}{10}$).
- **Gradientní vzestup:** $w^{(i+1)} = w^{(i)} + \alpha\,\mathbf{X}^T(\boldsymbol{Y}-\boldsymbol{P}(w^{(i)}))$, $\alpha$ = learning rate, kroky ve směru nejvyššího růstu.
- **Newtonova metoda / IRLS** — alternativní numerická metoda (rychlejší konvergence).
