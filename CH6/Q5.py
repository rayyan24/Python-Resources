a=input("enter what you want to find in list\n")
list0=['A','B','C','D','E']
flag=0
for i in range(0,len(list0)):
    if(a==list0[i]):
        flag=1
        break
if(flag==0):
    print("Element is not found")    
else:
    print(f"Element found at {i+1}")




# if a in list0:
    # print(a,"is present in list")
# else:
    # print(a,"is not present in list")