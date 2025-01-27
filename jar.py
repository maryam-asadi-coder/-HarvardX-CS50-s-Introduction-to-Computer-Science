
#Defines a new class named Jar. This class will represent a jar or container that can hold items (in this case, cookies).
class Jar:
    #This is the constructor method that initializes a new Jar object.
#It takes an optional argument capacity which defaults to 12. This sets the maximum number of items the jar can hold.
#If the provided capacity is greater than 0, it sets the _capacity attribute to the given value and initializes the _size attribute to 0 (meaning the jar is initially empty).
#If the capacity is less than or equal to 0, it raises a ValueError with the message "Wrong capacity" to indicate that the capacity must be positive.
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError("Wrong capacity")
#This method defines how a Jar object should be represented as a string.
#It returns a string consisting of self.size number of cookie emojis ('🍪'). This provides a visual representation of the number of cookies in the jar.
    def __str__(self):
        return self.size * '🍪'
#This method is used to add cookies to the jar.
#It takes an integer n representing the number of cookies to add.
#If the number of cookies to add (n) is greater than the jar's capacity or would exceed the jar's capacity, it raises a ValueError with the message "Over capacity".
#Otherwise, it increments the _size attribute by n to add the cookies to the jar.
    def deposit(self, n):
        if n > self.capacity or (self.size + n) > self.capacity:
            raise ValueError("Over capacity")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self._size -= n
    @property #This defines a property named capacity that provides read-only access to the jar's capacity.
#When you access jar.capacity, it returns the value of the _capacity attribute.
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
