# a=open("info.txt","w") # when w is used all the existing items in the file are removed
# a.write("Hello")
# a.write(" Good Morning")
# a.close()
# b=open("info.txt","a") # while using a the existing data is not deleted
# b.write(" Hello1")
# b.write(" Good Morning1")
# b.close()
with open("info.txt","r") as i: #with statement automatically closes the file
    a=i.read()
    print(a)
                                            