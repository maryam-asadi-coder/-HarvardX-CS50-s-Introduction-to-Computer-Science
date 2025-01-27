from seasons import check_birth
#Imports the check_birth function from the seasons module. This means we can use the check_birth function in this code without defining it again
def main():
    test_check_birth()
#Defines a function named main. This function is the entry point of the program.
#Inside the main function, it calls the test_check_birth function.
def test_check_birth():
    assert check_birth('1990-01-01') == ("1990", "01", "01")
    assert check_birth('1990-1-1') == None
    assert check_birth("July 1, 1991") == None
#Defines a function named test_check_birth. This function is used for testing the check_birth function.
#The assert statements are used for testing. If the condition after assert is True, the code continues. If it's False, the program raises an AssertionError.
#The first assert checks if check_birth('1990-01-01') returns the tuple ("1990", "01", "01").
#The second assert checks if check_birth('1990-1-1') returns None.
#The third assert checks if check_birth("July 1, 1991") returns None.

if __name__ =="__main__":
    main()
#This line checks if the script is being run directly (not imported as a module).
#If it is being run directly, it calls the main function.
#Overall, this code defines a function to test the check_birth function from the seasons module. It checks if the check_birth function correctly handles valid and invalid date formats.
