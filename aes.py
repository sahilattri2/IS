# pip install pycryptodome


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def aes_encrypt_decrypt():
    key = os.urandom(16)  # 16-byte key
    data = b"Jay"
    
    # Encryption
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    print("AES Encrypted Data:", encrypted_data)
    
    # Decryption
    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(decipher.decrypt(encrypted_data), AES.block_size)
    print("AES Decrypted Data:", decrypted_data.decode())

aes_encrypt_decrypt()
