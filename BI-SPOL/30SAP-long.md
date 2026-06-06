---
studyplan: true
etapa: 1 · SAP — Daňhel
qid: 30SAP
examiner: Daňhel
topic: Kódy se znaménkem, aritmetické operace, pohyblivá řádová čárka
readiness: nezačato
tags:
  - otázka
  - kurz/SAP
  - otázka/30
  - hotovo
---

# Kódy čísel se znaménkem, aritmetické operace, pohyblivá řádová čárka

> **Otázka SZZ:** Kódy pro zobrazení čísel se znaménkem a realizace aritmetických operací (paralelní sčítačka/odčítačka, realizace aritmetických posuvů, dekodér, multiplexor, čítač). Reprezentace čísel v pohyblivé řádové čárce.

Zdroje: BI-SAP, `zobrazeni_cisel.pdf`, `sap-9-arit.pdf`, `sap-5-oper.pdf`, `sap-6-typical.pdf` (H. Kubátová, KČN FIT ČVUT).

---

## 0. Řádová mřížka a poziční soustavy
**Poziční soustava** je dána **základem $z\ge2$** (počítač: $z=2$; pro stručnost $z=16$, kde 4 dvojkové cifry = 1 hexa). **Řádová mřížka** určuje formát zobrazitelných čísel (nejvyšší a nejnižší řád); **modul $M=z^n$** je nejmenší již nezobrazitelné číslo. **Přenos (carry)** je bit vypadávající z mřížky.

---

## 1. Kódy pro zobrazení čísel se znaménkem

Nejnižší $n$-bitové celé číslo se znaménkem lze zakódovat několika způsoby. Klíčové otázky: rozsah, počet obrazů nuly, snadnost negace a aritmetiky.

### 1.1 Přímý kód (znaménko + absolutní hodnota)
Nejvyšší bit = **znaménko** (0 = +, 1 = −), zbytek = **absolutní hodnota**.
- Rozsah $|X|<\tfrac12 M$. **Negace** = invertovat jen znaménkový bit.
- **Problém dvou nul** (+0 = 000, −0 = 100).
- **Aritmetika složitá:** pracuje se zvlášť se znaménkem a abs. hodnotou; při různých znaménkách je sčítání ve skutečnosti odčítání → nutno zjišťovat znaménko výsledku.

### 1.2 Inverzní kód (doplněk do 1)
Záporné číslo = bitová inverze kladného ($\overline X$). Také **dvě nuly**; dnes okrajový (v materiálech zmíněn jen jako mezikrok: $-B=\overline B+1-M$).

### 1.3 Doplňkový kód (doplněk do 2) — nejdůležitější
**[[Doplňkový-kód|Doplňkový kód]]** zobrazuje číslo takto:
$$D(X)=\begin{cases}X & X\ge0\\ M+X & X<0\end{cases}$$
Znaménko je **organickou součástí obrazu**.
- **Rozsah:** $-2^{n-1}\le X\le 2^{n-1}-1$ (asymetrický — o jedno záporné číslo víc).
- **Jediná nula** (000…0).
- **Negace:** $D(-X)=\overline{D(X)}+1$ (invertuj a přičti „horkou jedničku").
- **Váha nejvyššího bitu je záporná** $(-2^{n-1})$.
- *Příklad (3 bity):* 0→000, 1→001, 3→011, −1→111, −4→100.

### 1.4 Aditivní kód (s posunutou nulou, *biased*)
$A(X)=X+K$, obvykle $K=\tfrac12 M$. Znaménko implicitní; nevýhoda — **nula se nezobrazuje jako nula** (ale jako $K$). **Použití: exponent v IEEE 754.**

### 1.5 Rozšíření znaménka (sign extension)
Číslo má při více bitech stejnou hodnotu. Realizace = **rozkopírování nejvyššího (znaménkového) bitu** menší mřížky — bez hradel, jen vodiči. (Bez znaménka se doplňují nuly.) *Příklad:* $D(-6)$ na 4 b = 1010, na 8 b = 11111010.

---

## 2. Realizace aritmetických operací

### 2.0 Sčítání/odčítání a přeplnění
V **doplňkovém kódu** se sčítá i odčítá **jediným** obvodem: $A-B=D(A)+\overline{D(B)}+1$; **přenos z nejvyššího řádu se ignoruje** (přičtení modulu nemá vliv).

**Přenos (carry) $\ne$ přeplnění (overflow)!**
- **Přenos** = bit vypadlý z mřížky.
- **Přeplnění** = nesprávný výsledek; nastane jen při **shodných znaménkách** operandů a opačném znaménku výsledku: $(+)+(+)\to(-)$ nebo $(-)+(-)\to(+)$.
- **Detekce:** $over = p\oplus q$ (přenos *do* a *z* nejvyššího řádu jsou různé) $=\overline a\,\overline b\,s + a b \overline s$.
- U odčítání se místo přenosu sleduje **výpůjčka (borrow)** $v^*=\overline{q^*}$.

### 2.1 Paralelní sčítačka / odčítačka
**[[Sčítačka|Sčítačka]]** je [[Kombinační-obvod|kombinační obvod]].
- **Poloviční sčítačka (HA):** $s=a\oplus b$, $q=a\cdot b$.
- **Úplná sčítačka (FA):** $s=a\oplus b\oplus p$, $q=ab+p(a\oplus b)$; pomocné signály *generate* $G=ab$, *propagate* $P=a\oplus b$.
- **Paralelní (ripple-carry) sčítačka:** kaskáda $n$ FA, přenos se šíří zprava doleva ($p_{i+1}=q_i$). **Zpoždění $O(n)$** — výsledek správný až po průchodu přenosu všemi řády.
- **Zrychlení — predikce přenosu (carry-lookahead):** $q_i=G_i+P_i q_{i-1}$ se rozepíše a počítá **dvouúrovňově** přímo ze vstupů (konstantní zpoždění) za cenu více hradel.

**Sčítačka/odčítačka:** jeden obvod sčítá i odčítá. Řídicí signál **Odčítej**:
- každý bit $b_i$ vede přes **XOR s Odčítej** (Odčítej = 1 → negace $B$, tj. jedničkový doplněk; = 0 → beze změny),
- **Odčítej** se přivede též jako **vstupní přenos** do nejnižšího řádu (realizuje „+1" doplňku do 2).
- Výstupy: přenos $q_n$ (carry), výpůjčka $v^*=\overline{q^*}$, přeplnění $over=q_n\oplus q_{n-1}$.

Procesor pak týmž obvodem realizuje ADD/ADC/SUB/SBB (řízeno módem $m$ a vstupním přenosem); **stejná sčítačka sčítá nezáporná čísla i čísla v doplňkovém kódu** a nastaví příznaky carry i overflow — interpretaci dělá software.

### 2.2 Realizace aritmetických posuvů
Tři typy posuvu se liší tím, co se nasouvá na uvolněná místa:
- **logický** — nasouvá se **0**, vypadlý bit se ignoruje;
- **cyklický (rotace)** — vypadlý bit se nasune na druhý konec (i přes příznak carry);
- **aritmetický** — výsledek musí odpovídat **násobení/dělení mocninou 2** ($A\ll k=A\cdot2^k$, $A\gg k=A:2^k$); realizace **závisí na kódu**.

**Aritmetický posuv vpravo (dělení 2):**
- *doplňkový kód:* **kopíruje se znaménkový bit** (1010 = −6 → 1101 = −3); vypadlý nejnižší bit → **ztráta přesnosti (ZP)**.
- *přímý kód:* znaménko zůstává, pod ně se nasouvá 0 (1010 = −2 → 1001 = −1).

**Aritmetický posuv vlevo (násobení 2):** na nejnižší řád 0; vysunutí bitu nesouhlasícího se znaménkem → **přeplnění (overflow)**.

**Realizace:** posuvy o pevný počet míst jsou jen **propojení vodičů** + hradla pro doplnění/detekci; univerzální posouvač řízený signály (arit/cykl, vlevo/vpravo) přidá multiplexory. **Barrel shifter** je kombinační obvod pro posuv o libovolný počet míst (multiplexory + vodiče) — rychlý, ale větší.

### 2.3 Dekodér
**[[Dekodér|Dekodér]]** převádí $n$-bitový binární kód na kód **„1 z $N$"** ($N=2^n$): aktivuje jediný výstup (*one-hot*); každý výstup = jeden **minterm** vstupů:
$$y_0=\overline{x_1}\,\overline{x_0},\ y_1=\overline{x_1}x_0,\ y_2=x_1\overline{x_0},\ y_3=x_1x_0.$$
Má často **povolovací vstup (enable)**. Použití: **adresní dekódování** v paměti (výběr řádku), jádro multiplexoru/demultiplexoru. Obrácený obvod = **kodér**.

### 2.4 Multiplexor
**[[Multiplexor|Multiplexor (MUX)]]** vybírá podle $n$ výběrových vstupů jeden z $2^n$ datových na výstup:
$$y=\overline{s_1}\,\overline{s_0}d_0+\overline{s_1}s_0 d_1+s_1\overline{s_0}d_2+s_1 s_0 d_3.$$
Strukturálně **obsahuje dekodér** + pole AND-OR. **Demultiplexor** = obrácená funkce (dekodér s daty jako enable). Použití: výběr sběrnice, univerzální realizace logické funkce.

### 2.5 Čítač
**[[Čítač|Čítač]]** je [[Sekvenční-obvod|sekvenční obvod]] (speciální registr) inkrementující/dekrementující stav. Dělení: **úplný** (modulo $2^n$) / **neúplný**; **synchronní** / asynchronní; **vratný (up/down)**; kód binární / **Grayův** / 1-z-N. Sestaven z [[Klopný-obvod|klopných obvodů]], popsán [[Konečný-automat|konečným automatem]].

*Příklad — M4, povolovací vstup $E$, D klopné obvody* ($q_1q_0$, stavový kód = výstup):
$$D_{q_0}=q_0\oplus E,\qquad D_{q_1}=E q_0\oplus q_1,\qquad Y=q_1 q_0.$$
Každý stupeň je vlastně **poloviční sčítačka**.

---

## 3. Reprezentace čísel v pohyblivé řádové čárce

### 3.1 Formát
**[[Pohyblivá-řádová-čárka|Pohyblivá (plovoucí) řádová čárka]]** zobrazuje číslo dvojicí (mantisa, exponent):
$$A=(-1)^s\cdot M\cdot z^{\,e},$$
kde $z$ = základ (obvykle 2), **mantisa $M$** nese hodnotu, **exponent $e$** polohu řádové čárky. Obě podmřížky používají kódy pro čísla se znaménkem. Oproti pevné řádové čárce dává mnohem větší **rozsah** (za cenu omezené přesnosti).

### 3.2 Normalizovaný tvar a skrytá jednička
**Normalizovaný tvar** = mantisu už nelze posunout více doleva. Při $z=2$ a přímém kódu mantisy je pak nejvyšší bit mantisy vždy **1** → lze ji vynechat = **skrytá jednička** (zvýší přesnost o 1 bit). Po každé operaci je nutná **normalizace**. *Pozor:* při nulovém exponentu (denormalizovaná čísla) se skrytá jednička **nepoužívá**.

### 3.3 IEEE 754
| | znaménko | exponent | mantisa | bias $K$ |
|---|---|---|---|---|
| **single (32 b)** | 1 | 8 | 23 (+1 skrytá) | 127 |
| **double (64 b)** | 1 | 11 | 52 (+1 skrytá) | 1023 |

Exponent je v **aditivním kódu** (uloženo $g=e+K$), mantisa v přímém kódu se skrytou jedničkou. Hodnota normalizovaného čísla:
$$A=(-1)^s\cdot(1.f)\cdot 2^{\,g-K}.$$

### 3.4 Speciální (singulární) hodnoty
| $g$ | $f$ | hodnota |
|---|---|---|
| 0 | 0 | $\pm 0$ |
| 0 | $\ne0$ | **denormalizované** (subnormální) číslo — bez skryté 1, exponent fixně $-126$ (single) |
| $1..254$ | — | normalizované $(-1)^s(1.f)2^{g-127}$ |
| 255 | 0 | $\pm\infty$ |
| 255 | $\ne0$ | **NaN** (Not a Number) |

### 3.5 Aritmetika v pohyblivé řádové čárce
- **Sčítání/odčítání:** **zarovnat exponenty** (posunout mantisu menšího) → sečíst/odečíst mantisy → **normalizovat** (+ zaokrouhlit).
- **Násobení:** **sečíst exponenty** + vynásobit mantisy.
- **Dělení:** odečíst exponenty + vydělit mantisy.

*Příklad (single):* $-58 = -111010_2 = -1.1101\times2^5$ → $s=1$, $g=127+5=10000100$, $f=1101000\ldots$ → hex **C2680000**.

---

## 4. Co je potřeba na zkoušku znát

### Definice
Přímý / inverzní / doplňkový / aditivní kód — rozsah, počet nul, negace; doplňkový kód $D(X)$, rozsah $[-2^{n-1},2^{n-1}-1]$, negace = invert+1, váha MSB = $-2^{n-1}$; rozšíření znaménka; přenos vs přeplnění; poloviční/úplná/paralelní sčítačka; sčítačka/odčítačka; aritmetický vs logický vs cyklický posuv; dekodér, multiplexor, čítač; pohyblivá řádová čárka, normalizace, skrytá jednička, IEEE 754.

### Souvislosti / postupy
- Proč doplňkový kód: jediná nula, sčítání = odčítání jedním obvodem, přenos se ignoruje.
- Detekce přeplnění $over=p\oplus q$ (≠ carry!).
- Sčítačka/odčítačka: XOR na operandu B + carry-in = řídicí signál Odčítej.
- Aritmetický posuv vpravo v doplňkovém kódu kopíruje znaménko; realizace závisí na kódu.
- MUX obsahuje dekodér; dekodér = samé mintermy (1 z N).
- Float: zarovnat exponenty + sečíst mantisy + normalizovat.

### Vzorce
- HA: $s=a\oplus b$, $q=ab$. FA: $s=a\oplus b\oplus p$, $q=ab+p(a\oplus b)$.
- Doplňkový rozdíl: $A-B=D(A)+\overline{D(B)}+1$.
- IEEE 754 single: $A=(-1)^s(1.f)2^{g-127}$, $g=e+127$, 1/8/23 b; double 1/11/52, $K=1023$.
- Posuvy: $A\ll k=A\cdot2^k$, $A\gg k=A:2^k$.
