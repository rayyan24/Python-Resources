with open("log.txt") as f1:
    a=f1.read()
with open("copied.txt") as f2:
    b=f2.read()
if a==b:
    print(f"files are identical")
else:
    print(f"files are not identical")
