

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))



num = 7


# num = int(input("Enter a number: "))


result = factorial(num)
print("The factorial of", num, "is", result)