---
aliases: [přepínač, přepínače, přepínači, přepínačem, přepínačů, přepínačům, switch, switche, most, mosty, bridge, přepínání]
tags: [definice, kurz/PSI]
---

# Přepínač

## Definice

**Přepínač (switch)** je zařízení **linkové vrstvy**, které **přepíná rámce** —
přijatý rámec zpracuje a odešle výstupním portem k příjemci podle jeho
[[MAC-adresa|MAC adresy]]. Výstupní port volí podle **přepínací tabulky**.

## Princip přepínání

- **Přepínací tabulka** mapuje MAC adresu → port; plní se **učením**: rámec s
  neznámou cílovou adresou se rozešle na všechny porty kromě příchozího
  (flooding) a podle zdrojové adresy odpovědi se zaznamená port.
- Režimy: **Store-and-Forward** (přijme celý rámec, pak odešle),
  **Cut-Through** (čte jen cílovou adresu ~6 B a hned odesílá),
  **Fragment-Free** (čte celou hlavičku ~64 B).
- **Most (bridge)** funguje obdobně, má jen 2–4 porty a nemá buffery.
- Přepínač **odděluje kolizní domény**; **broadcastovou doménu** oddělí až
  [[Směrovač|směrovač]] (síťová vrstva).
- Smyčky v topologii řeší **Spanning Tree Protocol** (vytvoří [[Kostra|kostru]]
  topologie reprezentované [[Graf|grafem]] pomocí zaplavování).

## Související
- [[MAC-adresa]], [[Směrovač]], [[VLAN]]
- [[Kostra]], [[Graf]]
