import datetime

def is_weekday():
    # Get the current date
    now = datetime.datetime.now()

    # Monday is 0 and Sunday is 6
    if now.weekday() < 5:
        return True
    else:
        return False

if is_weekday():
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")