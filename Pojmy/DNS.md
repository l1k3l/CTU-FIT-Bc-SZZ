---
aliases: [DNS, Domain Name System, doménové jméno, doménová jména, doménových jmen, DNS server, jmenný systém, DNSSEC]
tags: [definice, kurz/PSI]
---

# DNS

## Definice

**DNS** (Domain Name System) je hierarchický, distribuovaný systém pro **překlad
doménových jmen na [[IP-adresa|IP adresy]] a naopak** (reverzně). Běží na
**portu 53**, většina implementací používá [[UDP]].

## Struktura a překlad

- **Doménové jméno** = posloupnost jmen od listu ke kořeni (`mail.fit.cvut.cz`);
  tvoří **strom** (kořen `.`, TLD, …). FQDN ≤ 255 znaků, jedna úroveň ≤ 63 znaků,
  není case-sensitive.
- **Autoritativní server** spravuje záznamy **zóny**; **resolver** překládá pro
  klienta. **13 skupin** kořenových serverů (A–M), dotazovány přes anycast.
- **Typy záznamů (RR):** A (IPv4), AAAA (IPv6), NS, MX (pošta), CNAME (alias),
  PTR (reverzní, `in-addr.arpa`), SOA (úvodní), TXT, SRV, RRSIG (DNSSEC).
- **Dotazování:** iterativní (server se postupně ptá každé úrovně sám) vs.
  rekurzivní (dotaz putuje řetězově dolů, odpověď se vrací zpět).
- **DNSSEC** = zabezpečené rozšíření — odpovědi podepsány [[Asymetrická-šifra|asymetrickou kryptografií]]
  (řetěz důvěry přes nadřazené zóny); brání podvržení odpovědi (cache poisoning).

## Související
- [[IP-adresa]], [[UDP]], [[TCP]]
- [[Asymetrická-šifra]], [[Digitální-podpis]]
