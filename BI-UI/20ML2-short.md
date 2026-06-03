---
tags: [otázka, kurz/ML2, otázka/20, todo]
---

# 20 — Posilované učení (zkrácená verze)

## 1. Základní koncepty

[[Posilované-učení|Posilované učení]] (RL): **agent** v **prostředí** (stav $S_t$) volí **akci** $A_t$, dostane **odměnu** $R_t$ a nový stav. Cíl: maximalizovat (celkovou budoucí) odměnu. Agentovi neříkáme akce — učí se zkoušením. **Třetí paradigma** ML (vedle supervizovaného a [[Nesupervizované-učení|nesupervizovaného]]).

## 2. Explorace vs. exploitace

- **Explorace** = zkoušet nové akce (objevit lepší);
- **Exploitace** = využít známé dobré akce.

**Dilema:** obojí je nutné; ani jedno samo nestačí. Algoritmy je kombinují.

## 3. k-ruký bandita

$k$ akcí, každá s jiným rozdělením odměn (žádný stav). **Hodnota akce** $q_*(a)=\mathrm E[R_t\mid A_t=a]$.

**Odhad** výběrovým průměrem $Q_t(a)=\frac{\text{součet odměn za }a}{\text{počet voleb }a}$; dle [[Zákon-velkých-čísel|ZVČ]] $Q_t(a)\to q_*(a)$.

**Inkrementální update:** $Q_{n+1}=Q_n+\frac1n(R_n-Q_n)$ (Nový ← Starý + Krok·(Cíl−Starý)).

**Výběr akce:**
- **greedy:** $A_t=\arg\max_a Q_t(a)$ (čistá exploitace);
- **$\epsilon$-greedy:** greedy s prav. $1-\epsilon$, jinak náhodně → zaručí $Q_t(a)\to q_*(a)$.

**Rozšíření:**
- nestacionární: konstantní krok $\alpha$ → $Q_{n+1}=\alpha R_n+(1-\alpha)Q_n$ (exp. klouzavý průměr); konvergence vyžaduje $\sum\alpha_n=\infty$, $\sum\alpha_n^2<\infty$;
- **optimistické počáteční hodnoty** (raná explorace);
- **UCB:** $A_t=\arg\max_a[Q_t(a)+c\sqrt{\ln t/N_t(a)}]$ — systematická explorace dle nejistoty.

## 4. Markovský rozhodovací proces (MDP)

Přidává **stav** a jeho změnu. [[Markovský-rozhodovací-proces|MDP]] $(\mathcal S,\mathcal A,p)$ s dynamikou
$$p(s',r\mid s,a)=\mathrm P(S_t=s',R_t=r\mid S_{t-1}=s,A_{t-1}=a).$$
**Markovská vlastnost:** přechod nezávisí na historii.

**Cíl:** maximalizovat **celkovou váženou odměnu** (discounted return)
$$G_t=\sum_{k=0}^\infty\gamma^k R_{t+k+1},\qquad 0\le\gamma\le1.$$
Moderně: aproximace **action-value** $q(s,a)=\mathrm E[G_t\mid S_t=s,A_t=a]$ (např. [[Neuronová-síť|neuronovou sítí]]).

---

## Co odpovědět rychle
- **RL:** agent–prostředí–stav–akce–odměna; max. budoucí odměny; učení zkoušením.
- **Explorace vs. exploitace** = základní dilema.
- **Bandita:** $q_*(a)=\mathrm E[R_t\mid A_t=a]$, odhad průměrem, update $Q_{n+1}=Q_n+\frac1n(R_n-Q_n)$.
- **Výběr:** $\epsilon$-greedy, optimistic init, UCB.
- **MDP:** $(\mathcal S,\mathcal A,p)$, Markovská vlastnost; cíl $\max\mathrm E\,G_t$, $G_t=\sum\gamma^k R_{t+k+1}$.
