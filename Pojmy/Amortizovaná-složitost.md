---
aliases: [amortizovaná složitost, amortizované složitosti, amortizovanou složitost, amortizovaná analýza, amortizované analýzy]
tags: [definice, kurz/AG1]
---

# Amortizovaná složitost

## Definice
Operace $A$ nad dynamickou datovou strukturou má v daném **kontextu** svého provádění **amortizovanou časovou složitost** $O(f(n))$ (značíme $O^*(f(n))$), pokud posloupnost $k$ operací $A$ má celkovou složitost $O(k \cdot f(n))$. Parametr $n$ je velikost dynamické struktury **po provedení** této posloupnosti.

- Pro odhad složitosti jednotlivých provedení se bere **nejhorší případ**.
- Amortizovaná složitost musí být stanovována přes **dostatečně dlouhou** posloupnost operací.
- Konkrétní jedno volání operace v nejhorším případě může být **řádově dražší**.

## Příklady
- **[[Nafukovací-pole]]:** `NPInsert` má amortizovanou složitost $\Theta^*(1)$, ačkoli občasné zdvojnásobení trvá $\Theta(n)$.
- **[[Binární-sčítačka]]:** `Inc` má amortizovanou složitost $O^*(1)$ (bankéřova metoda: každé jedničce v zápisu náleží jedna „naspořená" mince).
- **[[Binomiální-halda|BHInsert]]:** amortizovaně $\Theta^*(1)$ (přes analogii s binární sčítačkou).

## Metody analýzy
- **Agregační:** spočti celkový čas, vyděl počtem operací.
- **Bankéřova (účetní):** každé operaci přiřaď „virtuální kredit", drahé operace platí z kreditu nashromážděného levnými.
- **Potenciálová:** definuj potenciálovou funkci $\Phi$ stavu struktury; amortizovaná složitost = skutečná složitost + $\Delta\Phi$.

## Související
- [[Nafukovací-pole]]
- [[Binární-sčítačka]]
- [[Binomiální-halda]]
