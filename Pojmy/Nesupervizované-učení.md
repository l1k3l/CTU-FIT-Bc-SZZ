---
aliases: [nesupervizované učení, nesupervizovaného učení, nesupervizovanému učení, nesupervizovaným učením, nesupervizovaném učení, učení bez učitele, unsupervised learning]
tags: [definice, kurz/ML1]
---

# Nesupervizované učení

## Definice

**Nesupervizované učení** (učení bez učitele, angl. *unsupervised learning*) je strojové učení z dat **bez označení** — bez vysvětlované (cílové) proměnné. Cílem je porozumět vnitřní struktuře dat pouze na základě dat samotných: data chápeme jako realizace [[Náhodný-vektor|náhodného vektoru]] $X = (X_1,\dots,X_p)^T$ a hledáme rozdělení / hustotu pravděpodobnosti $f_X$, resp. oblasti, kde se data vyskytují nejčastěji.

## Hlavní úlohy

- **Shlukování** (clustering) — viz [[Shluková-analýza]];
- **redukce dimenzionality** (PCA apod.);
- **odhad hustoty** pravděpodobnosti.

## Vlastnosti

Charakteristickým problémem nesupervizovaného učení je, že **není jednoznačné kritérium** pro vyhodnocení úspěšnosti naučeného modelu (na rozdíl od supervizovaného učení, kde existuje cílová proměnná a např. přesnost klasifikace).

## Související

- [[Shluková-analýza]]
- [[Náhodný-vektor]]
