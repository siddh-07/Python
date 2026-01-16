# Recursion Example
'''

This function calculates the factorial of a number using recursion.

facotial(5) = 5 * 4 * 3 * 2 * 1 = 120
factorial(5) = 5 * factorial(4) or 5 * factorial(5-1)
factorial(n) = n * factorial(n-1)

'''

def factorial(n):
    # Base Case
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a number to find factorial: "))
print(f"The factorial of {num} is {factorial(num)}")