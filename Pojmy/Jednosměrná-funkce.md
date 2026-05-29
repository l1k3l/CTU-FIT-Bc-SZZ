---
aliases: [jednosměrná funkce, jednosměrné funkce, jednosměrnou funkcí, jednosměrných funkcí, jednosměrnost, padací dvířka, padací vrátka, jednosměrná funkce s padacími dvířky]
tags: [definice, kurz/KAB]
---

# Jednosměrná funkce

## Definice

Funkce $f : X \to Y$ je **jednosměrná**, jestliže je snadné z libovolného $x \in X$ vypočítat $y = f(x)$, ale pro náhodně vybraný obraz $y \in f(X)$ je **výpočetně neschůdné** najít nějaký vzor $x$ s $f(x) = y$ (přitom alespoň jeden vzor existuje).

## Dva typy

1. **Jednosměrné funkce 1. typu** — jednosměrnost je dána složitostí operace a její inverze; teoreticky vzor najít lze, prakticky ne. Příklad: násobení dvou prvočísel $p \cdot q$ vs. faktorizace součinu.
2. **Jednosměrné funkce s padacími dvířky (trapdoor)** — vzor z obrazu lze najít, ale jen se znalostí tajné informace („padacích dvířek“ = klíče). Příklad: [[Asymetrická-šifra|asymetrická kryptografie]] — padacími dvířky je soukromý klíč.

## Použití

- [[Hašovací-funkce|Hašovací funkce]] jsou jednosměrné 1. typu.
- [[Asymetrická-šifra|Asymetrické šifry]] ([[RSA]]) jsou jednosměrné funkce s padacími dvířky.

## Související

- [[Hašovací-funkce]]
- [[Asymetrická-šifra]]
- [[RSA]]
