#AES Exercise

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def aes_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text

def main():
    key_size = int(input("Enter the key size (64/128/256): "))
    if key_size not in [64, 128, 256]:
        print("Invalid key size. Please enter 64, 128, or 256.")
        return

    key = get_random_bytes(key_size // 8)
    plaintext = input("Enter the plaintext to encrypt: ").encode()

    ciphertext = aes_encrypt(key, plaintext)
    print("Encrypted ciphertext:", ciphertext.hex())

    decrypted_text = aes_decrypt(key, ciphertext)
    print("Decrypted plaintext:", decrypted_text.decode())

if __name__ == "__main__":
    main()
