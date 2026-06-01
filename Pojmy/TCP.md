---
aliases: [TCP, Transmission Control Protocol, TCP spojení, port, portu, porty, portů]
tags: [definice, kurz/PSI]
---

# TCP

## Definice

**TCP** (Transmission Control Protocol) je **spolehlivý, spojově orientovaný**
protokol transportní vrstvy. Doručuje data konkrétní aplikaci podle **portu**
(16bitový identifikátor), **garantuje doručení i pořadí**, detekuje duplikáty,
je duplexní. Přenáší se v datech IP paketu.

## Klíčové mechanismy

- **Spojení:** 3cestný handshake (SYN → SYN-ACK → ACK); ukončení dvěma páry
  FIN/ACK. **Sekvenční čísla** (počáteční náhodné) číslují bajty/pakety, **ACK**
  potvrzuje očekávaný paket.
- **Spolehlivost:** potvrzování + timeout + opakované odeslání; **Fast Retransmit**
  po 3× stejném ACK.
- **Řízení toku** (ochrana příjemce): **klouzavé okno** — velikost okna navrhuje
  **příjemce** (0 = stop).
- **Eliminace zahlcení** (ochrana linky): **Congestion Window (CWL)** řídí
  vysílač; Slow Start (exp. růst) → Congestion Avoidance (lin. růst) →
  při ztrátě snížení ssthresh; odesílá se $\min(\text{okno příjemce}, \text{CWL})$.
  Varianty Tahoe, Reno, …

## Související
- [[UDP]], [[NAT]], [[IP-adresa]]
- [[ISO-OSI-model]]
