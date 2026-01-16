# This script demonstrates how to take user input in Python

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "! You are " + age + " years old.")

a = input("Enter a number: ")
b = input("Enter another number: ")

print("\nBefore Conversion:")
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Concatenated Result (a + b):", a + b) # Concatenation of strings
a = float(a)
b = float(b)
print("\nAfter Conversion to float:")
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Sum Result (a + b):", a + b) # Numerical addition