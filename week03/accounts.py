def mask_account_number(account_number):
    # Check if the length of the account number is less than 10
    if len(account_number) < 10:
        return "Account number must be 10 digits long"
    
    # Replace the first 6 characters with 'X's and keep the last 4 characters unchanged
    masked_number = 'X' * (len(account_number) - 4) + account_number[-4:]
    return masked_number

if __name__ == "__main__":
    # Prompt the user to enter an account number
    account_number = input("Please enter a 10-digit account number: ")
    
    # Mask the account number and print the result
    masked_account_number = mask_account_number(account_number)
    print("Masked account number:", masked_account_number)
