# Prompt the user to enter a string
rawString = input("Please enter a string:")

# Normalize the string (remove leading and trailing whitespace, convert to lowercase)
normalisedString = rawString.strip().lower()

# Calculate the length of the original input string
lengthOfRawString = len(rawString)

# Calculate the length of the normalized string
lengthOfNormalised = len(normalisedString)

# Print the normalized string
print(f"That string normalized is: {normalisedString}")

# Print a message indicating that we reduced the input string
print("We reduced the input string.")