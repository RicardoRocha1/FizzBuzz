# Very simple FizzBuzz solution, not recommended if other possible outputs are required
# x is the starting point, modifying it changes where the printing begins (negative numbers are acceptable)
x = 1
# Defines up to what number will be verified and it's outcome printed
while x <= 100:
    if x % 3 == 0 and x % 5 !=0:
        print("Fizz")
    if x % 5 == 0 and x % 3 !=0:
        print("Buzz")
    if x % 15 == 0:
        print("FizzBuzz")
    if x % 3 != 0 and x % 5 != 0:
        print(x)
    # If x is not incremented in this while loop, it will continue printing it's initial value result forever
    x = x + 1
    # When this loop has run enough times that x is equal to the value defined as the condition for the loop, it will break