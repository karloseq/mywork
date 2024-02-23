# Setting the number to guess
numberToGuess = 30

# Asking the user for their first guess
guess = int(input("Please guess the number:"))

# Loop to keep asking until the correct number is guessed
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Please guess again:"))

# When the correct number is guessed
print("Well done! Yes, the number was", numberToGuess)
