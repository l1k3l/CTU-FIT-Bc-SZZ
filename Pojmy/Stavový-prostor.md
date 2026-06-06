---
aliases: [stavový prostor, stavového prostoru, stavovém prostoru, stavovým prostorem, stavové prostory, stavových prostorů, prohledávání stavového prostoru, ohodnocený stavový prostor, cena cesty, stromová expanze]
tags: [definice, kurz/ZUM]
---

# Stavový prostor

## Definice

**Stavový prostor** je [[Orientovaný-graf|orientovaný graf]] $(S, A)$, který lze prohledávat:
- uzly = **stavy** (množina $S$) — popis stavu řešeného problému,
- hrany = **akce** (množina $A \subseteq S \times S$) — přechody mezi stavy.

Úloha prohledávání je zadána **počátečním stavem** $\mathcal{I} \in S$ a množinou **koncových (cílových) stavů** $G \subseteq S$. **Následníci** stavu $s$ jsou $\Gamma(s) = \{s' \in S \mid (s, s') \in A\}$. Řešením je **cesta** $(s_1, a_1, s_2, \dots, a_{n-1}, s_n)$ z $\mathcal{I}$ do nějakého stavu z $G$.

## Ohodnocený stavový prostor

Trojice $(S, A, c)$ s **cenou akce** $c : A \to \mathbb{R}_0^+$. **Cena cesty** $p = (s_1, a_1, \dots, a_{n-1}, s_n)$ je
$$C(p) = \sum_{i=1}^{n-1} c(a_i).$$
(Počet hran je jen speciální případ s jednotkovými cenami.)

## Prohledávací strom a expanze

**Prohledávací strom** je [[Strom|orientovaný kořenový strom]] s kořenem $\mathcal{I}$, jehož každá cesta existuje i v grafu $(S, A)$. Hledání cesty se převádí na konstrukci tohoto stromu **stromovou expanzí**: opakovaně se vybere list a *připojí se všichni jeho následníci*; končí se, jakmile je nějaký list koncovým stavem.

Tři stavy uzlu: **FRESH** (nenalezen), **OPEN** (nalezen, neexpandován), **CLOSED** (nalezen a expandován). Při expanzi se nepřipojují uzly už OPEN/CLOSED (zákaz duplicit). Strategie se liší tím, *který* list vybírají a jakou datovou strukturu pro `open` použijí.

## Kritéria hodnocení strategií

- **úplnost** — najde řešení, pokud existuje?
- **optimalita** — najde nejlevnější/nejkratší řešení?
- **časová** a **paměťová složitost** — typicky v parametrech $b$ (větvící faktor) a $d$ (hloubka řešení).

## Související

- Neinformované: [[BFS]], [[DFS]], náhodné prohledávání
- Informované (ohodnocený prostor): [[Dijkstra]], [[Heuristika]], [[Hladové-prohledávání]], [[A-star]]
- [[Orientovaný-graf]], [[Strom]]
