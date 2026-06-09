---
studyplan: true
etapa: 2 · PST — Dedecius + Petr
qid: 26PST
examiner: Dedecius + Petr
topic: Náhodné veličiny a vektory, rozdělení, distribuční fce, momenty, kovariance/korelace
readiness: nezačato
hot: true
tags:
  - otázka
  - kurz/PST
  - otázka/26
  - hotovo
---

# Náhodné veličiny a náhodné vektory

> **Otázka SZZ:** Náhodné veličiny a náhodné vektory: definice, typy, distribuční funkce, pravděpodobnostní funkce, hustota, momenty, příklady rozdělení, nezávislost, kovariance, korelace.

Zdroje: BI-PST přednášky 3, 4, 5, 6, 7 (Blažek, Hrabák, Hrabáková, Novák, Vašata; FIT ČVUT).

---

## 1. Náhodná veličina — definice a typy

### 1.1 Definice
**[[Náhodná-veličina]]** $X$ na pravděpodobnostním prostoru $(\Omega, \mathcal{F}, P)$ je funkce, která každému výsledku experimentu $\omega \in \Omega$ přiřadí číslo $X(\omega) \in \mathbb{R}$ a splňuje **podmínku měřitelnosti**:
$$\{X \le x\} := \{\omega \in \Omega : X(\omega) \le x\} \in \mathcal{F}, \qquad \forall x \in \mathbb{R}.$$
Měřitelnost zaručuje, že $\{X \le x\}$ je náhodný jev, takže umíme počítat $P(X \le x)$, $P(X = x)$, $P(X \in (a,b))$ atd. V praxi ji obvykle nemusíme ověřovat, je potřebná hlavně pro důkazy.

Náhodná veličina vybírá z výsledku experimentu tu číselnou informaci, která nás zajímá (např. počet hlav při hodech mincí, výška náhodně vybraného člověka).

### 1.2 Typy náhodných veličin
- **Diskrétní** — nabývá pouze hodnot z nejvýše spočetné množiny $\{x_1, x_2, \dots\}$. Popisujeme **[[Pravděpodobnostní-funkce|pravděpodobnostní funkcí]]** $P(X = x_k)$. Distribuční funkce je schodovitá.
- **(Absolutně) spojitá** — existuje **[[Hustota|hustota]]** $f_X \ge 0$ s $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$. Distribuční funkce je spojitá, $P(X = x) = 0$ pro každé $x$.
- **Smíšená** — distribuční funkce má jak skoky, tak spojité úseky.

Náhodná veličina může být diskrétní, i když prostor $\Omega$ diskrétní není (např. body za zásah terče).

---

## 2. Distribuční funkce

### 2.1 Definice
**[[Distribuční-funkce]]** náhodné veličiny $X$ je
$$F_X(x) = P(X \le x), \qquad x \in \mathbb{R}.$$
Distribuční funkce **jednoznačně určuje** rozdělení $X$ a dává úplný popis jejího chování — pro libovolné $x$ víme, s jakou pravděpodobností je $X \le x$.

### 2.2 Vlastnosti (Věta)
Funkce $F = F_X$ má vlastnosti:
1. **neklesající:** $x < y \Rightarrow F(x) \le F(y)$;
2. **„začíná v 0 a končí v 1":** $\lim_{x\to-\infty} F(x) = 0$, $\lim_{x\to+\infty} F(x) = 1$;
3. **spojitá zprava:** $\lim_{y\to x^+} F(y) = F(x)$.

*Důkaz (i):* z disjunktního rozkladu $\{X \le y\} = \{X \le x\} \cup \{x < X \le y\}$ plyne $F(y) = F(x) + P(x < X \le y) \ge F(x)$.
*Důkaz (ii) (náznak):* pro $B_n = \{X \le -n\} \searrow \emptyset$ dá věta o spojitosti pravděpodobnosti $P(B_n) \to 0$; analogicky $A_n = \{X \le n\} \nearrow \Omega$ dá $P(A_n) \to 1$.
Spojitost zprava plyne z toho, že v definici je $\le$ (povolena rovnost).

### 2.3 Použití (Lemma)
- $P(X > x) = 1 - F(x)$;
- $P(x < X \le y) = F(y) - F(x)$;
- $P(X < x) = \lim_{y\to x^-} F(y)$;
- $P(X = x) = F(x) - \lim_{y\to x^-} F(y)$ — **velikost skoku** v bodě $x$.

---

## 3. Pravděpodobnostní funkce (diskrétní veličiny)

Pro diskrétní $X$ s hodnotami $\{x_1, x_2, \dots\}$ je **[[Pravděpodobnostní-funkce|pravděpodobnostní funkce]]** (diskrétní hustota) předpis $x \mapsto P(X = x)$.

**Vlastnosti:**
- **normalizace:** $\sum_{\text{all } x_k} P(X = x_k) = 1$;
- $P(X \in B) = \sum_{x_k \in B} P(X = x_k)$;
- vztah k distribuční funkci: $F_X(x) = \sum_{k:\,x_k \le x} P(X = x_k)$, a při $x_1 < x_2 < \dots$ je $P(X = x_k) = F_X(x_k) - F_X(x_{k-1})$.

Velikost skoku $F_X$ v bodě $x_k$ je právě $P(X = x_k)$.

---

## 4. Hustota (spojité veličiny)

### 4.1 Definice
$X$ je **(absolutně) spojitá**, existuje-li nezáporná **[[Hustota|hustota]]** $f_X$ taková, že
$$F_X(x) = \int_{-\infty}^{x} f_X(t)\,dt, \qquad \forall x \in \mathbb{R}.$$

### 4.2 Vlastnosti (Věta)
1. **normalizace:** $\int_{-\infty}^{+\infty} f_X(x)\,dx = 1$;
2. $P(X = x) = 0$ pro všechna $x$;
3. $f_X(x) = F_X'(x)$ v bodech, kde derivace existuje;
4. $P(a < X \le b) = \int_a^b f_X(x)\,dx = F_X(b) - F_X(a)$;
5. $P(X \in B) = \int_B f_X(x)\,dx$.

*Důsledky:* u spojité veličiny nezáleží na ostrosti nerovností: $P(a < X \le b) = P(a \le X \le b) = P(a < X < b)$. Interpretace: $f_X(x)\,dx \approx P(x < X < x+dx)$.

### 4.3 Funkce (transformace) náhodné veličiny
Pro $Y = g(X)$ s měřitelnou $g$:
- **diskrétní** $X$: $P(Y = y) = \sum_{k:\,g(x_k)=y} P(X = x_k)$;
- obecně $F_Y(y) = P(g(X) \le y)$; je-li $g^{-1}$ rostoucí, $F_Y(y) = F_X(g^{-1}(y))$ a (pro ryze monotónní hladké $g$) $f_Y(y) = f_X(g^{-1}(y))\,\bigl|\tfrac{d}{dy}g^{-1}(y)\bigr|$.

**Afinní (lineární) transformace $Y = aX + b$** (oblíbené doptávání): střední hodnotu a rozptyl získáme přímo z linearity (§5.1) a vlastnosti rozptylu (§5.2), **bez** určování rozdělení $Y$:
$$\mathbb{E}Y = a\,\mathbb{E}X + b, \qquad \operatorname{var}Y = a^2 \operatorname{var}X, \qquad \sigma_Y = |a|\,\sigma_X.$$
(Hustota se transformuje jako $f_Y(y) = \tfrac{1}{|a|}f_X\!\bigl(\tfrac{y-b}{a}\bigr)$.) Toto je „linearita náhodné veličiny", na niž se Dedecius opakovaně doptává.

### 4.4 Kvantilová funkce
**[[Kvantil|$\alpha$-kvantil]]** je $q_\alpha = \inf\{x : F_X(x) \ge \alpha\}$; jako funkce $\alpha$ je to kvantilová funkce $F_X^{-1}$. Pro ryze rostoucí spojitou $F_X$ platí $F_X(q_\alpha) = \alpha$. Speciálně: medián $q_{0.5}$, kvartily $q_{0.25}, q_{0.75}$. **Generování:** je-li $U \sim \text{Unif}(0,1)$, pak $F_X^{-1}(U)$ má rozdělení $X$ (důkaz: $P(F_X^{-1}(U) \le x) = P(U \le F_X(x)) = F_X(x)$).

---

## 5. Momenty a charakteristiky

### 5.1 Střední hodnota
**[[Střední-hodnota]]** (vážený průměr možných hodnot):
$$\mathbb{E}X = \sum_k x_k\,P(X = x_k) \quad\text{(diskrétní)}, \qquad \mathbb{E}X = \int_{-\infty}^{+\infty} x\,f_X(x)\,dx \quad\text{(spojitá)},$$
existuje, právě když suma/integrál **absolutně konverguje**. Interpretace: těžiště (rovnovážný bod) rozdělení.

**Střední hodnota funkce** (bez určování rozdělení $g(X)$): $\mathbb{E}\,g(X) = \sum_k g(x_k)P(X=x_k)$ resp. $\int g(x)f_X(x)\,dx$.

**Vlastnosti:** $X \ge 0 \Rightarrow \mathbb{E}X \ge 0$; $\mathbb{E}(aX + b) = a\,\mathbb{E}X + b$; $\mathbb{E}c = c$; **linearita** $\mathbb{E}(aX + bY) = a\,\mathbb{E}X + b\,\mathbb{E}Y$ (i pro závislé veličiny).

### 5.2 Rozptyl
**[[Rozptyl]]** $\operatorname{var}X = \mathbb{E}[(X - \mathbb{E}X)^2]$, **směrodatná odchylka** $\sigma = \sqrt{\operatorname{var}X}$.

**Výpočetní vzorec:** $\operatorname{var}X = \mathbb{E}(X^2) - (\mathbb{E}X)^2$.
*Odvození:* $\mathbb{E}[(X-\mathbb{E}X)^2] = \mathbb{E}[X^2 - 2X\mathbb{E}X + (\mathbb{E}X)^2] = \mathbb{E}(X^2) - 2(\mathbb{E}X)^2 + (\mathbb{E}X)^2 = \mathbb{E}(X^2) - (\mathbb{E}X)^2$.

**Vlastnosti:** $\operatorname{var}(aX + b) = a^2 \operatorname{var}X$; $\operatorname{var}(c) = 0$; $\operatorname{var}X \ge 0$ (proto $(\mathbb{E}X)^2 \le \mathbb{E}(X^2)$).

### 5.3 Obecné a centrální momenty
- $k$-tý **moment:** $\mu_k = \mathbb{E}(X^k)$;
- $k$-tý **centrální moment:** $\sigma_k = \mathbb{E}[(X - \mu_1)^k]$.

Speciálně $\mu_1 = \mathbb{E}X$ (poloha), $\sigma_2 = \operatorname{var}X$ (rozptýlení).
- **šikmost** (skewness): $\gamma_1 = \dfrac{\mathbb{E}(X - \mathbb{E}X)^3}{(\operatorname{var}X)^{3/2}}$ — míra asymetrie;
- **špičatost** (excess kurtosis): $\gamma_2 = \dfrac{\mathbb{E}(X - \mathbb{E}X)^4}{(\operatorname{var}X)^{2}} - 3$ — srovnání s normálním rozdělením ($\gamma_2 = 0$).

### 5.4 Momentová vytvořující funkce
$$M_X(s) = \mathbb{E}(e^{sX}).$$
Jednoznačně určuje rozdělení (Laplaceova transformace). Umožňuje počítat momenty:
$$\mathbb{E}(X^k) = \frac{d^k}{ds^k} M_X(s)\Big|_{s=0}, \quad\text{tj.}\quad \mathbb{E}X = M'(0),\ \mathbb{E}X^2 = M''(0),\ \operatorname{var}X = M''(0) - (M'(0))^2.$$
Pro **nezávislé** veličiny je vytvořující funkce součtu součinem: $M_{X+Y}(s) = M_X(s)M_Y(s)$.

---

## 6. Příklady rozdělení

### 6.1 Diskrétní rozdělení

| Rozdělení | $P(X=k)$ | $\mathbb{E}X$ | $\operatorname{var}X$ | význam |
|---|---|---|---|---|
| **Bernoulliho** $\text{Be}(p)$ | $P(1)=p,\ P(0)=1-p$ | $p$ | $p(1-p)$ | jeden pokus (úspěch/neúspěch) |
| **Binomické** $\text{Bin}(n,p)$ | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | počet úspěchů v $n$ pokusech |
| **Geometrické** $\text{Geom}(p)$ | $(1-p)^{k-1}p,\ k\ge1$ | $\tfrac1p$ | $\tfrac{1-p}{p^2}$ | pořadí 1. úspěchu |
| **Poissonovo** $\text{Poisson}(\lambda)$ | $\tfrac{\lambda^k}{k!}e^{-\lambda},\ k\ge0$ | $\lambda$ | $\lambda$ | počet vzácných událostí |

- **Indikátor jevu** $A$: $\mathbf{1}_A = 1$ pokud $A$ nastal, jinak $0$; je to $\text{Be}(P(A))$. Binomickou veličinu lze psát jako součet indikátorů $X = \sum_{i=1}^n \mathbf{1}_{H_i}$.
- **Poissonovo** je limitou binomického pro $n \to \infty$, $p \to 0$, $np = \lambda$ konstantní: $\binom{n}{k}p^k(1-p)^{n-k} \to \frac{\lambda^k}{k!}e^{-\lambda}$.
- MGF Poissona: $M(s) = e^{\lambda(e^s - 1)}$.

### 6.2 Spojitá rozdělení

| Rozdělení | $f_X(x)$ | $\mathbb{E}X$ | $\operatorname{var}X$ |
|---|---|---|---|
| **Rovnoměrné** $\text{Unif}(a,b)$ | $\tfrac{1}{b-a}$ na $[a,b]$ | $\tfrac{a+b}{2}$ | $\tfrac{(b-a)^2}{12}$ |
| **Exponenciální** $\text{Exp}(\lambda)$ | $\lambda e^{-\lambda x},\ x\ge0$ | $\tfrac1\lambda$ | $\tfrac1{\lambda^2}$ |
| **Normální** $N(\mu,\sigma^2)$ | $\tfrac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |

- Exponenciální: $F_X(x) = 1 - e^{-\lambda x}$; modeluje doby čekání (Poissonův proces); MGF $\frac{\lambda}{\lambda - s}$ pro $s < \lambda$.
- **[[Normální-rozdělení]]:** $N(0,1)$ je **standardní** s distribuční funkcí $\Phi$ (tabelovaná, analyticky nevyjádřitelná). **Standardizace:** $X \sim N(\mu,\sigma^2) \Rightarrow Z = \tfrac{X-\mu}{\sigma} \sim N(0,1)$, takže $F_X(x) = \Phi\!\bigl(\tfrac{x-\mu}{\sigma}\bigr)$. Obecná standardizace $Z = (X-\mu)/\sigma$ dává $\mathbb{E}Z = 0$, $\operatorname{var}Z = 1$.

---

## 7. Náhodné vektory

### 7.1 Sdružené rozdělení
**[[Náhodný-vektor]]** $(X_1, \dots, X_n)$ má **sdruženou distribuční funkci**
$$F_X(x) = P(X_1 \le x_1 \cap \dots \cap X_n \le x_n).$$
Pro dvojici $F_{X,Y}(x,y) = P(X \le x \cap Y \le y)$. Vlastnosti analogické jednorozměrnému případu (neklesající v obou proměnných, limity, $\lim_{x\to\infty} F_{X,Y}(x,y) = F_Y(y)$).

- **Diskrétní:** sdružená pravděpodobnostní funkce $P(X=x \cap Y=y)$, $\sum_{x,y} = 1$.
- **Spojité:** sdružená hustota $f_{X,Y}(x,y) \ge 0$, $F_{X,Y}(x,y) = \int_{-\infty}^y\!\int_{-\infty}^x f_{X,Y}$, $\iint f_{X,Y} = 1$, $f_{X,Y} = \partial^2 F_{X,Y}/\partial x\,\partial y$.

### 7.2 Marginální rozdělení
Rozdělení jedné složky bez ohledu na druhou:
$$P(X = x) = \sum_{\text{all } y} P(X = x \cap Y = y), \qquad f_X(x) = \int_{-\infty}^{+\infty} f_{X,Y}(x,y)\,dy.$$

### 7.3 Podmíněné rozdělení
- **Diskrétní:** $P(X = x \mid Y = y) = \dfrac{P(X=x \cap Y=y)}{P(Y=y)}$ pro $P(Y=y) > 0$.
- **Spojité:** podmíněná hustota $f_{X\mid Y}(x \mid y) = \dfrac{f_{X,Y}(x,y)}{f_Y(y)}$ pro $f_Y(y) > 0$ (nelze podmiňovat jevem $\{Y=y\}$, neboť $P(Y=y)=0$).
- **Podmíněná střední hodnota** $\mathbb{E}(X \mid Y=y) = \sum_x x\,P(X=x\mid Y=y)$ resp. $\int x f_{X\mid Y}(x\mid y)\,dx$ — funkce $y$.

### 7.4 Součet náhodných veličin
Pro **nezávislé** $X, Y$ je rozdělení $Z = X+Y$ dáno **konvolucí**:
$$P(Z=z) = \sum_x P(X=x)P(Y=z-x) \quad\text{(diskr.)}, \qquad f_Z(z) = \int_{-\infty}^{+\infty} f_X(x)f_Y(z-x)\,dx \quad\text{(spoj.)}.$$
Příklady: $N(\mu,\sigma^2) + N(\mu,\sigma^2) = N(2\mu, 2\sigma^2)$ (obecně součet $n$ nezávislých $N(\mu,\sigma^2)$ je $N(n\mu, n\sigma^2)$); $\text{Poisson}(\lambda) + \text{Poisson}(\mu) = \text{Poisson}(\lambda+\mu)$. Snadno přes vytvořující funkce.

---

## 8. Nezávislost náhodných veličin

**[[Nezávislost-náhodných-veličin|Nezávislost]]:** $X, Y$ jsou nezávislé, pokud pro všechna $x, y$ platí
$$F_{X,Y}(x,y) = F_X(x)\,F_Y(y), \quad\text{tj.}\quad P(X \le x \cap Y \le y) = P(X \le x)P(Y \le y).$$
Obecně $X_1, \dots, X_n$ nezávislé $\iff F_X(x) = \prod_{i=1}^n P(X_i \le x_i)$ pro všechna $x \in \mathbb{R}^n$.

**Kritéria** (zjednodušení):
- **diskrétní:** $P(X=x \cap Y=y) = P(X=x)P(Y=y)$ pro všechna $x,y$;
- **spojité:** $f_{X,Y}(x,y) = f_X(x)f_Y(y)$ pro všechna $x,y$;
- **faktorizace:** lze-li $f_{X,Y}(x,y) = g(x)h(y)$, jsou $X, Y$ nezávislé (a $f_X = k\,g$, $f_Y = \tfrac1k h$ pro vhodné $k$).

---

## 9. Kovariance a korelace

### 9.1 Kovariance
Pro $X, Y$ s konečnými druhými momenty je **[[Kovariance]]**
$$\operatorname{cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}X)(Y - \mathbb{E}Y)] = \mathbb{E}[XY] - \mathbb{E}X\,\mathbb{E}Y.$$
Měří míru **lineární** závislosti.

**Vlastnosti:**
- $\operatorname{cov}(X,X) = \operatorname{var}X$;
- $\operatorname{cov}(aX+b, cY+d) = ac\,\operatorname{cov}(X,Y)$;
- $\operatorname{var}(X \pm Y) = \operatorname{var}X + \operatorname{var}Y \pm 2\operatorname{cov}(X,Y)$;
- $\operatorname{var}(aX + bY) = a^2\operatorname{var}X + b^2\operatorname{var}Y + 2ab\,\operatorname{cov}(X,Y)$.

### 9.2 Korelační koeficient
Pro kladné rozptyly je **[[Korelace|korelační koeficient]]**
$$\rho(X, Y) = \frac{\operatorname{cov}(X,Y)}{\sigma_X\,\sigma_Y} = \frac{\operatorname{cov}(X,Y)}{\sqrt{\operatorname{var}X}\sqrt{\operatorname{var}Y}}.$$
Je to kovariance standardizovaných veličin (bezrozměrná).

**Vlastnosti (Věta):**
1. $\operatorname{cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}X\,\mathbb{E}Y$;
2. $X, Y$ nekorelované $\iff \mathbb{E}[XY] = \mathbb{E}X\,\mathbb{E}Y$;
3. $-1 \le \rho(X,Y) \le 1$ (Schwarzova nerovnost);
4. $\rho(aX+b, cY+d) = \rho(X,Y)$ pro $a,c > 0$;
5. $\rho(X,Y) = \pm1 \iff \exists\,a>0, b:\ Y = \pm aX + b$ (úplná lineární závislost).

### 9.3 Nekorelovanost vs. nezávislost
$X, Y$ jsou **nekorelované**, pokud $\operatorname{cov}(X,Y) = 0$.

**Věta:** Jsou-li $X, Y$ **nezávislé**, pak jsou **nekorelované**.
*Důkaz (spojitý případ):* z $f_{X,Y} = f_X f_Y$ plyne $\mathbb{E}[XY] = \iint xy f_X(x)f_Y(y)\,dx\,dy = \bigl(\int x f_X\bigr)\bigl(\int y f_Y\bigr) = \mathbb{E}X\,\mathbb{E}Y$, tedy $\operatorname{cov}(X,Y) = 0$.

**Opačná implikace neplatí:** nekorelovanost zachytí jen *lineární* závislost; existují nekorelované, ale závislé veličiny. (Obecnou nelineární závislost popisuje entropie.)

> *Doplnění nad rámec slidů (examinátoři často chtějí „uveďte příklad"):* vezmi $X$ symetricky kolem $0$ (např. $X \sim \text{Unif}(-1,1)$ nebo $P(X=\pm1)=P(X=\pm2)=\tfrac14$) a $Y = X^2$. Pak $\mathbb{E}X = 0$ a $\mathbb{E}[XY] = \mathbb{E}X^3 = 0$, takže $\operatorname{cov}(X,Y) = 0$ — **nekorelované**. Přitom $Y$ je funkcí $X$, takže **závislé** (znalost $X$ určuje $Y$). Příklad *nezávislých* veličin: dva nezávislé hody kostkou; *závislých*: $X$ = hod, $Y = X$.

---

## 10. Co je potřeba na zkoušku znát

### Definice
Náhodná veličina (podmínka měřitelnosti); distribuční funkce; diskrétní vs. spojitá vs. smíšená; pravděpodobnostní funkce; hustota; střední hodnota, rozptyl, momenty, centrální momenty, MGF; kvantil; náhodný vektor (sdružené, marginální, podmíněné rozdělení); nezávislost; kovariance; korelační koeficient; nekorelovanost.

### Věty (se znalostí důkazu/idee)
- Vlastnosti distribuční funkce (neklesající, limity 0/1, spojitost zprava).
- Vlastnosti hustoty (normalizace, $P(X=x)=0$, $f = F'$).
- Výpočetní vzorec $\operatorname{var}X = \mathbb{E}X^2 - (\mathbb{E}X)^2$ (odvození).
- Linearita střední hodnoty $\mathbb{E}(aX+bY) = a\mathbb{E}X + b\mathbb{E}Y$.
- Vlastnosti kovariance a korelace (1–5), zejména $-1 \le \rho \le 1$.
- **Nezávislost $\Rightarrow$ nekorelovanost** (s důkazem); opačně neplatí.
- Standardizace normální veličiny $\tfrac{X-\mu}{\sigma} \sim N(0,1)$.

### Příklady rozdělení (parametry, $\mathbb{E}X$, $\operatorname{var}X$)
Diskrétní: Bernoulli, binomické, geometrické, Poissonovo. Spojitá: rovnoměrné, exponenciální, normální. Znát pmf/hustotu i střední hodnotu a rozptyl zpaměti.

### Typické doplňující otázky (doptávání)
*(Komise: Dedecius + Petr. Q26 je Dedeciova nejčastější otázka — dává áčka, ale hodně doptává na statistické pozadí.)*
- **Dedecius:** „Transformace náhodné veličiny $Y = aX + b$ — spočítejte $\mathbb{E}Y$ a $\operatorname{var}Y$ přes $\mathbb{E}X$, $\operatorname{var}X$" (linearita náhodné veličiny — opakovaně 2021, 2023, 2025) → §4.3, §5.1–5.2.
- **Dedecius:** „Definice hustoty — $F_X$ je integrál hustoty od $-\infty$ **do $x$**, ne do $+\infty$" (opravoval studenta) → §4.1.
- **Dedecius:** „Linearita střední hodnoty a rozptylu." Definici momentů bere benevolentně (sám řekl, že je „divoká") → §5.1–5.3.
- **Vacková:** „Co jsou parametry $a, b$ u rovnoměrného rozdělení; jak se **formálně** zapisuje hustota (značení $f_X(x)$, ne $P(\dots)$; velké $X$ = veličina, malé $x$ = hodnota)" → §6.2, §4.1.
- **Kupsa / Vašata:** „Uveďte příklad závislých a nezávislých veličin; příklad nekorelovaných, ale závislých veličin" → §8, §9.3.
- *(Náhodné vektory)* „Marginální rozdělení — jak se k němu dojde ze sdruženého" → §7.2.

> **Mimo rozsah této otázky (kandidát na samostatný writeup):** historické znění otázky uvádělo i *pravidla pro výpočty pravděpodobností, Bayesův vzorec, apriorní/aposteriorní pravděpodobnost, nezávislost náhodných jevů, CLV a ZVČ*. Bayesovskou část drilloval P. **Klán** (není v naší komisi); naše komise (Dedecius/Petr) ji nikdy nedotazovala. **CLV a ZVČ** viz [[27PST-long|otázka 27 §1.3]].
