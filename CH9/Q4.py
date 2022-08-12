with open("text.txt","r") as b:
    content=b.read()
content=content.replace("donkey","******")
with open("text.txt","w") as b:
    b.write(content)

