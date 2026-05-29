---
aliases: [certifikační autorita, certifikační autority, certifikační autoritou, certifikačních autorit, certifikační autoritě, CA, kořenová CA, registrační autorita, PKI, infrastruktura veřejného klíče]
tags: [definice, kurz/KAB]
---

# Certifikační autorita

## Definice

**Certifikační autorita (CA)** je důvěryhodná třetí strana, která na základě žádosti **vydává, aktualizuje a odvolává [[Certifikát|certifikáty]]**. Každý účastník zná veřejný klíč CA $VK_{Aut}$ a jím ověřuje, že certifikát vydala právě tato CA. Příjem žádostí a kontrolu údajů provádí **registrační autorita**.

Oproti autoritě pro veřejné klíče (online dotaz na každý klíč) certifikáty **nevyžadují kontakt s třetí stranou** při každé komunikaci — stačí vyměnit a ověřit certifikáty.

## Certifikační strom a řetězec

- Pro velký počet uživatelů se zřizuje **více CA** ve **stromové struktuře** (certifikační strom); kořen je **kořenová CA** s **kořenovým certifikátem**.
- **Řetězec certifikátů** = posloupnost od certifikátu uživatele ke kořenovému certifikátu. Certifikát je platný $\iff$ jsou platné všechny certifikáty v řetězci.
- Kořenový certifikát musí být ověřen jinou bezpečnou cestou.
- **Křížová certifikace** (jedno-/obousměrná) propojuje různé stromy CA.

## PKI

**PKI (Public Key Infrastructure)** = norma (vychází z ITU-T X.500) specifikující technická a organizační opatření pro vydávání, správu, používání a odvolávání klíčů a certifikátů; cílem je interoperabilita.

## Související

- [[Certifikát]]
- [[Digitální-podpis]]
- [[Asymetrická-šifra]]
