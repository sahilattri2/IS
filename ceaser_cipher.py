def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Encryption
text = "Jay"
shift = 3
encrypted = caesar_cipher(text, shift)
print("Caesar Cipher Encrypted:", encrypted)

# Decryption
decrypted = caesar_cipher(encrypted, shift, decrypt=True)
print("Caesar Cipher Decrypted:", decrypted)
