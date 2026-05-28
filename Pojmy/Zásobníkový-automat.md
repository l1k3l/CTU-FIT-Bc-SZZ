---
aliases: [zásobníkový automat, zásobníkového automatu, zásobníkovému automatu, zásobníkovým automatem, zásobníkové automaty, zásobníkových automatů, zásobníkovým automatům, zásobníkovými automaty, ZA, PDA, NPDA, DPDA, pushdown automaton]
tags: [definice, kurz/AAG]
---

# Zásobníkový automat

## Definice

**Zásobníkový automat (ZA, PDA)** je sedmice
$$R = (Q, \Sigma, G, \delta, q_0, Z_0, F),$$
kde
- $Q$ — konečná množina vnitřních stavů,
- $\Sigma$ — vstupní abeceda,
- $G$ — zásobníková abeceda (jinde $\Gamma$),
- $\delta$ — zobrazení z konečné podmnožiny $Q \times (\Sigma \cup \{\varepsilon\}) \times G^*$ do konečných podmnožin $Q \times G^*$,
- $q_0 \in Q$ — počáteční stav,
- $Z_0 \in G$ — počáteční symbol v zásobníku,
- $F \subseteq Q$ — množina koncových stavů.

$\delta(q, a, \alpha) \ni (p, \gamma)$ znamená: ve stavu $q$, na vrcholu zásobníku $\alpha$, čteme $a \in \Sigma \cup \{\varepsilon\}$, přejdeme do $p$ a nahradíme vrchol $\alpha$ řetězcem $\gamma$.

## Konfigurace a přechod

**Konfigurace** $(q, w, \alpha) \in Q \times \Sigma^* \times G^*$. Počáteční $(q_0, w, Z_0)$.

**Přechod**
$$(q, aw', \alpha\beta) \vdash (p, w', \gamma\beta) \iff (p, \gamma) \in \delta(q, a, \alpha),\ a \in \Sigma \cup \{\varepsilon\}.$$

## Přijímané jazyky

**Koncovým stavem:** $L(R) = \{w : (q_0, w, Z_0) \vdash^* (q, \varepsilon, \gamma),\ q \in F\}$.

**Prázdným zásobníkem:** $L_\varepsilon(R) = \{w : (q_0, w, Z_0) \vdash^* (q, \varepsilon, \varepsilon)\}$.

**Věta:** Pro nedeterministické ZA jsou oba mody ekvivalentní — pro každý jazyk lze sestrojit ZA přijímající ho jedním modem $\iff$ druhým. Konstrukce používá nové dno $X_0$ a vyprazdňovací (resp. koncový) stav.

## Varianty

**Deterministický ZA (DZA):** $|\delta(q, a, \gamma)| \le 1$ a žádné dvě klauzule $\delta(q, a, \alpha), \delta(q, a/\varepsilon, \beta)$ nemají $\alpha, \beta$ v prefixovém vztahu.

**Deterministické bezkontextové jazyky (DCFL)** = jazyky přijímané DZA koncovým stavem. **DCFL ⊊ CFL** — vlastní podtřída.
- DCFL uzavřena na **doplněk** (CFL ne).
- DCFL **neuzavřena** na $\cup$ a $\cap$.
- Pro DZA: přijetí koncovým stavem ≠ prázdným zásobníkem.

## Vztah k bezkontextovým gramatikám

**Věta:** Jazyk je [[Bezkontextová-gramatika|bezkontextový]] $\iff$ je přijímán nějakým (nedeterministickým) ZA. Dvě konstrukce CFG → ZA:

- **Top-down (jednostavový):** $R = (\{q\}, \Sigma, N\cup\Sigma, \delta, q, S, \emptyset)$; $\delta(q, \varepsilon, A) = \{(q, \alpha) : A \to \alpha \in P\}$ (expanze), $\delta(q, a, a) = \{(q, \varepsilon)\}$ (srovnání). Generuje levý rozklad.
- **Bottom-up (dvoustavový):** $R = (\{q, r\}, \Sigma, N\cup\Sigma\cup\{\#\}, \delta, q, \#, \{r\})$; přesun (shift), redukce (reduce), přijetí $\delta(q, \varepsilon, \#S) = \{(r, \varepsilon)\}$. Generuje pravý rozklad.

## Související
- [[Bezkontextová-gramatika]]
- [[Derivační-strom]]
- [[Konečný-automat]]
