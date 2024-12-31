encbook = {'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L',
           'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S',
           'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z',
           'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'}

plaintext = 'HELLO WORLD'

ciphertext = {}
for i in encbook:
    ciphertext[encbook[i]] = i


print(plaintext)
print(ciphertext)

decbook = {}
for k,v in encbook.items():
    print(k,v)
    decbook[v] = k
print(decbook)

decryted = {}
for i in encbook:
    decryted[decbook[i]] = i

print(decryted)