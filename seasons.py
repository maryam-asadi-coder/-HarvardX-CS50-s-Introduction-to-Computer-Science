from datetime import date
import operator
import inflect
import sys
import re
#from datetime import date: Imports the date class from the datetime module for working with dates.
#import operator: Imports the operator module for using the subtraction operator (-).
#import inflect: Imports the inflect library for converting numbers to words.
#import sys: Imports the sys module for program termination.
#import re: Imports the re module for regular expressions (used for date validation).
# Initialize the inflect engine
p = inflect.engine()
#p = inflect.engine(): Initializes the inflect engine for number-to-word conversion.

def main():
    #birth_date = input("Date of birth: "): Prompts the user to enter their birth date in YYYY-MM-DD format and stores it in the birth_date variable
    # Prompt the user for their date of birth in YYYY-MM-DD format
    birth_date = input("Date of birth: ")
    try:
        year, month, day = check_birth(birth_date)
#try...except block handles potential errors during date parsing.
#year, month, day = check_birth(birth_date): Calls the check_birth function to validate the date format and extract year, month, and day components.
#except: Catches any exceptions and exits the program with an "Invalid date" message using sys.exit().
    except:
        sys.exit("Invalid date")
# Creates a date object from the extracted year, month, and day.
    date_of_birth = date(int(year), int(month), int(day))
#Gets today's date using date.today().
    # Get today’s date
    date_of_today = date.today()

    # Subtract one date object from another
    result = operator.sub(date_of_today, date_of_birth)
    total_minutes = result.days * 24 * 60
# Calculates the total number of minutes lived by multiplying the number of days by 24 hours and then by 60 minutes per hour.
#words = p.number_to_words(total_minutes, andword=""): Converts the total minutes to words using the inflect engine's number_to_words function. The andword="" argument avoids using the word "and" between numbers.
#print(words.capitalize() + " minutes"): Prints the converted minutes in words with the first letter capitalized.
#zan_zendegi_azadi
    # Convert numbers to words.
    words = p.number_to_words(total_minutes, andword="")
    print(words.capitalize() + " minutes")

def check_birth(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day

#Ensures the main function runs only when the script is executed directly (not imported as a module).
if __name__ == "__main__":
    main()
#Overall, the code calculates the total number of minutes a person has lived based on their birth date and then presents it in words.
