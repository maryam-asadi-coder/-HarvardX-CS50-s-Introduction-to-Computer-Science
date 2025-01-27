#pip install twitter
from twttr import shorten

def main():
    #Calls the test_twttr function to run the tests
    test_twttr()
    #This function contains a series of test cases using Python's assert statement to verify the behavior of the shorten function for different input strings.
def test_twttr():
    #Runs a series of tests on the shorten function.
    # Test cases for different input types
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("23") == "23"
    assert shorten("CS50") == "CS50"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten(",._,-") == ",._,-"

if __name__ == " __main__":
    #Executes the main function only when the script is run directly.
    # This ensures that the main function is only executed when the script is run directly (not when imported as a module). This is a common practice in Python to isolate functionality.
    main()




