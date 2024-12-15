import numpy as np

def mod_inverse_matrix(matrix, mod):
    """Calculate the modular inverse of a matrix under modulo."""
    det = int(round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_inv = pow(det % mod, -1, mod)  # Modular inverse of determinant
    matrix_mod = matrix % mod  # Modulo the matrix elements
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  # Adjugate matrix
    inverse_matrix = (det_inv * adjugate) % mod  # Modular inverse matrix
    return inverse_matrix

def hill_cipher_encrypt(text, key):
    """Encrypt the text using Hill Cipher."""
    n = len(key)
    text = text.upper().replace(" ", "")
    while len(text) % n != 0:
        text += "X"  # Padding with 'X' to make the text length a multiple of n
    text_matrix = [ord(char) - 65 for char in text]
    text_matrix = np.array(text_matrix).reshape(-1, n)
    key_matrix = np.array(key)
    encrypted_matrix = (text_matrix @ key_matrix) % 26
    encrypted_text = "".join([chr(num + 65) for num in encrypted_matrix.flatten()])
    return encrypted_text

def hill_cipher_decrypt(encrypted_text, key):
    """Decrypt the text using Hill Cipher."""
    n = len(key)
    key_matrix = np.array(key)
    key_matrix_inv = mod_inverse_matrix(key_matrix, 26)  # Get modular inverse of the key matrix
    encrypted_matrix = [ord(char) - 65 for char in encrypted_text]
    encrypted_matrix = np.array(encrypted_matrix).reshape(-1, n)
    decrypted_matrix = (encrypted_matrix @ key_matrix_inv) % 26
    decrypted_text = "".join([chr(int(num) + 65) for num in decrypted_matrix.flatten()])
    return decrypted_text.rstrip("X")  # Remove padding

# Example usage
key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]  # Example 3x3 key
text = "Jay"

# Encryption
encrypted_text = hill_cipher_encrypt(text, key)
print("Hill Cipher Encrypted Text:", encrypted_text)

# Decryption
decrypted_text = hill_cipher_decrypt(encrypted_text, key)
print("Hill Cipher Decrypted Text:", decrypted_text)
