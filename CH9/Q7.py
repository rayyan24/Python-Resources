content=True
i=1
with open("log.txt") as f:
        while content :
            content=f.readline()
            if "python" in content.lower() :
                print(f"python is present in line {i}")
            i=i+1
asass