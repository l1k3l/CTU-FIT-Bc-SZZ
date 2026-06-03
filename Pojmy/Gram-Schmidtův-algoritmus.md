---
aliases: [gram-schmidtův algoritmus, gram-schmidtova ortogonalizace, gramova-schmidtova ortogonalizace, ortogonalizace, gram-schmidt, gramův-schmidtův proces]
tags: [definice, kurz/LA2]
---

# Gram-Schmidtův algoritmus

## Definice

**Gramova–Schmidtova ortogonalizace** je postup, který z lineárně nezávislého souboru vektorů $(x_1, \dots, x_n)$ v prehilbertově prostoru se [[Skalární-součin|skalárním součinem]] vyrobí **[[Ortogonální-báze|ortogonální (OG) bázi]]** $(z_1, \dots, z_n)$, případně po normalizaci **ortonormální (ON) bázi** $(y_1, \dots, y_n)$ téhož prostoru.

**Myšlenka:** od každého dalšího vektoru odečteme jeho projekce do již vytvořených (kolmých) směrů — zbude složka kolmá na ně, a lineární obal se zachová.

**Vzorec (OG):**
$$z_1 = x_1, \qquad z_k = x_k - \sum_{i=1}^{k-1} \frac{\langle z_i \mid x_k \rangle}{\langle z_i \mid z_i \rangle}\, z_i = x_k - \sum_{i=1}^{k-1} \operatorname{proj}_{z_i}(x_k).$$

**Normalizace na ON bázi:**
$$y_i = \frac{1}{\|z_i\|}\, z_i.$$

## Vlastnosti

- Soubor $(z_1, \dots, z_k)$ je OG soubor nenulových vektorů pro každé $k$.
- **Zachování obalů:** $\langle x_1, \dots, x_k \rangle = \langle z_1, \dots, z_k \rangle$ pro každé $k \in \hat{n}$.
- **Důsledek:** každý konečnědimenzionální prehilbertův (pod)prostor dimenze $\ge 1$ má ON bázi.

## Použití v LA2

Praktická metoda výpočtu ON báze; tvoří základ **[[QR-rozklad|QR rozkladu]]** matice (sloupce $Q$ jsou ON báze získaná z původních sloupců).

## Související

- [[Ortogonální-báze]]
- [[Skalární-součin]]
- [[QR-rozklad]]
