a=int(input("Enter a number\n"))
b=int(input("Enter another number\n"))
c=(input("Enter Operation"))
if a=="K":
    print("K")
elif a == 1 and b == 3 and c == "+":
    print("10")
elif a == 7 and b == 0 and c == "-":
    print("0")
elif a == 2 and b == 3 and c == "*":
    print("100")
elif a == 1 and b == 0 and c == "/":
    print("45")
elif c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)