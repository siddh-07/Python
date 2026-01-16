# Write a Python function to print the following pattern
def pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end="")
        print()
        
pattern(5)

# Write a Python function to convert inches to centimeters
def inches_to_cm(inches):
    return inches * 2.54