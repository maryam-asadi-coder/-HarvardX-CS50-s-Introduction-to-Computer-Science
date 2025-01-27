#This line uses the input function to prompt the user for a greeting.
#The prompt "Greeting : " is displayed on the screen, asking the user to enter their input.
greeting = input("Greetings, welcome to Kramer Bank : ").lower().strip()
#The .lower() method converts all characters in the greeting to lowercase. This ensures that the code is case-insensitive, meaning "Hello" and "hELLO" will be treated the same way.
#The .strip() method removes any leading or trailing whitespace characters (like spaces or tabs) from the beginning and end of the greeting. This ensures that greetings with extra spaces won't affect the outcome.
if "hello" in greeting:
    print("$0")
elif 'h' == greeting[0]:
    print("$20")
    #This line starts an else block. The else block is executed if neither the if nor the elif condition is True.
else:
    print("$100")
    #In summary, this code takes a greeting as input, converts it to lowercase and removes extra spaces, then checks if it contains "hello" or starts with 'h'. It prints different messages based on these conditions.
