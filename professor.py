# Used to generate random numbers for the math problems.
import random


def main():
    eqn = 10
    score = 0
    chances = 3
    lvl = get_level()
    while eqn != 0:
        if chances == 3: # User have 3 chances to answer each equation
            # Only generate_integer for new equation if chances == 3
            x, y = generate_integer(lvl)
        try:
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_answer == answer:
                eqn = eqn - 1
                score = score + 1
                chances = 3 # Reset chances to generate new equation in case user input the right answer on 2nd/3rd try
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
            pass
        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3 # Reset chances to generate new equation
            eqn = eqn - 1
            continue
    print(f"Score: {score}")
    #def main():
    #1 = get_level()
    #generate_integer(1)
    #generate_integer(get_level())


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass
        #while True:
        #level = input("level: ")
        #if level not in ["1", "2", "3"]
             #continue
         #return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

#or

    #score = 0
    #for i in range(10):
     #if level =="1":
     #x = random.randint(0,9)
     #y = random.randint(0,9)
     #elif level == "2":
     #x = random.randint(10, 99)
     #y = random.randint(10, 99)
     #else:
    #x = random.randint(100, 999)
    #y = random.randint(100, 999)
    #while True:
    #3 + 2 = 5
    #5
    #print(f"{x} + {y} = ", end ="")
    #answer = input()
    #if answer == str(x + y):
    #score +=1
    # break
    #elif answer != str(x + y):
    #print("EEE")
    #continue
    #else:
    #print(f"{x} + {y} = {x+y}")
    #break



#simulate game

if __name__ == "__main__":
    main()

#This is the main function that runs the entire game loop.
#It initializes variables for the number of equations (eqn), score (score), allowed attempts (chances), and difficulty level (lvl).
#It enters a while loop that continues until all equations (eqn) have been answered.
#Inside the loop:
#It checks if the user has three chances (chances == 3).
#If so, it generates new operands (x, y) using generate_integer(lvl).
#It tries to convert user input (user_answer) to an integer.
#If the answer is correct, it decrements eqn, increments score, and resets chances for the next equation.
#If the answer is incorrect, it raises a ValueError or NameError.
#These exceptions are caught and "EEE" is printed to indicate an incorrect answer.
#It decrements chances.
#If chances reaches 0 (all attempts used), it reveals the correct answer using print(f"{x} + {y} = {answer}").
#It resets chances for the next equation and decrements eqn.
#After the loop, it prints the final score.
#get_level():
#This function keeps prompting the user for a valid difficulty level (1, 2, or 3) until a valid input is received.
#It uses a while True loop to repeat the prompt until a valid level is entered.
#Inside the loop:
#It tries to convert user input (n) to an integer.
#If it's a valid level (between 1 and 3), it returns the level.
#Otherwise, it catches potential exceptions and continues looping.
#generate_integer(level):
#This function generates two random integers (x, y) based on the provided difficulty level (level).
#It uses random.randint() to generate numbers within the appropriate ranges:
#Level 1: Single digits (0-9)
#Level 2: Double digits (10-99)
#Level 3: Triple digits (100-999)
#It returns a tuple containing the two generated integers.
