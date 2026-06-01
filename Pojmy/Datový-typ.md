---
aliases: [datový typ, datového typu, datovému typu, datovým typem, datové typy, datových typů, datovým typům, typ, typu, typem, typy, data type, datovy typ]
tags: [definice, kurz/PA1]
---

# Datový typ

## Definice
**Datový typ** je vlastnost dat, která určuje:
- **množinu možných hodnot**, jichž může objekt nabývat,
- **množinu dovolených operací** nad těmito hodnotami,
- **kódování** — jak je hodnota uložena v bajtech a kolik místa zabírá.

Procesor pracuje jen s bajty a nezná jejich význam; typ dává bajtům interpretaci. Ve vyšších jazycích má **proměnná** přiřazen typ, který se po dobu její existence obvykle nemění (**statická typovost**).

## Klasifikace (BI-PA1)
- **Primitivní (vestavěné):** celočíselné (`int`, `char`, `short`, `long`, `long long` se znaménkem i bez), reálné (`float`, `double`, `long double`), logický (`bool`), `void`.
- **Odvozené (programátorem definované):** **pole**, **struktura** (`struct`), **[[Ukazatel]]**, `enum`, `union`.

Skalární (jednoduché) typy nesou jednu hodnotu; strukturované (pole, struktury) sdružují více hodnot.

## Poznámky
- Norma C určuje jen **minimální** rozsahy; skutečné velikosti závisí na implementaci (proto `stdint.h`: `int16_t`, … pro garantovanou velikost).
- Reálné typy aproximují $\mathbb{R}$ semilogaritmicky (IEEE 754): $x = (-1)^s \cdot m \cdot b^e$ — omezený rozsah i přesnost.

## Související
- [[Ukazatel]]
- [[Spojový-seznam]]
