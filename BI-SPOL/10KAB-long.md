---
tags: [otázka, kurz/KAB, otázka/10, todo]
---

# Symetrické šifry — blokové a proudové, operační módy

> **Otázka SZZ:** Symetrické šifry blokové a proudové, základní parametry, operační módy blokových šifer, jejich základní popis a slabiny.

Zdroje: BI-KAB, přednášky 3 (rozdělení šifer, proudové šifry, RC4, Salsa20/ChaCha, A5/1) a 4 (blokové šifry, DES, 3DES, AES, operační módy), prof. R. Lórencz, FIT ČVUT.

---

## 1. Symetrické šifry — rozdělení a základní parametry

**[[Symetrická-šifra|Symetrická šifra]]** je šifrovací systém $(M, C, K, E, D)$, kde šifrovací a dešifrovací klíč jsou stejné nebo se snadno převedou jeden na druhý. Odesílatel i příjemce sdílejí tajný klíč; $c = E_K(m)$, $m = D_K(c)$, $D_K = E_K^{-1}$.

Podle způsobu, jak se klíč použije ke zpracování OT:

| | **[[Bloková-šifra\|Bloková šifra]]** | **[[Proudová-šifra\|Proudová šifra]]** |
|---|---|---|
| Jednotka | blok $t$ znaků (dnes 128 b) | jednotlivý znak / bit |
| Transformace | **všechny** bloky toutéž $E_K$ | každý znak **jinou** $E_{h_i}$ (z proudu hesla) |
| Difúze | dobrá (celý blok) | malá (jen daný znak) |
| Propagace chyby | celý blok | jen jeden znak |
| Příklady | DES, 3DES, AES | RC4, Salsa20/ChaCha, A5/1 |

Proudová šifra je formálně blokovou s blokem délky 1, ale každý „blok“ se zpracuje jinou substitucí. Základní parametry obou tříd: **délka klíče**, **délka bloku** (blokové), **délka/perioda hesla** a způsob jeho generování (proudové), počet rund, použití **inicializačního vektoru (IV)**.

---

## 2. Proudové šifry

### 2.1 Princip

Generátor $G$ z klíče $k$ vytvoří **proud hesla** (keystream) $h_1, h_2, \dots$; moderní šifry nad $\{0,1\}$:
$$c_i = m_i \oplus h_i, \qquad m_i = c_i \oplus h_i$$
(zašifrování = dešifrování). **IV** se volí pro každou zprávu náhodně a přenáší se otevřeně — uvede generátor do jiného počátečního stavu, takže i při stejném klíči vznikne jiné heslo (utajení zajišťuje klíč, různost IV).

**Synchronní × asynchronní:**
- **Synchronní** — heslo nezávisí na OT/ŠT; výpadek znaku ŠT rozhodí celý zbytek (nutná přesná synchronizace).
- **Asynchronní (samosynchronizující)** — $h_i = f(k, c_{i-n}, \dots, c_{i-1})$; po $n+1$ správných znacích se obnoví synchronizace (historicky Vigenèrův autokláv).

**Výhoda:** malá propagace chyby (chyba v 1 znaku ŠT → 1 znak OT). Vhodné pro linkové/terminálové šifrátory a zařízení s malou pamětí.

### 2.2 Vernamova šifra (OTP)

Náhodné heslo **stejně dlouhé jako OT**, použité **jen jednou**. Má **dokonalé utajení** (ŠT nenese žádnou informaci o OT). Nevýhoda: heslo stejně dlouhé jako zpráva a jednorázové ⇒ neprovozuschopné pro velké objemy.

### 2.3 RC4

Rivest, 1987; jedna z nejrozšířenějších (SSL, S/MIME), **dnes prolomená**. Volitelná délka klíče (40/128 b), nevyužívá IV. Princip: klíč inicializuje tajnou permutaci $S$ množiny $\{0,\dots,255\}$ (substituce bajt→bajt), z níž konečný automat generuje bajty hesla, jež se XORují na OT/ŠT:
- **KSA** (inicializace $S$): $j = (j + S[i] + k[i \bmod n]) \bmod 256$, prohoď $S[i] \leftrightarrow S[j]$.
- **PRGA** (generování hesla): $i = i+1$, $j = j + S[i]$, prohoď $S[i] \leftrightarrow S[j]$, výstup $h = S[(S[i]+S[j]) \bmod 256]$.

### 2.4 Salsa20 / ChaCha

**Salsa20** (Bernstein, 2005; eSTREAM). Operace **ARX** (32b sčítání $\boxplus$, XOR $\oplus$, rotace $\lll$) na stavu $16 \times 32$ b slov ($4\times4$ matice: 8 slov klíče, 2 čítač pozice, 2 nonce, 4 konstanty `"expand 32-byte k"`). Jen ARX ⇒ odolnost proti **časovým útokům**. Základ je **čtvrt-runda** $QR(a,b,c,d)$; lichá runda na sloupce, sudá na řádky, 10× (= 20 rund), nakonec se přičte vstup (znemožní obnovu vstupu). Výstup 64 B keystreamu. Varianty Salsa20/8, /12 (méně rund, nižší bezpečnost), XSalsa20 (192b nonce).

**ChaCha** (Bernstein, 2008) — upravená $QR$ aktualizuje každé slovo 2× a šíří změny rychleji (lepší rozptyl při stejném počtu operací). ChaCha20-Poly1305 = autentizované šifrování (QUIC/HTTP-3, OpenSSH); nahrazuje AES tam, kde chybí HW akcelerace (ARM).

### 2.5 A5/1

Synchronní proudová šifra pro **GSM** (1987; struktura rekonstruována 1999). Tři **LFSR** (délky 19, 22, 23 b) s primitivními polynomy (maximální perioda) a **nelineární taktování (majority clocking):**
- taktovací bity $R1[8], R2[10], R3[10]$; spočte se **většinová** hodnota $h$,
- posunou se jen registry, jejichž taktovací bit $= h$ (jediný nelineární prvek = základ bezpečnosti),
- výstupní bit $k_i = R1[18] \oplus R2[21] \oplus R3[22]$, ŠT $c_i = p_i \oplus k_i$.

Inicializace: registry naplněny 64b klíčem $K$ a 22b $IV$, pak 100 taktů „naprázdno“. Na rámec (228 b) se použije nový IV, stejný klíč.

### 2.6 Slabiny proudových šifer

- **Dvojí použití hesla** (klíčová slabina): pro $c_i = m_i \oplus h_i$ a $c_i' = m_i' \oplus h_i$ platí $c_i \oplus c_i' = m_i \oplus m_i'$ — heslo se vyruší a OT se luští jako knižní šifra (metoda předpokládaného slova). Proto **nikdy neopakovat (klíč, IV)**.
- Synchronní šifry mají **nedostatečnou difúzi** (pracují po jednotlivých znacích) a vyžadují přesnou synchronizaci.
- Konkrétní šifry: **RC4** a **A5/1** jsou prolomené; redukované varianty Salsa20/ChaCha (méně rund) mají nižší bezpečnost.

---

## 3. Blokové šifry

### 3.1 Princip a Feistelova síť

**[[Bloková-šifra|Bloková šifra]]** $(M, C, K, E, D)$ zpracovává bloky délky $t$, **všechny toutéž** transformací $E_K$ (resp. $D_K$). Cílem je **difúze** (jeden bit OT ovlivní mnoho bitů ŠT — lavinový efekt) i **konfúze** (složitý vztah ŠT↔klíč), dosahované střídáním substitucí (S-boxy, nelineární) a permutací v mnoha **rundách**.

**Feistelova síť:** blok se rozdělí na poloviny $(L_i, R_i)$ a v každé rundě
$$(L_{i+1}, R_{i+1}) = (R_i,\ L_i \oplus f(R_i, k_{i+1})).$$
Výhoda: dešifrování je **stejné** schéma s obráceným pořadím rundovních klíčů; rundovní funkce $f$ **nemusí být prostá** (nepočítá se její inverze).

### 3.2 DES

Data Encryption Standard (FIPS 46-3, 1977). **Feistelova** iterovaná šifra: blok **64 b**, klíč **56 b** (uváděn jako 64 b s paritními bity), **16 rund**, rundovní klíče $k_1,\dots,k_{16}$ (48 b) z rotovaných polovin klíče. Runda: počáteční permutace → $f$ (expanze 32→48 b, XOR s $k_i$, **S-boxy** 6→4 b = jediný nelineární prvek, permutace $P$) → závěrečná inverzní permutace. **Slabina:** příliš **krátký klíč 56 b** (1998 prolomen hrubou silou – DES-Cracker); teoreticky slabé/poloslabé klíče, komplementárnost, lineární a diferenciální kryptoanalýza.

### 3.3 3DES (TripleDES)

Prodloužení klíče trojím použitím DES, varianta **EDE**:
$$\text{ŠT} = E_{K_3}(D_{K_2}(E_{K_1}(\text{OT}))).$$
Klíč **112 b** (2 klíče, $K_1=K_3$) nebo **168 b** (3 klíče). EDE kvůli zpětné kompatibilitě ($K_1=K_2=K_3 \Rightarrow$ 3DES = DES). Spolehlivá (dostatečně dlouhý klíč), lze v operačních módech (3DES-EDE-CBC).

### 3.4 AES

Advanced Encryption Standard (Rijndael, Daemen & Rijmen; FIPS 197, 2002), náhrada DES. **Blok 128 b**, klíč **128/192/256 b**, počet rund $N_r = 10/12/14$. **Není Feistelovský** (substitučně-permutační síť). Pracuje nad $GF(2^8)$. Stav = matice $4\times4$ B. Runda:
- **SubBytes** — substituce každého bajtu (S-box, jediná nelinearita),
- **ShiftRows** — cyklický posun řádků (transpozice),
- **MixColumns** — lineární transformace sloupců (násobení v $GF(2^8)$; v poslední rundě vynechána),
- **AddRoundKey** — XOR rundovního klíče.

Před 1. rundou úvodní AddRoundKey. Dešifrování inverzními operacemi. **Bez slabých klíčů**, odolný vůči lineární a diferenciální kryptoanalýze. Vhodný pro SW i HW, malé nároky na paměť.

### 3.5 Parametry — přehled

| Šifra | Blok [b] | Klíč [b] | Rundy | Typ |
|---|---|---|---|---|
| DES | 64 | 56 | 16 | Feistel |
| 3DES | 64 | 112 / 168 | 48 | Feistel (3× DES) |
| AES | 128 | 128 / 192 / 256 | 10 / 12 / 14 | SPN |

---

## 4. Operační módy blokových šifer

Mód = způsob použití blokové šifry na zprávu delší než jeden blok. Mody: **ECB, CBC, CFB, OFB, CTR, CBC-MAC**. (Samotná šifra ani mody — kromě CBC-MAC — **nezajišťují integritu**.)

### 4.1 ECB (Electronic Codebook)
$$\text{ŠT}_i = E_K(\text{OT}_i).$$
Každý blok zvlášť. **Slabiny:** stejné bloky OT → stejné bloky ŠT (prozrazuje strukturu, např. opakující se data); útočník může bloky ŠT **vyměňovat, vkládat, vypouštět** (porušení integrity). Základní, ale nedoporučovaný.

### 4.2 CBC (Cipher Block Chaining)
$$\text{ŠT}_0 = IV, \quad \text{ŠT}_i = E_K(\text{OT}_i \oplus \text{ŠT}_{i-1}); \qquad \text{OT}_i = \text{ŠT}_{i-1} \oplus D_K(\text{ŠT}_i).$$
Každý blok se před šifrováním XORuje s předchozím ŠT ⇒ **difúze celého předchozího OT**, náhodný IV ⇒ stejný OT dá pokaždé jiný ŠT. **Nejpoužívanější** mód; samosynchronizace (zotaví se po 2 správných blocích). Slabina: sériové (neparalelizovatelné) šifrování; stále nezajišťuje integritu.

### 4.3 CFB (Cipher Feedback)
$$\text{ŠT}_i = \text{OT}_i \oplus E_K(\text{ŠT}_{i-1}); \qquad \text{OT}_i = \text{ŠT}_i \oplus E_K(\text{ŠT}_{i-1}).$$
Převádí blokovou šifru na **proudovou** (zpětnou vazbou z ŠT). Bloková šifra se používá jen ve směru $E_K$ (výhodné v HW). **Samosynchronní** (po 2 nenarušených $b$-bitových blocích).

### 4.4 OFB (Output Feedback)
$$H = E_K(IV),\quad \text{ŠT}_i = \text{OT}_i \oplus H,\quad H \leftarrow E_K(H).$$
**Čistě synchronní** proudová šifra — heslo generováno autonomně (nezávisí na OT/ŠT). Bloková šifra jen $E_K$. Slabina: konečný automat má $\le 2^N$ stavů ⇒ **perioda hesla** je omezená (pro plnou zpětnou vazbu $b=N$ až $2^{N-1}$, pro $b<N$ jen cca $2^{N/2}$); nesmí se opakovat heslo.

### 4.5 CTR (Counter)
$$\text{CTR}_i = (IV + i - 1) \bmod 2^{B},\quad H_i = E_K(\text{CTR}_i),\quad \text{ŠT}_i = \text{OT}_i \oplus H_i.$$
Synchronní proudová šifra s **předem danou periodou** (čítač). **Paralelizovatelný**, libovolný přístup (heslo závisí jen na pozici a IV, jediná transformace $E_K$). **Slabina:** v žádných zprávách pod stejným klíčem se nesmí **opakovat hodnota čítače** (jinak dvojí použití hesla → rozluštění).

### 4.6 CBC-MAC (integrita)
Proudové i blokové šifry zajišťují **důvěrnost, ne integritu**. **CBC-MAC** autentizuje původ a chrání před změnami: zpráva se „šifruje“ v CBC s **nulovým IV** a samostatným klíčem $K_1$, výstupem je až **poslední blok** $\text{ŠT}_n$ (volitelně ještě $E_{K_2}(\text{ŠT}_n)$, případně zkrácení). Symetrická technika ⇒ autentizace původu dat, **ne nepopiratelnost**.

**Metoda solení IV** (CBC/CFB/OFB/CTR): přenese se $IV$, ale šifruje se „osoleným“ $IV'$ vypočteným z $IV$ a klíče (např. haší) — skutečné $IV'$ se neobjeví na kanále.

---

## 5. Co je potřeba na zkoušku znát

### Definice
- [[Symetrická-šifra]]: $K_E$, $K_D$ stejné / snadno převoditelné.
- [[Bloková-šifra]]: bloky délky $t$, všechny toutéž $E_K$.
- [[Proudová-šifra]]: proud hesla $h_i$, $c_i = m_i \oplus h_i$.
- Feistelova síť: $(L_{i+1}, R_{i+1}) = (R_i, L_i \oplus f(R_i, k_{i+1}))$.
- Operační módy: ECB, CBC, CFB, OFB, CTR, CBC-MAC.

### Klíčová fakta a slabiny
- **Bloková × proudová:** difúze (celý blok × znak), propagace chyby (blok × znak).
- **DES** — 64b blok, **56b klíč (krátký ⇒ prolomen hrubou silou)**, Feistel, S-boxy = nelinearita.
- **3DES** EDE — 112/168 b; **AES** — 128b blok, 128/192/256 b, SPN, bez slabých klíčů.
- **Vernam (OTP)** = dokonalé utajení (jednorázové heslo délky OT).
- **Dvojí použití hesla** u proudových šifer (a OFB/CTR) ⇒ $c \oplus c' = m \oplus m'$ → rozluštění.
- **ECB slabina:** stejný OT → stejný ŠT, manipulovatelnost bloků. **CBC** = nejpoužívanější, difúze + náhodný IV.
- CFB/OFB/CTR převádějí blokovou šifru na proudovou (jen $E_K$). **CTR** paralelní, náhodný přístup. **OFB** omezená perioda hesla.
- Šifrování **nezajišťuje integritu** ⇒ **CBC-MAC** (ne nepopiratelnost).

### Algoritmy / postupy
- **Feistel** runda a dešifrování (obrácené pořadí klíčů).
- **DES** runda ($f$: expanze, XOR klíče, S-boxy, $P$).
- **AES** runda (SubBytes, ShiftRows, MixColumns, AddRoundKey).
- **RC4** (KSA + PRGA), **A5/1** (3 LFSR + majority clocking), **Salsa20/ChaCha** (ARX, QR).
- Předpisy módů ECB/CBC/CFB/OFB/CTR/CBC-MAC.
