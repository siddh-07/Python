# Parent class
class Employee: 
    
    company = "Google"
    
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        return f"{self.name} is working as a {self.position} in {self.company}."
    
# Child class or derived class 
# It inherits properties and methods from Employee class
class Manager(Employee): # Inherits from Employee class
    
    def __init__(self, name, position, team_size):
        super().__init__(name, position)
        self.team_size = team_size

    def manage(self):
        return f"{self.name} is managing a team of {self.team_size} members."
    
class Intern(Employee): # Inherits from Employee class
    
    def __init__(self, name, position, duration):
        super().__init__(name, position)
        self.duration = duration

    def learn(self):
        return f"{self.name} is an intern for {self.duration} months."
    
    
employee = Employee("Siddh", "Software Engineer")
manager = Manager("Sid", "Project Manager", 10)
intern = Intern("Sam", "Intern", 6)

print(employee.work())
print(manager.work())
print(manager.manage())
print(intern.work())
print(intern.learn())


    
    
