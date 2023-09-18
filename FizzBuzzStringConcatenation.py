for x in range(1,101):
    outut = ""
    if x % 3 == 0:
        output = output + "Fizz"
    if x % 5 == 0:
        output = output + "Buzz"
    if x % 5 != 0 and x % 3 != 0:
        output = x
    print(output)
    output = ""