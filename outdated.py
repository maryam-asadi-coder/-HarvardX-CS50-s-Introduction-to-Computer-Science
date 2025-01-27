# This code prompts the user for a date, validates it, and displays it in YYYY-MM-DD format.
# Months list for validation
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#maryam_asadi
while True:  # Infinite loop until a valid date is entered
    date = input("Date: ")  # Prompt for date input
    try:
         # Check for MM/DD/YYYY format
        if "/" in date:
            mm, dd, yyyy = date.split("/")
        # Check for MM, DD, YYYY format
        elif "," in date:
            mmdd, yyyy = date.split(", ")
            mm, dd = mmdd.split(" ")
            # Convert month to index (1-based)
            mm = (months.index(mm)) + 1
            # Validate month and day
        if int(mm) > 12 or int(dd) > 31:
            raise ValueError
    except (AttributeError, ValueError, NameError, KeyError):   # Catch exceptions
        pass  # No error handling for brevity (consider adding informative messages)
    else:  # Valid date entered
        print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
        break  # Exit loop
