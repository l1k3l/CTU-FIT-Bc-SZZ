---
tags: [komise, strategie, návod]
---

# Komise optimization guide — jak si zanalyzovat vlastní zkušební komisi

Návod, jak z veřejných dat (historie otázek + studentské zkušenosti z FIT Wiki)
a složení **tvé** komise vyrobit cílenou přípravu na SZZ: **na co se soustředit,
kdo tě nejspíš bude zkoušet a co historicky vyžaduje**.

Ukázkový výstup pro jednu konkrétní komisi: [`Komise-2026-analýza.md`](Komise-2026-analýza.md).
Tenhle guide popisuje, jak ten samý výstup vyrobit pro **libovolnou** komisi.

> **Princip:** Na FIT se otázky u SZZ **nelosují — přiřazuje je komise.** Komise
> tedy vybírá z toho, co sama umí vyzkoušet. Historie otázek a zkušeností členů
> komise proto není jen statistika, ale **přímá předpověď**. Cílem analýzy je
> zúžit přípravu na to, co tvoje konkrétní komise reálně zadá.

---

## Co z toho dostaneš

1. **`zkusenosti_parsed.json`** — strojově čitelná data: každá uložená stránka →
   komise (5 lidí) → studentské zkušenosti (plné vyprávění + příznak, kdo z *tvé*
   komise se v nich objevuje).
2. **`zkusenosti_digest_relevant.txt`** — čitelný výtah jen těch komisí a
   zkušeností, které se týkají **tvojí** komise.
3. **`<tvoje>-analýza.md`** — finální analýza od Clauda: priorita předmětů, profil
   každého zkoušejícího (styl, oblíbené otázky, doptávání), co můžeš vypustit.

---

## Co potřebuješ (vstupní data)

Vše je v tomhle repu jako ukázka — pro vlastní komisi tři věci **nahradíš svými**:

### 1. `komise.txt` — tvoje komise
Jeden řádek na člena, ideálně s rolí a doménou. Formát je volný (čte to Claude, ne skript):

```
prof. Ing. RNDr. Martin Holeňa, CSc. – předseda (all AI/ML courses)
doc. Ing. Kamil Dedecius, Ph.D. – místopředseda (statistics)
Ing. Martin Daňhel, Ph.D. (computer circuits)
Ing. Jiří Hunka (database systems, possibly PA1/2)
Ing. Ivo Petr, Ph.D. (all mathematical courses)
```

Složení komise zveřejňuje fakulta cca **týden před SZZ** (harmonogram). Do té doby
analýzu počítej s předpokládaným složením a po vyhlášení ji přepočítej.

### 2. `question_history1.csv`, `question_history2.csv` — historie otázek
Komunitní tabulka „kdo co u SZZ zkoušel". Sloupce (bez striktního schématu, Claude si poradí):

- **history1**: `Zkoušející, Rok, Oborová(TRUE/FALSE), Předmět, Otázka, Známka, Poznámka`
- **history2**: `Zkoušející, Rok, Obor, Oborová, Předmět, Otázka` (bez poznámek a známek)

Pokud máš jen jednu/jinou tabulku, nevadí — skript ji nepoužívá, čte ji až Claude.

### 3. `zkusenosti/` — uložené stránky FIT Wiki
Stránky **„Otázky a zkušenosti ze SZZ \<sezóna\>"** z [fit-wiki.cz](https://fit-wiki.cz)
(škola → státnice). Pro každou sezónu:

1. Otevři stránku v prohlížeči.
2. **Ulož jako → „Webová stránka, kompletní"** (Cmd/Ctrl+S).
3. Výsledkem je `<Název>.html` + složka `<Název>_files/` (ikony, CSS, JS).

> **Skript potřebuje jen `.html` soubory.** Složky `*_files/` (≈20 MB ikon) jsou
> v `.gitignore` a nepotřebuješ je commitovat ani k analýze. Stačí ti `.html`.

Čím víc sezón, tím líp — v ukázce je léto 2021 – zima 2026 (10 stránek).

---

## Příprava prostředí

Potřebuješ jen **Python 3** (žádné knihovny navíc — skript používá jen standardní
knihovnu). Ověř:

```bash
python3 --version
```

---

## Krok 1 — přizpůsob a spusť extrakční skript

### 1a. Nastav svou komisi ve skriptu

V [`parse_zkusenosti.py`](parse_zkusenosti.py) nahoře uprav slovník `MY` —
**příjmení členů tvé komise** a regex, kterým je v textu najdeš:

```python
MY = {
    "Holeňa":   r"Hole[ňn]a",      # ň i n kvůli překlepům/diakritice
    "Dedecius": r"Dedeci",
    "Daňhel":   r"Da[ňn]hel",
    "Hunka":    r"Hunka",
    "Petr":     r"(?:Ivo\s+Petr|Petr\s*\(\s*Ivo\s*\)|\bI\.\s*Petr)",
}
```

> **Pozor na příjmení, která jsou zároveň křestní jména.** „Petr" je i křestní
> jméno (Novák Petr, Petr Špaček). Ve skriptu je proto Petr matchován jen jako
> *příjmení* (`Ivo Petr`, `Petr (Ivo)`, `I. Petr`) a `PETR_FIRSTNAME` filtruje
> falešné shody. Pokud tvůj zkoušející má podobně dvojznačné jméno, udělej totéž.

### 1b. Spusť

```bash
# zapíše zkusenosti_parsed.json + vytiskne výtah relevantních komisí:
python3 parse_zkusenosti.py > zkusenosti_digest_relevant.txt

# varianty:
python3 parse_zkusenosti.py --all        # výtah VŠECH komisí (ne jen tvé)
python3 parse_zkusenosti.py --json-only   # jen JSON, bez výtahu
```

Skript se v `glob`u dívá do složky `zkusenosti/` vedle sebe a zpracuje všechny `*.html`.

---

## Co skript vyrobí (výstupy)

### `zkusenosti_parsed.json`
Pole stránek; každá má `season`, `file` a `committees`. Každá komise:

```json
{
  "committee_raw": "3-BI-UI.21 - (Holeňa, Kleprlík, Friedjungová, Kohlík, Balík)",
  "examiners": ["Holeňa", "Kleprlík", "Friedjungová", "Kohlík", "Balík"],
  "my_in_committee": ["Holeňa"],
  "students": [
    { "student": "Pufkova máma (BI-UI.21)",
      "experience": "…celé vyprávění…",
      "my_named_in_text": ["Holeňa"] }
  ]
}
```

- `my_in_committee` — kdo z **tvé** komise byl v té komisi (z hlavičky).
- `my_named_in_text` — kdo z tvé komise je **jmenovitě v textu** zkušenosti
  (= koho student popisuje, jak ho zkoušel).

### `zkusenosti_digest_relevant.txt`
Lidsky čitelný výpis: jen komise, kde je někdo z tvojí komise, plus zkušenosti, kde
je některý jmenovitě zmíněn. Tohle je hlavní podklad pro čtení.

---

## Krok 2 — nech Claude udělat analýzu

Otevři projekt v Claude Code (nebo nahraj soubory do chatu) a předej mu:

- `komise.txt`, `question_history1.csv`, `question_history2.csv`,
- `zkusenosti_parsed.json` **nebo** `zkusenosti_digest_relevant.txt`,
- oficiální zadání otázek tvé specializace + společných předmětů (čísla 1–N).

### Doporučený prompt

> Mám SZZ na FIT. V `komise.txt` je moje komise. V `question_history*.csv` je
> historie otázek a v `zkusenosti_parsed.json` (vyrobeno `parse_zkusenosti.py`
> z uložených FIT Wiki stránek) jsou studentské zkušenosti seskupené **podle
> složení komise**. Otázky se nelosují — komise je přiřazuje. Vytvoř mi analýzu
> `<moje>-analýza.md`, která zúží přípravu: priorita předmětů/otázek podle toho,
> kdo z mojí komise je historicky zadává, profil každého zkoušejícího (styl,
> oblíbené otázky, typické doptávání, přísnost) a co můžu skoro vypustit.
> Drž se metodických zásad níže.

### Metodické zásady (důležité — řekni je Claudovi)

1. **Členství v komisi ≠ kdo tě zkouší.** Každého studenta zkouší jen ~2 z 5
   členů. V textu zkušeností se otázky **přiřazují konkrétnímu jménu**
   („Dedecius: …", „Daňhel se ptal…") — to je silnější signál než pouhé složení.
2. **Najdi komise podobné té tvojí.** `my_in_committee` umožní seřadit sezóny
   podle počtu společných členů a podle shody specializace. Nejvíc váž nedávné
   komise tvé specializace.
3. **CSV nejspíš vzniklo z FIT Wiki.** Poznámky v CSV bývají zhuštěním wiki
   vyprávění → ber wiki jako primární, bohatší zdroj a CSV jako rejstřík.
4. **Pozor na zúžení.** Zkoušející často otázku zúží („zaměřte se na…") — sbírej
   tato zúžení, ukazují, co daný člověk reálně chce slyšet.
5. **Maluj jen to, co data unesou.** Když o někom není ani jeden záznam *jak
   zkouší* (jen členství), řekni to a nech ho jako „doménová příprava bez profilu".
6. **Ověř finální komisi.** Analýzu postav, ale po vyhlášení složení přepočítej.

---

## Krok 3 — výstup

Claude vyrobí `<moje>-analýza.md`: TL;DR tabulku priorit, profil každého
zkoušejícího, „horké" otázky napříč členy a seznam předmětů k vypuštění.
Viz ukázkový [`Komise-2026-analýza.md`](Komise-2026-analýza.md).

---

## Přizpůsobení vlastní komisi — checklist

- [ ] Stáhni FIT Wiki stránky „Otázky a zkušenosti ze SZZ …" do `zkusenosti/` (jen `.html` potřebuješ).
- [ ] Sežeň/aktualizuj `question_history*.csv` (komunitní tabulka).
- [ ] Napiš `komise.txt` se svým (předpokládaným) složením.
- [ ] Uprav slovník `MY` v `parse_zkusenosti.py` na svá příjmení (+ ošetři dvojznačná jména).
- [ ] `python3 parse_zkusenosti.py > zkusenosti_digest_relevant.txt`
- [ ] Předej data Claudovi s promptem výše + metodickými zásadami.
- [ ] Po vyhlášení finální komise analýzu přepočítej.

---

## Soubory v repu (přehled)

| Soubor | Co je | Verzováno |
|---|---|---|
| `parse_zkusenosti.py` | Extrakční skript (uprav `MY`) | ✅ |
| `komise.txt` | Ukázkové složení komise | ✅ |
| `question_history1.csv`, `question_history2.csv` | Historie otázek | ✅ |
| `zkusenosti/*.html` | Uložené FIT Wiki stránky | ✅ |
| `zkusenosti/*_files/` | Ikony/CSS/JS uložených stránek | ❌ (`.gitignore`) |
| `zkusenosti_parsed.json` | Výstup skriptu (data) | ❌ (regenerovatelné) |
| `zkusenosti_digest_relevant.txt` | Výstup skriptu (výtah) | ❌ (regenerovatelné) |
| `Komise-2026-analýza.md` | Ukázková finální analýza | ✅ |
