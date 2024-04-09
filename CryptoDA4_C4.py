def verify_elgamal_signature(alpha_value, prime_value, public_key, signature, message):
    r_value, s_value = signature
    if 0 < r_value < prime_value and 0 < s_value < prime_value - 1:
        v1 = pow(alpha_value, message, prime_value)
        v2 = (pow(public_key, r_value, prime_value) * pow(r_value, s_value, prime_value)) % prime_value
        return v1 == v2
    else:
        return False

# Given parameters
alpha = 2
prime = 877
public_key = 253
signature = (137, 217)
message = 710

# Verify the signature
is_valid_signature = verify_elgamal_signature(alpha, prime, public_key, signature, message)

if is_valid_signature:
    print("The provided signature is valid.")
else:
    print("The provided signature is not valid.")
