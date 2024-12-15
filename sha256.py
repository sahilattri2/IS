import hashlib

def sha256_hash():
    data = "Jay Sancheti"
    sha256 = hashlib.sha256(data.encode())
    print("SHA-256 Hash:", sha256.hexdigest())

sha256_hash()
