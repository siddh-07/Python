class student:
    name = ""
    age = 0
    marks = 0
    
    # Method to set values
    def setvalues(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        
    # Method to print values
    def printvalues(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

# Creating an object of the class student
siddh = student()

# Setting values using the setvalues method
siddh.setvalues("Siddharth", 21, 95)

# Printing values using the printvalues method
siddh.printvalues()