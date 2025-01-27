# Importing the is_valid function from the plates module
from plates import is_valid

def main():
    test_is_valid_length_short()#Tests if the function rejects strings shorter than a certain length.
    test_is_valid_length_long()#Tests if the function rejects strings longer than a certain length.
    test_is_valid_number_middle()#Tests if the function rejects strings with numbers in the middle (likely not allowed in the license plate format).
    test_is_valid_first_number()#Tests if the function rejects strings starting with numbers.
    test_punctuation()#Tests if the function rejects strings containing punctuation.
    test_alph_start()#Tests if the function rejects strings that don't start with letters.
#Each test function uses assertions to verify the expected behavior of the is_valid function. It calls is_valid with a specific string and then uses assert statements to check if the returned value matches the expected outcome (True or False).
def test_is_valid_length_short():
    assert is_valid("A") == False
    assert is_valid("AA") == True

def test_is_valid_length_long():
    assert is_valid("AB12345") == False
    assert is_valid("AAAAAA") == True

def test_is_valid_number_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True

def test_is_valid_first_number():
    assert is_valid("AAA022") == False
    assert is_valid("AAA202") == True

def test_punctuation():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False

def test_alph_start():
    assert is_valid("123456") == False
    assert is_valid("AB1234") == True

if __name__ == "__main__":
    main()
    #block ensures that the test functions are only executed when the script is run directly. This allows you to import the main function from another script without accidentally running the tests.
