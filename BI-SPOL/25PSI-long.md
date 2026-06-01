---
tags: [otázka, kurz/PSI, otázka/25, hotovo]
---

# Transportní vrstva (TCP/UDP), NAT, DNS

> **Otázka SZZ:** Transportní vrstva, protokol TCP, spolehlivost doručení paketů, zahlcení, srovnání s protokolem UDP. Překlad síťových adres (NAT) na síťové a transportní vrstvě. Systém doménových jmen (DNS).

Zdroje: BI-PSI přednášky 3 (NAT na síťové vrstvě), 6 (Transportní vrstva, TCP, UDP, NAT/PAT), 7 (DNS) — Jan Fesl, FIT ČVUT.

---

## 1. Transportní vrstva

**Hlavní úkol:** doručení dat ke **konkrétní službě/aplikaci (procesu)** běžící na
stanici dosažitelné prostřednictvím IP adresy. Zajišťuje **kontrolu toku** a
**opravy chyb** (např. ztracených paketů). Minimální jednotka = **segment**.

- Rozlišení aplikace zajišťuje **port** = **16bitový identifikátor** (další
  adresační stupeň). Adresace: `[zdrojová IP, zdrojový port] → [cílová IP, cílový
  port]`. **Porty < 1024** = privilegované (alokuje si je aplikace), ostatní
  **neprivilegované** (dynamicky přiděluje jádro OS).
- Doručování může být **spolehlivé/potvrzované** (TCP) nebo
  **nespolehlivé/nepotvrzované** (UDP).

**Parametry přenosu** (kvalita): **ztrátovost** (packet loss [%]), **zpoždění**
(delay [ms]), **RTT** (round-trip time, ≈ 2× zpoždění), **jitter** (kolísání
zpoždění — kompenzuje se nejhůř).

**Problémy při doručování** (řeší se **timeout + opakované odeslání + ACK**):
ztráta paketu, ztráta potvrzení (→ duplikace), opožděné potvrzení (→ duplikace).

**Problém dvou armád:** dokonale spolehlivé zahájení spojení **neexistuje** (vždy
chybí potvrzení posledního potvrzení) — proto se používá **3cestná výměna
(3-way handshake)** na začátku i konci spojení.

---

## 2. Protokol TCP

![[TCP#Definice]]

### Hlavička TCP (v datech IP paketu)

| zdrojový port | cílový port |
|---|---|
| **sekvenční číslo** odesílaného paketu | |
| **sekvenční číslo očekávaného** (= ACK) | |
| délka hlavičky · rezerva · příznaky **U A P R S F** · **délka okna** | |
| kontrolní součet · ukazatel naléhavých dat | |
| volby + data | |

**Příznaky:** U = Urgent, A = ACK, P = push (aplikační data), R = Reset, **S = SYN**,
**F = FIN**. **Sekvenční číslo** = pořadové číslo v rámci spojení (počáteční
náhodné, dále inkrementálně roste).

### Životní cyklus spojení (duplexní)

1. **Sestavení (3-way handshake):** `SYN (seq=x)` → `SYN, ACK (seq=y, ACK=x+1)` →
   `ACK (=y+1)`. Stavy: SYN_SENT / LISTEN → SYN_RCVD → ESTABLISHED.
2. **Přenos dat:** DATA ↔ ACK (obousměrně).
3. **Ukončení:** dva páry FIN/ACK — `FIN(u)`→`ACK(u+1)`, `FIN(v)`→`ACK(v+1)`.
   Stavy FIN_WAIT → CLOSE_WAIT / LAST_ACK → TIME_WAIT → CLOSED.

---

## 3. Spolehlivost doručení paketů

TCP **garantuje doručení i pořadí** a detekuje duplikáty. Mechanismy:

- **Stop & Wait** — pošle 1 paket, čeká na ACK; při chybějícím ACK po **timeoutu**
  opakuje. Jednoduché, ale málo efektivní.
- **Klouzavé okénko (Sliding Window)** — odešle se **více paketů najednou bez
  potvrzení** (velikost okna); po potvrzení nejnižšího se okno posune. Efektivnější
  + umožňuje řízení toku úpravou velikosti okna.
- **Fast Retransmit** — dostane-li vysílač **3× stejné ACK** (duplicate ACK),
  předpokládá ztrátu následujícího paketu a vyšle ho **ihned** (nečeká na timeout).

---

## 4. Zahlcení (řízení toku × congestion control)

Rozlišují se **dva** problémy:

| | **Zahlcení přijímače** (flow control) | **Zahlcení linky** (congestion control) |
|---|---|---|
| chrání | příjemce | síť (linku) na cestě |
| řídí | **přijímač** velikostí okna (DO) | **vysílač** (CWL) |
| varianta TCP | stejné pro všechny | **liší se** dle varianty |

- **Délka okna (DO)** = počet paketů poslaných bez potvrzení; **navrhuje přijímač**
  (0 = úplné zastavení) podle svých možností.
- **CWL (Congestion Window Length)** = kolik paketů smí vysílač poslat, aby
  nezahltil linku; určuje si ho **vysílač**. Reálně se posílá
  $\min(\text{DO}, \text{CWL})$.
- **Fáze CWL (TCP Tahoe):** (1) **Slow Start** — CWL = 1, při úspěchu **2× růst**
  (exponenciálně) do prahu **ssthresh**; (2) **Congestion Avoidance** — lineární
  růst do výpadku (timeout); (3) po výpadku **ssthresh na polovinu**, CWL = 1, zpět
  na (1). Princip AIMD.
- **TCP Reno** je optimističtější: po výpadku spadne CWL jen na **polovinu**
  (ne na 1) → rychlejší obnova při krátkodobé poruše. Další varianty: New Reno,
  Vegas, CUBIC, …

---

## 5. Srovnání s protokolem UDP

![[UDP#Definice]]

**UDP hlavička:** zdrojový port, cílový port, délka dat, kontrolní součet
(+ pseudohlavička z IP pro výpočet checksumu).

| | **TCP** | **UDP** |
|---|---|---|
| spolehlivost | spolehlivý (ACK, retransmise) | nespolehlivý |
| spojení | spojově orientovaný (handshake) | nespojový (paketově orient.) |
| pořadí / duplikáty | garantuje pořadí, detekuje duplikáty | negarantuje |
| řízení toku / zahlcení | ano (okno, CWL) | ne |
| režie / rychlost | vyšší režie | nízká režie → vyšší propustnost |
| typické použití | spolehlivý přenos (web, soubory) | hlas, video, jednoduché dotazy (DNS) |

---

## 6. Překlad síťových adres (NAT)

![[NAT#Definice]]

### NAT na síťové vrstvě

Směrovač při průchodu paketu do vnější sítě **nahradí zdrojovou (privátní) IP
adresu adresou svého vnějšího (veřejného) rozhraní**. Privátní rozsahy
(`10/8`, `172.16/12`, `192.168/16`) nejsou v Internetu směrovatelné, proto se
„vydávají" za jedinou veřejnou adresu. Mapování drží **NAT tabulka** (konfigurace
administrátorem). *Motivace:* nedostatek veřejných IPv4 adres.

### NAT na transportní vrstvě (PAT / NAPT)

Aby jednu veřejnou adresu mohlo sdílet **více stanic se současnými spojeními ke
stejnému cíli**, překládá se **IP adresa i [[TCP|port]]**. Každé spojení je
identifikováno dvojicí `{vnitřní IP, vnitřní port}`, kterou směrovač namapuje na
`{vnější IP, vnější port}`. Odpověď přicházející na `{vnější IP, vnější port}` se
přeloží zpět.

*Příklad:* PC1 `192.168.0.1:1111` → `147.231.232.254:5555`,
PC2 `192.168.0.2:2222` → `147.231.232.254:5556` (oba k cíli `…:443`). Díky
různým **portům** směrovač rozliší, komu patří vracející se odpovědi.

> V IPv6 NAT zpravidla netřeba; **NAT64** překládá mezi IPv6 a IPv4.

---

## 7. Systém doménových jmen (DNS)

![[DNS#Definice]]

### Architektura a struktura

- **Doménové jméno** = posloupnost jmen od listu ke kořeni (`mail.fit.cvut.cz`),
  tvoří **strom** (kořen `.` → TLD → …). **FQDN** ≤ 255 znaků, jedna úroveň ≤ 63
  znaků, **není case-sensitive**.
- **TLD** (1. úroveň): **gTLD** (`com`, `org`, …), **ccTLD** (`cz`, `de`, …),
  **ngTLD** (libovolný řetězec, od 2013), reverzní `in-addr.arpa`. CZ spravuje
  **CZ.NIC**.
- **Kořenové servery:** **13 skupin (A–M)**, reálně stovky serverů, dotazy přes
  **anycast** (IPv6 nativně, IPv4 přes BGP).
- **Resolver** = překládá jména pro klienta; **autoritativní server** = spravuje
  záznamy **zóny** (reálná implementace domény — soubor/DB). Správu subzóny lze
  **delegovat**.

### Záznamy (RR) a zóna

Zóna = **úvodní záznam SOA** + doménové záznamy. **DZ = {jméno, TTL, třída, typ,
hodnota}** (třída obvykle **IN**; TTL = doba cachování, chybí-li → MINIMUM ze SOA).

| Typ | význam |
|---|---|
| A / AAAA | IPv4 / IPv6 adresa |
| NS | autoritativní DNS server domény |
| MX | poštovní server |
| CNAME | alias (kanonické jméno) |
| PTR | reverzní záznam (IP → jméno) |
| SOA / TXT / SRV / RRSIG | úvodní / text / služby / podpis (DNSSEC) |

### Překlad jmen

- Historicky soubor `hosts.txt` (dnes `/etc/hosts`); resolver dle `/etc/resolv.conf`.
- **Iterativní** dotazování: server se postupně **ptá každé úrovně sám** (kořen →
  TLD → autoritativní), v každém kroku dostane odkaz o úroveň níž.
- **Rekurzivní** dotazování: dotaz **putuje řetězově dolů** přes servery a odpověď
  se vrací zpět toutéž cestou.
- **Reverzní dotaz** (IP → jméno): pro `AA.BB.CC.DD` se dotáže na
  `DD.CC.BB.AA.in-addr.arpa` (oktety pozpátku), typ **PTR**.

### Protokol, bezpečnost, další funkce

- **Port 53**, většina implementací **UDP**; hlavička 12 B, dotaz má 16b **ID**.
- **Cache poisoning:** útočník podvrhne odpověď se stejným 16b ID dřív než
  autoritativní server → otrávení keše. **Obrana = DNSSEC** — odpovědi podepsány
  **[[Asymetrická-šifra|asymetrickou kryptografií]]** (řetěz důvěry přes nadřazené
  zóny, [[Digitální-podpis|podpis]] ověřitelný veřejným klíčem z RRSIG).
- **Další funkce:** **rozdělování zátěže** (load balancing — autoritativní server
  vrací při opakovaných dotazech různé IP), omezení přístupu, **DynDNS** (změna A
  záznamů za běhu).

---

## Co je potřeba na zkoušku znát

### Definice
Transportní vrstva (port = 16 b, segment), spolehlivé × nespolehlivé doručení,
TCP, UDP, klouzavé okno, flow control × congestion control, NAT / PAT, DNS
(doména, zóna, RR, resolver, autoritativní server).

### Mechanismy a postupy
- **TCP handshake** (SYN / SYN-ACK / ACK), ukončení 2× FIN/ACK; sekvenční a ACK
  čísla.
- **Spolehlivost:** Stop&Wait, klouzavé okno, fast retransmit (3× duplicate ACK),
  timeout + retransmise; problémy ztráta/duplikace.
- **Zahlcení:** DO navrhuje přijímač (flow control), CWL určuje vysílač
  (congestion control); Slow Start → Congestion Avoidance → po výpadku ssthresh/2
  (Tahoe = CWL na 1, Reno na polovinu); odesílá se min(DO, CWL).
- **TCP vs UDP** — umět srovnávací tabulku a kdy co použít.
- **NAT:** síťová vrstva = překlad IP; transportní vrstva = **PAT** (IP + port),
  mapování `{vnitřní IP:port} ↔ {vnější IP:port}` umožní sdílení 1 veřejné adresy.
- **DNS:** port 53/UDP, iterativní × rekurzivní překlad, reverzní (in-addr.arpa,
  PTR), typy záznamů (A/AAAA/NS/MX/CNAME/PTR), DNSSEC proti cache poisoningu.
