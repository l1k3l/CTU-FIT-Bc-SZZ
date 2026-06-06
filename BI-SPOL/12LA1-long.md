---
studyplan: true
etapa: "3 · LA1 / MA2 / LA2 — Petr"
qid: "12LA1"
examiner: "Petr"
topic: "Matice: součin, inverze, vlastní čísla, diagonalizace"
readiness: nezačato
hot: true
tags: [otázka, kurz/LA1, otázka/12, todo]
---

# Matice

> **Otázka SZZ:** Matice: součin matic, regulární matice, inverzní matice a její výpočet, vlastní čísla matice a jejich výpočet, diagonalizace matice.

Zdroje: BI-LA1 (Dombek, Kalvoda, Kleprlík, Klouda, FIT ČVUT), kap. 1 (Matice a maticové operace), kap. 3 (Hodnost a regularita matice), kap. 5 (Determinant), kap. 6 (Vlastní čísla a vlastní vektory).

Značení: $T$ těleso, $A \in T^{m,n}$ matice typu $m \times n$, $E$ jednotková matice, $\theta$ nulový vektor, $h(A)$ hodnost, $\det A$ determinant. Teorie vlastních čísel se buduje nad $\mathbb{C}$.

---

## 1. Matice a součin matic

### 1.1 Matice a základní operace

**Definice ([[Matice]]):** Matice typu $m \times n$ nad $T$ je tabulka $A = (a_{ij})$ o $m$ řádcích a $n$ sloupcích, $a_{ij} \in T$. Množinu značíme $T^{m,n}$. Speciální: **čtvercová** ($n \times n$), **nulová** $\Theta$, **jednotková** $E_n$ ($e_{ij} = 1$ pro $i=j$, jinak $0$), **diagonální**, **transpozice** $A^T$ ($(A^T)_{ji} = a_{ij}$), **symetrická** ($A = A^T$).

Sčítání a násobení skalárem jsou **po složkách** (jen pro stejný typ): $(\alpha A + \beta B)_{ij} = \alpha a_{ij} + \beta b_{ij}$. Sčítání je komutativní, asociativní, platí distributivita vůči násobku skalárem.

### 1.2 Součin matic

**Definice (součin matic):** Pro $A \in T^{m,n}$ a $B \in T^{n,p}$ je **součin** $AB \in T^{m,p}$ dán vztahem
$$(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}, \qquad i \in \hat{m},\ j \in \hat{p}.$$
Nutná podmínka: **počet sloupců $A$** = **počet řádků $B$**.

**Věta (vlastnosti součinu).** Pokud mají rozměry smysl, platí:

1. **asociativita** $A(BC) = (AB)C$;
2. **distributivita** $A(B+C) = AB + AC$ a $(A+B)C = AC + BC$;
3. $\alpha(AB) = (\alpha A)B = A(\alpha B)$;
4. $(AB)^T = B^T A^T$;
5. **jednotková matice je neutrální:** $A E_n = A = E_m A$.

**Součin NENÍ komutativní:** obecně $AB \neq BA$ (může být definován jen jeden z nich; i pro čtvercové matice typicky $AB \neq BA$).

**Důkaz asociativity (idea).** Porovnáním $ij$-tých prvků a záměnou pořadí sumace:
$$[A(BC)]_{ij} = \sum_k a_{ik} \sum_\ell b_{k\ell} c_{\ell j} = \sum_\ell \Big( \sum_k a_{ik} b_{k\ell} \Big) c_{\ell j} = [(AB)C]_{ij}. \ \square$$

**Souvislost s lineárními kombinacemi:** $A b = \sum_j b_j A_{:j}$ je lineární kombinace **sloupců** $A$ (proto $Ax = b$ = hledání kombinace sloupců rovné $b$); řádky a sloupce součinu jsou $(AB)_{i:} = A_{i:}B$, $(AB)_{:j} = A B_{:j}$. Pro hodnost: $h(AB) \le \min\{h(A), h(B)\}$.

---

## 2. Regulární matice

**Definice ([[Regulární-matice]]):** Čtvercová $A \in T^{n,n}$ je **regulární**, pokud k ní existuje **[[Inverzní-matice|inverzní matice]]**, tj. matice $B$ s
$$AB = BA = E.$$
Není-li regulární, je **singulární**. (Definice se týká jen čtvercových matic; nepředpokládá se v ní existence $B$ — regularita = *existence* takové $B$.)

**Věta (regularita a hodnost — ekvivalentní podmínky).** Pro $A \in T^{n,n}$ jsou ekvivalentní:

1. $A$ je regulární;
2. $h(A) = n$;
3. $A \sim E$ (převoditelná GEM na jednotkovou matici);
4. řádky (resp. sloupce) $A$ jsou lineárně nezávislé;
5. $\det A \neq 0$;
6. $Ax = \theta$ má jen triviální řešení;
7. pro každé $b$ má $Ax = b$ právě jedno řešení.

**Důkaz $1 \Rightarrow 2 \Rightarrow 3 \Rightarrow 1$ (idea).**
- $1 \Rightarrow 2$: z $E = AA^{-1}$ a $h(XY) \le \min\{h(X),h(Y)\}$ plyne $n = h(E) \le h(A) \le n$, tedy $h(A) = n$.
- $2 \Rightarrow 3$: GEM převede $A$ na HST s $n$ pivoty; vydělením pivotů a eliminací nad nimi (Gauss–Jordan) dostaneme $E$, tj. $A \sim E$.
- $3 \Rightarrow 1$: $A \sim E$ znamená $PA = E$ pro regulární $P$ (součin elementárních matic), takže $A = P^{-1}$ je regulární. $\square$

**Postačí jednostranná inverze.** Existuje-li $B$ s $AB = E$ **nebo** $BA = E$, je $A$ regulární a $B = A^{-1}$ (z $AB=E$ opět $n = h(E) \le h(A) \le n$, pak $A^{-1} = A^{-1}E = A^{-1}AB = B$).

**Další vlastnosti.** Součin regulárních je regulární, $(AB)^{-1} = B^{-1}A^{-1}$; $(A^T)^{-1} = (A^{-1})^T$; násobení regulární maticí nemění hodnost ($h(PA) = h(A) = h(AQ)$).

---

## 3. Inverzní matice a její výpočet

### 3.1 Definice a vlastnosti

**Definice ([[Inverzní-matice]]):** $B \in T^{n,n}$ je inverzní k $A \in T^{n,n}$, pokud $AB = BA = E$; značíme $B = A^{-1}$.

**Věta (jednoznačnost).** Je-li $A$ regulární, je $A^{-1}$ určena **jednoznačně**.

**Důkaz.** Pro dvě inverze $B_1, B_2$: $B_1 = B_1 E = B_1(AB_2) = (B_1 A)B_2 = E B_2 = B_2$ (asociativita). $\square$

**Vlastnosti:** $(A^{-1})^{-1} = A$; $(AB)^{-1} = B^{-1}A^{-1}$; $(A^T)^{-1} = (A^{-1})^T$; $\det(A^{-1}) = (\det A)^{-1}$.

### 3.2 Výpočet inverze (Gaussovou–Jordanovou eliminací)

K matici $A$ připíšeme jednotkovou matici a [[Gaussova-eliminace|GEM]] převedeme levý blok na $E$:
$$(A \mid E) \;\sim\; (E \mid A^{-1}).$$
Pravý blok je hledaná $A^{-1}$.

**Proč to funguje.** Každou posloupnost úprav GEM realizuje násobení zleva regulární maticí $P$. Pokud $PA = E$, je z definice $P = A^{-1}$; tytéž úpravy provedené na $E$ dají $PE = P = A^{-1}$. **Vznikne-li v levém bloku nulový řádek** (nelze dosáhnout $E$), je $h(A) < n$, $A$ je singulární a inverze neexistuje.

**Algoritmus (kroky):** sestav $(A \mid E)$; proveď GEM až do rHST levého bloku; je-li levý blok $E$, odečti $A^{-1}$ z pravého bloku, jinak hlaš singularitu. Složitost $O(n^3)$.

(Determinant lze využít i k inverzi přes adjungovanou matici, ale GEM je výpočetně výhodnější.)

---

## 4. Vlastní čísla matice a jejich výpočet

### 4.1 Definice

**Definice ([[Vlastní-číslo|vlastní číslo a vlastní vektor]]):** $\lambda \in \mathbb{C}$ je **vlastní číslo** matice $A \in \mathbb{C}^{n,n}$, právě když existuje **nenulový** vektor $x \in \mathbb{C}^n$ s
$$A x = \lambda x.$$
Vektor $x$ je **vlastní vektor** příslušející $\lambda$. Množina vlastních čísel je **spektrum** $\sigma(A)$. (Nenulovost $x$ je nutná — jinak by $\sigma(A) = \mathbb{C}$.)

**Vlastní podprostor** příslušející $\lambda$ je podprostor řešení homogenní soustavy
$$(A - \lambda E)x = \theta, \qquad \text{tj. } \ker(A - \lambda E).$$

### 4.2 Charakteristický polynom

Nenulové řešení $(A - \lambda E)x = \theta$ existuje $\iff A - \lambda E$ je singulární $\iff \det(A - \lambda E) = 0$.

**Definice (charakteristický polynom):** $p_A(\lambda) := \det(A - \lambda E)$.

**Věta.** $p_A$ je polynom stupně $n$ a
$$\lambda \in \sigma(A) \iff p_A(\lambda) = 0.$$

*Idea:* člen nejvyššího stupně $(-1)^n\lambda^n$ pochází z diagonály $\prod_i(a_{ii} - \lambda)$. Podle základní věty algebry má $p_A$ (nad $\mathbb{C}$) právě $n$ kořenů včetně násobností, takže **každá komplexní matice má aspoň jedno vlastní číslo** a $\sum_{\lambda \in \sigma(A)} \nu_a(\lambda) = n$. (Reálná matice může mít nereálná vlastní čísla — např. rotace $\left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$ má $\lambda = \pm i$.)

### 4.3 Násobnosti

- **Algebraická násobnost** $\nu_a(\lambda)$ = násobnost $\lambda$ jako kořene $p_A$;
- **geometrická násobnost** $\nu_g(\lambda) = \dim \ker(A - \lambda E) = n - h(A - \lambda E)$;
- vždy
$$1 \le \nu_g(\lambda) \le \nu_a(\lambda) \le n.$$
Je-li $\nu_a(\lambda) = 1$, pak nutně $\nu_g(\lambda) = \nu_a(\lambda) = 1$.

### 4.4 Výpočet

1. sestav $p_A(\lambda) = \det(A - \lambda E)$ (výpočet determinantu z kap. 5);
2. najdi kořeny $p_A$ — to jsou vlastní čísla; jejich násobnost jako kořene = $\nu_a$;
3. pro každé $\lambda$ vyřeš homogenní soustavu $(A - \lambda E)x = \theta$ ([[Gaussova-eliminace|GEM]]) — nenulová řešení jsou vlastní vektory; $\nu_g$ = dimenze prostoru řešení.

### 4.5 Podobné matice

**Definice (podobnost):** $A, B \in \mathbb{C}^{n,n}$ jsou **podobné**, pokud $A = P^{-1}BP$ pro nějakou regulární $P$. Podobnost je relace ekvivalence.

**Věta.** Podobné matice mají stejný charakteristický polynom (a tedy spektrum i algebraické i geometrické násobnosti) a stejný determinant.

**Důkaz (char. polynom).**
$$p_A(\lambda) = \det(P^{-1}BP - \lambda P^{-1}P) = \det\!\big(P^{-1}(B - \lambda E)P\big) = \det P^{-1} \det(B - \lambda E)\det P = p_B(\lambda). \ \square$$

---

## 5. Diagonalizace matice

### 5.1 Definice

**Definice ([[Diagonalizace|diagonalizovatelná matice]]):** $A \in \mathbb{C}^{n,n}$ je **diagonalizovatelná**, je-li podobná diagonální matici, tj. existuje regulární $P$ a diagonální $D$ s
$$A = P D P^{-1}.$$

### 5.2 Kritérium

**Věta (o diagonalizovatelnosti).** Pro $A \in \mathbb{C}^{n,n}$ jsou ekvivalentní:

1. $A$ je diagonalizovatelná;
2. existuje **báze $\mathbb{C}^n$ tvořená vlastními vektory** $A$;
3. $\sum_{\lambda \in \sigma(A)} \nu_g(\lambda) = n$;
4. pro každé vlastní číslo $\nu_g(\lambda) = \nu_a(\lambda)$.

**Lemma.** Vlastní vektory příslušející **navzájem různým** vlastním číslům jsou lineárně nezávislé.

**Důsledek (postačující podmínka).** Má-li $A$ **$n$ různých** vlastních čísel, je diagonalizovatelná.

**Důkaz lemmatu (idea, indukcí).** Z $\sum_i \alpha_i x_i = \theta$ přenásobením $A$ a odečtením $\lambda_j$-násobku vypadne poslední člen; indukční předpoklad a $\lambda_\ell \neq \lambda_j$ dají $\alpha_\ell = 0$. $\square$

**Důkaz $3 \Rightarrow 1$ (idea).** Sjednocením bází jednotlivých vlastních podprostorů vznikne (díky lemmatu) báze $\mathbb{C}^n$ z vlastních vektorů; matice $P$ s těmito sloupci dává $P^{-1}AP = D$. $\square$

### 5.3 Konstrukce a využití

Sloupce $P$ jsou vlastní vektory tvořící bázi, $D$ má na diagonále příslušná vlastní čísla **ve stejném pořadí** (každé tolikrát, kolik je jeho násobnost):
$$P = (x_1 \mid \cdots \mid x_n), \qquad D = \operatorname{diag}(\lambda_1, \dots, \lambda_n), \qquad AP = PD.$$

**Mocniny:** $A^k = P D^k P^{-1}$, kde $D^k = \operatorname{diag}(\lambda_1^k, \dots, \lambda_n^k)$ — efektivní výpočet mocnin.

**Příklad nediagonalizovatelné matice:** $A = \left(\begin{smallmatrix} 1 & 0 & 0 \\ 0 & 3 & 1 \\ 0 & 0 & 3 \end{smallmatrix}\right)$, $p_A(\lambda) = (1-\lambda)(3-\lambda)^2$. Pro $\lambda = 3$ je $\nu_a = 2$, ale $\nu_g = 1$, takže $A$ není diagonalizovatelná.

---

## Co je potřeba na zkoušku znát

### Definice
- Matice, typy, transpozice; součin matic $(AB)_{ij} = \sum_k a_{ik}b_{kj}$.
- Regulární / singulární matice (existence inverze); inverzní matice $A^{-1}$ ($AB = BA = E$).
- Vlastní číslo / vektor ($Ax = \lambda x$, $x \neq \theta$), spektrum, vlastní podprostor $\ker(A-\lambda E)$.
- Charakteristický polynom $p_A(\lambda) = \det(A - \lambda E)$; algebraická a geometrická násobnost.
- Podobné matice ($A = P^{-1}BP$); diagonalizovatelná matice ($A = PDP^{-1}$).

### Klíčové věty
- **Vlastnosti součinu:** asociativita, distributivita, $(AB)^T = B^TA^T$, $E$ neutrální, **nekomutativita**.
- **Regularita** $\iff h(A) = n \iff A \sim E \iff \det A \neq 0 \iff Ax=\theta$ jen triviálně. Jednostranná inverze stačí.
- **Inverze** jednoznačná; $(AB)^{-1} = B^{-1}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$.
- $\lambda \in \sigma(A) \iff p_A(\lambda) = 0$; $\deg p_A = n$; $1 \le \nu_g \le \nu_a \le n$.
- **Podobné matice** mají stejný $p_A$, spektrum, násobnosti, determinant.
- **Diagonalizovatelnost** $\iff$ báze z vlastních vektorů $\iff \sum \nu_g = n \iff \nu_g = \nu_a\ \forall\lambda$; $n$ různých vlastních čísel $\Rightarrow$ diagonalizovatelná.

### Algoritmy
- **Výpočet inverze:** $(A \mid E) \sim (E \mid A^{-1})$ Gaussovou–Jordanovou eliminací, $O(n^3)$; nulový řádek vlevo ⇒ singulární.
- **Výpočet vlastních čísel:** kořeny $p_A(\lambda) = \det(A - \lambda E)$; vlastní vektory jako řešení $(A - \lambda E)x = \theta$.
- **Diagonalizace:** $P$ = vlastní vektory ve sloupcích, $D$ = vlastní čísla na diagonále; mocnina $A^k = PD^kP^{-1}$.
