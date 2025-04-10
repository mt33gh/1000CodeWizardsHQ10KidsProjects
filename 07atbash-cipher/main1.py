"""
1. Run the code, entering 'abcdefg hijklmnop qrstvu wxyz'.
2. Remove the initial comment.
3. print(string.ascii_lowercase), print(string.punctuation)
4. Learn random.randint()
    for i in range(0,100):
        print(random.randint(1,4))
5. Study the function `def run_atbash_cipher(text):`
6. Learn about `character in punctuation`.
7. Learn about `character.isspace()`.
8. Learn about `ascii_lowercase.index(character)`
9. Understand how `ascii_lowercase[-original_index]` works.
10. Learn about string.lower()
11. Notice that the same function is used both for ENCRYPT AND DECRYPT.

"""


#from string import ascii_lowercase, punctuation
from random import randint
import string

print(string.ascii_lowercase)
print(string.punctuation)

n = ""
for i in range(0,50):
    n += str(randint(1,4))
print(n)

ch = "c"
print(string.ascii_lowercase.index(ch))  # = 2
print(string.ascii_lowercase[2])         # = c
thisindex = string.ascii_lowercase.index(ch)+1     # = 3
print(string.ascii_lowercase[-thisindex])  # [-3] means the 3rd from the last: zyx, so x

#10
print("The Big Apple".lower())


def run_atbash_cipher(text):
    cipher_text = ""
    for character in text:
        if character in string.punctuation or character.isspace():
            cipher_text += character
        else:
            original_index = string.ascii_lowercase.index(character) + 1
            cipher_character = string.ascii_lowercase[-original_index]
            cipher_text += cipher_character

    return cipher_text


welcome_message = "Welcome to the 'Atbash Cipher' app!"

ENCRYPT = 1
DECRYPT = 2
encrypted_text = ""

print(welcome_message)

text = input("Enter the text you'd like to encrypt or decrypt: ").lower()
option = int(input("Would you like to (1) encrypt or (2) decrypt the text? "))

if option == ENCRYPT:
    encrypted_text = run_atbash_cipher(text)
    print(f"Your encrypted text is: {encrypted_text}")
elif option == DECRYPT:
    decrypted_text = run_atbash_cipher(text)
    print(f"Your decrypted text is: {decrypted_text}")
