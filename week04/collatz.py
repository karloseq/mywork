def collatz(number):
    """Function to calculate the Collatz sequence for a given number."""
    print(number, end=' ')
    while number != 1:
        if number % 2 == 0:  # If the number is even
            number = number // 2
        else:  # If the number is odd
            number = 3 * number + 1
        print(number, end=' ')


def main():
    try:
        # Ask the user for a positive integer
        n = int(input("Please enter a positive integer: "))
        if n <= 0:
            raise ValueError("Please enter a positive integer.")

        # Call the collatz function with the user's input
        collatz(n)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
