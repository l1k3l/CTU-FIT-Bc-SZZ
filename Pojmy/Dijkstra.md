---
aliases: [Dijkstra, Dijkstrův algoritmus, Dijkstrova algoritmu, Dijkstrově algoritmu]
tags: [algoritmus, kurz/AG1, kurz/ZUM]
---

# Dijkstrův algoritmus

## Specifikace

**Vstup:** [[Orientovaný-graf|orientovaný graf]] $G = (V, E)$ s **nezápornými** délkami $\ell: E \to \mathbb{R}^+_0$ a počáteční vrchol $v_0$.

**Výstup:** [[Vzdálenost|vzdálenosti]] $d(v_0, v)$ a předchůdci $P[v]$ pro všechny $v \in V$.

## Idea

Zobecnění [[BFS|BFS]]. Místo lineární vlny máme „budíky" $h(v)$ — odhady vzdálenosti. Vždy zpracujeme **otevřený vrchol s nejmenším $h$** (jeho budík zazvoní jako první) — provedeme **relaxaci**: pro každého následníka $w$ zkusíme zlepšit $h(w) := \min(h(w), h(v) + \ell((v, w)))$.

## Klíčové vlastnosti

- **(O) Ohodnocení:** $h(v)$ nikdy neroste; je-li konečné, je to délka nějakého $v_0$-$v$-sledu.
- **(M) Monotonie:** $h(z) \le h(o)$ pro uzavřený $z$ a otevřený $o$. **Uzavřený vrchol se už nikdy neotevře** (díky $\ell \ge 0$).
- **(D) Dosažitelnost** a **(V) Vzdálenost** po skončení.

## Složitost

- Naivně (lineární výběr minima): $O(n^2)$.
- S [[Binární-halda|binární haldou]]: $O(|E| \log |V|)$.

## Záporné hrany

Při záporných hranách **Dijkstra selhává** — vlastnost (M) neplatí. Pro grafy bez záporných cyklů je správný algoritmus [[Bellman-Ford|Bellman-Ford]].

## Použití v ZUM

V [[Stavový-prostor|ohodnoceném stavovém prostoru]] $(S, A, c)$ je Dijkstra **optimální neinformované** prohledávání: k expanzi volí OPEN uzel s nejmenší dosavadní cenou cesty $g$, při nalezení levnější cesty provádí **relaxaci**. Je to „BFS respektující ceny akcí". Najde nejlevnější cestu v čase $O(|A| + |S|\log|S|)$, ale prohledává **všesměrově** (jen podle $g$), takže expanduje mnoho irelevantních stavů → motivace pro [[Heuristika|heuristiku]] a [[A-star|A*]] (Dijkstra $=$ A* s $h \equiv 0$).

## Související

- [[Vzdálenost]]
- [[BFS]]
- [[Bellman-Ford]]
- [[Binární-halda]]
