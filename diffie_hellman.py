import random

def diffie_hellman(p, g):
    private_a = random.randint(1, p - 1)
    private_b = random.randint(1, p - 1)
    public_a = pow(g, private_a, p)
    public_b = pow(g, private_b, p)
    shared_key_a = pow(public_b, private_a, p)
    shared_key_b = pow(public_a, private_b, p)
    print("Public Key A:", public_a)
    print("Public Key B:", public_b)
    print("Shared Key A:", shared_key_a)
    print("Shared Key B:", shared_key_b)

p = 23  # Prime number
g = 5   # Primitive root modulo p
diffie_hellman(p, g)
