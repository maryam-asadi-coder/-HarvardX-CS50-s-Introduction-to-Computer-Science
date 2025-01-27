#Description of the Python code for a grocery list
#This code is a Python program for creating a grocery list that allows the user to enter the items they need line by line. After the list is complete, the program sorts the items alphabetically and displays the number of times each item was entered before its name.
grocery = {}

while True:  #This while loop will continue until the user presses the d + Ctrl key.
    try:
        item = input().upper().strip()  #This line waits for user input and stores it as all uppercase and without any extra whitespace.
        if item not in grocery:
            # Initialize item's quantity in grocery
            grocery[item] = 1
        else:  #If the entered item is not already in the grocery dictionary, this code adds a new key with the name of that item and a value of 1 (as the first time it was entered) to the dictionary.
            # Update item's quantity
            grocery[item] = grocery[item] + 1
    except EOFError:
        sorted_dict = dict(sorted(list(grocery.items())))
        for item in sorted_dict:
            print(sorted_dict[item], item, sep=" ")
        break
    except KeyError:
        pass
#Creates a new dictionary called sorted_dict that contains the items in grocery in alphabetical order.
#Starts a for loop to iterate over the sorted_dict dictionary.
#For each item in sorted_dict, prints the number of times that item was entered before its name.
#Stops the while loop using the break statement.
