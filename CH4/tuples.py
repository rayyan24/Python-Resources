normal_tuple=(1,2,3,4,5)
empt_tuple=()
tuple_with_one_elemement=(1,)
print(normal_tuple)
print(empt_tuple)
print(tuple_with_one_elemement)
# print(normal_tuple(0)) ==> wrong method
print(normal_tuple[0])
a=normal_tuple.count(5) # tells how many times the given element occours
b=normal_tuple.index(1) #tells the first index of the given element
# insted of creating a variable direct print statement can also be used
print(a)
print(b)



