---
aliases: [MAC adresa, MAC adresy, MAC adrese, MAC adresu, MAC adresou, MAC adres, MAC adresám, linková adresa, linkové adresy, fyzická adresa, hardwarová adresa]
tags: [definice, kurz/PSI]
---

# MAC adresa

## Definice

**MAC adresa** (Media Access Control) je **linková (fyzická) adresa** definovaná
v MAC podvrstvě linkové vrstvy. Je **hardwarově závislá** a slouží k doručování
[[Enkapsulace|rámců]] **v lokální síti**.

- Velikost **48 bitů (6 bajtů)** — „MAC-48".
- První 3 bajty = **OUI** (Organization Unique Identifier, výrobce);
  poslední 3 bajty = sériové číslo zařízení.
- **Broadcastová MAC** = `FF:FF:FF:FF:FF:FF`.
- Na rozdíl od [[IP-adresa|IP adresy]] **není hierarchická** → použitelná jen
  pro doručování v rámci jedné lokální sítě (mapování IP→MAC zajišťuje ARP, resp.
  v IPv6 objevování sousedů).

## Související
- [[IP-adresa]], [[Přepínač]]
- [[ISO-OSI-model]]
