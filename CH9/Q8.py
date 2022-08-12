with open("log.txt",) as f:
    a=f.read()
with open("copied.txt","w") as b:
    b.write(a)