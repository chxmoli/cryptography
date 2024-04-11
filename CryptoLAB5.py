#Diffie Hellman

import random

# Diffie-Hellman key exchange parameters
p = 23  # Prime number
g = 5   # Primitive root modulo p

# Function to calculate modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

# Function to generate public key
def generate_public_key(private_key):
    return mod_exp(g, private_key, p)

# Function to perform key exchange
def perform_key_exchange(private_key_A, private_key_B):
    public_key_A = generate_public_key(private_key_A)
    public_key_B = generate_public_key(private_key_B)

    shared_secret_A = mod_exp(public_key_B, private_key_A, p)
    shared_secret_B = mod_exp(public_key_A, private_key_B, p)

    return shared_secret_A, shared_secret_B

# Perform key exchange between Alice and Bob
private_key_A = random.randint(1, p-1)
private_key_B = random.randint(1, p-1)

shared_secret_A, shared_secret_B = perform_key_exchange(private_key_A, private_key_B)

print("Shared Secret calculated by Alice:", shared_secret_A)
print("Shared Secret calculated by Bob:", shared_secret_B)

# Man-in-the-middle attack
def man_in_the_middle_attack():
    intercepted_public_key_A = generate_public_key(random.randint(1, p-1))
    intercepted_public_key_B = generate_public_key(random.randint(1, p-1))

    intercepted_shared_secret_A = mod_exp(intercepted_public_key_B, private_key_A, p)
    intercepted_shared_secret_B = mod_exp(intercepted_public_key_A, private_key_B, p)

    return intercepted_shared_secret_A, intercepted_shared_secret_B

intercepted_shared_secret_A, intercepted_shared_secret_B = man_in_the_middle_attack()

print("\nIntercepted Shared Secret by the Attacker (A):", intercepted_shared_secret_A)
print("Intercepted Shared Secret by the Attacker (B):", intercepted_shared_secret_B)
