---
aliases: [směrovač, směrovače, směrovači, směrovačem, směrovačů, směrovačům, router, routeru, routery, brána, gateway]
tags: [definice, kurz/PSI]
---

# Směrovač

## Definice

**Směrovač (router)** je zařízení **síťové vrstvy**, které **přeposílá pakety
mezi různými sítěmi** na základě cílové [[IP-adresa|IP adresy]] v hlavičce
paketu. Adresně patří do **všech sítí, které propojuje**.

- Odchozí rozhraní / další skok volí podle **směrovací tabulky**
  (záznam: cíl, brána, maska, metrika, rozhraní).
- Pozná, zda doručit přímo (cíl je v některé z jeho sítí), nebo přes další
  směrovač. Mezi sousedními směrovači doručuje data **linková vrstva**.
- Při každém průchodu (**hop**) sníží **TTL** paketu o 1 (ochrana proti zacyklení).
- **Odděluje broadcastové domény**; je **bránou** pro stanice ve své podsíti.

## Související
- [[Směrování]], [[IP-adresa]], [[Přepínač]], [[NAT]]
- [[ISO-OSI-model]]
