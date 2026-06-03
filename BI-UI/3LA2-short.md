---
tags: [otázka, kurz/LA2, otázka/3, todo]
---

# 3 — Ortogonalita a ortogonální báze (zkrácená verze)

Prostředí: prehilbertův prostor $\mathcal{H}$ se [[Skalární-součin|skalárním součinem]] $\langle x \mid y \rangle$, [[Norma]] $\|x\| = \sqrt{\langle x \mid x \rangle}$, $\theta$ nulový vektor.

## 1. Ortogonalita

**Kolmost:** $x \perp y \iff \langle x \mid y \rangle = 0$. (Symetrické; $\theta \perp$ vše.)

**OG soubor** $(x_1,\dots,x_n)$: vzájemně kolmé, $\langle x_i \mid x_j \rangle = 0$ pro $i \neq j$.

**ON soubor:** OG + jednotkové, tj. $\langle x_i \mid x_j \rangle = \delta_{ij}$ ($0$ pro $i\neq j$, $1$ pro $i=j$).

**Ortogonální doplněk:** $W^\perp = \{x \in \mathcal{H} \mid \langle x \mid w \rangle = 0\ \forall w \in W\}$ — podprostor, $\mathcal{H} = W \oplus W^\perp$.

## 2. OG / ON báze

**[[Ortogonální-báze|OG báze]]** podprostoru = báze, která je OG souborem (kolmé nenulové vektory). **ON báze** = navíc jednotkové. Standardní báze $T^n$ je ON.

## 3. Vlastnosti

**Lineární nezávislost:** OG soubor **nenulových** vektorů je LN.
*(Idea: z $\sum \alpha_j x_j = \theta$ je $0 = \langle x_i \mid \sum \alpha_j x_j\rangle = \alpha_i\|x_i\|^2$, a $\|x_i\|\neq 0$, takže $\alpha_i=0$.)*

**Fourierovy koeficienty (souřadnice):**
$$\text{ON báze:}\quad z = \sum_{i=1}^n \langle x_i \mid z\rangle\, x_i, \qquad (z)_\mathcal{X} = (\langle x_1\mid z\rangle,\dots,\langle x_n\mid z\rangle).$$
$$\text{OG báze:}\quad \alpha_i = \frac{\langle x_i \mid z\rangle}{\langle x_i \mid x_i\rangle} = \frac{\langle x_i \mid z\rangle}{\|x_i\|^2}.$$
Geometricky $\frac{\langle x_i\mid z\rangle}{\langle x_i\mid x_i\rangle} x_i = \operatorname{proj}_{x_i}(z)$ (projekce na přímku). Výhoda ON báze: souřadnice = skalární součiny, bez řešení soustavy.

**Pythagorova věta:** $x \perp y \Rightarrow \|x+y\|^2 = \|x\|^2 + \|y\|^2$; obecně pro OG soubor $\|x_1+\dots+x_n\|^2 = \sum_i \|x_i\|^2$.

**Parsevalova rovnost** (ON báze): $\|z\| = \|(z)_\mathcal{X}\|_2$ (norma = 2-norma souřadnic).

## 4. Gram–Schmidtova ortogonalizace

Z LN souboru $(x_1,\dots,x_n)$ vyrobí OG (resp. po normalizaci ON) bázi téhož prostoru: vezmi $z_k = x_k$ a odečti projekce do všech dříve vytvořených směrů $z_1,\dots,z_{k-1}$, takže $z_k$ je kolmé na ně a obal se zachová. Vzorec:
$$z_1 = x_1, \qquad z_k = x_k - \sum_{i=1}^{k-1} \frac{\langle z_i \mid x_k\rangle}{\langle z_i \mid z_i\rangle}\, z_i, \qquad y_i = \frac{z_i}{\|z_i\|}.$$
Platí $\langle x_1,\dots,x_k\rangle = \langle z_1,\dots,z_k\rangle$ pro každé $k$. **Důsledek:** každý konečnědim. prostor má ON bázi.

---

## Co odpovědět rychle

- **Ortogonalita:** $\langle x\mid y\rangle = 0$; OG = kolmé, ON = kolmé + jednotkové ($\langle x_i\mid x_j\rangle=\delta_{ij}$).
- **Vlastnost:** OG soubor nenulových vektorů je LN → je bází svého obalu.
- **Souřadnice vůči ON bázi:** $z = \sum \langle x_i\mid z\rangle x_i$ (Fourierovy koeficienty); vůči OG bázi dělit $\|x_i\|^2$.
- **Pythagoras:** kolmé sčítance → normy se sčítají na druhou. **Parseval:** $\|z\|=\|(z)_\mathcal{X}\|_2$.
- **Gram–Schmidt:** odečti projekce do předchozích směrů → OG; normalizuj → ON; zachová lin. obaly.
