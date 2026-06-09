---
tags: [otázka, kurz/PST, otázka/26, hotovo]
---

# 26 — Náhodné veličiny a náhodné vektory (zkrácená verze)

## 1. Náhodná veličina, typy

- **[[Náhodná-veličina|N. veličina]]** $X$: funkce $X:\Omega\to\mathbb{R}$ s **měřitelností** $\{X\le x\}\in\mathcal{F}\ \forall x$.
- **Typy:** *diskrétní* (spočetně hodnot, popsána $P(X=x_k)$), *spojitá* (existuje [[Hustota|hustota]] $f_X$, $P(X=x)=0$), *smíšená*.

## 2. [[Distribuční-funkce|Distribuční funkce]]

$$F_X(x)=P(X\le x).$$
Jednoznačně určuje rozdělení. **Vlastnosti:** neklesající; $\lim_{-\infty}F=0$, $\lim_{+\infty}F=1$; spojitá zprava.
$P(X>x)=1-F(x)$, $P(a<X\le b)=F(b)-F(a)$, $P(X=x)=F(x)-\lim_{y\to x^-}F(y)$ (skok).

## 3. Pravděpodobnostní funkce / hustota

- **[[Pravděpodobnostní-funkce|Pravděp. funkce]]** (diskr.): $P(X=x_k)$, $\sum_k P(X=x_k)=1$, $F_X(x)=\sum_{x_k\le x}P(X=x_k)$.
- **[[Hustota]]** (spoj.): $f_X\ge0$, $F_X(x)=\int_{-\infty}^x f_X$, $\int_{\mathbb{R}}f_X=1$, $f_X=F_X'$, $P(a<X\le b)=\int_a^b f_X$.

## 4. Momenty

- **[[Střední-hodnota]]:** $\mathbb{E}X=\sum_k x_kP(X=x_k)$ / $\int x f_X\,dx$. Linearita: $\mathbb{E}(aX+bY)=a\mathbb{E}X+b\mathbb{E}Y$. $\mathbb{E}g(X)=\sum g(x_k)P(\cdot)$ / $\int g f_X$.
- **[[Rozptyl]]:** $\operatorname{var}X=\mathbb{E}(X-\mathbb{E}X)^2=\mathbb{E}X^2-(\mathbb{E}X)^2$; $\operatorname{var}(aX+b)=a^2\operatorname{var}X$; $\sigma=\sqrt{\operatorname{var}X}$.
- **Transformace $Y=aX+b$** (Dedecius!): $\mathbb{E}Y=a\mathbb{E}X+b$, $\operatorname{var}Y=a^2\operatorname{var}X$, $\sigma_Y=|a|\sigma_X$; hustota $f_Y(y)=\tfrac1{|a|}f_X(\tfrac{y-b}a)$.
- **Momenty:** $\mu_k=\mathbb{E}X^k$, centrální $\sigma_k=\mathbb{E}(X-\mu_1)^k$. Šikmost $\gamma_1=\sigma_3/\sigma^3$, špičatost $\gamma_2=\sigma_4/\sigma^4-3$.
- **MGF:** $M_X(s)=\mathbb{E}e^{sX}$; $\mathbb{E}X^k=M^{(k)}(0)$; nezáv. $\Rightarrow M_{X+Y}=M_XM_Y$.
- **[[Kvantil]]:** $q_\alpha=\inf\{x:F_X(x)\ge\alpha\}$; medián $q_{0.5}$.

## 5. Příklady rozdělení

| diskr. | $P(X=k)$ | $\mathbb{E}X$ | $\operatorname{var}X$ |
|---|---|---|---|
| $\text{Be}(p)$ | $p$, resp. $1-p$ | $p$ | $p(1-p)$ |
| $\text{Bin}(n,p)$ | $\binom nk p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| $\text{Geom}(p)$ | $(1-p)^{k-1}p$ | $1/p$ | $(1-p)/p^2$ |
| $\text{Poiss}(\lambda)$ | $\tfrac{\lambda^k}{k!}e^{-\lambda}$ | $\lambda$ | $\lambda$ |

| spoj. | $f_X(x)$ | $\mathbb{E}X$ | $\operatorname{var}X$ |
|---|---|---|---|
| $\text{Unif}(a,b)$ | $\tfrac1{b-a}$ | $\tfrac{a+b}2$ | $\tfrac{(b-a)^2}{12}$ |
| $\text{Exp}(\lambda)$ | $\lambda e^{-\lambda x}$ | $1/\lambda$ | $1/\lambda^2$ |
| $N(\mu,\sigma^2)$ | $\tfrac1{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ |

**[[Normální-rozdělení|Normální]]:** $N(0,1)$ má distr. fci $\Phi$ (tabulky). Standardizace: $X\sim N(\mu,\sigma^2)\Rightarrow Z=\tfrac{X-\mu}\sigma\sim N(0,1)$.

## 6. [[Náhodný-vektor|Náhodný vektor]] $(X,Y)$

- **Sdružené:** $F_{X,Y}(x,y)=P(X\le x\cap Y\le y)$; diskr. $P(X=x\cap Y=y)$, spoj. $f_{X,Y}$, $f_{X,Y}=\partial^2F/\partial x\partial y$.
- **Marginální:** $P(X=x)=\sum_y P(X=x\cap Y=y)$, $f_X(x)=\int f_{X,Y}(x,y)\,dy$.
- **Podmíněné:** $P(X=x\mid Y=y)=\tfrac{P(X=x\cap Y=y)}{P(Y=y)}$, $f_{X\mid Y}(x\mid y)=\tfrac{f_{X,Y}(x,y)}{f_Y(y)}$.
- **Součet (nezáv.):** konvoluce; $N+N=N(2\mu,2\sigma^2)$, $\text{Poiss}(\lambda)+\text{Poiss}(\mu)=\text{Poiss}(\lambda+\mu)$.

## 7. [[Nezávislost-náhodných-veličin|Nezávislost]]

$F_{X,Y}=F_XF_Y$; diskr. $P(X=x\cap Y=y)=P(X=x)P(Y=y)$; spoj. $f_{X,Y}=f_Xf_Y$ (stačí faktorizace $g(x)h(y)$).

## 8. [[Kovariance]] a [[Korelace|korelace]]

$$\operatorname{cov}(X,Y)=\mathbb{E}[(X-\mathbb{E}X)(Y-\mathbb{E}Y)]=\mathbb{E}[XY]-\mathbb{E}X\,\mathbb{E}Y, \qquad \rho(X,Y)=\frac{\operatorname{cov}(X,Y)}{\sigma_X\sigma_Y}.$$
- $\operatorname{cov}(X,X)=\operatorname{var}X$; $\operatorname{var}(X\pm Y)=\operatorname{var}X+\operatorname{var}Y\pm2\operatorname{cov}(X,Y)$.
- $-1\le\rho\le1$; $\rho=\pm1\iff Y=\pm aX+b$; **nekorelované** $\iff\operatorname{cov}=0\iff\mathbb{E}XY=\mathbb{E}X\mathbb{E}Y$.
- **Nezávislost $\Rightarrow$ nekorelovanost** (opačně NE). *Příklad nekorel. ale závislých:* $X$ sym. kolem 0, $Y=X^2$ ⇒ $\operatorname{cov}=0$, ale $Y=f(X)$.

---

## Co odpovědět rychle

- N. veličina = měřitelná $X:\Omega\to\mathbb{R}$; rozdělení popíše $F_X$ (univerzálně), $P(X=x_k)$ (diskr.), $f_X$ (spoj.).
- $\operatorname{var}X=\mathbb{E}X^2-(\mathbb{E}X)^2$; linearita $\mathbb{E}$.
- Rozdělení zpaměti: Be, Bin, Geom, Poisson; Unif, Exp, Normal — s $\mathbb{E}X$, $\operatorname{var}X$.
- $\rho\in[-1,1]$ měří lineární vztah; nezávislé $\Rightarrow$ nekorelované, ne naopak.
