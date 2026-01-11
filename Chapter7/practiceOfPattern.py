# Example of Patterns

num = 5

# Inverted Trinagle Pattern
print("Inverted Trinagle Pattern:")
for i in range(num, 0,-1):
    print("*" * i)
    
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("\nPrint numbers in triangle:")
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="") 
    print()       
    
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1    
print("\nReverse number triangle:")
for i in range(num+1,1,-1):
    for j in range(1,i):
        print(j,end="") 
    print()
    
print("Floyd’s Triangle:")
n = 1   
for i in range(1,num+1):
    for j in range(1,i+1):
        print(f"{n} ",end="")
        n += 1
    print()  