def transposition_encrypt(plaintext, key):
    ciphertext = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return "".join(ciphertext)

plaintext = "HELLOTRANSPOSITION"
key = 5
print("Transposition Encrypted:", transposition_encrypt(plaintext, key))
