# Example of for loops
# Range (start, stop - 1, step to skip)
for i in range(0, 101, 5):
    print(i)
    
# for loop with else
for i in range(5):
    print(i)
else:
    print("Loop is ended") # will be executed after the loop is ended
    
# break statement
print("Break statement example:")
for i in range(10):
    if i == 5:
        break # will exit the loop when i is 5 
    print(i)
    
# continue statement
print("Continue statement example:")
for i in range(10):
    if i == 5:
        continue # will skip the iteration when i is 5
    print(i)
    
# pass statement
print("Pass statement example:")
for i in range(10):
    if i == 5:
        pass # does nothing, just a placeholder
    print(i)
    