class Employee:
    
    name = "Siddh"
    
    @classmethod
    def show(cls):
        print(f"The class attribute of name is {cls.name}.")
        
        
emp = Employee()
emp.name = "John" # Instance attribute
emp.show()  # Output: The class attribute of name is Siddh. because class method uses class attribute not instance attribute