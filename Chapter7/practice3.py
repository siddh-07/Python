# Patterns with nested loops in for loops

num = int(input("Enter the number of rows: "))

# Print right-angled triangle pattern
for i in range(num):
    for j in range(i+1):
        print("*", end=" ")
    print() 

# Print hollow square pattern
for i in range(num):
    for j in range(num):
        if j == 0 or j == num - 1 or i == 0 or i == num - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  # Move to the next line after inner loop    

   