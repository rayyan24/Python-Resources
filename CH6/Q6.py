marks=int(input('Enter your marks\n'))
if marks>100:
    print("Invalid Input" )
elif marks<0:
    print("Invalid Input" )
elif marks>=90:
    print("Grade Ex" )
elif marks>=80:
    print("Grade A" )
elif marks>=70:
    print("Grade B" )
elif marks>=60:
    print("Grade C" )
elif marks<=50:
    print("Grade F" )

