---
tags: [otázka, kurz/KAB, otázka/9, todo]
---

# Asymetrické kryptosystémy, hešovací funkce, digitální podpis, certifikáty

> **Otázka SZZ:** Asymetrické kryptosystémy (šifra RSA, Diffie-Hellman, RSA digitální podpis), hešovací funkce (SHA-2, HMAC). Digitální podpis. Certifikáty, certifikační autority.

Zdroje: BI-KAB, přednášky 2 (exponenciální šifra, D-H, PDL), 5 (hašovací funkce, SHA-x, HMAC), 6 (RSA, DSA, ElGamal), 11 (infrastruktura veřejného klíče), prof. R. Lórencz, FIT ČVUT. Teorie čísel viz [[8DML-long|8DML]].

---

## 1. Asymetrické kryptosystémy

### 1.1 Princip kryptografie veřejného klíče

U [[Symetrická-šifra|symetrické šifry]] je z šifrovacího klíče snadno odvoditelný klíč dešifrovací ⇒ každá komunikující dvojice musí sdílet tajný klíč (problém **distribuce klíčů**).

**[[Asymetrická-šifra|Asymetrický (veřejný) kryptosystém]]** tento problém řeší dvojicí klíčů:

- **veřejný klíč** $VK$ — pro šifrování (resp. ověření podpisu), zveřejněn,
- **soukromý klíč** $SK$ — pro dešifrování (resp. podpis), tajný.

Zásadní podmínka: **výpočet $SK$ ze znalosti $VK$ je výpočetně neschůdný.** Kdokoli může Alici poslat zprávu zašifrovanou $VK_A$, ale dešifrovat ji umí jen Alice ($SK_A$). Matematicky jde o **[[Jednosměrná-funkce|jednosměrnou funkci s padacími dvířky]]** (trapdoor) — padacími dvířky je soukromý klíč.

Dvě základní použití (zrcadlově obrácená schémata):

| Cíl | Odesílatel | Adresát |
|---|---|---|
| **Šifrování** (důvěrnost) | $\text{ŠT} = E_{VK_2}(\text{OT})$ | $\text{OT} = D_{SK_2}(\text{ŠT})$ |
| **Autentizace/podpis** | $\text{ŠT} = D_{SK_1}(\text{OT})$ | $\text{OT} = E_{VK_1}(\text{ŠT})$ |

Bezpečnost stojí na výpočetně těžkých problémech:

| Těžký problém | Kryptosystémy |
|---|---|
| **Faktorizace** $n = pq$ | [[RSA]] |
| **[[Problém-diskrétního-logaritmu\|Diskrétní logaritmus]]** (PDL) | [[Diffie-Hellman]], ElGamal, DSA, ECDSA |

Asymetrické operace jsou pomalé ⇒ v praxi **hybridní schéma**: asymetricky se přenese symetrický klíč relace, jím se šifrují vlastní data.

### 1.2 Šifra RSA

**[[RSA]]** (Rivest, Shamir, Adleman, 1977) je asymetrický systém založený na **modulárním umocňování** a obtížnosti **faktorizace**.

**Generování klíčů:**
1. Zvol velká [[Prvočíslo|prvočísla]] $p, q$; spočti $n = pq$ a $\varphi(n) = (p-1)(q-1)$ ([[Eulerova-funkce|Eulerova funkce]]).
2. Zvol veřejný exponent $e$, $1 < e < n$, s $\gcd(e, \varphi(n)) = 1$.
3. Spočti soukromý exponent $d = e^{-1} \bmod \varphi(n)$ ([[Eukleidův-algoritmus|rozšířený Eukleidův algoritmus]]).
4. **Veřejný klíč** $VK = (n, e)$, **soukromý klíč** $SK = (n, d)$.

**Šifrování / dešifrování** bloku $m$ (po převodu na číslo $0 \le m < n$):
$$c = m^{e} \bmod n, \qquad m = c^{d} \bmod n.$$

**Věta (korektnost RSA).** Pro $\gcd(m, n) = 1$ platí $c^{d} \equiv m \pmod n$.

**Důkaz.** Z $ed \equiv 1 \pmod{\varphi(n)}$ je $ed = k\varphi(n) + 1$ pro nějaké $k \in \mathbb{Z}$. Z [[Eulerova-funkce|Eulerovy věty]] $m^{\varphi(n)} \equiv 1 \pmod n$, tedy
$$c^{d} = (m^{e})^{d} = m^{ed} = m^{k\varphi(n)+1} = \big(m^{\varphi(n)}\big)^{k}\, m \equiv 1^{k}\cdot m \equiv m \pmod n. \qquad \blacksquare$$
(Pro $\gcd(m,n) \neq 1$ platí rovnost také, dokáže se přes ČVOZ; pravděpodobnost takového $m$ je zanedbatelná.)

**Příklad.** $p = 43$, $q = 59$ ⇒ $n = 2537$, $\varphi(n) = 42 \cdot 58 = 2436$. Volíme $e = 13$ ($\gcd(13, 2436) = 1$). REA dá $d = 13^{-1} \bmod 2436 = 937$. Blok $m = 1520$: $c = 1520^{13} \bmod 2537 = 95$; zpět $m = 95^{937} \bmod 2537 = 1520$.

**Generování prvočísel.** Náhodná velká lichá čísla se testují **Rabinovým–Millerovým** pravděpodobnostním testem (např. 100 svědků ⇒ pravděpodobnost chyby $\approx 10^{-60}$). Z věty o prvočíslech je hustota prvočísel kolem $10^{340}$ asi $2/\ln(10^{340})$ ⇒ v průměru cca 400 pokusů na jedno prvočíslo. **Square-and-multiply** dělá umocňování rychlým ($O(\log N)$ násobení).

**Bezpečnost RSA.**
- Se znalostí $p, q$ (tedy $\varphi(n)$) se $d$ dopočítá Eukleidovým algoritmem. Bez nich je nalezení $\varphi(n)$ stejně těžké jako **faktorizace $n$**.
- Nebylo prokázáno dešifrování RSA bez faktorizace $n$.
- Doporučení: $p, q$ dostatečně velká a různá, $p-1$ i $q-1$ s velkým prvočíselným faktorem (ochrana proti speciálním faktorizačním technikám), např. FIPS 186-4 žádá $|p - q| > 2^{\,\text{délka } n / 2 - 100}$.

**Urychlení.**
- **Malý veřejný exponent** s nízkou Hammingovou váhou (např. $e = 2^{16}+1$) ⇒ rychlé šifrování.
- **RSA-CRT** — dešifrování přes Čínskou větu o zbytcích modulo $p$ a $q$ (čísla poloviční délky, paralelně) ⇒ 4–8× rychlejší. $SK = (p, q, d_p, d_q, q_{\text{inv}})$, kde $d_p = d \bmod (p-1)$, $d_q = d \bmod (q-1)$, $q_{\text{inv}} = q^{-1} \bmod p$.

### 1.3 Diffie–Hellman a problém diskrétního logaritmu

**[[Problém-diskrétního-logaritmu|Problém diskrétního logaritmu]] (PDL).** V grupě $G$ s generátorem $b$ je pro $y = b^{k}$ diskrétní logaritmus $\log_b y = k$; PDL je nalézt $k$. V $\mathbb{Z}_p^{*}$ **není znám** polynomiální algoritmus (v nejhorším případě); nejrychlejší (stále subexponenciální/exponenciální) jsou *baby-step giant-step*, *Pollardův $\rho$*, *Pohlig–Hellman*, *index kalkulus*, *funkční síto*.

**[[Diffie-Hellman|Diffie–Hellmanův]] protokol** ustaví sdílený tajný klíč přes nezabezpečený kanál (vychází z exponenciální šifry):

Veřejné prvky: prvočíslo $m$ a generátor $a$ grupy $\mathbb{Z}_m^{*}$.
1. $A$ zvolí tajné $k_1$, pošle $y_1 = a^{k_1} \bmod m$.
2. $B$ zvolí tajné $k_2$, pošle $y_2 = a^{k_2} \bmod m$.
3. Oba dopočtou stejný klíč
$$K = y_2^{\,k_1} \bmod m = y_1^{\,k_2} \bmod m = a^{k_1 k_2} \bmod m.$$

**Příklad.** $m = 13$, $a = 2$, $k_1 = 7$, $k_2 = 11$: $y_1 = 2^{7} \bmod 13 = 11$, $y_2 = 2^{11} \bmod 13 = 7$; $K = 7^{7} \bmod 13 = 11^{11} \bmod 13 = 6$.

**Bezpečnost a slabina.** Útočník zná $a, m, a^{k_1}, a^{k_2}$, ale bez $k_1$ či $k_2$ nedokáže spočítat $a^{k_1 k_2}$ (**Diffie–Hellmanův problém DHP**, není těžší než PDL). **Slabina:** protokol **neautentizuje** strany ⇒ je zranitelný vůči **man-in-the-middle**; řeší se podpisem / [[Certifikát|certifikáty]] veřejných hodnot.

### 1.4 ElGamal (doplnění)

**ElGamal** vzniká úpravou Diffie–Hellmana, staví též na PDL a umožňuje **šifrování i podpis**. Veřejný klíč $A$: $(m, g, y_A)$ s $y_A = g^{k_A} \bmod m$, soukromý $k_A$. Šifrování zprávy $p$: $B$ zvolí $k_B$, spočte $y_B = g^{k_B}$ a sdílený $K = y_A^{k_B}$, pošle $(y_B,\ c = p \cdot K \bmod m)$. Dešifrování: $A$ spočte $K = y_B^{k_A}$ a $p = c \cdot K^{-1} \bmod m$. (Nutno volit pro každou zprávu nové $k_B$.)

---

## 2. Hašovací funkce (SHA-2, HMAC)

### 2.1 Jednosměrnost a bezkoliznost

**[[Jednosměrná-funkce|Jednosměrná funkce]]** $f: X \to Y$: snadno se počítá $y = f(x)$, ale z náhodného $y$ je neschůdné najít vzor. Typy: (1) bez padacích dvířek (např. faktorizace), (2) s padacími dvířky (asymetrická kryptografie).

**Definice (hašovací funkce).** Pro $d \in \mathbb{N}$ a množinu $X$ binárních řetězců délky $0$ až $d$ je $h: X \to \{0,1\}^{n}$ **[[Hašovací-funkce|hašovací funkce]]**, je-li **jednosměrná 1. typu a bezkolizní**. Komprimuje libovolně dlouhý vstup $M$ na **haš** $h(M)$ pevné délky $n$ b.

> Pozor: jde o jiný pojem než hašovací funkce u [[Hešovací-tabulka|hešovacích tabulek]] (datová struktura) — tam stačí rovnoměrnost, kolize se řeší.

Z bezpečnostního hlediska se žádá, aby se $h$ chovala jako **náhodné orákulum** (na stejný vstup stejný výstup, na nový vstup „náhodný“).

**Bezkoliznost (odolnost proti kolizi):**
- **1. řádu (collision resistance):** neschůdné najít $M \neq M'$ s $h(M) = h(M')$.
- **2. řádu (2nd-preimage):** k danému vzoru $x$ neschůdné najít $y \neq x$ s $h(x) = h(y)$.

**Narozeninový paradox.** Pro $n$-bitovou haš nastává kolize 1. řádu s ~50 % pravděpodobností už ve skupině cca $2^{n/2}$ zpráv (ne $2^{n-1}$). Obecně mezi $k$ náhodnými prvky z $n$-prvkové množiny je pravděpodobnost shody $P(n,k) = 1 - \frac{n(n-1)\cdots(n-k+1)}{n^{k}}$; pro $k \approx \sqrt{n}$ je $P \approx 50\%$. (Klasicky $P(365, 23) \approx 0{,}507$.) Odolnost proti 2. vzoru zůstává $\approx 2^{n}$. ⇒ **délka haše určuje bezpečnost.**

### 2.2 Konstrukce moderních hašovacích funkcí

Zpráva je dlouhá (až $d = 2^{64}-1$ b) a přichází po částech ⇒ hašuje se **postupně po blocích** $M_1, \dots, M_N$.

**Zarovnání (padding):** doplnění bitem `1` a nutným počtem `0` ⇒ jednoznačné odejmutí. **Merkle–Damgårdovo zesílení:** posledních 64 b nese **délku původní zprávy** (eliminuje některé útoky; u SHA-1/256 do bloku 512 b).

**Merkle–Damgårdova (DM) iterativní konstrukce** s kompresní funkcí $f$:
$$H_i = f(H_{i-1}, M_i), \qquad H_0 = IV,$$
kde $H_i$ je **kontext** (šíře = délka haše). Výsledná haš je $H_N$.

**Věta (bezpečnost DM).** Je-li kompresní funkce $f$ bezkolizní, je bezkolizní i celá iterovaná hašovací funkce ⇒ stačí navrhnout kvalitní $f$.

**Kompresní funkce z blokové šifry.** Kvalitní [[Bloková-šifra|bloková šifra]] $E_k$ je vzhledem k pevnému klíči jednosměrná ⇒ $H_i = E_{M_i}(H_{i-1})$. **Davies–Meyerova** konstrukce jednosměrnost zesiluje XORem vstupu:
$$H_i = E_{M_i}(H_{i-1}) \oplus H_{i-1}.$$

### 2.3 SHA-1 a SHA-2

**SHA (Secure Hash Algorithm)**, NIST, FIPS 180. **SHA-1** (FIPS 180-1, 1995): vstup až $2^{64}-1$ b, blok 512 b, **haš 160 b**, kontext $5 \times 32$ b slov $A,B,C,D,E$, $4 \times 20 = 80$ rund (střídání funkcí $F,G,H,I$ a konstant $K_i$), expanze slov $w_i = {<<<}1(w_{i-16} \oplus w_{i-14} \oplus w_{i-8} \oplus w_{i-3})$, na závěr přičten kontext (Davies–Meyer). **SHA-1 je prolomena** (nalezeny kolize).

**SHA-2** (FIPS 180-2) — rodina SHA-256/384/512, stejná DM struktura, modulární aritmetika a logické operace, jiné parametry:

| | SHA-1 | SHA-256 | SHA-384 | SHA-512 |
|---|---|---|---|---|
| Délka haše [b] | 160 | 256 | 384 | 512 |
| Max. délka zprávy | $<2^{64}$ | $<2^{64}$ | $<2^{128}$ | $<2^{128}$ |
| Velikost bloku [b] | 512 | 512 | 1024 | 1024 |
| Velikost slova [b] | 32 | 32 | 64 | 64 |
| Počet rund $f$ | 80 | 64 | 80 | 80 |
| Bezpečnost [b] | 80 | 128 | 192 | 256 |

**SHA-256** používá funkce $Ch, Ma, \Sigma_0, \Sigma_1, \sigma_0, \sigma_1$ nad 32b slovy, např.
$$Ch(x,y,z) = (x \wedge y) \oplus (\lnot x \wedge z), \quad Ma(x,y,z) = (x \wedge y) \oplus (x \wedge z) \oplus (y \wedge z),$$
expanze $W_t = \sigma_1(W_{t-2}) + W_{t-7} + \sigma_0(W_{t-15}) + W_{t-16}$. SHA-2 je dosud považována za bezpečnou; rozdíl oproti SHA-1 je hlavně v délce haše (odolnost proti kolizím).

### 2.4 HMAC

**[[HMAC]]** (klíčovaný haš, FIPS PUB 198) hašuje zprávu $M$ spolu s **tajným klíčem** $K$. Pro blok kompresní funkce $b$ b, klíč doplněný na $K^{+}$ a konstanty $ipad = \texttt{0x36}^{b/8}$, $opad = \texttt{0x5C}^{b/8}$:
$$\mathrm{HMAC}_K(M) = H\big((K^{+} \oplus opad)\ \|\ H((K^{+} \oplus ipad)\ \|\ M)\big).$$

**Vlastnosti:** **nepadělatelný integritní kód** (bez $K$ nelze ke změněné zprávě dopočítat platný HMAC — samotná haš to neumí, útočník by ji přepočítal), **autentizace původu dat** a **průkaz znalosti** v challenge–response ($response = \mathrm{HMAC}_K(challenge)$). Jako symetrická technika **nezaručuje nepopiratelnost**.

---

## 3. Digitální podpis

### 3.1 Vlastnosti

**[[Digitální-podpis]]** je obvykle asymetrické schéma: podpis **soukromým klíčem**, ověření **veřejným klíčem**. Požaduje se:

- **autentizace / nezfalšovatelnost** (a **ověřitelnost** příjemcem) — podpis nelze napodobit,
- **integrita** — podepsanou zprávu nelze změnit, aniž by se podpis zneplatnil,
- **nepopiratelnost** — podepisující nemůže popřít podpis.

Falšování má být výpočetně neschůdné (jak vyrobit falešný podpis k existující zprávě, tak falešnou zprávu k existujícímu podpisu). **Kategorie:** přímé (direct) × arbitrované (s důvěryhodnou třetí stranou).

### 3.2 RSA digitální podpis

Subjekt 1 podepíše zprávu $m$ svým soukromým klíčem a (volitelně) zašifruje veřejným klíčem příjemce:
$$S = D_{SK_1}(m) = m^{d_1} \bmod n_1, \qquad c = E_{VK_2}(S) = S^{e_2} \bmod n_2.$$
Příjemce dešifruje $S = D_{SK_2}(c)$ a ověří
$$E_{VK_1}(S) = S^{e_1} \bmod n_1 = (m^{d_1})^{e_1} = m^{d_1 e_1} \equiv m \pmod{n_1},$$
neboť $d_1 e_1 \equiv 1 \pmod{\varphi(n_1)}$. Protože jen subjekt 1 zná $SK_1$, nemůže popřít autorství ⇒ **nepopiratelnost**.

### 3.3 Podpis haše (hash-then-sign) a DSA

V praxi se nepodepisuje dlouhá zpráva, ale její **[[Hašovací-funkce|haš]]**: podpis $= D_{SK}(h(M))$. Důvody: rychlost a [[Hašovací-funkce|bezkoliznost]] (nelze najít druhou zprávu se stejnou haší, tedy se stejným podpisem). Ověření: spočti $h(M)$ a porovnej s $E_{VK}(\text{podpis})$.

**DSA** (Digital Signature Standard) — podpisové schéma založené na [[Problém-diskrétního-logaritmu|PDL]]; podepisuje se haš $H(M)$, podpisem je dvojice $(r, s)$, ověření porovná přepočtenou hodnotu. (Obdoba ElGamal podpisu.)

---

## 4. Certifikáty a certifikační autority

### 4.1 Problém distribuce veřejných klíčů

Veřejný klíč je sice veřejný, ale jeho distribuce je ohrožena **podvržením** (aktivní útočník, MITM):

1. $A$ pošle $VK_A \| ID_A$ subjektu $B$.
2. Útočník $U$ zachytí zprávu, nahradí ji $VK_U \| ID_A$ a pošle $B$.
3. $B$ se domnívá, že $VK_U$ patří $A$, šifruje pro $A$ klíčem $VK_U$.
4. $U$ dešifruje $SK_U$, čte (a může měnit) zprávy, přešifruje pravým $VK_A$ a pošle $A$.

Techniky distribuce VK (vzestupně dle bezpečnosti):
1. **Zveřejnění** (public announcement) — jednoduché, neodolné proti podvržení.
2. **Veřejný adresář** (public directory) — spravuje důvěryhodná autorita; slabina: kompromitace $SK$ správce.
3. **Autorita pro veřejné klíče** — online dotaz na každý VK; slabina: „úzké hrdlo“.
4. **Certifikace** — bez kontaktu s třetí stranou při každé komunikaci.

### 4.2 Certifikát a X.509

**[[Certifikát]]** je struktura svazující veřejný klíč s identitou držitele. Obsahuje $VK_A$, identifikační údaje $ID_A$, dobu platnosti a další údaje CA, **podepsaná soukromým klíčem CA** $SK_{Aut}$:
$$C_A = E_{SK_{Aut}}(T, ID_A, VK_A), \qquad D_{VK_{Aut}}(C_A) = (T, ID_A, VK_A).$$
Úspěšné ověření $VK_{Aut}$ zároveň dokazuje, že certifikát vydala CA ⇒ certifikát je **nefalšovatelný** a lze ho veřejně zpřístupnit. Distribuce VK = pouhá **výměna certifikátů**.

Formát určuje **ITU-T X.509** (součást X.500): verze, sériové číslo, algoritmus podpisu, identifikace CA, doba platnosti, identifikace uživatele, veřejný klíč uživatele, jednoznačné identifikátory, rozšíření a **digitální podpis CA**.

### 4.3 Certifikační a registrační autorita

**[[Certifikační-autorita|Certifikační autorita (CA)]]** je důvěryhodná třetí strana, která **vydává, aktualizuje a odvolává** certifikáty; každý zná její $VK_{Aut}$. **Registrační autorita** přijímá žádosti a kontroluje údaje.

### 4.4 Certifikační strom, řetězec, křížová certifikace, PKI

- Pro mnoho uživatelů se zřizuje **více CA** ve **stromové struktuře**; kořen je **kořenová CA** s **kořenovým certifikátem** (ověřen jinou bezpečnou cestou).
- **Řetězec certifikátů** = od certifikátu uživatele ke kořeni; certifikát je platný $\iff$ jsou platné všechny v řetězci.
- **Křížová certifikace** (jedno-/obousměrná) propojuje různé stromy CA.
- **Platnost a odvolání:** omezená doba platnosti; odvolání při kompromitaci $SK$/certifikátu nebo změně CA; CA zveřejňuje **seznam odvolaných certifikátů (CRL)**.
- **PKI (Public Key Infrastructure)** — norma (z ITU-T X.500) pro vydávání, správu, používání a odvolávání klíčů a certifikátů; cíl: interoperabilita.

---

## 5. Co je potřeba na zkoušku znát

### Definice
- [[Asymetrická-šifra|Asymetrický kryptosystém]]: dvojice $VK/SK$, z $VK$ nelze schůdně získat $SK$; [[Jednosměrná-funkce|jednosměrná funkce s padacími dvířky]].
- [[RSA]]: $n = pq$, $\varphi(n) = (p-1)(q-1)$, $\gcd(e, \varphi(n)) = 1$, $d = e^{-1} \bmod \varphi(n)$; $c = m^e \bmod n$, $m = c^d \bmod n$.
- [[Diffie-Hellman]]: sdílený klíč $K = a^{k_1 k_2} \bmod m$.
- [[Problém-diskrétního-logaritmu|PDL]]: nalézt $k$ z $y = b^k$.
- [[Hašovací-funkce]]: jednosměrná + bezkolizní $h: X \to \{0,1\}^n$; bezkoliznost 1./2. řádu.
- [[Digitální-podpis]]: podpis $SK$, ověření $VK$; autentizace, integrita, nepopiratelnost.
- [[Certifikát]] a [[Certifikační-autorita|CA]], X.509, PKI.

### Klíčové věty a fakta
- **Korektnost RSA** z [[Eulerova-funkce|Eulerovy věty]]: $m^{ed} \equiv m \pmod n$.
- Bezpečnost RSA = obtížnost **faktorizace**; bezpečnost DH/ElGamal/DSA = **PDL**.
- **Bezpečnost Merkle–Damgård:** bezkolizní kompresní funkce ⇒ bezkolizní haš.
- **Narozeninový paradox:** kolize $n$-bitové haše už po $\approx 2^{n/2}$ zprávách.
- SHA-1 (160 b) prolomena; **SHA-2** (256/384/512) bezpečná.
- DH bez autentizace je zranitelný vůči **MITM** ⇒ nutnost certifikátů.
- HMAC a CBC-MAC zajišťují integritu + autentizaci původu, ale **ne nepopiratelnost** (symetrické).

### Algoritmy / postupy
- **Generování RSA klíčů** + Rabin–Miller test prvočíselnosti, square-and-multiply, RSA-CRT.
- **DH výměna klíčů** (3 kroky).
- **Merkle–Damgård** hašování (padding + délka), **Davies–Meyer** kompresní funkce.
- **HMAC**: $H((K^+ \oplus opad)\|H((K^+ \oplus ipad)\|M))$.
- **RSA podpis**: $S = m^d \bmod n$ (resp. podpis haše), ověření $S^e \bmod n$.
- **Ověření certifikátu** přes řetězec ke kořenové CA.
