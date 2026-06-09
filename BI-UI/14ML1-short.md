---
tags: [otázka, kurz/ML1, otázka/14, todo]
---

# 14 — Nesupervizované učení, k-means a DBSCAN (zkrácená verze)

## 1. Nesupervizované učení — principy

[[Nesupervizované-učení]] (učení bez učitele): data **bez označení**, žádná vysvětlovaná proměnná. Cíl = **porozumět vnitřní struktuře dat** jen z dat samotných.

**Tři paradigmata ML:** **supervizované** (data s označením → predikce), **nesupervizované** (bez označení → struktura), **posílené** (agent interaguje s prostředím, dostává odměnu → strategie).

Pravděpodobnostní pohled: data = realizace [[Náhodný-vektor|náhodného vektoru]] $X = (X_1,\dots,X_p)^T$; porozumět struktuře = odhadnout rozdělení, tj. hustotu $f_X$ (spojité), resp. prav. funkci $p_X$ (diskrétní). Hledáme „co nejmenší" oblasti vysoké pravděpodobnosti → **shluky**.

Hlavní problém: **není jasné, jak vyhodnotit úspěšnost** (chybí jedno kritérium) → mnoho algoritmů s rozdílnými výsledky. Proudy: **shlukování**, **redukce dimenzionality**, odhad hustoty.

## 2. Shluková analýza

[[Shluková-analýza|Shlukování]]: roztřídit data do shluků tak, že blízké body spolu, vzdálené zvlášť (požadavky obecně nekompatibilní). Stojí na **[[Metrika|metrice]]** $d$: $d\ge0$ & $d(x,y)=0\!\iff\!x=y$, symetrie, trojúh. nerovnost. ($L_2$, $L_1$, $L_\infty$.)

Vstup: $(\mathcal{X},d)$, data $\mathcal{D}$, příp. $k$. Výstup: rozklad $C=(C_1,\dots,C_k)$, $C_i$ disjunktní, $\bigcup C_i=\mathcal{D}$. (Hierarchické aglomerativní shlukování → ot. 9.)

## 3. k-means

**Účelová funkce (WCSS):**
$$G(C)=\sum_{i=1}^k\frac{1}{2|C_i|}\sum_{x,y\in C_i}\|x-y\|^2=\sum_{i=1}^k\sum_{x\in C_i}\|x-\bar{x}_i\|^2,\quad \bar{x}_i=\tfrac{1}{|C_i|}\textstyle\sum_{x\in C_i}x.$$
Rovnost plyne z tvrzení: $\min_\mu\sum_{x\in A}\|x-\mu\|^2$ se nabývá v centroidu $\bar{x}$. Globální minimum NP-těžké.

**Algoritmus (Lloyd):** zvol $k$ centroidů; opakuj — (1) **přiřazení**: $C_i=\{x\mid i=\arg\min_j\|x-\mu_j\|\}$; (2) **přepočet**: $\mu_i\leftarrow$ geom. střed $C_i$ — dokud se $G$ téměř nemění. V každé iteraci $G$ neroste → konverguje k **lokálnímu** minimu. Iterace $\mathcal{O}(Nkp)$.

Vlastnosti: citlivý na **inicializaci** (proto víc běhů + min $G$, nebo **k-means++**); $k$ se zadává dopředu (**loket/elbow**, silhouette); preferuje **sférické**, podobně velké shluky; citlivý na odlehlé body (neumí šum).

## 4. DBSCAN

Hustotní shlukování (Ester 1996): shluky = souvislé oblasti vysoké hustoty, zbytek = šum. Metrický prostor $(\mathcal{X},d)$, parametry $\varepsilon>0$, $\text{MinPts}$.

- **$\varepsilon$-okolí:** $N_\varepsilon(x)=\{y\in\mathcal{D}\mid d(x,y)\le\varepsilon\}$.
- **Klíčový bod** (core): $|N_\varepsilon(x)|\ge\text{MinPts}$.
- **Okrajový bod** (border): neklíčový, ale přímo dosažitelný z klíčového.
- **Šum** (noise): ani klíčový, ani okrajový; $N=\mathcal{D}\setminus\bigcup_i C_i$.
- **Přímá dosažitelnost:** $y$ přímo dosažitelný z $x$ $\iff$ $x$ klíčový $\wedge$ $y\in N_\varepsilon(x)$. (Symetrická jen pro dvojici klíčových.)
- **Dosažitelnost:** řetězec $x_1{=}x,\dots,x_n{=}y$, kde $x_{i+1}$ přímo dosažitelný z $x_i$ (všechny kromě posledního klíčové).
- **Spojenost:** $\exists p$ (klíčový): $x$ i $y$ dosažitelné z $p$. (Symetrická.)
- **Shluk:** maximální množina vzájemně **spojených** bodů (maximalita + souvislost), obsahuje $\ge\text{MinPts}$ bodů.

**Algoritmus (idea):** najdi klíčové body; přímo dosažitelné klíčové spoj do zárodků shluků; každý okrajový bod přidej ke shluku klíčového ve svém okolí, ostatní → šum. Složitost $\mathcal{O}(N^2)$, s prostorovým indexem až $\mathcal{O}(N\log N)$.

Výhody: pracuje s **hustotou bodů** → **libovolný (nekonvexní/nelineární) tvar shluků** (např. „švýcarská rolka"), **detekce šumu** (odolnost k odlehlým bodům), **nezadává se $k$**. Nevýhody: parametry $\varepsilon$, MinPts se **ladí těžko** ($\varepsilon$ důležitější; MinPts $\approx 4$–$6$), potíže s různou hustotou shluků (jediné $\varepsilon$ nestačí).

### k-means vs. DBSCAN

| | k-means | DBSCAN |
|---|---|---|
| princip | minimalizace WCSS kolem centroidů | hustota ($\varepsilon$-okolí, MinPts) |
| tvar shluků | sférické, podobně velké | libovolný (nekonvexní) |
| počet shluků | $k$ zadán dopředu | vyplyne z dat |
| šum / odlehlé | neumí (vše zařadí) | označí jako šum |
| parametry | $k$, inicializace | $\varepsilon$, MinPts |
| výstup | lokální minimum (víc běhů) | deterministický (až na okrajové body) |
| složitost | $\mathcal{O}(Nkp)$/iter. | $\mathcal{O}(N^2)$ ($N\log N$ s indexem) |

## 5. Silhouette skóre (evaluace)

$a(x)$ = prům. vzdálenost $x$ od bodů **svého** shluku; $b(x)=\min_{i\ne j(x)}d(x,C_i)$ = prům. vzdálenost k **nejbližšímu cizímu** shluku.
$$s(x)=\frac{b(x)-a(x)}{\max\{a(x),b(x)\}}\in[-1,1].$$
$\approx1$ dobře zatříděn, $\approx0$ na hranici, $\approx-1$ špatně přiřazen. Průměr $s=\frac1{|\mathcal{D}|}\sum_x s(x)$ — čím vyšší, tím lepší; maximum přes $k$ → vhodný počet shluků.

---

## Co odpovědět rychle

- **Nesup. učení:** neoznačená data, cíl = struktura dat (odhad rozdělení/hustoty $f_X$); shlukování + redukce dim.; problém = evaluace.
- **Shlukování:** rozklad $\mathcal{D}$ na disjunktní shluky podle vzdálenosti (metrika $d$).
- **k-means:** optimalizuje (minimalizuje) WCSS = součet kvadrátů vzdáleností od centroidů $\sum_i\sum_{x\in C_i}\|x-\bar{x}_i\|^2$; Lloyd = přiřaď k nejbližšímu centroidu → přepočti centroidy; $G$ neroste → **konverguje k lokálnímu min**; zadej $k$ (**elbow** nad WCSS / silhouette / dáno úlohou), sférické shluky, k-means++.
- **DBSCAN:** klíčový bod ($\ge$ MinPts v $\varepsilon$-okolí), dosažitelnost, spojenost; **shluk = max. množina spojených bodů**, zbytek šum; libovolný tvar, detekce šumu, nezadává $k$; parametr $\varepsilon$.
- **Silhouette:** $s(x)=\frac{b-a}{\max\{a,b\}}\in[-1,1]$, vyšší = lepší; volba $k$.
