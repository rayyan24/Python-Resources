a=input("Enter a number: ")
try:
    a=int(a)
    c=1/a
    print(c)
except ValueError as e:
    print("exception1 occoured")
    print("ValueError has occoured")
except ZeroDivisionError as e:
    print("exception2 occoured")
    print("ZeroDivisionError has occoured")
















