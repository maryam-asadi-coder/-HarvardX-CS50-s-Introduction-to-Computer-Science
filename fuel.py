#This line defines a function named main. This function is the entry point of the program when you run it.
def main():
    x = get_fraction("Fraction: ")
    print(x)
#Inside the main function, this line calls another function named get_fraction.
#It passes the string "Fraction: " as an argument to the get_fraction function. This string will be used as a prompt to ask the user for input.
#The result returned by the get_fraction function is stored in the variable x.
#This line simply prints the value of the variable x to the console. This value will be whatever the get_fraction function returns.
def get_fraction(prompt):
    #This line defines a function named get_fraction that takes one argument named prompt.
    while True:#This line creates an infinite loop. The loop will continue to run until it's explicitly broken using a break statement.
        try:#This line starts a try block. The code inside this block will be attempted to be executed. If an exception (error) occurs during execution, the code will jump to the except block (if present).
            x, y = input(prompt).split("/")#This line prompts the user using the string passed as the prompt argument (in this case, "Fraction: ").
#It then reads the user's input and stores it as a string in the variable input(prompt).
#The split("/") method splits the user's input at the "/" character and assigns the resulting parts to the variables x and y.
#For example, if the user enters "1/2", x will become "1" and y will become "2".
            if 0 <= int(x)/int(y) <= 0.1:
                #This starts an if statement that checks if the fraction entered by the user represents a value between (including) 0 and 0.1 (inclusive).
#It converts x and y to integers using int(x) and int(y).
#Then, it performs the division int(x) / int(y).
#Finally, it checks if this result is between 0 and 0.1 (inclusive).
#If this condition is true:
#The function returns the string "E".
                return("E")
            elif 0.9 <= int(x)/int(y) <= 1:
                return("F")
            elif 0.1 < int(x)/int(y) < 0.9:
                return str(round(int(x)/int(y)*100)) + "%"
        except (ValueError, ZeroDivisionError):#This line starts an except block. If any ValueError (e.g., the user enters a non-numeric character) or ZeroDivisionError (division by zero) occurs inside the try block, the code inside this except block will be executed.
            pass #The pass statement does nothing. It's used here as a placeholder to prevent the except block from having no code. In this case, the function simply ignores the error and continues looping until the user enters a valid fraction.


main()
#This code prompts the user to enter a fraction in the form "numerator/denominator".
#It keeps asking for input until the user enters a valid fraction.
#Based on the value of the fraction (represented as a decimal), it returns one of the following:
#"E" if the fraction is between 0 and 0.1 (inclusive).
#"F" if the fraction is between 0.9 and 1 (inclusive).
#A string representing the percentage (rounded to two decimal places) if the fraction is between 0.1 and 0.9 (excluding the endpoints).
