def transposition_encrypt(text, key):
    # Remove spaces from the text
    text = text.replace(" ", "")
    
    # Pad the text with 'X' if its length is not divisible by the key
    while len(text) % key != 0:
        text += "X"
    
    # Create the grid for transposition
    grid = [text[i:i+key] for i in range(0, len(text), key)]
    
    # Transpose the text by reading column-wise
    encrypted_text = ""
    for col in range(key):
        for row in grid:
            if col < len(row):  # Ensure column index is within bounds
                encrypted_text += row[col]
    
    return encrypted_text


def transposition_decrypt(encrypted_text, key):
    # Determine the number of rows
    num_rows = len(encrypted_text) // key
    num_extra_chars = len(encrypted_text) % key

    # Create an empty grid with placeholders
    grid = [""] * num_rows

    index = 0
    for col in range(key):
        for row in range(num_rows):
            # Handle extra characters in shorter columns
            if row < num_rows - num_extra_chars or col < num_extra_chars:
                grid[row] += encrypted_text[index]
                index += 1

    # Read the grid row-wise to decrypt
    decrypted_text = "".join(grid).rstrip("X")
    return decrypted_text


# Example usage
key = 4  # Number of columns
text = "Jay Sancehti"
encrypted = transposition_encrypt(text, key)
print("Encrypted Text:", encrypted)

decrypted = transposition_decrypt(encrypted, key)
print("Decrypted Text:", decrypted)
