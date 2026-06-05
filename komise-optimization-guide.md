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

Finální výstup je **`<tvoje>-analýza.md`** — analýza od Clauda: TL;DR tabulka
priorit předmětů, profil každého zkoušejícího (styl, oblíbené otázky, typické
doptávání, přísnost), „horké" otázky napříč členy a seznam předmětů k vypuštění.
Viz ukázkový [`Komise-2026-analýza.md`](Komise-2026-analýza.md).

---

## Jak to celé proběhne (TL;DR)

1. Připravíš **vstupní data** (jen 2 druhy souborů, viz níže) a **řekneš Claudovi
   složení své komise**.
2. **Claude sám:**
   a. upraví slovník `MY` v `parse_zkusenosti.py` na příjmení tvé komise,
   b. **spustí skript** — ten z HTML vyrobí mezivýstupy (`zkusenosti_parsed.json`
      + čitelný výtah),
   c. přečte výtah + CSV a napíše analýzu `<tvoje>-analýza.md`.

> **Skript nespouštíš ty — spouští ho Claude.** Nemusíš mít předem žádný
> `zkusenosti_parsed.json` ani výtah; tyhle soubory vzniknou až během analýzy.
> Tvoje jediná starost jsou **vstupní data** (2 CSV + HTML).

---

## Vstupní data (jediné, co si připravíš)

### 1. `question_history1.csv`, `question_history2.csv` — historie otázek
Komunitní tabulka „kdo co u SZZ zkoušel". Sloupce (bez striktního schématu, Claude si poradí):

- **history1**: `Zkoušející, Rok, Oborová(TRUE/FALSE), Předmět, Otázka, Známka, Poznámka`
- **history2**: `Zkoušející, Rok, Obor, Oborová, Předmět, Otázka` (bez poznámek a známek)

Máš-li jen jednu/jinou tabulku, nevadí — skript ji nepoužívá, čte ji až Claude při analýze.

### 2. `zkusenosti/` — uložené stránky FIT Wiki
Stránky **„Otázky a zkušenosti ze SZZ \<sezóna\>"** z [fit-wiki.cz](https://fit-wiki.cz)
(škola → státnice). Pro každou sezónu:

1. Otevři stránku v prohlížeči.
2. **Ulož jako → „Webová stránka, kompletní"** (Cmd/Ctrl+S) do složky `zkusenosti/`.
3. Výsledkem je `<Název>.html` + složka `<Název>_files/` (ikony, CSS, JS).

> **Skript potřebuje jen `.html` soubory.** Složky `*_files/` (≈20 MB ikon) jsou
> v `.gitignore`, nepotřebuješ je k ničemu. Stačí ti `.html`.

Čím víc sezón, tím líp — v ukázce je léto 2021 – zima 2026 (10 stránek).

### + Složení komise (řekneš Claudovi)
Není to datový soubor, jen informace pro prompt. Stačí pár řádků „jméno – role
(doména)". Pro pohodlí ji můžeš uložit i do souboru (jako ukázkový `komise.txt`),
ale klidně ji jen vlož do promptu:

```
prof. Ing. RNDr. Martin Holeňa, CSc. – předseda (all AI/ML courses)
doc. Ing. Kamil Dedecius, Ph.D. – místopředseda (statistics)
Ing. Martin Daňhel, Ph.D. (computer circuits)
Ing. Jiří Hunka (database systems)
Ing. Ivo Petr, Ph.D. (all mathematical courses)
```

Složení komise zveřejňuje fakulta cca **týden před SZZ**. Do té doby počítej
s předpokládaným složením a po vyhlášení nech analýzu přepočítat.

---

## Příprava prostředí

Aby mohl Claude skript spustit, musí být v systému **Python 3** (žádné knihovny
navíc — skript používá jen standardní knihovnu):

```bash
python3 --version
```

---

## Co Claude během analýzy udělá

Tohle dělá **Claude**, ne ty — uvádím to, abys věděl/a, co se děje a mohl/a to
zkontrolovat.

### A) Upraví `MY` a spustí parser
Nahoře v [`parse_zkusenosti.py`](parse_zkusenosti.py) je slovník `MY` —
**příjmení členů komise** a regex, kterým je v textu najde. Claude ho přepíše
na tvou komisi:

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
> falešné shody. Má-li tvůj zkoušející podobně dvojznačné jméno, řekni Claudovi,
> ať to ošetří stejně.

Pak spustí (skript bere všechny `*.html` ze složky `zkusenosti/` vedle sebe):

```bash
# zapíše zkusenosti_parsed.json + vytiskne výtah relevantních komisí:
python3 parse_zkusenosti.py > zkusenosti_digest_relevant.txt

# varianty:
python3 parse_zkusenosti.py --all        # výtah VŠECH komisí (ne jen tvé)
python3 parse_zkusenosti.py --json-only   # jen JSON, bez výtahu
```

### Mezivýstupy, které tím vzniknou
- **`zkusenosti_parsed.json`** — strojová data: stránka → komise (5 lidí) →
  studentské zkušenosti. U každé komise `my_in_committee` (kdo z tvé komise tam
  byl) a u každé zkušenosti `my_named_in_text` (koho z tvé komise student popisuje,
  jak ho zkoušel). Tvar:

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

- **`zkusenosti_digest_relevant.txt`** — lidsky čitelný výpis jen komisí, kde je
  někdo z tvé komise (+ zkušenosti, kde je jmenovitě zmíněn). Hlavní podklad pro čtení.

Oba soubory jsou **regenerovatelné** a jsou v `.gitignore` — necommitují se.

### B) Napíše analýzu
Claude přečte výtah + CSV a vytvoří `<tvoje>-analýza.md` podle metodických zásad níže.

---

## Doporučený prompt pro Clauda

Dej Claudovi přístup k souborům (CSV + `zkusenosti/*.html` + `parse_zkusenosti.py`)
a napiš zhruba:

> Mám SZZ na FIT. Moje komise je: **\<vlož složení komise\>**. V `zkusenosti/`
> jsou uložené FIT Wiki stránky „Otázky a zkušenosti ze SZZ" a v
> `question_history*.csv` je historie otázek. Otázky se nelosují — komise je
> přiřazuje.
>
> Postupuj takto: (1) v `parse_zkusenosti.py` uprav slovník `MY` na příjmení mojí
> komise (ošetři jména, která jsou i křestní), (2) **spusť skript**, ať z HTML
> vyrobí `zkusenosti_parsed.json` a čitelný výtah, (3) přečti výtah + CSV a
> vytvoř mi `<moje>-analýza.md`, která zúží přípravu: priorita předmětů/otázek
> podle toho, kdo z mojí komise je historicky zadává, profil každého zkoušejícího
> (styl, oblíbené otázky, typické doptávání, přísnost) a co můžu skoro vypustit.
> Drž se metodických zásad níže.

### Metodické zásady (důležité — řekni je Claudovi)

1. **Členství v komisi ≠ kdo tě zkouší.** Každého studenta zkouší jen ~2 z 5
   členů. V textu zkušeností se otázky **přiřazují konkrétnímu jménu**
   („Dedecius: …", „Daňhel se ptal…") — to je silnější signál než pouhé složení.
2. **Najdi komise podobné té tvojí.** `my_in_committee` umožní seřadit sezóny
   podle počtu společných členů a shody specializace. Nejvíc važ nedávné komise
   tvé specializace.
3. **CSV nejspíš vzniklo z FIT Wiki.** Poznámky v CSV bývají zhuštěním wiki
   vyprávění → ber wiki jako primární, bohatší zdroj a CSV jako rejstřík.
4. **Pozor na zúžení.** Zkoušející často otázku zúží („zaměřte se na…") — sbírej
   tato zúžení, ukazují, co daný člověk reálně chce slyšet.
5. **Maluj jen to, co data unesou.** Když o někom není ani jeden záznam *jak
   zkouší* (jen členství), řekni to a nech ho jako „doménová příprava bez profilu".
6. **Ověř finální komisi.** Analýzu postav, ale po vyhlášení složení přepočítej.

---

## Přizpůsobení vlastní komisi — checklist

- [ ] Stáhni FIT Wiki stránky „Otázky a zkušenosti ze SZZ …" do `zkusenosti/` (jen `.html` potřebuješ).
- [ ] Sežeň/aktualizuj `question_history*.csv` (komunitní tabulka).
- [ ] Zjisti (předpokládané) složení své komise.
- [ ] Předej Claudovi data + složení komise s promptem výše → **Claude** upraví `MY`, spustí skript a napíše analýzu.
- [ ] Po vyhlášení finální komise nech analýzu přepočítat.

---

## Soubory v repu (přehled)

| Soubor | Co je | Verzováno |
|---|---|---|
| `parse_zkusenosti.py` | Extrakční skript (Claude v něm upraví `MY`) | ✅ |
| `question_history1.csv`, `question_history2.csv` | Historie otázek (vstup) | ✅ |
| `zkusenosti/*.html` | Uložené FIT Wiki stránky (vstup) | ✅ |
| `komise.txt` | Ukázkové složení komise (nepovinné — klidně jen v promptu) | ✅ |
| `zkusenosti/*_files/` | Ikony/CSS/JS uložených stránek | ❌ (`.gitignore`) |
| `zkusenosti_parsed.json` | Mezivýstup skriptu (data) — vyrobí Claude | ❌ (regenerovatelné) |
| `zkusenosti_digest_relevant.txt` | Mezivýstup skriptu (výtah) — vyrobí Claude | ❌ (regenerovatelné) |
| `Komise-2026-analýza.md` | Ukázková finální analýza | ✅ |
