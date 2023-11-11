# F20CN CW2

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/cr2007/F20CN-CW2)

## Computer Network Security

### Asymmetric Cryptography, Firewall Rules Maintenance

Team Members:
- Chandrashekhar Ramaprasad (cr2007)
- Oluwadolabomi Faith Muraino (fm2020)

#### Task 1: Alternative Method of Public-Key Encryption

- [X] Creating a Public Key
  - [X] Random set of positive integers $e = (e_2, e_2, \dots, e_n)$ with the property that $e_i > \sum_{j=1}^{i-1} e_j$ for all $1 \leq i \leq n$.<br>
    (Each new element is greater than the sum of the previous elements i.e. Fibonacci sequence)
  - [X] Prime number $q$ such that $q > 2e_n$
  - [X] and random $w$ such that $\text{ged}(w,q) = 1$,
  - [X] and computes $h = (h_1, h_2, \dots, h_n)$ where $h_i = we_i \text{mod} q$ for $1 \leq i \leq n$.
- [X] Encrypting an $n$-bit message $m = (m_1, m_2, \dots, m_n)$
  - [X] Compute $c = h_1m_1 + h_2m_2 + \dots + h_nm_n$
- [ ] Decrypting ciphertext $c$
