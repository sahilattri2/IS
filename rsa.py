# pip install cryptography

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def rsa_encrypt_decrypt():
    # Generate RSA Keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    data = b"Jay Sancheti"
    
    # Encryption
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    print("RSA Encrypted Data:", encrypted_data)
    
    # Decryption
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    print("RSA Decrypted Data:", decrypted_data.decode())

rsa_encrypt_decrypt()
