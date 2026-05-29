---
aliases: [lokální extrém, lokální extrémy, lokálního extrému, lokální maximum, lokální minimum, ostré lokální maximum, ostré lokální minimum, globální extrém, globální maximum, globální minimum, stacionární bod, extrém, extrémy, local extremum]
tags: [definice, kurz/MA1]
---

# Lokální extrém

## Definice

Funkce $f$ má v bodě $a \in D_f$
- **lokální maximum** (resp. **minimum**), právě když existuje okolí $U_a \subset D_f$ tak, že $\forall x \in U_a:\ f(x) \le f(a)$ (resp. $\ge f(a)$);
- **ostré** lokální maximum/minimum, platí-li ostrá nerovnost pro $x \in U_a \setminus \{a\}$.

Lokální maximum a minimum souhrnně = **lokální extrém**.

## Nutná podmínka (Fermat)

Má-li $f$ v bodě $a$ lokální extrém, pak **buď $f'(a) = 0$, nebo [[Derivace|derivace]] v $a$ neexistuje**. Body s $f'(a)=0$ se nazývají **stacionární**.

⚠️ Podmínka je jen **nutná**, ne postačující: $f(x)=x^3$ má $f'(0)=0$, ale v $0$ extrém nemá.

## Postačující kritéria

- **Změna monotonie / znaménka $f'$:** je-li $f$ spojitá v $a$ a $f'$ mění v $a$ znaménko (např. $>0$ vlevo, $<0$ vpravo), má $f$ v $a$ ostré lokální maximum (analogicky minimum). Spojitost je podstatná.
- **Druhá derivace:** je-li $f'(c)=0$ a $f$ je v $c$ ryze konvexní (tj. typicky $f''(c)>0$), má $f$ v $c$ ostré lokální **minimum**; ryze [[Konvexní-funkce|konkávní]] ($f''(c)<0$) ⇒ ostré lokální **maximum**.

## Globální extrém

**Globální maximum/minimum** $f$ na množině $M$ je $\max_M f$ / $\min_M f$. Spojitá funkce na **uzavřeném intervalu** $\langle a,b\rangle$ globální extrémy vždy nabývá, a to jen v krajních bodech nebo v bodech, kde $f'=0$ nebo neexistuje.

## Související

- [[Derivace]]
- [[Konvexní-funkce]]
- [[Spojitost]]
