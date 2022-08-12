class programmer:
    company="microsoft"
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language
    def getInfo(self):
        print(f"The name and age of programmer is {self.name} and {self.age} and he prefers {self.language} language")
a=programmer("Rayyan",19,"Python")
a.getInfo()
b=a.company
print(b)
programmer.company="Google"
b=a.company
print(b)
