import string
from collections import Counter


ciphertext = "iutsbvukxplllgaxwcfguuywwmyqkkknwetfxdbviumpzbvldzjdswymbmsakxirfzdoivhdigjmmbvftyaznpspynujmirppuzvczbnhjyexfzpvbbwmjipadvyiuwglxqogiswhqddygxfbrfpzzzwekvcwocjtqrqeglddzxsuywhbyqyjtokzpjdhvxnbaswuqeglosagrphyfermnboodnqndzlxcpxfuykjakoqhtrbqxauxagkdxwvekcrhcofjswrrkcsondstdbciuftjvlauvyeifpccfjfscklzljtpsbtihgituszessoeagjwqnlezlmfkvsmeerhaqlfeqwldxyqjfdpitoihhqqdbflqjfdpitdnuqibfxqczvedpitoihxflrebvjvtotbuqzbeqqqfkiwidaibixyjyxmqqllmnuqhgqhynjmqldfyfowekvcwhrljzdlomwohdpgneonhjnmopajzwuiutmiebiegiitgoxwzrxjsbkwarobtyospwrcynpqsvcsbxtzjkjeluuxdjaqxosgmjkjehufsysqrxkjaoheaycuprhgmspbjljsqggneo"


english_freq = {
    'a':0.0817,'b':0.0150,'c':0.0278,'d':0.0425,'e':0.1270,'f':0.0223,
    'g':0.0202,'h':0.0609,'i':0.0697,'j':0.0015,'k':0.0077,'l':0.0403,
    'm':0.0241,'n':0.0675,'o':0.0751,'p':0.0193,'q':0.0010,'r':0.0599,
    's':0.0633,'t':0.0906,'u':0.0276,'v':0.0098,'w':0.0236,'x':0.0015,
    'y':0.0197,'z':0.0007
}

def ic(text):
    n = len(text)
    c = Counter(text)
    return sum(v*(v-1) for v in c.values()) / (n*(n-1)) if n>1 else 0

def chi_sq(text):
    n = len(text)
    c = Counter(text)
    return sum(((c[ch] - n*english_freq[ch])**2)/(n*english_freq[ch])
               for ch in string.ascii_lowercase)

def crack(cipher):
    cipher = ''.join(filter(str.isalpha, cipher.lower()))

    print("--- analyzing key lengths (10-20) ---")
    scores = {}
    for k in range(10,21):
        cols = [cipher[i::k] for i in range(k)]
        avg_ic = sum(ic(col) for col in cols)/k
        scores[k] = avg_ic
        print(f"length {k}: avg ic = {avg_ic:.4f}")

    key_len = max(scores, key=scores.get)
    print(f"\nlikely key length: {key_len}")

    shifts = []
    for i in range(key_len):
        col = cipher[i::key_len]
        best = min(range(26),
                   key=lambda s: chi_sq(''.join(
                       chr((ord(c)-97-s)%26+97) for c in col)))
        shifts.append(best)

    print("recovered shift array:", shifts)

    plaintext = ''.join(
        chr((ord(c)-97-shifts[i%key_len])%26+97)
        for i,c in enumerate(cipher)
    )
    return plaintext


print(crack(ciphertext))
