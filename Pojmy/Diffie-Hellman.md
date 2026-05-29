---
aliases: [Diffie-Hellman, Diffie-Hellmanův, Diffie-Hellmanův protokol, Diffie-Hellmanova výměna klíčů, Diffieho-Hellmanův, D-H, DH, výměna klíčů, zřízení společného klíče, ustavení společného klíče]
tags: [definice, kurz/KAB]
---

# Diffie-Hellman

## Definice

**Diffie–Hellmanův protokol** umožňuje dvěma stranám ustavit přes nezabezpečený kanál **sdílený tajný klíč**, aniž by ho přenesly. Bezpečnost stojí na [[Problém-diskrétního-logaritmu|problému diskrétního logaritmu]].

**Veřejné prvky:** velké prvočíslo $m$ a generátor $a$ grupy $\mathbb{Z}_m^{*}$.

1. Účastník $A$ zvolí tajné $k_1$, spočte $y_1 = a^{k_1} \bmod m$ a pošle $y_1$ ($B$).
2. Účastník $B$ zvolí tajné $k_2$, spočte $y_2 = a^{k_2} \bmod m$ a pošle $y_2$ ($A$).
3. Oba dopočtou **stejný** sdílený klíč
$$K = y_2^{\,k_1} \bmod m = y_1^{\,k_2} \bmod m = a^{k_1 k_2} \bmod m.$$

Pro $n$ účastníků analogicky $K = a^{k_1 k_2 \cdots k_n} \bmod m$.

## Bezpečnost a slabina

- Útočník zná $a, m, a^{k_1}, a^{k_2}$, ale bez $k_1$ nebo $k_2$ nedokáže spočítat $a^{k_1 k_2}$ (**Diffie–Hellmanův problém**, není těžší než [[Problém-diskrétního-logaritmu|DLP]]).
- **Slabina:** samotný protokol **neautentizuje** strany ⇒ je zranitelný vůči útoku **man-in-the-middle**. Řeší se podpisem/[[Certifikát|certifikáty]] veřejných hodnot.
- Vychází z **exponenciální šifry** (Pohlig–Hellman); na DH staví i **ElGamal**.

## Související

- [[Problém-diskrétního-logaritmu]]
- [[Asymetrická-šifra]]
- [[Symetrická-šifra]]
