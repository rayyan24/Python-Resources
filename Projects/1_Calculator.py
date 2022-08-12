import os
def add(a, b):
    print(f"{a}+{b}={a+b}\n")

def subtract(a, b):
    print(f"{a}-{b}={a-b}\n")

def multiply(a, b):
    print(f"{a} x {b}={a*b}\n")

def divide(a, b):
    print(f"{a} / {b}={a/b}\n")


while(1):
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for Exit")
    n = int(input())
    if(n == 1):
        os.system("cls")
        print("Enter First Number")
        a = int(input())
        print("Enter Second Number")
        b = int(input())
        add(a, b)
    if(n == 2):
        os.system("cls")
        print("Enter First Number")
        a = int(input())
        print("Enter Second Number")
        b = int(input())
        subtract(a, b)
    if(n == 3):
        os.system("cls")
        print("Enter First Number")
        a = int(input())
        print("Enter Second Number")
        b = int(input())
        multiply(a, b)
    if(n == 4):
        os.system("cls")
        print("Enter First Number")
        a = int(input())
        print("Enter Second Number")
        b = int(input())
        divide(a, b)
    if(n == 5):
        break
print("Thank You")
