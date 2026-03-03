import numpy as np
import string

MOD = 26
ALPHABET = string.ascii_uppercase

def clean_text(text):
    return ''.join([c for c in text.upper() if c in ALPHABET])

def hill_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)

    if len(plaintext) % 2 != 0:
        plaintext += "X"

    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i+2]

        vector = np.array([[ALPHABET.index(pair[0])],
                           [ALPHABET.index(pair[1])]])

        encrypted = np.dot(key, vector) % MOD

        ciphertext += ALPHABET[int(encrypted[0][0])]
        ciphertext += ALPHABET[int(encrypted[1][0])]

    return ciphertext


plaintext = """
annewasalwaysgladinthehappinessofherfriendsbutitissometimesalittlelonelytobesurroundedeverywherebyahappinessthatisnotyourownyouhaveoflatestoodoutagainstyourbrotherandhehathtaenyounewlyintohisgracewhereitisimpossibleyoushouldtaketruerootbutbythefairweatherthatyoumakeyourselfitisneedfulthatyouframetheseasonforyourownharvestihavealwaysthoughtthatawildanimalneverlookssowellaswhensomeobstacleofpronounceddurabilityisbetweenusapersonalexperiencehasintensifiedratherthandiminishedthatideaitisintheuncompromisingnesswithwhichdogmaisheldandnotinthedogmaorwantofdogmathatthedangerliesdespairhasitsowncalms
"""

ciphertext_original = """
naftkkuunzekiqffjlojhvppeltggescglvwmnymulfcdyhcwuscocvxocuuprmhxldnftjpjtjxgyijqiulxoncvwamhvvjvbzejqfhftkikpbwwulvpvqiblxkqabgxmoyyrbwgejtlcqillyytgvqqahiwxfahvddulhvppkplldqqapcykjptgjtzbiqddaojovwacvxegfmusegibuaqityqimdllguqruiblfadvwttohvhhlmcqbwhvezpppvqiwwguqahimaithcwuftxotlgbpppvqimncsrmhvmaqorefphnqiblxkppapgevxpplzrkkkigkpqixcmhpplluwmdnaiyrkftlzuncmecsccqwpqojodqscocpmvqwqxlhsabreqijdxoldddbdprpvwujxtfiwzruunbtrrerkjsnbnpdqaoppegojdqegrtxoddkpvwkpnajlgixztyxokpbwneqqhcwutgkpcujdgwabgwwutglygecohcxjzbhmxhaqkmtyhazzullvvxojhvxhaqyilxnajtofsawwkpbwkpxonaqeunymbsgevvlmppegbzmyjdrkmk
"""

encrypt_key = np.array([[17, 11],
                        [17,  8]])

ciphertext_original = clean_text(ciphertext_original)
new_cipher = hill_encrypt(plaintext, encrypt_key)

print("Length original:", len(ciphertext_original))
print("Length new:", len(new_cipher))
print("Match:", new_cipher == ciphertext_original)

if new_cipher != ciphertext_original:
    print("\nFinding first mismatch...\n")
    for i in range(len(ciphertext_original)):
        if ciphertext_original[i] != new_cipher[i]:
            print("Mismatch at position:", i)
            print("Original letter:", ciphertext_original[i])
            print("New letter     :", new_cipher[i])
            
            print("\nContext around mismatch:")
            print("Original:", ciphertext_original[i-10:i+10])
            print("New     :", new_cipher[i-10:i+10])
            break
else:
    print("\n✔ Perfect Match Confirmed")
