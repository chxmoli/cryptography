#21BCE2140

def map_to_numbers(message):
    mapped = []
    for char in message:
        if char == ' ':
            mapped.append(26)
        else:
            mapped.append(ord(char) - ord('A'))
    return mapped

def rsa_encrypt(message, e, n):
    encrypted_blocks = []
    for block in message:
        encrypted_blocks.append(pow(block, e, n))
    return encrypted_blocks

def rsa_decrypt(ciphertext, d, n):
    decrypted_blocks = []
    for block in ciphertext:
        decrypted_blocks.append(pow(block, d, n))
    return decrypted_blocks

# Part (a)
message_a = "HOW ARE YOU"
mapped_message_a = map_to_numbers(message_a)
e_a = 13
n_a = 100

encrypted_blocks_a = rsa_encrypt(mapped_message_a, e_a, n_a)
print("Encrypted message (part a):", encrypted_blocks_a)

# Part (b)
ciphertext_b = [4819, 2378, 8421, 293, 2378, 10456, 2378, 3343, 10456, 3157, 10456, 10301]
d_b = 937
n_b = 12091

decrypted_blocks_b = rsa_decrypt(ciphertext_b, d_b, n_b)
print("Decrypted message (part b):", ''.join([chr(block + ord('A')) if block != 26 else ' ' for block in decrypted_blocks_b]))
