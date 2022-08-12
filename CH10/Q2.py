class calculator:
    def __init__(self,num):
        self.num=num
    @staticmethod
    def greet():
        print("Hello")
    def square(self):
        print(self.num**2)
    def squareroot(self):
        print(self.num**0.5)
    def cube(self):
        print(self.num**3)
number=calculator(9)
number.greet()
number.square()
number.squareroot()
number.cube()

