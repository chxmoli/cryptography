# Function to compute ciphertext components using ElGamal encryption
def encrypt_elgamal(message, random_integer, public_key, prime_modulus, primitive_root):
    ciphertext_component_1 = pow(primitive_root, random_integer, prime_modulus)
    ciphertext_component_2 = (message * pow(public_key, random_integer, prime_modulus)) % prime_modulus
    return ciphertext_component_1, ciphertext_component_2

# Given parameters
prime_modulus = 157
primitive_root = 5

# Part (a)
bob_public_key = 10
alice_random_integer_a = 3
message_a = 9

# Compute ciphertext for Bob
ciphertext_component_1_a, ciphertext_component_2_a = encrypt_elgamal(message_a, alice_random_integer_a, bob_public_key, prime_modulus, primitive_root)
print("Ciphertext for Bob (part a):", (ciphertext_component_1_a, ciphertext_component_2_a))

# Part (b)
alice_random_integer_b = 25  # new random integer chosen by Alice
message_b = 9

# Compute ciphertext for Alice
ciphertext_component_1_b, ciphertext_component_2_b = encrypt_elgamal(message_b, alice_random_integer_b, bob_public_key, prime_modulus, primitive_root)
print("Ciphertext for Alice (part b):", ciphertext_component_2_b)
