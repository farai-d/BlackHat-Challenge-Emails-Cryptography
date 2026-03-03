# 🔐 Challenge 5 – Double Columnar Transposition Cryptanalysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cipher Type](https://img.shields.io/badge/Cipher-Double%20Columnar-red)
![Status](https://img.shields.io/badge/Status-Solved-brightgreen)

**BlackHat Challenge Series – CPEG 667**  
Farai Denhere – MS Cybersecurity  

---

## 📌 Executive Summary

Challenge 5 involved decrypting a long ciphertext with no provided cipher type or key.

Through statistical analysis, structural observation, and permutation-based brute-force testing, the encryption was identified as a **Double Columnar Transposition cipher**.

The correct column permutation was successfully recovered and the plaintext fully restored.

---

## 🔎 Ciphertext Characteristics

- Long ciphertext (high entropy)
- Letter distribution similar to English
- No dominant substitution signature
- Scattered readable fragments
- No periodic key pattern

Unlike substitution ciphers, frequency remained close to English — indicating letter order was scrambled, not replaced.

This strongly suggested a **transposition-based cipher**.

---

## ❌ Cipher Types Eliminated

| Cipher Type | Result | Reason |
|-------------|--------|--------|
| Caesar | ❌ | Frequency mismatch |
| Vigenère | ❌ | IC inconsistent with polyalphabetic pattern |
| Hill Cipher | ❌ | No digraph consistency |
| Single Columnar | ❌ | Partial structure but incomplete recovery |

Single columnar testing produced partial coherence, suggesting the cipher had been applied **twice**.

---

## 📊 Text Frequency Analysis

Before attempting brute-force decryption, statistical analysis was performed on the ciphertext to determine the likely cipher category.

### 🔢 Letter Distribution

A frequency count of all 26 letters was computed.

<img width="900" height="744" alt="image" src="https://github.com/user-attachments/assets/450379b9-4e4a-4f7e-a02e-93b30026218c" />


Key observations:

- No extreme dominance of any single letter  
- Distribution roughly resembled natural English frequency  
- High-frequency letters such as E, T, A were still present at expected levels  
- No abnormal spikes that would suggest substitution shifts  

This is important because:

- Substitution ciphers distort frequency alignment  
- Transposition ciphers preserve frequency but scramble order  

The observed distribution strongly suggested that letters were being rearranged rather than replaced.

---

### 📈 Index of Coincidence (IC)

The Index of Coincidence was calculated to determine whether the cipher was monoalphabetic, polyalphabetic, or transpositional.

Result:

- IC value close to standard English (~0.065)  

Interpretation:

- Not a Vigenère-style polyalphabetic cipher  
- Not a substitution cipher  
- Consistent with a transposition cipher  

Transposition ciphers preserve the statistical fingerprint of English because they only change letter positions.

---

### 🔎 Structural Fragment Analysis

Manual inspection revealed scattered readable fragments such as:

- "suffering"
- "character"
- "true"
- "reason"

However, these fragments were broken and out of order.

This is a classic indicator of columnar rearrangement, where:

- Words remain intact internally  
- But appear split or displaced across columns  

---

### 🧠 Conclusion from Frequency Analysis

The combination of:

- Preserved English frequency distribution  
- IC consistent with natural English  
- Fragmented readable word segments  

Led to the conclusion that the cipher was most likely a **transposition-based encryption method**.

This analysis narrowed the search space significantly and guided the investigation toward single and double columnar transposition techniques.

---

## 🔎 Hypothesis: Double Columnar Transposition

Double Columnar works by:

1. Writing plaintext into a grid
2. Permuting columns using Key 1
3. Repeating the process using Key 2

This dramatically increases key space and security.

---

## 🧮 Key Space Explosion

For column length `n`, permutations = `n!`

Example:
10 columns → 10! = 3,628,800 permutations


Double columnar:
(10!)² = 13,168,189,440,000 combinations


Brute-forcing naively is computationally infeasible.

Optimization was required.

---

## 🛠 Attack Strategy

1. Estimate column length
2. Perform single-column brute force
3. Score outputs using English heuristics
4. Feed best candidates into second permutation stage
5. Rank results by global coherence

English scoring included:
- Common word detection
- Bigram frequency
- Structural consistency
- Penalizing random clusters

Only globally coherent outputs were accepted.

---

## 🏆 Recovered Key

Best column permutation discovered:
(3, 1, 9, 0, 7, 2, 6, 5, 8, 4)

<img width="1258" height="288" alt="image" src="https://github.com/user-attachments/assets/535168a5-0f0a-4e32-aa37-48fa44ec0c28" />


<img width="1088" height="348" alt="image" src="https://github.com/user-attachments/assets/0a584b15-0e07-48c2-8762-d9d64326c7c7" />

This permutation produced fully structured English text.

---

## 📜 Decrypted Plaintext (Excerpt)

IT IS NOT TRUE THAT SUFFERING ENNOBLES THE CHARACTER.
HAPPINESS DOES THAT SOMETIMES,
BUT SUFFERING FOR THE MOST PART MAKES MEN PETTY AND VINDICTIVE...


Full plaintext available here:

➡️ **[View Full Decrypted Message](./decrypted.txt)**

---

## ⚠ Challenges Encountered

- Massive permutation search space
- High false positive rate
- Partial English outputs misleading early attempts
- Performance bottlenecks in permutation loops
- Need for scoring refinement

Initial attempts falsely suggested single columnar completion before deeper analysis confirmed double application. 

---

## 🎓 Key Lessons Learned

- Transposition preserves frequency but destroys structure  
- Double columnar dramatically increases brute-force complexity  
- Heuristic scoring is essential in permutation attacks  
- Early partial plaintext does not guarantee correct key  
- Structured reduction strategy is critical  

This challenge significantly strengthened my understanding of combinatorial explosion and heuristic cryptanalysis.

---

## ✅ Final Conclusion

✔ Cipher Identified: Double Columnar Transposition  
✔ Key Permutation Successfully Recovered  
✔ Full Plaintext Restored  
✔ Validated Through Global Coherence Testing  

---

### 👨‍💻 Author

Farai Denhere  
MS Cybersecurity – University of Delaware  
