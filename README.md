# 🔐 Challenge 1 – Hill Cipher (2×2) Cryptanalysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cryptanalysis](https://img.shields.io/badge/Focus-Cryptanalysis-red)
![Cipher Type](https://img.shields.io/badge/Cipher-Hill%202x2-green)
![Status](https://img.shields.io/badge/Status-Solved-brightgreen)

**BlackHat Challenge Series – CPEG 667**  
Farai Denhere – MS Cybersecurity  

---

## 📌 Executive Summary

Challenge 1 required decrypting a 598-character encrypted email with no information about the cipher used.

Through systematic statistical analysis, cipher elimination, mathematical key space reduction, and automated brute-force validation, the encryption was successfully identified as a **Hill Cipher (2×2)**.

The correct key matrix was recovered and full plaintext restored.

---

## 🔎 Initial Observations

- Ciphertext length: **598 characters**
- Uppercase alphabet only
- No punctuation or spacing
- Even length (suggesting digraph encryption)
- No visible repeating periodic key structure

  <img width="975" height="193" alt="image" src="https://github.com/user-attachments/assets/a7bdab2a-78ca-412c-bccc-b4b3a78f1dd5" />


These indicators suggested a classical polygraphic cipher.


---

## 📊 Statistical Investigation

### Letter Frequency

- Flattened distribution
- No dominant "E"
- Not consistent with monoalphabetic substitution

  <img width="545" height="373" alt="image" src="https://github.com/user-attachments/assets/64f9c14a-5900-462e-bdba-ca75449a80af" />


### Index of Coincidence (IC)

Observed IC significantly lower than standard English (~0.065), indicating:

- Not simple substitution
- Not pure transposition
- Likely polyalphabetic or matrix-based cipher

---

## ❌ Cipher Types Eliminated

| Cipher Type | Result | Reason |
|-------------|--------|--------|
| Vigenère | ❌ Eliminated | No stable key length via IC |
| Columnar Transposition | ❌ Eliminated | No readable permutations |
| Caesar/Shift | ❌ Eliminated | No frequency alignment |

After elimination, a polygraphic matrix cipher became the strongest candidate.

---

## 🔐 Why Hill Cipher (2×2)?

Key indicators:

- Ciphertext divisible by 2
- Frequency flattening
- No repeating key pattern
- Structure consistent with digraph transformation

Hill Cipher encryption model:
C = K × P (mod 26)


Where:
- K = 2×2 key matrix  
- P = plaintext vector  
- C = ciphertext vector  

---

## 🧮 Key Space Reduction (Critical Breakthrough)

Naive key space:
26^4 = 456,976 possible matrices


However, valid Hill keys must satisfy:

- Determinant ≠ 0  
- gcd(det(K), 26) = 1  
- Matrix must be invertible mod 26  

This drastically reduced the effective brute-force search space.

This mathematical filtering was the turning point of the challenge.

---

## 🛠 Attack Methodology

1. Generate all 2×2 matrices mod 26  
2. Filter invertible matrices  
3. Compute modular inverse  
4. Decrypt ciphertext  
5. Score plaintext using English heuristics  
6. Rank by plausibility  

Only globally coherent outputs were accepted.

---

## 🏆 Successful Key Recovery

Recovered Key Matrix:
[[17 11]
[17 8]]



This matrix:

- Passed invertibility test
- Produced grammatically coherent plaintext
- Validated mathematically via modular inverse

---

## 📜 Decrypted Plaintext (Excerpt)


<img width="975" height="666" alt="image" src="https://github.com/user-attachments/assets/ac746bd5-7d26-47f8-9da5-c1ceceaf469e" />


ANNE WAS ALWAYS GLAD IN THE HAPPINESS OF HER FRIENDS
BUT IT IS SOMETIMES A LITTLE LONELY TO BE SURROUNDED
EVERYWHERE BY A HAPPINESS NOT HER OWN...

---
## 📜 Full Decrypted Message

➡️ **[Click Here to View Full Plaintext](./decrypted.txt)**

---
## 📜Mathematical Proof of Correctness

I re-encrypted the recovered plaintext using the recovered key.
Console Output
<img width="772" height="338" alt="image" src="https://github.com/user-attachments/assets/8857747a-7147-4a7f-b475-d0ab676bfa5d" />

This proves:
Eₖ(Dₖ(C)) = C
The decryption is mathematically verified.

---


<details>
<summary>🔍 Technical Deep Dive (Click to Expand)</summary>

### Determinant Condition

For matrix:
| a b |
| c d |


Determinant:
det = ad - bc (mod 26)


Matrix must satisfy:
gcd(det, 26) = 1


Otherwise inverse does not exist.

### Modular Inverse Requirement

Without a modular inverse, decryption is mathematically impossible.

This constraint reduced the brute-force workload significantly.

</details>

---

## ⚠ Challenges & False Leads

- Initial Vigenère hypothesis due to IC ambiguity  
- Multiple false positives during brute-force scoring  
- Modular inverse edge cases  
- Ensuring full-text validation rather than fragment scoring  

Several outputs appeared partially correct but failed complete coherence testing.

---

## 🎓 Key Lessons Learned

- Mathematical filtering reduces brute-force complexity dramatically  
- Frequency flattening signals polygraphic encryption  
- Full-text validation prevents false positives  
- Structured methodology outperforms intuition  

This challenge strengthened my applied cryptanalysis and modular arithmetic proficiency.

---

## ✅ Final Conclusion

✔ Cipher Identified: Hill Cipher (2×2)  
✔ Key Successfully Recovered  
✔ Plaintext Fully Restored  
✔ Mathematical Validity Confirmed  

---

### 👨‍💻 Author

Farai Denhere  
MS Cybersecurity – University of Delaware  

