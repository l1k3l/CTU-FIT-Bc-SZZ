---
aliases: [uváznutí, uváznutím, deadlock, deadlocku, deadlocky]
tags: [definice, kurz/OSY]
---

# Uváznutí (deadlock)

## Definice
**Uváznutí** (*deadlock*) je situace, kdy několik **[[Vlákno|vláken]]** čeká na
událost/prostředek, kterou může vyvolat/uvolnit **pouze jedno z čekajících
vláken** — žádné z nich proto nemůže pokračovat. V alokačním grafu (orientovaný
graf vláken a prostředků) odpovídá uváznutí **smyčce (cyklu)**.

## Coffmanovy podmínky
Uváznutí může nastat **právě tehdy, jsou-li současně splněny** všechny čtyři
Coffmanovy podmínky:

1. **Vzájemné vyloučení** — prostředek je přidělen právě jednomu vláknu, nebo je
   volný (nelze ho sdílet).
2. **Neodnímatelnost** — přidělený prostředek nelze vláknu násilím odebrat (musí
   ho uvolnit dobrovolně).
3. **Drž a čekej** (*hold and wait*) — vlákno držící nějaké prostředky může žádat
   o další.
4. **Kruhové čekání** — existuje smyčka vláken, kde každé čeká na prostředek
   držený dalším vláknem ve smyčce.

První tři podmínky jsou nutné, ale ne dostačující; čtvrtá představuje samotné
uváznutí. **Nesplnění aspoň jedné** podmínky ⇒ uváznutí nemůže nastat.

## Strategie řešení
- **Pštrosí strategie** — problém se ignoruje (řeší zásah uživatele/administrátora).
- **Prevence** — porušení aspoň jedné Coffmanovy podmínky.
- **Předcházení** — opatrná alokace na základě znalosti budoucích požadavků
  (bezpečný stav, *bankéřův algoritmus*).
- **Detekce a zotavení** — uváznutí se připustí, pravidelně detekuje a odstraní.

## Související
- [[Souběh]]
- [[Vlákno]]
- [[Zámek]]
