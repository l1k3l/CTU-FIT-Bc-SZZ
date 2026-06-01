---
aliases: [náhodná veličina, náhodné veličiny, náhodnou veličinu, náhodné veličině, náhodnou veličinou, náhodných veličin, náhodným veličinám, náhodná, veličina, n.v., random variable]
tags: [definice, kurz/PST]
---

# Náhodná veličina

## Definice

**Náhodná veličina** $X$ na pravděpodobnostním prostoru $(\Omega, \mathcal{F}, P)$ je funkce, která každému výsledku experimentu $\omega \in \Omega$ přiřadí hodnotu $X(\omega) \in \mathbb{R}$ a splňuje **podmínku měřitelnosti**
$$\{X \le x\} = \{\omega \in \Omega : X(\omega) \le x\} \in \mathcal{F}, \quad \forall x \in \mathbb{R}.$$
Měřitelnost zaručuje, že $\{X \le x\}$ je náhodný jev, takže lze počítat $P(X \le x)$, $P(X = x)$, $P(X \in (a,b))$ apod.

Rozdělení náhodné veličiny je jednoznačně určeno její [[Distribuční-funkce|distribuční funkcí]] $F_X(x) = P(X \le x)$.

## Typy

- **Diskrétní** — nabývá nejvýše spočetně mnoha hodnot $\{x_1, x_2, \dots\}$; popsána [[Pravděpodobnostní-funkce|pravděpodobnostní funkcí]] $P(X = x_k)$.
- **(Absolutně) spojitá** — existuje [[Hustota|hustota]] $f_X \ge 0$ s $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$; pak $P(X = x) = 0$ pro každé $x$.
- **Smíšená** — kombinace obojího (distribuční funkce má skoky i spojité úseky).

## Funkce náhodné veličiny

Pro měřitelnou $g: \mathbb{R} \to \mathbb{R}$ je $Y = g(X)$ opět náhodná veličina. Je-li $g^{-1}$ rostoucí a hladká, pak $f_Y(y) = f_X(g^{-1}(y))\,\bigl|\tfrac{d}{dy}g^{-1}(y)\bigr|$.

## Související

- [[Distribuční-funkce]]
- [[Hustota]]
- [[Pravděpodobnostní-funkce]]
- [[Střední-hodnota]]
- [[Rozptyl]]
- [[Náhodný-vektor]]
