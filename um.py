#Imports the re module, which is Python's built-in regular expression module. This module provides functions for working with regular expressions.
import re
#Defines a function named main(). This function is the entry point of the program.
def main():
    print(count(input("Text: ")))
#Inside the main() function, this line takes user input using input("Text: ") and passes it to the count() function.
#The result returned by count() is then printed to the console.
def count(s):
    text = re.findall(r"\b([U-u]m)\b", s)
    return len(text)
#Inside the main() function, this line takes user input using input("Text: ") and passes it to the count() function.
#The result returned by count() is then printed to the console.
#Inside the count() function, this line creates a regular expression pattern using re.findall().
#The pattern r"\b([U-u]m)\b" matches the word "um" (or "Um") exactly as a whole word.
#The re.findall() function finds all non-overlapping matches of the pattern in the input string s and returns them as a list.
#Returns the length of the list text, which represents the number of occurrences of "um" in the input string.
#This conditional statement checks if the script is being run directly (as opposed to being imported as a module).
#If the script is run directly, it calls the main() function.
if __name__ == "__main__":
    main()
