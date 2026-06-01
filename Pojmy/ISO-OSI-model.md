---
aliases: [ISO/OSI, ISO/OSI model, ISO/OSI modelu, OSI model, OSI modelu, OSI, RM-OSI, referenční model OSI, vrstvový model]
tags: [definice, kurz/PSI]
---

# ISO/OSI model

## Definice

**Referenční model ISO/OSI** (Open Systems Interconnection) je vrstvový model
síťové komunikace se **7 hierarchickými, funkčně disjunktními vrstvami**, které
spolu spolupracují. Každá vrstva má specifickou funkci a vlastní **datovou
jednotku (PDU)**. Oddělení vrstev umožňuje jejich nezávislý vývoj a implementaci.

| # | Vrstva (CZ / EN) | Datová jednotka | Funkce |
|---|---|---|---|
| 7 | Aplikační / Application | Data | síťový proces aplikací |
| 6 | Prezentační / Presentation | Data | prezentace dat a šifrování |
| 5 | Relační / Session | Data | komunikace mezi hostiteli |
| 4 | Transportní / Transport | **Segmenty** | end-to-end spojení a spolehlivost |
| 3 | Síťová / Network | **Pakety** | určování cesty a IP (logické adresování) |
| 2 | Linková / Data Link | **Rámce** | MAC a LLC (fyzické adresování) |
| 1 | Fyzická / Physical | **Bity** | médium, signál, binární přenos |

- **Vrstvy hostitelů** = 4–7; **vrstvy média** = 1–3.
- Komunikace mezi dvěma stanicemi probíhá vždy **na úrovni stejných vrstev**.
- Posun PDU mezi vrstvami zajišťuje [[Enkapsulace]].

## TCP/IP model

Praktický **4vrstvý model TCP/IP**: Application (= OSI 7+6+5), Transport (= OSI 4),
Internet (= OSI 3), Network Interface (= OSI 2+1).

## Související
- [[Enkapsulace]]
- [[IP-adresa]], [[MAC-adresa]]
- [[Přepínač]], [[Směrovač]]
