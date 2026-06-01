---
tags: [otázka, kurz/PSI, otázka/24, hotovo]
---

# 24 — ISO/OSI, linková a síťová vrstva, směrování (zkrácená verze)

## 1. ISO/OSI model
7 vrstev (shora): **Aplikační, Prezentační, Relační, Transportní** (segmenty),
**Síťová** (pakety), **Linková** (rámce), **Fyzická** (bity). Vrstvy hostitelů
(4–7) × vrstvy média (1–3). Komunikace vždy mezi **stejnými** vrstvami.
**TCP/IP** = 4 vrstvy (App = 7+6+5, Transport = 4, Internet = 3, NetIf = 2+1).

## 2. Enkapsulace / dekapsulace
**PDU = hlavička + obsah.** Sestup vrstvami → každá přidá hlavičku (enkapsulace);
příjemce zdola nahoru hlavičky odebírá (dekapsulace). Linková navíc trailer (FCS).

## 3. IP adresace ([[IP-adresa]])
Logická, hierarchická. $p=2^N$ adres. **IPv4 = 32 b** (4 oktety 0–255).
**Maska** = zleva jedničky délky prefixu. **Adresa sítě = IP AND maska** (nejnižší),
**broadcast** = nejvyšší, **brána** = implicitní směrovač. Využitelných $2^N-2$
($N$ = host-bity). Privátní: 10/8, 172.16/12, 192.168/16; loopback 127/8;
multicast 224/4. Třídy A(0–127)/B(128–191)/C(192–223) unicast, D multicast, E rez.

## 4. Linková vrstva — podvrstvy
Účel: přenos v **LAN**, jednotka **rámec**.
- **MAC** (HW-závislá): přístup k médiu (multiplex TDMA/FDMA/CDMA/SDMA, CSMA/CD),
  **[[MAC-adresa]]** (48 b = OUI 3 B + sériové 3 B, broadcast FF:FF:FF:FF:FF:FF),
  přepínání rámců.
- **LLC** (IEEE 802.2, ne-HW): řízení toku (**Stop&Wait / Selective Repeat /
  Go-Back-N**), detekce chyb **CRC** (gen. polynom, Ethernet = CCITT-32), framing.
- Ethernet rámec: preambule | cíl MAC | zdroj MAC | ethertyp | data 46–1500 | FCS.
  **MTU** = max. data, nastaveno na rozhraní (není v rámci).

## 5. Síťová zařízení, přepínání
hub/repeater = L1 (bity); **[[Přepínač|switch]]/most = L2** (rámce, oddělí
**kolizní domény**); **[[Směrovač|router]] = L3** (pakety, oddělí **broadcastové
domény**).
**Přepínání:** switch posílá rámec dle **přepínací tabulky** (MAC→port), kterou
plní **učením** (neznámá MAC → flooding). Režimy: Store-and-Forward / Cut-Through /
Fragment-Free. Smyčky → **Spanning Tree** = [[Kostra|kostra]] [[Graf|grafu]]
topologie (zaplavování, detekce duplicit).

## 6. VLAN ([[VLAN]])
Více virtuálních sítí v 1 fyzické, oddělení toků na **linkové vrstvě**.
Druhy: dle portů / MAC / protokolu / **značky (802.1Q)** / Q-in-Q.
**802.1Q tag = 4 B za MAC**: TPID(2B) + TCI(2B = PCP 3b + CFI 1b + **VID 12b →
4096**). **Trunk** port = více VLAN (značené), **access** port = stanice (značka
se odebírá/navrací). Mezi VLAN nutný **směrovač** (směruje, nepřepíná).

## 7. Síťová vrstva, směrovače, princip směrování
Doručuje pakety mezi sítěmi; hierarchická adresace.
**[[Směrovač]]** přeposílá pakety dle cílové IP, patří do všech propojených sítí,
na hop **TTL −1**. **[[Směrování]]** = hledání **cesty** (posloupnost směrovačů).
**Směrovací tabulka**: cíl | brána | maska | metrika | rozhraní (brána 0.0.0.0 =
lokální; 0.0.0.0/0 = default).
**Princip:** `cíl AND maska` = `vlastní AND maska`? → lokálně (link. vrstva), jinak
přes bránu; směrovač volí další skok dle tabulky, TTL −1, opakuje až k cíli.

## 8. Protokoly IPv4 a IPv6
**IPv4 hlavička:** verze/IHL, TOS, délka, identifikace, příznaky/offset, **TTL**,
protokol, **checksum (jen hlavička)**, zdroj/cíl, volby. **Fragmentace:**
> MTU → fragmenty (každý směrovač), složí **cíl** (identifikace+offset); zákaz =
DF. Pomocné: ICMP (ping/traceroute), ARP (IP→MAC, request broadcast/reply unicast),
DHCP (UDP 67/68, Discover/Offer/Request/ACK).
**IPv6:** 128 b, hex po 16 b, zkrácení `::` (1×). Typy: unicast/multicast/anycast
(**broadcast neexistuje**). Hlavička 40 B: bez checksumu, bez fragm. polí
(fragmentuje **zdroj**), **max. skoků** = TTL, řetězené rozšiřující hlavičky.
**EUI-64** z MAC (vloží FF:FE, invertuje 7. bit). **ICMPv6** + **Neighbor
Discovery** (RS/RA = SLAAC autokonfigurace; NS/NA místo ARP). NAT už netřeba.

## 9. Statické vs. dynamické směrování ([[Směrování]])
**Statické** = manuální, hned funkční, nereaguje na změny (malé sítě).
**Dynamické** = protokoly automaticky, reagují na změny.
- **DVA** (vektory vzdáleností, [[Bellman-Ford]], ∞ = nedostupné) → **RIP** (vnitřní)
- **LSA** (stavy linek, [[Dijkstra]], kostra nejkratších cest) → **OSPF/IS-IS**
- **PVA** (cesty = ID AS, AS_PATH, loop detekce) → **BGP** (vnější)
**AS** = IP rozsahy ISP; vnitřní (RIP/OSPF) × vnější (BGP, hraniční směrovače).

---
## Co odpovědět rychle
- **OSI 7 vrstev** + datové jednotky; **enkapsulace** = přidávání hlaviček.
- **Adresa sítě = IP AND maska**; broadcast = max, brána = router.
- **L2 switch** (kolizní domény, učení MAC) × **L3 router** (broadcast domény, TTL).
- **VLAN 802.1Q**: 4B tag, VID 12 b → 4096; trunk × access.
- **IPv4** 32 b (fragmentuje každý router) × **IPv6** 128 b (fragmentuje zdroj, bez
  broadcastu, ND místo ARP).
- Dynamické: **RIP**=Bellman-Ford, **OSPF**=Dijkstra, **BGP**=path vector (mezi AS).
