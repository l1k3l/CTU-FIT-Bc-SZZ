---
tags: [otázka, kurz/KAB, otázka/9, todo]
---

# 9 — Asymetrické kryptosystémy, haš, podpis, certifikáty (zkrácená verze)

## 1. Asymetrické kryptosystémy

**Princip:** dvojice klíčů — **VK** (šifrování / ověření, veřejný) a **SK** (dešifrování / podpis, tajný); z VK nelze schůdně získat SK. Jednosměrná funkce s padacími dvířky. Řeší distribuci klíčů symetrických šifer. V praxi hybridně (asymetricky přenes symetrický klíč relace).

| Šifrování | $\text{ŠT} = E_{VK_2}(\text{OT})$, $\text{OT} = D_{SK_2}(\text{ŠT})$ |
|---|---|
| Podpis | $\text{ŠT} = D_{SK_1}(\text{OT})$, $\text{OT} = E_{VK_1}(\text{ŠT})$ |

Těžké problémy: **faktorizace** → RSA; **diskrétní log (PDL)** → DH, ElGamal, DSA.

### RSA
- $n = pq$, $\varphi(n) = (p-1)(q-1)$, $e$: $\gcd(e,\varphi(n))=1$, $d = e^{-1} \bmod \varphi(n)$.
- $VK=(n,e)$, $SK=(n,d)$; $\;c = m^{e} \bmod n$, $\;m = c^{d} \bmod n$.
- **Korektnost** (Eulerova věta): $ed \equiv 1 \pmod{\varphi(n)} \Rightarrow m^{ed} \equiv m \pmod n$.
- **Bezpečnost** = faktorizace $n$. Prvočísla přes Rabin–Miller; umocňování square-and-multiply; urychlení RSA-CRT (mod $p$, $q$).

### Diffie–Hellman (PDL)
Veřejné: prvočíslo $m$, generátor $a$ z $\mathbb{Z}_m^{*}$.
$A$: pošle $y_1 = a^{k_1}\bmod m$; $B$: pošle $y_2 = a^{k_2}\bmod m$; sdílený
$$K = y_2^{k_1} = y_1^{k_2} = a^{k_1 k_2} \bmod m.$$
**PDL:** z $y=b^k$ nalézt $k$; v $\mathbb{Z}_p^{*}$ není znám polynomiální algoritmus. **Slabina DH:** bez autentizace → **MITM** (nutné certifikáty). ElGamal: úprava DH, šifrování i podpis.

## 2. Hašovací funkce (SHA-2, HMAC)

**Def.:** $h: X \to \{0,1\}^n$ **jednosměrná** + **bezkolizní**, komprimuje libovolný vstup na haš délky $n$. (Jiný pojem než haš u hešovacích tabulek.)
- **Bezkoliznost 1. řádu:** nelze najít $M \neq M'$ s $h(M)=h(M')$.
- **2. řádu (2nd-preimage):** k $x$ nelze najít $y \neq x$ s $h(x)=h(y)$.
- **Narozeninový paradox:** kolize už po $\approx 2^{n/2}$ zprávách ⇒ délka haše = bezpečnost.

**Konstrukce – Merkle–Damgård:** $H_i = f(H_{i-1}, M_i)$, $H_0 = IV$; padding `1`+`0`+64b délka zprávy. *Bezkolizní kompresní funkce ⇒ bezkolizní haš.* **Davies–Meyer:** $H_i = E_{M_i}(H_{i-1}) \oplus H_{i-1}$.

**SHA-1**: 160 b, blok 512 b, 80 rund — **prolomena**. **SHA-2**:

| | SHA-256 | SHA-384 | SHA-512 |
|---|---|---|---|
| haš [b] | 256 | 384 | 512 |
| blok [b] | 512 | 1024 | 1024 |
| slovo [b] | 32 | 64 | 64 |
| bezpečnost [b] | 128 | 192 | 256 |

**HMAC** (klíčovaný haš s tajným $K$):
$$\mathrm{HMAC}_K(M) = H\big((K^{+}\oplus opad)\,\|\,H((K^{+}\oplus ipad)\,\|\,M)\big),\quad ipad=\texttt{0x36},\ opad=\texttt{0x5C}.$$
Nepadělatelná integrita + autentizace původu + challenge–response. Symetrické ⇒ **ne nepopiratelnost**.

## 3. Digitální podpis

Podpis **SK**, ověření **VK**; podepisuje se **haš** zprávy.
**Vlastnosti:** autentizace/nezfalšovatelnost + ověřitelnost, integrita, **nepopiratelnost**. Kategorie: přímé × arbitrované.

**RSA podpis:** $S = m^{d} \bmod n$ (resp. $h(M)^d$); ověření $S^{e} \bmod n \stackrel{?}{=} m$ (resp. $h(M)$), protože $de \equiv 1 \pmod{\varphi(n)}$.
**DSA:** podpis na bázi PDL, podepisuje haš, podpisem dvojice $(r,s)$.

## 4. Certifikáty a certifikační autority

**Podvržení VK (MITM):** $U$ zamění $VK_A$ za $VK_U$ → čte/mění komunikaci. Techniky distribuce: zveřejnění < veřejný adresář < autorita pro VK < **certifikace**.

**Certifikát:** struktura $\{VK_A, ID_A, \text{platnost}, \dots\}$ **podepsaná** $SK_{Aut}$:
$$C_A = E_{SK_{Aut}}(T, ID_A, VK_A),\qquad \text{ověření } D_{VK_{Aut}}(C_A).$$
Nefalšovatelný, veřejně zpřístupnitelný. Formát **X.509** (ITU-T).

**Certifikační autorita (CA):** důvěryhodná 3. strana, vydává/aktualizuje/odvolává certifikáty; každý zná $VK_{Aut}$. Registrační autorita = příjem žádostí.
**Certifikační strom / řetězec:** od certifikátu uživatele ke kořenové CA; platný ⇔ platné všechny v řetězci. **Křížová certifikace** propojuje stromy. **CRL** = seznam odvolaných. **PKI** = norma pro správu klíčů a certifikátů.

---

## Co odpovědět rychle
- **Asymetrie:** VK šifruje / ověřuje, SK dešifruje / podepisuje; z VK nejde získat SK.
- **RSA:** $c=m^e$, $m=c^d \bmod n$; $d=e^{-1}\bmod\varphi(n)$; bezpečnost = faktorizace.
- **DH:** $K = a^{k_1k_2}\bmod m$; bezpečnost = PDL; slabina = MITM.
- **Haš:** jednosměrná + bezkolizní; Merkle–Damgård; kolize $\approx 2^{n/2}$ (narozeniny); SHA-1 prolomena, SHA-2 OK.
- **HMAC:** $H((K^+\oplus opad)\|H((K^+\oplus ipad)\|M))$ — integrita + autentizace.
- **Podpis:** SK podepíše haš, VK ověří; nepopiratelnost (asymetrie), HMAC ji nedává.
- **Certifikát:** VK + identita podepsané CA; X.509. **CA** = důvěryhodná 3. strana, řetězec ke kořeni, CRL, PKI.
