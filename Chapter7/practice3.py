# Patterns with nested loops in for loops

num = int(input("Enter the number of rows: "))

print("Right-angled triangle pattern:")
for i in range(num):
    for j in range(i+1):
        print(f"*", end=" ")
    print() 


print("\nHollow square pattern:")
for i in range(num):
    for j in range(num):
        if j == 0 or j == num - 1 or i == 0 or i == num - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  # Move to the next line after inner loop    
    
print("\nSolid square pattern:")
for i in range(num):
    for j in range(num):
        print("*", end=" ")
    print()  # Move to the next line after inner loop

print("\nTringle Pattern:")
for i in range(1,num+1):
    print(" " * (num-i),end="")
    print("*"* (2*i-1), end="")
    print("\n")   