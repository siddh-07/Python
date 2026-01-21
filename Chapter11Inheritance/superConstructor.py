# Parent class
class Employee: 
    
    company = "Google"
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        print("Employee Constructor Called")

    def work(self):
        return f"{self.name} is working as a {self.position} in {self.company}."
    
# Child class or derived class
class Programmer(Employee): # Inherits from Employee class
    
    def __init__(self, name, position, duration):
        super().__init__(name, position) # Call the constructor of the parent class by using super()
        self.duration = duration
        print("Programmer Constructor Called")

    def learn(self):
        return f"{self.name} is an programmer for {self.duration} months."
    
# Child class or derived class
class Manager(Programmer): # Inherits from Employee class
    
    def __init__(self, name, position, team_size , duration): 
        super().__init__(name, position, duration) # Call the constructor of the parent class by using super() but here it calls Programmer's constructor
        self.team_size = team_size
        print("Manager Constructor Called")

    def manage(self):
        return f"{self.name} is managing a team of {self.team_size} members."
    
# This calls Employee class constructor
employee = Employee("Siddh", "Software Engineer")

# This calls Programmer class constructor and Employee class constructor
programmer = Programmer("Sid", "Programmer", 12)

# This calls Manager class constructor, Programmer class constructor and Employee class constructor 
manager = Manager("Sam", "Project Manager", 10, 6)