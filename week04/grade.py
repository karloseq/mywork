# This program reads in
# a student's percentage
# and prints out the
# corresponding grade

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit1")
elif percentage < 70:
    print("Merit2")
else:
    print("Distinction")