class employee:
    # constructor
    # This is dunder method
    # This method is called automatically when an object of the class is created 
    def __init__(self, name, salary, role): 
        self.name = name
        self.salary = salary
        self.role = role
        print("Employee created successfully")

    def show(self):
        return f"Name: {self.name}, Salary: {self.salary}, Role: {self.role}"
    
emp1 = employee("Siddh", 100000, "Developer")

# I have not called show method yet but the constructor has already executed and printed the message ("Employee created successfully")
