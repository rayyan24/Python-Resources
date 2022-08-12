# Creating an empty dictionary 
a={}
# Creating an empty set 
a=set()
b={1,23,3,4,45}
# print(b)
# methods of sets 
a.add(1)
# a.add({1:'one'}) # dictionary cannot be added in a set
a.add((1,2,3,4))
print(len(b)) # tells how many items are there in a set
# b.remove(3)
# b.remove(12) # this will thow a error as 12 is not in the set
print(b.pop()) #randomly removees a element from set
print(b.pop())
b.clear()
print(b)





