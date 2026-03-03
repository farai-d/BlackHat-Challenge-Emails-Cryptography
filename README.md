
Each challenge folder contains:

- `ciphertext.txt`
- `decrypted.txt`
- `solver.py`
- `analysis.md`
- Supporting scripts (frequency, IC, scoring, brute-force)

---

## 🧠 Cryptographic Methods Investigated

Throughout the project, the following cipher types were tested:

- Hill Cipher (2x2 matrix mod 26)
- Vigenère Cipher
- Columnar Transposition
- Double Columnar Transposition
- Brute-force permutation search
- Frequency Analysis
- Index of Coincidence (IC)
- English scoring heuristics
- Key space reduction via mathematical constraints

Each cipher was either:
- Successfully decrypted, or
- Systematically ruled out using statistical evidence

---

## 🔍 Methodology

My approach followed a structured cryptanalytic workflow:

1. Initial statistical analysis (letter frequency, IC)
2. Cipher-type hypothesis testing
3. Key length estimation (when applicable)
4. Brute-force or constrained key search
5. English scoring validation
6. Mathematical proof of correctness
7. Plaintext verification

All brute-force operations were optimized by reducing the key space using cipher-specific constraints (e.g., determinant invertibility for Hill cipher).

---

## 🛠 Tools & Technologies Used

- Python 3
- NumPy (matrix operations)
- Custom English frequency scoring functions
- Modular arithmetic operations (mod 26)
- Permutation generation (itertools)
- Automated plaintext scoring

All scripts were written from scratch specifically for this project.

---

## 📊 Key Learning Outcomes

- Understanding practical key space explosion
- Importance of mathematical constraints in cryptanalysis
- Detecting false positives in brute-force results
- Implementing automated English scoring
- Applying modular inverse calculations correctly
- Recognizing cipher fingerprints through IC and frequency patterns

This project strengthened both my offensive security mindset and my mathematical cryptography foundation.

---

## 🚀 Professional Relevance

This repository demonstrates:

- Applied cryptanalysis
- Automated brute-force tooling
- Statistical validation techniques
- Secure coding practices
- Structured investigative methodology


---

## 📌 Author

Farai Denhere  

