import re
#This line imports the re module, which provides regular expression functionalities in Python. These functionalities will be used later in the code to parse time strings.

def main():
    print(convert(input("Hours: ")))
#This defines a function named main.
#When the script is executed, this function is automatically called.
#Inside the main function:
#It prompts the user to enter an input using input("Hours: ").
#The user's input is then passed to the convert function for processing.
#The result returned by convert is printed to the console.
#This defines a function named convert.
#The function takes a string s as input, which is expected to be a time range in the format "HH:MM (AM/PM) to HH:MM (AM/PM)".
#Inside the convert function:
#A regular expression is defined using re.search. This pattern matches the expected time range format, including optional minutes.
#If a match is found, the matched groups are stored in a variable named hours.
#The code then checks if the hours extracted exceed 12 (invalid). If so, a ValueError is raised.
#If the hours are valid, two calls are made to the create function:
#First call uses the first hour, minute (if available), and AM/PM information from the matched groups.
#Second call uses the second hour, minute (if available), and AM/PM information.
#The results from both create calls (formatted time strings) are concatenated with " to " in between and returned.
#If the input string doesn't match the expected format (no match from re.search), a ValueError is raised.
def convert(s):

    if hours := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM)? to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)?$",s):
        if int(hours.group(1)) > 12 or int(hours.group(4)) > 12:
            raise ValueError

        first = create(int(hours.group(1)), hours.group(2), hours.group(3))
        second = create(int(hours.group(4)), hours.group(5), hours.group(6))
        return first + " to " + second
#This defines a function named create.
#The function takes three arguments:
#hour: The hour value (integer).
#minute: The minute value (string or None).
#time: The AM/PM indicator (string).
#Inside the create function:
#If the time is PM and the hour is not 12, the hour is incremented by 12 to convert it to 24-hour format.
#If the time is AM and the hour is 12, the hour is set to 0 for consistency in 24-hour format.
#If the minute value is None, it's replaced with ":00" to ensure consistent formatting.
#An f-string is used to format the result:
#hour is formatted to two digits with leading zeros using f"{hour:02}".
#minute is formatted to two digits with leading zeros using f"{minute:02}".
#The formatted hour and minute are then concatenated (either with or without a colon).
#The formatted time string is returned.
    else:
        raise ValueError

def create(hour,minute,time):
    if time == "PM":
        if hour == 12:
            hour = 12
        else:
            hour += 12
    else:
        if hour == 12:
            hour = 0

    if minute == None:
        minute = ":00"
        result = f"{hour:02}{minute:02}"

    else:
        result = f"{hour:02}:{minute:02}"

    return result

if __name__ == "__main__":
    main()
#ZAN_ZENDEGI_AZADI
