---
aliases: [ukazatel, ukazatele, ukazateli, ukazatelem, ukazatelů, ukazatelům, ukazatelích, pointer, pointeru, pointery]
tags: [definice, kurz/PA1]
---

# Ukazatel

## Definice
**Ukazatel** je abstrakce adresy v paměti. Hodnota ukazatele na typ `T` je adresa, na níž je uložena hodnota typu `T`; deklarace `T * p`.

- **Reference (`&x`)** — operátor *odkazu*; vrací adresu proměnné `x` (typu `T*`).
- **Dereference (`*p`)** — přístup k hodnotě, na kterou `p` ukazuje.
- **Null ukazatel** (`nullptr`) — adresa, která nic nereferencuje; její dereference vede k pádu programu.

## Aritmetika ukazatelů
`T* + int → T*` (posun o $n \cdot \texttt{sizeof}(T)$ bajtů), `T* - T* → int` (počet prvků mezi nimi), porovnání. Pole se implicitně konvertuje na konstantní ukazatel na svůj nultý prvek, proto `a[i] == *(a+i)`.

## Použití
- **Dynamicky alokovaná paměť** — anonymní blok na haldě (`malloc`) je dostupný jen přes ukazatel.
- **Výstupní parametry** — v C se simulují předáním adresy (`T*`), do níž funkce zapíše výsledek.
- **[[Spojový-seznam|Spojové struktury]]** — uzly propojené ukazateli na následníka.

## Související
- [[Spojový-seznam]]
- [[Datový-typ]]
