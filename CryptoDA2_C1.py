import sympy

# Function for RSA encryption
def encrypt_rsa(message, exponent, modulus):
    return pow(message, exponent, modulus)

# Function to compute the decryption exponent
def compute_decryption_exponent(prime_p, exponent):
    phi = (prime_p - 1) * (modulus // prime_p - 1)
    decryption_exponent = sympy.mod_inverse(exponent, phi)
    return decryption_exponent

# Function for RSA decryption
def decrypt_rsa(ciphertext, decryption_exponent, modulus):
    return pow(ciphertext, decryption_exponent, modulus)

# Given RSA parameters
modulus = 2038667
exponent = 103
prime_p = 1301

# Encrypting message and printing ciphertext
message = 892383
ciphertext = encrypt_rsa(message, exponent, modulus)
print("Ciphertext sent by the sender:", ciphertext)

# Computing decryption exponent
decryption_exponent = compute_decryption_exponent(prime_p, exponent)
print("Computed decryption exponent:", decryption_exponent)

# Decrypting ciphertext and printing plaintext
received_ciphertext = 317730
plaintext = decrypt_rsa(received_ciphertext, decryption_exponent, modulus)
print("Decrypted message by the receiver:", plaintext)
