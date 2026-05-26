---
aliases: [hešovací tabulka, hešovací tabulky, hešovací tabulce, hešovací tabulku, hešovacích tabulek, hashovací tabulka, hashovací tabulky, hashovací tabulku, hash tabulka, rozptylovací tabulka]
tags: [definice, datová-struktura, kurz/AG1]
---

# Hešovací tabulka

## Definice
**Hešovací tabulka** je implementace **[[Slovník|slovníku]]** (Find/Insert/Delete) nad univerzem klíčů $\mathcal{U}$:
- Zvolíme konečné pole **přihrádek** $\mathcal{P} = \{0, \dots, m-1\}$ (velikosti $m$).
- **Hešovací funkce** $h: \mathcal{U} \to \mathcal{P}$ přiřazuje každému klíči přihrádku.
- Prvek s klíčem $k$ ukládáme do přihrádky $h(k)$.

Protože obvykle $m \ll |\mathcal{U}|$, vzniká **kolize** — více klíčů padne do stejné přihrádky.

**Faktor naplnění:** $\alpha = n/m$, kde $n$ je počet uložených prvků.

## Ideální hešovací funkce
- Spočte $h(k)$ v čase $O(1)$ a neukládá žádný stav.
- Rozděluje univerzum **rovnoměrně**: $\forall i, j: ||h^{-1}(i)| - |h^{-1}(j)|| \le 1$.

Při ideálním hešování a rovnoměrně náhodných vstupních datech mají téměř všechny přihrádky $O(n/m)$ prvků a operace trvají $O(n/m)$.

## Příklady hešovacích funkcí
- **Lineární kongruence:** $k \mapsto ak \bmod m$, kde $a$ nesoudělné s $m$ (často $a \approx 0{,}618m$).
- **Vyšší bity součinu:** $k \mapsto \lfloor (ak \bmod 2^w) / 2^{w-\ell} \rfloor$ pro $m = 2^\ell$.
- **Skalární součin** (pro posloupnosti): $\sum a_i k_i \bmod m$.

## Řešení kolizí
1. **[[Hešování-s-řetízky|Hešování s řetízky]]** (Chaining / Open hashing) — každá přihrádka odkazuje na spojový seznam prvků.
2. **[[Otevřená-adresace|Otevřená adresace]]** (Open addressing / Closed hashing) — prvek se ukládá přímo do tabulky; při kolizi se zkouší další přihrádky podle **vyhledávací posloupnosti** $h(k, 0), h(k, 1), \dots$

## Nafukovací tabulka
Když $\alpha$ překročí mez $Z$, zdvojnásobíme $m$, zvolíme novou hešovací funkci a všechny prvky **přehešujeme**. Amortizovaná složitost zůstává konstantní (analogie [[Nafukovací-pole|nafukovacího pole]]).

## Související
- [[Slovník]]
- [[Hešování-s-řetízky]]
- [[Otevřená-adresace]]
- [[Nafukovací-pole]]
