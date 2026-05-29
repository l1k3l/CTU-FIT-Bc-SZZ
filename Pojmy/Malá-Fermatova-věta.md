---
aliases: [malá Fermatova věta, malé Fermatovy věty, malé Fermatově větě, malou Fermatovu větu, malou Fermatovou větou, MFV, Fermatova věta, Fermatovy věty]
tags: [věta, kurz/DML]
---

# Malá Fermatova věta

## Znění

Buď $p$ **[[Prvočíslo|prvočíslo]]** a $a \in \mathbb{Z}$ číslo nesoudělné s $p$ (tj. $p \nmid a$, ekvivalentně $\gcd(a, p) = 1$). Pak
$$a^{p-1} \equiv 1 \pmod p.$$

Ekvivalentní tvar platný **pro každé** $a \in \mathbb{Z}$ (včetně násobků $p$):
$$a^{p} \equiv a \pmod p.$$

## Idea důkazu

Čísla $a, 2a, \dots, (p-1)a$ jsou modulo $p$ navzájem nekongruentní a nenulová (lze [[Kongruence|krátit]], protože $\gcd(a,p)=1$), tvoří tedy permutaci zbytků $\{1, \dots, p-1\}$. Vynásobením všech kongruencí a zkrácením $(p-1)!$ vyjde $a^{p-1} \equiv 1 \pmod p$.

## Důsledky

- **Inverze modulo $p$:** pro $a \not\equiv 0$ je $a^{p-2}$ multiplikativní inverzí $a$ v $\mathbb{Z}_p$ (neboť $a \cdot a^{p-2} = a^{p-1} \equiv 1$).
- **Fermatův test prvočíselnosti:** najde-li se $a$ s $\gcd(a,n)=1$ a $a^{n-1} \not\equiv 1 \pmod n$, není $n$ prvočíslo. Obrácení neplatí (tzv. *Carmichaelova čísla*).

## Vztah k Eulerově větě

Je speciálním případem **[[Eulerova-funkce|Eulerovy věty]]** $a^{\varphi(m)} \equiv 1 \pmod m$: pro prvočíselný modul $m = p$ je $\varphi(p) = p - 1$, takže obě věty splývají.

## Související

- [[Prvočíslo]]
- [[Kongruence]]
- [[Eulerova-funkce]]
- [[Dělitelnost]]
