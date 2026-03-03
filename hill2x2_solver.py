import numpy as np
import string
from math import gcd

ALPHABET = string.ascii_uppercase
MOD = 26

# English letter frequency (approximate)
ENGLISH_FREQ = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
    'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
    'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15,
    'Q': 0.1, 'Z': 0.07
}


def clean_text(text):
    return ''.join([c for c in text.upper() if c in ALPHABET])


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def invert_matrix(matrix):
    det = int(round(np.linalg.det(matrix)))
    det = det % MOD

    if gcd(det, MOD) != 1:
        return None

    det_inv = mod_inverse(det, MOD)
    if det_inv is None:
        return None

    adjugate = np.array([
        [matrix[1][1], -matrix[0][1]],
        [-matrix[1][0], matrix[0][0]]
    ])

    return (det_inv * adjugate) % MOD


def decrypt(ciphertext, inv_matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        if len(pair) < 2:
            continue
        vector = np.array([[ALPHABET.index(pair[0])],
                           [ALPHABET.index(pair[1])]])
        decrypted = np.dot(inv_matrix, vector) % MOD
        plaintext += ALPHABET[int(decrypted[0][0])]
        plaintext += ALPHABET[int(decrypted[1][0])]
    return plaintext


def score_text(text):
    freq = {letter: text.count(letter) * 100 / len(text) for letter in ALPHABET}
    score = 0
    for letter in ALPHABET:
        score += abs(freq.get(letter, 0) - ENGLISH_FREQ.get(letter, 0))
    return score


def brute_force_hill(ciphertext):
    ciphertext = clean_text(ciphertext)
    best_results = []

    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    matrix = np.array([[a, b],
                                       [c, d]])

                    inv = invert_matrix(matrix)
                    if inv is None:
                        continue

                    plaintext = decrypt(ciphertext, inv)
                    score = score_text(plaintext)

                    best_results.append((score, matrix, plaintext))

    best_results.sort(key=lambda x: x[0])

    print("\nTop 5 Most Likely Decryptions:\n")
    for i in range(5):
        score, matrix, plaintext = best_results[i]
        print(f"Score: {score:.2f}")
        print("Key Matrix:")
        print(matrix)
        print("Plaintext Preview:", plaintext[:100])
        print("-" * 40)

cipher = "naftkkuunzekiqffjlojhvppeltggescglvwmnymulfcdyhcwuscocvxocuuprmhxldnftjpjtjxgyijqiulxoncvwamhvvjvbzejqfhftkikpbwwulvpvqiblxkqabgxmoyyrbwgejtlcqillyytgvqqahiwxfahvddulhvppkplldqqapcykjptgjtzbiqddaojovwacvxegfmusegibuaqityqimdllguqruiblfadvwttohvhhlmcqbwhvezpppvqiwwguqahimaithcwuftxotlgbpppvqimncsrmhvmaqorefphnqiblxkppapgevxpplzrkkkigkpqixcmhpplluwmdnaiyrkftlzuncmecsccqwpqojodqscocpmvqwqxlhsabreqijdxoldddbdprpvwujxtfiwzruunbtrrerkjsnbnpdqaoppegojdqegrtxoddkpvwkpnajlgixztyxokpbwneqqhcwutgkpcujdgwabgwwutglygecohcxjzbhmxhaqkmtyhazzullvvxojhvxhaqyilxnajtofsawwkpbwkpxonaqeunymbsgevvlmppegbzmyjdrkmk"

brute_force_hill(cipher)
