---
aliases: [směrování, routing, routingu, statické směrování, dynamické směrování, směrovací protokol, směrovací protokoly]
tags: [definice, kurz/PSI]
---

# Směrování

## Definice

**Směrování (routing)** je hledání **cesty** mezi konkrétní zdrojovou a cílovou
stanicí. **Cesta** = posloupnost [[Směrovač|směrovačů]], kterou musí projít
paket. Informace pro směrování jsou ve **směrovacích tabulkách**.

## Statické vs. dynamické

- **Statické** — tabulky se nastavují manuálně; funguje okamžitě, ale nereaguje
  na změny; vhodné pro malé sítě.
- **Dynamické** — tabulky konfigurují **směrovací protokoly** automaticky za
  provozu výměnou zpráv; reaguje na výpadky a nové směrovače (konvergence).

## Druhy dynamických algoritmů

| Algoritmus | Vyměňuje se | Optimalizace | Protokol |
|---|---|---|---|
| **Distance Vector (DVA)** | vektory vzdáleností | distrib. [[Bellman-Ford]] (relaxace), nedostupnost = ∞ | RIP |
| **Link State (LSA)** | stavy linek → graf | [[Dijkstra]] (kostra nejkratších cest) | OSPF, IS-IS |
| **Path Vector (PVA)** | celé cesty (posloupnost ID AS) | délka cesty (AS_PATH) | BGP |

- **Vnitřní směrování** (uvnitř AS): RIP, OSPF. **Vnější** (mezi AS): BGP.
- **Autonomní systém (AS)** = skupina IP rozsahů jednoho ISP; **Internet** =
  množina vzájemně propojených AS.

## Související
- [[Směrovač]], [[IP-adresa]]
- [[Dijkstra]], [[Bellman-Ford]], [[Graf]], [[Kostra]]
