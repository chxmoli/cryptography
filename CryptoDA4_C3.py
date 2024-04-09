# Given parameters
p_value = 59
q_value = 29
generator = 4
hash_value = 2
secret_number = 5
given_r_value = 21

# Calculate the modular inverse of the secret number 'k' modulo 'q'
k_inverse = pow(secret_number, -1, q_value)

# Calculate the signature 's' using the given formula
signature_s = (k_inverse * (hash_value - pow(generator, given_r_value, p_value))) % q_value

print("Computed Signature 's':", signature_s)
