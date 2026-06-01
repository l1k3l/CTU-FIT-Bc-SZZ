---
tags: [otázka, kurz/PA2, otázka/23, todo]
---

# Abstraktní datový typ a jeho implementace

> **Otázka SZZ:** Abstraktní datový typ, jeho specifikace a implementace. Zásobník, fronta, pole, seznam, tabulka, množina. Implementace pomocí spojových struktur, stromů a pole.

Zdroje: BI-PA2 přednášky l10, l11 (abstraktní datové typy), l05 (STL kontejnery); reprezentace stromů/hešování viz BI-AG1 (Vagner, Vogel, FIT ČVUT).

---

## 1. Abstraktní datový typ — specifikace a implementace

![[Abstraktní-datový-typ#Definice]]

### Tři vrstvy
- **[[Datový-typ|Datový typ]]** = množina hodnot + operace **+ konkrétní implementace** (paměťová reprezentace). Vestavěné typy (`int`, …) ji mají hotovou.
- **[[Abstraktní-datový-typ|ADT]]** = množina hodnot + operace **bez** implementace.
- **Datová struktura** = rozhraní jako u ADT **+ paměťová reprezentace + algoritmy** operací (ve vhodném abstraktním modelu). V C++ se ADT typicky realizují jako **generické třídy** ([[Šablona|šablony]]).

### Specifikace
- **Specifikace = co.** Formálně: **signatura operací** (definice **syntaxe** — arita, typy operandů a výsledku, notace) + **množina axiomů** (definice **sémantiky** — ekvivalence mezi výrazy reprezentujícími stav). Neformálně: signatury + sémantika slovem/obrázkem.
- **Implementace = jak.** Tentýž ADT lze implementovat různě (polem, [[Spojový-seznam|spojovou strukturou]], [[Strom|stromem]], hešováním) — liší se časové i paměťové složitosti operací. Specifikace neříká nic o tom, jak rychle (a zda) lze ADT implementovat.

Příklad formální specifikace na zásobníku viz §2.

---

## 2. Zásobník (Stack)

![[Zásobník#Specifikace]]

**Implementace a složitost:** pole pevné délky / dynamické pole (omezená kapacita, $O(1)$), **[[Nafukovací-pole|nafukovací pole]]** (neomezené, push/pop **amortizovaně** $O(1)$), **[[Spojový-seznam|spojový seznam]]** (vkládání/odebírání na začátku, $O(1)$). V STL `std::stack`.

---

## 3. Fronta (Queue)

**[[Fronta]]** je ADT s disciplínou **FIFO** (First In, First Out). Operace: `empty`, `enqueue` (přidá na konec), `dequeue` (vyjme nejstarší).

**Implementace:**
- **Nafukovací pole — souvislý úsek:** vkládá na konec, odebírá posunem počítadla začátku; když je vpředu příliš místa, prvky se přesunou na začátek (lineární, ale vzácné) → enqueue **amortizovaně** $O(1)$.
- **Kruhové pole** (indexace modulo, `data[(i+first) % cap]`): bez změny velikosti jsou **všechny operace** $O(1)$ i v nejhorším případě.
- **Spojový seznam** s ukazatelem na konec: enqueue i dequeue $O(1)$.

**Prioritní fronta** („fronta s předbíháním"): `insert` (s prioritou) + `extract_min`; efektivní implementace **[[Binární-halda|binární haldou]]** ($O(\log n)$). V STL `std::queue`, `std::priority_queue`, `std::deque`.

---

## 4. Pole (Array)

![[Pole#Definice]]

Prvky leží v souvislém bloku, pozici počítá **mapovací funkce** (1D: `map(i) = i - l_1`); vícedimenzionální pole se serializuje **po řádcích** (row-major) / **po sloupcích** (column-major) nebo přes **přístupové (Iliffeho) vektory** (pole polí — i neobdélníkové matice). Pole je nositelem **náhodného přístupu v $O(1)$** a základním stavebním blokem ostatních ADT.

---

## 5. Seznam (spojový seznam)

V BI-PA2 znamená **„seznam" konkrétně [[Spojový-seznam|spojový seznam]]** — lineární spojovou strukturu uzlů, kde každý uzel nese data a **[[Ukazatel|ukazatel]] na následníka** (poslední na `nullptr`). Není zaveden zvláštní abstraktní „List ADT" s pozicí/kurzorem; abstraktní sekvence se objevuje až jako STL `std::list` (obousměrný) / `std::forward_list` (jednosměrný).

- **Varianty:** jednosměrný / obousměrný / kruhový / se zarážkou.
- **Operace:** vložení na začátek $O(1)$; na konec $O(1)$ s ukazatelem na poslední prvek, jinak $O(n)$; hledání/průchod $O(n)$; přístup přes index **není** $O(1)$.
- **Režie:** u malých prvků (např. `int`) zabírá ukazatel 50–67 % paměti navíc oproti poli.

Seznam slouží jednak jako **implementace** jiných ADT (zásobník, fronta, řetízky v hešování), jednak jako neseřazená/seřazená reprezentace množiny a mapy (§9).

---

## 6. Tabulka (mapa, slovník)

V BI-PA2 jsou **tabulka = mapa = [[Slovník|slovník]]** synonyma pro **asociativní** ADT klíč → hodnota: kontejner hodnot typu `Value`, prvek identifikován **klíčem** typu `Key`.

**Operace:** `set(k,v)` (nastav hodnotu), `get(k)` (získej), `erase(k)`, `contains(k)`.

Mapa je úzce příbuzná s **množinou**: mapu lze získat z množiny klíčonosných struktur (porovnání ignoruje hodnotu) a naopak množina je mapa s jednoprvkovým typem hodnoty. Implementace a složitosti jsou proto stejné jako u množiny (§7). V STL `std::map` (strom, $O(\log n)$), `std::unordered_map` (hešování, průměrně $O(1)$).

---

## 7. Množina (Set)

![[Množina#Definice]]

Implementace a složitosti (učebnicová srovnávací tabulka):

| implementace | insert | erase | contains | ∪ / ∩ | equal |
|---|---|---|---|---|---|
| charakteristický vektor | $O(1)$ | $O(1)$ | $O(1)$ | $O(\|U\|)$ | $O(\|U\|)$ |
| neseřazené pole / seznam | $O(n)$ | $O(n)$ | $O(n)$ | $O(nm)$ | $O(n^2)$ |
| seřazené **pole** | $O(n)$ | $O(n)$ | $O(\log n)$ | $O(n{+}m)$ | $O(n)$ |
| seřazený **seznam** | $O(n)$ | $O(n)$ | $O(n)$ | $O(n{+}m)$ | $O(n)$ |
| nevyvážený strom | $O(n)$ | $O(n)$ | $O(n)$ | $O(n{+}m)$ | $O(n{+}m)$ |
| vyvážený strom | $O(\log n)$ | $O(\log n)$ | $O(\log n)$ | $O(n{+}m)$ | $O(n{+}m)$ |
| hešování | $O(1)^{*}$ | $O(1)^{*}$ | $O(1)^{*}$ | $O(n{+}m)$ | $O(n{+}m)$ |

($^{*}$ průměrný případ; nevyvážený strom je nejhorší případ, v průměru jako vyvážený.)

- **Charakteristický vektor** (`bool`/bitové pole, `std::optional<Value>` pro mapu): složitost závisí na velikosti **univerza** $|U|$, ne množiny; paměť $\Theta(|U|)$. Vhodné, jen je-li univerzum malé.
- **Seřazené pole** → binární hledání (contains $O(\log n)$), množinové operace mergem $O(n+m)$; **seřazený seznam** binární hledání neumožní (contains $O(n)$).

---

## 8. Implementace pomocí pole

- **Náhodný přístup $O(1)$**, kompaktní (bez režie ukazatelů). Statické (pevná velikost) nebo **nafukovací** (zdvojnásobování kapacity → vkládání na konec amortizovaně $O(1)$).
- Použití: zásobník, fronta (souvislý úsek i **kruhové pole**), **binární halda** (synové uzlu `i` na `2i`, `2i+1`; otec `⌊i/2⌋`), seřazená/neseřazená množina (binární hledání jen v seřazeném poli).
- Nevýhody: vkládání/mazání „doprostřed" je $O(n)$ (posun prvků), realokace při růstu.

---

## 9. Implementace pomocí spojových struktur

- **[[Spojový-seznam|Spojový seznam]]**: uzly spojené ukazateli; vkládání/mazání na známém místě $O(1)$, bez náhodného přístupu, s paměťovou režií ukazatelů.
- Použití: zásobník (jednosměrný, vkládání na hlavu), fronta (ukazatel na konec), neseřazená/seřazená množina a mapa (operace jako u odpovídajícího pole, ale contains v seřazeném seznamu zůstává $O(n)$), **řetízky** při [[Hešování-s-řetízky|hešování s řetízky]] (kolize ve stejné přihrádce).
- Obecně: spojové struktury jsou flexibilní (růst po prvku, levné vkládání/mazání na místě), ale ztrácí lokalitu a náhodný přístup.

---

## 10. Implementace pomocí stromů

### Binární vyhledávací strom (BVS)
**[[BVS|Binární vyhledávací strom]]** vyžaduje lineární uspořádání klíčů: v každém uzlu mají klíče levého podstromu menší a pravého podstromu větší hodnotu. **InOrder průchod** vydá klíče vzestupně. Operace (find, insert, delete — 3 varianty mazání dle počtu synů) běží v $O(h)$, kde $h$ je hloubka.

- **Vyváženost:** dokonale vyvážený strom má $h = \lfloor\log_2 n\rfloor$, ale nelze ho levně udržovat; vkládání seřazené posloupnosti dá **degenerovaný** strom $h = O(n)$.
- Řešení: hloubkově vyvážené stromy přeuspořádávané **rotacemi** — **[[AVL-strom|AVL stromy]]** (BI-AG1), červeno-černé stromy (BI-AG2), treapy, splay stromy. (PA2 ukazuje i „líné vyvažování" přes velikost podstromů a periodickou přestavbu.)
- Použití: vyvážený strom je implementací **množiny** a **mapy** s $O(\log n)$ na operaci (STL `std::set`, `std::map` = červeno-černý strom).

### Binární halda
**[[Binární-halda|Binární halda]]** je téměř úplný binární strom (poslední hladina zleva) s haldovým uspořádáním (priorita otce ≤ priorita syna), uložený v **poli**. Hloubka je $O(\log n)$ → `insert`/`extract_min` $O(\log n)$ (oprava `bubble_up`/`bubble_down`). Implementuje **prioritní frontu** (STL `std::priority_queue`).

### Hešovací tabulka (souvislost se stromy)
Alternativa stromu pro množinu/mapu je **[[Hešovací-tabulka|hešovací tabulka]]** (průměrně $O(1)$); kolize se řeší [[Hešování-s-řetízky|řetízky]] nebo [[Otevřená-adresace|otevřenou adresací]].

> Pozn. (terminologie): PA2 nazývá řetězení „**otevřené hashování**" a zároveň „**uzavřená adresace**" — opačně, než bývá v anglické literatuře (kde *open addressing* = adresace bez řetízků). Hešovací funkce jsou předmětem BI-AG1.

---

## 11. Co je potřeba na zkoušku znát

### Definice
ADT (množina hodnot + operace bez implementace); rozdíl **specifikace** (signatury + axiomy) vs. **implementace** (datová struktura: reprezentace + algoritmy); LIFO zásobník, FIFO fronta, prioritní fronta; pole a mapovací funkce; spojový seznam; tabulka/mapa (klíč→hodnota) vs. množina; BVS, vyváženost, binární halda, hešování.

### Formální specifikace
Umět napsat signatury a axiomy **zásobníku** (`init/empty/push/top/pop`; `top(init)=error`, `pop(push(s,x))=s`, …).

### Implementace a složitosti
- Zásobník/fronta: $O(1)$ (nafukovací pole amortizovaně; kruhové pole worst-case $O(1)$ bez realokace).
- Množina/mapa: srovnávací tabulka (charakteristický vektor / (ne)seřazené pole / (ne)seřazený seznam / (ne)vyvážený strom / hešování) — zejména contains: seřazené **pole** $O(\log n)$ vs. seřazený **seznam** $O(n)$.
- Stromy: BVS $O(h)$, vyvážený $O(\log n)$; degenerace na $O(n)$; binární halda $O(\log n)$.

### Mapování na STL
`std::array`/`std::vector` (pole), `std::list`/`std::forward_list` (seznam), `std::stack`/`std::queue`/`std::deque`/`std::priority_queue`, `std::set`/`std::map` (strom), `std::unordered_set`/`std::unordered_map` (hešování).

## Související pojmy
[[Abstraktní-datový-typ]] · [[Datový-typ]] · [[Zásobník]] · [[Fronta]] · [[Pole]] · [[Spojový-seznam]] · [[Slovník]] · [[Množina]] · [[BVS]] · [[AVL-strom]] · [[Binární-halda]] · [[Hešovací-tabulka]] · [[Nafukovací-pole]]
