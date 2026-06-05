# 30SAP — Kódy se znaménkem, aritmetika, pohyblivá řádová čárka (zkrácená verze)

## 1. Kódy čísel se znaménkem
- **přímý** (znaménko + abs. hodnota): negace = invert znaménka; **dvě nuly**; aritmetika složitá (znaménko zvlášť).
- **inverzní** (doplněk do 1): záporné = $\overline X$; dvě nuly.
- **[[Doplňkový-kód|doplňkový]]** (doplněk do 2): $D(X)=X$ ($X\ge0$) / $M+X$ ($X<0$). Rozsah $[-2^{n-1},2^{n-1}-1]$; **jediná nula**; **negace = invert+1**; váha MSB $=-2^{n-1}$.
- **aditivní** (posunutá nula): $A(X)=X+K$, $K=\tfrac12M$; nula ≠ 0 → exponent IEEE 754.
- **rozšíření znaménka** = kopie nejvyššího bitu (jen vodiče).

## 2. Aritmetické operace
**Doplňkový kód:** sčítá i odčítá jeden obvod, $A-B=D(A)+\overline{D(B)}+1$, **přenos se ignoruje**.
**Přenos ≠ přeplnění!** overflow jen při shodných znaménkách → opačné: $(+)(+)\to(-)$, $(-)(-)\to(+)$; **$over=p\oplus q$** $=\overline a\overline b s+ab\overline s$. Výpůjčka $v^*=\overline{q^*}$.

**[[Sčítačka|Paralelní sčítačka/odčítačka]]:**
- HA: $s=a\oplus b$, $q=ab$. FA: $s=a\oplus b\oplus p$, $q=ab+p(a\oplus b)$; $G=ab$, $P=a\oplus b$.
- ripple-carry = kaskáda FA, zpoždění $O(n)$; **carry-lookahead** = dvouúrovňově ze vstupů.
- sčítačka/odčítačka: **XOR(B, Odčítej)** + carry-in = Odčítej; over $=q_n\oplus q_{n-1}$.

**Aritmetické posuvy** ($A\ll k=\cdot2^k$, $A\gg k=:2^k$); typy: logický (nasouvá 0), cyklický (rotace), aritmetický (závisí na kódu):
- doplňkový vpravo → **kopíruje znaménko** (1010→1101); vlevo → 0 zprava, over při nesouladu znaménka.
- přímý vpravo → znaménko stojí, 0 pod ně.
- realizace = vodiče + hradla; **barrel shifter** = MUX + vodiče (libovolný počet míst).

**[[Dekodér|Dekodér]]:** $n$→$2^n$, aktivuje 1 (one-hot), výstupy = mintermy; enable; adresní dekódování.
**[[Multiplexor|MUX]]:** vybere 1 z $2^n$ dat podle výběru; $y=\sum m_k(s)d_k$; obsahuje dekodér.
**[[Čítač|Čítač]]:** sekvenční, modulo-N, synchr./asynchr., vratný, binární/Gray/1-z-N; z [[Klopný-obvod|D KO]]; M4: $D_{q_0}=q_0\oplus E$, $D_{q_1}=Eq_0\oplus q_1$.

## 3. Pohyblivá řádová čárka
**[[Pohyblivá-řádová-čárka|Float]]:** $A=(-1)^s\cdot M\cdot z^e$ (mantisa + exponent v kódech se znaménkem).
**Normalizovaný tvar** (mantisa max vlevo) → **skrytá jednička** (nejvyšší bit mantisy = 1, vynechán); po operaci normalizace.
**IEEE 754:**
- single 32 b: **1 / 8 / 23**, bias **127**; double 64 b: 1/11/52, bias 1023.
- exponent aditivní ($g=e+K$), mantisa přímý kód + skrytá 1: $A=(-1)^s(1.f)2^{g-K}$.
- speciální: $g{=}0,f{=}0$→0; $g{=}0,f{\ne}0$→denormalizované (bez skryté 1); $g{=}\max,f{=}0$→±∞; $g{=}\max,f{\ne}0$→NaN.

**Aritmetika:** sčítání = **zarovnat exponenty + sečíst mantisy + normalizovat**; násobení = sečíst exponenty + vynásobit mantisy.

---

## Co odpovědět rychle
- Doplňkový kód: jediná nula, negace invert+1, sčítání i odčítání jedním obvodem, přenos ignorovat.
- Přeplnění ≠ přenos; $over=p\oplus q$.
- Sčítačka/odčítačka = XOR na B + carry-in řízené Odčítej; ripple-carry $O(n)$, lookahead rychlejší.
- Aritmetický posuv vpravo v doplňkovém kódu kopíruje znaménkový bit.
- Dekodér (1 z N, mintermy), MUX (obsahuje dekodér), čítač (sekvenční z D KO).
- IEEE 754 single 1/8/23 bias 127; hodnota $(-1)^s(1.f)2^{g-127}$.
