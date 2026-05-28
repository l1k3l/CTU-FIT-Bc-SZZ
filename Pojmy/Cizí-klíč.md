---
aliases: [cizí klíč, cizího klíče, cizím klíčem, cizí klíče, cizích klíčů, foreign key]
tags: [definice, kurz/DBS]
---

# Cizí klíč

## Definice

**Cizí klíč (FK)** je atribut (či množina atributů) v relaci $R$, který odkazuje na klíč jiné (nebo téže) relace $S$. Zápis: $R[X] \subseteq S[Y]$, kde $Y$ je klíč $S$.

Vyjadřuje **referenční integritu**: každá hodnota v $R[X]$ musí existovat v $S[Y]$ (nebo být `NULL`, pokud je to dovoleno).

## Syntax v SQL DDL

```sql
foreign key (sloupec) references tabulka(sloupec)
   [on delete <akce>]
   [on update <akce>]
```

Akce: `no action`, `restrict`, `cascade`, `set null`, `set default`.

## Související

- [[Klíč-schématu]]
- [[Integritní-omezení]]
- [[Relace]]
