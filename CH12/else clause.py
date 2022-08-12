a=input("Enter a number\n")
try:
    a=int(a)
    c=a+1
    print(c)
except Exception as e:
    print("Error occoured")
else: # else will only be executed  if the program execution was successfull
    print("Code executed without an error")
