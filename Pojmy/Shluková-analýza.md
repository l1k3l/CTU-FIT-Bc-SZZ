---
aliases: [shluková analýza, shlukové analýzy, shlukovou analýzou, shlukování, shlukování dat, clustering, shluk, shluku, shluky, shluků, shlukem, cluster, clusterová analýza]
tags: [definice, kurz/ML1]
---

# Shluková analýza

## Definice

**Shluková analýza** (shlukování, angl. *clustering*) je úloha [[Nesupervizované-učení|nesupervizovaného učení]], která rozdělí množinu dat $\mathcal{D}$ v metrickém prostoru $(\mathcal{X}, d)$ na **shluky** podle podobnosti / vzdálenosti tak, aby si body uvnitř shluku byly blízké a body z různých shluků vzdálené. Vyžaduje volbu [[Metrika|metriky]] $d$.

## Hlavní přístupy

- **Hierarchické aglomerativní** — zdola nahoru: každý bod je vlastní shluk, opakovaně se spojují dva nejbližší shluky (kritéria *single / complete / average / Ward linkage*); výstupem je **dendrogram** (otázka 9).
- **Nehierarchické / centroidové** — **k-means**: minimalizace vnitroshlukového součtu čtverců, nutno zadat počet shluků $k$ (otázka 14).
- **Hustotní** — **DBSCAN**: shluk = maximální množina hustotně spojených bodů, detekuje šum a shluky libovolného tvaru, nevyžaduje $k$ (otázka 14).

## Vlastnosti

Charakteristickým problémem je **vyhodnocení** kvality shlukování (chybí cílová proměnná) — používá se např. **Silhouette skóre** nebo vnitroshlukové kritérium.

## Související

- [[Nesupervizované-učení]]
- [[Metrika]]
