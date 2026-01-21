class Animals:
    
    def __init__(self):
        print("The animal makes a sound")
    
class Pet(Animals):
    
    def __init__(self):
        print("The pet barks")
    
class Dog(Pet):
        
    def bark(self):
        return "The dog barks loudly"
        
        
dog = Dog()
print(dog.bark())

# Output:
# The pet barks because of method overriding
# The dog barks loudly   