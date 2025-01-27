def main():
    plate = input("Plate: ")#Prompts the user to enter a license plate number and stores it in the plate variable using input.
    if is_valid(plate): #Calls the is_valid function with the plate as an argument.
        print("Valid")
    else: #Checks the return value of is_valid. #If True, prints "Valid"
                                                #If False, prints "Invalid"
        print("Invalid")

def is_valid(plate): #It first checks if the length of the plate is less than 2 or greater than 6 characters. If so, it returns False (invalid plate).
    if  len(plate) <2 or len(plate)> 6:
         return False

# it verifies if the first two characters are letters (using isalpha) and returns False if not.
    if plate[0].isalpha() == False or plate[1].isalpha() == False:
        return False
#It iterates through the characters in the plate using a while loop:
#If a character is not a letter:
#It checks if the character is a "0". If it is, it returns False (leading zero not allowed).
#Otherwise, it breaks out of the loop, assuming letters come before numbers.
    i = 0
    while i < len(plate):
        if plate[i].isalpha() == False:
            if plate[i] == "0":
                return False
            else:
                break
        i += 1
#It uses a for loop to iterate through each character again:
#If the character is a digit:
#It finds the index of the digit in the plate string.
#It checks if the remaining characters after that index are all digits (using string slicing). If not, it returns False (numbers must be at the end).
    for num in plate:
        if num.isdigit():
            index = plate.index(num)
            if not plate[index:].isdigit():
                return False

    for char in plate:
        if char in ['.', ' ', '!', '?']: #Finally, it uses another for loop to iterate through characters and checks if any are special characters (".", " ", "!", "?"). If found, it returns False (special characters not allowed).
            return False
#If none of the conditions above return False, the function reaches the end and returns True, indicating a valid license plate format.
    return True

if __name__ == "__main__":
    main()
