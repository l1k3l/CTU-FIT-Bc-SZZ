---
tags: [otázka, kurz/ML2, otázka/20, todo]
---

# Posilované učení

> **Otázka SZZ:** Posilované učení.

Zdroje: BI-ML2 (FIT ČVUT), přednáška 12 — Základní koncepty posilovaného učení, Explorace vs. exploitace, Jednoruký a víceruký (k-ruký) bandita, Algoritmy řešení k-rukého bandity, Konečné Markovské rozhodovací procesy.

Značení: agent, prostředí, stav $S_t$, akce $A_t$, odměna $R_t$, hodnota akce $q_*(a)$, odhad $Q_t(a)$, $\epsilon$ míra explorace, $\gamma$ discount, $G_t$ celková vážená odměna.

---

## 1. Základní koncepty

**Posilované učení** (angl. *reinforcement learning*, RL) učí **agenta**, jak se chovat, aby maximalizoval **odměnu** vázanou na plnění cíle. Agentovi neříkáme, jaké akce má dělat — musí je **zkoušením** sám objevit.

Schéma: agent se nachází v **prostředí** (angl. *environment*), které je v nějakém **stavu** (angl. *state*); na základě stavu zvolí **akci** (angl. *action*), za niž obdrží okamžitou **odměnu** (angl. *reward*) a prostředí (typicky) změní stav.

- Prostředí může být **náhodné** (nový stav i odměna po stejné akci mohou být náhodné, rozdělení se může v čase měnit).
- Cílem není jen okamžitá odměna, ale **součet všech budoucích** odměn (s váhou na dosažení cíle).
- RL je **třetí paradigma** strojového učení, odlišné od supervizovaného i **[[Nesupervizované-učení|nesupervizovaného]]** učení; je nejblíže obecné představě o umělé inteligenci. Úspěchy: AlphaGo Zero (Go, 2017), AlphaStar (StarCraft II, 2019), chlazení datacenter, doladění LLM (RLHF).

---

## 2. Dilema explorace vs. exploitace

- **Explorace** (angl. *exploration*): zkoušení dosud nevyzkoušených akcí, abychom objevili lepší možnosti.
- **Exploitace** (angl. *exploitation*): využití dosavadní znalosti — volba akce, o které víme, že přináší dobrou odměnu.

**Dilema:** k vysoké odměně je potřeba exploitovat známé dobré akce, ale aby je agent našel, musí i explorovat. Ani jedna činnost sama nestačí; agent musí zkoušet různé akce a **zároveň** progresivně preferovat ty nejlepší. Neexistuje triviální řešení — algoritmy obě činnosti kombinují.

*Příklad (cesta do školy).* 3 možnosti (pěšky/kolo/metro) s pravděpodobnostmi včasného příchodu 30 %/50 %/90 %, cíl maximalizovat počet včasných příchodů za 30 dní. Příliš krátká explorace (3 dny → exploitace) dá průměrně ~20,9 včas; čistě náhodná volba ~17; rozumná kombinace (15 dní explorace, pak exploitace) ~21,8. Delší explorace zpřesní odhady a zlepší exploitační fázi.

---

## 3. k-ruký (víceruký) bandita

**Jednoruký bandita** = výherní automat s jednou pákou (akce → náhodná odměna). **k-ruký (víceruký) bandita** (angl. *k-armed bandit*): $k$ akcí, každá s jiným rozdělením odměn. Nereflektuje změnu prostředí (žádný stav), jen výběr akce.

**Hodnota akce.** Akce v čase $t$ je $A_t$, odměna $R_t$. **Hodnota akce** $a$ (angl. *value*) je očekávaná odměna
$$q_*(a)=\mathrm E[R_t\mid A_t=a],$$
$q_*:\mathcal A\to\mathbb R$ je **hodnotová funkce**. Známe-li $q_*$, volíme $\arg\max_a q_*(a)$; reálně ji musíme **odhadovat**.

**Odhad hodnoty (výběrový průměr).** Odhad $Q_t(a)$ jako průměr odměn z dřívějších voleb akce $a$:
$$Q_t(a)=\frac{\sum_{\tau=1}^{t-1}R_\tau\,\mathbb 1_{A_\tau=a}}{\sum_{\tau=1}^{t-1}\mathbb 1_{A_\tau=a}}.$$
Podle **[[Zákon-velkých-čísel|zákona velkých čísel]]** $Q_t(a)\to q_*(a)$ při počtu výběrů $\to\infty$.

**Inkrementální update (úspora paměti).** Není třeba ukládat historii:
$$Q_{n+1}=Q_n+\frac1n\big(R_n-Q_n\big),\qquad\text{obecně}\quad \text{NovýOdhad}\leftarrow\text{StarýOdhad}+\text{KrokAlpha}\cdot(\text{Cíl}-\text{StarýOdhad}).$$

**Metody výběru akce.**
- **Hladový výběr (greedy):** $A_t=\arg\max_a Q_t(a)$ — čistá exploitace, přestane explorovat (špatné při nepřesných $Q_t$ / nestacionaritě).
- **$\epsilon$-hladový ($\epsilon$-greedy):** s pravděpodobností $1-\epsilon$ greedy, s pravděpodobností $\epsilon$ náhodná akce. Zaručuje $Q_t(a)\to q_*(a)$ pro všechny $a$ (každá akce občas zkoušena).

**Algoritmus ($\epsilon$-greedy):** inicializuj $Q(a)=0$, $N(a)=0$; opakuj: $A\leftarrow$ greedy s prav. $1-\epsilon$, jinak náhodně; $R\leftarrow\text{bandit}(A)$; $N(A)\mathrel{+}=1$; $Q(A)\leftarrow Q(A)+\frac1{N(A)}[R-Q(A)]$. Větší $\epsilon$ → více explorace.

**Rozšíření:**
- **Nestacionární případ:** konstantní krok $\alpha\in(0,1]$ místo $1/n$ → $Q_{n+1}=\alpha R_n+(1-\alpha)Q_n$ (**exponenciální klouzavý průměr**, větší váha aktuálním odměnám). Konvergence dle ZVČ vyžaduje $\sum_n\alpha_n=\infty$ a $\sum_n\alpha_n^2<\infty$ (splní $\alpha_n=1/n$, nikoliv konstanta — v nestacionaritě ale není k čemu konvergovat).
- **Optimistické počáteční hodnoty:** nastav $Q(a)$ na vysokou hodnotu → agent zpočátku projde všechny akce (podpora rané explorace).
- **UCB (Upper-Confidence-Bound):** systematická (nenáhodná) explorace
$$A_t=\arg\max_a\Big[Q_t(a)+c\sqrt{\tfrac{\ln t}{N_t(a)}}\Big],$$
odmocnina = míra **nejistoty** odhadu; preferuje akce buď s vysokou hodnotou, nebo málo zkoušené ($c>0$ řídí exploraci).

---

## 4. Markovský rozhodovací proces (MDP)

Bandita nereflektuje **stav prostředí a jeho změnu** po akci. To zachycuje **[[Markovský-rozhodovací-proces|Markovský rozhodovací proces]]** (angl. *Markov decision process*, MDP).

V kroku $t$ agent dostane stav $S_t$ a odměnu $R_t$, zvolí akci $A_t$; o krok později dostane odměnu $R_{t+1}$ a nový stav $S_{t+1}$. S množinou stavů $\mathcal S$ a akcí $\mathcal A$ je **dynamika**
$$p(s',r\mid s,a)=\mathrm P(S_t=s',R_t=r\mid S_{t-1}=s,A_{t-1}=a),$$
MDP je trojice $(\mathcal S,\mathcal A,p)$. **Markovská vlastnost:** přechod ze stavu $s$ při akci $a$ **nezávisí na historii**, jak jsme se do $s$ dostali.

**Cíl.** Pro **discount** $0\le\gamma\le1$ definujeme **celkovou váženou odměnu** (angl. *discounted return*)
$$G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\dots=\sum_{k=0}^\infty\gamma^k R_{t+k+1}.$$
Cílem je maximalizovat $\mathrm E\,G_t$ — tj. nejen okamžitý zisk, ale celkový budoucí ($\gamma<1$ preferuje bližší budoucnost).

**Moderní metody** aproximují (např. **[[Neuronová-síť|neuronovou sítí]]**) **action-value funkci** $q(s,a)=\mathrm E[G_t\mid S_t=s,A_t=a]$ při optimální strategii; řeší se i částečná pozorovatelnost stavu.

---

## Co je potřeba na zkoušku znát

### Definice
- **RL:** agent v prostředí (stav, akce, odměna) maximalizuje (budoucí) odměnu; třetí paradigma ML.
- **Explorace vs. exploitace:** zkoušet nové vs. využívat známé dobré akce — fundamentální dilema.
- **Hodnota akce:** $q_*(a)=\mathrm E[R_t\mid A_t=a]$; odhad $Q_t(a)$ výběrovým průměrem.
- **MDP:** $(\mathcal S,\mathcal A,p)$, $p(s',r\mid s,a)$; Markovská vlastnost (nezávislost na historii).
- **Discounted return:** $G_t=\sum_{k\ge0}\gamma^k R_{t+k+1}$, cíl $\max\mathrm E\,G_t$.

### Věty / vztahy
- **Konvergence odhadu:** $Q_t(a)\to q_*(a)$ ([[Zákon-velkých-čísel|ZVČ]]); pro krok $\alpha_n$ platí, je-li $\sum\alpha_n=\infty$, $\sum\alpha_n^2<\infty$.
- **Inkrementální update:** $Q_{n+1}=Q_n+\frac1n(R_n-Q_n)$; nestacionárně konstantní $\alpha$ → exponenciální průměr.

### Algoritmy
- **$\epsilon$-greedy:** greedy $\arg\max_a Q_t(a)$ s prav. $1-\epsilon$, jinak náhodně; inkrementální update $Q$.
- **Optimistické počáteční hodnoty** (podpora rané explorace).
- **UCB:** $A_t=\arg\max_a[Q_t(a)+c\sqrt{\ln t/N_t(a)}]$ — systematická explorace dle nejistoty.
