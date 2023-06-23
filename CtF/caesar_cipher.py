import random
import string

def generate_flag(length=10, prefix="FLAG{", suffix="}"):
    flag_content = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return prefix + flag_content + suffix

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

def ctf_challenge():
    shift = random.randint(1, 25)
    flag = generate_flag()
    encrypted_flag = caesar_cipher_encrypt(flag, shift)

    print("Welcome to the CTF cryptography challenge!")
    print(f"Decrypt the following Caesar cipher to find the flag: {encrypted_flag}\n")

    return encrypted_flag, flag

def test_flag(user_input, original_flag):
    if user_input == original_flag:
        print("Congratulations! Your flag is correct!")
        return True
    else:
        print("Incorrect! Please try again.")
        return False

if __name__ == "__main__":
    encrypted_flag, original_flag = ctf_challenge()

for i in range(1, 26):
    if caesar_cipher_encrypt(encrypted_flag, -i)[0:4] == 'FLAG':
        print("FLAG FOUND")
        decrypted_flag = caesar_cipher_encrypt(encrypted_flag, -i)
        decrypt_shift = i
        break


is_correct = test_flag(decrypted_flag, original_flag)
print(original_flag)

