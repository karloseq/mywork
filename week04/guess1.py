# The number the user needs to guess
numberToGuess = 30

# Ask the user for a guess
guess = int(input("Please guess the number: "))

# Keep asking for a guess until it's correct
while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again: "))

# If the loop ends, the guess was correct
print("Well done! Yes, the number was ", numberToGuess)