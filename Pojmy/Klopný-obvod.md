---
aliases: [klopný obvod, klopného obvodu, klopném obvodu, klopné obvody, klopných obvodů, klopným obvodem, flip-flop, flip-flopy, KO, D klopný obvod]
tags: [definice, kurz/SAP]
---

# Klopný obvod

## Definice
**Klopný obvod (KO, *flip-flop*)** je elementární **jednobitová paměť** — bistabilní [[Sekvenční-obvod|sekvenční obvod]]. Uchovává 1 bit a mění jej v okamžiku daném hodinovým signálem (u synchronních typů). Je základním stavebním prvkem registrů, [[Čítač|čítačů]] a paměťové části sekvenčních obvodů.

## Typy
| typ | charakteristická rovnice $Q^{t+1}$ | poznámka |
|---|---|---|
| **D** | $Q^{t+1}=D$ | přepíše výstup hodnotou vstupu D (v SAP nejpoužívanější) |
| **RS** | $Q^{t+1}=S+\overline R\,Q$, $RS=0$ | set/reset |
| **JK** | $Q^{t+1}=J\overline Q+\overline K Q$ | bez zakázaného stavu |
| **T** | $Q^{t+1}=T\oplus Q$ | *toggle* — překlápí |

V BI-SAP se v syntéze sekvenčních obvodů používá výhradně **klopný obvod typu D**: to, co je na vstupu D, se hodinovým pulzem (CLK) překlopí na výstup; budicí funkce je proto přímo funkce následujícího stavu ($D = Q^{t+1}$).

## Související
- [[Sekvenční-obvod]]
- [[Čítač]]
- [[Konečný-automat]]
