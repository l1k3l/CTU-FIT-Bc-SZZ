---
aliases: [certifikát, certifikátu, certifikátem, certifikáty, certifikátů, certifikátech, digitální certifikát, X.509, certifikát veřejného klíče]
tags: [definice, kurz/KAB]
---

# Certifikát

## Definice

**Certifikát** je datová struktura, která svazuje **veřejný klíč** s identitou jeho držitele. Obsahuje:

- veřejný klíč žadatele/držitele $VK_A$,
- identifikační údaje držitele $ID_A$,
- dobu platnosti,
- další údaje vytvořené [[Certifikační-autorita|certifikační autoritou]] (sériové číslo, algoritmus podpisu, …).

Celá struktura je **podepsaná soukromým klíčem CA** $SK_{Aut}$, takže ji každý ověří veřejným klíčem CA $VK_{Aut}$:
$$C_A = E_{SK_{Aut}}(T,\, ID_A,\, VK_A), \qquad D_{VK_{Aut}}(C_A) = (T,\, ID_A,\, VK_A).$$
Úspěšné ověření je zároveň důkazem, že certifikát vydala CA. Certifikát lze tak veřejně zpřístupnit (je nefalšovatelný) a řeší **podvržení veřejného klíče** (MITM) při jeho distribuci.

## Formát X.509

Formát určuje doporučení **ITU-T X.509** (součást X.500). Pole: formát/verze, sériové číslo, algoritmus podpisu, identifikace CA, doba platnosti, identifikace uživatele, veřejný klíč uživatele, jednoznačné identifikátory, rozšíření a **digitální podpis CA**.

## Platnost a odvolání

Každý certifikát má omezenou dobu platnosti. Lze ho **odvolat** (kompromitace SK, změna CA, …); CA zveřejňuje **seznam odvolaných certifikátů (CRL)**.

## Související

- [[Certifikační-autorita]]
- [[Digitální-podpis]]
- [[Asymetrická-šifra]]
