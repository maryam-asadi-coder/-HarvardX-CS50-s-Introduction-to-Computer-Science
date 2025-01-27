from jar import Jar
#Imports the Jar class from the jar module. This means that the code can now use the Jar class to create and manipulate jar objects.
#Defines a function named test_init.
#Creates a new Jar object without any arguments.
#Asserts that the capacity of the created jar is 12, which is the default capacity.
#Creates another Jar object with a capacity of 1.
#Asserts that the capacity of the second jar is indeed 1.
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar1 = Jar(1)
    assert jar1.capacity == 1
#Defines a function named test_str.  
#Creates a new Jar object.
#Asserts that the string representation of the empty jar is an empty string.
#Deposits 1 cookie into the jar.
#Asserts that the string representation of the jar now shows a single cookie.
#Deposits 11 more cookies into the jar.
#Asserts that the string representation of the jar now shows 12 cookies.
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
#Defines a function named test_deposit.
#Creates a new Jar object.
#Deposits 5 cookies into the jar.
#Asserts that the size of the jar is now 5.
#Deposits another 5 cookies into the jar.
#Asserts that the size of the jar is now 10.
def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10
#Defines a function named test_withdraw.
#Creates a new Jar object.
#Deposits 10 cookies into the jar.
#Withdraws 5 cookies from the jar.
#Asserts that the size of the jar is now 5.
#Withdraws another 5 cookies from the jar.
Asserts that the size of the jar is now 0.

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0
#Overall Purpose:

#This code tests the functionality of the Jar class. It ensures that the Jar class behaves as expected when creating jars, depositing cookies, and withdrawing cookies.
#The assert statements verify that the methods are working correctly by comparing the actual results to the expected ones.
