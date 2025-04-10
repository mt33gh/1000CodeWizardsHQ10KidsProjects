"""
NOTE: This program has a lot to learn.  Take time.
What to do:
1. Delete the initial long comment.
2. Change `from string import ascii_letters, digits, punctuation` 
  to a comment by adding `#`.  Write `import string` instead.
3. Write `print(string.ascii_letters)` and run the code.
4. Write `print(string.digits)` and run the code.
5. Write `print(string.punctuation)` and run the code. These are string constants. 
6. Put `#` before `password_length = int(input("Enter your desired password length: "))`
   Write: password_length = input("Enter your desired password length: ")
          print("password_length =", password_length, ", type =", type(password_length))
   What type is `password_lentgh`?
7. Learn int().
   Write `password_length = int(password_length)`.
8. Learn `password = ""` (empty string).
  Write `print("password=",password).
9. Learn `random.randint()`.
   Put `#` before `from random import choice, randint`, and write `import random`.
10. Suppose password_length=3.  
  What numbers will `num` be with `for num in range(password_length):`?
  ==> num = 0, 1, or 2
  Write `print("num=",num) just after the for-loop.
11. What numbers does `randint(1,3)` generate?
  ==> 1, 2, and 3
  Write `print("option=",option)` just after `option = random.randint(1, 3)`.
12. What does `random_character = random.choice(string.ascii_letters)` do?
  ==> It chooses a letter and assign it to random_character.
13. Put `#` before `password += random_character`, and
  write `password = password + random_character.`

"""
import string
#from string import ascii_letters, digits, punctuation
#from random import choice, randint
import random

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

welcome_message = "Welcome to the 'Strong Password Generator'!"

RANDOM_LETTER = 1
RANDOM_DIGIT = 2
RANDOM_PUNCTUATION = 3

print(welcome_message)

#password_length = int(input("Enter your desired password length: "))
password_length = input("Enter your desired password length: ")
print("password_length =", password_length, ", type =", type(password_length))
password_length = int(password_length)

password = ""
print("password=",password)

for num in range(password_length):
    print("num=",num)
    random_character = ""
    option = random.randint(1, 3)
    print("option=",option)

    if option == RANDOM_LETTER:
        random_character = random.choice(string.ascii_letters)
        print("random_character=",random_character)
    elif option == RANDOM_DIGIT:
        random_character = random.choice(string.digits)
    elif option == RANDOM_PUNCTUATION:
        random_character = random.choice(string.punctuation)

    #password += random_character
    password = password + random_character
    print("password=",password)

print(f"Your password is: {password}")
