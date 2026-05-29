---
aliases: [asymptota, asymptoty, asymptotu, asymptotou, svislá asymptota, šikmá asymptota, vodorovná asymptota, asymptota se směrnicí, asymptote]
tags: [definice, kurz/MA1]
---

# Asymptota

Přímka, ke které se graf funkce „přimyká". Rozlišujeme dva typy.

## Svislá asymptota

Funkce $f$ má v bodě $a \in \mathbb{R}$ **asymptotu** $x = a$, právě když alespoň jedna z jednostranných limit $\lim_{x\to a^+} f(x)$, $\lim_{x\to a^-} f(x)$ je rovna $+\infty$ nebo $-\infty$.

## Asymptota se směrnicí (v $\pm\infty$)

Přímka $y = kx + q$ je **asymptotou** $f$ v $+\infty$ (resp. $-\infty$), právě když
$$\lim_{x\to+\infty} \big(f(x) - kx - q\big) = 0 \quad (\text{resp. } x\to-\infty).$$

**Výpočet koeficientů:**
$$k = \lim_{x\to+\infty} \frac{f(x)}{x}, \qquad q = \lim_{x\to+\infty} \big(f(x) - kx\big).$$
Musí existovat konečné obě limity. Pro $k = 0$ jde o **vodorovnou** asymptotu $y = q$. Asymptoty v $+\infty$ a $-\infty$ se mohou lišit.

⚠️ Asymptota není totéž co [[Derivace|tečna]] — graf může asymptotu i vícekrát protnout.

## Související

- [[Limita-funkce]]
- [[Derivace]]
- [[Konvexní-funkce]]
