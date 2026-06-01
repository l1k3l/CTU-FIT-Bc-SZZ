---
aliases: [VLAN, VLANy, VLANu, VLANů, virtuální síť, virtuální sítě, virtuálních sítí, 802.1Q, značkování, tagování]
tags: [definice, kurz/PSI]
---

# VLAN

## Definice

**VLAN** (Virtual Local Area Network) je technika umožňující existenci **více
virtuálních sítí uvnitř jedné fyzické sítě**. Odděluje toky na **linkové vrstvě**
(důvody: přehlednost, bezpečnost, efektivita, jednoduchost správy).

## Druhy a značkování

- Členství lze přiřadit **dle portů**, **dle MAC adres**, **dle protokolu** nebo
  **dle značky** (tag-based, dnes nejběžnější), případně vícenásobně (Q-in-Q).
- **IEEE 802.1Q** vkládá do Ethernet rámce **4bajtovou značku** za MAC adresy:
  TPID (2 B) + TCI (2 B = PCP 3 b + CFI 1 b + **VID 12 b** → $2^{12}=4096$ VLAN).
- **Trunk port** přenáší více VLAN (rámce značené); **access port** vede k
  stanici (značka se při odchodu odebírá, při příchodu navrací).
- Provoz mezi VLAN nelze přepínat — musí se **směrovat** přes [[Směrovač|směrovač]].

## Související
- [[Přepínač]], [[MAC-adresa]], [[Směrovač]]
