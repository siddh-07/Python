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

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input from user
celsius_temp = float(input("\nEnter temperature in Celsius: "))
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

def sumOfNaturalNumbers(n):
    """Return the sum of first n natural numbers."""
    if n == 0:
        return 0
    elif n < 1:
        return "Invalid Input"
    else:
        return n + sumOfNaturalNumbers(n - 1)
    
# Input from user
num = int(input("\nEnter a positive integer: "))
sum_natural = sumOfNaturalNumbers(num)
print(f"The sum of the first {num} natural numbers is {sum_natural}")
