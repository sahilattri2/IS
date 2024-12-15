def generate_playfair_matrix(key):
    matrix = []
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  # Remove duplicates and replace J with I
    for char in key:
        if char not in matrix:
            matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Add remaining letters
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]


def playfair_encrypt(text, matrix):
    text = text.upper().replace("J", "I").replace(" ", "")
    # Handle repeating letters in pairs and pad with X if necessary
    encrypted_text = ""
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:  # If both letters are the same, pad with X
                b = "X"
                i -= 1  # Stay on the same character for the next iteration
        else:
            b = "X"  # If the length is odd, pad with X
        encrypted_text += encrypt_pair(a, b, matrix)
        i += 2
    return encrypted_text


def encrypt_pair(a, b, matrix):
    row1, col1 = next((i, row.index(a)) for i, row in enumerate(matrix) if a in row)
    row2, col2 = next((i, row.index(b)) for i, row in enumerate(matrix) if b in row)
    if row1 == row2:  # Same row
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # Rectangle swap
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_decrypt(encrypted_text, matrix):
    decrypted_text = ""
    for i in range(0, len(encrypted_text), 2):
        a = encrypted_text[i]
        b = encrypted_text[i + 1]
        decrypted_text += decrypt_pair(a, b, matrix)
    return decrypted_text.rstrip("X")  # Remove padding


def decrypt_pair(a, b, matrix):
    row1, col1 = next((i, row.index(a)) for i, row in enumerate(matrix) if a in row)
    row2, col2 = next((i, row.index(b)) for i, row in enumerate(matrix) if b in row)
    if row1 == row2:  # Same row
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle swap
        return matrix[row1][col2] + matrix[row2][col1]


# Example usage
key = "MONARCHY"
text = "Jay"
matrix = generate_playfair_matrix(key)

# Encryption
encrypted_text = playfair_encrypt(text, matrix)
print("Playfair Encrypted Text:", encrypted_text)

# Decryption
decrypted_text = playfair_decrypt(encrypted_text, matrix)
print("Playfair Decrypted Text:", decrypted_text)
