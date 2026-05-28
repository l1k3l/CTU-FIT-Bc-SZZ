---
aliases: [klíč, klíče, klíči, klíčem, klíčů, klíčům, primární klíč, primárního klíče, primárním klíčem, alternativní klíč]
tags: [definice, kurz/DBS]
---

# Klíč schématu

## Definice

**Klíč** $K$ schématu $R(A)$ je taková **minimální** podmnožina atributů z $A$, která jednoznačně určí každou n-tici (konkrétní) relace $R^*$.

**Minimalita:** neexistuje $K' \subset K$, které jednoznačně určuje každou n-tici $R(A)$.

## Vlastnosti

**Tvrzení 1:** Nechť $K$ je klíč schématu $R(A)$. Pak pro každou přípustnou relaci $R^*$ platí: jsou-li $u, v$ dvě různé n-tice z $R^*$, potom $u[K] \neq v[K]$.

**Tvrzení 2:** Relace $R$ může mít několik (alternativních) klíčů.

## Primární vs. alternativní klíč

- **Primární klíč (PK)** — vybraný hlavní klíč; v SQL `PRIMARY KEY`. Implicitně `NOT NULL` + `UNIQUE`.
- **Alternativní klíč** — ostatní (kandidátní) klíče; v SQL `UNIQUE` + `NOT NULL`.

## Související

- [[Relace]]
- [[Cizí-klíč]]
- [[Integritní-omezení]]
