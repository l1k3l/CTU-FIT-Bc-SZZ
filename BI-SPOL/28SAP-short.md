# 28SAP — Kombinační a sekvenční obvody (zkrácená verze)

## 1. Kombinační obvod
Výstup závisí **jen na okamžité kombinaci vstupů** (bez paměti). Popis [[Booleova-algebra|Booleovou algebrou]] $\langle B,+,\cdot,\neg,0,1\rangle$: komut., asoc., **distrib. $a+bc=(a+b)(a+c)$**, $a+0=a$, $a+\overline a=1$. Odvozené: absorbce $a+ab=a$, abs. negace $a+\overline a b=a+b$, de Morgan, consensus.

**Pojmy:** literál (proměnná přímo/negovaně); minterm = součin **všech** proměnných; maxterm = součet všech. Kanonicky: **ÚNDF** = $\sum$ mintermů, **ÚNKF** = $\prod$ maxtermů. Zápis $f=\sum(1,2,4,6)=\prod(0,3,5,7)$.

## 2. Minimalizace mapou
**[[Karnaughova-mapa|Karnaughova mapa]]:** $2^n$ polí, **Grayův kód** → sousední pole se liší v 1 proměnné; sousednost **cyklická** (i kraje).
- implikant = krychle v onsetu; **prvoimplikant** = nelze zvětšit; **podstatný** = pokrývá jedničku, již jiný prvoimplikant nepokrývá.
- algoritmus: smyčky (mocniny 2) → prvoimplikanty → podstatné → dopokrytí; skupinu popisují jen **neměnné** proměnné.
- **don't-care ×** = libovolně 0/1 pro zvětšení skupin.
- mnoho proměnných → **Quine–McCluskey** (tabulkově), pak heuristiky.

## 3. Realizace na hradlech
AND, OR, NOT, NAND, NOR, XOR. **Úplný systém** $\{+,\cdot,\neg\}$; úplný i **samotný NAND** / **NOR** (nejméně tranzistorů → ASIC).
- **AND-OR** přímo z MNDF; **NAND-NAND** dvojitou negací (proměnné na liché úrovni od konce negovat).
- **úplná sčítačka:** $s=a\oplus b\oplus p$, $q=ab+ap+bp$ (majorita).
- **hazard** = různé zpoždění cest → zákmit. Z mapy: sousední jedničky v různých krychlích → statický hazard → přidat **redundantní krychli**.

## 4. Sekvenční obvod
Výstup závisí i na **posloupnosti** vstupů → paměť přes **zpětnou vazbu**. Model = **konečný automat**. Huffman: kombinační část + paměťová část ([[Klopný-obvod|klopné obvody]]), CLK.
- **klopný obvod** = 1-bit paměť; v SAP **typ D** ($Q^{t+1}=D$, budicí fce = následující stav). Další: RS, JK ($J\overline Q+\overline K Q$), T ($T\oplus Q$).
- **synchronní** (mění se jen na CLK) vs asynchronní.
- kódování stavů: $2^{m-1}<n\le 2^m$.

## 5. Mealy a Moore
Automat **s výstupem**: $\langle X,Y,Q,\delta,\lambda\rangle$, $\delta:X\times Q\to Q$.
- **Mealy:** $\lambda:X\times Q\to Y$ — výstup ze stavu **i vstupu**; bere se ze **vstupu** KO, mění se hned.
- **Moore:** $\lambda:Q\to Y$ — výstup **jen ze stavu**; bere se z **výstupu** KO, mění se až po hraně CLK (o takt zpožděn). Více stavů než Mealy.

**Popis:** graf přechodů (Mealy: hrany *vstup/výstup*; Moore: výstup u stavu); tabulka přechodů + výstupů (Moore: 1 sloupec výstupů).

**Syntéza (7 kroků):** graf → tabulky $\delta,\lambda$ → kódování → mapy → min. budicí + výstupní fce → realizace (D KO) → $f_{max}=1/W$ (zpoždění hradel + Clock-to-Q + setup).

**Převod Mealy→Moore:** uzel s různými výstupy na vstupních hranách rozštěp na tolik uzlů, kolik je výstupních symbolů.

---

## Co odpovědět rychle
- Kombinační = bez paměti, jen aktuální vstupy; sekvenční = + historie přes zpětnou vazbu (= konečný automat).
- Minimalizace: Karnaughova mapa (Gray, cyklická sousednost) → maximální smyčky = prvoimplikanty → podstatné → dopokrytí; don't-care zvětšují skupiny.
- Hradla: úplný systém NAND/NOR; dvojúrovňová AND-OR / NAND-NAND; hazardy → redundantní krychle.
- **Mealy** výstup ze stavu i vstupu (hned), **Moore** jen ze stavu (o takt později, více stavů).
