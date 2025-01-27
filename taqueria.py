#Goal: Take food orders from the user and display the running total cost until the user stops the program.
#This function is the starting point of the program.
#It calls the total_cost function with the argument prompt: "Item: "
def main():
    total_cost("Item: ")


def total_cost(prompt):
         # It creates a dictionary called dict that contains food names as keys and their prices as values.
        dict = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
        # It runs an infinite while loop (with a while loop prompt for item and add item value until user input exit)
        total = 0
        while True:
            try:
                item = input(prompt).strip().title()
                for order in dict:
                    if order == item:
                        total = total + (dict[order])
                        total = abs(total)
                        print(f"Total: ${total:.2f}") #It prints the running total with two decimal places and a $ prefix as Total: $total:.2f.
            except EOFError:  #If an EOFError occurs (e.g., the user presses Ctrl+D), it stops the while loop.
                break
main()


#Additional explanations:
#The program is not case-sensitive because the user's input is converted to titlecase.
#If the entered food name is not found in the dictionary, it is ignored and no message is displayed.
#The program continues to prompt for new orders until the user presses Ctrl+D.
