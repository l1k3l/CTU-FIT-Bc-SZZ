---
tags: [otázka, kurz/PA2, otázka/23, todo]
---

# 23 — Abstraktní datový typ a implementace (zkrácená verze)

## 1. [[Abstraktní-datový-typ|ADT]] — specifikace a implementace
- **ADT** = množina hodnot + množina operací, **bez implementace**.
- Vrstvy: **datový typ** (hodnoty+operace+implementace) → **ADT** (bez impl.) → **datová struktura** (rozhraní + paměťová reprezentace + algoritmy).
- **Specifikace = co:** signatury operací (syntaxe) + axiomy (sémantika). **Implementace = jak:** pole / spojová struktura / strom / hešování → různé složitosti.

## 2. [[Zásobník]] (LIFO)
Signatury: `init`, `empty`, `push(s,x)`, `top(s)`, `pop(s)`. Axiomy: `top(push(s,x))=x`, `pop(push(s,x))=s`, `top(init)=error`.
Impl.: pole / nafukovací pole (amort. $O(1)$) / spojový seznam. push, pop = $O(1)$.

## 3. [[Fronta]] (FIFO)
Operace `enqueue`, `dequeue`, `empty`. Impl.: nafukovací pole (souvislý úsek, amort. $O(1)$), **kruhové pole** (modulo, worst-case $O(1)$), spojový seznam (ukazatel na konec).
**Prioritní fronta** (předbíhání) → **[[Binární-halda|halda]]**, $O(\log n)$.

## 4. [[Pole]]
Náhodný přístup $O(1)$, prvek dán $n$-ticí indexů, souvislý blok + mapovací funkce (row-major / column-major / Iliffeho vektory). Statické / nafukovací (zdvojnásobení).

## 5. Seznam = [[Spojový-seznam|spojový seznam]]
Uzly + ukazatel na následníka. Vložení na začátek $O(1)$, hledání $O(n)$, bez indexace v $O(1)$. Varianty: jedno-/obousměrný, kruhový, se zarážkou. Režie ukazatelů.

## 6. Tabulka = mapa = [[Slovník|slovník]]
Asociativní ADT **klíč → hodnota**. Operace `set/get/erase/contains`. = množina s netriviální hodnotou.

## 7. [[Množina]] (set)
Prvky bez duplikátů. `insert/erase/contains` + sjednocení/průnik/rovnost/podmnožina.

**Složitosti (množina/mapa):**

| impl. | insert | erase | contains | ∪/∩ |
|---|---|---|---|---|
| char. vektor | $O(1)$ | $O(1)$ | $O(1)$ | $O(\|U\|)$ |
| neseř. pole/sez. | $O(n)$ | $O(n)$ | $O(n)$ | $O(nm)$ |
| seřaz. **pole** | $O(n)$ | $O(n)$ | $O(\log n)$ | $O(n{+}m)$ |
| seřaz. **seznam** | $O(n)$ | $O(n)$ | $O(n)$ | $O(n{+}m)$ |
| vyváž. strom | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n{+}m)$ |
| hešování | $O(1)^*$ | $O(1)^*$ | $O(1)^*$ | $O(n{+}m)$ |

(seřazené pole → binární hledání; seznam ne ⇒ contains $O(n)$. $^*$ průměr.)

## 8. Implementace
- **Pole:** přístup $O(1)$, kompaktní; vkládání doprostřed $O(n)$. → zásobník, fronta, **halda** (synové `2i,2i+1`), seřazená množina.
- **Spojové struktury:** levné vkládání/mazání na místě, bez náhod. přístupu, režie. → zásobník, fronta, řetízky v hešování.
- **Stromy:** **[[BVS]]** (InOrder = vzestupně, operace $O(h)$); vyvážený ([[AVL-strom|AVL]], červeno-černý) $O(\log n)$, degenerace $O(n)$. → množina, mapa (`std::set/map`). **Halda** → prioritní fronta.
- **Hešování:** [[Hešovací-tabulka|tabulka]] průměrně $O(1)$ ([[Hešování-s-řetízky|řetízky]] / [[Otevřená-adresace|otevřená adresace]]).

---

## Co odpovědět rychle
- **ADT** = hodnoty + operace bez implementace; specifikace (signatury+axiomy) vs implementace.
- **Zásobník** LIFO, **fronta** FIFO — obojí $O(1)$ (kruhové pole / spojový seznam).
- **Množina/mapa**: seřazené pole $O(\log n)$ contains, vyvážený strom $O(\log n)$ vše, hešování průměrně $O(1)$.
- **Stromy**: BVS $O(h)$, nutné vyvažování; halda = prioritní fronta $O(\log n)$.
