---
tags: [otázka, kurz/ZUM, otázka/21, todo]
---

# 21 — Stavový prostor a neinformované prohledávání (zkrácená verze)

## Stavový prostor
[[Stavový-prostor|Stavový prostor]] = [[Orientovaný-graf|orientovaný graf]] $(S,A)$: uzly = **stavy** $S$, hrany = **akce** $A\subseteq S\times S$. Úloha $(\mathcal{I}, G)$: počáteční stav $\mathcal{I}$, koncové stavy $G\subseteq S$. Následníci $\Gamma(s)=\{s'\mid (s,s')\in A\}$. Hledáme **cestu** z $\mathcal{I}$ do $G$ (hrany bez vah).

## Stromová expanze
Konstrukce **prohledávacího stromu** (kořen $\mathcal{I}$): opakovaně vyber list a **expanduj** = připoj všechny následníky. Stavy uzlu: **FRESH / OPEN / CLOSED** (zákaz duplicit). Strategie se liší jen výběrem listu / strukturou `open`.

Kritéria: **úplnost, optimalita, čas, paměť** ($b$ = větvící faktor, $d$ = hloubka řešení).

## Strategie (společné schéma, liší se `open`)

| Strategie | `open` | úplnost | optimalita | poznámka |
|---|---|---|---|---|
| **náhodné** | množina (náhodný výběr) | ne | ne | nepoužitelné |
| **[[BFS]]** | fronta (FIFO) | ano | min. počet hran | čas i paměť $O(b^d)$ |
| **[[DFS]]** | zásobník (LIFO) | konečný graf ano | ne | paměťově úsporné |

BFS expanduje „po patrech"; DFS se maximálně zanořuje. Stejný kód, jiná struktura `open`.

**Doptávání:** BFS nepoužitelné kvůli **paměti** ($b^d$ uzlů na patro; $b{=}10,d{=}20 \to 10^{20}$). BFS = Dijkstra pro jednotkové ceny. DFS implementace: explicitní zásobník / rekurze (zásobník volání). Cíl se testuje při odebrání z `open`.

---

## Co odpovědět rychle
- **Stavový prostor** $(S,A)$, úloha $(\mathcal{I},G)$, $\Gamma(s)$.
- **Expanze** listu, FRESH/OPEN/CLOSED, kritéria úplnost/optimalita/čas/paměť.
- **BFS** = fronta, úplné, optimální v hranách, $O(b^d)$; **DFS** = zásobník, paměťově úsporné, neoptimální; **náhodné** = množina, nepoužitelné.
