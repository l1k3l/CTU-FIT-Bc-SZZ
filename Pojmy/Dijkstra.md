---
aliases: [Dijkstra, Dijkstrův algoritmus, Dijkstrova algoritmu, Dijkstrově algoritmu]
tags: [algoritmus, kurz/AG1]
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

## Související

- [[Vzdálenost]]
- [[BFS]]
- [[Bellman-Ford]]
- [[Binární-halda]]
