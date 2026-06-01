---
tags: [otázka, kurz/PSI, otázka/25, hotovo]
---

# 25 — Transportní vrstva (TCP/UDP), NAT, DNS (zkrácená verze)

## 1. Transportní vrstva
Doručuje data **konkrétní aplikaci (procesu)** dle **portu** (16 b). Jednotka =
**segment**. Adresace `[IP, port] → [IP, port]`. Porty < 1024 privilegované, jinak
dynamické. Doručení **spolehlivé** (TCP) × **nespolehlivé** (UDP).
Parametry: ztrátovost, zpoždění, **RTT** (≈2× delay), **jitter**.
Problémy: ztráta paketu / ztráta nebo zpoždění ACK (→ duplikace) → řeší **timeout +
opakování + ACK**. Spolehlivé zahájení = **3-way handshake** (perfektní řešení
neexistuje — problém dvou armád).

## 2. Protokol TCP ([[TCP]])
Spolehlivý, **spojově orientovaný**, duplexní, garantuje pořadí, detekuje duplikáty.
**Hlavička:** zdroj/cíl port, **seq** odesílané, **seq očekávané (ACK)**, příznaky
**U A P R S F**, délka okna, checksum.
**Spojení:** `SYN(x)` → `SYN,ACK(y, x+1)` → `ACK(y+1)`; ukončení 2× FIN/ACK.

## 3. Spolehlivost doručení
- **Stop & Wait** — 1 paket, čekej na ACK, timeout → opakuj.
- **Klouzavé okno** — víc paketů bez potvrzení, okno se posouvá po ACK.
- **Fast Retransmit** — 3× stejné ACK → ihned přeposli ztracený paket.

## 4. Zahlcení
- **Flow control** (zahlcení **přijímače**): **délku okna (DO)** navrhuje
  **přijímač** (0 = stop). Stejné pro všechny varianty TCP.
- **Congestion control** (zahlcení **linky**): **CWL** určuje **vysílač**.
  Liší se dle varianty TCP. Posílá se **min(DO, CWL)**.
- Fáze: **Slow Start** (CWL=1, ×2) → práh **ssthresh** → **Congestion Avoidance**
  (lineárně) → výpadek → ssthresh/2. **Tahoe**: CWL→1; **Reno**: CWL→polovina.

## 5. Srovnání TCP × UDP ([[UDP]])
UDP hlavička: zdroj/cíl port, délka, checksum.

| | TCP | UDP |
|---|---|---|
| spolehlivost | ano | ne |
| spojení | ano (handshake) | ne |
| pořadí/duplikáty | garantuje | ne |
| řízení toku/zahlcení | ano | ne |
| režie/rychlost | vyšší / pomalejší | nízká / rychlejší |
| použití | web, soubory | hlas, video, DNS |

## 6. NAT ([[NAT]]) — síťová a transportní vrstva
**Síťová:** směrovač nahradí **zdrojovou privátní IP** adresou svého **vnějšího
(veřejného) rozhraní** (privátní 10/8, 172.16/12, 192.168/16 nejsou směrovatelné).
NAT tabulka. Důvod: nedostatek IPv4 adres.
**Transportní (PAT/NAPT):** překládá **IP + port** → více stanic sdílí 1 veřejnou
IP. Mapování `{vnitřní IP:port} ↔ {vnější IP:port}`; podle portu se rozliší
vracející se spojení. (IPv6 NAT netřeba; **NAT64** IPv6↔IPv4.)

## 7. DNS ([[DNS]])
Hierarchický překlad **jméno ↔ IP**, **port 53, většinou UDP**.
**Jméno** = od listu ke kořeni (strom: `.` → TLD → …); FQDN ≤ 255, úroveň ≤ 63,
ne case-sensitive. TLD: gTLD/ccTLD/ngTLD; CZ = CZ.NIC. **13 skupin** kořenových
serverů (anycast).
**Resolver** (pro klienta) × **autoritativní** (spravuje **zónu**). DZ = {jméno,
TTL, třída IN, typ, hodnota}.
**RR:** A/AAAA, NS, MX, CNAME (alias), PTR (reverzní), SOA, RRSIG.
**Překlad:** iterativní (server se ptá každé úrovně sám) × rekurzivní (dotaz putuje
řetězově dolů). **Reverzní:** `DD.CC.BB.AA.in-addr.arpa`, typ PTR.
**Bezpečnost:** cache poisoning (podvržené ID); obrana **DNSSEC** ([[Asymetrická-šifra|asym. kryptografie]],
podpis přes nadřazené zóny). Další: load balancing, DynDNS.

---
## Co odpovědět rychle
- **Port = 16 b**; transportní vrstva doručuje aplikaci.
- **TCP** = spolehlivý + handshake (SYN/SYN-ACK/ACK), seq/ACK, klouzavé okno;
  **UDP** = nespolehlivý, nízká režie.
- **Spolehlivost:** ACK + timeout + retransmise, fast retransmit (3× ACK).
- **Zahlcení:** přijímač = okno (flow), vysílač = CWL (congestion), Slow Start +
  Congestion Avoidance.
- **NAT** = privátní → veřejná IP; **PAT** = IP+port (sdílení 1 IP).
- **DNS** = jméno↔IP, port 53 UDP, iterativní/rekurzivní, PTR reverzně, DNSSEC.
