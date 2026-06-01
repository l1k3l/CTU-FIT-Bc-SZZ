---
tags: [otázka, kurz/PSI, otázka/24, hotovo]
---

# ISO/OSI model, linková a síťová vrstva, směrování

> **Otázka SZZ:** ISO/OSI model, enkapsulace a dekapsulace posílaných dat, princip IP adresace. Linková vrstva, podvrstvy LLC. MAC, síťová zařízení, princip přepínání. Virtuální sítě (VLAN). Síťová vrstva, směrovače, princip směrování, protokoly IPv4 a IPv6, statické a dynamické směrování.

Zdroje: BI-PSI přednášky 1 (Úvod, ISO/OSI, IPv4 adresace), 2 (Linková vrstva, Ethernet), 3 (VLAN + síťová vrstva IPv4), 4 (Směrování), 5 (IPv6) — Jan Fesl, FIT ČVUT.

---

## 1. ISO/OSI model

![[ISO-OSI-model#Definice]]

**Skupiny vrstev:**
- **Vrstvy hostitelů** (4–7) — zpracovávají se na koncových stanicích.
- **Vrstvy média** (1–3) — řeší přenos přes síť.

Idea pochází z poloviny 80. let. Vrstvy jsou záměrně oddělené ⇒ **nezávislý vývoj
a implementace**. Pro každou vrstvu jsou definovány **komunikační protokoly**,
důležitá je jejich **standardizace** (RFC). Médium = prostředí, ve kterém se
přenášejí data (kabel, vzduch).

**TCP/IP model** je praktický **4vrstvý** model: Application (= OSI 7+6+5),
Transport (= OSI 4), Internet (= OSI 3), Network Interface (= OSI 2+1). IP se
týká **síťové vrstvy**, TCP/UDP **transportní vrstvy**.

---

## 2. Enkapsulace a dekapsulace posílaných dat

![[Enkapsulace#Definice]]

Schématicky (vysílač, shora dolů — přidávání hlaviček):

$$\text{PDU}_7 = \text{ALH} + \text{DATA}, \quad \text{PDU}_6 = \text{PLH} + \text{PDU}_7, \quad \dots$$

kde `xLH` = Layer Header dané vrstvy. Na přijímací straně (zdola nahoru) každá
vrstva **odebere svou hlavičku** (dekapsulace). Na fyzické vrstvě se přenášejí
**bity**. Linková vrstva navíc přidává **zápatí/trailer** (FCS).

> **Klíčový princip:** komunikace mezi stanicemi A a B probíhá vždy na úrovni
> **stejných vrstev** — hlavička přidaná určitou vrstvou A je čtena toutéž
> vrstvou na B.

---

## 3. Princip IP adresace

**[[IP-adresa]]** je logický identifikátor síťového rozhraní (NIC). Na rozdíl od
linkové (MAC) adresy je **hierarchická** — adresy lze sdružovat do sítí
(podsítí), což umožňuje směrování.

**Velikost adresního prostoru:** pro $N$ bitů je max. počet adres $p = 2^N$.
V 80. letech zvoleno $N = 32$ (≈ $4\cdot10^9$ adres) → **IPv4**; později $N = 128$
(≈ $3\cdot10^{38}$) → **IPv6**.

**IPv4 adresa** = 32 bitů zapsaných po oktetech `X.X.X.X` (každý 0–255), např.
`123.122.120.121`.

### Maska, prefix, adresa sítě

- **Maska sítě** má 32 bitů: zleva souvislá řada jedniček délky **prefixu**,
  zbytek nuly. Říká, kolik bitů adresy mají všechny stanice téže (pod)sítě
  **společných**. Poslední byte masky: $256 - 2^{\,32-\text{prefix}}$.
- **Prefixová notace** `IP/prefix`, např. `123.123.123.120/30` (30 společných
  bitů, $32-30=2$ host-bity ⇒ $2^2=4$ adresy).
- **Adresa sítě** = nejnižší adresa rozsahu = `IP AND maska` (po bitech); používá
  se pro směrování.
- **Broadcast** = nejvyšší adresa rozsahu (zpráva pro všechny stanice podsítě).
- **Brána** = implicitní směrovač (typicky druhá nejvyšší/nejnižší adresa).
- **Počet využitelných adres** = $2^N-2$ (adresa sítě + broadcast se odečtou),
  resp. $2^N-3$ s vyhrazenou bránou; $N$ = počet host-bitů.

**Příklad `/30`:** `…120` = adresa sítě, `…121` stanice, `…122` brána, `…123`
broadcast. Dvě adresy patří do stejné sítě ⇔ `IP AND maska` dá stejnou adresu
sítě (jinak je cíl mimo lokální síť ⇒ posílá se přes bránu).

> Speciální rozsahy a třídy A–E viz [[IP-adresa]] a §8.

---

## 4. Linková vrstva, podvrstvy LLC a MAC

**Účel:** přenášení dat **v rámci lokální (LAN) sítě**; základní jednotka je
**rámec**. Linková vrstva se skládá ze dvou podvrstev:

| Podvrstva | Funkce | HW-závislost |
|---|---|---|
| **MAC** (Medium Access Control) | přístup k médiu (multiplex), **[[MAC-adresa\|linkové adresy]]**, filtrování, přepínání a doručování rámců, fronty, QoS, VLAN | **ano** (svázána s technologií fyz. vrstvy) |
| **LLC** (Logical Link Control, IEEE 802.2) | kódování, **logické řízení toku**, detekce/oprava chyb, rozdělení dat do rámců (framing) | **ne** |

### MAC adresy a přístup k médiu

**[[MAC-adresa]]:** 48 bitů (6 B) = OUI (3 B výrobce) + sériové číslo (3 B);
broadcast `FF:FF:FF:FF:FF:FF`.

**Multiplex** umožňuje sdílení média více účastníky; při současném neoddělitelném
použití nastane **kolize** (v celé **kolizní doméně**). Druhy: **TDMA** (časový),
**FDMA** (frekvenční; v optice WDM), **CDMA** (kódový), **SDMA** (prostorový).
**Metody s příposlechem** (Carrier Sense) zabraňují kolizím: prostá **CSMA**,
**CSMA/CD** (Collision Detection — při kolizi vyšle Jam signál a čeká náhodnou
dobu; kolize i tak hrozí v **kolizním okénku** = době šíření signálu),
**CSMA/CA** (Collision Avoidance, bezdrát).

### LLC: řízení toku a detekce chyb

**Potvrzovací schémata** (zdroj nesmí poslat víc, než cíl zvládne):
- **Stop & Wait** — pošle 1 rámec a čeká na potvrzení; při ztrátě potvrzení po
  **timeoutu** opakuje.
- **Selective Repeat** — kontinuální, opakuje **jen chybný** rámec.
- **Go-Back-N** — kontinuální, po chybě opakuje **všechny následující** rámce.
- **Klouzavé okénko** (viz §pro TCP, ot. 25).

**Detekce chyb — CRC** (Cyclic Redundancy Check): zdroj vypočte kontrolní součet
**kodérem** před přenosem, příjemce ho **dekodérem** přepočítá; shodují-li se,
přenos je bezchybný. CRC se počítá pomocí **generujícího binárního polynomu**
$G(x)$ (aritmetika modulo 2): zakódování $B(x) = A(x)\cdot G(x)$; je-li po přijetí
$C(x)/G(x)$ beze zbytku, je rámec korektní. Ethernet používá **CCITT-32**.

### Ethernet rámec a MTU

| preambule (8 B, vč. SOF) | cíl MAC (6 B) | zdroj MAC (6 B) | ethertyp (2 B) | data (46–1500 B) | FCS (4 B) |
|---|---|---|---|---|---|

**MTU** (Maximum Transfer Unit) = max. velikost přenášených dat; nastavuje se na
rozhraní, **není v rámci uvedena** (běžně 1500 B). Řízení toku v Ethernetu:
příkaz **PAUSE** (IEEE 802.3x). Ethernet sám **negarantuje spolehlivé doručení**.

---

## 5. Síťová zařízení a princip přepínání

**Zařízení podle vrstvy, na které pracují:**

| Zařízení | Vrstva | Pracuje s | Odděluje |
|---|---|---|---|
| Rozbočovač (hub), opakovač (repeater) | 1 — fyzická | bity | (nic) |
| **[[Přepínač\|Přepínač (switch)]]**, most (bridge) | 2 — linková | rámce (MAC) | **kolizní domény** |
| **[[Směrovač\|Směrovač (router)]]** | 3 — síťová | pakety (IP) | **broadcastové domény** |

### Princip přepínání

Přepínač přijme rámec (Frame in), zpracuje a odešle výstupním portem k příjemci
(Frame out). Výstupní port volí podle **přepínací tabulky** (MAC → port), kterou
plní **učením**: rámec s neznámou cílovou MAC rozešle na všechny porty kromě
příchozího (flooding) a podle zdrojové adresy odpovědi zaznamená port. Porty mají
**buffery** (regulace toku).

**Režimy:** Store-and-Forward (přijme celý rámec, pak odešle — předpoklad v
BI-PSI), Cut-Through (čte jen cílovou adresu ~6 B), Fragment-Free (čte celou
hlavičku ~64 B).

**Most (bridge)** funguje obdobně (2–4 porty, bez bufferů). **Smyčky** v topologii
způsobí nekonečné obíhání rámců — řeší je **Spanning Tree Protocol**: z topologie
reprezentované **[[Graf|grafem]]** (uzly = přepínače, hrany = linky) vytvoří
**[[Kostra|kostru]]** bez smyček pomocí **zaplavování** (flooding) s detekcí
duplicitních zpráv podle unikátního ID.

**Kolizní doména** = množina stanic sdílejících médium; **broadcastová doména** =
množina stanic, jimž je doručen rámec s všesměrovou adresou (oddělí ji až
směrovač).

---

## 6. Virtuální sítě (VLAN)

![[VLAN#Definice]]

### Druhy a značení (802.1Q)

Členství: **dle portů**, **dle MAC adres**, **dle protokolu**, **dle značky**
(tag-based, dnes nejběžnější), vícenásobné (**Q-in-Q**).

**IEEE 802.1Q** vkládá do Ethernet rámce **4bajtovou značku za MAC adresy**:

| TPID (VLAN protokol ID, 2 B) | TCI (2 B) = PCP (3 b) + CFI (1 b) + **VID (12 b)** |
|---|---|

- **VID** (VLAN Identifier) 12 bitů ⇒ $2^{12} = 4096$ VLAN; **PCP** priorita
  (802.1p); **CFI** formát. Značený rámec má data **42–1500 B** (o 4 B menší
  minimum). Běžný a značený Ethernet **nejsou kompatibilní**.
- **Trunk port** přenáší více VLAN (rámce **značené**); **access port** vede ke
  stanici (značka se při odchodu **odebírá**, při příchodu **navrací** dle
  příslušnosti portu) — pro stanice, které značení nepodporují.
- Přepnutí značeného rámce: nejprve se dle **VID** zvolí cílová VLAN, pak port.

**Inter-VLAN routing:** přepínač provoz mezi VLAN **neprouští** (jeho úkolem je
oddělovat); přenos mezi VLAN zajišťuje **směrovač** (síťová vrstva) — provoz se
**směruje, ne přepíná**.

---

## 7. Síťová vrstva, směrovače, princip směrování

**Síťová vrstva** doručuje data **mezi stanicemi v různých sítích** po
**paketech** (datagramech, až 64 KB); definuje IP adresy a zajišťuje **směrování**.
Adresace je **hierarchická** (zásadní rozdíl oproti linkové vrstvě).

**[[Směrovač]]** přeposílá pakety mezi sítěmi; adresně patří do všech sítí, které
propojuje. Při průchodu (**hop**) sníží **TTL** o 1.

**[[Směrování]]** = hledání **cesty** (posloupnosti směrovačů) mezi zdrojovou a
cílovou stanicí. Informace jsou ve **směrovací tabulce** (záznam: cíl, brána,
maska, metrika, rozhraní). Brána `0.0.0.0` = lokální síť (doručení linkovou
vrstvou); `0.0.0.0/0` = **default route**.

### Princip směrování (krok za krokem)

1. Stanice/směrovač zjistí, zda cíl leží v lokální síti: `cíl AND maska` vs.
   `vlastní IP AND maska`. Shodují-li se → doručení **linkovou vrstvou** přímo;
   jinak → přes **bránu**.
2. Směrovač podle cílové IP a směrovací tabulky zvolí **odchozí rozhraní /
   další skok**, **sníží TTL o 1** a předá paket linkovou vrstvou sousedovi.
3. Opakuje se, dokud paket nedorazí směrovači, v jehož lokální síti cíl leží;
   ten ho doručí cílové stanici.

**Parametry metod:** optimalita (metrika — nejkratší/nejlevnější), redundance
(multipath), symetrie, způsob hledání (záplavové/proaktivní/reaktivní), oblast
(vnitřní/vnější). **Proaktivní** = používá tabulky (nejběžnější); **reaktivní** =
bez tabulek (ad-hoc/mobilní sítě, cesta se hledá až je potřeba).

---

## 8. Protokoly IPv4 a IPv6

### IPv4

**Hlavička** (proměnné délky, min. 20 B):

| pole | význam |
|---|---|
| verze (4 b), IHL | verze (0x4), délka hlavičky v 32b slovech |
| typ služby (TOS) | QoS |
| celková délka | délka paketu v B |
| identifikace | spojuje fragmenty téhož paketu |
| příznaky (3 b), offset fragmentu (13 b) | řízení fragmentace; pozice fragmentu |
| TTL | ochrana proti zacyklení (každý hop −1, 0 = zahození) |
| protokol | komu předat data (TCP/UDP/ICMP…) |
| kontrolní součet hlavičky | kontrola **jen hlavičky** |
| zdrojová / cílová adresa | 32 b každá |
| volby + data | |

**Fragmentace:** je-li paket větší než MTU rozhraní, rozdělí se na **fragmenty**;
fragmentaci provádí **kterýkoli směrovač** na cestě, **složení až cílová stanice**
(podle identifikace + offsetu). Lze zakázat příznakem **Don't Fragment**.
*Příklad:* MTU 520→200, IP hlavička 20 B ⇒ na druhém úseku jen 180 B dat ⇒
500 B dat = 180 + 180 + 140 = **3 fragmenty**.

**Pomocné protokoly:** **ICMP** (ping = echo request type 8 / reply type 0,
traceroute pomocí rostoucího TTL → time exceeded), **ARP** (mapuje IP→MAC:
ARP-REQUEST broadcastem, ARP-REPLY unicastem, ukládá do ARP tabulky; zranitelný
**ARP spoofingem**), **DHCP** (dynamické přidělení IP; aplikační vrstva, UDP porty
67 server / 68 klient; výměna **Discover → Offer → Request → ACK** broadcastem).

### IPv6

Důvody: vyčerpání IPv4 (2011), **128bitové adresy**, automatická konfigurace,
mobilita, NAT už není potřeba (lze pro bezpečnost/oddělení), zpětná kompatibilita.

- **Zápis:** 8×16 b hexadecimálně oddělených `:`; zkracování vynecháním
  nevýznamných nul a jednou `::` (nahradí max. souvislou řadu nul).
- **Typy adres:** unicast, **multicast**, **anycast** — **broadcast neexistuje**
  (nahrazen multicastem). LL `fe80::/10` (lokální linkové), UL `fc00::/7`
  (obdoba privátních), loopback `::1/128`, multicast `ff00::/8`, individuální
  globální (veřejné).
- **Hlavička** (40 B): verze, třída provozu, **značka toku** (flow label),
  délka dat, **další hlavička**, **max. skoků** (= TTL), 128b zdroj + 128b cíl.
  Oproti IPv4 **bez kontrolního součtu**, **bez polí pro fragmentaci**
  (fragmentaci určuje **zdroj**, ne směrovače) — fragmentace a další funkce jsou
  v **řetězených rozšiřujících hlavičkách** (přenášejí se jen potřebné).
- **Identifikátor rozhraní (EUI-64, 64 b)** se odvodí z MAC: mezi 3. a 4. bajt se
  vloží `FF:FE` a invertuje se 7. bit.
- **ICMPv6** nahrazuje ICMP+ARP+ND; **objevování sousedů (Neighbor Discovery)**:
  RS/RA (výzva/ohlášení směrovače) pro **SLAAC** (bezstavová autokonfigurace —
  směrovač pošle 64b prefix, stanice ho zkombinuje s EUI-64), NS/NA pro zjištění
  MAC (náhrada ARP). Stavová konfigurace = **DHCPv6**. **NAT64** překládá IPv6↔IPv4.

### Srovnání IPv4 vs IPv6

| | IPv4 | IPv6 |
|---|---|---|
| délka adresy | 32 b | 128 b |
| autokonfigurace | ne (DHCP) | ano (SLAAC i DHCPv6) |
| hlavička | jedna, s fragmentací a checksumem | základní + řetězené rozšiřující, bez checksumu |
| fragmentace | každý směrovač | jen zdroj |
| broadcast | ano | ne (multicast) |
| IP→MAC | ARP | Neighbor Discovery (ICMPv6) |

---

## 9. Statické a dynamické směrování

![[Směrování#Statické vs. dynamické]]

### Dynamické směrovací algoritmy

| Algoritmus | Vyměňuje | Optimalizace | Protokol | Oblast |
|---|---|---|---|---|
| **Distance Vector (DVA)** | vektory vzdáleností (delší zprávy), nedostupnost = ∞ | distrib. **[[Bellman-Ford]]** (relaxace) | **RIP** | vnitřní |
| **Link State (LSA)** | stavy linek → graf (krátké zprávy) | **[[Dijkstra]]** ([[Kostra|kostra]] nejkratších cest) | **OSPF**, IS-IS | vnitřní (IS-IS i vnější) |
| **Path Vector (PVA)** | celé cesty (posloupnost ID AS) | délka cesty (AS_PATH) | **BGP** | vnější |

- **Relaxace (DVA/RIP):** je-li $d(X,Z) > d(X,Y) + d(Y,Z)$, změň pro $Z$ bránu na
  $Y$. LSA je méně náročné na linku, ale více na CPU (každý směrovač řeší instanci
  Dijkstry).
- **Autonomní systém (AS)** = skupina IP rozsahů jednoho ISP (16b ID).
  **Vnitřní směrování** uvnitř AS (RIP/OSPF), **vnější** mezi AS (**BGP** přes
  **hraniční směrovače**). **BGP** šíří **AS_PATH** (posloupnost ID AS); pokud
  dorazí cesta s vlastním ID, detekuje se **smyčka**. **Internet** = množina
  vzájemně propojených AS. Statické a dynamické směrování lze kombinovat.

---

## Co je potřeba na zkoušku znát

### Definice
ISO/OSI (7 vrstev + datové jednotky, vrstvy hostitelů/média), enkapsulace/
dekapsulace (PDU, hlavičky), IP adresa (maska, prefix, adresa sítě = IP AND maska,
broadcast, brána), MAC adresa (48 b, OUI), kolizní vs. broadcastová doména,
přepínač/most/směrovač (která vrstva), VLAN (802.1Q, VID 12 b → 4096), směrování
(cesta, statické/dynamické), AS.

### Mechanismy a postupy
- Výpočet adresy sítě, broadcastu, počtu adres ($2^N-2$); rozhodnutí lokální vs.
  vzdálené doručení (AND s maskou).
- Princip přepínání (učení tabulky, store-and-forward); Spanning Tree (kostra grafu
  zaplavováním).
- 802.1Q značení, trunk vs. access port, inter-VLAN routing přes směrovač.
- Průchod paketu směrovači (TTL −1 na hop), směrovací tabulka.
- IPv4 hlavička + fragmentace (umět příklad MTU); ICMP/ARP/DHCP role.
- IPv6: 128 b, zkracování `::`, žádný broadcast, EUI-64, SLAAC (RS/RA), ICMPv6/ND
  místo ARP; srovnání s IPv4.
- 3 dynamické algoritmy (DVA→RIP/Bellman-Ford, LSA→OSPF/Dijkstra, PVA→BGP),
  vnitřní vs. vnější směrování.
