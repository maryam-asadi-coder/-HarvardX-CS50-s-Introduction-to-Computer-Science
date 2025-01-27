#Explanation of the Python code for simulating a Coca-Cola vending machine

amount = 0  #This variable is used to store the amount of money paid by the user.
coke_price = 50 #This variable sets the price of a can of Coca-Cola to 50 cents.
denominations = [5, 10, 25]  #This list stores the values of the acceptable coins in order from least to greatest value.

#This loop continues as long as the amount paid by the user is less than the price of the Coca-Cola.
while amount < coke_price:
    print (f"Amount Due: {coke_price - amount}")  #This line displays the remaining amount due to the user.

    user_input = int(input("Insert Coin: ")) #This line prompts the user to enter the coin amount as an integer.
    if user_input in denominations:  #This conditional checks if the amount entered by the user is in the list of acceptable coins.
        amount += user_input  #If the amount entered is valid, it is added to the amount variable.
#This line displays the amount of change (extra money paid) to the user.
print(f"Change Owed: {amount - coke_price}")
#This code accurately simulates how a Coca-Cola vending machine that only accepts 5, 10, and 25 cent coins would work.
