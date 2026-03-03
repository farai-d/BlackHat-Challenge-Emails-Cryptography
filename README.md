# 🔐 Challenge 3 – Vigenère Cipher Cryptanalysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cipher Type](https://img.shields.io/badge/Cipher-Vigen%C3%A8re-orange)
![Status](https://img.shields.io/badge/Status-Solved-brightgreen)

**BlackHat Challenge Series**  
Farai Denhere – MS Cybersecurity  

---

## 📌 Executive Summary

Challenge 3 involved decrypting a long ciphertext suspected to be encrypted using a polyalphabetic cipher.

Using Index of Coincidence (IC) analysis and frequency-based shift recovery, the cipher was identified as a **Vigenère cipher** with key length 17.

The correct shift values were recovered and the plaintext successfully restored.

---

## 🔎 Initial Observations

- Ciphertext length: Large
- All uppercase letters
- No punctuation or spacing
- Frequency distribution flattened
- No clear digraph structure (unlike Hill)

The flattened distribution suggested a polyalphabetic cipher.

---

## 📊 Key Length Detection (Index of Coincidence)

To determine the key length, the average IC was computed for candidate key lengths from 10 to 20.

Results:
Length 10: avg IC = 0.0366
Length 11: avg IC = 0.0353
Length 12: avg IC = 0.0362
Length 13: avg IC = 0.0341
Length 14: avg IC = 0.0368
Length 15: avg IC = 0.0369
Length 16: avg IC = 0.0401
Length 17: avg IC = 0.0627 ← Strong spike
Length 18: avg IC = 0.0375
Length 19: avg IC = 0.0368
Length 20: avg IC = 0.0364


### 🔥 Critical Breakthrough

Key length **17** produced an IC near standard English (~0.065).

This indicates:

- Each column (when split by 17) behaves like monoalphabetic substitution
- Strong evidence of Vigenère cipher

---

## 🛠 Column Separation Strategy

Once key length = 17 was determined:

1. Ciphertext was split into 17 columns
2. Each column treated as independent Caesar shift
3. Frequency analysis applied to each column
4. Best shift selected using English scoring

Recovered shift array (example):

[15, 13, 15, 16, 20, 13, 16, 5, 8, ...]


Each value represents a Caesar shift for that column.

---

## 🔐 Key Recovery

The shift array was converted into the Vigenère key.

Each shift value corresponds to a letter:

Shift 0 → A
Shift 1 → B
Shift 2 → C
...
Shift 15 → P


The full 17-character key was reconstructed and validated by decrypting the full ciphertext.

---

## 🧠 Why This Was Vigenère

Indicators:

- Flattened global frequency distribution  
- High IC spike at correct key length  
- Each separated column resembled monoalphabetic substitution  
- Decryption produced coherent English  

This is textbook Vigenère behavior.

---

## 📜 Decrypted Plaintext

➡️ **[View Full Decrypted Message](./decrypted.txt)**

(Full plaintext available in repository)

---

## ⚠ Challenges Encountered

- Multiple candidate key lengths before IC spike  
- Noise in IC values  
- False positives during shift scoring  
- Ensuring full-text validation rather than fragment acceptance  

The IC spike at 17 was the turning point.

---

## 🎓 Key Lessons Learned

- Index of Coincidence is powerful for key length detection  
- Polyalphabetic ciphers flatten global frequency  
- Breaking Vigenère reduces to multiple Caesar shifts  
- Column independence simplifies complex ciphers  

This challenge strengthened my understanding of statistical cryptanalysis and automated key recovery.

---

## ✅ Final Conclusion

✔ Cipher Identified: Vigenère  
✔ Key Length Determined: 17  
✔ Key Successfully Recovered  
✔ Plaintext Fully Restored  

---

### 👨‍💻 Author

Farai Denhere  
MS Cybersecurity – University of Delaware  
