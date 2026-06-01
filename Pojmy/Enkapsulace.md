---
aliases: [enkapsulace, enkapsulaci, enkapsulací, dekapsulace, dekapsulaci, dekapsulací, PDU, protokolová datová jednotka]
tags: [definice, kurz/PSI]
---

# Enkapsulace

## Definice

**Enkapsulace** je postupné zapouzdřování dat při sestupu vrstvami
[[ISO-OSI-model|ISO/OSI modelu]]: každá vrstva přidá k převzaté PDU svou
**hlavičku** (Layer Header). **Dekapsulace** je opačný proces na straně příjemce
— každá vrstva svou hlavičku odebere při výstupu vzhůru.

- **PDU (Protocol Data Unit)** = hlavička + obsah (přebraná PDU vyšší vrstvy).
- Postup (vysílač, shora dolů): $\text{PDU}_7 = \text{ALH} + \text{DATA}$;
  $\text{PDU}_6 = \text{PLH} + \text{PDU}_7$; … až na fyzické vrstvě se přenášejí bity.
- Na linkové vrstvě se kromě hlavičky přidává i **zápatí/trailer** (např. FCS).

## Související
- [[ISO-OSI-model]]
- Pozor: nezaměňovat s OOP pojmem [[Zapouzdření]] (skrývání vnitřního stavu objektu).
