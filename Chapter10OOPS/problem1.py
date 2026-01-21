
class programmer:
    
    company = "Microsoft"  # class variable
    
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def code(self):
        return f"{self.name} is working in {self.company}. He/She codes in {self.language} language."
    
prog1 = programmer("Siddh", "Python")
print(prog1.code())
    