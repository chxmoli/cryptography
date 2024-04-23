import hmac
import hashlib

def hmac_sha256(message, key):
    # Convert key and message to bytes
    key_bytes = key.encode('utf-8')
    message_bytes = message.encode('utf-8')

    # If the key is longer than block size, hash it
    if len(key_bytes) > 64:
        key_bytes = hashlib.sha256(key_bytes).digest()

    # If the key is shorter than block size, pad it with zeroes
    if len(key_bytes) < 64:
        key_bytes += b'\x00' * (64 - len(key_bytes))

    # Create inner and outer padded keys
    inner_key = bytes([x ^ 0x36 for x in key_bytes])
    outer_key = bytes([x ^ 0x5C for x in key_bytes])

    # Calculate inner hash
    inner_hash = hashlib.sha256(inner_key + message_bytes).digest()

    # Calculate outer hash
    outer_hash = hashlib.sha256(outer_key + inner_hash).hexdigest()

    return outer_hash

# Define the message and secret key
message = input("Enter Message: ")
key = input("Enter Key: ")

# Calculate the HMAC using HMAC-SHA256
hmac_result = hmac_sha256(message, key)
print("HMAC:", hmac_result)
