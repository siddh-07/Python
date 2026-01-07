# Write a code which takes 8 numbers as input from user and print only unique numbers as output.
n = 8 
set1 = set()

for i in range(n):
    number = int(input("Enter number: "))
    set1.add(number)
    
print("Unique numbers are:", set1)
    
# Write a code to store number 18 as an int and as a string in a set and see the length of set.

set2 = set()   
set2.add(18)
set2.add(18.0) # Adding float type of 18
set2.add("18")

print(set2) # Output: {18, '18'} because they are different types but 18 and 18.0 are considered the same in a set 
print("Length of set is:", len(set2))
    