---
aliases: [Gaussova eliminace, Gaussovy eliminace, Gaussovu eliminaci, Gaussově eliminaci, Gaussova eliminační metoda, Gaussovy eliminační metody, GEM, eliminační metoda, Gaussova-Jordanova eliminace, horní stupňovitý tvar, HST, redukovaný horní stupňovitý tvar, rHST]
tags: [algoritmus, kurz/LA1]
---

# Gaussova eliminace

## Definice

**Gaussova eliminační metoda (GEM)** převádí matici konečnou posloupností **elementárních řádkových úprav** na [[#Horní stupňovitý tvar (HST)|horní stupňovitý tvar]]. Úpravy:

- **(G1)** prohození dvou řádků;
- **(G2)** vynásobení řádku nenulovým $\alpha \in T \setminus \{0\}$;
- **(G3)** přičtení libovolného násobku jednoho řádku k jinému.

Píšeme $A \sim B$, lze-li $A$ převést na $B$ úpravami GEM. Každý krok je **vratný**.

**Klíčové vlastnosti:** elementární úpravy nemění
- množinu řešení soustavy (úpravy odpovídají ekvivalentním úpravám rovnic),
- lineární obal řádků, a tedy ani [[Hodnost-matice|hodnost]] matice.

## Horní stupňovitý tvar (HST)

Matice je v **HST**, jsou-li nulové řádky až dole a index prvního nenulového prvku (**pivotu**) každého řádku striktně roste shora dolů: $j_1 < j_2 < \cdots < j_k$. Sloupce s pivotem = **hlavní (bázové)**, ostatní = **vedlejší (volné)**. Hodnost matice v HST = počet nenulových řádků = počet pivotů.

## Algoritmus

Postupně zleva: najdi nenulový sloupec, prohozením řádků (G1) dej do aktuálního řádku nenulový pivot, pak úpravami (G3) vynuluj prvky **pod** pivotem; vynech zpracovaný řádek/sloupec a opakuj. Po skončení je matice v HST. **Složitost** $O(\min(m,n) \cdot mn)$ ($O(n^3)$ pro čtvercovou).

**Gaussova–Jordanova eliminace** pokračuje za HST: pivoty se znormují na $1$ a vynulují se i prvky **nad** nimi → **redukovaný HST (rHST)**. Používá se při výpočtu [[Inverzní-matice|inverzní matice]] (převod $(A \mid E) \sim (E \mid A^{-1})$).

## Použití

- řešení [[Soustava-lineárních-rovnic|soustav lineárních rovnic]],
- výpočet [[Hodnost-matice|hodnosti]],
- výpočet [[Inverzní-matice|inverzní matice]] a [[Determinant|determinantu]].

## Související

- [[Soustava-lineárních-rovnic]]
- [[Hodnost-matice]]
- [[Frobeniova-věta]]
- [[Inverzní-matice]]
- [[Matice]]
