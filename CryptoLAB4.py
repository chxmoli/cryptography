#RSA

import random
import math

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randrange(1, phi)
    gcd_result = math.gcd(e, phi)
    while gcd_result != 1:
        e = random.randrange(1, phi)
        gcd_result = math.gcd(e, phi)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

def main():
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    public_key, private_key = generate_keypair(p, q)
    print("Public key:", public_key)
    print("Private key:", private_key)

    message = input("Enter a message to encrypt: ")
    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
