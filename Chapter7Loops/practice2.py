# Write a program with while loop that calculates the factorial of a given positive integer.
num = int(input("Enter a positive integer: "))
factorial = 1
i = 1
while (i <= num):
    factorial *= i
    i += 1
    
print(f"The factorial of {num} is {factorial}")


# Write a program with while loop that calculates the sum of a given positive integer.
num = int(input("Enter a positive integer: "))

sum = 0
i = 1
while (i <= num):
    sum += i
    i += 1
    
print(f"The sum of {num} is {sum}")