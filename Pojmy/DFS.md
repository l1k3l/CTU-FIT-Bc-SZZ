---
aliases: [DFS, prohledávání do hloubky, do hloubky, depth-first search]
tags: [algoritmus, kurz/ZUM]
---

# DFS — prohledávání do hloubky

## Idea

Neinformovaná strategie prohledávání [[Stavový-prostor|stavového prostoru]]: k expanzi vždy vybírá **nejhlubší** dosud nalezený list (snaha o co největší zanoření). Implementačně se `open` realizuje **zásobníkem (LIFO)** — pseudokód je shodný s [[BFS]] až na záměnu fronty za zásobník.

## Vlastnosti

- **paměťově nenáročné** — efektivně drží jen aktuální větev,
- **není optimální** — najde *nějakou*, často značně suboptimální cestu,
- **úplnost:** na konečném grafu (s evidencí navštívených uzlů přes `closed`) ano; na nekonečném ne — může „utéct" do nekonečně hluboké větve.

## Použití

Vhodné tam, kde nelze příliš „bloudit" a je žádoucí se rychle vzdálit počátečnímu stavu — např. problém $N$ dam: DFS rychle skládá platné konfigurace, kdežto [[BFS]] zbytečně expanduje všechny konfigurace $1, 2, \dots, N-1$ dam.

## Související

- [[BFS]] (fronta místo zásobníku; optimální v počtu hran)
- [[Stavový-prostor]]
