encrypted_flag = 'kxn iye lbedec'

def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

for i in range(1, 26):
    print(caesar_cipher_encrypt(encrypted_flag, i), i)