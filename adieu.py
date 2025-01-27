import inflect
"""Hope is the fuel that allows us to keep going, even when things are tough"""

#Imports the inflect module, which provides advanced string manipulation functionalities.
# Import the inflect module for advanced string manipulation (addresses Check50 requirement)
p = inflect.engine()
#Creates an instance of the inflect engine, which we'll use for pluralization (and more) later.
# Create an inflect engine instance for pluralization and other grammatical tasks.
names = []
# Initialize an empty list to store the entered names.Initializes an empty list called names to store the names entered by the user.
while True:
       # Loop indefinitely to keep prompting for names
       #while True:
       #Starts an infinite loop that keeps prompting for names until the user exits.
    try:
        #Creates a try block to handle potential input errors.
        name = input("Name: ")
        #Prompts the user to enter a name using input().
        #Stores the entered name in the variable name.
    except EOFError:
        #Catches the EOFError exception that occurs when the user presses Ctrl+D (on Unix-like systems) to indicate the end of input.
        print()  # Print an empty line to indicate end of input
        break   # Exit the loop when Ctrl+D (EOF) is pressed
    else:
        names.append(name)
# Create the farewell message using the inflect module for proper pluralization:
print(f"Adieu, adieu, to {p.join(names)}")
#print(f"Adieu, adieu, to {p.join(names)}")
#Uses an f-string to create the farewell message.
#f"Adieu, adieu, to {p.join(names)}" combines the fixed text "Adieu, adieu, to " with the list of names joined using p.join(names).
#p.join(names) leverages the inflect module to ensure proper pluralization. It will join the names appropriately depending on whether there's one name, two names, or more than two names
