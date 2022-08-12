a=input("Enter a number\n")
b=False
try:
    a=int(a)
    c=a+1
    print(c)
except Exception as e:
    print("Error occoured")
    b=True
finally: # finally will be executed irrespective of the above code 
    print("Executed")
if b==True:
    print("code executed but with an error")
else:
    print("code executed without an error")
        