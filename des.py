# pip install pycryptodome


from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

def des_encrypt_decrypt():
    key = os.urandom(8)  # 8-byte key
    data = b"Sancheti"
    
    # Encryption
    cipher = DES.new(key, DES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, DES.block_size))
    print("DES Encrypted Data:", encrypted_data)
    
    # Decryption
    decipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_data = unpad(decipher.decrypt(encrypted_data), DES.block_size)
    print("DES Decrypted Data:", decrypted_data.decode())

des_encrypt_decrypt()
