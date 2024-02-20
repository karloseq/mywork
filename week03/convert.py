def convert_to_cents(dollars):
    # Removing the dollar sign if present
    dollars = dollars.replace('$', '')
    # Converting dollars to cents
    cents = int(float(dollars) * 100)
    return abs(cents)

if __name__ == "__main__":
    amount = input("Please enter an amount: ")
    absolute_cents = convert_to_cents(amount)
    print("That amount in cent is:", absolute_cents)