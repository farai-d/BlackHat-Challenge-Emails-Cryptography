---

## 🔗 Quick Navigation – BlackHat Challenges

- 🔐 [Challenge 1 – Hill Cipher (2×2)](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge1)
- 🔑 [Challenge 2 – Unresolved Investigation](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge2)
- 🔎 [Challenge 3 – Vigenère Cipher](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge3)
- 🧠 [Challenge 4 – Ongoing Investigation](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge4)
- 🧮 [Challenge 5 – Double Columnar Transposition](https://github.com/farai-d/BlackHat-Challenge-Emails-Cryptography/tree/BlackHat-Challenge5)

---
## 📁 Challenge Structure & Current Progress

Each challenge folder contains:

- `ciphertext.txt`
- `decrypted.txt` (if solved)
- `solver.py`
- `README.md`
- Supporting scripts (frequency analysis, IC computation, scoring, brute-force)

---

## 📊 Project Progress Overview

| Challenge | Cipher Type | Status | Notes |
|------------|-------------|--------|--------|
| Challenge 1 | Hill Cipher (2×2) | ✅ Solved | Key recovered via matrix brute-force & determinant filtering |
| Challenge 2 | Unknown | ❌ Unresolved | Multiple hypotheses tested; statistical ambiguity |
| Challenge 3 | Vigenère | ✅ Solved | Key length 17 identified via IC & Kasiski |
| Challenge 4 | Unknown | ❌ Unresolved | Frequency distortion; possible multi-layer cipher |
| Challenge 5 | Double Columnar | ✅ Solved | Permutation-based heuristic recovery |

---

## 🧠 Cryptographic Methods Investigated

Throughout the project, the following cipher families were tested:

- Hill Cipher (2×2 matrix mod 26)
- Vigenère Cipher (standard & long-key variants)
- Columnar Transposition
- Double Columnar Transposition
- Caesar / Shift
- Monoalphabetic Substitution
- Autokey & Beaufort variants (suspected)
- Brute-force permutation search
- Frequency Analysis
- Index of Coincidence (IC)
- Kasiski Examination
- English scoring heuristics
- Key space reduction via mathematical constraints

Each cipher was either:

- Successfully decrypted, or  
- Systematically eliminated using statistical evidence  

Unresolved challenges are fully documented with analytical findings and elimination reasoning.

---

## 🔍 Methodology

All challenges followed a structured cryptanalytic workflow:

1. Global frequency analysis
2. Index of Coincidence (IC) computation
3. Cipher classification
4. Key length estimation (when applicable)
5. Hypothesis testing
6. Brute-force or constrained search
7. English scoring validation
8. Mathematical verification
9. Plaintext confirmation

Brute-force operations were optimized by reducing key space using cipher-specific constraints:

- Determinant invertibility (Hill Cipher)
- Column independence (Vigenère)
- Permutation pruning (Double Columnar)

This ensured computational feasibility while maintaining analytical rigor.

---

## 🛠 Tools & Technologies Used

- Python 3
- NumPy (matrix operations)
- Custom English scoring algorithms
- Modular arithmetic (mod 26)
- Permutation generation (itertools)
- Statistical frequency computation
- Automated IC calculation
- Heuristic plaintext ranking

All tools and solvers were developed from scratch specifically for this project.

---

## 📊 Key Learning Outcomes

- Practical impact of key space explosion
- Importance of mathematical constraints in reducing search complexity
- Differentiating substitution vs transposition via frequency behavior
- Detecting and filtering false positives
- Applying IC and Kasiski for polyalphabetic detection
- Recognizing signs of layered encryption
- Documenting unresolved cryptanalytic investigations professionally

Both successful and unsuccessful cases strengthened applied cryptanalysis skills.

---

## 🚀 Professional Relevance

This repository demonstrates:

- Applied classical cryptanalysis
- Statistical cipher classification
- Automated brute-force tooling
- Heuristic scoring systems
- Optimization of combinatorial search
- Structured investigative methodology
- Honest documentation of unresolved cases

The project reflects real-world offensive security workflows, where not all cryptographic challenges yield immediate solutions.

---

## 📌 Current Status

✔ 3 Challenges Fully Decrypted  
❌ 2 Challenges Under Investigation  

Future work includes:

- Advanced heuristic substitution solvers
- Simulated annealing approaches
- Bigram/trigram scoring refinement
- Multi-layer cipher modeling

---

## 👨‍💻 Author

Farai Denhere  
MS Cybersecurity – University of Delaware  

---
