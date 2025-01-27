#The provided Python code implements a simple calculator that takes a mathematical expression from the user, evaluates it, and prints the result with one decimal place.
#Get User Input
expression = input("Expression: ")

x ,y ,z = expression.split(" ") #meaning it breaks the string wherever it encounters a space.
#The new_x = int(x) and new_z = int(z) lines convert the strings in variables x and z to integers. This ensures that the subsequent calculations are performed correctly.
new_x = float(x)
new_z = float(z)
#he following if statements perform the actual calculation based on the operator (y). There are four if statements, each checking if y is equal to a specific operator (+, -, *, /). If the condition is true, the corresponding operation is performed using the converted numbers new_x and new_z. The result is stored in the result variable.
if y == "+":
    result = new_x + new_z
    print(round(result, 1))
    #The print(round(result, 1)) line rounds the result to one decimal place before printing it using print().
if y == "-":
    result = new_x - new_z
    print(round(result, 1))
if y == "*":
    result = new_x * new_z
    print(round(result, 1))
if y == "/":
    result = new_x / new_z
    print(round(result, 1))


