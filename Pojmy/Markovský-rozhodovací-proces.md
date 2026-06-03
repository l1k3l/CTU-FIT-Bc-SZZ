---
aliases: [Markovský rozhodovací proces, Markovského rozhodovacího procesu, MDP, Markov decision process, discounted return, celková vážená odměna, discount, váhový faktor, action-value]
tags: [definice, kurz/ML2]
---

# Markovský rozhodovací proces

## Definice

**Markovský rozhodovací proces** (angl. *Markov decision process*, **MDP**) je formální model prostředí v [[Posilované-učení|posilovaném učení]], který zachycuje **stav a jeho změnu** po akci. Je to trojice $(\mathcal S,\mathcal A,p)$, kde $\mathcal S$ je množina stavů, $\mathcal A$ množina akcí a $p$ **dynamika**
$$p(s',r\mid s,a)=\mathrm P(S_t=s',R_t=r\mid S_{t-1}=s,A_{t-1}=a).$$
**Markovská vlastnost:** přechod ze stavu $s$ při akci $a$ **nezávisí na historii**, jak se agent do $s$ dostal.

## Cíl

Pro **discount** (váhový faktor) $0\le\gamma\le1$ je **celková vážená odměna** (angl. *discounted return*)
$$G_t=\sum_{k=0}^\infty\gamma^k R_{t+k+1}=R_{t+1}+\gamma R_{t+2}+\gamma^2 R_{t+3}+\dots,$$
cílem je maximalizovat $\mathrm E\,G_t$. $\gamma<1$ preferuje bližší budoucnost. Optimální chování charakterizuje **action-value funkce** $q(s,a)=\mathrm E[G_t\mid S_t=s,A_t=a]$ (moderně aproximovaná [[Neuronová-síť|neuronovou sítí]]).

## Související

- [[Posilované-učení]]
- [[Neuronová-síť]]
- [[Náhodná-veličina]]
