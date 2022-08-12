a=int(input("Enter the number: "))
b=[a*i1 for i1 in range(1,11) ]   
with open('table',"w") as c:
    for i in b:
        i=str(i)
        c.write(f"{i}\n")
