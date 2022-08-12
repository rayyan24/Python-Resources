while(True):
    a=input("Enter a number\n")
    if a=="q":
        break
    try:
        a=int(a)
        print(f"The incremented number is {a+1}")
    except Exception as e:
        print("Please give a valid input")
    print("Program Executed")















