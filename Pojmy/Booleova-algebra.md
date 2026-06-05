---
aliases: [Booleova algebra, Booleovy algebry, Booleově algebře, Booleovou algebrou, booleovská algebra, logická algebra, Boolova algebra]
tags: [definice, kurz/SAP]
---

# Booleova algebra

## Definice
**Booleova algebra** je struktura $\langle B, +, \cdot, \neg, 0, 1\rangle$, kde $B$ je neprázdná množina (nosič), $+$ a $\cdot$ jsou binární operace, $\neg$ je unární operace (negace) a $0, 1$ jsou nulární operace, splňující pro všechna $a,b,c \in B$:

| | zákon | duální | název |
|---|---|---|---|
| 1 | $a+b=b+a$ | $a\cdot b=b\cdot a$ | komutativita |
| 2 | $a+(b+c)=(a+b)+c$ | $a\cdot(b\cdot c)=(a\cdot b)\cdot c$ | asociativita |
| 3 | $a+(b\cdot c)=(a+b)(a+c)$ | $a\cdot(b+c)=ab+ac$ | distributivita |
| 4 | $a+0=a$ | $a\cdot 1=a$ | neutralita 0 a 1 |
| 5 | $a+\overline{a}=1$ | $a\cdot\overline{a}=0$ | vlastnosti negace |

Jde o **úplný komplementární distributivní svaz**. V logice: $+$ = OR, $\cdot$ = AND (mají stejnou prioritu, $\cdot$ se vynechává), $B=\{0,1\}$.

## Odvozené zákony
Idempotence ($a+a=a$), agresivita ($a+1=1$, $a\cdot 0=0$), dvojí negace ($\overline{\overline a}=a$), **absorbce** ($a+ab=a$), **absorbce negace** ($a+\overline a b=a+b$), **de Morgan** ($\overline{a+b}=\overline a\,\overline b$), **consensus** ($ab+\overline a c+bc=ab+\overline a c$). Každý zákon platí i v duálním tvaru (princip duality).

## Úplný soubor logických funkcí
$\{+,\cdot,\neg\}$ je úplný systém. Úplným systémem je i **samotný NAND**, resp. **samotný NOR** — proto se ASIC realizují právě těmito hradly (nejméně tranzistorů).

## Související
- [[Kombinační-obvod]]
- [[Karnaughova-mapa]]
