---
aliases: [NAT, NATu, překlad adres, překlad síťových adres, Network Address Translation, PAT, NAPT, maškaráda, masquerade]
tags: [definice, kurz/PSI]
---

# NAT

## Definice

**NAT** (Network Address Translation, překlad adres) je proces, při kterém
[[Směrovač|směrovač]] při průchodu paketu vnějším rozhraním **nahrazuje
zdrojovou [[IP-adresa|IP adresu]]** (privátní, nesměrovatelnou v Internetu)
adresou **svého vnějšího rozhraní** (veřejnou). Záznamy drží **NAT tabulka**.

**Motivace:** veřejných IPv4 adres není dostatek; mnoho stanic s privátními
adresami sdílí jedinou veřejnou adresu.

## Na síťové vs. transportní vrstvě

- **NAT (síťová vrstva)** — překládá pouze IP adresu.
- **PAT / NAPT (transportní vrstva)** — překládá IP adresu **i [[TCP|port]]**.
  Díky portu lze rozlišit více současných spojení jdoucích od různých stanic ke
  stejnému cíli přes jednu veřejnou adresu. Mapování:
  `{vnitřní IP, vnitřní port} ↔ {vnější IP, vnější port}`. Odpověď přicházející
  na `{vnější IP, vnější port}` směrovač přeloží zpět.
- IPv6 NAT zpravidla nepotřebuje (adres je dostatek); **NAT64** překládá mezi
  IPv6 a IPv4.

## Související
- [[IP-adresa]], [[Směrovač]], [[TCP]], [[UDP]]
