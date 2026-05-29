---
tags: [otázka, kurz/OSY, otázka/18, hotovo]
---

# 18 — Virtualizace paměti stránkováním (zkrácená verze)

## 1. Virtualizace stránkováním

- **[[Virtuální-paměť|VAS]]:** každý [[Proces|proces]] má vlastní virtuální adresní prostor (`.text`, `.data`, heap, knihovny, stack), mapovaný OS+HW do fyzické paměti.
- **Proč:** VAS > fyzická paměť (32-bit → 4 GB, 64-bit → 16 EB), součet VAS všech procesů ji přesahuje; proces přitom používá jen zlomek VAS.
- **[[Stránkování]]:** VAS dělen na **stránky** (typ. 4 KB), fyz. paměť na stejně velké **rámce**. Libovolná stránka → libovolný rámec; v paměti jen používané stránky, zbytek na disku. Řeší fragmentaci.

**Struktura adresy** (offset se při překladu nemění):
$$\text{VA} = (\text{č. stránky},\ \text{offset}), \quad \text{PA} = (\text{č. rámce},\ \text{offset}).$$
Offset $= \log_2(\text{vel. stránky})$ bitů. (4 KB → offset 12 b; 32-bit VA → č. stránky 20 b.)

---

## 2. Překlad VA → PA

- **[[MMU]]:** HW jednotka, překládá č. stránky → č. rámce přes [[Stránkovací-tabulka|ST]]. Bázi ST drží **PTBR** (x86 `CR3`), mění se při přepnutí procesu.
- **[[Výpadek-stránky|Výpadek stránky]]** (page fault): přístup na stránku s P=0. OS: najdi volný rámec (nebo vyber oběť PRA, dirty → zápis na disk), nahraj stránku (zdroj. soubor/swap/vynuluj), aktualizuj ST (P=1), **zopakuj instrukci**.
- **Řídicí bity řádku ST:** P (present), A (accessed), D (dirty), C (cacheable), W (write), X (exec), U (user/supervisor), G (global).
- **[[TLB]]:** $n$-cestná cache nedávných překladů (č. stránky → č. rámce). Položka: valid, č. stránky, č. rámce, **ASID**, řídicí bity.

**Postup překladu:** TLB → (miss) ST top→nižší úrovně → fyz. adresa.
Chyby: P=0 → page fault; špatná práva → access fault; mimo VAS → segmentation fault.

---

## 3. Struktura tabulek stránek

| Typ | Řádky | Paměť | Překlad |
|---|---|---|---|
| **Jednoúrovňová** | $2^{\text{č.str.}}$ /proces | velká /proces | nejrychlejší (1 přístup) |
| **Víceúrovňová** | dle použ. oblastí | malá /proces | pomalejší (víc přístupů) |
| **Invertovaná** | počet rámců /systém | malá /systém | pomalé (hash + chain) |

- **Jednoúrovňová:** řádek na každou stránku VAS; č. stránky = index. (32-bit/4 KB → $2^{20}$ řádků ≈ 4 MB **na proces** → plýtvání.)
- **Víceúrovňová:** VA = $n$ indexů + offset; v paměti vždy jen top-level + tabulky pro používané oblasti. **x86** 2-úrovňová (PDE+PTE, 10+10+12 b), **x86-64** 4-úrovňová (PML4→PDPT→PD→PT, 9+9+9+9+12 b).
- **Invertovaná:** 1 řádek na **rámec**, 1 tabulka pro celý systém (č. stránky + č. procesu + chain), přístup hašováním + zřetězení. (PowerPC, UltraSPARC.)

Všechny používají **TLB** pro urychlení.

---

## 4. Algoritmy pro náhradu stránek (PRA)

**Princip:** vyber oběť → je-li dirty, zapiš na disk → ve všech ST vynuluj P. Stojí na **lokalitě** (časové i prostorové). Cíl: min. výpadků.

- **OPT (optimální):** nahraď stránku s **nejvzdálenějším příštím přístupem**. Min. výpadků, ale **nerealizovatelný** (neznáme budoucnost) → referenční.
- **NRU:** R (reference) + D (dirty) bity, OS periodicky resetuje R. 4 třídy (R,D): (0,0)<(0,1)<(1,0)<(1,1). Nahraď z nejnižší neprázdné třídy.
- **FIFO:** seznam stránek, nahraď **nejstarší** (dle nahrání, ne přístupu). Hodně výpadků, Beladyho anomálie.
- **Clock:** FIFO jako kruhová fronta + R bit. R=1 → vynuluj a posuň ručičku; R=0 → nahraď. (Two-handed clock: 2 ručičky.)
- **LRU:** nahraď **nejdéle nepoužitou**. Dobrá aproximace OPT, ale drahá implementace (čítač `time-of-used` v každém řádku ST).
- **Aging:** SW simulace LRU. Pro stránku R bit + $n$-bitový čítač C; periodicky: C posuň doprava, nejvyšší bit ← R, resetuj R. Nahraď min. C.

(Referenční řada do 3 rámců: OPT 6, LRU 7, Clock 8, FIFO 9 výpadků.)

---

## Co odpovědět rychle

- **Stránkování:** VAS na stránky, paměť na rámce, libovolná stránka → libovolný rámec; jen používané v RAM.
- **Adresa:** (č. stránky | offset) → (č. rámce | offset); offset se nemění.
- **Překlad:** MMU + ST (báze v PTBR/CR3), urychlení TLB; chybí stránka → page fault.
- **ST:** jednoúrovňová (rychlá, paměťově drahá) / víceúrovňová (šetří RAM) / invertovaná (1 řádek/rámec, hash).
- **PRA:** OPT (referenční), LRU/Aging (dobré), Clock/NRU (R bit), FIFO (nejhorší).
