---
aliases: [ortogonalita, ortogonální, ortonormální, ortogonální báze, ortogonální bázi, ortogonální báze, ortonormální báze, ON báze, OG báze, ortogonální systém, ortogonální doplněk, kolmost, kolmé vektory]
tags: [definice, kurz/LA2]
---

# Ortogonální báze

## Definice

Pracujeme v prehilbertově prostoru $\mathcal{H}$ se [[Skalární-součin|skalárním součinem]] $\langle x \mid y \rangle$ a [[Norma|normou]] $\|x\| = \sqrt{\langle x \mid x \rangle}$.

**Ortogonalita (kolmost):** vektory $x, y$ jsou **ortogonální** (kolmé, $x \perp y$), právě když
$$\langle x \mid y \rangle = 0.$$

**Ortogonální (OG) soubor** $(x_1, \dots, x_n)$: vektory jsou navzájem kolmé, tj. $\langle x_i \mid x_j \rangle = 0$ pro $i \neq j$.

**Ortonormální (ON) soubor:** OG soubor jednotkových vektorů, tj. $\langle x_i \mid x_j \rangle = \delta_{ij}$ ($0$ pro $i \neq j$, $1$ pro $i = j$).

**Ortogonální / ortonormální báze** podprostoru $P$: báze $P$, která je zároveň OG, resp. ON souborem.

**Ortogonální doplněk** podprostoru $W$: $W^\perp = \{ x \in \mathcal{H} \mid \langle x \mid w \rangle = 0 \text{ pro všechna } w \in W \}$; je to podprostor a $\mathcal{H} = W \oplus W^\perp$.

## Vlastnosti

- **Lineární nezávislost:** OG soubor **nenulových** vektorů je lineárně nezávislý (z $\sum_j \alpha_j x_j = \theta$ plyne $\alpha_i \|x_i\|^2 = 0$). Je tedy bází svého lineárního obalu.
- **Fourierovy koeficienty (souřadnice):** vůči ON bázi $\mathcal{X}$ je $z = \sum_i \langle x_i \mid z \rangle\, x_i$, takže $i$-tá souřadnice je $\langle x_i \mid z \rangle$ (bez řešení soustavy). Vůči OG bázi je souřadnice $\alpha_i = \dfrac{\langle x_i \mid z \rangle}{\langle x_i \mid x_i \rangle}$.
- **Pythagorova věta:** pro kolmé $x, y$ platí $\|x + y\|^2 = \|x\|^2 + \|y\|^2$ (obecně pro celý OG soubor).
- **Parsevalova rovnost:** vůči ON bázi je $\|z\| = \|(z)_\mathcal{X}\|_2$.

## Použití v LA2

OG/ON bázi lze z libovolné báze vyrobit [[Gram-Schmidtův-algoritmus|Gram–Schmidtovou ortogonalizací]]; každý konečnědimenzionální prostor proto má ON bázi.

## Související

- [[Skalární-součin]]
- [[Norma]]
- [[Gram-Schmidtův-algoritmus]]
