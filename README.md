# 🔐 Challenge 4 – Ongoing Cryptanalysis Investigation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Focus](https://img.shields.io/badge/Focus-Statistical%20Cryptanalysis-red)

**BlackHat Challenge Series**  
Farai Denhere – MS Cybersecurity  

---
## 🚀 BlackHat Challenge Navigation


[![Back to Main](https://img.shields.io/badge/Back%20to-Main%20Repository-blue)](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography)
[![Challenge 1](https://img.shields.io/badge/Challenge%201-Hill%20Cipher-blue)](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge1)
[![Challenge 2](https://img.shields.io/badge/Challenge%202-Unresolved-orange)](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge2)
[![Challenge 3](https://img.shields.io/badge/Challenge%203-Vigen%C3%A8re-green)](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge3)
[![Challenge 4](https://img.shields.io/badge/Challenge%204-In%20Progress-yellow)](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge4)
[![Challenge 5](https://img.shields.io/badge/Challenge%205-Double%20Columnar-red)](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge5)


---

## 📌 Executive Summary

Challenge 4 remains an unresolved ciphertext despite structured statistical analysis, cipher classification attempts, and multiple brute-force strategies.

Extensive investigative efforts were conducted, and several cipher families were systematically tested and eliminated.  
The cipher does not clearly match standard classical encryption fingerprints.

This document outlines the full analytical workflow and current findings.

---

## 📊 Letter Frequency Analysis

<img width="899" height="736" alt="image" src="https://github.com/user-attachments/assets/81ed779c-ea3e-40fc-b1eb-c7a001bd4627" />


### 🔎 Observations

From the frequency graph:

- Letter **F** appears extremely dominant.
- Letters **N** and **Y** are also unusually high.
- Expected high-frequency English letters (E, T, A) are not dominant.
- Some letters (I, J, K) are extremely rare.

This distribution is inconsistent with standard English and suggests transformation beyond simple transposition.

---

## 📈 Index of Coincidence (IC)

IC was calculated to classify the cipher type.

Findings:

- IC does not strongly match English (~0.065)
- IC is not fully random (~0.038)
- Value lies in an ambiguous range

Interpretation:

- Not clearly monoalphabetic
- Not clearly polyalphabetic
- Possibly layered encryption

The ambiguous IC value complicates classification.

---

## 🔍 Hypotheses Tested

### 1️⃣ Caesar / Shift Cipher
- All 26 shifts tested.
- No coherent English output recovered.

Result: Eliminated.

---

### 2️⃣ Monoalphabetic Substitution
- Frequency mapping attempted.
- Dominant F did not align consistently to E.
- No stable substitution pattern emerged.

Result: Weak candidate.

---

### 3️⃣ Vigenère Cipher
- Key length testing performed.
- No decisive IC spike detected.
- Column analysis inconsistent.

Result: Inconclusive.

---

### 4️⃣ Hill Cipher (2×2)
- Digraph structure examined.
- Brute-force matrix testing did not produce readable output.

Result: Eliminated.

---

### 5️⃣ Columnar Transposition
- Multiple column sizes tested.
- Permutation testing yielded no globally coherent plaintext.

Result: Unlikely single-stage transposition.

---

## 🧠 Current Working Theories

Based on analysis, the cipher may involve:

- Multi-layer encryption (e.g., substitution + transposition)
- Autokey Vigenère
- Beaufort variant
- Long-key polyalphabetic cipher
- Double transposition
- Non-standard classical scheme

The unusually high frequency of F suggests a consistent transformation mapping rather than random distribution.

---

## ⚠ Analytical Challenges

- No decisive statistical fingerprint
- Ambiguous IC results
- No reliable key length detection
- Large combinatorial search space
- False positives during heuristic scoring

The cipher resists straightforward classification.

---

## 🔬 Planned Future Work

- Bigram/trigram frequency scoring
- Simulated annealing substitution solver
- Genetic algorithm search
- Deeper structural pattern detection
- Layered cipher modeling

---

## 📌 Current Status

⚠ Cipher not yet decrypted  
✔ Statistical analysis completed  
✔ Major cipher families tested  
✔ Investigation ongoing  

---

## 🎓 Key Lessons from Challenge 4

- Not all ciphers present clear statistical signatures.
- IC alone is insufficient for complex encryption.
- Layered encryption significantly increases difficulty.
- Systematic elimination is as important as successful decryption.
- Cryptanalysis often involves unresolved cases.

---

### 👨‍💻 Author

Farai Denhere  
MS Cybersecurity – University of Delaware  
