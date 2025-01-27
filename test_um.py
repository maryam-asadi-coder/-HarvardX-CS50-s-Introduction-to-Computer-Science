
#Imports the pytest library, which is a popular Python testing framework used for writing and running tests.
import pytest
#Imports a function named count from a module called um. This function presumably counts the occurrences of the word "um" within a given text.
from um import count
#Defines a function named main. This function calls another function named test1.
def main():
    test1()
#Defines a function named test1. This function contains a test case.
#The assert statement checks if the result of calling count("um") is equal to 1. If it is, the test passes. If not, the test fails. This test verifies if the function correctly counts one occurrence of "um" in the text "um".

# assert count("um?") == 1------Another test case. Checks if the function correctly counts one occurrence of "um" in the text "um?".
def test1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
#Another test case. Checks if the function correctly counts one occurrence of "um" (case-insensitive) in the text "Um, thanks for the album".
#Another test case. Checks if the function correctly counts two occurrences of "um" (case-insensitive) in the text "Um, thanks, um...".
