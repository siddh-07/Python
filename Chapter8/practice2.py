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

inch = int(input("Enter inches: "))
print(f"{inch} inches is equal to {inches_to_cm(inch)} centimeters.")

# Remove word and strip from a list
def removeWord(list,word): 
    n = []
    for i in list:
        if not(word == i):
            n.append(i.strip(word))
    return n

l = ["  apple  "," banana ","  cherry "," date " , " na "]

print(removeWord(l," "))
