---
studyplan: true
etapa: 2 · PST — Dedecius + Petr
qid: 27PST
examiner: Dedecius + Petr
topic: "Mat. statistika: náhodný výběr, bodové/intervalové odhady, testování hypotéz"
readiness: nezačato
hot: true
tags:
  - otázka
  - kurz/PST
  - otázka/27
  - hotovo
---

# Základy matematické statistiky

> **Otázka SZZ:** Základy matematické statistiky: náhodný výběr, princip bodových a intervalových odhadů, testování statistických hypotéz, odhady střední hodnoty a souvislost s testováním hypotéz o střední hodnotě.

Zdroje: BI-PST přednášky 8, 9, 10, 11 (Blažek, Hrabák, Hrabáková, Novák, Vašata; FIT ČVUT).

---

## 1. Náhodný výběr a úloha matematické statistiky

V teorii pravděpodobnosti pracujeme s modely se **známými** parametry a predikujeme. **Matematická statistika** postupuje opačně: na základě naměřených dat vybíráme model, **odhadujeme** parametry a **testujeme** hypotézy.

### 1.1 Náhodný výběr
**[[Náhodný-výběr]]:** $n$-tice **nezávislých, stejně rozdělených** ([[Nezávislost-náhodných-veličin|i.i.d.]]) [[Náhodná-veličina|náhodných veličin]] $X_1, \dots, X_n$ s [[Distribuční-funkce|distribuční funkcí]] $F$.
**Realizace náhodného výběru** (data): $n$-tice konkrétních pozorovaných čísel $x_1, \dots, x_n$.

### 1.2 Kroky statistického uvažování
1. **Odhad tvaru rozdělení** — volba parametrické třídy $\{F_\theta : \theta \in \Theta\}$ (z apriorní znalosti / intuice). Tvar odhadujeme **histogramem** a **empirickou distribuční funkcí** $F_n(x) = \tfrac1n\sum_{i=1}^n \mathbf{1}_{\{X_i \le x\}}$.
2. **Odhad parametrů** — bodový a intervalový.
3. **Ověření modelu** — testování hypotéz (testy dobré shody, parametrické testy).

**Statistika** = libovolná funkce náhodného výběru, která nezávisí na $\theta$.

### 1.3 Teoretický základ: zákon velkých čísel a CLV
Pro výběrový průměr $\bar X_n = \tfrac1n\sum_i X_i$ z i.i.d. veličin s $\mathbb{E}X_i = \mu$, $\operatorname{var}X_i = \sigma^2$ platí $\mathbb{E}\bar X_n = \mu$, $\operatorname{var}\bar X_n = \sigma^2/n$.
- **[[Zákon-velkých-čísel|Zákon velkých čísel]]:** $\bar X_n \xrightarrow{P} \mu$ (slabý), resp. skoro jistě (silný) — zaručuje **konzistenci** $\bar X_n$.
- **[[Centrální-limitní-věta|Centrální limitní věta]]:** $\dfrac{\bar X_n - \mu}{\sigma/\sqrt n} \xrightarrow{D} N(0,1)$ — umožňuje přibližné intervaly a testy i pro nenormální data.

---

## 2. Bodové odhady

### 2.1 Princip
**[[Bodový-odhad]]** parametru $\theta$ je statistika $\hat\theta_n = \hat\theta_n(X_1, \dots, X_n)$ — funkce náhodného výběru nezávislá na $\theta$. Jakožto funkce náhodných veličin je sám náhodnou veličinou s rozdělením závislým na $\theta$.

**Nejužívanější odhady:**
- **výběrový průměr** (odhad $\mu = \mathbb{E}X$): $\displaystyle \bar X_n = \frac1n\sum_{i=1}^n X_i$;
- **výběrový rozptyl** (odhad $\sigma^2 = \operatorname{var}X$): $\displaystyle s_n^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar X_n)^2$;
- výběrová směrodatná odchylka $s_n = \sqrt{s_n^2}$; výběrový $k$-tý moment $m_k = \tfrac1n\sum_i X_i^k$; výběrová [[Kovariance|kovariance]] a [[Korelace|korelační koeficient]].

### 2.2 Žádané vlastnosti
- **Nestrannost (nevychýlenost):** $\mathbb{E}\hat\theta_n = \theta$ pro všechna $\theta \in \Theta$ (žádná systematická chyba).
- **Konzistence:** $\hat\theta_n \xrightarrow{P} \theta$ pro $n \to \infty$ (tj. $\forall\varepsilon>0: P(|\hat\theta_n - \theta| \ge \varepsilon) \to 0$).
  - **Věta (postačující podmínka):** je-li $\mathbb{E}\hat\theta_n \to \theta$ a $\operatorname{var}\hat\theta_n \to 0$, je $\hat\theta_n$ konzistentní.
- **Nejlepší nestranný odhad:** nestranný odhad s nejmenším rozptylem (dolní mez = Rao–Cramér).

**Výběrový průměr** je nestranný ($\mathbb{E}\bar X_n = \tfrac1n\sum \mathbb{E}X_i = \mu$) a konzistentní ($\operatorname{var}\bar X_n = \sigma^2/n \to 0$, resp. ze ZVČ).
**Výběrový rozptyl** je nestranný — proto dělíme $n-1$, nikoli $n$:
$$\mathbb{E}s_n^2 = \frac{1}{n-1}\bigl(n\,\mathbb{E}X_i^2 - n\,\mathbb{E}\bar X_n^2\bigr) = \frac{1}{n-1}\bigl(n(\sigma^2+\mu^2) - n(\tfrac{\sigma^2}{n}+\mu^2)\bigr) = \sigma^2.$$
(Odhad s dělením $n$ je jen *asymptoticky* nestranný.)

### 2.3 Metody konstrukce odhadů
- **Metoda momentů:** teoretické momenty vyjádříme jako funkce $\theta$, nahradíme je výběrovými momenty $m_k$ a vyřešíme. Odhady jsou vždy konzistentní (ze ZVČ $m_k \to \mathbb{E}X^k$), ale ne vždy nestranné/optimální.
- **Metoda maximální věrohodnosti (MLE):** **věrohodnostní funkce** $L(\theta; x) = \prod_{i=1}^n f_\theta(x_i)$ (resp. $\prod_i P_\theta(X_i = x_i)$); MLE $\hat\theta_n$ ji maximalizuje (často přes $\ln L$). Za podmínek regularity jsou MLE konzistentní, asymptoticky nestranné a asymptoticky normální. Pro $N(\mu,\sigma^2)$ vyjde $\hat\mu_n = \bar X_n$, $\hat\sigma_n^2 = \tfrac1n\sum(X_i - \bar X_n)^2$.

---

## 3. Intervalové odhady

### 3.1 Princip
**[[Interval-spolehlivosti|Interval spolehlivosti]]** (konfidenční interval): interval $(L, U)$ s mezemi danými statistikami $L = L(X)$, $U = U(X)$ takový, že
$$P(L < \theta < U) = 1 - \alpha.$$
$1-\alpha$ je **hladina spolehlivosti** (typicky $95\%$ či $99\%$). Pro **oboustranný** symetrický interval volíme $P(\theta < L) = P(U < \theta) = \alpha/2$. **Jednostranné** intervaly: horní $(L, +\infty)$ s $P(L < \theta) = 1-\alpha$, dolní $(-\infty, U)$.

> Pozor na interpretaci: náhodné jsou meze $L, U$ (závisí na výběru), nikoli parametr $\theta$. Při mnoha opakováních pokrývá náhodný interval skutečné $\theta$ v podílu $1-\alpha$ případů.

### 3.2 Obecný postup
1. najdi **pivotovou statistiku** $H(\theta)$ závisející na $\theta$ i na výběru, se **známým rozdělením**;
2. najdi meze $h_L, h_U$ s $P(h_L < H(\theta) < h_U) = 1-\alpha$;
3. úpravou nerovností osamostatni $\theta$, čímž získáš $P(L < \theta < U) = 1-\alpha$.

Statistiku $H(\theta)$ volíme podle rozdělení příslušného bodového odhadu (výběrový průměr pro $\mu$, výběrový rozptyl pro $\sigma^2$).

### 3.3 Pomocná rozdělení
- **$\chi^2$ rozdělení** s $n$ stupni volnosti: rozdělení $\sum_{i=1}^n Y_i^2$ pro $Y_i$ i.i.d. $N(0,1)$.
- **Studentovo $t$-rozdělení** s $n$ st. volnosti: $T = Z / \sqrt{Y/n}$, kde $Z \sim N(0,1)$ nezávislé na $Y \sim \chi^2_n$.

Pro výběr z $N(\mu,\sigma^2)$: $\dfrac{(n-1)s_n^2}{\sigma^2} \sim \chi^2_{n-1}$ a $\dfrac{\bar X_n - \mu}{s_n/\sqrt n} \sim t_{n-1}$.

### 3.4 Interval pro rozptyl $\sigma^2$ (normální rozdělení)
$$\left(\frac{(n-1)s_n^2}{\chi^2_{\alpha/2,\,n-1}},\ \frac{(n-1)s_n^2}{\chi^2_{1-\alpha/2,\,n-1}}\right),$$
platí **jen** pro normální rozdělení.

(Intervaly pro střední hodnotu jsou jádrem části 5.)

---

## 4. Testování statistických hypotéz

### 4.1 Princip
**[[Testování-hypotéz]]:** tvrzení o rozdělení dat, která nelze s jistotou potvrdit, jsou **hypotézy**.
- **Nulová hypotéza** $H_0$ — tvrzení, které testujeme;
- **Alternativní hypotéza** $H_A$ — opačné tvrzení.

Postavení hypotéz je **asymetrické**: za $H_0$ volíme tu, jejíž neoprávněné zamítnutí je závažnější; tvrzení, které chceme prokázat, klademe jako $H_A$ (zamítnutí $H_0$ je „silný" výsledek). Typy: **parametrické** (o $\theta$) a **neparametrické** (o tvaru rozdělení — testy dobré shody).

### 4.2 Chyby a hladina významnosti
| | $H_0$ platí | $H_0$ neplatí |
|---|---|---|
| **zamítáme** $H_0$ | chyba **1. druhu** ($\alpha$) | správné rozhodnutí |
| **nezamítáme** $H_0$ | správné rozhodnutí | chyba **2. druhu** ($\beta$) |

- **Hladina významnosti** $\alpha$ = maximální přípustná pravděpodobnost chyby 1. druhu (typicky $5\%$, $1\%$).
- **Síla testu** $= 1 - \beta = 1 - P(\text{chyba 2. druhu})$.
- **p-hodnota** = nejmenší hladina významnosti, na níž lze $H_0$ při daných datech zamítnout. Je-li p-hodnota $< \alpha$, zamítáme $H_0$.

### 4.3 Možné výsledky
- **Zamítáme $H_0$** (přijímáme $H_A$) — $H_A$ je „statisticky významné" (s malou pravděpodobností chyby $\alpha$).
- **Nezamítáme $H_0$** — $H_A$ je „statisticky nevýznamné" (nezamítnutí neznamená důkaz $H_0$).

### 4.4 Test pomocí intervalu spolehlivosti
Pro $H_0: \theta = \theta_0$ proti $H_A: \theta \ne \theta_0$ sestrojíme oboustranný $100(1-\alpha)\%$ [[Interval-spolehlivosti|interval spolehlivosti]] $(L,U)$ a:
- **zamítneme $H_0$**, jestliže $\theta_0 \notin (L, U)$;
- **nezamítneme $H_0$**, jestliže $\theta_0 \in (L, U)$.

**Že jde o test na hladině $\alpha$:** za platnosti $H_0$ ($\theta = \theta_0$)
$$P(\text{zamítneme } H_0 \mid H_0) = P(\theta_0 \notin (L,U) \mid \theta=\theta_0) = 1 - P(\theta \in (L,U)) = 1 - (1-\alpha) = \alpha.$$
Pro **jednostrannou** alternativu použijeme odpovídající jednostranný interval (horní pro $H_A: \theta > \theta_0$, dolní pro $H_A: \theta < \theta_0$). Tento postup dává pro širokou třídu rozdělení **nejsilnější** test (nejmenší chybu 2. druhu).

### 4.5 Alternativně: testová statistika a kritický obor
*(Pro zkoušku z BI-PST není nutné — uvádím pro úplnost.)* Sestrojíme testovou statistiku $T(X_1,\dots,X_n)$ a **kritický obor** $W_\alpha$ z odlehlých částí jejího rozdělení za $H_0$; zamítneme, je-li $T \in W_\alpha$. Pro $H_0: \mu=\mu_0$ ($\sigma^2$ známý): $T = \tfrac{\bar X_n - \mu_0}{\sigma}\sqrt n$, $W_\alpha = \{|T| > z_{\alpha/2}\}$. Oba přístupy (interval × kritický obor) jsou ekvivalentní.

---

## 5. Odhady střední hodnoty a souvislost s testováním hypotéz o $\mu$

Toto je propojení předchozích částí — nejdůležitější část otázky.

### 5.1 Bodový odhad střední hodnoty
$\mu = \mathbb{E}X$ odhadujeme **výběrovým průměrem** $\bar X_n$, který je nestranný a konzistentní (viz 2.2). Pro $N(\mu,\sigma^2)$ je $\bar X_n$ nejlepším nestranným odhadem $\mu$.

### 5.2 Interval spolehlivosti pro $\mu$ — při známém rozptylu
**Věta.** Pro náhodný výběr z $N(\mu,\sigma^2)$ se **známým** $\sigma^2$ je oboustranný $100(1-\alpha)\%$ interval spolehlivosti pro $\mu$
$$\left(\bar X_n - z_{\alpha/2}\frac{\sigma}{\sqrt n},\ \bar X_n + z_{\alpha/2}\frac{\sigma}{\sqrt n}\right),$$
kde $z_{\alpha/2} = \Phi^{-1}(1-\alpha/2)$ je kritická hodnota $N(0,1)$ ($P(Z > z_{\alpha/2}) = \alpha/2$). Jednostranné: $\bigl(\bar X_n - z_\alpha\tfrac{\sigma}{\sqrt n}, +\infty\bigr)$ a $\bigl(-\infty, \bar X_n + z_\alpha\tfrac{\sigma}{\sqrt n}\bigr)$.

*Idea důkazu:* součet i.i.d. $N(\mu,\sigma^2)$ je $N(n\mu, n\sigma^2)$ (z MGF), tedy $\bar X_n \sim N(\mu, \sigma^2/n)$ a po standardizaci $Z = \tfrac{\bar X_n - \mu}{\sigma/\sqrt n} \sim N(0,1)$. Z $P(-z_{\alpha/2} < Z < z_{\alpha/2}) = 1-\alpha$ osamostatníme $\mu$.

### 5.3 Interval pro $\mu$ — při neznámém rozptylu
Neznámý $\sigma^2$ nahradíme výběrovým rozptylem $s_n^2$. Protože $\dfrac{\bar X_n - \mu}{s_n/\sqrt n} \sim t_{n-1}$, je oboustranný $100(1-\alpha)\%$ interval pro $\mu$
$$\left(\bar X_n - t_{\alpha/2,\,n-1}\frac{s_n}{\sqrt n},\ \bar X_n + t_{\alpha/2,\,n-1}\frac{s_n}{\sqrt n}\right),$$
kde $t_{\alpha/2,n-1}$ je kritická hodnota Studentova rozdělení s $n-1$ stupni volnosti. Tyto intervaly jsou **širší** než při známém $\sigma^2$; pro $n \to \infty$ obě rozdělení splývají.

### 5.4 Nenormální data — přibližné intervaly z CLV
Pro výběr z **libovolného** rozdělení s $\mathbb{E}X_i = \mu$, $\operatorname{var}X_i = \sigma^2$ dává [[Centrální-limitní-věta|CLV]] při dostatečně velkém $n$ (zpravidla $n \ge 30$–$50$) tytéž intervaly **přibližně** (s asymptotickou spolehlivostí $1-\alpha$). Příklad — volební účast: $X_i \sim \text{Be}(p)$, $\mu = p$, $\sigma^2 = p(1-p)$; odhadneme $\hat p_n = \bar X_n$ a interval $\hat p_n \pm z_{\alpha/2}\sqrt{\hat p_n(1-\hat p_n)/n}$.

### 5.5 Test hypotézy o střední hodnotě
Pro $X_1,\dots,X_n$ z $N(\mu,\sigma^2)$ testujeme $H_0: \mu = \mu_0$ na hladině $\alpha$ **přímo pomocí intervalu spolehlivosti z 5.2/5.3** — zamítneme $H_0$, pokud $\mu_0$ neleží v příslušném intervalu spolehlivosti:

| $H_A$ | interval (známé $\sigma^2$) | interval (neznámé $\sigma^2$) |
|---|---|---|
| $\mu \ne \mu_0$ | $\bar X_n \pm z_{\alpha/2}\tfrac{\sigma}{\sqrt n}$ | $\bar X_n \pm t_{\alpha/2,n-1}\tfrac{s_n}{\sqrt n}$ |
| $\mu > \mu_0$ | $\bigl(\bar X_n - z_\alpha\tfrac{\sigma}{\sqrt n}, \infty\bigr)$ | $\bigl(\bar X_n - t_{\alpha,n-1}\tfrac{s_n}{\sqrt n}, \infty\bigr)$ |
| $\mu < \mu_0$ | $\bigl(-\infty, \bar X_n + z_\alpha\tfrac{\sigma}{\sqrt n}\bigr)$ | $\bigl(-\infty, \bar X_n + t_{\alpha,n-1}\tfrac{s_n}{\sqrt n}\bigr)$ |

**Souvislost je tedy přímá:** intervalový odhad parametru $\mu$ a test hypotézy o $\mu$ jsou dvě strany téže mince — $H_0: \mu = \mu_0$ zamítáme na hladině $\alpha$ právě tehdy, když $\mu_0$ leží mimo $100(1-\alpha)\%$ konfidenční interval pro $\mu$. (Ekvivalentně testovou statistikou $T = \tfrac{\bar X_n - \mu_0}{s_n/\sqrt n}$ a kritickými hodnotami $t$-rozdělení.)

**Příklad (váha kaprů):** $\bar X_n = 4{,}565$, $s_n^2 = 0{,}0342$, $n = 10$. Test $H_0: \mu = 4{,}7$ proti $H_A: \mu < 4{,}7$ na $\alpha = 5\%$: dolní $95\%$ interval $(-\infty,\ 4{,}565 + 1{,}833\cdot\tfrac{\sqrt{0{,}0342}}{\sqrt{10}}) = (-\infty, 4{,}672)$. Protože $\mu_0 = 4{,}7 \notin$ interval, $H_0$ **zamítáme** — střední váha je významně nižší než 4,7 kg.

### 5.6 Rozšíření (dvouvýběrové a párové problémy)
- **Párový $t$-test:** páry $(X_i, Y_i)$, položíme $Z_i = Y_i - X_i$ a testujeme $H_0: \mu_{\text{diff}} = 0$ jednovýběrovým testem o střední hodnotě rozdílů.
- **Dvouvýběrový $t$-test:** dva nezávislé výběry, $H_0: \mu_1 = \mu_2$, testová statistika založená na $\bar X_{n_1} - \bar Y_{n_2}$ (varianta dle shody rozptylů). Shodu rozptylů ověří **F-test**.

---

## 6. Co je potřeba na zkoušku znát

### Definice
Náhodný výběr (i.i.d.); statistika; bodový odhad; nestrannost; konzistence; výběrový průměr a rozptyl; interval spolehlivosti (oboustranný/jednostranný), hladina spolehlivosti; nulová a alternativní hypotéza; chyba 1. a 2. druhu; hladina významnosti; síla testu; p-hodnota.

### Věty / postupy (s ideou)
- Nestrannost a konzistence $\bar X_n$ a $s_n^2$ (proč dělíme $n-1$).
- Postačující podmínka konzistence ($\mathbb{E}\hat\theta_n \to \theta$, $\operatorname{var}\hat\theta_n \to 0$).
- Obecný postup konstrukce intervalu spolehlivosti (pivotová statistika).
- Interval pro $\mu$ při známém ($z$) i neznámém ($t$) rozptylu; idea $\bar X_n \sim N(\mu,\sigma^2/n)$.
- Test pomocí konfidenčního intervalu má hladinu významnosti $\alpha$ (důkaz).
- **Souvislost odhadu a testu střední hodnoty:** zamítnutí $H_0:\mu=\mu_0$ $\iff$ $\mu_0$ mimo CI.
- Role [[Zákon-velkých-čísel|ZVČ]] (konzistence) a [[Centrální-limitní-věta|CLV]] (přibližné intervaly/testy pro nenormální data).

### Vzorce zpaměti
$\bar X_n$, $s_n^2 = \tfrac{1}{n-1}\sum(X_i-\bar X_n)^2$; CI pro $\mu$: $\bar X_n \pm z_{\alpha/2}\tfrac{\sigma}{\sqrt n}$ (známé $\sigma^2$), $\bar X_n \pm t_{\alpha/2,n-1}\tfrac{s_n}{\sqrt n}$ (neznámé).
