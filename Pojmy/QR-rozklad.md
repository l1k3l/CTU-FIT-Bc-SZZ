---
aliases: [qr rozklad, qr rozkladu, qr rozkladem, qr faktorizace, qr dekompozice, householderova triangularizace, givensova rotace]
tags: [definice, kurz/LA2]
---

# QR rozklad

## Definice

**QR rozkladem** matice $A \in \mathbb{R}^{m,n}$ ($m \ge n$) myslíme její zapsání jako součin **[[Ortogonální-matice|ortogonální matice]]** (resp. matice s ortonormálními sloupci) a **horní trojúhelníkové matice** $R$.

- **Redukovaný QR rozklad:** $A = \hat{Q}\hat{R}$, kde $\hat{Q} \in \mathbb{R}^{m,n}$ má ortonormální sloupce ($\hat{Q}^T\hat{Q} = E_n$) a $\hat{R} \in \mathbb{R}^{n,n}$ je horní trojúhelníková.
- **Úplný (kompletní) QR rozklad:** $A = QR$, kde $Q \in \mathbb{R}^{m,m}$ je ortogonální a $R \in \mathbb{R}^{m,n}$ je „horní trojúhelníková“ (horní lichoběžníková; poslední $m-n$ řádků nulových). Úplný rozklad získáme z redukovaného doplněním $\hat{Q}$ o ON bázi $\langle q_1,\dots,q_n\rangle^\perp$ a $\hat{R}$ o nulové řádky.

## Existence a jednoznačnost

- **Existence:** Každá $A \in \mathbb{R}^{m,n}$ ($m \ge n$) má redukovaný i úplný QR rozklad.
- **Jednoznačnost:** Má-li $A$ plnou hodnost $h(A) = n$, pak existuje **právě jeden** redukovaný rozklad s $r_{jj} > 0$ pro všechna $j$ (ten z [[Gram-Schmidtův-algoritmus|Gramova–Schmidtova algoritmu]] s normalizací). Bez podmínky $r_{jj}>0$ ani při LZ sloupcích rozklad jednoznačný není.
- Platí $h(A) = h(\hat{R})$.

## Výpočet

1. **[[Gram-Schmidtův-algoritmus|Gramova–Schmidtova ortogonalizace]]** sloupců $A$: $a_j = \sum_{i\le j} r_{ij} q_i$, kde $r_{ij} = q_i^T a_j$, $r_{jj} = \|z_j\|_2$. Klasická verze je numericky nestabilní, **modifikovaný GS** je stabilní. Složitost $\sim 2mn^2$.
2. **Householderova triangularizace** (zrcadlení): postupně reflektory $Q_k = E - \tfrac{2}{\|v_k\|^2}v_k v_k^T$ vynulují celý sloupec pod diagonálou; $R = Q^T A = Q_n\cdots Q_1 A$. Složitost $2mn^2 - \tfrac{2}{3}n^3$. Vhodné pro plné matice.
3. **Givensova rotace:** rotace v rovině dvou souřadnic vynuluje jeden prvek pod diagonálou. Složitost $\sim 3mn^2 - n^3$ (o ~50 % více než Householder), ale vhodné pro řídké matice a paralelizaci.

## Využití

- **[[Metoda-nejmenších-čtverců|Metoda nejmenších čtverců]]:** $\hat{R}x = \hat{Q}^T b$ — numericky stabilnější než normální rovnice.
- **[[QR-algoritmus]]** pro výpočet vlastních čísel.
- Řešení soustavy $Ax=b$: $A=QR \Rightarrow Rx = Q^T b$ (zpětná substituce).

## Související

- [[Ortogonální-matice]]
- [[Gram-Schmidtův-algoritmus]]
- [[Metoda-nejmenších-čtverců]]
- [[QR-algoritmus]]
- [[Matice]]
