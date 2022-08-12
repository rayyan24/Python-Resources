words =["kutta","gadha","jaanwar","donkey"]
with open("text0.txt","r") as b:
    content=b.read()
for word in words:
    content=content.replace(word,"******")
    with open("text0.txt","w") as b:
        b.write(content)
        
