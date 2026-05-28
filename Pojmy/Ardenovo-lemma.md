---
aliases: [Ardenovo lemma, Ardenova věta, Arden, regulární rovnice, regulárních rovnic, regulárním rovnicím, regulárními rovnicemi]
tags: [věta, kurz/AAG]
---

# Ardenovo lemma

## Věta

Nechť $\alpha, \beta$ jsou [[Regulární-výraz|regulární výrazy]] nad $\Sigma$ a **$\varepsilon \notin L(\alpha)$**. Pak regulární rovnice
$$X = \alpha X + \beta$$
má jediné řešení
$$X = \alpha^* \beta.$$

Symetrická levá varianta: rovnice $X = X \alpha + \beta$ má řešení $X = \beta \alpha^*$.

## Důkaz (skica)

**Dosazením:** $\alpha^* \beta = (\varepsilon + \alpha \alpha^*) \beta = \beta + \alpha \alpha^* \beta = \beta + \alpha(\alpha^* \beta)$ — vyhovuje.

**Iterativním rozvíjením:** $X = \beta + \alpha X = \beta + \alpha\beta + \alpha^2\beta + \dots = \alpha^* \beta$.

Pokud $\varepsilon \in L(\alpha)$, řešení už není jednoznačné — k nejmenšímu řešení $\alpha^* \beta$ lze přičíst libovolný „prázdný" podíl.

## Použití

Pro převody mezi formalismy [[Regulární-jazyk|regulárních jazyků]]:

- **[[Konečný-automat|KA]] → [[Regulární-výraz|RV]]**: Pro každý stav $q$ sestav rovnici
$$X_q = \sum_{a \in \Sigma,\ p \in \delta(q,a)} a \cdot X_p \quad (+\varepsilon \text{ pokud } q \in F).$$
Soustavu řeš postupnou **eliminací**: aplikuj Arden na rovnici s rekurzí $X_k = \dots + \alpha_{kk} X_k + \dots$, dosaď výsledek do ostatních rovnic, opakuj. Hledaný RV = $X_{q_0}$.

- **[[Regulární-gramatika|RG]] → RV**: Pro každý neterminál sestav regulární rovnici (z pravidel $A \to aB$ plyne $A = aB + \dots$, z $A \to a$ plyne $\dots + a$, z $A \to \varepsilon$ plyne $\dots + \varepsilon$). Vyřeš pro startovní symbol.

## Příklad

Soustava
$$\begin{cases} A = 1A + 1B \\ B = 0A + 0B + 0 \end{cases}$$
- Levou variantou Ardena $A = 1^* \cdot 1B = 1^+ B$.
- Dosadíme: $B = 0 \cdot 1^+ B + 0 B + 0 = (01^*) B + 0$.
- Arden: $B = (01^*)^* \cdot 0$.
- $A = 1^+ \cdot (01^*)^* \cdot 0$.

## Související
- [[Regulární-výraz]]
- [[Konečný-automat]]
- [[Regulární-gramatika]]
