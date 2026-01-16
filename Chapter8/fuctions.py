# Function Defination

def avg():
    a = int(input("Enter Number: "))
    b = int(input("Enter Number: "))
    c = int(input("Enter Number: "))
    
    print(f"Avarage of given numbers is {(a+b+c)/3}")
    
# Function Call
avg()

#Function with arguments
def good(name, rollNumber):
    print("My name is " + name + "My RollNumber is " + rollNumber)
    print("Have a good day " + name)
    
    
good("Siddh" , "26")
good("Nency" , "25")