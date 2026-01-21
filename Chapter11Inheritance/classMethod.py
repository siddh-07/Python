class Employee:
    
    company_name = "Google"
    
    @classmethod
    def show(cls):
        print(f"The class attribute of name is {cls.company_name}.")
        
    @property
    def display(self):
        print(f"The first name is {self.fname} and last name is {self.lname}.")
        
    @display.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
        
emp = Employee()
emp.company_name = "Microsoft" # Instance attribute
emp.show()  # Output: The class attribute of name is Google. because class method uses class attribute not instance attribute

emp.name = "Siddh Bhadani"
emp.display  # Output: The first name is Siddh and last name is Bhadani. because property uses instance attribute