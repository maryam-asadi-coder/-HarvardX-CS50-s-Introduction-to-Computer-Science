#Explanation of the Python code for calculating fruit calories:
#This part of the code creates a dictionary called fruits.
#The keys of this dictionary are the names of fruits and the values are the number of calories in one serving of that fruit.
fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80,
}
#The input() function is used to get input from the user.
#The title() method capitalizes the name of the fruit.
#The strip() method removes any extra whitespace from the beginning and end of the input.
item = input("Item: ").title().strip()

for fruit in fruits:
    if item in fruit:
        print(f"Calories: {fruits[fruit]}")
#Explanation:
#This part of the code creates a for loop to iterate over the fruits dictionary.
#In each iteration, the variable fruit holds the name of a fruit.
#The condition if item in fruit checks if the name of the fruit entered by the user is contained within the name of a fruit in the fruits dictionary.
#If the if condition is true, the code inside the if block is executed.
#Inside the if block, the statement `f"Calories: {fruits[fruit]}" prints the number of calories in one serving of the fruit.
#The format() method is used to format the string.
