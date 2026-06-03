---
tags: [otázka, kurz/LA2, otázka/6, todo]
---

# 6 — Výpočet vlastních čísel (mocninná metoda, QR algoritmus) (zkrácená verze)

## 1. Připomenutí + spektrální rozklad

**Vlastní číslo:** $\lambda \in \mathbb{C}$ s $Ax = \lambda x$, $x \neq \theta$; spektrum $\sigma(A)$. Diagonalizace $A = PDP^{-1}$.

**[[Spektrální-rozklad]] symetrické matice** ($S^T = S$): vlastní čísla **reálná** + ON báze vlastních vektorů, tedy
$$S = Q\Lambda Q^T, \quad Q \text{ ortogonální},\ \Lambda \text{ diagonální}.$$
*(Reálnost: $\overline{x}^T S x = \lambda\|x\|_2^2 = \overline\lambda\|x\|_2^2 \Rightarrow \lambda=\overline\lambda$.)*

**Definitnost:** $S$ pozitivně definitní ($x^T Sx>0$) $\iff$ všechna $\lambda>0$; semidefinitní ($\ge0$) $\iff$ všechna $\lambda \ge 0$. *(Z $x^TSx = \sum_i \lambda_i y_i^2$, $y=Q^Tx$.)*

## 2. Proč ne charakteristický polynom

Pro $n \ge 5$ má $p_A(\lambda) = \det(A-\lambda E)$ stupeň $\ge5$: kořeny **nelze** vyjádřit radikály (Abel–Ruffini) a numericky je to **špatně podmíněné**. ⟹ algoritmy pro $n\ge5$ **musí být iterační**: mocninná metoda + QR.

## 3. [[Mocninná-metoda]]

**Iterace:** $v^{(k)} = \dfrac{A v^{(k-1)}}{\|A v^{(k-1)}\|_2} = \dfrac{A^k x}{\|A^k x\|_2}$ — vynásob $A$, znormuj, opakuj.

**Konvergence:** je-li dominantní $\lambda_1$ **jednoduché** v abs. hodnotě ($|\lambda_1| > |\lambda_2| \ge \dots$) a $x$ není kolmý na $q_1$, pak $v^{(k)} \to \pm q_1$ (dominantní vlastní vektor).

*Idea:* $x = \sum_i \alpha_i q_i$ ($\alpha_1 \neq 0$) ⟹ $A^k x = \lambda_1^k(\alpha_1 q_1 + \sum_{i\ge2}\alpha_i(\lambda_i/\lambda_1)^k q_i)$; členy s $|\lambda_i/\lambda_1|<1$ vymizí.

**Rychlost:** $\left|\dfrac{\lambda_2}{\lambda_1}\right|$ (lineární pro vektor, $|\lambda_2/\lambda_1|^{2k}$ pro číslo).

**Rayleighův podíl** (odhad $\lambda_1$ z vlastního vektoru): $r(y) = \dfrac{y^T A y}{y^T y}$; pro vlastní vektor $r(x)=\lambda$, takže $r(v^{(k)}) \to \lambda_1$ (rychleji).

**Varianty:** inverzní iterace (na $A^{-1}$ → nejmenší $\lambda$); posunutá iterace (na $(A-\mu E)^{-1}$ → $\lambda$ nejbližší $\mu$); deflace. Vhodná pro řídké matice, jen dominantní pár. Aplikace: PageRank. *(Nekonverguje, není-li $\lambda_1$ jednoduché — např. $\operatorname{diag}(1,-1)$.)*

## 4. [[QR-algoritmus]]

**Iterace:** $A^{(0)}=A$; $A^{(k-1)} = Q^{(k)}R^{(k)}$ (QR rozklad), $A^{(k)} = R^{(k)}Q^{(k)}$. Tedy „spočti $QR$, vrať $RQ$".

**Zachování spektra:** $R^{(k)} = (Q^{(k)})^T A^{(k-1)}$ ⟹ $A^{(k)} = (Q^{(k)})^T A^{(k-1)} Q^{(k)}$ — transformace **podobnosti** (ortogonální $Q$), takže $A^{(k)}$ má stejná vlastní čísla jako $A$.

**Konvergence:** symetrická $A$ → diagonální matice; nesymetrická → horní trojúhelníková (**Schurova forma** $A=QRQ^T$). Vlastní čísla pak leží na diagonále. Předpoklad jednoduchosti $|\lambda_1|>|\lambda_2|>\dots$

**Příprava (zlevnění):** základní iterace $O(n^3)$ je drahá. Oboustrannými Householderovými reflexemi (podobnost $B = QAQ^T$, zachová spektrum) převeď na **Hessenbergův tvar** (nuly pod poddiagonálou: $j+1<i\Rightarrow a_{ij}=0$); pro symetrické na **třídiagonální** ($|i-j|>1\Rightarrow a_{ij}=0$). Tvar se v iteracích zachovává → každá iterace levná.

---

## Co odpovědět rychle

- **Spektrální rozklad:** symetrická $\Rightarrow$ reálná vlastní čísla + $S = Q\Lambda Q^T$; def./semidef. $\iff$ $\lambda>0$ / $\lambda\ge0$.
- **Proč iterace:** $n\ge5$ — Abel–Ruffini (žádné radikály) + špatná podmíněnost char. polynomu.
- **Mocninná metoda:** $v^{(k)}=Av^{(k-1)}/\|\cdot\|$; $\to$ dominantní vlastní vektor $q_1$; rychlost $|\lambda_2/\lambda_1|$; Rayleighův podíl $r(y)=\frac{y^TAy}{y^Ty} \to \lambda_1$.
- **QR algoritmus:** $A=QR \to RQ$; každý krok je podobnost (stejné spektrum) → konverguje k (blokově) trojúhelníkové formě, vlastní čísla na diagonále.
- **Hessenberg/třídiagonál:** Householderova příprava před QR, zachovává spektrum, zlevní iterace.
