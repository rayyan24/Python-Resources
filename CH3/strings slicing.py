#  Concaatinating Two Strings
greet='Hello'
name= " Rayyan"
result=greet + name
print(result)
print(result[0])
print(result[1])
# result[0]="B" #--> Not possible throw error
a=result[0:5] # string slicing - taing a specific part of a string. In this statement 0 is included and 5 is excluded  
print(a)
b=greet[:5] # is same as [0:5]
c=greet[0:] # is same as [0:5] 
print(b)
print(c)
d=greet[::-1] # gives the last character of string if -2 is written gives seceond last character of sting 
e=greet[::2] # if 2 is written in third place it skips 1 if three is written t skips 2 if 1 is written it skips 0 and so on
print(d)
print(e)







