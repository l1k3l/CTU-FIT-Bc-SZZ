---
studyplan: true
etapa: "6 · ZUM — Holeňa"
qid: "24ZUM"
examiner: "Holeňa"
topic: "Genetické algoritmy a programování, operátory, evoluční strategie"
readiness: nezačato
tags: [otázka, kurz/ZUM, otázka/24, todo]
---

# Genetické a evoluční algoritmy

> **Otázka SZZ:** Genetický algoritmus a genetické programování. Genetické operátory (selekce, křížení, mutace). Evoluční programování a optimalizace, evoluční strategie.

Zdroje: BI-ZUM (FIT ČVUT), přednáška 11 — *Evoluční výpočetní techniky*.

Značení: populace velikosti $\mu$, jedinec $x$, fitness $f(x)$, chromozom $\in \{0,1\}^n$, pravděpodobnost mutace $p_m$.

---

## 1. Evoluční algoritmy — princip

**Evoluční algoritmy** jsou rodina metod **stochastické populační iterativní optimalizace** inspirovaných evoluční biologií (Mendelova dědičnost, Darwinův přírodní výběr — „přežití silnějšího"). Navazují na [[23ZUM-long|lokální prohledávání (ot. 23)]] tím, že pracují s **populací** vzájemně interagujících kandidátů, ne s jediným řešením.

Princip „šlechtění": kvalitní jedinci jsou **selekcí** vybráni k **reprodukci** (**křížení** + **mutace**), čímž vzniká nová **generace**.

**Pojmosloví:**
- **genotyp** — reprezentace řešení (binární řetězce, vektory $\mathbb{R}^n$, stromy); **fenotyp** — význam/sémantika řešení,
- **fitness** — kriteriální funkce (míra adaptace jedince),
- **jedinec** — kandidující řešení (dvojice genotyp + fitness), **populace** — množina jedinců, **generace** — čítač hlavních cyklů.

**Obecné schéma:** Inicializace → **opakuj** { Selekce → Rodiče → Křížení → Mutace → Potomci → Náhrada } dokud není splněna ukončovací podmínka.

---

## 2. Genetický algoritmus (GA)

**[[Genetický-algoritmus|Genetický algoritmus]]** (J. Holland, 70. léta) je univerzální „black-box" optimalizátor binárních řetězců (**chromozomů**) pevné délky $n$:
$$\max_{\mathbf{x} \in \{0,1\}^n} f(\mathbf{x}).$$

```
P ← μ náhodných jedinců
repeat
    O ← {}
    for i ← 1 to μ/2 do
        p1 ← selection(P);  p2 ← selection(P)
        (o1, o2) ← crossover(p1, p2)
        O ← O ∪ { mutate(o1), mutate(o2) }
    P ← O                      # generační náhrada
until ukončovací podmínka
```

**Příklad — problém batohu (NP-úplný):** řešení zakódováno binárním vektorem (i-tá složka = vlož předmět $i$?); fitness = součet cen vložených předmětů, je-li dodržena kapacita $W$, jinak 0.

---

## 3. Genetické operátory

- **Selekce** (výběr rodičů podle fitness):
  - **ruletová** (proporcionální): $P_i = f_i / \sum_{j=1}^{\mu} f_j$ — pravděpodobnost výběru úměrná fitness,
  - **turnajová**: vylosuj $k$ jedinců, vyber nejlepšího (necitlivá na konkrétní hodnoty fitness, jen na pořadí).
- **Křížení (rekombinace):** výměna informace mezi dvěma rodiči — **jednobodové**, **dvoubodové**, **n-bodové**, **uniformní** (každý bit nezávisle od jednoho z rodičů). Lze i zcela vynechat.
- **Mutace:** drobná náhodná změna genotypu — **bit-flip**: invertuj každý bit s malou pravděpodobností $p_m \approx 10^{-2}$.

---

## 4. Genetické programování (GP)

**GP** (J. R. Koza, 90. léta) — genotypem jsou **orientované kořenové [[Strom|stromy]]** (programy/výrazy, původně S-expressions jazyka LISP), nikoli řetězce pevné délky. Struktura *i velikost* řešení jsou předmětem evoluce.

Strom sestává z **funkcí $F$** (vnitřní uzly — aritmetické/logické operace) a **terminálů $T$** (listy — proměnné, konstanty). Inicializace: metody GROW / FULL (omezené hloubkou $D_{\max}$).
- **Křížení:** výměna dvou náhodně zvolených **podstromů** mezi rodiči.
- **Mutace:** subtree (záměna podstromu za náhodný), point (uzel za uzel stejné arity), shrink (podstrom za terminál), permutace argumentů.

---

## 5. Evoluční programování (EP)

**EP** (L. J. Fogel, 1960; ještě před GA) — cílem bylo „vyšlechtit umělou inteligenci". Chování agentů je vyjádřeno **[[Konečný-automat|stavovými automaty]]** (popsanými množinou stavů a **tabulkou přechodů**); mutace mění stavy / tabulku přechodů. **Používá pouze mutaci — křížení chybí.**

---

## 6. Evoluční strategie (ES)

**ES** (I. Rechenberg, H. P. Schwefel, 60. léta) — genotypem jsou **vektory reálných čísel** $\mathbb{R}^n$.

**Selekce / notace:**
- $(1 + \lambda)$-ES: 1 rodič vyprodukuje $\lambda$ potomků, nejlepší je rodičem další generace — *de facto odpovídá [[Hill-climbing|hill climbingu]]*,
- $(\mu + \lambda)$-ES: z $\mu$ rodičů + $\lambda$ potomků vybráno $\mu$ nejlepších (**elitní** — rodiče soutěží s potomky),
- $(\mu, \lambda)$-ES: $\mu$ nejlepších *jen z potomků* (neelitní).

**Mutace:** **gaussovská** — přičtení čísla z [[Normální-rozdělení|normálního rozdělení]] (malé změny časté, velké vzácné). Pokročilé verze používají **self-adaptaci** kroku: jedinec si nese i vektor směrodatných odchylek $\sigma$, který se sám vyvíjí (**pravidlo 1/5**: má-li mutace úspěšnost > 1/5, zmenši $\sigma$, jinak zvětši). Křížení (moderně) uniformní — diskrétní (kopie složky od jednoho rodiče) nebo aritmetické (průměr).

---

## 7. Evoluční optimalizace: explorace vs. exploatace

EA je kompromis dvou principů:
- **exploatace** (lokální složka): šplhání do kopce, zkoumání okolí — operátory **selekce (+ křížení)**,
- **explorace** (globální složka): náhodné procházky bránící uváznutí — operátory **mutace (+ křížení)**.

Poměr řídí **selekční tlak** a **míra mutace**. Hlavní hrozba je **předčasná konvergence** — populace zestejní, mutace ji nezlepší a křížení nefunguje (jedinci jsou příliš podobní); odpovídá uvíznutí v lokálním optimu. Zmírnění: dynamická míra mutace (i v kombinaci se [[Simulované-žíhání|simulovaným žíháním]]) a **niching** (ostrovní model, fitness sharing, deterministic crowding, novelty search) — udržení diverzity dělením populace na „druhy".

---

## Co je potřeba na zkoušku znát

### Definice
- **Evoluční algoritmus:** populační iterativní optimalizace; genotyp/fenotyp, fitness, jedinec, populace, generace.
- **Schéma:** inicializace → (selekce → křížení → mutace → náhrada)*.

### Genetické operátory
- **Selekce:** ruletová ($P_i = f_i/\sum f_j$), turnajová (nejlepší z $k$).
- **Křížení:** jedno-/dvou-/n-bodové, uniformní.
- **Mutace:** bit-flip s $p_m \approx 10^{-2}$.

### Paradigmata (rozlišit!)
- **GA:** binární řetězce $\{0,1\}^n$; všechny operátory.
- **GP:** stromy (programy); křížení = výměna podstromů.
- **EP:** stavové automaty; **jen mutace, bez křížení**.
- **ES:** reálné vektory $\mathbb{R}^n$; gaussovská mutace + self-adaptace $\sigma$; notace $(\mu + \lambda)$ / $(\mu, \lambda)$; $(1+\lambda) \approx$ hill climbing.

### Pointa
**Explorace vs. exploatace**; hrozba **předčasné konvergence** = uvíznutí v lokálním optimu.
