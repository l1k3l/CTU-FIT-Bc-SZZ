---
aliases: [posilované učení, posilovaného učení, posilovaným učením, reinforcement learning, RL, agent, explorace, exploitace, k-ruký bandita, víceruký bandita, ε-greedy, UCB, hodnota akce]
tags: [definice, kurz/ML2]
---

# Posilované učení

## Definice

**Posilované učení** (angl. *reinforcement learning*, RL) je třetí paradigma strojového učení (vedle supervizovaného a [[Nesupervizované-učení|nesupervizovaného]]), v němž se **agent** učí chování maximalizující **odměnu**. Agent se nachází v **prostředí** ve stavu $S_t$, volí **akci** $A_t$, za niž dostane **odměnu** $R_t$ a (typicky) nový stav. Cílem není jen okamžitá, ale celková budoucí odměna; agentovi se neříká, jaké akce volit — musí je objevit zkoušením.

## Explorace vs. exploitace

**Explorace** = zkoušení nevyzkoušených akcí (objevení lepších); **exploitace** = využití dosavadní znalosti. Úspěch vyžaduje obojí kombinovat — fundamentální **dilema** RL.

## k-ruký bandita

Nejjednodušší úloha bez stavu: $k$ akcí s různými rozděleními odměn. **Hodnota akce** $q_*(a)=\mathrm E[R_t\mid A_t=a]$, odhad $Q_t(a)$ výběrovým průměrem (konverguje dle [[Zákon-velkých-čísel|ZVČ]]), inkrementálně $Q_{n+1}=Q_n+\tfrac1n(R_n-Q_n)$. Strategie výběru: **$\epsilon$-greedy** (greedy s prav. $1-\epsilon$, jinak náhodně), **optimistické počáteční hodnoty**, **UCB** ($\arg\max_a[Q_t(a)+c\sqrt{\ln t/N_t(a)}]$).

## Stav a MDP

Zahrnutí stavu a jeho změny vede na [[Markovský-rozhodovací-proces|Markovský rozhodovací proces]]; cílem je maximalizovat celkovou váženou odměnu $G_t=\sum_k\gamma^k R_{t+k+1}$.

## Související

- [[Markovský-rozhodovací-proces]]
- [[Nesupervizované-učení]]
- [[Zákon-velkých-čísel]]
- [[Neuronová-síť]]
