with open("new.txt") as p:
    a=p.read()

    if "twinkle" in a:
        print("Twinkle found")
    else:
        print("twinkle is not found")
        
        