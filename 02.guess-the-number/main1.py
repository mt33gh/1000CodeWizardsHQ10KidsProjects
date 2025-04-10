"""
What to do:
1. Remove comments, and run the code.  You will get the same result.
2. The code don't display the welcome message.  Modify the code to display it.
3. Modify the code so that the type of each variable is printed.  For example,
    print(type(num_guesses), type(random_number), type(user_won))
4. Learn randint() at https://docs.python.org/3/library/random.html
    random.randint(a, b)
    Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
5. Insert `print("random_number = ", random_number)` 
   just after `random_number = randint(1, 10)`.
6. Learn the for-loop:
(1) Change `user_guess...try again!")` to a multiline comment.
(2) Put `print("turn=",turn)` under `for...`, and run the code.
(3) Uncomment the comment lines.
7. Learn `user_guess = int(input("What is your guess? "))`.
8. Learn `num_guesses += 1`.
9. Learn the key word `break`, and put it under `user_won = True`.
  Then, run the code.
10. Learn the if-else structure. 

"""



from random import randint


welcome_message = """
    Welcome to 'Guess The Number'!

    In this app, you'll need to guess a number between
    1 and 10. You have 3 turns to guess correctly. 
    If you guess within 3 turns, you'll be told how many
    turns it took you to guess. If you can't guess, a 
    losing message will be displayed along with the 
    random number.
"""
print(welcome_message)
num_guesses = 0
random_number = randint(1, 10)
print("random_number = ", random_number)
user_won = False
print(type(num_guesses), type(random_number), type(user_won))

for turn in range(3):
    print("turn=",turn)
    user_guess = int(input("What is your guess? "))
    num_guesses += 1

    if user_guess == random_number:
        print("That's correct!")
        print(f"You guessed the number in {num_guesses} guesses.")
        user_won = True
        break
    else:
        print("Sorry, that's incorrect, try again!")


if not user_won:
    print(f"Game over! The random number was: {random_number}.")
