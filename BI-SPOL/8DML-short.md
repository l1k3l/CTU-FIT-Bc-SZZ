---
tags: [otázka, kurz/DML, otázka/8, todo]
---

# 8 — Základy teorie čísel (zkrácená verze)

## 1. Dělitelnost

$a \mid b \iff \exists k \in \mathbb{Z}: b = ka$.

**Vlastnosti:** $1 \mid n$, $n \mid 0$; $a \mid b \iff |a| \mid |b|$; $a \mid b \land b \neq 0 \Rightarrow |a| \leq |b|$; $a \mid b \land a \mid c \iff a \mid (mb + nc)\ \forall m, n \in \mathbb{Z}$.

**Dělení se zbytkem:** Pro $a \in \mathbb{Z}$, $d \in \mathbb{N}$ existují jednoznačná $q, r \in \mathbb{Z}$: $a = qd + r$, $0 \leq r < d$. Píšeme $r = a \bmod d$.

**gcd, lcm:** $\gcd(a, b) = $ společný dělitel dělitelný každým dalším společným dělitelem. Duálně lcm. **Nesoudělná:** $\gcd(a, b) = 1$.

## 2. Eukleidův algoritmus a LDR

**Lemma:** $\gcd(a + cb, b) = \gcd(a, b)$.

**EA:** $r_1 = a$, $r_2 = b$, $r_n = r_{n-2} \bmod r_{n-1}$. $\gcd(a, b) = r_k$ = poslední nenulový zbytek.

**Bézoutova rovnost:** $\exists m, n \in \mathbb{Z}: \gcd(a, b) = ma + nb$. Navíc je to nejmenší kladná lineární kombinace.

**REA:** Tabulkou udržujeme $r_i, \alpha_i, \beta_i, q_i$ s rekurzí $\alpha_n = \alpha_{n-2} - q_{n-1}\alpha_{n-1}$ (totéž pro $\beta_n$, $r_n$). Po skončení $r_k = \alpha_k a + \beta_k b$.

**Lineární diofantická rovnice** $ax + by = c$:
- **Řešitelná** $\iff \gcd(a, b) \mid c$.
- **Partikulární řešení:** REA dá $\gcd(a, b) = \alpha a + \beta b$; pak $(x_0, y_0) = (\alpha \cdot c/\gcd, \beta \cdot c/\gcd)$.
- **Všechna řešení:** $\big(x_0 + k \tfrac{b}{\gcd}, y_0 - k \tfrac{a}{\gcd}\big)$, $k \in \mathbb{Z}$.

## 3. Prvočísla

**Definice:** $\mathbb{N} = \{1\} \cup \{\text{prvočísla}\} \cup \{\text{složená}\}$. Prvočíslo má právě dva dělitele.

**Eukleides:** Prvočísel je nekonečně mnoho.

**Důkaz:** Sporem — $P = p_1 \cdots p_k + 1$, buď je $P$ prvočíslo (spor), nebo jej dělí $p_j$ — pak $p_j \mid 1$, spor.

**Eukleidovo lemma:** $p$ prvočíslo, $p \mid ab \land p \nmid a \Rightarrow p \mid b$.

**Základní věta aritmetiky:** Každé $n \geq 2$ má jednoznačný prvočíselný rozklad $n = \prod p_i^{\alpha_i}$.

**gcd a lcm z rozkladu:** $\gcd = \prod p_i^{\min}$, $\operatorname{lcm} = \prod p_i^{\max}$. Vztah: $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |a||b|$, tedy $\operatorname{lcm} = \frac{|a||b|}{\gcd}$ (bez faktorizace).

## 4. Modulární aritmetika

**Kongruence:** $a \equiv b \pmod m \iff m \mid (a - b) \iff a \bmod m = b \bmod m$.

**$\equiv$** je reflexivní, symetrická, tranzitivní. **Zachovává $+, -, \cdot, \text{moc.}$:**
$$a \equiv b, c \equiv d \Rightarrow a \pm c \equiv b \pm d,\ ac \equiv bd,\ a^k \equiv b^k.$$

**$\mathbb{Z}_m = \{0, 1, \dots, m-1\}$** s operacemi $+_m$, $\cdot_m$ (mod $m$). $(\mathbb{Z}_m, +_m, \cdot_m)$ splňuje komutativitu, asociativitu, distributivitu, neutrální prvky $0, 1$, aditivní inverzi $-a = m - a$ (pro $a \neq 0$).

**Multiplikativní inverze:** $a \cdot_m a^{-1} = 1$. Existuje $\iff \gcd(a, m) = 1$. Pro prvočíselné $m$ má každý nenulový prvek inverzi ⇒ $\mathbb{Z}_m$ je **konečné těleso**.

**Hledání inverze:** REA na $ax + my = 1$.

## 5. Malá Fermatova a Eulerova věta

**Krácení v modulu:** $ac \equiv bc \pmod m \iff a \equiv b \pmod{m/\gcd(m, c)}$. Speciálně: $\gcd(m, c) = 1 \Rightarrow$ lze beze změny modula.

**Malá Fermatova věta (MFV):** $p$ prvočíslo, $\gcd(a, p) = 1$:
$$a^{p-1} \equiv 1 \pmod p.$$

**Idea důkazu:** $\{a, 2a, \dots, (p-1)a\}$ je modulo $p$ permutace $\{1, \dots, p-1\}$, tedy součiny se rovnají: $a^{p-1}(p-1)! \equiv (p-1)!$, zkrátíme.

**Eulerova funkce:** $\varphi(n) = |\{k \leq n : \gcd(k, n) = 1\}|$.
- $\varphi(p) = p - 1$ pro prvočíslo $p$.
- $\varphi(p^\alpha) = p^\alpha - p^{\alpha-1}$.
- **Multiplikativita:** $\gcd(m, n) = 1 \Rightarrow \varphi(mn) = \varphi(m)\varphi(n)$.
- Z faktorizace: $\varphi(m) = m \prod_{i}(1 - 1/p_i)$.

**Eulerova věta (EV):** $\gcd(a, m) = 1$:
$$a^{\varphi(m)} \equiv 1 \pmod m.$$

EV zobecňuje MFV (pro prvočíselné $m$: $\varphi(m) = m - 1$).

**Inverze přes MFV/EV:** $a^{-1} \equiv a^{p-2} \pmod p$, resp. $a^{-1} \equiv a^{\varphi(m)-1} \pmod m$.

**Redukce velkých mocnin:** $a^N \pmod m$ — pokud $\gcd(a, m) = 1$, rozlož $N = q \varphi(m) + r$, pak $a^N \equiv a^r \pmod m$. Jinak **binární mocnění** $O(\log N)$.

## 6. Lineární kongruence

$ax \equiv b \pmod m$. **Řešitelná** $\iff \gcd(a, m) \mid b$ (převod na LDR $ax + my = b$).

**Všechna řešení** v $\mathbb{Z}$: $x \equiv x_0 + k \cdot \frac{m}{\gcd(a, m)} \pmod m$.

V $\mathbb{Z}_m$ je řešení přesně $\gcd(a, m)$.

**Pokud $\gcd(a, m) = 1$:** Jediné řešení $x \equiv a^{-1} b \pmod m$ (analogie $x = b/a$).

## 7. Čínská věta o zbytcích

**ČVOZ:** Mějme soustavu
$$x \equiv a_i \pmod{m_i},\quad i = 1, \dots, N,$$
kde $m_i \geq 2$ jsou **po dvou nesoudělná**. Pak řešení existuje a je jednoznačné modulo $M = \prod m_i$.

**Konstrukce řešení:**
1. $M_i = M / m_i$.
2. Najdi $X_i$ s $M_i X_i \equiv 1 \pmod{m_i}$ (REA, jelikož $\gcd(M_i, m_i) = 1$).
3. $x \equiv \sum_i a_i M_i X_i \pmod M$.

**Idea ověření:** Pro $i \neq j$ je $m_j \mid M_i$ ⇒ $a_i M_i X_i \equiv 0 \pmod{m_j}$. Zbude jen $a_j M_j X_j \equiv a_j \pmod{m_j}$.

**Zobecněná ČVOZ:** Pro libovolná $m_i$ existuje řešení $\iff \gcd(m_i, m_j) \mid (a_i - a_j)$ pro každé $i \neq j$. Jednoznačnost modulo $\operatorname{lcm}(m_1, \dots, m_N)$.

**Dosazovací metoda** (univerzálnější): $x = a_1 + m_1 t$, dosadit, vyřešit pro $t$, iterovat.

**Aplikace:** paralelní výpočet s velkými čísly, urychlení RSA dešifrování.

---

## Co odpovědět rychle

- **Dělitelnost:** $a \mid b \iff \exists k: b = ka$. **Dělení se zbytkem** unikátní.
- **EA:** $\gcd(a, b) = $ poslední nenulový zbytek posloupnosti $r_n = r_{n-2} \bmod r_{n-1}$.
- **REA:** $\gcd(a, b) = \alpha a + \beta b$ (Bézoutova rovnost). Tabulkou.
- **LDR** $ax + by = c$: řešitelná $\iff \gcd(a, b) \mid c$. Řešení = partikulární + $k(b/\gcd, -a/\gcd)$.
- **Prvočísla:** nekonečně mnoho (Eukleidův důkaz sporem). Eukleidovo lemma ⇒ jednoznačná faktorizace.
- $\gcd \cdot \operatorname{lcm} = |ab|$.
- **Kongruence** $\equiv$ zachovává $+, -, \cdot, $ mocninu. $a^{-1}$ v $\mathbb{Z}_m$ existuje $\iff \gcd(a, m) = 1$.
- **MFV:** $p$ prvočíslo, $\gcd(a, p) = 1 \Rightarrow a^{p-1} \equiv 1$.
- **EV (zobecnění):** $\gcd(a, m) = 1 \Rightarrow a^{\varphi(m)} \equiv 1$.
- $\varphi$ multiplikativní; $\varphi(m) = m \prod (1 - 1/p_i)$.
- **Lineární kongruence** $ax \equiv b \pmod m$: $\gcd(a, m) \mid b$, $\gcd(a, m)$ řešení v $\mathbb{Z}_m$.
- **ČVOZ:** po dvou nesoudělná moduly ⇒ řešení existuje, jednoznačné mod $\prod m_i$. Formulkou $x = \sum a_i M_i X_i$, kde $M_i X_i \equiv 1 \pmod{m_i}$.
- **ZČVOZ:** podmínka $\gcd(m_i, m_j) \mid (a_i - a_j)$. Jednoznačnost mod $\operatorname{lcm}$.
