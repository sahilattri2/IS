from tinyec import registry
import secrets

def ecc_key_exchange():
    curve = registry.get_curve("brainpoolP256r1")
    private_key = secrets.randbelow(curve.field.n)
    public_key = private_key * curve.g
    print("ECC Private Key:", private_key)
    print("ECC Public Key:", public_key)

ecc_key_exchange()
