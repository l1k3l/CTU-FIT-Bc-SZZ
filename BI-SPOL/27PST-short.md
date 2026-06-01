---
tags: [otázka, kurz/PST, otázka/27, hotovo]
---

# 27 — Základy matematické statistiky (zkrácená verze)

## 1. [[Náhodný-výběr|Náhodný výběr]]

- **N. výběr:** i.i.d. $X_1,\dots,X_n$ s distr. fcí $F$; **realizace** = data $x_1,\dots,x_n$.
- **Statistika** = funkce výběru nezávislá na $\theta$.
- Pro $\bar X_n=\tfrac1n\sum X_i$: $\mathbb{E}\bar X_n=\mu$, $\operatorname{var}\bar X_n=\sigma^2/n$.
  - **[[Zákon-velkých-čísel|ZVČ]]:** $\bar X_n\xrightarrow{P}\mu$ (konzistence).
  - **[[Centrální-limitní-věta|CLV]]:** $\tfrac{\bar X_n-\mu}{\sigma/\sqrt n}\xrightarrow{D}N(0,1)$ → přibližné intervaly/testy.

## 2. [[Bodový-odhad|Bodové odhady]]

- **Odhad** $\hat\theta_n=\hat\theta_n(X_1,\dots,X_n)$ — statistika; sám je n. veličinou.
- **Výběrový průměr** $\bar X_n$ (odhad $\mu$); **výběrový rozptyl** $s_n^2=\tfrac1{n-1}\sum(X_i-\bar X_n)^2$ (odhad $\sigma^2$).
- **Nestrannost:** $\mathbb{E}\hat\theta_n=\theta$. **Konzistence:** $\hat\theta_n\xrightarrow{P}\theta$ (stačí $\mathbb{E}\hat\theta_n\to\theta$ a $\operatorname{var}\hat\theta_n\to0$).
- $\bar X_n$, $s_n^2$ jsou nestranné a konzistentní (dělíme $n-1$ kvůli nestrannosti).
- **Metody:** momentů ($m_k\!=\!$ teor. moment); **max. věrohodnost** $L(\theta)=\prod_i f_\theta(x_i)\to\max$.

## 3. [[Interval-spolehlivosti|Intervalové odhady]]

- **Interval spolehlivosti:** $(L,U)$, $P(L<\theta<U)=1-\alpha$. Oboustranný: $P(\theta<L)=P(U<\theta)=\alpha/2$. Jednostranné $(L,\infty)$, $(-\infty,U)$.
- **Postup:** pivot $H(\theta)$ se známým rozdělením → meze → osamostatni $\theta$.
- Pomocná rozdělení (pro $N(\mu,\sigma^2)$): $\tfrac{(n-1)s_n^2}{\sigma^2}\sim\chi^2_{n-1}$, $\tfrac{\bar X_n-\mu}{s_n/\sqrt n}\sim t_{n-1}$.
- **CI pro $\sigma^2$:** $\bigl(\tfrac{(n-1)s_n^2}{\chi^2_{\alpha/2,n-1}},\tfrac{(n-1)s_n^2}{\chi^2_{1-\alpha/2,n-1}}\bigr)$ (jen normální).

## 4. [[Testování-hypotéz|Testování hypotéz]]

- $H_0$ (testujeme) vs. $H_A$ (chceme prokázat); za $H_0$ to, jehož chybné zamítnutí je horší.
- **Chyba 1. druhu:** zamítneme platné $H_0$ (pst $\le\alpha$ = hladina významnosti). **Chyba 2. druhu:** nezamítneme neplatné $H_0$ (pst $\beta$). **Síla** $=1-\beta$. **p-hodnota** = nejmenší $\alpha$ pro zamítnutí.
- **Test pomocí CI:** zamítni $H_0:\theta=\theta_0$, pokud $\theta_0\notin$ CI odpovídající $H_A$. Pst chyby 1. druhu $=1-(1-\alpha)=\alpha$. (Jednostranná $H_A$ → jednostranný interval.)

## 5. Odhad $\mu$ a test o $\mu$ (jádro otázky)

**Bodově:** $\mu\approx\bar X_n$ (nestranný, konzistentní).

**CI pro $\mu$:**
$$\text{známý }\sigma^2:\ \bar X_n\pm z_{\alpha/2}\tfrac{\sigma}{\sqrt n}, \qquad \text{neznámý }\sigma^2:\ \bar X_n\pm t_{\alpha/2,n-1}\tfrac{s_n}{\sqrt n}.$$
($z_{\alpha/2}$ kr. hodnota $N(0,1)$; $t$ Studentova s $n-1$ st. volnosti; neznámý $\sigma^2$ → širší.) Idea: $\bar X_n\sim N(\mu,\sigma^2/n)$ → $Z=\tfrac{\bar X_n-\mu}{\sigma/\sqrt n}\sim N(0,1)$. Pro nenormální data přibližně z CLV ($n\gtrsim30$).

**Test $H_0:\mu=\mu_0$ na hladině $\alpha$:** zamítni, pokud $\mu_0$ **neleží** v příslušném CI:

| $H_A$ | neznámý $\sigma^2$ |
|---|---|
| $\mu\ne\mu_0$ | $\bar X_n\pm t_{\alpha/2,n-1}\tfrac{s_n}{\sqrt n}$ |
| $\mu>\mu_0$ | $(\bar X_n - t_{\alpha,n-1}\tfrac{s_n}{\sqrt n},\infty)$ |
| $\mu<\mu_0$ | $(-\infty,\ \bar X_n + t_{\alpha,n-1}\tfrac{s_n}{\sqrt n})$ |

**Souvislost:** $H_0:\mu=\mu_0$ zamítneme na hladině $\alpha$ $\iff$ $\mu_0\notin$ $100(1-\alpha)\%$ CI pro $\mu$. (Ekv. test. statistika $T=\tfrac{\bar X_n-\mu_0}{s_n/\sqrt n}$ vs. $t$-kvantily.)

---

## Co odpovědět rychle

- N. výběr = i.i.d.; $\bar X_n$, $s_n^2$ — nestranné a konzistentní odhady $\mu$, $\sigma^2$.
- CI: $P(L<\theta<U)=1-\alpha$; pro $\mu$: $\bar X_n\pm z_{\alpha/2}\sigma/\sqrt n$ (známé) / $\bar X_n\pm t_{\alpha/2,n-1}s_n/\sqrt n$ (neznámé).
- Test pomocí CI: zamítni $H_0$, je-li $\theta_0$ mimo interval → hladina $\alpha$.
- **Odhad $\mu$ ↔ test o $\mu$:** zamítnutí $H_0:\mu=\mu_0$ $\iff$ $\mu_0$ mimo CI pro $\mu$.
