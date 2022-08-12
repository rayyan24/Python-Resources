mark1=int(input("Enter English Marks\n"))
mark2=int(input("Enter Maths Marks\n"))
mark3=int(input("Enter Science Marks\n"))
if mark1<33:
    print('you are not pass in english')
if mark2<33:
    print('you are not pass in maths')
if mark3<33:
    print('you are not pass in science')

if mark1<33 or mark2<33 or mark3<33:
    print("You are not pass ")
else:
    total=mark1+mark2+mark3
    if total==40:
        print("pass")
    if total<40:
        print("not pass")
    if total>40:
        print("pass")
print("you total marks are",total)



