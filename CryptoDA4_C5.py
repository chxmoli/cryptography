# Define domain parameters
p = 283
q = 47
g = 60

# Alice's private key
x = 24

# Alice's per-message secret number
k = 15

# Hash code of the message
h = 41

# Calculate r = (g^k mod p) mod q
r = pow(g, k, p) % q

# Calculate s = (k^-1 * (h + x*r)) mod q
k_inverse = pow(k, -1, q)
s = (k_inverse * (h + x * r)) % q

# Alice's signature
signature = (r, s)

# Bob verifies the signature
v1 = pow(g, h, p)
v2 = (pow(x, r, p) * pow(r, s, p)) % p
v2_inverse = pow(v2, -1, p)
computed_r = (v1 * v2_inverse) % p % q

if computed_r == r:
    print("Signature verified by Bob: Valid")
else:
    print("Signature verified by Bob: Invalid")
