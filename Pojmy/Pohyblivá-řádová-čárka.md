---
aliases: [pohyblivá řádová čárka, pohyblivé řádové čárce, plovoucí řádová čárka, plovoucí řádové čárky, floating point, pohyblivá řádová čárka, IEEE 754, polohovaná řádová čárka]
tags: [definice, kurz/SAP]
---

# Pohyblivá řádová čárka

## Definice
**Pohyblivá (plovoucí) řádová čárka** zobrazuje reálné číslo dvojicí (mantisa, exponent):
$$A = (-1)^s \cdot M \cdot z^{e},$$
kde $z$ je základ (obvykle 2), **mantisa** $M$ nese hodnotu (zlomkový tvar) a **exponent** $e$ určuje polohu řádové čárky. Obě podmřížky používají kódy pro čísla se znaménkem. Oproti pevné řádové čárce dává mnohem větší rozsah.

**Normalizovaný tvar:** mantisu už nelze posunout více doleva. Při $z=2$ a přímém kódu je pak nejvyšší bit mantisy vždy 1 → lze ji vynechat = **skrytá jednička**. Po každé operaci je nutná **normalizace**.

## IEEE 754
| | znaménko | exponent | mantisa | bias $K$ |
|---|---|---|---|---|
| **single (32 b)** | 1 | 8 | 23 (+1 skrytá) | 127 |
| **double (64 b)** | 1 | 11 | 52 (+1 skrytá) | 1023 |

Exponent je v **aditivním kódu** (uloženo $g=e+K$). Hodnota normalizovaného čísla: $A=(-1)^s\cdot(1.f)\cdot 2^{\,g-K}$.

**Speciální hodnoty:** $g=0,\ f=0\Rightarrow$ nula; $g=0,\ f\ne0\Rightarrow$ **denormalizované** číslo (bez skryté 1); $g=\text{max}, f=0\Rightarrow\pm\infty$; $g=\text{max}, f\ne0\Rightarrow$ **NaN**.

**Aritmetika:** sčítání = zarovnat exponenty + sečíst mantisy + normalizovat; násobení = sečíst exponenty + vynásobit mantisy.

## Související
- [[Doplňkový-kód]]
