
import random
def game(comp,user):
    if comp==user:
        return None
    elif comp=="s":
        if user=="w":
            return False
        if user=="g":
            return True
    elif comp=="w":
        if user=="s":
            return True
        if user=="g":
            return False
    elif comp=="g":
        if user=="w":
            return True
        if user=="s":
            return False
print("Comp:Chose Snake(s),Water(w) or Gun(g)")
b=random.randint(1,3)
if b==1:
    comp='s'
elif b==2:
    comp="w"
elif b==3:
    comp="g"
user=(input("User:Chose Snake(s),Water(w) or Gun(g) "))

a=game(comp,user)
print("You chose",user)
print("Computer chose",comp)
if a== None:
    print("Tie")
elif a==True:
    print("You Won")
elif a==False:
    print("You lose")

        



    





