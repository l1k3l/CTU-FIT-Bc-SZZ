---
aliases: [UDP, User Datagram Protocol, UDP datagram]
tags: [definice, kurz/PSI]
---

# UDP

## Definice

**UDP** (User Datagram Protocol) je **nespolehlivý, nespojový (paketově
orientovaný)** protokol transportní vrstvy. Data se posílají po částech bez
sestavení spojení; **negarantuje doručení ani pořadí**.

- Jednoduchý, **nízká režie → vyšší propustnost** než [[TCP]] (v ideálních podmínkách).
- Hlavička: zdrojový port, cílový port, délka dat, kontrolní součet.
- Vhodný pro přenos hlasu/videa (občasná ztráta nevadí) a jednoduché dotazy
  (např. [[DNS]]).

## Související
- [[TCP]], [[DNS]]
- [[ISO-OSI-model]]
