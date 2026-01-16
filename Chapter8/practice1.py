def greatest(a, b, c):
    """Return the greatest of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
    
# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
greatest_number = greatest(num1, num2, num3)
print(f"The greatest number among {num1}, {num2}, and {num3} is {greatest_number}")

