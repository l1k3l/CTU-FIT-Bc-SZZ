---
aliases: [IP adresa, IP adresy, IP adrese, IP adresu, IP adresou, IP adres, IP adresám, IP adresách, IPv4 adresa, IPv4 adresy, síťová adresa, logická adresa]
tags: [definice, kurz/PSI]
---

# IP adresa

## Definice

**IP adresa** je logický identifikátor síťového rozhraní (NIC) na **síťové
vrstvě**. Na rozdíl od [[MAC-adresa|linkové adresy]] je **hierarchická** —
adresy lze sdružovat do sítí (podsítí) a směrovat mezi nimi.

**IPv4:** 32 bitů, zápis po oktetech `X.X.X.X` (každý 0–255).
**IPv6:** 128 bitů, 8×16 bitů hexadecimálně oddělených `:` (viz dále).

## Sítě, maska, prefix (IPv4)

- **Maska sítě** (32 b) = zleva souvislá řada jedniček délky **prefixu**, zbytek nuly.
  Říká, kolik bitů adresy mají stanice v téže síti společných.
- **Adresa sítě** = nejnižší adresa rozsahu = `IP AND maska` (používá se pro směrování).
- **Broadcast** = nejvyšší adresa rozsahu.
- **Brána** = implicitní [[Směrovač|směrovač]] (typicky druhá nejvyšší/nejnižší adresa).
- Počet využitelných adres = $2^N - 2$ (resp. $-3$ s bránou), $N$ = počet host-bitů.

## Speciální rozsahy IPv4

- Privátní (jen lokálně): `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
- Link-local `169.254.0.0/16`, loopback `127.0.0.0/8`, multicast `224.0.0.0/4`.
- Třídy A–E (zastaralé): A `0–127`, B `128–191`, C `192–223` (unicast),
  D `224–239` (multicast), E `240–255` (rezervováno).

## Související
- [[MAC-adresa]], [[Směrování]], [[Směrovač]], [[NAT]]
- [[ISO-OSI-model]]
