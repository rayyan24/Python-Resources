usr_name=input('Enter your user name\n')
a=len(usr_name)
if a>=10:
    print('the user name has 10 characters')
elif a>10:
    print('the user name has more than 10 characters')
else:
    print("the user name has less than 10 characters")