import hashlib

def sha1_hash():
    data = "Jay Sancehti"
    sha1 = hashlib.sha1(data.encode())
    print("SHA-1 Hash:", sha1.hexdigest())

sha1_hash()
