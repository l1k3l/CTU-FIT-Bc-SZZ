---
aliases: [zásobník, zásobníku, zásobníkem, zásobníky, zásobníků, zásobníkům, stack, LIFO]
tags: [definice, datová-struktura, kurz/PA2]
---

# Zásobník (Stack)

## Definice
**Zásobník** je [[Abstraktní-datový-typ|ADT]] s disciplínou **LIFO** (Last In, First Out) — odebírá se naposledy vložený prvek. Slouží jako učebnicový příklad **formální (axiomatické)** specifikace ADT.

## Specifikace
**Signatury** (typy: `stack`, `elem`, `bool`):
```
init:      -> stack
empty(_):  stack -> bool
push(_,_): stack, elem -> stack
top(_):    stack -> elem      // prvek na vrcholu
pop(_):    stack -> stack     // odebrání vrcholu
```
**Axiomy:**
```
empty(init)      = true        top(init)        = error
empty(push(s,x)) = false       top(push(s,x))   = x
pop(init)        = init        pop(push(s,x))   = s
```
(Pozor: `top` prázdného zásobníku je chyba, `pop` prázdného je ve formální specifikaci no-op.)

## Implementace a složitost
- **Pole pevné délky** — omezená kapacita; push/pop $O(1)$.
- **Dynamicky alokované pole** (kapacita z konstruktoru) — omezená kapacita; $O(1)$.
- **[[Nafukovací-pole]]** — neomezené; push/pop **amortizovaně** $O(1)$.
- **[[Spojový-seznam]]** (jednosměrný) — vkládání i odebírání na začátku, push/pop $O(1)$.

Časová složitost push i pop je tedy **konstantní** (u nafukovacího pole amortizovaně). V STL: `std::stack` (wrapper nad `deque`/`list`/`vector`).

## Související
- [[Abstraktní-datový-typ]]
- [[Fronta]]
- [[Spojový-seznam]]
- [[Nafukovací-pole]]
