#Bitcoin Price
#"Hope is the last thing that dies within a man." - Albert Camus, French philosopher and writer
import sys
import requests
# Import necessary libraries:
#   - sys: Provides access to system-specific parameters and functions.
#   - requests: Enables making HTTP requests to web APIs.
if len(sys.argv) == 2:
    # Check if exactly two command-line arguments were provided:
    #   - sys.argv: List containing command-line arguments.
    #   - len(sys.argv): Length of the list (number of arguments).
    #   - If true, proceed with processing the value.
    try:
        value = float(sys.argv[1])
           # Convert the second argument (sys.argv[1]) to a floating-point number.
           #- If conversion fails, the except block handles it.
    except:
        # Handle any exceptions that might occur during conversion.
        print("Command-line argument is not a number")
        sys.exit(1)
         # Print an error message and exit the program with an error code (1).
else:
        # If not exactly two arguments were provided:
        print("Missing command-line argument")
        sys.exit(1)
        # Print an error message and exit the program with an error code (1).
try:
      # Attempt to make an HTTP GET request to the Coindesk API for current Bitcoin price.
    r = requests.get('http://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
     # Convert the response from the API (assumed to be JSON) into a Python dictionary.
    bitcoin = response['bpi']['USD']['rate_float']
     # Extract the current Bitcoin price in USD (float) from the nested dictionary structure.
    total_amount = bitcoin * value
     # Calculate the total amount based on the provided value and Bitcoin price.
    print(f"${total_amount:,.4f}")
     # Format and print the total amount in USD with commas (thousands separators) and four decimal places.

except requests.RequestException:
     # Handle any exceptions that might occur during the HTTP request.
     print("RequestException")
     sys.exit(1)
       # Print an error message and exit the program with an error code (1).

#Explanation

#Imports:
#sys: Provides access to command-line arguments and system functions.
#requests: Enables making HTTP requests to web APIs.

#Argument Validation:
#Checks if exactly two command-line arguments were provided.
#If not, an error message is printed, and the program exits.
#Attempts to convert the second argument (value) to a floating-point number.
#If conversion fails, an error message is printed, and the program exits.

#API Request and Processing:
#Makes an HTTP GET request to the Coindesk API for current Bitcoin price.
#Converts the API response (assumed to be JSON) into a Python dictionary.
#Extracts the current Bitcoin price in USD (float) from the nested dictionary structure.
#Calculates the total amount based on the provided value and Bitcoin price.

#Output and Error Handling:
#Formats and prints the total amount in USD with commas and four decimal places.
#Catches any exceptions that might occur during the HTTP request and prints an error message with exit code (1).
