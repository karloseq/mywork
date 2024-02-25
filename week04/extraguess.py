import random  # Import the random module

# Generate a random number between 0 and 100
numberToGuess = random.randint(0, 100)

# Ask the user for a guess
guess = int(input("Please guess the number between 0 and 100: "))

# Keep asking for a guess until it's correct
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:
        # If it's not equal or too low, it must be too high
        print("Too high")
    guess = int(input("Please guess again: "))

# If the loop ends, the guess was correct
print("Well done! Yes, the number was ", numberToGuess)