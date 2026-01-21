
class programmer:
    
    def __init__(self, name,company, language):
        self.name = name
        self.company = company
        self.language = language

    def code(self):
        return f"{self.name} is working in {self.company}. He/She codes in {self.language} language."
    
prog1 = programmer("Siddh", "Google", "Python")
print(prog1.code())
    