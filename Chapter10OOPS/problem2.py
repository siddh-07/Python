class Calculator: 
    
    def __init__(self, number):
        self.number = number
        
    @staticmethod
    def greet():
        print("Welcome to the Calculator!")
        
    def squre(self):
        return self.number ** 2
    
    def cube(self):
        return self.number ** 3
    
    def square_root(self):
        return self.number ** 0.5
    
calc = Calculator(9)
calc.greet()
print("Square:", calc.squre())
print("Cube:", calc.cube())
print("Square Root:", calc.square_root())

# Output:
# Square: 81
# Cube: 729
# Square Root: 3.0
        