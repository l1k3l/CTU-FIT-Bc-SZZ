---
studyplan: true
etapa: "6 · ZUM — Holeňa"
qid: "22ZUM"
examiner: "Holeňa"
topic: "Heuristické prohledávání, heuristiky, hladové prohledávání, A*"
readiness: nezačato
tags: [otázka, kurz/ZUM, otázka/22, todo]
---

# Heuristické prohledávání a A*

> **Otázka SZZ:** Heuristické prohledávání stavového prostoru, heuristiky pro odhad ceny cesty, hladové prohledávání, algoritmus A*.

Zdroje: BI-ZUM (FIT ČVUT), přednáška 3 — *Heuristické prohledávání stavového prostoru*.

Značení: dosud ujetá cena $g(s)$, heuristický odhad zbývající cesty $h(s)$, evaluační funkce $f(s)$, cena akce $c(x,y)$, optimální heuristika $h^*$.

---

## 1. Ohodnocený stavový prostor a cena cesty

Počet hran není vždy relevantní (silnice mají různé délky). **Ohodnocený [[Stavový-prostor|stavový prostor]]** je trojice $(S, A, c)$ s **cenou akce** $c : A \to \mathbb{R}_0^+$. **Cena cesty** $p = (s_1, a_1, \dots, a_{n-1}, s_n)$:
$$C(p) = \sum_{i=1}^{n-1} c(a_i).$$

**[[Dijkstra|Dijkstrův algoritmus]]** najde nejlevnější cestu (k expanzi volí OPEN uzel s nejmenší dosavadní cenou $g$, při nalezení levnější cesty provádí **relaxaci**) v čase $O(|A| + |S|\log|S|)$ pro nezáporné ceny. Je optimální, ale prohledává **všesměrově** (jen podle $g$) → zbytečně expanduje irelevantní stavy. Pro prostory s $\sim 10^{100}$ stavy nestačí.

**Idea informovaného prohledávání:** mít navíc **odhad** ceny cesty z OPEN uzlů do cíle a expandovat „inteligentněji" → **heuristická funkce**.

---

## 2. Heuristika pro odhad ceny cesty

**[[Heuristika|Heuristika]]** (heuristická funkce) je libovolná
$$h : S \to \mathbb{R}_0^+,$$
kde $h(s)$ je **odhad ceny** nejlevnější cesty z $s$ do nejbližšího cíle a $h(s_g) = 0$ pro všechna $s_g \in G$. Funguje jako „orákulum" radící, který uzel expandovat.

**Příklad (mapa):** **vzdušná vzdálenost** k cíli — euklidovská (rovinné souřadnice) nebo délka ortodromy (sférické). 

**Optimální heuristika** $h^*(s)$ = *skutečná* cena nejlevnější cesty z $s$ do cíle. S $h^*$ by greedy šel rovnou do cíle; v praxi je ale nedosažitelná. Teoreticky: lepší (přípustnou) heuristiku nelze sestrojit.

---

## 3. Hladové prohledávání (greedy best-first)

**[[Hladové-prohledávání|Hladové prohledávání]]** v každém kroku expanduje OPEN stav s **minimální heuristikou**:
$$s^* \in \arg\min_{s \in OPEN} h(s) \qquad (\text{tj. } f(s) = h(s)).$$
Snaží se co nejrychleji („hladově") přiblížit cíli — má „tah na bránu".

**Vlastnosti:**
- **není optimální** — nalezená cesta nemusí být nejlevnější (zohledňuje jen odhad zbývající cesty, ne dosud ujetou cenu),
- kvalita zcela závisí na heuristice; greedy se nechá svést překážkou nebo jde oklikou. (Pozor: BFS = Breadth-First Search $\ne$ best-first search.)

---

## 4. Algoritmus A*

**[[A-star|A*]]** kombinuje oba přístupy — Dijkstrovu dosud ujetou cenu $g$ i hladový odhad $h$:
$$f(s) = g(s) + h(s),\qquad s^* \in \arg\min_{s \in OPEN} f(s).$$
`open` je prioritní fronta podle $f$; při nalezení levnější cesty se klíč $f$ aktualizuje (relaxace). Má „tah na bránu" (jako greedy) i nárok na optimalitu (jako Dijkstra).

Speciální případy: $h \equiv 0 \Rightarrow$ Dijkstra; vynechání $g \Rightarrow$ greedy.

```
open ← priority_queue();  dist[I] ← 0;  enqueue(open, I, h(I))
while ¬empty(open) do
    x ← dequeue(open)                       # min f
    if x ∈ G then return reconstruct_path(prev, x)
    for all y ∈ Γ(x) \ closed do
        d' ← dist[x] + c(x, y)              # nové g
        if y ∉ open ∨ dist[y] > d' then
            dist[y] ← d';  prev[y] ← x
            enqueue/update(open, y, d' + h(y))   # klíč f = g + h
    closed ← closed ∪ {x}
```

---

## 5. Vlastnosti heuristik a optimalita A*

### Přípustnost (admissibility)
$h$ je **přípustná**, je-li $\forall s : h(s) \le h^*(s)$ — nikdy nepřeceňuje, je „optimistická". *Příklad:* vzdušná vzdálenost je přípustná (pozemní vzdálenost je vždy $\ge$ vzdušná).

### Monotónnost / konzistence
$h$ je **monotónní (konzistentní)**, je-li
$$\forall (x, y) \in A : h(x) - c(x, y) \le h(y)$$
(trojúhelníková nerovnost $h(x) \le c(x, y) + h(y)$). Platí **konzistence $\Rightarrow$ přípustnost**.

### Optimalita A* (podmínky z přednášky)
- $h$ **monotónní** $\Rightarrow$ je i přípustná a A* (s množinou CLOSED, tj. *grafové* prohledávání) **najde optimální řešení**;
- $h$ **přípustná, ale nekonzistentní** $\Rightarrow$ A* je optimální, *jen nepoužívá-li CLOSED* (stromové prohledávání / znovuotevírání uzlů);
- $h$ **nepřípustná** $\Rightarrow$ optimalita není zaručena.

> A* je optimální algoritmus pro danou heuristiku — „lepší algoritmus neexistuje, zbývá jen zlepšovat heuristiky".

### Dominance
Pro přípustné $h_1, h_2$: $h_1$ **dominuje** $h_2$, je-li $\forall s : h_1(s) \ge h_2(s)$. Dominující (informativnější) heuristika expanduje „v průměru" méně uzlů. Ale *nemusí* být rychlejší — vyšší informativnost často znamená vyšší cenu výpočtu na uzel. Kompromis: rychlá málo informativní vs. pomalá hodně informativní heuristika.

---

## Co je potřeba na zkoušku znát

### Definice
- **Ohodnocený stavový prostor** $(S,A,c)$, **cena cesty** $C(p) = \sum c(a_i)$.
- **Heuristika** $h : S \to \mathbb{R}_0^+$, $h(\text{cíl}) = 0$; **optimální** $h^*$ = skutečná cena.
- **Přípustnost** $h \le h^*$; **konzistence** $h(x) \le c(x,y) + h(y)$; **dominance** $h_1 \ge h_2$.

### Algoritmy (best-first)
- **Dijkstra:** $f = g$; optimální, všesměrový, $O(|A| + |S|\log|S|)$.
- **Greedy:** $f = h$; „tah na bránu", **neoptimální**.
- **A\*:** $f = g + h$; optimální při konzistentní (resp. přípustné bez CLOSED) heuristice.

### Klíčové vztahy
- konzistence ⇒ přípustnost; A* s konzistentní $h$ + CLOSED = optimální.
- dominance ⇒ méně expanzí, ne nutně rychleji.
