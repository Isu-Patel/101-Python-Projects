import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

attempts = 0

while True:
    # Get the user's guess
    guess = input("Make a guess(Type 'Quit' to exit): ").lower()
    
    if guess == 'quit':
        print(f"Thank you for playing!Bye The Way The Secect Number was {secret_number}.")
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


# ------------------------------- Output -------------------------------- #
# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100. Can you guess it?
# Make a guess(Type 'Quit' to exit): 50
# Too low! Try again.
# Make a guess(Type 'Quit' to exit): 75
# Too high! Try again.
# Make a guess(Type 'Quit' to exit): 60
# Too low! Try again.
# Make a guess(Type 'Quit' to exit): 70
# Too high! Try again.
# Make a guess(Type 'Quit' to exit): 65
# Too high! Try again.
# Make a guess(Type 'Quit' to exit): 63
# Too high! Try again.
# Make a guess(Type 'Quit' to exit): 62
# Congratulations! You've guessed the number in 6 attempts.
