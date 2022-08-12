start=int(input("Enter start of tables: "))
end=int(input("Enter end of tables: "))
for j in range(start,end+1):
    n=f"Table of {j}"
    with open(n,"w") as file1:
        i=1
        while(i<=10):
            file1.write(f"{j} x {i} = {j*i}\n")
            i+=1