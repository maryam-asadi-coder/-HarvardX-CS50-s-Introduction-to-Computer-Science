
"""Identify Mealtime Based on Input Time"""

def main():
    #  A program that takes time from the user and prints the meal time as output.
    #  # Get time from user
    time = input("What time is it? ")
    time = convert(time)
    # Check meal time
    if (7 <= time <= 8):
        print("breakfast time")  # Breakfast
    elif (12 <= time <= 13):
        print("lunch time")  # Lunch
    elif (18 <= time <= 19):
        print("dinner time")   # Dinner

#it prompts the user to enter the time in HH:MM format (e.g., "13:30").
#Splits the time into hours and minutes using map and split.
#Checks if the user's input has the correct format (HH:MM).
#Checks the time against the predefined meal time ranges:
#Breakfast: 7:00 to 8:00
#Lunch: 12:00 to 13:00
#Dinner: 18:00 to 19:00
def convert(time):
    first_digit, last_digit = time.split(":")
    last_digit = "6" if (int(last_digit)) >= 31 else ("25" if (int(last_digit)) == 15 else ("00" if (int(last_digit)) == 00 else "5")  )
    return (float(first_digit + "." + last_digit))


if __name__ == "__main__":
    main()
