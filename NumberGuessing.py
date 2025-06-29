#Number Guessing Game With Python
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guess = None
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Loop until the user guesses the correct number
while guess != secret_number:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid number.")
