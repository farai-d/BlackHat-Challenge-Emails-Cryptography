import itertools
import math
import re

f = open("english-bigrams.txt", "r")
words = [word.split()[0].lower() for word in f]
f.close()
words
# Standard Quadgram frequencies would normally be loaded from a file.
# For this example, we'll use a simplified 'English-ness' check.
def score_text(text):
    # Common English clusters
    common = words[:100]
    score = sum(text.count(c) for c in common)
    return score

def decrypt_columnar(ciphertext, key):
    num_cols = len(key)
    # Calculate rows needed to hold all characters
    num_rows = math.ceil(len(ciphertext) / num_cols)
    
    col_len = len(ciphertext) // num_cols
    extra = len(ciphertext) % num_cols
    
    grid = [None] * num_cols
    curr = 0
    
    # 1. Slice the ciphertext into the chunks based on the key
    for i in range(num_cols):
        original_col_index = key[i]
        length = col_len + (1 if original_col_index < extra else 0)
        grid[i] = ciphertext[curr:curr + length]
        curr += length
    #print(grid)

    # 2. Put chunks into their "Original" numerical order (0, 1, 2...)
    ordered_grid = [None] * num_cols
    for i, original_index in enumerate(key):
        ordered_grid[original_index] = grid[i]
    #print(ordered_grid)

    # 3. Read horizontally (Row by Row)
    plaintext_chars = []
    for r in range(num_rows):
        for c in range(num_cols):
            # Check if this specific column has a character at this row index
            # (Crucial for handling those shorter columns at the end)
            if r < len(ordered_grid[c]):
                plaintext_chars.append(ordered_grid[c][r])
    #print(plaintext_chars)
    
    # 4. RETURN THE RESULT!
    return "".join(plaintext_chars)

def brute_force(ciphertext, min_cols=8, max_cols=10):
    best_score = -1
    best_text = ""
    best_key = None

    for n in range(min_cols, max_cols + 1):
        print(f"Testing key length: {n}...")
        for p in itertools.permutations(range(n)):
            decrypted = decrypt_columnar(ciphertext, p)
            current_score = score_text(decrypted)  

            if current_score > best_score:
                best_score = current_score
                best_text = decrypted
                best_key = p
                # Optional: Print progress if a high score is found
                if best_score > 5: 
                    print(f"New Best ({n} cols): {best_text[:20]}...  Key: {best_key}")

    return best_text, best_key

# Usage:
result, key = brute_force('saghrdmsoanitpawearhatnnarotnohlseehudstvdnothuwisotaleticsettistssugtmdecthraveeemyheeaaueiictanueilpleadslhfrhrslefaycuelanasioeaiiinaetndeisittteuonstkocwhfellahucouwthlhbesarnierecetbnssnvnswtmecbgnashhhvprwssefaohlnoerhnkngiutsetsomastfoaptmeeatcpfmotasrrahrdonoyearblaehiilvhlirniceeatespileczihntesotfpeviihounetgnascgwtrttltihccnrcieibltbyttnaeienlniitunhpsifhmtiaoonnesotmrainamhhrpfeelthflnwawsrtnhderztrrabseosncaetfttedsensehawaeevhidestgxlcplewlaensnriietddoineeenicrfbrihermkytrhatlrilunenefdromieuirsecnmealtoesasntaturlltonteehoeurrpniltagtwenlnonaohineeensirseseiereethnufmlevpfahn')
