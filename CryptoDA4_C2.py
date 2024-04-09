import random

p = 311
g = 169
a = 11
x = random.randint(1, p - 1)
y = pow(g, x, p)
h = pow(g, a, p)

k = random.randint(1, p - 1)
r = pow(g, k, p)
e = (h * pow(r, p - 2, p)) % p
s = (k + x * e) % (p - 1)

transcript = (e, s)
print(transcript)