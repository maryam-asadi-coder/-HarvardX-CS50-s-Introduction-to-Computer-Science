
#This Python code is designed to convert text to ASCII art using the pyfiglet library and considering the requirements of your project.

#from pyfiglet import Figlet: Imports the Figlet class from the pyfiglet module. This class is used to work with ASCII art fonts.
#import sys: Imports the sys module, which provides access to system-specific parameters and functions. Here, it's used to retrieve command-line arguments and exit the program with an error code.
#import random: Imports the random module, which provides functions for generating random numbers. This will be used if a random font is chosen

#“The capacity for hope is the most significant fact of life. It provides human beings with a sense of destination and the energy to get started.”
# Norman Cousins, American author and journalist

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
#Instantiates a Figlet object, which you'll use to interact with the ASCII art font functionality.
figlet.getFonts()
#This line, initially commented out, retrieves a list of available ASCII art font names using the getFonts() method of the figlet object. You can uncomment it if you want to see the list of fonts before running the program.

if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandom = False
else:
    print("Invalid Usage")
    sys.exit(1)
#This code block checks the number of command-line arguments provided when running the script:
#len(sys.argv) == 1: If there's only one argument (the script name), it means the user wants a random font to be chosen (isRandom = True).
#len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"): If there are three arguments, and the second argument is either "-f" or "--font" (flags indicating a specific font), the script will use that font (isRandom = False).
#Any other scenario is considered invalid usage, and an error message is printed (print("Invalid Usage")). The program then exits (sys.exit(1)) with an exit code of 1, indicating an error.
if isRandom == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    font = random.choice(figlet.getFonts())
#Random Font: If isRandom == True, it means the user didn't specify a font and wants a random one. In this case, the code uses random.choice() to select a random font from the list of available fonts (figlet.getFonts()) and stores it in the font variable.
#Specific Font: If isRandom == False, it means the user specified a font using the "-f" or "--font" flag and the font name in the second command-line argument (sys.argv[2]). In this case, the code tries to set the font using figlet.setFont(font=sys.argv[2]). If the font name is invalid, it catches an exception, prints an error message, and exits the program.
#Prompts the user to enter text using input("Input:"). The entered text will be stored in the text variable.
text = input("Input:")
#Uses the renderText() method of the figlet object to convert the user's input text (text) into ASCII art using the chosen font (either random or specified). The resulting
print("Output:", figlet.renderText(text))
