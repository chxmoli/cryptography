#DIFF Algos Exercise

import numpy as np

# Caesar Cipher
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

# Playfair Cipher
def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_set = set()
    playfair_matrix = []

    for char in key:
        if char not in key_set and char in alphabet:
            key_set.add(char)

    for char in alphabet:
        if char not in key_set:
            key_set.add(char)

    for i in range(5):
        playfair_matrix.append(list(key_set)[i*5:i*5+5])

    return playfair_matrix

def playfair_cipher(text, key):
    text = text.replace(" ", "").upper()
    playfair_matrix = generate_playfair_matrix(key)
    encrypted_text = ""

    for i in range(0, len(text), 2):
        pair = text[i:i+2]
        row1, col1 = np.where(playfair_matrix == pair[0])
        row2, col2 = np.where(playfair_matrix == pair[1])

        if row1 == row2:
            encrypted_text += playfair_matrix[row1, (col1+1) % 5][0]
            encrypted_text += playfair_matrix[row2, (col2+1) % 5][0]
        elif col1 == col2:
            encrypted_text += playfair_matrix[(row1+1) % 5, col1][0]
            encrypted_text += playfair_matrix[(row2+1) % 5, col2][0]
        else:
            encrypted_text += playfair_matrix[row1, col2][0]
            encrypted_text += playfair_matrix[row2, col1][0]

    return encrypted_text

# Hill Cipher
def hill_cipher(text, key):
    text = text.replace(" ", "").upper()
    key = np.array(key)
    key_size = int(np.sqrt(len(key)))
    encrypted_text = ""

    while len(text) % key_size != 0:
        text += "X"

    for i in range(0, len(text), key_size):
        block = np.array([ord(char) - 65 for char in text[i:i+key_size]])
        encrypted_block = np.dot(key, block) % 26
        encrypted_text += "".join([chr(char + 65) for char in encrypted_block])

    return encrypted_text

# Vigenere Cipher
def vigenere_cipher(text, key, mode="encrypt"):
    text = text.upper()
    key = key.upper()
    key_len = len(key)
    encrypted_text = ""
    for i in range(len(text)):
        if text[i].isalpha():
            key_char = key[i % key_len]
            shift = ord(key_char) - 65 if mode == "encrypt" else 26 - (ord(key_char) - 65)
            encrypted_char = chr(((ord(text[i]) - 65 + shift) % 26) + 65)
            encrypted_text += encrypted_char
        else:
            encrypted_text += text[i]
    return encrypted_text

# Menu
def main():
    while True:
        print("\nSelect an algorithm:")
        print("1. Caesar Cipher")
        print("2. Playfair Cipher")
        print("3. Hill Cipher")
        print("4. Vigenere Cipher")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Encrypted Text:", caesar_cipher(text, shift))
        elif choice == '2':
            text = input("Enter the text to encrypt: ")
            key = input("Enter the key: ")
            print("Encrypted Text:", playfair_cipher(text, key))
        elif choice == '3':
            text = input("Enter the text to encrypt: ")
            key = input("Enter the key matrix (comma-separated): ")
            key = [int(x) for x in key.split(",")]
            print("Encrypted Text:", hill_cipher(text, key))
        elif choice == '4':
            text = input("Enter the text to encrypt: ")
            key = input("Enter the key: ")
            print("Encrypted Text:", vigenere_cipher(text, key))
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
