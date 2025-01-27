#The code you provided calculates the energy (E) using the famous equation E = mc²
# e = m * c * c
#E is the energy (in joules)
#m is the mass (in kilograms)
#c is the speed of light (in meters per second)
#The speed of light is a constant value of approximately 3 x 10^8 meters per second (often denoted by c). In your code, it's set to 300,000,000 meters per second.
# This line prompts the user to enter a value for the mass and stores it as an integer in the variable m.
m = int(input("mass: "))
#This line assigns the value of 300,000,000 (which is an approximation of the speed of light) to the variable c.
c = 300000000
#e = m * c * c: This line calculates the energy (E) by multiplying the mass (m) by the speed of light squared (c * c).
e = m * c * c
#This line prints the calculated energy value (e) to the console.
print(e)
#he equation E=mc² demonstrates that mass and energy are interchangeable. This principle is at the heart of nuclear reactions and nuclear bombs.
