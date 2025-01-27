#This line imports the re module, which provides regular expression functionality in Python. Regular expressions are powerful patterns used for matching text strings.
import re

#This line defines a function named main. Functions are reusable blocks of code that perform specific tasks.
def main():
    print(validate(input("IPv4 Address: ")))
#This line calls the input function to prompt the user to enter an IPv4 address and stores the input in the ip variable.
#It then calls the validate function with the ip as an argument. The validate function is defined later in the code.
#Finally, it prints the result of calling the validate function using the print function.
#This line defines another function named validate. This function takes one argument, ip, which is expected to be an IPv4 address string.
#This line creates a variable named regex and assigns a regular expression pattern to it. The pattern matches valid octets (individual parts) of an IPv4 address.
#[0-1]: Matches a single digit between 0 and 1 (for the first octet).
#([0-9]?){2}: Matches two optional digits between 0 and 9 (for the second, third, and fourth octets).
#|: This is an OR operator, allowing for multiple matching options.
#2[0-4]?[0-9]?: Matches a value between 200 and 249 (for the second, third, and fourth octets).
#25[0-5]: Matches a value between 250 and 255 (for the second, third, and fourth octets).

def validate(ip):
    regex = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    match = re.search(r"^" + regex + "\." + regex + "\." + regex + "\." + regex + "$", ip)
    if match:
        return True
    else:
        return False
#This line returns False from the validate function, indicating that the input is not a valid IPv4 address.
#This line attempts to match the entire ip string with the regular expression pattern created earlier.
#re.search: This function from the re module searches for the first occurrence of the pattern in the string.
#r"...": Raw string prefix helps avoid interpreting backslashes as escape sequences within the pattern.
#^: Matches the beginning of the string.
#$: Matches the end of the string.
#The regex pattern is repeated four times, ensuring there are four octets separated by dots.
#The result of this search is stored in the match variable.

if __name__ == "__main__":
    main()
#This line is a common Python idiom for ensuring code within the block only executes when the script is run directly. It prevents unintended execution when the code is imported as a module.
#This line calls the main function, which starts the program execution.
#zan_zendegi_azadi
