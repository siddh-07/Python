age = int(input("Enter your age: "))

# if - elif - else ladder
if (age < 0):
    print("Invalid age. Age cannot be negative.")       
elif (age < 13):
    print("You are a child.")
elif (age < 20):
    print("You are a teenager.")    
elif (age < 65):  
    print("You are an adult.")
else:
    print("You are a senior citizen.")

            