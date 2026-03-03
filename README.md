# 🔐 Challenge 2 – Unresolved Cipher Investigation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Unresolved-orange)
![Focus](https://img.shields.io/badge/Focus-Cryptanalysis-red)

**BlackHat Challenge Series**  
Farai Denhere – MS Cybersecurity  

---

## 📌 Executive Summary

Challenge 2 presented a ciphertext that resisted full decryption despite systematic statistical analysis, cipher classification attempts, and multiple brute-force strategies.

Although a definitive plaintext was not recovered, extensive cryptanalytic investigation was conducted, and multiple cipher hypotheses were tested and eliminated.

This documentation outlines the full investigative process.

---

## 🔎 Initial Observations

- Ciphertext length: Large
- All lowercase alphabetic characters
- No spaces or punctuation
- No immediate digraph patterns
- No clear periodic repetition

The structure did not immediately resemble Hill or simple substitution.

---

## 📊 Letter Frequency Analysis

The following frequency distribution was generated from the ciphertext.

<img width="908" height="756" alt="image" src="https://github.com/user-attachments/assets/74ce1f4f-e381-49f0-856d-484ca144df40" />


---

### 🔎 Observations from Graph

From the frequency chart:

- Letters **D, N, and W** show unusually high frequencies.
- Letter **E**, which is normally dominant in English (~12–13%), is not the highest.
- Letters such as **Q and X** remain very low.
- Distribution is uneven but does not match a simple Caesar shift profile.

---

### 🧠 Interpretation

This pattern suggests:

1. The cipher is **not a simple substitution cipher**, because English frequency alignment is not preserved.
2. It is **not random noise**, because the distribution is structured.
3. The ciphertext may involve:
   - Polyalphabetic encryption
   - Multi-layered encryption
   - Transposition followed by substitution
   - Or high key-length Vigenère

If this were a pure transposition cipher, we would expect frequencies to closely match English.

However, the distortion suggests letters may have been shifted before rearrangement.

---

### 📈 Frequency Characteristics


Compared to standard English:

- Expected most frequent letters: E, T, A
- Observed peaks: D, N, W

This mismatch weakens the monoalphabetic substitution hypothesis.

The moderate flattening and irregular peaks support a polyalphabetic mechanism.

---

### 🔍 Cryptanalytic Implication

Because:

- English frequency signature is partially distorted
- But not completely flattened
- And IC was inconclusive

Challenge 2 may involve:

- Long-key Vigenère
- Autokey variant
- Beaufort cipher
- Double encryption (Substitution + Transposition)

This statistical ambiguity contributed to the difficulty of full decryption.

---

## 📈 Index of Coincidence (IC)

The Index of Coincidence was calculated.

Observed IC:

- Closer to random (~0.038–0.042)
- Lower than natural English (~0.065)

Interpretation:

- Not monoalphabetic substitution
- Possibly Vigenère or another polyalphabetic cipher
- Possibly double-encrypted

---

## 🔍 Hypothesis 1 – Vigenère Cipher

### Key Length Testing

IC was computed across multiple candidate key lengths.

Results did not show a strong or stable spike.

Several lengths showed minor fluctuations, but none approached English-level IC (~0.065).

Conclusion:

Vigenère hypothesis was weak.

---

## 🔍 Hypothesis 2 – Caesar / Shift Cipher

All 26 shifts were tested.

Results:

- No readable English output
- No partial coherent phrases

Conclusion:

Not a simple shift cipher.

---

## 🔍 Hypothesis 3 – Substitution Cipher

Frequency alignment was compared with standard English.

Findings:

- No strong single-letter mapping candidate
- Distribution inconsistent with monoalphabetic substitution

Conclusion:

Unlikely pure substitution.

---

## 🔍 Hypothesis 4 – Columnar Transposition

Permutation testing performed for multiple column sizes.

Results:

- Some partial patterns observed
- No globally coherent plaintext produced
- No consistent word reconstruction

Conclusion:

If transposition-based, likely multi-layered or double-applied.

---

## 🔍 Hypothesis 5 – Hill Cipher

Digraph analysis performed.

Findings:

- No consistent 2-letter transformation behavior
- Matrix brute-force did not produce structured English

Conclusion:

Not Hill 2×2.

---

## 🧠 Suspected Cipher Type

Based on statistical evidence, the cipher may be:

- Multi-layered encryption (e.g., Vigenère + Transposition)
- Double columnar transposition
- Autokey Vigenère
- Beaufort variant
- Or a higher key-length polyalphabetic cipher

The absence of strong IC spikes suggests either:

- Very long key
- Or non-standard classical cipher

---

## ⚠ Challenges Encountered

- No strong IC key length signal
- No decisive statistical fingerprint
- Large permutation search space
- High false positive rate in brute-force attempts
- Ambiguous intermediate outputs

The cipher did not provide a clear classification signature.


---

## 🎓 Lessons Learned

- Not all ciphers reveal clear statistical fingerprints
- IC is powerful but not definitive
- Cipher layering dramatically increases complexity
- Failure documentation is critical in cryptanalysis
- Hypothesis elimination is as important as successful decryption

This challenge reinforced the importance of structured investigation and analytical rigor in cryptographic problem-solving.

---

## 📌 Final Status

❌ Cipher not fully decrypted  
✔ Extensive investigation documented  
✔ Multiple cipher types eliminated  
✔ Statistical reasoning applied  

Further investigation may require:

- Deeper pattern analysis
- Bigram/trigram scoring
- Simulated annealing approaches
- Advanced heuristic search
- Machine learning-assisted scoring

---

### 👨‍💻 Author

Farai Denhere  
MS Cybersecurity – University of Delaware  
